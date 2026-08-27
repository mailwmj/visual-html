#!/usr/bin/env python3
"""Initialize a new Visual HTML style pack with complete scaffolds, preview files, and registry integration."""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
import zlib
from pathlib import Path
from typing import Any

from sync_registry import generate_skill_table, load_registry_payload, sync_gallery_file, sync_skill_file
from validate_previews import validate_svg_file


VALID_CATEGORIES = ("tech", "pop", "editorial", "lifestyle")
STYLE_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def generate_placeholder_png(output_path: Path, width: int = 800, height: int = 480,
                             bg_rgb: tuple[int, int, int] = (12, 15, 20),
                             accent_rgb: tuple[int, int, int] = (56, 189, 248)) -> None:
    """Generate a valid 800x480 PNG placeholder file using pure Python stdlib."""
    raw_rows = bytearray()
    for y in range(height):
        raw_rows.append(0)  # Filter type 0 (None)
        t = y / max(1, height - 1)
        r_line = int(bg_rgb[0] * (1.0 - t * 0.25) + accent_rgb[0] * (t * 0.12))
        g_line = int(bg_rgb[1] * (1.0 - t * 0.25) + accent_rgb[1] * (t * 0.12))
        b_line = int(bg_rgb[2] * (1.0 - t * 0.25) + accent_rgb[2] * (t * 0.12))
        for x in range(width):
            if 40 <= x < width - 40 and 140 <= y < height - 70:
                cr = min(255, int(r_line + 18))
                cg = min(255, int(g_line + 24))
                cb = min(255, int(b_line + 36))
                raw_rows.extend((cr, cg, cb))
            else:
                raw_rows.extend((r_line, g_line, b_line))

    compressed = zlib.compress(bytes(raw_rows), level=6)

    def make_chunk(chunk_type: bytes, chunk_data: bytes) -> bytes:
        length = struct.pack(">I", len(chunk_data))
        crc = struct.pack(">I", zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF)
        return length + chunk_type + chunk_data + crc

    header = b"\x89PNG\r\n\x1a\n"
    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    ihdr_chunk = make_chunk(b"IHDR", ihdr_data)
    idat_chunk = make_chunk(b"IDAT", compressed)
    iend_chunk = make_chunk(b"IEND", b"")

    output_path.write_bytes(header + ihdr_chunk + idat_chunk + iend_chunk)


def generate_preview_svg(style_id: str, name: str, english_name: str,
                         accent: str = "#38BDF8", bg: str = "#0C0F14") -> str:
    """Generate a preview SVG conforming strictly to the 4-tier vertical coordinate grid."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="800" height="480">
  <defs>
    <linearGradient id="card-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
  </defs>
  <rect width="400" height="240" fill="{bg}" rx="8"/>

  <!-- Tier 1: Eyebrow (y: 8 ~ 30) -->
  <g transform="translate(20, 14)">
    <rect x="0" y="0" width="112" height="18" rx="9" fill="{accent}" fill-opacity="0.15" stroke="{accent}" stroke-opacity="0.6" stroke-width="1"/>
    <circle cx="10" cy="9" r="3" fill="{accent}"/>
    <text x="20" y="12" fill="#94A3B8" font-family="monospace" font-size="8" letter-spacing="1">STYLE // 01</text>
  </g>

  <!-- Tier 2: Title (y: 48 ~ 64, baseline ~58) -->
  <g transform="translate(20, 58)">
    <text x="0" y="0" fill="#F8FAFC" font-family="sans-serif" font-size="16" font-weight="700">{name}</text>
    <text x="170" y="-1" fill="#64748B" font-family="monospace" font-size="8">{english_name.upper()}</text>
  </g>

  <!-- Tier 3: Main Card (y: 66 ~ 76, height: 114 ~ 124) -->
  <g transform="translate(20, 72)">
    <rect width="360" height="120" rx="8" fill="url(#card-grad)" stroke="#334155" stroke-width="1"/>
    <text x="18" y="24" fill="{accent}" font-family="monospace" font-size="8" letter-spacing="1">SIGNATURE COMPONENT</text>
    <text x="18" y="62" fill="#F8FAFC" font-family="sans-serif" font-size="24" font-weight="800">100<tspan fill="{accent}" font-size="14">%</tspan></text>
    <text x="18" y="80" fill="#94A3B8" font-family="monospace" font-size="8" letter-spacing="0.5">HIGH FIDELITY PREVIEW</text>
    <line x1="180" y1="36" x2="180" y2="100" stroke="#334155" stroke-dasharray="2 3"/>
    <text x="200" y="60" fill="#F8FAFC" font-family="sans-serif" font-size="20" font-weight="700">18+1</text>
    <text x="200" y="80" fill="#94A3B8" font-family="monospace" font-size="8" letter-spacing="0.5">COMPONENTS READY</text>
    <line x1="18" y1="104" x2="342" y2="104" stroke="#334155" stroke-opacity="0.6"/>
  </g>

  <!-- Tier 4: Footer Meta (y: 205 ~ 228, baseline ~220) -->
  <g transform="translate(20, 220)">
    <text x="0" y="0" fill="#64748B" font-family="monospace" font-size="8">style_id: <tspan fill="#94A3B8">{style_id}</tspan></text>
    <rect x="270" y="-10" width="14" height="14" fill="#0C0F14" stroke="#334155" rx="2"/>
    <rect x="288" y="-10" width="14" height="14" fill="#1E293B" stroke="#334155" rx="2"/>
    <rect x="306" y="-10" width="14" height="14" fill="{accent}" rx="2"/>
    <rect x="324" y="-10" width="14" height="14" fill="#F8FAFC" rx="2"/>
  </g>
</svg>
"""


