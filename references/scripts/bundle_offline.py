#!/usr/bin/env python3
"""Create a self-contained, offline-capable HTML delivery from a scaffold.

The default output is hybrid: local assets are embedded, while online-only
fonts and Mermaid are optional enhancements.  A browser that cannot load them
keeps the system font stack and the generated static SVG flowchart.

Use --strict to remove those optional network enhancements as well.
"""

from __future__ import annotations

import argparse
import base64
import html as html_module
import json
import mimetypes
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


MERMAID_IMPORT = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs"
RESOURCE_TAGS = ("img", "source", "video", "audio", "input", "script", "link", "use")
RESOURCE_ATTRS = ("src", "href", "poster")


def data_url_bytes(name: str, content: bytes) -> str:
    mime = mimetypes.guess_type(name)[0] or "application/octet-stream"
    encoded = base64.b64encode(content).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def data_url(path: Path) -> str:
    return data_url_bytes(path.name, path.read_bytes())


def is_remote(value: str) -> bool:
    parsed = urlparse(value)
    return value.startswith("//") or parsed.scheme in {"http", "https"}


def is_ignorable_resource(value: str) -> bool:
    return not value or value.startswith(("data:", "#", "%23", "mailto:", "javascript:"))


def resolve_local(value: str, base_dir: Path) -> Path:
    parsed = urlparse(value)
    clean = parsed.path
    return (base_dir / clean).resolve()


def replace_external_font_links(source: str, strict: bool) -> str:
    if not strict:
        return source
    pattern = re.compile(r"\s*<link\b[^>]*?(?:fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*?/?>", re.I)
    source = pattern.sub("", source)
    return re.sub(r"@import\s+url\(\s*['\"]?https?://fonts\.[^)\s'\"]+[^)]*\)\s*;?", "", source, flags=re.I)


def inline_css_urls(source: str, base_dir: Path, strict: bool, warnings: list[str]) -> str:
    if strict:
        import_match = re.search(
            r"@import\s+(?:url\(\s*)?['\"]?((?:https?:)?//[^'\"\s)]+)", source, flags=re.I
        )
        if import_match:
            raise ValueError(f"external CSS resource remains: {import_match.group(1)}")

    css_pattern = re.compile(r"url\(\s*(['\"]?)([^)'\"]+)\1\s*\)", re.I)

    def replace_css(match: re.Match[str]) -> str:
        value = match.group(2).strip()
        if is_ignorable_resource(value):
            return match.group(0)
        if is_remote(value):
            if strict:
                raise ValueError(f"external CSS resource remains: {value}")
            return match.group(0)
        path = resolve_local(value, base_dir)
        if not path.is_file():
            message = f"missing local CSS resource: {value} (resolved to {path})"
            if strict:
                raise ValueError(message)
            warnings.append(message)
            return match.group(0)
        return f"url('{data_url(path)}')"

    return css_pattern.sub(replace_css, source)


def inline_local_resources(source: str, base_dir: Path, strict: bool, warnings: list[str]) -> str:
    tag_pattern = "|".join(RESOURCE_TAGS)
    attr_pattern = "|".join(RESOURCE_ATTRS)
    pattern = re.compile(
        rf"(?P<open><(?P<tag>{tag_pattern})\b(?P<body>[^>]*?)\b(?P<attr>{attr_pattern})\s*=\s*)(?P<quote>['\"])(?P<value>.*?)(?P=quote)",
        re.I | re.S,
    )

    def replace(match: re.Match[str]) -> str:
        value = match.group("value").strip()
        if is_ignorable_resource(value):
            return match.group(0)
        if is_remote(value):
            if strict:
                raise ValueError(f"external resource remains: {value}")
            return match.group(0)

        path = resolve_local(value, base_dir)
        if not path.is_file():
            message = f"missing local resource: {value} (resolved to {path})"
            if strict:
                raise ValueError(message)
            warnings.append(message)
            return match.group(0)
        if path.suffix.lower() == ".css":
            css_source = path.read_text(encoding="utf-8")
            css_source = inline_css_urls(css_source, path.parent, strict, warnings)
            replacement = data_url_bytes(path.name, css_source.encode("utf-8"))
        else:
            replacement = data_url(path)
        prefix = match.group("open")
        quote = match.group("quote")
        return f"{prefix}{quote}{replacement}{quote}"

    source = pattern.sub(replace, source)
    return inline_css_urls(source, base_dir, strict, warnings)


