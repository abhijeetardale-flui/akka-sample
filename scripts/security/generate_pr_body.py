import json
import os
from pathlib import Path


def load_json(path: Path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    severity = os.environ.get("TARGET_SEVERITY", "CRITICAL")

    pr_fixes = Path("pr-fixes")
    issues = load_json(pr_fixes / "issues.json")
    fixes = load_json(pr_fixes / "fixes.json")

    sca_issues = [item for item in issues if item.get("type") == "SCA"]
    sast_issues = [item for item in issues if item.get("type") == "SAST"]

    lines = []
    lines.append(f"# 🔒 Automated Security Fixes – {severity} Severity")
    lines.append("")
    lines.append(
        f"This PR addresses **{len(issues)} {severity} severity security findings** detected by the comprehensive security scan."
    )
    lines.append("")

    lines.append("## 📊 Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Total Findings | {len(issues)} |")
    lines.append(f"| SCA (Dependencies) | {len(sca_issues)} |")
    lines.append(f"| SAST (Code) | {len(sast_issues)} |")
    lines.append(f"| Auto-fixable dependencies | {len(fixes)} |")
    lines.append("")

    if sca_issues:
        lines.append("## 📦 Dependency Vulnerabilities")
        for item in sca_issues:
            lines.append(f"### {item['cve']} – {item['title']}")
            lines.append(f"- Package: `{item['package']}`")
            lines.append(f"- Current version: `{item['current_version']}`")
            lines.append(f"- Fixed version: `{item['fixed_version'] or 'Manual review required'}`")
            candidates = item.get("candidate_versions") or []
            if candidates:
                lines.append(f"- Recommended secure versions: {', '.join(candidates)}")
            lines.append(f"- Description: {item['description']}")
            lines.append("")

    if sast_issues:
        lines.append("## 🔍 Code Findings (Manual review required)")
        for item in sast_issues:
            lines.append(f"### {item['cve']} – {item['title']}")
            lines.append(f"- Location: `{item['file']}:{item['line']}`")
            lines.append(f"- Description: {item['description']}")
            lines.append("")

    if fixes:
        lines.append("## ✅ Dependency Updates Applied")
        for fix in fixes:
            lines.append(
                f"- `{fix['package']}`: `{fix['from_version']}` → `{fix['to_version']}` ({fix['cve']})"
            )
        lines.append("")
    else:
        lines.append("## ⚠️ Manual Action Required")
        lines.append(
            "No automatic dependency updates were available. Please review the findings above and apply manual code changes where necessary."
        )
        lines.append("")

    lines.append("## 🧪 Testing Checklist")
    lines.append("- [ ] Build succeeds")
    lines.append("- [ ] Unit tests pass")
    lines.append("- [ ] Integration tests pass")
    lines.append("- [ ] Security regression review complete")
    lines.append("")

    lines.append("---")
    lines.append("*Generated automatically by the Security Fix Pull Requests by Severity workflow.*")

    pr_fixes.mkdir(parents=True, exist_ok=True)
    (pr_fixes / "pr-body.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
