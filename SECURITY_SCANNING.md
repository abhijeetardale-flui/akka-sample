# Security Scanning Setup

This repository includes automated security and code quality scanning using three complementary tools.

## 🔍 Scanning Tools

### 1. **Semgrep** - Fast Static Analysis
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

1. **Start with Semgrep** - Quick feedback on security issues
2. **Review SpotBugs** - Deep dive into bytecode-level bugs
3. **Check PMD** - Address code quality and maintainability issues
4. **Prioritize**:
   - 🔴 High: Security vulnerabilities (Semgrep, SpotBugs security rules)
   - 🟡 Medium: Bugs and error-prone code (SpotBugs, PMD error-prone)
   - 🟢 Low: Code smells and style issues (PMD code style)

## 🛡️ Benefits

- **Early Detection**: Catches vulnerabilities before they reach production
- **Automated**: Runs automatically on every code change
- **Comprehensive**: Three complementary tools cover different aspects
- **GitHub Integration**: Results appear in Security tab and PR checks
- **Zero Cost**: All tools are free and open-source

## 📝 Notes

- These scans complement (not replace) Veracode or other commercial SAST tools
- False positives may occur - review findings carefully
- Customize rulesets based on your security requirements
- Consider adding these checks as required status checks for PRs

## 🔗 Resources

- [Semgrep Documentation](https://semgrep.dev/docs/)
- [SpotBugs Documentation](https://spotbugs.github.io/)
- [PMD Documentation](https://pmd.github.io/)

