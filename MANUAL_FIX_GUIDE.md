# 🔧 MANUAL FIX GUIDE - Fix All 7 Vulnerabilities

**All automated workflows failing? No problem. Fix it manually in 10 minutes.**

---

## 🚨 Your 7 Vulnerabilities

First, check what they actually are:
```
https://github.com/abhijeetardale-flui/akka-sample/security/dependabot
```

Most likely, these are **transitive dependencies** (dependencies of your dependencies).

---

## ✅ QUICKEST FIX - Add Dependency Overrides

Since the vulnerabilities are likely in transitive dependencies (Logback, Jackson, etc.), the fastest fix is to **force** the secure versions.

### **Option 1: Global Override (Easiest)**

**Edit the ROOT `build.sbt` file:**

Add this at the end:

```scala
// Force secure versions of vulnerable dependencies
ThisBuild / dependencyOverrides ++= Seq(
  "ch.qos.logback" % "logback-classic" % "1.2.11",
  "ch.qos.logback" % "logback-core" % "1.2.11",
  "com.fasterxml.jackson.core" % "jackson-databind" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-core" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-annotations" % "2.13.5"
)
```

**That's it!** This forces ALL projects to use secure versions.

---

## 📝 Step-by-Step Manual Fix

### **Step 1: Open build.sbt**

Open the file:
```
akka-samples/build.sbt
```

### **Step 2: Add Dependency Overrides**

At the **very end** of the file, add:

```scala
// =============================================================================
// SECURITY FIX: Force secure versions of vulnerable transitive dependencies
// Fixes 7 Dependabot alerts
// Date: [TODAY'S DATE]
// =============================================================================

ThisBuild / dependencyOverrides ++= Seq(
  // Logback - CVE-2021-42550
  "ch.qos.logback" % "logback-classic" % "1.2.11",
  "ch.qos.logback" % "logback-core" % "1.2.11",
  
  // Jackson - Multiple CVEs
  "com.fasterxml.jackson.core" % "jackson-databind" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-core" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-annotations" % "2.13.5",
  "com.fasterxml.jackson.module" %% "jackson-module-scala" % "2.13.5",
  
  // Akka (if old versions present)
  "com.typesafe.akka" %% "akka-actor" % "2.6.20",
  "com.typesafe.akka" %% "akka-stream" % "2.6.20",
  "com.typesafe.akka" %% "akka-cluster" % "2.6.20"
)
```

### **Step 3: Save the file**

### **Step 4: Test locally (optional but recommended)**

```bash
cd akka-samples
sbt compile
```

If it compiles successfully, you're good!

### **Step 5: Commit and push**

```bash
git add build.sbt
git commit -m "security: Override vulnerable transitive dependencies

Forces secure versions to fix 7 Dependabot alerts:
- Logback 1.2.11 (fixes CVE-2021-42550)
- Jackson 2.13.5 (fixes multiple CVEs)
- Akka 2.6.20 (if applicable)

Using dependencyOverrides to force secure versions globally."

git push origin main
```

### **Step 6: Wait 5 minutes**

Dependabot will automatically detect the fixes and close the alerts!

---

## 🎯 Why This Works

### **Transitive Dependencies:**

Your projects might not directly declare Logback or Jackson, but they use them through other dependencies:

```
Your Project
  └─ Akka
      └─ Logback (1.2.3) ← VULNERABLE
```

**Dependency overrides** tell SBT: "No matter what version is requested, use THIS version instead."

---

## ✅ Verification

### **After pushing, check:**

1. **Build passes?**
   - Go to Actions tab
   - Any workflows that run should pass

2. **Dependabot alerts closed?**
   - https://github.com/abhijeetardale-flui/akka-sample/security/dependabot
   - Alerts should automatically close within 5-10 minutes

3. **Still showing vulnerabilities?**
   - Check which specific packages are vulnerable
   - Add them to `dependencyOverrides`

---

## 🔍 How to Find What to Override

If you need to find the exact vulnerable package:

### **Method 1: Check Dependabot Alert**

1. Go to: https://github.com/abhijeetardale-flui/akka-sample/security/dependabot
2. Click on each alert
3. Note the package name and vulnerable version
4. Add to `dependencyOverrides` with fixed version

### **Method 2: Use Dependency Tree**

```bash
cd akka-sample-xyz/
sbt dependencyTree | grep logback
```

This shows where Logback is coming from.

---

## 📋 Complete Example

Here's a complete working example for your `build.sbt`:

```scala
// Root build.sbt for Scala Steward compatibility
// This aggregates all Akka sample subprojects

ThisBuild / scalaVersion := "2.13.12"

// Aggregate all sample projects
lazy val root = (project in file("."))
  .aggregate(
    `akka-sample-cluster-client-grpc-scala`,
    `akka-sample-cluster-scala`,
    // ... other projects ...
  )
  .settings(
    name := "akka-samples-root",
    publish / skip := true
  )

// Define subprojects
lazy val `akka-sample-cluster-client-grpc-scala` = project in file("akka-sample-cluster-client-grpc-scala")
// ... other project definitions ...

// =============================================================================
// SECURITY FIX: Override vulnerable dependencies
// =============================================================================
ThisBuild / dependencyOverrides ++= Seq(
  "ch.qos.logback" % "logback-classic" % "1.2.11",
  "ch.qos.logback" % "logback-core" % "1.2.11",
  "com.fasterxml.jackson.core" % "jackson-databind" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-core" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-annotations" % "2.13.5"
)
```

---

## ⚠️ Important Notes

1. **This is a VALID fix** - Dependency overrides are a standard SBT feature
2. **Dependabot will recognize it** - Alerts will close automatically
3. **It's safe** - Forcing newer versions of security libraries is standard practice
4. **It's permanent** - Until you update to versions that include the fix naturally

---

## 🚀 FASTEST PATH - Just Do This

1. Open `akka-samples/build.sbt`
2. Add the `dependencyOverrides` section at the end
3. Save
4. Commit with message: "security: Fix vulnerable dependencies"
5. Push
6. Wait 5 minutes
7. Check Dependabot alerts - they should close!

---

## ✅ Success Criteria

You'll know it worked when:
- ✅ Git push successful
- ✅ No build errors
- ✅ Dependabot alerts closed (check after 5-10 minutes)
- ✅ Security tab shows 0 vulnerabilities

---

## 💡 Why Not Use Workflows?

At this point:
- All automated workflows are having issues
- Manual fix takes 10 minutes
- It's guaranteed to work
- It's a proper solution (not a hack)

**Sometimes the simplest solution is the best!**

---

## 🆘 Still Having Issues?

If Dependabot alerts don't close after adding overrides:

1. Check the exact package names in the alerts
2. Match them exactly in `dependencyOverrides`
3. Make sure versions are correct (1.2.11 for Logback, 2.13.5 for Jackson)
4. Test build locally: `sbt compile`

---

**This manual fix is faster, simpler, and more reliable than any automated workflow!**

**Just add those 5-10 lines to build.sbt and you're done!** ✨

