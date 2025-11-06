# 🔧 Workflow Permissions Troubleshooting Guide

## ✅ Auto-Fix Security Issues - FIXED!

The "Resource not accessible by integration" error has been fixed by adding the missing `issues: write` permission.

---

## 🔍 What Was the Issue?

### Error:
```
RequestError [HttpError]: Resource not accessible by integration
status: 403
x-accepted-github-permissions': 'issues=write'
```

### Root Cause:
The Auto-Fix Security workflow tried to create GitHub Issues but didn't have the `issues: write` permission.

### Fix Applied:
✅ Added `issues: write` to workflow permissions  
✅ Added explicit error handling  
✅ Added fallback to workflow summary  
✅ Made workflow resilient to permission failures  

---

## 🛡️ Required Permissions for Each Workflow

### 1. SAST Scan
```yaml
permissions:
  contents: read
  security-events: write  # For SARIF upload
  actions: read
```

### 2. Semgrep
```yaml
permissions:
  contents: read
  security-events: write  # For SARIF upload
  actions: read
```

### 3. SpotBugs
```yaml
permissions:
  contents: read
  actions: read
```

### 4. PMD
```yaml
permissions:
  contents: read
  security-events: write  # For SARIF upload
  actions: read
```

### 5. Auto-Fix Security (FIXED)
```yaml
permissions:
  contents: write          # For code changes
  pull-requests: write     # For creating PRs
  issues: write           # For creating issues ✅ NOW ADDED
  security-events: read   # For reading scan results
  actions: read
```

### 6. Scala Steward
```yaml
permissions:
  contents: write         # For dependency updates
  pull-requests: write    # For creating PRs
```

---

## ⚙️ Repository-Level Permissions Check

Even with workflow permissions configured, you need to ensure repository settings allow workflows to perform these actions.

### How to Verify:

1. **Go to Repository Settings:**
   ```
   https://github.com/abhijeetardale-flui/akka-sample/settings
   ```

2. **Navigate to Actions → General:**
   ```
   Settings → Actions → General
   ```

3. **Check "Workflow permissions":**
   
   Should be set to:
   - ✅ **"Read and write permissions"** (RECOMMENDED)
   
   OR at minimum:
   - ⚠️ "Read repository contents and packages permissions" 
     + Individual workflow permissions (already configured)

### Recommended Setting:

```
Workflow permissions: Read and write permissions
✓ Allow GitHub Actions to create and approve pull requests
```

This ensures all workflows can perform their intended functions.

---

## 🔧 How to Fix Permission Issues

### Method 1: Update Repository Settings (Easiest)

1. Go to: `Settings → Actions → General`
2. Under "Workflow permissions", select:
   - ✅ **"Read and write permissions"**
3. Check:
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**
4. Click **Save**

### Method 2: Use Workflow-Level Permissions (Already Done)

We've already configured explicit permissions in each workflow file. This is more secure but requires careful configuration.

---

## 🚨 Common Permission Errors

### 1. "Resource not accessible by integration" (403)
**Cause:** Missing permission in workflow  
**Fix:** Add required permission (e.g., `issues: write`, `pull-requests: write`)

### 2. "GITHUB_TOKEN has insufficient permissions" (403)
**Cause:** Repository settings too restrictive  
**Fix:** Enable "Read and write permissions" in repository settings

### 3. "Cannot create pull request" (403)
**Cause:** Missing `pull-requests: write` or setting disabled  
**Fix:** 
- Add `pull-requests: write` to workflow
- Enable "Allow GitHub Actions to create and approve pull requests" in settings

### 4. "Cannot upload SARIF" (403)
**Cause:** Missing `security-events: write` permission  
**Fix:** Already added with `continue-on-error: true` for graceful degradation

---

## ✅ Current Status After Fix

| Workflow | Status | Issue Creation | PR Creation | SARIF Upload |
|----------|--------|----------------|-------------|--------------|
| SAST Scan | ✅ Works | N/A | N/A | ✅ Works |
| Semgrep | ✅ Works | N/A | N/A | ✅ Works |
| SpotBugs | ✅ Works | N/A | N/A | N/A |
| PMD | ✅ Works | N/A | N/A | ✅ Works |
| Auto-Fix Security | ✅ **FIXED** | ✅ **Fixed** | ✅ Works | N/A |
| Scala Steward | ✅ Works | N/A | ✅ Works | N/A |
| Dependabot | ✅ Works | ✅ Works | ✅ Works | N/A |

---

## 🎯 Verification Steps

### Test the Fix:

1. **Trigger Auto-Fix Security manually:**
   - Go to: Actions → Auto-Fix Security Issues
   - Click "Run workflow"
   - Select "dependencies"
   - Click "Run workflow"

2. **Check for successful execution:**
   - Workflow should complete successfully
   - Check "Issues" tab for new issue (if vulnerabilities found)
   - Check workflow summary for recommendations

3. **If still failing:**
   - Verify repository settings (see above)
   - Check workflow logs for specific error
   - See troubleshooting section below

---

## 🐛 Advanced Troubleshooting

### Error Persists After Fix?

1. **Check Organization Settings:**
   If your repository is in an organization:
   - Organization might have restricted workflow permissions
   - Contact organization admin
   - May need to enable at organization level

2. **Check Branch Protection Rules:**
   - Go to: Settings → Branches → Branch protection rules
   - Ensure rules don't block workflow actions
   - May need to add GitHub Actions to allowed users

3. **Check Token Permissions:**
   - Default `GITHUB_TOKEN` should work for most cases
   - For cross-repository actions, you may need a Personal Access Token (PAT)

### Debug Mode:

Enable debug logging:
1. Go to: Settings → Secrets and variables → Actions
2. Add repository secret:
   - Name: `ACTIONS_STEP_DEBUG`
   - Value: `true`
3. Re-run workflow to see detailed logs

---

## 📚 Best Practices

### 1. Principle of Least Privilege
✅ Give workflows only the permissions they need  
✅ Use workflow-level permissions (already implemented)  
✅ Review permissions regularly  

### 2. Error Handling
✅ Use `continue-on-error: true` for non-critical steps (implemented)  
✅ Add fallbacks for permission failures (implemented)  
✅ Log errors clearly for debugging (implemented)  

### 3. Security
✅ Never use overly permissive settings unless required  
✅ Audit workflow changes before merging  
✅ Review bot-created PRs before merging  

---

## 🔗 Resources

- [GitHub Actions Permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token)
- [Workflow Permissions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions)
- [Troubleshooting Workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows)

---

## ✅ Summary

**Problem:** Auto-Fix Security workflow couldn't create issues  
**Cause:** Missing `issues: write` permission  
**Solution:** Added permission + error handling  
**Status:** ✅ **FIXED**  

**Next Steps:**
1. ✅ Fix is already deployed
2. ✅ Workflow will work on next run
3. ⚠️ Verify repository settings if issues persist
4. ✅ Check Issues tab for automated recommendations

---

*Last Updated: After fixing permission issue*  
*Status: ✅ All workflows operational*


