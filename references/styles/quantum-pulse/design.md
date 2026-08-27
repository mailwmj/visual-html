# Quantum Pulse (量子脉冲黑蓝风)

## 1. Visual Theme & Atmosphere

Quantum Pulse 把长文页面当作一张正在扫描的深空测量图：近黑画布承载 48px 极淡精密工程网格与十字测量刻度，右上方的电光群青数学正圆巨弧（R=720px）以同心轨道与微半调点阵形成纯粹严谨的深空能量场，-16.5° 斜向超导高能光束（带星芒聚焦点）把阅读路径切成清晰的前进方向。图 1 是主参考，提供黑、白、钴蓝的色彩比例和纯正巨弧/网格/斜线骨架；图 2 作为辅参考，提供单色粒子束、速度感和高密度微点纹理。

采用**直铺沉浸型 (Direct Immersive Flow)**。Layer 0 是固定环境背景（精密网格、正圆天体巨弧、同心轨道刻度环、斜向激光束）；Layer 1 是无界的 `.pulse-sheet` 阅读流，不额外套白色画板；Layer 2 使用带切角、细边框和微发光的深色语义组件。移动端保留网格、蓝色正圆局部曲面和主光束，降低粒子密度与装饰不透明度。

### Core Visual DNA

1. **黑底精密网格**：`#04060A` 画布上使用 48px 单层超低透明度极细工程网格（`rgba(116, 216, 255, 0.04)`）配合精密十字测量刻度，通透深邃。
2. **深空精密巨弧**：以 `#4FA1FF`、`#145CFF` 到 `#072288` 的数学正圆弧（R=720px）电光群青渐变配合平滑微半调点阵切入右上角，外围环绕极细精密同心测量环（Radar Orbit Rings），严谨纯粹。
3. **斜向超导激光束与静谧双锥光脉**：-16.5° 单轴超导微光底线，承载周期为 20s 的 170px 纤长双锥微光脉冲（两端 0px 锐利收尖，6.5s 悠长漫游，13.5s 静谧期），不打扰正文阅读同时指引核心。
4. **粒子与微半调体块**：用 CSS/SVG 点阵、短划线和 `radial-gradient` 组织“高速扫描”质感，不使用照片或专有插画。
5. **单色高亮信息层**：白色标题和冰蓝正文配合蓝色信号色；数字、状态和边框发光克制，保证阅读优先。

### Reference Boundary

- **Preserve**：黑/蓝/白主色关系、精密工程网格、数学正圆天体巨弧、同心轨道环、斜向高能光束、微半调点阵和清晰的英文等宽元数据。
- **Adapt**：把单张海报的视觉焦点转译为可循环使用的背景层、标题导视线、半调数据卡和流程连接线；长文本采用连续无界阅读流。
- **Exclude**：参考图中的品牌 Logo、产品名称、真实发布文案、固定几何坐标、专有图标、摄影/插画资产和一次性卡片数量。
- **Unknown**：参考图未证明完整交互、复杂图表、响应式断点和动效强度；以下规则属于可解释的 `Inferred` 推演。

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Usage |
|---|---|---|
| Canvas | `#04060A` | 全局直铺画布与打印背景 |
| Deep Surface | `#020308` | 代码、输入、凹陷区域 |
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
| Status Amber | `#FFC857` | 仅用于极少数高危 warning/attention 语义，严禁用于常规总结、核心结论或关键洞见 |

```css
:root {
  --canvas: #04060A;
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
  --grid-major: rgba(116, 216, 255, 0.04);
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
    <svg class="energy-surface" viewBox="0 0 1200 700" preserveAspectRatio="none">
      <defs>
        <radialGradient id="celestial-grad" cx="90%" cy="0%" r="85%">
          <stop offset="0%" stop-color="#4FA1FF"/>
          <stop offset="25%" stop-color="#145CFF"/>
          <stop offset="55%" stop-color="#072288"/>
          <stop offset="85%" stop-color="#040C30"/>
          <stop offset="100%" stop-color="#04060A"/>
        </radialGradient>
        <pattern id="halftone-dots" width="10" height="10" patternUnits="userSpaceOnUse">
          <circle cx="5" cy="5" r="1.1" fill="#90D5FF" fill-opacity="0.3"/>
        </pattern>
      </defs>
      <circle cx="1150" cy="-50" r="720" fill="url(#celestial-grad)" />
      <circle cx="1150" cy="-50" r="720" fill="url(#halftone-dots)" />
      <circle cx="1150" cy="-50" r="720" fill="none" stroke="#74D8FF" stroke-width="1.2" stroke-opacity="0.75" />
      <circle cx="1150" cy="-50" r="735" fill="none" stroke="#74D8FF" stroke-width="0.8" stroke-dasharray="3 6" stroke-opacity="0.35" />
      <circle cx="1150" cy="-50" r="820" fill="none" stroke="#74D8FF" stroke-width="0.6" stroke-dasharray="1 8" stroke-opacity="0.2" />
      <circle cx="1150" cy="-50" r="920" fill="none" stroke="#2F83FF" stroke-width="0.5" stroke-opacity="0.15" />
      <g transform="translate(680, 240)" opacity="0.6">
        <line x1="-12" y1="0" x2="12" y2="0" stroke="#74D8FF" stroke-width="1"/>
        <line x1="0" y1="-12" x2="0" y2="12" stroke="#74D8FF" stroke-width="1"/>
        <circle cx="0" cy="0" r="4" fill="none" stroke="#74D8FF" stroke-width="0.8"/>
        <text x="16" y="4" fill="#74D8FF" font-family="monospace" font-size="9" letter-spacing="1">RAD: 720.00 KM</text>
      </g>
      <line x1="1150" y1="-50" x2="350" y2="520" stroke="#74D8FF" stroke-opacity="0.08" stroke-width="1" stroke-dasharray="4 8" />
    </svg>
    <div class="beam"><div class="beam-pulse"></div></div>
  </div>
  <main class="pulse-sheet">...</main>
</body>
```

