import json
import re
import subprocess
from pathlib import Path


def load_fixes(path: Path):
    if not path.exists():
        print("ℹ️ No fixes.json file found")
        return []
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def update_pom_files(fixes, pom_files):
    changes = 0
    for fix in fixes:
        pkg = fix["package"]
        from_ver = fix["from_version"]
        to_ver = fix["to_version"]
        group = pkg.split(":")[0] if ":" in pkg else pkg
        artifact = pkg.split(":")[1] if ":" in pkg else pkg

        for pom in pom_files:
            if not pom:
                continue
            path = Path(pom)
            try:
                content = path.read_text(encoding="utf-8")
            except FileNotFoundError:
                continue

            original = content
            content = content.replace(
                f"<{pkg}.version>{from_ver}</{pkg}.version>",
                f"<{pkg}.version>{to_ver}</{pkg}.version>",
            )

            pattern = re.compile(
                rf"<groupId>{re.escape(group)}</groupId>\s*<artifactId>{re.escape(artifact)}</artifactId>\s*<version>{re.escape(from_ver)}</version>"
            )
            content = pattern.sub(
                lambda _: f"<groupId>{group}</groupId><artifactId>{artifact}</artifactId><version>{to_ver}</version>",
                content,
            )

            content = content.replace(f"<version>{from_ver}</version>", f"<version>{to_ver}</version>")

            if content != original:
                path.write_text(content, encoding="utf-8")
                print(f"   ✅ Updated {path}")
                changes += 1
    return changes


def update_sbt_files(fixes, sbt_files):
    changes = 0
    for fix in fixes:
        pkg = fix["package"]
        from_ver = fix["from_version"]
        to_ver = fix["to_version"]
        group = pkg.split(":")[0] if ":" in pkg else pkg
        artifact = pkg.split(":")[1] if ":" in pkg else pkg

        for sbt in sbt_files:
            if not sbt:
                continue
            path = Path(sbt)
            try:
                content = path.read_text(encoding="utf-8")
            except FileNotFoundError:
                continue

            original = content
            lines = content.splitlines()
            updated_lines = []
            local_change = False

            for line in lines:
                updated_line = line
                if (
                    f'"{group}"' in line
                    and f'"{artifact}"' in line
                    and f'"{from_ver}"' in line
                ):
                    updated_line = line.replace(f'"{from_ver}"', f'"{to_ver}"')
                    if updated_line != line:
                        local_change = True
                updated_lines.append(updated_line)

            if not local_change and pkg in content and f'"{from_ver}"' in content:
                temp_lines = []
                for line in updated_lines:
                    updated_line = line
                    if pkg in line and f'"{from_ver}"' in line:
                        updated_line = line.replace(f'"{from_ver}"', f'"{to_ver}"')
                    if updated_line != line:
                        local_change = True
                    temp_lines.append(updated_line)
                updated_lines = temp_lines

            if local_change:
                new_content = "\n".join(updated_lines)
                path.write_text(new_content, encoding="utf-8")
                print(f"   ✅ Updated {path}")
                changes += 1
    return changes


def main():
    fixes_path = Path("pr-fixes/fixes.json")
    fixes = load_fixes(fixes_path)

    if not fixes:
        print("ℹ️ No dependency fixes to apply")
        return

    pom_files = (
        subprocess.run(
            ["find", ".", "-name", "pom.xml", "-type", "f"],
            capture_output=True,
            text=True,
            check=False,
        )
        .stdout.strip()
        .split("\n")
    )

    sbt_files = (
        subprocess.run(
            ["find", ".", "-name", "build.sbt", "-type", "f"],
            capture_output=True,
            text=True,
            check=False,
        )
        .stdout.strip()
        .split("\n")
    )

    print(f"🔧 Applying {len(fixes)} dependency updates...")
    pom_changes = update_pom_files(fixes, pom_files)
    sbt_changes = update_sbt_files(fixes, sbt_files)
    print(f"Total updated files: {pom_changes + sbt_changes}")


if __name__ == "__main__":
    main()
