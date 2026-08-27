# Quantum Pulse (量子脉冲黑蓝风)

## 1. Visual Theme & Atmosphere

Quantum Pulse 把长文页面当作一张正在扫描的深空测量图：近黑画布承载极淡工程网格，右上方的电蓝切入曲面以不对称贝塞尔边缘形成能量场，斜向白色光束把阅读路径切成清晰的前进方向。图 1 是主参考，提供黑、白、钴蓝的色彩比例和曲面/网格/斜线骨架；图 2 作为辅参考，提供单色粒子束、速度感和高密度微点纹理。

采用**直铺沉浸型 (Direct Immersive Flow)**。Layer 0 是固定环境背景（网格、曲面、轨迹弧线、斜向光束）；Layer 1 是无界的 `.pulse-sheet` 阅读流，不额外套白色画板；Layer 2 使用带切角、细边框和微发光的深色语义组件。移动端保留网格、蓝色局部曲面和一条主光束，降低粒子密度与装饰不透明度。

### Core Visual DNA

1. **黑底工程网格**：`#05070B` 画布上使用 32px 主网格和 8px 微网格，线条低于正文对比度。
2. **钴蓝切入曲面**：以 `#145CFF` 到 `#071A67` 的非对称贝塞尔曲面渐变作为环境焦点，覆盖面积控制在视口的 18%~30%，避免完整圆盘轮廓。
3. **斜向白色光束**：从左下/左侧指向右上或核心数据点，作为标题、流程和数据组件的共同导视语法。
4. **粒子与半调体块**：用 CSS/SVG 点阵、短划线和 `radial-gradient` 组织“高速扫描”质感，不使用照片或专有插画。
5. **单色高亮信息层**：白色标题和冰蓝正文配合蓝色信号色；数字、状态和边框发光克制，保证阅读优先。

### Reference Boundary

- **Preserve**：黑/蓝/白主色关系、工程网格、曲面蓝色环境层、斜向光束、粒子扫描和清晰的英文等宽元数据。
- **Adapt**：把单张海报的视觉焦点转译为可循环使用的背景层、标题导视线、半调数据卡和流程连接线；长文本采用连续无界阅读流。
- **Exclude**：参考图中的品牌 Logo、产品名称、真实发布文案、固定几何坐标、专有图标、摄影/插画资产和一次性卡片数量。
- **Unknown**：参考图未证明完整交互、复杂图表、响应式断点和动效强度；以下规则属于可解释的 `Inferred` 推演。

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Usage |
|---|---|---|
| Canvas | `#05070B` | 全局直铺画布与打印背景 |
| Deep Surface | `#080D16` | 代码、输入、凹陷区域 |
| Surface | `rgba(12, 18, 31, .92)` | 语义组件承托面，带细微蓝黑层次 |
| Text Primary | `#F7FAFF` | 标题、关键数字、表头 |
| Text Secondary | `#B6C2D8` | 正文、导读、说明 |
| Text Muted | `#71809A` | 元数据、脚注、单位 |
| Border | `rgba(143, 169, 214, .22)` | 普通边框与分隔线 |
| Border Strong | `#376BFF` | 聚焦、选中、关键连接 |

### Signal Palette

| Channel | Value | Usage Boundary |
|---|---|---|
| Cobalt Signal | `#145CFF` | 主标题强调、流程主线、选中态，占约 4%~7% |
| Electric Blue | `#2F83FF` | 光束高光、数据条、链接，占约 2%~4% |
| Ice Cyan | `#74D8FF` | 次级标记、图表节点、可访问焦点，占约 1%~2% |
| Beam White | `#F4F7FF` | 斜向光束、主要分割线、反差高光 |
| Status Amber | `#FFC857` | 仅用于 warning/attention 语义，避免蓝色通道混淆 |

```css
:root {
  --canvas: #05070B;
  --canvas-deep: #020308;
  --surface-0: #080D16;
  --surface-1: rgba(12, 18, 31, 0.92);
  --surface-2: rgba(19, 30, 52, 0.82);
  --text-primary: #F7FAFF;
  --text-secondary: #B6C2D8;
  --text-muted: #71809A;
  --border: rgba(143, 169, 214, 0.22);
  --border-strong: #376BFF;
  --signal-blue: #145CFF;
  --signal-electric: #2F83FF;
  --signal-cyan: #74D8FF;
  --beam-white: #F4F7FF;
  --status-amber: #FFC857;
  --grid-major: rgba(102, 137, 196, 0.09);
  --grid-minor: rgba(102, 137, 196, 0.035);
  --shadow-scan: 0 0 24px rgba(20, 92, 255, 0.18);
  --shadow-panel: 0 16px 44px rgba(0, 0, 0, 0.52), inset 0 1px 0 rgba(244, 247, 255, 0.07);
  --radius-cut: 4px;
  --radius-pill: 999px;
  --container: 1240px;
  --font-display: "Inter", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", Consolas, monospace;
}
```

## 3. Style-Owned Layout Contract

### Top-level structure

The ambient layer is part of the style and must not be removed:

