#!/usr/bin/env python3
"""Check that the style registry and human-facing references stay aligned."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


STYLE_ID_RE = re.compile(r"^\| \*\*`([^`]+)`\*\*")
THEME_ID_RE = re.compile(r"^\| \*\*`([^`]+)`\*\* \|")


def ids_from_file(path: Path, pattern: re.Pattern[str]) -> list[str]:
    if not path.is_file():
        return []
    return [match.group(1) for line in path.read_text(encoding="utf-8").splitlines() if (match := pattern.search(line))]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, help="repository root; defaults to the script parent")
    args = parser.parse_args()
    root = (args.project_root or Path(__file__).resolve().parents[2]).resolve()
    references = root / "references"
    styles_root = references / "styles"
    registry_path = styles_root / "registry.json"
    errors: list[str] = []

    if not registry_path.is_file():
        print(f"registry validation failed: missing {registry_path}", file=sys.stderr)
        return 1
    try:
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
    except Exception as error:
        print(f"registry validation failed: {error}", file=sys.stderr)
        return 1

    entries = payload.get("styles") if isinstance(payload, dict) else None
    if not isinstance(entries, list) or not entries:
        errors.append("registry styles must be a non-empty array")
        entries = []

    registry_ids: list[str] = []
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append(f"registry entry is not an object: {entry!r}")
            continue
        style_id = entry.get("id")
        style_dir = entry.get("dir")
        name = entry.get("name")
        categories = entry.get("categories")
        if not isinstance(style_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", style_id):
            errors.append(f"invalid style id: {style_id!r}")
            continue
        if style_id in registry_ids:
            errors.append(f"duplicate style id: {style_id}")
        registry_ids.append(style_id)
        if not isinstance(style_dir, str) or Path(style_dir).name != style_dir:
            errors.append(f"{style_id}: invalid style directory")
            continue
        if not isinstance(name, str) or not name:
            errors.append(f"{style_id}: missing display name")
        if not isinstance(categories, list) or not categories or not all(isinstance(category, str) and category for category in categories):
            errors.append(f"{style_id}: categories must be a non-empty string array")
        style_path = styles_root / style_dir
        for required in ("design.md", "scaffold-web.html", "scaffold-ppt.html", "preview.svg", "preview.png"):
            if not (style_path / required).is_file():
                errors.append(f"{style_id}: missing {required}")

    actual_dirs = sorted(path.name for path in styles_root.iterdir() if path.is_dir() and not path.name.startswith("."))
    if sorted(registry_ids) != actual_dirs:
        missing = sorted(set(actual_dirs) - set(registry_ids))
        orphaned = sorted(set(registry_ids) - set(actual_dirs))
        if missing:
            errors.append("unregistered style directories: " + ", ".join(missing))
        if orphaned:
            errors.append("registry entries without directories: " + ", ".join(orphaned))

    skill_ids = ids_from_file(root / "SKILL.md", STYLE_ID_RE)
    theme_ids = ids_from_file(references / "shared-components.md", THEME_ID_RE)
    for label, actual in (("SKILL.md", skill_ids), ("Mermaid theme table", theme_ids)):
        if set(actual) != set(registry_ids):
            errors.append(f"{label} IDs do not match registry content")

    if errors:
        print("❌ Registry validation failed")
        for error in errors:
            print(f"   - {error}")
        return 1

    print(f"✅ Registry validated: {len(registry_ids)} styles, resources and references aligned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
