import json
import os
import re
from datetime import datetime
from pathlib import Path


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"⚠️ Missing file: {path}")
    except json.JSONDecodeError as exc:
        print(f"⚠️ Could not decode {path}: {exc}")
    return {}


def version_key(version: str):
    numbers = [int(part) for part in re.findall(r"\d+", version or "")]
    return tuple(numbers) if numbers else (0,)


def extract_prefix(version: str):
    if not version:
        return None
    match = re.match(r"^(\d+)(?:\.(\d+))?", version)
    if not match:
        return None
    major = match.group(1)
    minor = match.group(2)
    return f"{major}.{minor}" if minor is not None else major


def normalize_candidates(raw: str):
    normalized = (raw or "").replace(";", ",").replace("/", ",")
    candidates = [cand.strip() for cand in normalized.split(",") if cand.strip()]
    seen = set()
    unique = []
    for cand in candidates:
        if cand not in seen:
            seen.add(cand)
            unique.append(cand)
    return unique


def matches_prefix(candidate: str, prefix: str):
    if not prefix:
        return False
    return (
        candidate.startswith(f"{prefix}.")
        or candidate == prefix
        or candidate.startswith(f"{prefix}-")
    )


def choose_fixed_version(current_version: str, candidates):
    if not candidates:
        return None
    prefix = extract_prefix(current_version)
    same_prefix = [cand for cand in candidates if matches_prefix(cand, prefix)]
    selectable = same_prefix if same_prefix else candidates
    return max(selectable, key=version_key)


def better_version(current_version: str, existing_version: str, new_version: str):
    prefix = extract_prefix(current_version)

    def preference(value: str):
        matches = 1 if matches_prefix(value, prefix) else 0
        return (matches, version_key(value))

    return max([existing_version, new_version], key=preference)


def main():
    target_severity = os.environ.get("TARGET_SEVERITY", "CRITICAL")

    scan_dir = Path("security-scan-data")
    trivy_data = load_json(scan_dir / "trivy-results.json")
    semgrep_data = load_json(scan_dir / "semgrep-results.json")

    issues = []
    fix_map = {}
    sca_count = 0
    sast_count = 0

    if isinstance(trivy_data, dict) and "Results" in trivy_data:
        for result in trivy_data.get("Results", []):
            for vuln in result.get("Vulnerabilities", []):
                severity = vuln.get("Severity", "UNKNOWN")
                if severity != target_severity:
                    continue
                sca_count += 1

                package = vuln.get("PkgName", "Unknown")
                current_version = vuln.get("InstalledVersion", "Unknown")
                candidates = normalize_candidates(vuln.get("FixedVersion", ""))
                chosen_version = choose_fixed_version(current_version, candidates)

                entry = {
                    "source": "Trivy",
                    "type": "SCA",
                    "severity": severity,
                    "cve": vuln.get("VulnerabilityID", "N/A"),
                    "package": package,
                    "current_version": current_version,
                    "fixed_version": chosen_version or "",
                    "candidate_versions": candidates,
                    "title": vuln.get("Title", "No title"),
                    "description": (vuln.get("Description") or "No description")[:400],
                    "cvss": vuln.get("CVSS", {}).get("nvd", {}).get("V3Score"),
                    "references": vuln.get("References", []),
                }
                issues.append(entry)

                if not chosen_version or chosen_version == current_version:
                    continue

                fix_entry = fix_map.get(package)
                if fix_entry:
                    best_version = better_version(
                        current_version, fix_entry["to_version"], chosen_version
                    )
                    if best_version != fix_entry["to_version"]:
                        fix_entry["to_version"] = best_version
                    fix_entry["cves"].add(entry["cve"])
                    fix_entry["candidates"].update(candidates)
                else:
                    fix_map[package] = {
                        "package": package,
                        "from_version": current_version,
                        "to_version": chosen_version,
                        "severity": severity,
                        "cves": {entry["cve"]},
                        "candidates": set(candidates),
                    }

    severity_map = {"ERROR": "HIGH", "WARNING": "MEDIUM", "INFO": "LOW"}

    if isinstance(semgrep_data, dict) and "results" in semgrep_data:
        for finding in semgrep_data.get("results", []):
            raw_severity = finding.get("extra", {}).get("severity", "INFO")
            mapped_severity = severity_map.get(raw_severity, "LOW")
            if mapped_severity != target_severity:
                continue
            sast_count += 1
            entry = {
                "source": "Semgrep",
                "type": "SAST",
                "severity": mapped_severity,
                "cve": finding.get("check_id", "N/A"),
                "file": finding.get("path", "Unknown"),
                "line": finding.get("start", {}).get("line"),
                "title": finding.get("extra", {}).get("message", "Security issue detected")[:160],
                "description": finding.get("extra", {}).get("metadata", {}).get("description", "No description")[:400],
                "references": finding.get("extra", {}).get("metadata", {}).get("references", []),
            }
            issues.append(entry)

    issues.sort(key=lambda item: item.get("cve", ""))

    fixes = []
    for data in fix_map.values():
        fixes.append({
            "package": data["package"],
            "from_version": data["from_version"],
            "to_version": data["to_version"],
            "cve": ", ".join(sorted(data["cves"])),
            "severity": data["severity"],
            "candidate_versions": sorted(data["candidates"]) if data["candidates"] else [],
        })

    pr_fixes = Path("pr-fixes")
    reports_auto = Path("security-reports/auto")
    pr_fixes.mkdir(parents=True, exist_ok=True)
    reports_auto.mkdir(parents=True, exist_ok=True)

    with (pr_fixes / "issues.json").open("w", encoding="utf-8") as handle:
        json.dump(issues, handle, indent=2)

    with (pr_fixes / "fixes.json").open("w", encoding="utf-8") as handle:
        json.dump(fixes, handle, indent=2)

    summary_lines = [
        f"# Security Findings – {target_severity}",
        f"Generated on {datetime.utcnow().isoformat()} UTC",
        "",
        f"- Total issues: {len(issues)}",
        f"- SCA issues: {sca_count}",
        f"- SAST issues: {sast_count}",
        f"- Auto-fixable dependencies: {len(fixes)}",
        "",
    ]

    if issues:
        summary_lines.append("## Detailed Findings")
        for idx, item in enumerate(issues, start=1):
            summary_lines.append(f"{idx}. **{item.get('cve', 'N/A')}** – {item.get('title')}")
            if item.get("type") == "SCA":
                summary_lines.append(f"   - Package: `{item.get('package')}`")
                summary_lines.append(
                    f"   - Version: `{item.get('current_version')}` → `{item.get('fixed_version') or 'Manual review'}`"
                )
                candidates = item.get("candidate_versions") or []
                if candidates:
                    summary_lines.append(f"   - Recommended versions: {', '.join(candidates)}")
            else:
                summary_lines.append(
                    f"   - Location: `{item.get('file')}:{item.get('line')}`"
                )
            summary_lines.append(f"   - Source: {item.get('source')} ({item.get('type')})")
            summary_lines.append("")
    else:
        summary_lines.append("No security issues detected for this severity.")

    summary_path = reports_auto / f"{target_severity.lower()}-security-summary.md"
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as handle:
            handle.write(f"issue_count={len(issues)}\n")
            handle.write(f"sca_count={sca_count}\n")
            handle.write(f"sast_count={sast_count}\n")
            handle.write(f"fixable_count={len(fixes)}\n")
            handle.write(f"has_issues={'true' if issues else 'false'}\n")


if __name__ == "__main__":
    main()