```html
<body class="quantum-pulse">
  <div class="ambient" aria-hidden="true">
    <svg class="energy-surface" viewBox="0 0 1200 700" preserveAspectRatio="none"><defs><linearGradient id="quantum-surface-gradient" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2F83FF"/><stop offset=".55" stop-color="#145CFF"/><stop offset="1" stop-color="#071A67"/></linearGradient></defs><path d="M420 -24H1200V252C1130 282 1030 298 930 292C790 282 690 250 600 200C520 154 470 70 420 -24Z" fill="url(#quantum-surface-gradient)" /></svg>
    <svg class="orbit-lines" viewBox="0 0 1200 700"><path d="M40 580 C380 70 760 30 1180 170" /></svg>
    <div class="beam"></div>
  </div>
  <main class="pulse-sheet">...</main>
</body>
```

```css
body.quantum-pulse {
  background-color: var(--canvas);
  background-image: linear-gradient(var(--grid-major) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-major) 1px, transparent 1px),
    linear-gradient(var(--grid-minor) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-minor) 1px, transparent 1px);
  background-size: 32px 32px, 32px 32px, 8px 8px, 8px 8px;
}
.pulse-sheet { position: relative; z-index: 1; max-width: var(--container); margin: 0 auto; padding: 0 48px; }
.ambient { position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
.energy-surface { position: absolute; inset: 0; width: 100%; height: 100%; opacity: .88; }
.beam { position: absolute; width: 125vw; height: 2px; left: -20vw; top: 67vh; transform: rotate(-17deg); background: linear-gradient(90deg, transparent, var(--beam-white) 42%, rgba(244,247,255,.12) 76%, transparent); box-shadow: 0 0 16px rgba(244,247,255,.28); }
```

### Web Adaptation

- 12-column desktop rhythm; `.pulse-sheet` remains direct on the ambient canvas with sections separated by 56–88px.
- Components use `clip-path` micro-cut corners or 0–4px radii, never soft white cards. Keep content surfaces opaque enough to preserve body contrast.
- Data and comparison matrices scroll horizontally at widths below 760px. Hero switches to a single column; the energy surface scales down to a shallow corner sweep and the beam becomes a 1px low-opacity line.
- Motion is optional and prefers `prefers-reduced-motion`; use 6–10s opacity/translate pulses only on ambient particles.

### PPT Adaptation

- Fixed 1280×720 16:9 `.slide` stage with 6% safe padding. Each slide carries its own grid, asymmetric energy surface and one beam motif.
- Use one claim per slide. Cover uses the largest surface/beam; data and comparison pages use smaller corner energy fields so text remains legible in projection.
- Keep body copy at 16px minimum in the 1280×720 design coordinate system. Footer metadata sits at the bottom safe edge.

## 4. Typography Scale & Rules

### Font stacks

- **Display**: `--font-display`, a neutral grotesk with Chinese sans fallback. Use weight 700–800 for titles.
- **Body**: `--font-display`, weight 400–500, maximum 70ch for reading paragraphs.
- **Mono**: `--font-mono` for eyebrows, units, code, IDs, timestamps and technical labels.

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Role |
|---|---|---:|---:|---:|---:|---|
| Hero headline | `h1.hero` | 44–78px | 800 | 1.02 | -0.03em | 第一视觉焦点 |
| Section title | `h2.section-title` | 30–46px | 750 | 1.12 | -0.02em | 章节主论点 |
| Card title | `h3` | 18–24px | 700 | 1.28 | 0 | 组件标题 |
| Lead | `.lead` | 18–22px | 400 | 1.55 | 0 | 导读与摘要 |
| Body | `.body`, `.rich-text` | 15–16px | 400 | 1.78 | 0 | 长文阅读 |
| Eyebrow | `.eyebrow` | 11–13px | 600 | 1.1 | .12em | 章节索引 |
| Stat metric | `.stat-val` | 44–62px | 800 | 1 | -0.02em | 核心数字 |
| Unit / tag | `.unit`, `.tag` | 10–12px | 600 | 1.2 | .08em | 技术元数据 |
| Code | `pre`, `code` | 13–14px | 500 | 1.6 | 0 | 可复制代码 |

Rules: use deliberate line breaks in hero titles when a Chinese phrase would become a stranded single character; never use negative letter spacing below `-0.04em`; keep labels uppercase only for short English metadata, not for prose.

## 5. Signature Component Patterns

### 1. Pulse panel with cut corner

```html
<article class="pulse-panel selected">
  <div class="panel-kicker"><span class="signal-dot"></span> 02 / ACTIVE NODE</div>
  <h3>可观测的系统状态</h3>
  <p>用深色承托面收纳长文中的关键结论，再用一条蓝色信号线标记当前焦点。</p>
</article>
```

```css
.pulse-panel { position: relative; background: var(--surface-1); border: 1px solid var(--border); border-radius: var(--radius-cut); box-shadow: var(--shadow-panel); padding: 24px; clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 0 100%); }
.pulse-panel.selected { border-color: var(--border-strong); box-shadow: var(--shadow-panel), 0 0 22px rgba(20, 92, 255, .22); }
.panel-kicker { font: 600 11px/1.2 var(--font-mono); letter-spacing: .1em; color: var(--signal-cyan); }
.signal-dot { display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: var(--signal-cyan); box-shadow: 0 0 12px var(--signal-cyan); }
```