def generate_design_md(style_id: str, name: str, english_name: str,
                       visual_traits: str, scenarios: str) -> str:
    """Generate design.md template with all 7 standard sections and Mermaid configuration."""
    return f"""# {english_name} ({name}) — Design Language Reference

## 1. Visual Theme & Atmosphere

- **设计哲学**：{visual_traits}
- **推荐场景**：{scenarios}
- **空间形态原型**：悬浮画板型 / 直铺沉浸型 (依美学诉求选定)
- **Core Visual DNA**：
  1. 主题底色与专属空间纵深体系
  2. 具象材质层与高对比度排版
  3. 专属信号色彩通道与微光点缀
  4. 规范化的 18 项语义组件映射能力

---

## 2. Color Palette & Roles

### Core Interface Colors

| Role | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|
| Background (Canvas) | `#0C0F14` | `--bg` | 页面全局画布底色 |
| Surface (Primary Card) | `#141A23` | `--surface-1` | 主阅读画板与核心卡片 |
| Surface (Secondary Panel) | `#1D2533` | `--surface-2` | 次级嵌套面板、代码块与规格表格 |
| Text (Primary) | `#F8FAFC` | `--text-primary` | 大标题与正文核心文字 |
| Text (Secondary) | `#94A3B8` | `--text-secondary` | 导读段落与次要说明 |
| Text (Muted) | `#64748B` | `--text-muted` | 注释、页脚与元数据标签 |
| Border (Default) | `rgba(255, 255, 255, 0.08)` | `--border` | 卡片外边框与模块分割线 |
| Border (Highlight) | `rgba(56, 189, 248, 0.4)` | `--border-strong` | 选中高亮与悬浮边框 |
| Accent (Primary Brand) | `#38BDF8` | `--accent` | 标头胶囊、核心重点与行动徽章 |

### CSS Design Tokens

```css
:root {{
  /* Canvas & Surface */
  --bg: #0C0F14;
  --surface-1: #141A23;
  --surface-2: #1D2533;

  /* Typography */
  --text-primary: #F8FAFC;
  --text-secondary: #94A3B8;
  --text-muted: #64748B;

  /* Borders & Highlights */
  --border: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(56, 189, 248, 0.4);
  --accent: #38BDF8;
  --accent-soft: rgba(56, 189, 248, 0.12);

  /* Dimensions & Fonts */
  --radius: 12px;
  --radius-sm: 6px;
  --container: 1140px;
  --font-display: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: "Cascadia Code", Consolas, "SFMono-Regular", monospace;
}}
```

---

## 3. Style-Owned Layout Contract

- **Web Adaptation**：
  - 桌面端居中容器最大宽度 `1140px`，两侧保留至少 `24px` 安全边距。
  - 移动端单栏流式排列，字号与卡片内边距等比收敛。
- **PPT Adaptation**：
  - 固定 16:9 舞台（`1280x720` / `min(92vw, 1160px)`），内边距 `5%~7%`。
  - 单页单焦点，内置键盘导航、全屏与无边距打印适配。

---

## 4. Typography Scale & Rules

| Element | Tag / Class | Size | Weight | Line Height | Role |
|---|---|---|---|---|---|
| Hero Title | `h1.hero` | `38px` | 800 | 1.2 | 全文首屏主标题 |
| Section Title | `h2.section-title` | `26px` | 700 | 1.3 | 各阶段一级章节标题 |
| Subsection Title | `h3.sub-title` | `18px` | 600 | 1.4 | 卡片与子模块标题 |
| Body Text | `p, .rich-text` | `15px` | 400 | 1.65 | 长文正文内容 |
| Meta & Caption | `.meta, .unit` | `12px` | 500 | 1.4 | 标签、单位与脚注 |

---

## 5. Signature Component Patterns

### 1. 核心特征数据卡片
```html
<div class="stat-card">
  <div class="stat-val">100<span class="unit">%</span></div>
  <div class="stat-label">HIGH FIDELITY / 高保真设计</div>
</div>
```

---

## 6. Mermaid Theme Configuration

在线增强时，在 `</body>` 前注入以下匹配{name}的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```javascript
mermaid.initialize({{
  startOnLoad: false,
  theme: 'base',
  themeVariables: {{
    darkMode: true,
    background: '#141A23',
    primaryColor: '#1D2533',
    primaryTextColor: '#F8FAFC',
    primaryBorderColor: 'rgba(56, 189, 248, 0.4)',
    lineColor: '#38BDF8',
    secondaryColor: '#0C0F14',
    tertiaryColor: '#141A23'
  }}
}});
```

---

## 7. Do's and Don'ts

### 7 项核心金律 (Do's)
1. 必须保持空间纵深架构与专属色谱严谨一致。
2. 必须保留 18 项语义组件的覆盖能力。
3. 必须确保文本对比度满足无障碍阅读标准。
4. 必须实现 16:9 PPT 舞台与完整翻页逻辑。
5. 必须在 `design.md` 中完整维护 `themeVariables` 配置。
6. 必须确保离线交付时支持纯静态无损渲染。
7. 必须在完成 Stage 8 质量门后再执行最终注册并网。

### 7 项严禁红线 (Don'ts)
1. 严禁将专属材质漂白为千篇一律的普通纯白卡片。
2. 严禁在圆角卡片顶部叠加未裁切的直角彩色矩形条。
3. 严禁标题文字基线与卡片顶部间距小于 12px。
4. 严禁在未完成质量门前直接修改注册表。
5. 严禁省略 18 项语义组件中的任意一项。
6. 严禁将 Web 样式通过简单缩放直接套用至 PPT。
7. 严禁引入未声明的外部硬依赖资源。
"""


