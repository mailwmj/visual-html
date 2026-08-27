#!/usr/bin/env python3
"""
Preview SVG Mathematical Grid Validator (AST Parser)
Validates that preview.svg conforms to the locked 4-tier vertical layout:
  Tier 1: Eyebrow      (y: 10 ~ 32)
  Tier 2: Header Title (y: 40 ~ 64, baseline ~58)
  Tier 3: Main Card    (y: 68 ~ 196, height: 114 ~ 124)
  Tier 4: Footer Meta  (y: 206 ~ 230, baseline ~220)
"""
import argparse
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def parse_translate(transform_str):
    if not transform_str:
        return 0.0, 0.0
    m = re.search(r'translate\(\s*(-?\d+(?:\.\d+)?)\s*(?:,\s*(-?\d+(?:\.\d+)?))?\s*\)', transform_str)
    if m:
        x = float(m.group(1))
        y = float(m.group(2)) if m.group(2) is not None else 0.0
        return x, y
    return 0.0, 0.0


def local_name(tag):
    return tag.rsplit('}', 1)[-1]


def png_size(filepath):
    data = Path(filepath).read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n' or len(data) < 24:
        raise ValueError('not a PNG file')
    return struct.unpack('>II', data[16:24])

def validate_svg_file(filepath):
    issues = []
    try:
        xml_text = open(filepath, 'r', encoding='utf-8').read()
        xml_text = re.sub(r'\sxmlns="[^"]+"', '', xml_text, count=1)
        root = ET.fromstring(xml_text)
    except Exception as e:
        return [f"XML Parse Error: {e}"]

    # 1. ViewBox Check
    viewbox = root.attrib.get('viewBox', '').strip()
    if viewbox != '0 0 400 240':
        issues.append(f"Invalid viewBox: expected '0 0 400 240', got '{viewbox}'")

    # 2. Extract Tier 1 & Tier 2 groups
    groups = [child for child in root if local_name(child.tag) == 'g']
    if len(groups) < 4:
        issues.append(f"Expected at least 4 top-level groups (Eyebrow, Title, Card, Footer), found {len(groups)}")
        return issues

    # Tier 1 Group (Eyebrow)
    g_eyebrow = groups[0]
    _, y_eyebrow = parse_translate(g_eyebrow.attrib.get('transform', ''))
    if y_eyebrow < 8 or y_eyebrow > 30:
        issues.append(f"Tier 1 (Eyebrow) group y={y_eyebrow} out of range [8, 30]")

    # Tier 2 Group (Title)
    g_title = groups[1]
    _, y_title = parse_translate(g_title.attrib.get('transform', ''))
    if y_title < 48 or y_title > 64:
        issues.append(f"Tier 2 (Title) group y={y_title} out of range [48, 64]")

    # Verify gap between Eyebrow and Title
    gap_eyebrow_title = y_title - (y_eyebrow + 18) # 18 is max eyebrow height
    if gap_eyebrow_title < 10:
        issues.append(f"Gap between Eyebrow bottom and Title baseline is too small ({gap_eyebrow_title:.1f}px < 10px), causes text collision!")

    # Tier 3 Group (Card)
    g_card = groups[2]
    _, y_card = parse_translate(g_card.attrib.get('transform', ''))
    if y_card < 66 or y_card > 76:
        issues.append(f"Tier 3 (Card) group y={y_card} out of range [66, 76]")

    # Verify clearance between Title baseline and Card top (prevent font descender collision)
    clearance_title_card = y_card - y_title
    if clearance_title_card < 12:
        issues.append(f"Clearance between Title baseline (y={y_title}) and Card top (y={y_card}) is too small ({clearance_title_card:.1f}px < 12px), causes font descender clipping!")

    # Anti-Pattern Check: Unclipped Top Accent Bars directly on rounded cards
    card_rects = g_card.findall('./rect')
    base_card_rx = 0.0
    if len(card_rects) > 0:
        try:
            base_card_rx = float(card_rects[0].attrib.get('rx', '0'))
        except ValueError:
            base_card_rx = 0.0

    for r in card_rects[1:]:
        try:
            r_y = float(r.attrib.get('y', '0'))
            r_w = float(r.attrib.get('width', '0'))
            r_h = float(r.attrib.get('height', '0'))
            if r_y <= 2.0 and r_w >= 300.0 and r_h <= 8.0:
                issues.append(
                    f"Anti-Pattern Detected: Top accent bar <rect width='{r_w}' height='{r_h}' y='{r_y}'> placed directly on rounded card (rx={base_card_rx}). "
                    f"This causes corner clipping and visual detachment (floating progress bar glitch). Remove it or integrate into card stroke."
                )
        except ValueError:
            pass

    # Tier 4 Group (Footer)
    g_footer = groups[3]
    _, y_footer = parse_translate(g_footer.attrib.get('transform', ''))
    if y_footer < 205 or y_footer > 228:
        issues.append(f"Tier 4 (Footer) group y={y_footer} out of range [205, 228]")

    return issues

