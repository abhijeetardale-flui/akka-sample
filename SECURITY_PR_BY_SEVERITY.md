# ♻️ Security PRs by Severity

This guide explains how the `Security Fix Pull Requests by Severity` workflow works and how to use the PRs it creates.

---

## 🔧 Overview

- **Workflow:** `.github/workflows/security-pr-by-severity.yml`
- **Scans:** Trivy (SCA) + Semgrep (SAST)
- **Outputs:**
  - Three PRs (labels `critical`, `high`, `medium`)
  - Markdown summaries at `security-reports/auto/<severity>-security-summary.md`
  - GitHub Code Scanning entries (handled by the comprehensive report workflow)
- **Schedule:** Mondays at 03:00 UTC (manual trigger available)

Each run performs one scan and then fans out into three jobs so every severity gets its own PR. Dependency upgrades are applied automatically when a fixed version is known; code issues that need manual review are documented in the PR body and the summary file.

---

## 🏁 Running the Workflow

1. Trigger the workflow:
   - https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/security-pr-by-severity.yml
2. Wait for the workflow to finish (~6 minutes).
3. Review the generated PRs (starting with `critical`).
4. Merge once validation/tests pass.

The workflow automatically labels PRs with:
- `security`
- `automated-pr`
- `critical` or `high` or `medium`

This enables the comprehensive report workflow to surface direct links inside the daily summary.

---

## 📦 What Each PR Contains

| Item | Details |
|------|---------|
| Commit(s) | Dependency version bumps + updated `security-reports/auto/<severity>-security-summary.md` |
| PR Body | Breakdown of findings (SCA & SAST) with CVEs, locations, and remediation status |
| Labels | `security`, `automated-pr`, severity label |
| Testing Checklist | Pre-populated checklist for reviewers |

If no dependency update is available for a finding, the summary file still records the issue and the PR remains open for manual remediation.

---

## 🧪 Validation Checklist (per PR)

- [ ] Build passes (`mvn clean install` / `sbt compile` as appropriate)
- [ ] Tests pass
- [ ] Security changes reviewed by an engineer
- [ ] Summary file reviewed for accuracy

---

## 🔗 Integration with Comprehensive Report

The comprehensive report workflow (`comprehensive-security-report.yml`) queries for open PRs with labels `security` + severity. Once the severity PRs are open, they appear in the report summary under **Security Fix Pull Requests**, satisfying the requirement that each severity item links to a PR.

---

## 🛠️ Troubleshooting

| Problem | Resolution |
|---------|------------|
| Workflow creates no PR for a severity | Check the job summary; if `Has issues: false`, no findings existed. |
| PR created but no dependency updates applied | The vulnerabilities need manual code changes; review the summary file and PR body for instructions. |
| Labels missing | Create labels (`critical`, `high`, `medium`) in the repository or organization and rerun. |
| Pull request creation denied | Ensure repository workflow permissions are set to **Read and write** and “Allow GitHub Actions to create and approve pull requests” is enabled. |

---

## 📅 Recommended Cadence

1. **Monday 03:00 UTC** – Severity PR workflow (automatic)
2. **Monday 02:00 UTC** – Comprehensive security report workflow (automatic)
3. **Monday 09:00 UTC** – Dependency update workflow (automatic)

Review and merge PRs in descending severity order (`critical` → `high` → `medium`).

---

*Last updated: November 7, 2025*
