import json
import xml.etree.ElementTree as ET
import os

# Load vulnerabilities
with open('fixes/transitive-vulns.json') as f:
    vulns = json.load(f)

print("=" * 80)
print("APPLYING DEPENDENCY MANAGEMENT FIXES")
print("=" * 80)

# Process each pom.xml
import glob
pom_files = glob.glob('**/pom.xml', recursive=True)
pom_files = [p for p in pom_files if 'target' not in p]

for pom_path in pom_files:
    print(f"\n📝 Processing: {pom_path}")
    
    try:
        # Read pom.xml
        with open(pom_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Register namespaces to preserve them
        ET.register_namespace('', 'http://maven.apache.org/POM/4.0.0')
        ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        
        tree = ET.parse(pom_path)
        root = tree.getroot()
        
        # Maven namespace
        ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}
        
        # Find or create dependencyManagement section
        dep_mgmt = root.find('maven:dependencyManagement', ns)
        if dep_mgmt is None:
            # Create new dependencyManagement section
            dep_mgmt = ET.SubElement(root, '{http://maven.apache.org/POM/4.0.0}dependencyManagement')
            dependencies = ET.SubElement(dep_mgmt, '{http://maven.apache.org/POM/4.0.0}dependencies')
            print("  ✅ Created new dependencyManagement section")
        else:
            dependencies = dep_mgmt.find('maven:dependencies', ns)
            if dependencies is None:
                dependencies = ET.SubElement(dep_mgmt, '{http://maven.apache.org/POM/4.0.0}dependencies')
        
        # Add/update dependencies
        added_count = 0
        for vuln in vulns:
            group_id = vuln['groupId']
            artifact_id = vuln['artifactId']
            fixed_version = vuln['fixedVersion']
            
            if not fixed_version or fixed_version == 'Not available':
                continue
            
            # Check if dependency already exists
            existing = dependencies.findall('maven:dependency', ns)
            found = False
            
            for dep in existing:
                g = dep.find('maven:groupId', ns)
                a = dep.find('maven:artifactId', ns)
                if g is not None and a is not None:
                    if g.text == group_id and a.text == artifact_id:
                        # Update version
                        v = dep.find('maven:version', ns)
                        if v is not None:
                            v.text = fixed_version
                        else:
                            v = ET.SubElement(dep, '{http://maven.apache.org/POM/4.0.0}version')
                            v.text = fixed_version
                        found = True
                        print(f"  ✅ Updated: {group_id}:{artifact_id} → {fixed_version}")
                        added_count += 1
                        break
            
            if not found:
                # Add new dependency
                dep = ET.SubElement(dependencies, '{http://maven.apache.org/POM/4.0.0}dependency')
                g = ET.SubElement(dep, '{http://maven.apache.org/POM/4.0.0}groupId')
                g.text = group_id
                a = ET.SubElement(dep, '{http://maven.apache.org/POM/4.0.0}artifactId')
                a.text = artifact_id
                v = ET.SubElement(dep, '{http://maven.apache.org/POM/4.0.0}version')
                v.text = fixed_version
                print(f"  ✅ Added: {group_id}:{artifact_id}:{fixed_version}")
                added_count += 1
        
        if added_count > 0:
            # Write back with proper formatting
            tree.write(pom_path, encoding='utf-8', xml_declaration=True)
            
            # Fix formatting (ElementTree doesn't preserve nice formatting)
            with open(pom_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add XML declaration if missing
            if not content.startswith('<?xml'):
                content = '<?xml version="1.0" encoding="UTF-8"?>\n' + content
            
            with open(pom_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  💾 Saved changes ({added_count} dependencies managed)")
        
    except Exception as e:
        print(f"  ⚠️ Error processing {pom_path}: {e}")

print("\n" + "=" * 80)
print("✅ Dependency management applied to all pom.xml files")
print("=" * 80)
