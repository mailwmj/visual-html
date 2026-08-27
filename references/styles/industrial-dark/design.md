# Industrial Dark (暗黑极客工业风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Industrial Dark 将冷峻的工业工程手册与精密技术档案美学升华为界面语言。全站以接近纯黑的冷色调 `#090C0B` 为画布，辅以极淡的 CAD 技术标尺网格（2.5%~4.5% 不透明度），构建出如同 CAD 蓝图、硬件规格书一般的严谨骨架。

界面的核心魅力在于**绝对的理性与克制**。拒绝任何无意义的软糯渐变、大圆角与模糊重阴影；所有模块采用 0–2px（极限 ≤4px）硬边几何、1px 锐利边框与深黑实心 Surface（`#0D1110`），形成物理级阻断层，确保底层标尺网格绝不穿透干扰文本。色彩严格收敛：信号绿（`#67E38B`）作为唯一主通道标识活跃状态与核心数据，信号紫（`#8C7CFF`）仅用于第二状态对比（用量 ≤ 绿色的 40%），警告黄（`#E7E65D`）极度克制。整体呈现出精密、克制、高精度且值得工程信赖的硬核极客气质。

---

## 2. Color Palette & Roles

### Core Interface Colors

| Role | Value | Hex | CSS Token / Source | Usage |
|---|---|---|---|---|
| Background (Canvas) | `rgb(9, 12, 11)` | `#090C0B` | `--bg` | 全局页面画布基底 |
| Background (Deep) | `rgb(6, 8, 8)` | `#060808` | `--bg-deep` | 凹陷区域、终端底座、输入框底色 |
| Surface (Card / Panel) | `rgb(13, 17, 16)` | `#0D1110` | `--surface-1` | 实体卡片、模块底座（阻断网格） |
| Surface (Elevated) | `rgb(17, 22, 21)` | `#111615` | `--surface-2` | 悬浮卡片、下拉菜单、交互浮层 |
| Text (Primary) | `rgb(242, 243, 239)` | `#F2F3EF` | `--text-primary` | 大标题、核心数值、主阅读正文 |
| Text (Secondary) | `rgb(168, 173, 168)` | `#A8ADA8` | `--text-secondary` | 说明段落、次级标签、导读副标题 |
| Text (Muted) | `rgb(111, 118, 114)` | `#6F7672` | `--text-muted` | 注释、禁用状态、等宽元数据标签 |
| Border (Default) | `rgb(42, 48, 46)` | `#2A302E` | `--border` | 容器外框、1px 分割线、表格线 |
| Border (Strong / Focus) | `rgb(64, 71, 67)` | `#404743` | `--border-strong` | 活跃边框、高对比线、外描边 |

### Accent & Signal Palette

| Channel | Role | Value | Hex | Token | Usage Boundary |
|---|---|---|---|---|---|
| **Primary Signal** | 信号绿 (Active / Focus) | `rgb(103, 227, 139)` | `#67E38B` | `--signal-green` | Eyebrow、主序号、核心高亮指标、CTA (占 3–5%) |
| **Secondary Signal** | 信号紫 (Selected / Alt) | `rgb(140, 124, 255)` | `#8C7CFF` | `--signal-violet` | 推荐卡片描边、对比矩阵高亮列 (≤ 绿色的 40%) |
| **Warning / Alert** | 警告黄 (Caution / Note) | `rgb(231, 230, 93)` | `#E7E65D` | `--warning` | 警告便签、极少量警示角标 (占 < 1%) |
| **Soft Green** | 柔光绿 (Subtle Glow) | `rgb(160, 240, 183)` | `#A0F0B7` | `--signal-green-soft` | 局部微文字高光与次级数据 |

### CSS Design Tokens

```css
:root {
  /* 背景层 */
  --bg: #090C0B;
  --bg-deep: #060808;
  --surface-1: #0D1110;
  --surface-2: #111615;

  /* 文字层 */
  --text-primary: #F2F3EF;
  --text-secondary: #A8ADA8;
  --text-muted: #6F7672;

  /* 边框与网格 */
  --border: #2A302E;
  --border-strong: #404743;
  --grid-line: rgba(130, 150, 140, .04);

  /* 信号色通道 */
  --signal-green: #67E38B;
  --signal-green-soft: #A0F0B7;
  --signal-violet: #8C7CFF;
  --warning: #E7E65D;

  /* 尺寸与间距 */
  --radius: 2px;
  --radius-sm: 1px;
  --radius-pill: 2px;
  --container: 1240px;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 96px;
  --space-10: 128px;

  /* 字体栈 */
  --font-display: "Inter", -apple-system, BlinkMacSystemFont, "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", "Roboto Mono", monospace;
}
```

