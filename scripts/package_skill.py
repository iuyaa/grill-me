"""Build or check Grill's text-file manifest. No network or third-party packages."""

import argparse
import hashlib
import json
import re
from pathlib import Path


def package_skill(root, *, check=False, bump_patch=False):
    root = Path(root)
    if check and bump_patch:
        raise ValueError("Cannot check and bump a version together")
    paths = sorted(root.rglob("*"))
    if any(path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()) for path in paths):
        raise ValueError("Package links are not supported")
    skill = root / "SKILL.md"
    content = skill.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not frontmatter or not re.search(r"^name: grill$", frontmatter[1], re.M):
        raise ValueError("Expected Grill frontmatter")
    version = re.search(r'^metadata:\n  version: "(\d+)\.(\d+)\.(\d+)"$', frontmatter[1], re.M)
    if not version:
        raise ValueError("Expected metadata.version with three integer components")
    if bump_patch:
        major, minor, patch = map(int, version.groups())
        start = frontmatter.start(1) + version.start(1)
        end = frontmatter.start(1) + version.end(3)
        content = content[:start] + f"{major}.{minor}.{patch + 1}" + content[end:]

    manifest = {}
    for path in paths:
        if not path.is_file() or path == root / "manifest.json":
            continue
        text = content if path == skill else path.read_text(encoding="utf-8")
        manifest[path.relative_to(root).as_posix()] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    payload = {"files": manifest}
    target = root / "manifest.json"
    if check:
        if not target.is_file() or json.loads(target.read_text(encoding="utf-8")) != payload:
            raise ValueError("Manifest differs from package; preserve local edits or regenerate before release")
    else:
        if bump_patch:
            skill.write_text(content, encoding="utf-8", newline="\n")
        target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    return len(manifest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--bump-patch", action="store_true")
    args = parser.parse_args()
    try:
        count = package_skill(Path(__file__).resolve().parents[1] / "grill", **vars(args))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Package check failed: {error}\n")
    print(f"{'Verified' if args.check else 'Generated'} manifest for {count} files.")


if __name__ == "__main__":
    main()
