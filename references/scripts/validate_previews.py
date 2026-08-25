#!/usr/bin/env python3
"""
Preview SVG Mathematical Grid Validator (AST Parser)
Validates that preview.svg conforms to the locked 4-tier vertical layout:
  Tier 1: Eyebrow      (y: 10 ~ 32)
  Tier 2: Header Title (y: 40 ~ 64, baseline ~58)
  Tier 3: Main Card    (y: 68 ~ 196, height: 114 ~ 124)
  Tier 4: Footer Meta  (y: 206 ~ 230, baseline ~220)
"""
import glob
import sys
import xml.etree.ElementTree as ET
import re

def parse_translate(transform_str):
    if not transform_str:
        return 0.0, 0.0
    m = re.search(r'translate\(\s*(-?\d+(?:\.\d+)?)\s*(?:,\s*(-?\d+(?:\.\d+)?))?\s*\)', transform_str)
    if m:
        x = float(m.group(1))
        y = float(m.group(2)) if m.group(2) is not None else 0.0
        return x, y
    return 0.0, 0.0

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
    groups = root.findall('./g')
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
    gap = y_title - (y_eyebrow + 18) # 18 is max eyebrow height
    if gap < 10:
        issues.append(f"Gap between Eyebrow bottom and Title baseline is too small ({gap:.1f}px < 10px), causes text collision!")

    # Tier 3 Group (Card)
    g_card = groups[2]
    _, y_card = parse_translate(g_card.attrib.get('transform', ''))
    if y_card < 66 or y_card > 76:
        issues.append(f"Tier 3 (Card) group y={y_card} out of range [66, 76]")

    # Tier 4 Group (Footer)
    g_footer = groups[3]
    _, y_footer = parse_translate(g_footer.attrib.get('transform', ''))
    if y_footer < 205 or y_footer > 228:
        issues.append(f"Tier 4 (Footer) group y={y_footer} out of range [205, 228]")

    return issues

def main():
    svg_files = sorted(glob.glob('references/styles/*/preview.svg'))
    print(f"=== Validating {len(svg_files)} Style Preview Cards ===")
    failed = 0
    for svg in svg_files:
        issues = validate_svg_file(svg)
        if issues:
            print(f"❌ [FAIL] {svg}")
            for iss in issues:
                print(f"   • {iss}")
            failed += 1
        else:
            print(f"✅ [PASS] {svg}")

    if failed == 0:
        print(f"\n🎉 All {len(svg_files)} preview cards passed 4-tier grid validation!")
        sys.exit(0)
    else:
        print(f"\n⚠️ {failed} files failed validation.")
        sys.exit(1)

if __name__ == '__main__':
    main()