def main():
    parser = argparse.ArgumentParser(description='Validate registered Visual HTML previews or one unregistered style draft.')
    parser.add_argument('--project-root', type=Path, help='repository root; defaults to the script parent')
    parser.add_argument('--style-dir', type=Path, help='validate one style directory without requiring registry membership')
    args = parser.parse_args()

    project_root = (args.project_root or Path(__file__).resolve().parents[2]).resolve()
    styles_root = project_root / 'references' / 'styles'
    setup_issues = []
    preview_files = []

    if args.style_dir:
        style_path = args.style_dir.resolve()
        style_id = style_path.name
        svg_path = style_path / 'preview.svg'
        png_path = style_path / 'preview.png'
        preview_files.append((style_id, svg_path, png_path))
        if not style_path.is_dir():
            setup_issues.append(f'{style_id}: missing style directory {style_path}')
        if not svg_path.is_file():
            setup_issues.append(f'{style_id}: missing {svg_path}')
        if not png_path.is_file():
            setup_issues.append(f'{style_id}: missing {png_path}')
    else:
        registry_path = styles_root / 'registry.json'
        entries = []
        if registry_path.is_file():
            try:
                payload = json.loads(registry_path.read_text(encoding='utf-8'))
                entries = payload.get('styles', [])
                if not isinstance(entries, list) or not entries:
                    setup_issues.append(f'Invalid or empty style registry: {registry_path}')
            except Exception as error:
                setup_issues.append(f'Cannot read style registry {registry_path}: {error}')
        else:
            setup_issues.append(f'Missing style registry: {registry_path}')

        if entries:
            for entry in entries:
                style_id = entry.get('id') if isinstance(entry, dict) else None
                style_dir = entry.get('dir') if isinstance(entry, dict) else None
                if not style_id or not style_dir:
                    setup_issues.append(f'Invalid registry entry: {entry!r}')
                    continue
                svg_path = styles_root / style_dir / 'preview.svg'
                png_path = styles_root / style_dir / 'preview.png'
                preview_files.append((style_id, svg_path, png_path))
                if not svg_path.is_file():
                    setup_issues.append(f'{style_id}: missing {svg_path}')
                if not png_path.is_file():
                    setup_issues.append(f'{style_id}: missing {png_path}')
        else:
            setup_issues.append('No preview files selected; refusing to treat an empty set as success.')

    print(f"=== Validating {len(preview_files)} Style Preview Cards ===")
    failed = len(setup_issues)
    for issue in setup_issues:
        print(f"❌ [SETUP] {issue}")

    for style_id, svg, png in preview_files:
        if not svg.is_file():
            continue
        issues = validate_svg_file(svg)
        try:
            width, height = png_size(png)
            if (width, height) != (800, 480):
                issues.append(f"Invalid PNG dimensions: expected 800x480, got {width}x{height}")
        except Exception as error:
            issues.append(f"PNG validation error: {error}")
        if issues:
            print(f"❌ [FAIL] {svg}")
            for iss in issues:
                print(f"   • {iss}")
            failed += 1
        else:
            print(f"✅ [PASS] {svg}")

    if not preview_files:
        print("\n⚠️ No preview cards were found; validation failed.")
        sys.exit(1)
    if failed == 0:
        print(f"\n🎉 All {len(preview_files)} preview cards passed 4-tier grid validation!")
        sys.exit(0)
    else:
        print(f"\n⚠️ {failed} files failed validation.")
        sys.exit(1)

if __name__ == '__main__':
    main()
