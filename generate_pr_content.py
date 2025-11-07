import json

with open('pr-fixes/issues.json', 'r') as f:
    issues = json.load(f)

# Group by severity and type
critical = [i for i in issues if i['severity'] == 'CRITICAL']
high = [i for i in issues if i['severity'] == 'HIGH']
sca_issues = [i for i in issues if i['type'] == 'SCA']
sast_issues = [i for i in issues if i['type'] == 'SAST']

# Generate PR body
total = len(issues)
crit_count = len(critical)
high_count = len(high)
sca_count = len(sca_issues)
sast_count = len(sast_issues)

pr_body = "# 🔒 Automated Security Fixes: CRITICAL & HIGH Issues\n\n"
pr_body += "This PR automatically addresses **" + str(total) + " CRITICAL and HIGH severity security issues** "
pr_body += "detected by automated security scanning.\n\n"
pr_body += "## 📊 Issue Breakdown\n\n"
pr_body += "| Type | Count | Description |\n"
pr_body += "|------|-------|-------------|\n"
pr_body += "| 🔴 **CRITICAL** | " + str(crit_count) + " | Immediate action required |\n"
pr_body += "| 🟠 **HIGH** | " + str(high_count) + " | High priority fixes |\n"
pr_body += "| 📦 **SCA** (Dependencies) | " + str(sca_count) + " | Third-party library vulnerabilities |\n"
pr_body += "| 🔍 **SAST** (Code) | " + str(sast_count) + " | Code-level security issues |\n\n"
pr_body += "---\n\n"
pr_body += "## 🔴 CRITICAL Severity Issues\n\n"

if critical:
    for issue in critical:
        if issue['type'] == 'SCA':
            pr_body += "\n### " + issue['cve'] + ": " + issue['title'][:80] + "\n"
            pr_body += "- **Package:** `" + issue['package'] + "`\n"
            pr_body += "- **Current Version:** " + str(issue['current_version']) + "\n"
            pr_body += "- **Fixed Version:** " + str(issue['fixed_version']) + "\n"
            pr_body += "- **Type:** Software Composition Analysis (SCA)\n"
            pr_body += "- **Description:** " + str(issue['description']) + "\n"
            pr_body += "- **✅ Auto-fixed:** Updated to secure version\n\n"
        else:  # SAST
            pr_body += "\n### " + issue['cve'] + ": " + issue['title'][:80] + "\n"
            pr_body += "- **File:** `" + issue['file'] + "`\n"
            pr_body += "- **Line:** " + str(issue['line']) + "\n"
            pr_body += "- **Type:** Static Application Security Testing (SAST)\n"
            pr_body += "- **Description:** " + str(issue['description']) + "\n"
            pr_body += "- **⚠️ Manual review required** - Please review and apply suggested fix\n\n"
else:
    pr_body += "_No CRITICAL issues found._\n\n"

pr_body += "---\n\n"
pr_body += "## 🟠 HIGH Severity Issues\n\n"

if high:
    for issue in high:
        if issue['type'] == 'SCA':
            pr_body += "\n### " + issue['cve'] + ": " + issue['title'][:80] + "\n"
            pr_body += "- **Package:** `" + issue['package'] + "`\n"
            pr_body += "- **Current Version:** " + str(issue['current_version']) + "\n"
            pr_body += "- **Fixed Version:** " + str(issue['fixed_version']) + "\n"
            pr_body += "- **Type:** Software Composition Analysis (SCA)\n"
            pr_body += "- **Description:** " + str(issue['description']) + "\n"
            pr_body += "- **✅ Auto-fixed:** Updated to secure version\n\n"
        else:  # SAST
            pr_body += "\n### " + issue['cve'] + ": " + issue['title'][:80] + "\n"
            pr_body += "- **File:** `" + issue['file'] + "`\n"
            pr_body += "- **Line:** " + str(issue['line']) + "\n"
            pr_body += "- **Type:** Static Application Security Testing (SAST)\n"
            pr_body += "- **Description:** " + str(issue['description']) + "\n"
            pr_body += "- **⚠️ Manual review required** - Please review and apply suggested fix\n\n"
else:
    pr_body += "_No HIGH severity issues found._\n\n"

pr_body += "---\n\n"
pr_body += "## ✅ What Was Fixed Automatically\n\n"
pr_body += "This PR includes **automatic fixes** for:\n"
pr_body += "- ✅ **" + str(sca_count) + " SCA (dependency) vulnerabilities** - Updated to secure versions\n"
pr_body += "- ⚠️ **" + str(sast_count) + " SAST (code) issues** - Identified for manual review\n\n"
pr_body += "### Automatic Dependency Updates Applied:\n"

for issue in sca_issues:
    if issue.get('fixed_version') and issue['fixed_version'] != 'Not available':
        pr_body += "- `" + issue['package'] + "`: " + str(issue['current_version']) + " → " + str(issue['fixed_version']) + " (" + issue['cve'] + ")\n"

pr_body += "\n### Manual Code Review Required:\n"

if sast_issues:
    pr_body += "The following SAST issues require manual code changes:\n\n"
    for issue in sast_issues:
        pr_body += "- [ ] **" + issue['file'] + ":" + str(issue['line']) + "** - " + issue['title'][:60] + " (" + issue['cve'] + ")\n"
else:
    pr_body += "_No manual code changes required._\n"

pr_body += "\n---\n\n"
pr_body += "## 🧪 Testing\n\n"
pr_body += "Please verify:\n"
pr_body += "1. ✅ All builds pass\n"
pr_body += "2. ✅ Tests pass\n"
pr_body += "3. ✅ No regressions introduced\n"
pr_body += "4. ⚠️ Review SAST issues and apply fixes if needed\n\n"
pr_body += "---\n\n"
pr_body += "## 📚 Additional Information\n\n"
pr_body += "- **Scan Type:** SAST + SCA (Comprehensive)\n"
pr_body += "- **Severity Filter:** CRITICAL and HIGH only\n"
pr_body += "- **Auto-Generated:** Yes, by security automation workflow\n"
pr_body += "- **Triggered By:** workflow_dispatch\n\n"
pr_body += "---\n\n"
pr_body += "## 🎯 Next Steps\n\n"
pr_body += "1. **Review this PR** - Check all changes\n"
pr_body += "2. **Test thoroughly** - Ensure no breaking changes\n"
pr_body += "3. **Merge when ready** - Apply security fixes\n"
pr_body += "4. **Monitor** - Watch for any issues post-merge\n\n"
pr_body += "**This is an automated security PR. Please review carefully before merging.**\n\n"
pr_body += "---\n\n"
pr_body += "*Generated by: Auto PR for Critical & High Vulnerabilities workflow*\n"
pr_body += f"*Scan Date: 19153375413*\n"

# Save PR body
with open('pr-fixes/pr-body.md', 'w') as f:
    f.write(pr_body)

print("✅ PR content generated")
