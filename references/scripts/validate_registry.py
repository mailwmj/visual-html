#!/usr/bin/env python3
"""Check that the style registry, style packs, and human-facing references stay aligned."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from sync_registry import generate_skill_table, sync_skill_file


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, help="repository root; defaults to project root of script")
    args = parser.parse_args()
    root = (args.project_root or Path(__file__).resolve().parents[2]).resolve()
    references = root / "references"
    styles_root = references / "styles"
    registry_path = styles_root / "registry.json"
    skill_path = root / "SKILL.md"
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
        english_name = entry.get("englishName")
        categories = entry.get("categories")
        visual_traits = entry.get("visualTraits")
        scenarios = entry.get("scenarios")

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
        if not isinstance(english_name, str) or not english_name:
            errors.append(f"{style_id}: missing englishName")
        if not isinstance(categories, list) or not categories or not all(isinstance(c, str) and c for c in categories):
            errors.append(f"{style_id}: categories must be a non-empty string array")
        if not isinstance(visual_traits, str) or not visual_traits.strip():
            errors.append(f"{style_id}: missing visualTraits description")
        if not isinstance(scenarios, str) or not scenarios.strip():
            errors.append(f"{style_id}: missing scenarios description")

        style_path = styles_root / style_dir
        for required in ("design.md", "scaffold-web.html", "scaffold-ppt.html", "preview.svg", "preview.png"):
            if not (style_path / required).is_file():
                errors.append(f"{style_id}: missing {required}")

        design_md = style_path / "design.md"
        if design_md.is_file():
            design_content = design_md.read_text(encoding="utf-8")
            if "themeVariables" not in design_content:
                errors.append(f"{style_id}: design.md missing Mermaid themeVariables configuration")

    actual_dirs = sorted(path.name for path in styles_root.iterdir() if path.is_dir() and not path.name.startswith("."))
    if sorted(registry_ids) != actual_dirs:
        missing = sorted(set(actual_dirs) - set(registry_ids))
        orphaned = sorted(set(registry_ids) - set(actual_dirs))
        if missing:
            errors.append("unregistered style directories: " + ", ".join(missing))
        if orphaned:
            errors.append("registry entries without directories: " + ", ".join(orphaned))

    # Verify SKILL.md sync
    try:
        table_content = generate_skill_table(entries)
        synced, msg = sync_skill_file(skill_path, table_content, check_only=True)
        if not synced:
            errors.append(f"SKILL.md style table out of sync: {msg}")
    except Exception as exc:
        errors.append(f"Failed to verify SKILL.md table synchronization: {exc}")

    if errors:
        print("❌ Registry validation failed")
        for error in errors:
            print(f"   - {error}")
        return 1

    print(f"✅ Registry validated: {len(registry_ids)} styles, resources and references aligned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