### Color Distribution Philosophy

- **60% 基底暗色** (`#090C0B`, `#0D1110`)：奠定深邃沉静的工业机房与控制台底色。
- **30% 高清晰度文字与冷灰边框** (`#F2F3EF`, `#2A302E`)：保证极端严苛的 WCAG AAA 级别可读性。
- **7% 结构化辅助色** (`#A8ADA8`, `#111615`)：用于卡片微层级与参数注释。
- **3% 信号色** (`#67E38B`, `#8C7CFF`)：精准点亮视觉锚点，严禁出现大面积彩色色块平涂。

---

## 3. Typography Rules

### Font Stacks & Type System

- **Display & Interface Text**: `--font-display` (`"Inter", "PingFang SC", "HarmonyOS Sans SC", sans-serif`)
- **Code, Specs, Indices & Metadata**: `--font-mono` (`"IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", monospace`)

### Type Hierarchy Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 64px~84px | 800 | 1.0 (64~84px) | **-0.035em** | `--font-display` | 页面第一视觉主标题（支持中文主动换行） |
| **Section Title** | `h2.section-title` | 32px~40px | 700 | 1.15 (37~46px) | **-0.02em** | `--font-display` | 章节二级大标题 |
| **Card Title** | `h3`, `.card-title`| 18px~20px | 600 | 1.3 (24~26px) | -0.01em | `--font-display` | 模块/卡片核心标题 |
| **Subsection** | `h4` | 15px | 600 | 1.4 (21px) | normal | `--font-display` | 次级子模块标题 |
| **Lead Paragraph** | `.lead` | 18px | 400 | 1.6 (28.8px) | normal | `--font-display` | 核心摘要导读段落 |
| **Body Text** | `p`, `.body` | 14px~15px | 400 | 1.65 (23~25px)| normal | `--font-display` | 长篇正文与解析说明 |
| **Section Eyebrow**| `.eyebrow` | 12px~13px | 500 | 1.0 (12~13px) | **0.08em** | `--font-mono` | 章节大写索引标头（`◆ 02 / SYSTEM`） |
| **Stat Metric** | `.stat-val` | 48px~56px | 800 | 1.0 (48~56px) | -0.025em | `--font-display` | 核心量化指标超大数值 |
| **Spec Unit / Tag**| `.unit`, `.tag` | 11px~12px | 500 | 1.2 (14px) | **0.06em** | `--font-mono` | 规格单位、大写状态标签、Badge |
| **Code Snippet** | `code`, `pre` | 13px | 500 | 1.55 (20px) | normal | `--font-mono` | 代码块、终端输出、API 参数 |
| **Metadata Footer**| `footer .meta` | 12px | 400 | 1.4 (17px) | 0.05em | `--font-mono` | 底部对齐的技术元数据 |

### Typography Principles

1. **紧凑负字距 (Negative Tracking)**：Hero 标题使用 `-0.035em`，Section 标题使用 `-0.02em`，呈现如同机械冲压铭牌般的凝聚力；正文恢复 `normal`；Mono 标签开启 `0.06em~0.08em` 正字距以提升小字辨识度。
2. **三字重约束**：全站严格使用 `400`（正文）、`600`（小标题/标签）、`800`（大标题/核心数据），杜绝随意使用 300 或 900。

---

## 4. Component Stylings & Interaction Matrix

### Interactive State Matrix

