# 🏢 Organization Repository Setup Guide

## Why No PRs Are Being Created?

Your repository is **public but under an organization**. This requires additional permissions at the **organization level**.

---

## 🔧 Required Fixes (Step-by-Step)

### **STEP 1: Organization Settings** ⚠️ IMPORTANT

You or your **organization admin** need to configure these:

#### 1.1 Enable GitHub Actions for the Organization

1. Go to your **organization settings**:
   ```
   https://github.com/organizations/YOUR_ORG_NAME/settings/actions
   ```

2. Under **"Actions permissions"**, ensure:
   - ✅ **"Allow all actions and reusable workflows"** is selected
   
   OR at minimum:
   - ✅ **"Allow select actions and reusable workflows"**
     - Add: `actions/*`, `github/*`, `scala-steward-org/*`, `AppThreat/*`

#### 1.2 Enable Dependabot for the Organization

1. Go to organization settings:
   ```
   https://github.com/organizations/YOUR_ORG_NAME/settings/security_analysis
   ```

2. Enable:
   - ✅ **Dependency graph**
   - ✅ **Dependabot alerts**
   - ✅ **Dependabot security updates**

#### 1.3 Configure Workflow Permissions (Organization Level)

1. Go to:
   ```
   https://github.com/organizations/YOUR_ORG_NAME/settings/actions
   ```

2. Scroll to **"Workflow permissions"**

3. Select:
   - ✅ **"Read and write permissions"**

4. Check:
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**

---

### **STEP 2: Repository Settings**

Even after organization settings, configure at repository level:

#### 2.1 Enable Actions

1. Go to:
   ```
   https://github.com/abhijeetardale-flui/akka-sample/settings/actions
   ```

2. Under **"Actions permissions"**:
   - ✅ Enable actions (should inherit from organization)

3. Under **"Workflow permissions"**:
   - ✅ **"Read and write permissions"**
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**

#### 2.2 Enable Dependabot

1. Go to:
   ```
   https://github.com/abhijeetardale-flui/akka-sample/settings/security_analysis
   ```

2. Enable these features:
   - ✅ **Dependency graph** → Click "Enable"
   - ✅ **Dependabot alerts** → Click "Enable"
   - ✅ **Dependabot security updates** → Click "Enable"

---

### **STEP 3: Manually Trigger Workflows**

After enabling all settings, manually trigger the workflows:

#### 3.1 Trigger Scala Steward (Main Dependency Agent)

1. Go to:
   ```
   https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/scala-steward.yml
   ```

2. Click **"Run workflow"**

3. Select branch: **main**

4. Click **"Run workflow"**

#### 3.2 Trigger Manual Dependency Check

1. Go to:
   ```
   https://github.com/abhijeetardale-flui/akka-sample/actions/workflows/manual-dependency-check.yml
   ```

2. Click **"Run workflow"**

3. Select **"Auto-create PRs: true"**

4. Click **"Run workflow"**

---

## 🚨 Important Note About SBT Projects

### Dependabot Limitation:
**Dependabot does NOT support SBT (Scala Build Tool)** natively. That's why:

✅ **Use Scala Steward instead** - Better support for SBT  
✅ **Dependabot only handles** GitHub Actions updates  
✅ **Manual Dependency Check workflow** can also help  

### Supported by Dependabot:
- ✅ GitHub Actions (`.github/workflows/*.yml`)
- ❌ SBT (`build.sbt`) - **NOT SUPPORTED**
- ❌ Scala dependencies - **NOT SUPPORTED**

### Supported by Scala Steward:
- ✅ SBT (`build.sbt`)
- ✅ Scala dependencies
- ✅ Plugin dependencies
- ✅ All Akka-related libraries

---

## 🔍 Verify Setup

### Check if Dependabot is Working:

1. Go to:
   ```
   https://github.com/abhijeetardale-flui/akka-sample/network/updates
   ```

2. You should see:
   - Dependabot status
   - Any pending updates
   - Update history

### Check Current Vulnerabilities:

Visit:
```
https://github.com/abhijeetardale-flui/akka-sample/security/dependabot
```

You should see your **7 vulnerabilities** listed with options to:
- "Create Dependabot security update" buttons
- Or manual fix instructions

---

## 🎯 Quick Test

### Test 1: Create a Test PR Manually

Let's verify permissions work by manually triggering Scala Steward:

```bash
# Go to Actions → Scala Steward → Run workflow
```

