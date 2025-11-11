import json
import os
import re

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

print("=" * 80)
print("TRANSITIVE DEPENDENCY VULNERABILITY ANALYSIS")
print("=" * 80)

trivy = load_json('scan-results/trivy-full.json')

# Track vulnerabilities by package
vulnerabilities = {}

if 'Results' in trivy:
    for result in trivy['Results']:
        target = result.get('Target', 'Unknown')
        print(f"\n📦 Analyzing: {target}")
        
        for vuln in result.get('Vulnerabilities', []):
            if vuln.get('Severity') in ['CRITICAL', 'HIGH']:
                pkg_name = vuln.get('PkgName', 'Unknown')
                current_ver = vuln.get('InstalledVersion', 'Unknown')
                fixed_ver = vuln.get('FixedVersion', '')
                cve = vuln.get('VulnerabilityID', 'N/A')
                severity = vuln.get('Severity', 'Unknown')
                
                print(f"  🔴 [{severity}] {pkg_name}:{current_ver}")
                print(f"     CVE: {cve}")
                print(f"     Fix: {fixed_ver}")
                
                # Maven coordinates
                if ':' in pkg_name:
                    parts = pkg_name.split(':')
                    if len(parts) >= 2:
                        group_id = parts[0]
                        artifact_id = parts[1]
                    else:
                        group_id = pkg_name
                        artifact_id = pkg_name
                else:
                    # Try common Maven group IDs for known packages
                    artifact_id = pkg_name
                    if pkg_name.startswith('logback'):
                        group_id = 'ch.qos.logback'
                    elif pkg_name.startswith('jackson'):
                        group_id = 'com.fasterxml.jackson.core'
                    elif pkg_name.startswith('akka'):
                        group_id = 'com.typesafe.akka'
                    else:
                        group_id = pkg_name
                
                key = f"{group_id}:{artifact_id}"
                if key not in vulnerabilities or fixed_ver:
                    vulnerabilities[key] = {
                        'groupId': group_id,
                        'artifactId': artifact_id,
                        'currentVersion': current_ver,
                        'fixedVersion': fixed_ver if fixed_ver else current_ver,
                        'cve': cve,
                        'severity': severity,
                        'target': target
                    }

# Save identified vulnerabilities
with open('fixes/transitive-vulns.json', 'w') as f:
    json.dump(list(vulnerabilities.values()), f, indent=2)

print("\n" + "=" * 80)
print(f"✅ Found {len(vulnerabilities)} unique vulnerable dependencies")
print("=" * 80)

# Set output
with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write(f"vuln_count={len(vulnerabilities)}\n")
    f.write(f"has_vulns={'true' if len(vulnerabilities) > 0 else 'false'}\n")
