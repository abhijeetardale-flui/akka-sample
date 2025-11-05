# GitHub Security Scanning Setup

## ⚠️ Important: GitHub Advanced Security Requirement

To use **Code Scanning** (SARIF uploads) with Semgrep and PMD, you need:

### For Public Repositories
✅ **Code Scanning is FREE and enabled by default**

### For Private Repositories
You need **GitHub Advanced Security** enabled:

#### How to Check/Enable GitHub Advanced Security:

1. Go to your repository on GitHub
2. Click **Settings** → **Code security and analysis**
3. Look for **"GitHub Advanced Security"** section
4. If you see it's disabled, click **Enable**

**Note**: GitHub Advanced Security may require a paid plan for private repositories.

## 🔧 Alternative: Artifact-Only Scanning

If you cannot enable GitHub Advanced Security (for private repos), you can still use the tools by viewing reports as artifacts:

### Modified PMD Workflow (No SARIF Upload)

If you're getting permission errors, you can comment out or remove the SARIF upload step in `.github/workflows/pmd.yml`:

```yaml
# Comment out this step if GitHub Advanced Security is not available
# - name: Upload PMD SARIF results to GitHub
#   uses: github/codeql-action/upload-sarif@v3
#   if: always()
#   with:
#     sarif_file: pmd-reports/pmd-report.sarif
```

The HTML and JSON reports will still be available as workflow artifacts.

## 📊 Current Status

### Workflow Permissions Added:
- ✅ **Semgrep**: `contents: read`, `security-events: write`, `actions: read`
- ✅ **PMD**: `contents: read`, `security-events: write`, `actions: read`
- ✅ **SpotBugs**: `contents: read`, `actions: read`

### Repository Settings to Verify:

1. **Actions Permissions**:
   - Go to Settings → Actions → General
   - Under "Workflow permissions", ensure:
     - ✅ "Read and write permissions" is selected, OR
     - ✅ "Read repository contents and packages permissions" + explicit permissions in workflow

2. **Code Scanning**:
   - Go to Settings → Code security and analysis
   - Ensure "Code scanning" tools can be enabled

## 🐛 Troubleshooting

### Error: "Resource not accessible by integration"

**Possible causes:**

1. **Private repository without GitHub Advanced Security**
   - Solution: Enable GitHub Advanced Security or use artifact-only mode

2. **Insufficient workflow permissions**
   - Solution: Already fixed in the updated workflows

3. **Organization restrictions**
   - Solution: Contact your GitHub organization admin to enable code scanning

### Error: "security-events: write permission required"

**Solution**: This has been fixed by adding proper permissions at the workflow level.

## ✅ Verification Steps

After pushing the permission fixes:

1. Go to **Actions** tab
2. Wait for workflows to complete
3. Check if the error persists

If the error is still there:
- Verify your repository is **public** OR has **GitHub Advanced Security** enabled
- Check the **Settings → Actions → General** for workflow permissions
- Contact your repository/organization admin if needed

## 📝 What Works Without GitHub Advanced Security

| Tool | Artifact Reports | SARIF Upload | Works Without GH Advanced Security |
|------|------------------|--------------|-----------------------------------|
| **Semgrep** | ✅ JSON reports | ❌ Requires GH Advanced Security | ✅ Partial (artifacts only) |
| **SpotBugs** | ✅ HTML/XML reports | N/A | ✅ Yes |
| **PMD** | ✅ HTML reports | ❌ Requires GH Advanced Security | ✅ Partial (artifacts only) |

## 🎯 Recommended Action

**If this is a public repository:**
- The fixes should work immediately after the next workflow run

**If this is a private repository:**
- Enable GitHub Advanced Security in repository settings
- Or modify workflows to remove SARIF upload steps and use artifacts only

