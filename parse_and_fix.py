import json
import os
from collections import defaultdict

# Load scan results
def load_json_safe(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Could not load {filepath}: {e}")
        return {}

trivy_data = load_json_safe('scan-results/trivy-sca.json')
semgrep_data = load_json_safe('scan-results/semgrep-sast.json')

critical_high_issues = []
fixes_to_apply = []

# Parse Trivy SCA results (CRITICAL/HIGH only)
print("📊 Parsing SCA (Software Composition Analysis) results...")
sca_count = 0
if 'Results' in trivy_data:
    for result in trivy_data.get('Results', []):
        for vuln in result.get('Vulnerabilities', []):
            severity = vuln.get('Severity', 'UNKNOWN')
            if severity in ['CRITICAL', 'HIGH']:
                sca_count += 1
                pkg_name = vuln.get('PkgName', 'Unknown')
                current_version = vuln.get('InstalledVersion', 'Unknown')
                fixed_version = vuln.get('FixedVersion', '')
                
                issue = {
                    'type': 'SCA',
                    'severity': severity,
                    'cve': vuln.get('VulnerabilityID', 'N/A'),
                    'package': pkg_name,
                    'current_version': current_version,
                    'fixed_version': fixed_version,
                    'title': vuln.get('Title', 'No title'),
                    'description': vuln.get('Description', 'No description')[:200]
                }
                critical_high_issues.append(issue)
                
                # Generate fix if version available
                if fixed_version and fixed_version != 'Not available':
                    fixes_to_apply.append({
                        'type': 'dependency_update',
                        'package': pkg_name,
                        'from_version': current_version,
                        'to_version': fixed_version,
                        'severity': severity,
                        'cve': vuln.get('VulnerabilityID', 'N/A')
                    })

print(f"✅ SCA: Found {sca_count} CRITICAL/HIGH vulnerabilities")

# Parse Semgrep SAST results (ERROR/WARNING = HIGH/MEDIUM)
print("📊 Parsing SAST (Static Application Security Testing) results...")
sast_count = 0
if 'results' in semgrep_data:
    for result in semgrep_data.get('results', []):
        severity_str = result.get('extra', {}).get('severity', 'INFO')
        # Map ERROR -> HIGH, WARNING -> MEDIUM
        severity = 'HIGH' if severity_str == 'ERROR' else ('MEDIUM' if severity_str == 'WARNING' else 'LOW')
        
        if severity in ['HIGH']:  # Only HIGH for SAST (Semgrep ERROR)
            sast_count += 1
            issue = {
                'type': 'SAST',
                'severity': severity,
                'cve': result.get('check_id', 'N/A'),
                'file': result.get('path', 'Unknown'),
                'line': result.get('start', {}).get('line', 'N/A'),
                'title': result.get('extra', {}).get('message', 'Security issue detected')[:100],
                'description': result.get('extra', {}).get('metadata', {}).get('description', 'No description')[:200]
            }
            critical_high_issues.append(issue)

print(f"✅ SAST: Found {sast_count} HIGH severity issues")

# Save results
with open('pr-fixes/issues.json', 'w') as f:
    json.dump(critical_high_issues, f, indent=2)

with open('pr-fixes/fixes.json', 'w') as f:
    json.dump(fixes_to_apply, f, indent=2)

# Summary
total_issues = len(critical_high_issues)
total_fixes = len(fixes_to_apply)

print(f"\n📊 SUMMARY:")
print(f"   Total CRITICAL/HIGH Issues: {total_issues}")
print(f"   - SCA (Dependencies): {sca_count}")
print(f"   - SAST (Code): {sast_count}")
print(f"   Auto-fixable: {total_fixes}")

# Set output
with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write(f"total_issues={total_issues}\n")
    f.write(f"sca_count={sca_count}\n")
    f.write(f"sast_count={sast_count}\n")
    f.write(f"fixable_count={total_fixes}\n")
    f.write(f"has_issues={'true' if total_issues > 0 else 'false'}\n")