If it **fails** with permission errors → Organization settings need adjustment  
If it **succeeds** but no PR → No updates needed or SBT issues  

### Test 2: Check Workflow Logs

1. Go to **Actions** tab
2. Click on **Scala Steward** workflow
3. Check the logs for errors

Common errors:
- ❌ "Permission denied" → Organization/repo permissions
- ❌ "Cannot create PR" → Workflow permissions
- ❌ "Dependabot not enabled" → Security settings

---

## 📋 Checklist

Use this checklist to ensure everything is configured:

### Organization Level (Need Admin Access):
- [ ] Actions enabled for organization
- [ ] Dependabot enabled for organization
- [ ] Workflow permissions: Read and write
- [ ] Allow Actions to create PRs: Enabled

### Repository Level:
- [ ] Actions enabled for repository
- [ ] Dependabot alerts: Enabled
- [ ] Dependabot security updates: Enabled
- [ ] Dependency graph: Enabled
- [ ] Workflow permissions: Read and write
- [ ] Allow Actions to create PRs: Enabled

### Workflows:
- [ ] Scala Steward workflow present
- [ ] Manual Dependency Check workflow present
- [ ] Auto-Fix Security workflow present
- [ ] All workflows have proper permissions

### Testing:
- [ ] Manually triggered Scala Steward
- [ ] Manually triggered Dependency Check
- [ ] Checked for PRs in Pull Requests tab
- [ ] Checked for issues in Issues tab
- [ ] Verified workflow logs for errors

---

## 🛠️ Manual Workaround (If Organization Settings Can't Be Changed)

If you **don't have organization admin access** and can't change settings:

### Option 1: Fork to Personal Account
Fork the repository to your personal account where you have full control.

### Option 2: Manual Updates
Use the manual dependency check workflow:
1. Trigger it weekly
2. Review dependency report
3. Update `build.sbt` manually
4. Create PRs yourself

### Option 3: Local Scala Steward
Run Scala Steward locally:

```bash
# Install Scala Steward
# See: https://github.com/scala-steward-org/scala-steward

# Run locally
scala-steward --workspace <path> \
  --repos-file repos.md \
  --git-author-name "Your Name" \
  --git-author-email "your@email.com"
```

---

## 🤖 Expected Behavior After Setup

Once everything is configured correctly:

### Immediately:
- ✅ Manual workflows can be triggered
- ✅ Workflows complete without permission errors

### Within 24 Hours:
- ✅ Dependabot scans for GitHub Actions updates
- ✅ Creates PRs for any outdated actions

### Every Monday 08:00 UTC:
- ✅ Scala Steward runs automatically
- ✅ Checks all SBT projects for updates
- ✅ Creates PRs for dependency updates

### When Vulnerability Detected:
- ✅ Dependabot creates immediate PR (for supported ecosystems)
- ✅ Issue created with recommendations

---

## 💡 Pro Tips

### 1. Check Organization Admin:
Find out who has admin access:
```
Go to: https://github.com/orgs/YOUR_ORG_NAME/people
Filter by: "Role: Owner"
```

### 2. Request Settings Change:
Send this guide to your organization admin with these specific requests:
- Enable Actions with "Read and write permissions"
- Enable "Allow GitHub Actions to create and approve pull requests"
- Enable Dependabot at organization level

### 3. Monitor Progress:
After settings are changed:
- Watch the **Pull Requests** tab
- Check **Actions** tab for workflow runs
- Review **Security** tab for Dependabot alerts

---

## 📞 Need Help?

### Still Not Working?

1. **Check workflow logs** for specific errors
2. **Verify all checkboxes** in the checklist above
3. **Contact organization admin** to verify organization settings
4. **Try manual trigger** of workflows to test permissions

### Common Organization Issues:

| Issue | Cause | Solution |
|-------|-------|----------|
| No PRs created | Organization restricts Actions | Admin must enable Actions |
| Permission denied | Workflow permissions too restrictive | Enable "Read and write" |
| Can't create PRs | PR creation blocked | Enable "Allow Actions to create PRs" |
| Dependabot not running | Dependabot disabled | Enable at org + repo level |

---

## ✅ Summary

**Problem**: No coding PRs being created  
**Cause**: Organization-level permissions  
**Solution**: Enable Actions + Dependabot at organization level  
**Required**: Organization admin access  

**After Fix**: PRs will be created automatically by Scala Steward and Dependabot

---

*Last Updated: Added organization configuration guide*  
*Status: Awaiting organization-level permission changes*