def generate_web_scaffold(base_web_content: str, style_id: str, name: str) -> str:
    """Generate scaffold-web.html by injecting style tokens and starter CSS into base scaffold."""
    starter_css = f"""<style>
:root {{
  --bg: #0C0F14;
  --surface-1: #141A23;
  --surface-2: #1D2533;
  --text-primary: #F8FAFC;
  --text-secondary: #94A3B8;
  --text-muted: #64748B;
  --border: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(56, 189, 248, 0.4);
  --accent: #38BDF8;
  --accent-soft: rgba(56, 189, 248, 0.12);
  --radius: 12px;
  --radius-sm: 6px;
  --container: 1140px;
  --font-display: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", sans-serif;
  --font-mono: "Cascadia Code", Consolas, "SFMono-Regular", monospace;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background-color: var(--bg);
  color: var(--text-primary);
  font-family: var(--font-display);
  font-size: 15px;
  line-height: 1.65;
  padding: 48px 20px 100px;
}}
.wrap {{
  max-width: var(--container);
  margin: 0 auto;
}}
section {{ margin-bottom: 64px; }}
h1.hero {{ font-size: clamp(28px, 4vw, 40px); font-weight: 800; line-height: 1.25; margin: 16px 0; color: #FFF; }}
h2.section-title {{ font-size: 24px; font-weight: 700; margin-bottom: 20px; color: var(--text-primary); }}
p.lead {{ font-size: 16px; color: var(--text-secondary); margin-bottom: 28px; }}

.eyebrow {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--accent);
  letter-spacing: 0.05em;
  padding: 4px 12px;
  background: var(--accent-soft);
  border: 1px solid var(--border-strong);
  border-radius: 999px;
  margin-bottom: 12px;
}}
.stats-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin: 24px 0;
}}
.stat-card {{
  background: var(--surface-1);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
}}
.stat-val {{ font-size: 32px; font-weight: 800; color: var(--text-primary); }}
.stat-label {{ font-size: 12px; color: var(--text-secondary); font-family: var(--font-mono); margin-top: 4px; }}

.spec-row {{
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 16px;
}}
.spec {{
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 10px 16px;
}}
.spec .val {{ font-weight: 700; color: var(--text-primary); }}
.spec .unit {{ font-size: 11px; color: var(--text-muted); font-family: var(--font-mono); }}

.admonition {{
  background: var(--surface-1);
  border-left: 4px solid var(--accent);
  border-radius: 0 var(--radius) var(--radius) 0;
  padding: 16px 20px;
  margin: 20px 0;
}}
.admonition-title {{ font-weight: 700; margin-bottom: 6px; color: var(--accent); }}

.data-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  background: var(--surface-1);
  border-radius: var(--radius);
  overflow: hidden;
}}
.data-table th, .data-table td {{
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  text-align: left;
}}
.data-table th {{ background: var(--surface-2); font-weight: 600; color: var(--text-secondary); }}

.code-block {{
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  font-family: var(--font-mono);
  font-size: 13px;
  overflow-x: auto;
  margin: 16px 0;
}}

.flowchart-wrap, .timeline-wrap, .faq-wrap {{
  background: var(--surface-1);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  margin: 20px 0;
}}
</style>
"""
    content = base_web_content
    # Replace Title
    content = re.sub(
        r"<title>.*?</title>",
        f"<title>{name} ({style_id}) — Web Scaffold</title>",
        content,
        count=1,
    )
    # Insert Starter CSS
    if "</head>" in content:
        content = content.replace("</head>", f"{starter_css}</head>", 1)
    return content