def parse_font_map(font_map_path: Path) -> str:
    payload = json.loads(font_map_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("font map must be a JSON object keyed by family name")

    declarations: list[str] = []
    for family, entries in payload.items():
        if isinstance(entries, dict):
            entries = [entries]
        if not isinstance(entries, list):
            raise ValueError(f"font map entry for {family!r} must be an object or array")
        for entry in entries:
            if isinstance(entry, str):
                entry = {"path": entry}
            if not isinstance(entry, dict) or not entry.get("path"):
                raise ValueError(f"font map entry for {family!r} is missing path")
            font_path = (font_map_path.parent / str(entry["path"])).resolve()
            if not font_path.is_file():
                raise ValueError(f"font file not found: {font_path}")
            weight = entry.get("weight", 400)
            style = entry.get("style", "normal")
            fmt = "woff2" if font_path.suffix.lower() == ".woff2" else font_path.suffix.lower().lstrip(".")
            declarations.append(
                "@font-face {"
                f"font-family: {json.dumps(str(family))};"
                f"font-style: {style};"
                f"font-weight: {weight};"
                f"font-display: swap;"
                f"src: url('{data_url(font_path)}') format('{fmt}');"
                "}"
            )
    return "\n".join(declarations)


def strip_mermaid_markup(label: str) -> list[str]:
    label = re.sub(r"<br\s*/?>", "\n", label, flags=re.I)
    label = re.sub(r"<[^>]+>", "", label)
    label = html_module.unescape(label).strip().strip('"')
    return [line.strip() for line in label.splitlines() if line.strip()] or ["Node"]


def parse_endpoint(token: str) -> tuple[str, list[str]] | None:
    token = token.strip()
    match = re.match(r"^([A-Za-z][\w-]*)\s*(?:\[([^]]*)\]|\{([^}]*)\}|\(([^)]*)\))?$", token)
    if not match:
        return None
    node_id = match.group(1)
    label = next((value for value in match.groups()[1:] if value is not None), node_id)
    return node_id, strip_mermaid_markup(label)


def parse_style_tokens(value: str) -> dict[str, str]:
    value_pattern = r"(?:rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}|[A-Za-z]+)"
    return {key: val for key, val in re.findall(rf"(fill|stroke|color):\s*({value_pattern})", value, flags=re.I)}


def mermaid_svg(source: str, index: int) -> str:
    lines = [line.strip() for line in source.splitlines() if line.strip() and not line.strip().startswith("%%")]
    direction = "LR"
    if lines:
        direction_match = re.match(r"(?:graph|flowchart)\s+(LR|RL|TB|TD|BT)\b", lines[0], flags=re.I)
        if direction_match:
            direction = direction_match.group(1).upper()

    nodes: dict[str, list[str]] = {}
    edges: list[tuple[str, str, str]] = []
    styles: dict[str, dict[str, str]] = {}
    endpoint_pattern = r"[A-Za-z][\w-]*(?:\s*(?:\[[^]]*\]|\{[^}]*\}|\([^)]*\)))?"
    edge_pattern = re.compile(
        rf"^(?P<left>{endpoint_pattern})\s*(?:-->|==>|-\.->)\s*(?P<label>\|[^|]*\|\s*)?(?P<right>{endpoint_pattern})$"
    )

    for line in lines[1:]:
        if line.lower().startswith("style "):
            style_match = re.match(r"style\s+([A-Za-z][\w-]*)\s+(.+)$", line, flags=re.I)
            if style_match:
                styles[style_match.group(1)] = parse_style_tokens(style_match.group(2))
            continue
        edge_match = edge_pattern.match(line)
        if edge_match:
            left = parse_endpoint(edge_match.group("left"))
            right = parse_endpoint(edge_match.group("right"))
            if left and right:
                nodes.setdefault(left[0], left[1])
                nodes.setdefault(right[0], right[1])
                label = edge_match.group("label") or ""
                edges.append((left[0], right[0], label.strip().strip("|").strip()))
            continue
        for node_match in re.finditer(r"([A-Za-z][\w-]*)\s*(\[[^]]*\]|\{[^}]*\}|\([^)]*\))", line):
            parsed = parse_endpoint(node_match.group(0))
            if parsed:
                nodes.setdefault(parsed[0], parsed[1])

    if not nodes:
        return fallback_svg(source, index)

    horizontal = direction in {"LR", "RL"}
    columns = min(4, len(nodes)) if horizontal else 1
    rows = (len(nodes) + columns - 1) // columns
    node_width, node_height = 190, 68
    gap_x, gap_y, padding = 28, 30, 32
    width = padding * 2 + columns * node_width + (columns - 1) * gap_x
    height = padding * 2 + rows * node_height + (rows - 1) * gap_y
    positions: dict[str, tuple[float, float]] = {}
    for offset, node_id in enumerate(nodes):
        row, column = divmod(offset, columns)
        if horizontal:
            x = padding + column * (node_width + gap_x)
            y = padding + row * (node_height + gap_y)
        else:
            x = padding + column * (node_width + gap_x)
            y = padding + row * (node_height + gap_y)
        positions[node_id] = (x, y)

    marker_id = f"offline-arrow-{index}"
    parts = [
        f'<svg class="mermaid-static" role="img" aria-label="Offline static flowchart" viewBox="0 0 {width} {height}" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">',
        f"<title>Offline static flowchart</title>",
        f'<defs><marker id="{marker_id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="currentColor" /></marker></defs>',
    ]

    for left_id, right_id, label in edges:
        x1, y1 = positions[left_id]
        x2, y2 = positions[right_id]
        start_x = x1 + node_width if x2 >= x1 else x1
        end_x = x2 if x2 >= x1 else x2 + node_width
        start_y = y1 + node_height / 2
        end_y = y2 + node_height / 2
        if not horizontal:
            start_x, start_y = x1 + node_width / 2, y1 + node_height
            end_x, end_y = x2 + node_width / 2, y2
        parts.append(
            f'<line x1="{start_x:g}" y1="{start_y:g}" x2="{end_x:g}" y2="{end_y:g}" stroke="currentColor" stroke-opacity=".42" stroke-width="1.5" marker-end="url(#{marker_id})" />'
        )
        if label:
            mid_x, mid_y = (start_x + end_x) / 2, (start_y + end_y) / 2 - 5
            parts.append(f'<text x="{mid_x:g}" y="{mid_y:g}" text-anchor="middle" fill="currentColor" font-size="11">{html_module.escape(label)}</text>')

    for node_id, label_lines in nodes.items():
        x, y = positions[node_id]
        style = styles.get(node_id, {})
        fill = style.get("fill", "currentColor")
        stroke = style.get("stroke", "currentColor")
        color = style.get("color", "currentColor")
        fill_opacity = ".92" if fill != "currentColor" else ".08"
        radius = 12 if "{" not in node_id else 12
        parts.append(f'<rect x="{x:g}" y="{y:g}" width="{node_width}" height="{node_height}" rx="{radius}" fill="{html_module.escape(fill)}" fill-opacity="{fill_opacity}" stroke="{html_module.escape(stroke)}" stroke-width="1.5" />')
        line_start = y + node_height / 2 - (len(label_lines) - 1) * 8
        for line_index, text in enumerate(label_lines[:4]):
            baseline = line_start + line_index * 16 + 5
            parts.append(f'<text x="{x + node_width / 2:g}" y="{baseline:g}" text-anchor="middle" fill="{html_module.escape(color)}" font-size="13" font-family="system-ui, sans-serif">{html_module.escape(text)}</text>')

    parts.append("</svg>")
    return "".join(parts)


def fallback_svg(source: str, index: int) -> str:
    lines = [line.strip() for line in source.splitlines() if line.strip()][:16]
    line_height = 18
    height = max(72, 38 + len(lines) * line_height)
    marker_id = f"offline-fallback-{index}"
    parts = [
        f'<svg class="mermaid-static" role="img" aria-label="Offline diagram source" viewBox="0 0 900 {height}" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">',
        "<title>Offline diagram source</title>",
        '<rect x="1" y="1" width="898" height="%d" rx="12" fill="currentColor" fill-opacity=".06" stroke="currentColor" stroke-opacity=".4" />' % (height - 2),
    ]
    for line_index, line in enumerate(lines):
        parts.append(f'<text x="18" y="{30 + line_index * line_height}" fill="currentColor" font-size="13" font-family="ui-monospace, monospace">{html_module.escape(line)}</text>')
    parts.append("</svg>")
    return "".join(parts)


def replace_mermaid_blocks(source: str, strict: bool) -> tuple[str, int]:
    pattern = re.compile(r'<pre\b(?=[^>]*\bclass=["\'][^"\']*\bmermaid\b[^"\']*["\'])[^>]*>(.*?)</pre>', re.I | re.S)
    counter = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        raw = html_module.unescape(match.group(1)).strip()
        static = mermaid_svg(raw, counter)
        source_block = "" if strict else f'<pre class="mermaid mermaid-source" hidden>{html_module.escape(raw)}</pre>'
        return f'<div class="mermaid-hybrid" data-offline-fallback="true"><div class="mermaid-static-wrap">{static}</div>{source_block}</div>'

    return pattern.sub(replace, source), counter


def remove_mermaid_scripts(source: str) -> str:
    pattern = re.compile(r"<script\b[^>]*>.*?</script>", re.I | re.S)

    def replace(match: re.Match[str]) -> str:
        block = match.group(0)
        if re.search(r"(?:import\s+mermaid|mermaid\.initialize|mermaidElements|mermaid\.run)", block, flags=re.I):
            return ""
        return block

    return pattern.sub(replace, source)


def extract_mermaid_theme(source: str) -> str:
    matches = re.findall(r"themeVariables\s*:\s*\{([^{}]*)\}", source, flags=re.I | re.S)
    if not matches:
        return "{}"
    return "{" + matches[-1].strip() + "}"


def hybrid_runtime(count: int, strict: bool, theme_variables: str) -> str:
    if strict or count == 0:
        return ""
    return f"""
<script>
(() => {{
  const blocks = [...document.querySelectorAll('.mermaid-hybrid')];
  if (!blocks.length || navigator.onLine === false) return;
  import({json.dumps(MERMAID_IMPORT)})
    .then(module => {{
      const mermaid = module.default || module;
      mermaid.initialize({{ startOnLoad: false, theme: 'base', themeVariables: {theme_variables} }});
      return Promise.all(blocks.map(async block => {{
        const source = block.querySelector('.mermaid-source');
        if (!source) return;
        source.hidden = false;
        source.classList.remove('mermaid-source');
        await mermaid.run({{ nodes: [source] }});
        block.querySelector('.mermaid-static-wrap')?.remove();
      }}));
    }})
    .catch(() => {{ /* Keep the deterministic SVG fallback when offline or blocked. */ }});
}})();
</script>"""


def inject_font_css(source: str, font_css: str) -> str:
    if not font_css:
        return source
    block = f"<style data-visual-html-fonts>\n{font_css}\n</style>"
    return re.sub(r"</head>", f"{block}\n</head>", source, count=1, flags=re.I)


def inject_offline_css(source: str) -> str:
    block = """
<style data-visual-html-offline>
  .mermaid-hybrid { display: block; width: 100%; }
  .mermaid-static-wrap { display: block; width: 100%; overflow-x: auto; }
  .mermaid-static { display: block; width: 100%; height: auto; min-height: 120px; }
  .mermaid-source[hidden] { display: none !important; }
</style>"""
    return re.sub(r"</head>", f"{block}\n</head>", source, count=1, flags=re.I)


def bundle(input_path: Path, output_path: Path | None, strict: bool, font_map: Path | None, check: bool) -> int:
    source = input_path.read_text(encoding="utf-8")
    warnings: list[str] = []
    theme_variables = extract_mermaid_theme(source)
    source = replace_external_font_links(source, strict)
    source = remove_mermaid_scripts(source)
    source, mermaid_count = replace_mermaid_blocks(source, strict)
    source = inline_local_resources(source, input_path.parent, strict, warnings)
    source = inject_offline_css(source)
    if font_map:
        source = inject_font_css(source, parse_font_map(font_map))
    source = source.replace("</body>", f"{hybrid_runtime(mermaid_count, strict, theme_variables)}\n</body>", 1)
    marker = f'<meta name="visual-html-offline-bundle" content="{"strict" if strict else "hybrid"}-v1" />'
    source = re.sub(r"</head>", f"{marker}\n</head>", source, count=1, flags=re.I)

    if strict:
        remaining = re.findall(
            r"(?:src|href|poster)\s*=\s*['\"]((?:https?:)?//[^'\"]+)", source, flags=re.I
        )
        if remaining:
            raise ValueError("strict offline bundle still references: " + ", ".join(sorted(set(remaining))))

    if check:
        print(f"offline bundle check: {input_path} -> {'strict' if strict else 'hybrid'}")
        print(f"  mermaid blocks: {mermaid_count}")
        print(f"  optional external enhancements: {'disabled' if strict else 'enabled'}")
        for warning in sorted(set(warnings)):
            print(f"  warning: {warning}")
        return 0

    if output_path is None:
        suffix = ".offline.html" if strict else ".hybrid.html"
        output_path = input_path.with_name(input_path.stem + suffix)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(source, encoding="utf-8")
    print(f"wrote {output_path}")
    for warning in sorted(set(warnings)):
        print(f"warning: {warning}", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="HTML scaffold or generated page")
    parser.add_argument("-o", "--output", type=Path, help="bundled output path")
    parser.add_argument("--font-map", type=Path, help="JSON map of local font files to embed")
    parser.add_argument("--strict", action="store_true", help="remove optional network fonts and Mermaid runtime")
    parser.add_argument("--check", action="store_true", help="validate the transformed output without writing it")
    args = parser.parse_args()

    input_path = args.input.resolve()
    if not input_path.is_file():
        parser.error(f"input file not found: {input_path}")
    try:
        return bundle(input_path, args.output.resolve() if args.output else None, args.strict, args.font_map.resolve() if args.font_map else None, args.check)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"offline bundle failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
