#!/usr/bin/env python3
"""Synchronize human-facing references and SKILL.md from styles/registry.json."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


TABLE_HEADER = "| Style ID | 风格名称 | 核心视觉特征 | 推荐场景 |"
TABLE_ALIGN = "|---|---|---|---|"
TABLE_PATTERN = re.compile(
    r"(\| Style ID \| 风格名称 \| 核心视觉特征 \| 推荐场景 \|\n\|---\|---\|---\|---\|\n(?:\| \*\*`[^`]+`\*\* \|[^\n]*\n)+)",
    re.MULTILINE,
)


def load_registry(registry_path: Path) -> list[dict[str, Any]]:
    if not registry_path.is_file():
        raise FileNotFoundError(f"Registry file not found: {registry_path}")
    payload = json.loads(registry_path.read_text(encoding="utf-8"))
    styles = payload.get("styles", [])
    if not isinstance(styles, list) or not styles:
        raise ValueError("Registry must contain a non-empty 'styles' array.")
    return styles


def generate_skill_table(styles: list[dict[str, Any]]) -> str:
    lines = [TABLE_HEADER, TABLE_ALIGN]
    for style in styles:
        style_id = style.get("id", "").strip()
        name = style.get("name", "").strip()
        traits = style.get("visualTraits", "").strip()
        scenarios = style.get("scenarios", "").strip()
        if not style_id or not name:
            raise ValueError(f"Style entry missing required id or name: {style}")
        lines.append(f"| **`{style_id}`** | **{name}** | {traits} | {scenarios} |")
    return "\n".join(lines) + "\n"


def sync_skill_file(skill_path: Path, table_content: str, check_only: bool = False) -> tuple[bool, str]:
    if not skill_path.is_file():
        return False, f"SKILL.md not found at {skill_path}"

    content = skill_path.read_text(encoding="utf-8")
    match = TABLE_PATTERN.search(content)
    if not match:
        return False, "Could not locate style registry table in SKILL.md"

    current_table = match.group(1)
    if current_table == table_content:
        return True, "SKILL.md is already in sync with registry.json"

    if check_only:
        return False, "SKILL.md style table differs from registry.json (run sync_registry.py to update)"

    new_content = content[: match.start(1)] + table_content + content[match.end(1) :]
    skill_path.write_text(new_content, encoding="utf-8")
    return True, "Successfully updated style table in SKILL.md"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, help="repository root; defaults to project root of script")
    parser.add_argument("--check", action="store_true", help="check synchronization without writing changes")
    args = parser.parse_args()

    root = (args.project_root or Path(__file__).resolve().parents[2]).resolve()
    registry_path = root / "references" / "styles" / "registry.json"
    skill_path = root / "SKILL.md"

    try:
        styles = load_registry(registry_path)
        table_content = generate_skill_table(styles)
        success, message = sync_skill_file(skill_path, table_content, check_only=args.check)

        if not success:
            print(f"❌ {message}", file=sys.stderr)
            return 1

        prefix = "✅ Check passed:" if args.check else "✅ Sync complete:"
        print(f"{prefix} {message} ({len(styles)} styles)")
        return 0

    except Exception as exc:
        print(f"❌ Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