def generate_ppt_scaffold(base_ppt_content: str, style_id: str, name: str) -> str:
    """Generate scaffold-ppt.html by updating title and base config."""
    content = base_ppt_content
    content = re.sub(
        r"<title>.*?</title>",
        f"<title>{name} ({style_id}) — PPT Scaffold</title>",
        content,
        count=1,
    )
    return content


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("style_id", help="unique style identifier in lowercase kebab-case (e.g. cyber-bento)")
    parser.add_argument("--name", required=True, help="human-readable Chinese style name (e.g. 赛博便当风)")
    parser.add_argument("--english-name", help="English name of the style (default: derived from style_id)")
    parser.add_argument(
        "--categories",
        nargs="+",
        choices=VALID_CATEGORIES,
        default=["tech"],
        help="style categories (default: tech)",
    )
    parser.add_argument(
        "--visual-traits",
        default="浅色极简底色 + 层次网格 + 精致字阶排版 + 主题强调色",
        help="short summary of core visual traits",
    )
    parser.add_argument(
        "--scenarios",
        default="专业报告、技术白皮书、产品发布、系统架构展示",
        help="recommended usage scenarios",
    )
    parser.add_argument("--force", action="store_true", help="overwrite existing style directory and files")
    parser.add_argument("--no-register", action="store_true", help="skip registering in registry.json")
    parser.add_argument("--project-root", type=Path, help="repository root directory")

    args = parser.parse_args()

    style_id = args.style_id.strip()
    if not STYLE_ID_PATTERN.fullmatch(style_id):
        print(f"❌ Error: invalid style_id '{style_id}'. Must be lowercase kebab-case (e.g. 'neon-dark').", file=sys.stderr)
        return 1

    name = args.name.strip()
    english_name = args.english_name.strip() if args.english_name else style_id.replace("-", " ").title()
    categories = args.categories
    visual_traits = args.visual_traits.strip()
    scenarios = args.scenarios.strip()

    root = (args.project_root or Path(__file__).resolve().parents[2]).resolve()
    references_dir = root / "references"
    styles_root = references_dir / "styles"
    target_style_dir = styles_root / style_id
    registry_path = styles_root / "registry.json"

    base_web_path = references_dir / "web" / "base-scaffold.html"
    base_ppt_path = references_dir / "ppt" / "base-scaffold.html"

    if not base_web_path.is_file() or not base_ppt_path.is_file():
        print("❌ Error: base scaffold files (web/base-scaffold.html or ppt/base-scaffold.html) not found.", file=sys.stderr)
        return 1

    if target_style_dir.exists() and not args.force:
        print(f"❌ Error: style directory already exists at {target_style_dir}. Use --force to overwrite.", file=sys.stderr)
        return 1

    target_style_dir.mkdir(parents=True, exist_ok=True)

    # 1. design.md
    design_md_content = generate_design_md(style_id, name, english_name, visual_traits, scenarios)
    (target_style_dir / "design.md").write_text(design_md_content, encoding="utf-8")

    # 2. scaffold-web.html
    base_web_content = base_web_path.read_text(encoding="utf-8")
    web_scaffold_content = generate_web_scaffold(base_web_content, style_id, name)
    (target_style_dir / "scaffold-web.html").write_text(web_scaffold_content, encoding="utf-8")

    # 3. scaffold-ppt.html
    base_ppt_content = base_ppt_path.read_text(encoding="utf-8")
    ppt_scaffold_content = generate_ppt_scaffold(base_ppt_content, style_id, name)
    (target_style_dir / "scaffold-ppt.html").write_text(ppt_scaffold_content, encoding="utf-8")

    # 4. preview.svg
    preview_svg_content = generate_preview_svg(style_id, name, english_name)
    preview_svg_path = target_style_dir / "preview.svg"
    preview_svg_path.write_text(preview_svg_content, encoding="utf-8")

    # 5. preview.png
    preview_png_path = target_style_dir / "preview.png"
    generate_placeholder_png(preview_png_path)

    # Verify generated preview SVG with AST validator
    svg_issues = validate_svg_file(preview_svg_path)
    if svg_issues:
        print(f"⚠️ Warning: generated preview.svg had validation issues: {svg_issues}", file=sys.stderr)

    print(f"✨ Scaffold created successfully for style '{style_id}':")
    print(f"   📁 {target_style_dir.relative_to(root)}/")
    print("   ├── design.md")
    print("   ├── scaffold-web.html")
    print("   ├── scaffold-ppt.html")
    print("   ├── preview.svg")
    print("   └── preview.png")

    # 6. Registry integration
    if not args.no_register:
        try:
            payload = load_registry_payload(registry_path)
            styles = payload.get("styles", [])
            existing_idx = next((i for i, s in enumerate(styles) if s.get("id") == style_id), -1)

            entry = {
                "id": style_id,
                "name": name,
                "englishName": english_name,
                "categories": categories,
                "dir": style_id,
                "visualTraits": visual_traits,
                "scenarios": scenarios,
            }

            if existing_idx >= 0:
                if args.force:
                    styles[existing_idx] = entry
                    print(f"   🔄 Updated existing entry in registry.json for '{style_id}'")
                else:
                    print(f"   ℹ️ Entry '{style_id}' already in registry.json")
            else:
                styles.append(entry)
                payload["styles"] = styles
                print(f"   ➕ Added '{style_id}' to registry.json")

            registry_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            # Run sync_registry
            skill_path = root / "SKILL.md"
            gallery_path = references_dir / "style-gallery.html"
            table_content = generate_skill_table(styles)
            sync_skill_file(skill_path, table_content)
            sync_gallery_file(gallery_path, payload)
            print("   ✅ Synced SKILL.md table and style-gallery.html embedded registry")

        except Exception as exc:
            print(f"❌ Failed to update registry: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
