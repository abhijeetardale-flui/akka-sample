import json
import os
from pathlib import Path


def append(lines):
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        print("⚠️ GITHUB_STEP_SUMMARY is not set. Skipping summary generation.")
        return
    with open(summary_path, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
        handle.write("\n")


def append_results():
    report_path = Path("security-reports/comprehensive-report.json")
    if not report_path.exists():
        append(["- No comprehensive report summary available", ""])
        return

    data = json.loads(report_path.read_text(encoding="utf-8"))
    lines = ["### 🎯 Results:"]
    lines.append(f"- **Total Vulnerabilities:** {data.get('total_vulnerabilities', 0)}")
    emoji_map = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🟢"}
    for severity, count in data.get("severity_breakdown", {}).items():
        emoji = emoji_map.get(severity, "⚪")
        lines.append(f"- **{severity}:** {emoji} {count}")
    lines.append("")
    append(lines)


def append_pr_links():
    links_raw = os.environ.get("PR_LINKS") or "{}"
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    base_url = f"https://github.com/{repo}" if repo else ""

    try:
        links = json.loads(links_raw)
    except json.JSONDecodeError:
        links = {}

    lines = ["### 🔗 Security Fix Pull Requests:"]
    severity_labels = [
        ("critical", "🔴 Critical"),
        ("high", "🟠 High"),
        ("medium", "🟡 Medium"),
    ]

    for key, label in severity_labels:
        entries = links.get(key, [])
        search_url = f"{base_url}/pulls?q=is:open+label:{key}+label:security" if base_url else ""
        if entries:
            lines.append(f"- {label}:")
            for entry in entries:
                title = (entry.get("title") or f"PR #{entry.get('number')}").strip()
                lines.append(f"  - [#{entry.get('number')} – {title}]({entry.get('url')})")
            if search_url:
                lines.append(f"  - [View all {label} PRs]({search_url})")
        else:
            if search_url:
                lines.append(
                    f"- {label}: _No open security PRs with '{key}' label found_. [Search]({search_url})"
                )
            else:
                lines.append(f"- {label}: _No open security PRs with '{key}' label found_")
    lines.append("")
    append(lines)


def main():
    header_lines = [
        "## 🔒 Comprehensive Security Scan Complete",
        "",
        "### 📊 Scan Coverage:",
        "- ✅ **SAST** (Static Application Security Testing) - Semgrep",
        "- ✅ **SCA** (Software Composition Analysis) - Trivy, OWASP",
        "- ✅ **Code Quality** - SpotBugs",
        "- ✅ **Secret Detection** - Trivy",
        "- ✅ **Config Scanning** - Trivy",
        "- ✅ **Code Scanning Uploads** - Trivy (SARIF), Semgrep (SARIF)",
        "",
    ]
    append(header_lines)

    append_results()
    append_pr_links()

    footer_lines = [
        "### 📥 Download Reports:",
        "1. Go to **Actions** tab → This workflow run",
        "2. Scroll to **Artifacts** section",
        "3. Download **security-reports.zip**",
        "",
        "### 📄 Available Reports:",
        "- 📊 **comprehensive-report.html** - Main Veracode-style report ⭐",
        "- 📊 **owasp/dependency-check-report.html** - OWASP full report",
        "- 📄 **comprehensive-report.json** - Machine-readable summary",
        "- 📄 **raw/trivy-table.txt** - Trivy scan results",
        "- 📄 **SARIF files** - GitHub Security tab integration",
        "",
        "---",
        f"*Scan completed at {os.popen('date -u').read().strip()}*",
    ]
    append(footer_lines)


if __name__ == "__main__":
    main()
