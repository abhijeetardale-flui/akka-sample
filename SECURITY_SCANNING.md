# Security Scanning Setup

This repository includes automated security and code quality scanning using **four complementary tools** that provide comprehensive coverage.

## 🔍 Scanning Tools

### 1. **SAST Scan (ShiftLeft/AppThreat)** - All-in-One Security Scanner ⭐ RECOMMENDED
- **Purpose**: Comprehensive SAST, dependency scanning, license checking, and IaC analysis
- **Strengths**: 
  - Multi-language support (Java, Scala, Python, JavaScript, etc.)
  - Dependency vulnerability detection (CVEs)
  - License compliance checking
  - Infrastructure as Code (IaC) security
  - Container security scanning
  - No server required, fully CI-based
  - Combines SAST + SCA in one tool
- **Runs**: On push, PR, and weekly on Mondays
- **Results**: Available in GitHub Security tab and as artifacts

### 2. **Semgrep** - Fast Static Analysis
- **Purpose**: Detects code-level security vulnerabilities
- **Strengths**: 
  - Quick execution
  - Low false positive rate
  - Detects OWASP Top 10 vulnerabilities
  - Language-aware pattern matching
- **Runs**: On every push, PR, and daily at midnight UTC
- **Results**: Available in GitHub Security tab (Code scanning alerts)

### 2. **SpotBugs** - Java/Scala Bug Detector
- **Purpose**: Finds bugs and potential vulnerabilities in Java bytecode
- **Strengths**:
  - Deep bytecode analysis
  - Detects concurrency issues
  - Finds resource leaks
  - Security vulnerability detection
- **Runs**: On every push and PR
- **Results**: Available as workflow artifacts

### 3. **PMD** - Code Quality & Maintainability
- **Purpose**: Identifies code smells and maintainability issues
- **Strengths**:
  - Detects potential security risks through code quality issues
  - Best practices enforcement
  - Performance issue detection
  - Thread safety problems
- **Runs**: On every push and PR
- **Results**: Available in GitHub Security tab and as artifacts

## 🆚 Tool Comparison

| Feature | SAST Scan | Semgrep | SpotBugs | PMD |
|---------|-----------|---------|----------|-----|
| **SAST (Security)** | ✅ Excellent | ✅ Excellent | ✅ Good | ⚠️ Limited |
| **Dependency Scan** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **License Check** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **IaC Security** | ✅ Yes | ⚠️ Limited | ❌ No | ❌ No |
| **Code Quality** | ⚠️ Basic | ❌ No | ✅ Yes | ✅ Excellent |
| **Speed** | ⚠️ Medium | ✅ Fast | ⚠️ Slow | ⚠️ Medium |
| **False Positives** | ⚠️ Some | ✅ Low | ⚠️ Some | ⚠️ Many |
| **Multi-language** | ✅ Yes | ✅ Yes | ❌ JVM only | ❌ Java only |

**Recommendation**: Use **SAST Scan** as your primary security tool, and complement with:
- **SpotBugs** for deep JVM bytecode analysis
- **PMD** for code quality and maintainability
- **Semgrep** for fast security checks (optional if SAST Scan is sufficient)

## 📊 Viewing Results

### Security Tab (SARIF Reports)
1. Go to your repository on GitHub
2. Click on the **Security** tab
3. Select **Code scanning alerts**
4. View detailed findings from Semgrep and PMD

### Workflow Artifacts
1. Go to **Actions** tab
2. Click on a completed workflow run
3. Scroll down to **Artifacts** section
4. Download reports for detailed analysis

## 🚀 Local Execution

### Run SAST Scan Locally
```bash
# Using Docker (recommended)
docker run --rm -v $(pwd):/app shiftleft/sast-scan scan --src /app --type java,scala

# Or install locally
pip install appthreat-depscan
scan --src . --type java,scala
```

### Run Dependency Scan Locally
```bash
# Using Docker
docker run --rm -v $(pwd):/app shiftleft/scan-slim depscan --src /app --type java

# Or install locally
pip install appthreat-depscan
depscan --src . --type java
```

### Run Semgrep Locally
```bash
# Install Semgrep
pip install semgrep

# Run scan
semgrep --config auto .
```

### Run SpotBugs Locally
```bash
# In each project directory with build.sbt
sbt compile
sbt spotbugs
```

### Run PMD Locally
```bash
# Download PMD
wget https://github.com/pmd/pmd/releases/download/pmd_releases%2F7.0.0/pmd-dist-7.0.0-bin.zip
unzip pmd-dist-7.0.0-bin.zip

# Run analysis
./pmd-bin-7.0.0/bin/pmd check -d . -R pmd-ruleset.xml -f html -r pmd-report.html
```

## 🔧 Configuration

### Semgrep
- Uses auto-configuration (community rules)
- Customize by creating `.semgrep.yml` in repository root

### SpotBugs
- Configuration: `project/plugins.sbt`
- Customize rules by adding `spotbugs-exclude.xml`

### PMD
- Ruleset: `pmd-ruleset.xml` (auto-generated in workflow)
- Modify the workflow file to customize rules

## 📈 Recommended Workflow

1. **Start with SAST Scan** - Comprehensive security + dependency analysis (runs weekly)
2. **Review Semgrep** - Quick feedback on security issues (runs on every push)
3. **Check SpotBugs** - Deep dive into bytecode-level bugs
4. **Review PMD** - Address code quality and maintainability issues
5. **Review Dependency Scan** - Check for vulnerable dependencies and license issues

### Prioritization Guide:
- 🔴 **Critical**: CVEs in dependencies (SAST Scan dep-scan)
- 🔴 **High**: Security vulnerabilities in code (SAST Scan, Semgrep, SpotBugs)
- 🟡 **Medium**: Bugs and error-prone code (SpotBugs, PMD error-prone)
- 🟢 **Low**: Code smells and style issues (PMD code style)
- 📋 **Info**: License compliance (SAST Scan)

## 🛡️ Benefits

- **Early Detection**: Catches vulnerabilities before they reach production
- **Automated**: Runs automatically on every code change
- **Comprehensive**: Four complementary tools cover all security aspects
  - SAST (Static Application Security Testing)
  - SCA (Software Composition Analysis - dependencies)
  - Code Quality & Maintainability
  - License Compliance
- **GitHub Integration**: Results appear in Security tab and PR checks
- **Zero Cost**: All tools are free and open-source
- **CI-Friendly**: No external servers or infrastructure required

## 📝 Notes

- These scans complement (not replace) Veracode or other commercial SAST tools
- False positives may occur - review findings carefully
- Customize rulesets based on your security requirements
- Consider adding these checks as required status checks for PRs

## 🔗 Resources

- [SAST Scan (AppThreat) Documentation](https://slscan.io/)
- [SAST Scan GitHub Action](https://github.com/marketplace/actions/sast-scan)
- [Dependency Scan (AppThreat)](https://github.com/AppThreat/dep-scan)
- [Semgrep Documentation](https://semgrep.dev/docs/)
- [SpotBugs Documentation](https://spotbugs.github.io/)
- [PMD Documentation](https://pmd.github.io/)

## 🆕 What's New

**Latest Addition: SAST Scan (ShiftLeft/AppThreat)**
- All-in-one security scanning solution
- Includes SAST, SCA (dependency scanning), and license checking
- No server infrastructure required
- Perfect for CI/CD pipelines
- Runs weekly to catch new vulnerabilities in dependencies

