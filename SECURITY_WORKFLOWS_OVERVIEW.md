# 🔒 Security Workflows Overview

Quick reference for all automated security scanning and reporting in this repository.

---

## 🎯 Available Workflows

### 1. ♻️ Security Fix Pull Requests by Severity (NEW)
**File:** `.github/workflows/security-pr-by-severity.yml`

**What it does:**
- Runs a **single scan (Trivy + Semgrep)** and creates **separate PRs** for each severity: CRITICAL, HIGH, MEDIUM
- Auto-updates vulnerable dependencies when a fixed version is available
- Adds a Markdown summary (`security-reports/auto/<severity>-security-summary.md`) so every PR has context even when manual fixes are required
- Labels PRs with `security`, `automated-pr`, and the severity (`critical`, `high`, `medium`)

**When it runs:**
- ✅ Every Monday at 3 AM UTC
- ✅ Manual trigger available

**Quick Action:**
https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/security-pr-by-severity.yml

---

### 2. 🤖 Automated Third-Party Library Security Update
**File:** `.github/workflows/working-dependency-update.yml`

**What it does:**
- Scans Maven (pom.xml) and SBT (build.sbt) for vulnerable **DIRECT** dependencies
- **Automatically creates PRs** with security fixes (all severities)
- Fixes your current 7 Dependabot alerts

**When it runs:**
- ✅ Every Monday at 9 AM UTC
- ✅ On every pom.xml/build.sbt change
- ✅ Manual trigger available

**Quick Action:**
https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/working-dependency-update.yml

---

### 3. 📊 Comprehensive Security Report (Veracode-style)
**File:** `.github/workflows/comprehensive-security-report.yml`

**What it does:**
- Generates professional security reports like Veracode
- SAST + SCA + Secret Detection + Config Scanning
- Beautiful HTML reports with dashboards
- CVE/CWE + CVSS scores + Remediation guidance

**When it runs:**
- ✅ Every Monday at 2 AM UTC
- ✅ On every push to main
- ✅ Manual trigger available

**Quick Action:**
https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/comprehensive-security-report.yml

**Documentation:** [VERACODE_STYLE_SECURITY_REPORTS.md](VERACODE_STYLE_SECURITY_REPORTS.md)

---

### 4. 🔍 Semgrep Security Scan
**File:** `.github/workflows/semgrep.yml`

**What it does:**
- SAST (Static Application Security Testing)
- Detects code-level vulnerabilities
- OWASP Top 10 coverage
- Uploads to GitHub Security tab

**When it runs:**
- ✅ On every push to main
- ✅ On every pull request
- ✅ Daily at midnight UTC

---

### 5. 🛡️ CodeQL Analysis
**File:** `.github/workflows/codeql.yml`

**What it does:**
- GitHub's native code scanning
- Deep semantic analysis
- Vulnerability detection
- Security alerts

**When it runs:**
- ✅ On every push to main
- ✅ On every pull request

---

## 📊 Comparison Table

| Workflow | Severity Filter | Auto PRs | Frequency | Your Issues | Target |
|----------|-----------------|----------|-----------|-------------|--------|
| **♻️ Security PRs by Severity** | Runs per severity (CRITICAL/HIGH/MEDIUM) | ✅ | Weekly | Severity-specific | Code + Deps |
| **🤖 Dependency Update** | All | ✅ | Weekly | Direct dependency alerts | Direct Deps |
| **📊 Comprehensive Report** | All | ❌ Report | Weekly | **112 issues** | All |
| **🔍 Semgrep** | All | ❌ Alert | Daily | Real-time | Code |
| **🛡️ CodeQL** | All | ❌ Alert | On Push | Real-time | Code |

---

## 🚀 Quick Actions

### Create Security PRs for Specific Severities (CRITICAL → HIGH → MEDIUM)
**Run the severity workflow (creates three PRs automatically):**
```
https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/security-pr-by-severity.yml
```
Click "Run workflow" → Wait ~6 minutes → Review PRs labelled `critical`, `high`, `medium` → Merge in priority order.

