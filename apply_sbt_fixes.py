import json
import os

# Load vulnerabilities
with open('fixes/transitive-vulns.json') as f:
    vulns = json.load(f)

# Check if root build.sbt exists
if os.path.exists('build.sbt'):
    with open('build.sbt', 'r') as f:
        content = f.read()
    
    # Check if dependencyOverrides already exists
    if 'dependencyOverrides' not in content:
        # Add dependencyOverrides section
        overrides = '\n// Security: Override vulnerable transitive dependencies\n'
        overrides += 'ThisBuild / dependencyOverrides ++= Seq(\n'
        
        for vuln in vulns:
            if vuln['fixedVersion'] and vuln['fixedVersion'] != 'Not available':
                group_id = vuln['groupId']
                artifact_id = vuln['artifactId']
                version = vuln['fixedVersion']
                overrides += f'  "{group_id}" % "{artifact_id}" % "{version}",  // {vuln["cve"]}\n'
        
        overrides += ')\n'
        
        with open('build.sbt', 'a') as f:
            f.write(overrides)
        
        print("✅ Added dependencyOverrides to build.sbt")
    else:
        print("ℹ️ dependencyOverrides already exists in build.sbt")
else:
    print("ℹ️ No root build.sbt file found")