| Component / State | Default | Hover | Active / Pressed | Focus (Keyboard) | Disabled |
|---|---|---|---|---|---|
| **Standard Card (`.num-card`)** | Bg: `#0D1110`<br>Border: `1px solid #2A302E`<br>Text: `#F2F3EF` | Bg: `#111615`<br>Border: `1px solid #404743`<br>Transform: `translateY(-2px)` | Bg: `#0D1110`<br>Transform: `translateY(0)` | Box-Shadow: `0 0 0 2px #090C0B, 0 0 0 4px #67E38B` | Bg: `#090C0B`<br>Opacity: `0.45`<br>Border: `1px solid #1B211F` |
| **Selected Card (`.selected`)** | Bg: `#0D1110`<br>Border: `1px solid #8C7CFF`<br>Glow: `0 0 16px rgba(140,124,255,0.18)` | Bg: `#13121F`<br>Border: `1px solid #8C7CFF`<br>Transform: `translateY(-2px)` | Bg: `#0D1110`<br>Transform: `none` | Box-Shadow: `0 0 0 2px #090C0B, 0 0 0 4px #8C7CFF` | - |
| **Action Button (`.btn-primary`)** | Bg: `#67E38B`<br>Text: `#090C0B`<br>Font: 600 Mono | Bg: `#A0F0B7`<br>Box-Shadow: `0 2px 8px rgba(103,227,139,0.3)` | Bg: `#52C573`<br>Transform: `scale(0.98)` | Outline: `2px solid #FFFFFF`<br>Outline-Offset: `2px` | Bg: `#2A302E`<br>Text: `#6F7672`<br>Cursor: `not-allowed` |
| **Code Block (`.code-block`)** | Bg: `#0D1110`<br>Border: `1px solid #2A302E` | Border: `1px solid #404743` | - | - | - |
| **Form Input (`input`, `textarea`)** | Bg: `#060808`<br>Border: `1px solid #2A302E`<br>Text: `#F2F3EF` | Border: `1px solid #404743` | - | Border: `1px solid #67E38B`<br>Box-Shadow: `0 0 0 1px #67E38B` | Bg: `#090C0B`<br>Text: `#6F7672` |

### Signature Patterns

#### 1. Hard-Edge Double Focus Ring (工业硬核双环聚焦)
```css
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px #090C0B, 0 0 0 4px var(--signal-green);
  border-radius: 2px;
}
```

#### 2. Section Eyebrow Structure
```html
<div class="eyebrow">
  <span class="diamond">◆</span>
  <span>01 / ARCHITECTURE</span>
</div>
```

### Border Radius Scale

| Token / Value | Usage |
|---|---|
| `0px` | 极限制图网格容器、直角表格单元格、流程图硬节点 |
| `2px` (`--radius`) | 标准工业组件：卡片、代码块、输入框、按钮、状态标签（核心默认值） |
| `4px` (Max) | 允许的最大圆角，仅用于外层弹窗或主容器 |
| `50%` | 极小状态信号灯指示圆点（`size: 8px`） |

---

## 5. Layout & Spacing Principles

### Spacing Scale (4px Base Grid)

| Token | Value | Multiplier | Semantic Usage |
|---|---|---|---|
| `--space-1` | 4px | 1x | 微型组件内边距、图标与文字间隙 |
| `--space-2` | 8px | 2x | 标签 Padding、小按钮垂直间距、表格紧凑单元 |
| `--space-3` | 12px | 3x | 标准表单输入内边距、卡片紧凑间隙 |
| `--space-4` | 16px | 4x | 标准网格 Gap、卡片内边距（移动端） |
| `--space-5` | 24px | 6x | 标准卡片内边距（桌面端）、组件组间距 |
| `--space-6` | 32px | 8x | 章节内部模块间距、统计栏间距 |
| `--space-7` | 48px | 12x | 小章节垂直间隔（Sub-section Margin） |
| `--space-8` | 64px | 16x | 标准主章节垂直间隔（Section Margin） |
| `--space-9` | 96px | 24x | Hero 区域上下留白 |
| `--space-10` | 128px | 32x | 巨幅页面断章留白 |

### Page Layout Dimension Tokens

| Dimension | Value | Role |
|---|---|---|
| `--container` | `1240px` | 页面正文最大宽度（桌面端版心） |
| `--header-height` | `60px` | 固定工业顶栏高度 |
| Page Horizontal Margin | `24px` (桌面端) / `16px` (移动端) | 视口两侧安全外边距 |
| Grid Pitch (Minor) | `32px` | CAD 次级标尺网格步长 |
| Grid Pitch (Major) | `128px` | CAD 主级标尺网格步长 |

---

## 6. Depth, Elevation & Motion

### The Surface Blocking & Shadow-as-Border Technique

Industrial Dark 摒弃扩散模糊阴影，依靠 **实体 Surface 阻断（Surface Occlusion）** 与 **1px 精密边框** 表达层级：