### Fix All Dependency Vulnerabilities
**Use this workflow to create an automated PR with direct dependency bumps:**
```
 https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/working-dependency-update.yml
 ```
 Click "Run workflow" → Wait 2 minutes → Review PR → Merge!

### Generate Security Report NOW
**Use this workflow to get a Veracode-style report:**
```
https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/comprehensive-security-report.yml
```
Click "Run workflow" → Wait 5-10 minutes → Download reports from Artifacts!

---

## 📥 Where to Find Results

### Dependabot Alerts
- **Location:** Security tab → Dependabot alerts
- **Current Status:** 7 vulnerabilities (6 HIGH, 1 MODERATE)
- **How to Fix:** Run the Dependency Update workflow

### Security Scan Reports (Veracode-style)
- **Location:** Actions → Comprehensive Security Report → Artifacts
- **Download:** security-reports.zip
- **Main Report:** html/comprehensive-report.html
- **Contains:** CVE, CVSS, severity, remediation guidance

### Code Scanning Alerts
- **Location:** Security tab → Code scanning alerts
- **Sources:** Semgrep, CodeQL
- **Real-time:** Updated on every push/PR

---

## 🎯 Recommended Workflow

### For Fixing Known Vulnerabilities:
1. ✅ **Use:** Automated Third-Party Library Security Update
2. ✅ **Benefit:** Creates PR automatically with fixes
3. ✅ **Time:** 2-3 minutes

### For Detailed Security Analysis:
1. ✅ **Use:** Comprehensive Security Report
2. ✅ **Benefit:** Professional Veracode-like reports
3. ✅ **Time:** 5-10 minutes

### For Continuous Monitoring:
1. ✅ **Use:** Semgrep + CodeQL (automatic)
2. ✅ **Benefit:** Catch issues on every code change
3. ✅ **Time:** Automatic, no action needed

---

## 📚 Documentation

- **[SECURITY_PR_BY_SEVERITY.md](SECURITY_PR_BY_SEVERITY.md)** ♻️ NEW – How the severity-based PR workflow works
- **[AUTOMATED_SECURITY_COMPLETE_GUIDE.md](AUTOMATED_SECURITY_COMPLETE_GUIDE.md)** - Complete automation guide
- **[VERACODE_STYLE_SECURITY_REPORTS.md](VERACODE_STYLE_SECURITY_REPORTS.md)** - Report generation guide
- **[SECURITY_SCANNING.md](SECURITY_SCANNING.md)** - Technical scanning details

---

## ✅ Current Setup Summary

Your repository has:
- ✅ **6 automated security workflows**
- ✅ **Severity-aware PR automation** (creates PR per severity)
- ✅ **SAST + SCA combined coverage**
- ✅ **Automatic PR creation** for direct dependencies
- ✅ **Professional security reports** (Veracode-style)
- ✅ **Daily + Weekly automated scans**
- ✅ **Real-time monitoring** on every push/PR

**Result: Enterprise-grade security automation with severity-prioritised remediation!** 🎉

---

## 🚨 URGENT ACTION REQUIRED

**You currently have 112 total vulnerabilities:**
- 🔴 **8 CRITICAL** - IMMEDIATE ACTION REQUIRED!
- 🟠 **61 HIGH** - High priority
- 🟡 **43 MEDIUM/LOW** - Address after critical/high

### Step 1: Run Severity PR Workflow (CRITICAL → HIGH → MEDIUM)
1. Trigger: https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/security-pr-by-severity.yml
2. Wait for completion (~6 minutes)
3. Review the three generated PRs starting with `critical`
4. Merge and deploy in priority order

### Step 2: Run Direct Dependency Update
Use the dependency update workflow to clear remaining Dependabot alerts.

---

*Last updated: November 7, 2025*