### 2. Beam stat card

```html
<div class="beam-stat"><div class="stat-val">4.8<span>ms</span></div><div class="stat-label">MEDIAN RESPONSE</div><div class="stat-spark"></div></div>
```

```css
.beam-stat { background: linear-gradient(145deg, rgba(19,30,52,.96), rgba(8,13,22,.96)); border: 1px solid var(--border); padding: 22px 24px; position: relative; overflow: hidden; }
.beam-stat::after { content: ""; position: absolute; width: 160%; height: 1px; left: -30%; bottom: 22px; transform: rotate(-14deg); background: var(--beam-white); opacity: .42; box-shadow: 0 0 10px var(--beam-white); }
.stat-val { color: var(--text-primary); font: 800 52px/1 var(--font-display); }
.stat-val span { color: var(--signal-cyan); font: 600 16px/1 var(--font-mono); margin-left: 6px; }
.stat-label { color: var(--text-muted); font: 600 10px/1.2 var(--font-mono); letter-spacing: .1em; margin-top: 12px; }
```

### 3. Halftone feature frame

```html
<div class="halftone-frame"><div class="frame-grid"></div><div class="frame-copy">SIGNAL / 03</div></div>
```

```css
.halftone-frame { min-height: 180px; border: 1px solid var(--border); background: radial-gradient(circle at 70% 45%, rgba(116,216,255,.65) 0 1px, transparent 1.5px) 0 0/8px 8px, linear-gradient(135deg, #0A1734, #05070B 70%); position: relative; }
.frame-copy { position: absolute; bottom: 14px; left: 16px; color: var(--beam-white); font: 600 11px var(--font-mono); letter-spacing: .12em; }
```

### 4. Orbit timeline

```html
<div class="orbit-timeline"><div class="timeline-node"><b>2024</b><span>基线建立</span></div><div class="timeline-node active"><b>2026</b><span>规模化部署</span></div></div>
```

```css
.orbit-timeline { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; border-top: 1px solid var(--border); padding-top: 22px; }
.timeline-node { position: relative; padding-left: 18px; border-left: 2px solid var(--border); }
.timeline-node::before { content: ""; position: absolute; left: -6px; top: 0; width: 9px; height: 9px; background: var(--canvas); border: 2px solid var(--signal-blue); border-radius: 50%; }
.timeline-node.active { border-color: var(--signal-blue); }.timeline-node.active::before { background: var(--signal-blue); box-shadow: 0 0 14px var(--signal-blue); }
```

### 5. Signal admonition

```html
<aside class="signal-note warning"><strong>注意</strong><p>将假设和证据分开标注，避免把推演当成事实。</p></aside>
```

```css
.signal-note { border: 1px solid var(--border); border-left: 3px solid var(--signal-blue); background: rgba(12,18,31,.84); padding: 16px 20px; }
.signal-note.warning { border-left-color: var(--status-amber); }.signal-note strong { color: var(--text-primary); font: 700 12px var(--font-mono); letter-spacing: .08em; text-transform: uppercase; }.signal-note p { margin-top: 6px; color: var(--text-secondary); }
```

## 6. Do's and Don'ts

### 7 Do's

1. 保留 Layer 0 的黑底网格、蓝色曲面和至少一条斜向光束。
2. 用白色标题、冰蓝正文和钴蓝信号建立明确对比，不让发光效果代替层级。
3. 将半调点阵和短划线作为局部材质，避免覆盖整段正文。
4. 用等宽字体承载编号、单位、状态和来源，建立技术测量感。
5. 组件优先使用切角、细边框和深色内衬，保持 0–4px 的硬朗轮廓。
6. 在移动端减少环境装饰密度，保证正文、表格和代码可读且可横向滚动。
7. 对图表、流程和数据维持一条可追踪的蓝色信号线，突出当前节点而非装饰所有节点。

### 7 Don'ts

1. 不要把背景改成白色、米色或大面积渐变紫，破坏黑蓝主基调。
2. 不要移除环境层后用普通白卡片替代直铺阅读流。
3. 不要复制参考图的 Logo、产品名、原文案、固定坐标或专有插画。
4. 不要使用大面积霓虹描边、强噪点或闪烁动效造成阅读疲劳。
5. 不要把所有组件都做成相同的圆角玻璃卡，必须区分正文、数据、代码和图表承托。
6. 不要让网格、粒子或光束与正文形成低对比度叠压；必要时提高组件不透明度。
7. 不要为追求海报效果压缩正文、隐藏溢出或使用不可读的小字号。

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配量子脉冲黑蓝风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: true,
    background: "#05070B",
    primaryColor: "#0C121F",
    primaryTextColor: "#F7FAFF",
    primaryBorderColor: "#376BFF",
    lineColor: "#2F83FF",
    secondaryColor: "#0E1726",
    tertiaryColor: "#05070B",
    fontFamily: ""JetBrains Mono", "Inter", monospace"
  }
});
```