1. **背景标尺层**：`body` 绘制 2.5%~4.5% 不透明度的 CAD 细线网格。
2. **卡片阻断层**：所有卡片必须带有 100% 实心背景色 `#0D1110`，彻底切断底层网格线穿透。
3. **层级提升**：悬浮时不增加模糊半径，仅将边框提亮至 `#404743`，并叠加硬边缘微阴影。

### Shadow Elevation Scale

| Level | Value | Role |
|---|---|---|
| **Base Border** | `0 0 0 1px #2A302E` | 默认卡片边界、参数栏划分 |
| **Hover Lift** | `0 0 0 1px #404743, 0 4px 16px rgba(0, 0, 0, 0.6)` | 卡片悬浮状态微升 |
| **Selected Glow** | `0 0 0 1px #8C7CFF, 0 0 20px rgba(140, 124, 255, 0.18)` | 第二通道推荐态专属微光 |
| **Terminal Drop** | `0 8px 32px rgba(0, 0, 0, 0.75), 0 0 0 1px #2A302E` | 代码块与浮动终端 |
| **Modal / Overlay**| `0 16px 48px rgba(0, 0, 0, 0.9), 0 0 0 1px #404743` | 模态弹窗与大浮层 |

### Motion Tokens

```css
--ease-snap: cubic-bezier(0.16, 1, 0.3, 1);
--duration-fast: 0.15s;
--duration-normal: 0.25s;
```

---

## 7. Do's and Don'ts

### Do's (7 项金律)

1. **Do 使用实心深黑 Surface 阻断网格** — 所有卡片必须使用 `#0D1110`，绝对禁止半透明导致背景网格线切断正文文字。
2. **Do 严格控制圆角在 0–2px** — 保持如工业仪器面板般的硬朗几何边界。
3. **Do 坚持信号绿与信号紫的分工** — 信号绿（`#67E38B`）作为主焦点；信号紫（`#8C7CFF`）仅作第二状态对比（≤绿色的 40%）。
4. **Do 在序号、规格与元数据中使用 Mono 字体** — 强化工程图纸与技术手册的精密感。
5. **Do 保持对比矩阵中紫色推荐列的绝对统一** — 推荐列内的表头、边框、圆点、文字全列统一为紫色，杜绝紫绿杂糅。
6. **Do 使用硬核双环聚焦状态** — 确保键盘导航在黑色画布上具有 100% 的无障碍清晰度。
7. **Do 在大标题中进行中文主动语义断句** — 大字号标题短小精悍，利用 `<br>` 控制视线呼吸。

### Don'ts (7 项红线)

1. **Don't 使用 8px 以上的大圆角** — 大圆角会彻底破坏工业极客风的冷峻精密感。
2. **Don't 使用毛玻璃（Backdrop-filter）或软糯彩色渐变** — 拟物透明或多巴胺渐变在此风格中严格禁止。
3. **Don't 使用大面积彩色色块作为容器背景** — 信号色仅允许出现在 1px 边框、点状指示灯、小胶囊和文字高光上。
4. **Don't 让 CAD 网格线过于显眼** — 背景网格透明度必须控制在 2.5%~4.5% 之间，仅作隐约参考标尺，绝不能喧宾夺主。
5. **Don't 使用字重 700 以下的淡细字体做 Hero 标题** — Hero 大标题必须使用 800 字重，具备强烈的工业视觉压迫感。
6. **Don't 引入第三种暖色杂色（如暖红、亮粉、橙色）** — 保持冷灰、近黑、信号绿与信号紫的纯净技术光谱。
7. **Don't 在卡片悬浮时添加大幅度旋转或弹性回弹动效** — 交互应保持干脆迅速（`0.15s ease`，轻微上浮 2px）。

---

## 8. Responsive Behavior & Breakpoints

### Breakpoint Groups

| Breakpoint | Range | Target Device | Layout Adaptation Rules |
|---|---|---|---|
| **Mobile** | `< 640px` | 手机端 | 页面边距设为 `16px`；Hero 字号降为 `36px~44px`；`cards-3` 变为单列垂直堆叠；参数栏变为 2 列；隐藏次级装饰网格线。 |
| **Tablet** | `640px ~ 1024px` | iPad / 平板 | 页面边距 `24px`；Hero 字号 `48px~56px`；`cards-3` 变为 2 列（第 3 张卡片通栏）；参数栏 4 列紧凑排布。 |
| **Desktop** | `1024px ~ 1400px`| 标准笔记本 / 桌面显示器 | 启用完整 `1240px` 版心；Hero 字号 `64px~76px`；3 列卡片自适应对齐；启用完整 CAD 网格背景。 |
| **Wide** | `> 1400px` | 4K / 超宽带鱼屏 | 版心锁定在 `1240px` 居中；两侧留白铺设完整 CAD 极淡背景网格。 |