```css
body.quantum-pulse {
  background-color: var(--canvas);
  background-image: 
    radial-gradient(circle at 50% 50%, rgba(20, 92, 255, 0.05) 0%, transparent 80%),
    radial-gradient(circle, rgba(143, 169, 214, 0.2) 1px, transparent 1.5px);
  background-size: 100% 100%, 24px 24px;
}
.pulse-sheet { position: relative; z-index: 1; max-width: var(--container); margin: 0 auto; padding: 0 48px; }
.wrap { max-width: 980px; margin: 0 auto; width: 100%; }
.ambient { position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
.energy-surface { position: absolute; top: 0; right: 0; width: 100%; height: 100%; overflow: visible; }
.beam { position: absolute; width: 140vw; height: 1.5px; left:-20vw; top: 62vh; transform: rotate(-16.5deg); background: linear-gradient(90deg, transparent 0%, rgba(116,216,255,0.05) 15%, rgba(116,216,255,0.14) 50%, rgba(47,131,255,0.08) 85%, transparent 100%); }
.beam-pulse { position: absolute; top: -4px; left: 0; width: 170px; height: 10px; display: flex; align-items: center; justify-content: center; pointer-events: none; animation: beamGliding 20s cubic-bezier(0.28, 0, 0.28, 1) infinite; }
.beam-pulse::before { content: ""; width: 100%; height: 2.8px; clip-path: polygon(0% 50%, 35% 15%, 50% 0%, 65% 15%, 100% 50%, 65% 85%, 50% 100%, 35% 85%); background: linear-gradient(90deg, rgba(116,216,255,0) 0%, rgba(20,92,255,0.25) 25%, rgba(116,216,255,0.65) 42%, rgba(240,248,255,0.85) 50%, rgba(116,216,255,0.65) 58%, rgba(20,92,255,0.25) 75%, rgba(116,216,255,0) 100%); filter: drop-shadow(0 0 2.5px rgba(116, 216, 255, 0.55)); }
@keyframes beamGliding { 0% { transform: translateX(-220px); opacity: 0; } 2.5% { opacity: 0.85; } 28% { opacity: 0.85; } 33% { transform: translateX(145vw); opacity: 0; } 100% { transform: translateX(145vw); opacity: 0; } }
.matrix-stars { position: absolute; inset: 0; pointer-events: none; }
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
.pulse-panel { position: relative; background: var(--surface-1); box-shadow: var(--shadow-panel); padding: 24px; clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 0 100%); }
.pulse-panel::before { content: ""; position: absolute; inset: 0; pointer-events: none; clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 0 100%, 0 0, 1px 1px, 1px calc(100% - 1px), calc(100% - 1px) calc(100% - 1px), calc(100% - 1px) 14.4px, calc(100% - 14.4px) 1px, 1px 1px); background-color: rgba(143, 169, 214, 0.12); }
.pulse-panel.selected::before { background-color: var(--border-strong); box-shadow: var(--shadow-panel), 0 0 22px rgba(20, 92, 255, .22); }
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

### 5. Signal admonition (智能语义提示框)

核心结论、前置摘要与关键提炼**默认使用冷蓝/电光蓝高光**，严禁滥用黄色 warning 破坏黑蓝科技感；仅在真正的系统错误、阻断警示或重大风险时才启用 `.warning`：

```html
<!-- 标准核心结论 / 关键洞见 (默认推荐) -->
<aside class="signal-note">
  <strong>核心结论 // CORE TAKEAWAYS</strong>
  <p>将假设和证据分开标注，避免把推演当成事实。保持信号纯净与逻辑可验证。</p>
</aside>

<!-- 极少数明确的高危警告变体 -->
<aside class="signal-note warning">
  <strong>风险提示 // CRITICAL WARNING</strong>
  <p>破坏性迁移操作不可逆，执行前必须确认全量快照已经落盘。</p>
</aside>
```

```css
.signal-note, .admonition {
  border: 1px solid var(--border);
  border-left: 3px solid var(--signal-electric);
  background: linear-gradient(90deg, rgba(20, 92, 255, 0.12), rgba(12, 18, 31, 0.9));
  padding: 16px 20px;
  box-shadow: var(--shadow-panel);
}
.signal-note strong, .admonition-title {
  color: var(--signal-cyan);
  font: 700 12px var(--font-mono);
  letter-spacing: .08em;
  text-transform: uppercase;
  display: block;
  margin-bottom: 6px;
}
.signal-note p, .admonition p {
  color: var(--text-secondary);
  font-size: 14.5px;
  line-height: 1.7;
}
.signal-note.warning, .admonition.warning {
  border-left-color: var(--status-amber);
}
.signal-note.error, .admonition.error {
  border-left-color: var(--status-red, #FF5A78);
}
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
7. 不要滥用暖色警示黄（`--status-amber`），常规核心结论、洞见和引言一律使用冷蓝/电光蓝。

---

## 7. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配量子脉冲黑蓝风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: true,
    background: "#080D16",
    primaryColor: "#0E1726",
    primaryTextColor: "#F7FAFF",
    primaryBorderColor: "#2F83FF",
    lineColor: "#74D8FF",
    secondaryColor: "#131E34",
    tertiaryColor: "#04060A",
    fontFamily: '"IBM Plex Mono", "Inter", sans-serif'
  }
});
```