---

## 9. 核心特征组件拼装示范 (Signature Component Snippets)

### Quick Reference Tokens

```
Background:        #090C0B (Canvas), #0D1110 (Surface Card), #060808 (Deep Input)
Text primary:      #F2F3EF (Headings & Main Body)
Text secondary:    #A8ADA8 (Explanations & Subtitles)
Text muted:        #6F7672 (Mono Metadata & Footers)
Primary Signal:    #67E38B (Active Green, Eyebrow, Key Stats)
Secondary Signal:  #8C7CFF (Selected Purple, Alt State)
Border:            #2A302E (1px Default), #404743 (Strong)
Radius:            2px (Strict Hard Edge)
Fonts:             Display: Inter, PingFang SC (800 for Hero, 400 for Body)
                   Mono: IBM Plex Mono, JetBrains Mono (500)
Focus Ring:        0 0 0 2px #090C0B, 0 0 0 4px #67E38B
```

### 1. Section Eyebrow + Technical Spec Row (标尺标头与硬件规格栏)

```html
<div class="eyebrow">
  <span class="diamond">◆</span>
  <span>01 / SPECIFICATIONS</span>
</div>

<div class="spec-row">
  <div class="spec">
    <div class="val">8.4<em>TFLOPS</em></div>
    <div class="unit">FP32 COMPUTE / 算力</div>
  </div>
  <div class="spec">
    <div class="val">128<em>GB</em></div>
    <div class="unit">UNIFIED MEMORY / 统一内存</div>
  </div>
  <div class="spec">
    <div class="val">&lt; 1.2<em>ms</em></div>
    <div class="unit">P99 LATENCY / 延迟</div>
  </div>
  <div class="spec">
    <div class="val">99.99<em>%</em></div>
    <div class="unit">SYSTEM AVAILABILITY / 可用性</div>
  </div>
</div>
```

### 2. Industrial Number Cards with Selected State (硬边卡片组与第二通道推荐态)

```html
<div class="cards-3">
  <div class="num-card">
    <div class="num">01</div>
    <h3>标准内核架构</h3>
    <p>提供基础并发调度与分布式管道管理，保障常规负载下的稳定运行。</p>
  </div>
  
  <!-- 推荐状态使用 .selected 激活紫色第二通道 -->
  <div class="num-card selected">
    <div class="tag">RECOMMENDED</div>
    <div class="num">02</div>
    <h3>异构加速引擎</h3>
    <p>深度整合 GPU 与 NPU 混合编排流水线，支持零拷贝显存直连与动态显存压缩。</p>
  </div>
  
  <div class="num-card">
    <div class="num">03</div>
    <h3>边缘容灾节点</h3>
    <p>具备毫秒级故障自动切流与本地状态快照回滚能力，确保极端环境零宕机。</p>
  </div>
</div>
```

### 3. Engineering CLI Terminal (工业代码与终端窗口)

```html
<div class="code-block">
  <div class="code-header">
    <div class="controls">
      <span class="ctrl-dot"></span>
      <span class="ctrl-dot"></span>
      <span class="ctrl-dot"></span>
    </div>
    <div class="code-title">deploy-cluster.sh</div>
    <div class="code-badge">BASH</div>
  </div>
  <pre><code class="language-bash"><span class="token-comment"># 启动分布式集群与工业控制节点</span>
<span class="token-function">curl</span> -sSL https://cluster.internal/install.sh | <span class="token-function">bash</span> -- --nodes=8
<span class="token-keyword">export</span> CLUSTER_SECRET=<span class="token-string">"sec_industrial_984"</span>
<span class="token-keyword">systemctl</span> enable --now cluster-daemon</code></pre>
</div>
```

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配暗黑极客工业风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: true,
    background: "#0D1110",
    primaryColor: "#131924",
    primaryTextColor: "#F2F3EF",
    primaryBorderColor: "#67E38B",
    lineColor: "#67E38B",
    secondaryColor: "#1B2433",
    tertiaryColor: "#090C0B",
    fontFamily: '"IBM Plex Mono", Consolas, monospace'
  }
});
```
