# Pixel Pop (日系像素波普风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Pixel Pop（日系像素波普风 / Houkago Vibe）将 90 年代街机像素美学、高饱和波普色彩与现代看板排版融为一体。界面以**高饱和亮蓝底色（`#0b45f3`）搭配全屏 Sunburst 阳光射线旋转放射渐变**与彩色波点为环境层，正文区域收敛承托于**浅奶油色整体看板画布（`--surface-board: #fcf9f2`）**内，在释放强烈青春张力的同时，确保长文阅读的极致清晰度与专注度。

界面的核心魅力在于**Sunburst 放射渐变背景、浅奶油看板、粗黑描边与 5px/10px 纯黑硬投影（Sunburst Rays, Cream Board & Pop Shadows）**：

1. **全屏 Sunburst 放射环境层（Layer 0: `.global-bg` + `.global-dots`）**：
   - 采用多色 Conic 放射渐变（荧光青蓝 `#43c2f0`、糖果西瓜粉 `#f76a9f`、鲜绿 `#19d15e`、明黄 `#ffde00`），配合点阵波点层，形成强烈的波普空间冲击力。
2. **浅奶油整体看板画布（Layer 1: `main.container`）**：
   - 为避免背景放射线条干扰正文阅读，所有正文章节包裹在 32px 大圆角奶油看板（`#fcf9f2`，搭配 4px 粗黑边框与 10px 硬投影）中，背景退居为氛围。
3. **粗黑描边与硬阴影（Layer 2: Pop Solid Shadows）**：
   - 告别所有模糊弥散阴影，全面使用纯黑实色 5px 偏移硬投影（`box-shadow: 5px 5px 0 #111111`）与 3px 实线描边。
4. **蜡笔手绘质感微点缀（Layer 3: Crayon Filter Decorators）**：
   - 蜡笔置换滤镜（`filter: url(#crayon-filter)`）严格仅应用于背景散落的装饰性线条与多边形（`.decorator`），绝不作用于文字与可读内容，保障极致文本清晰度。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background Base (Blue) | `rgb(11, 69, 243)` | `#0b45f3` | `--bg-base` | 全局亮蓝环境底色 |
| Surface Board (Cream) | `rgb(252, 249, 242)` | `#fcf9f2` | `--surface-board` | 正文整体浅奶油看板画布 |
| Surface Card (Pure White) | `rgb(255, 255, 255)` | `#ffffff` | `--surface-card` | 内部普通卡片底色 |
| Surface Card (Yellow Alt) | `rgb(255, 253, 230)` | `#fffde6` | `--surface-card-alt` | 内部高亮推荐卡片底色 |
| Text Main (Bold Black) | `rgb(17, 17, 17)` | `#111111` | `--text-main` | 粗黑主文字、硬阴影颜色 |
| Text Light (Hero White) | `rgb(255, 255, 255)` | `#ffffff` | `--text-light` | Hero 大标题白字 |
| Text Muted (Charcoal) | `rgb(85, 85, 85)` | `#555555` | `--text-muted` | 正文段落描述、次级说明文字 |

### Pop Accent Palette

| Channel | Role | Value | Hex | Usage Boundary |
|---|---|---|---|---|
| **Candy Pink** | 糖果西瓜粉 | `rgb(247, 106, 159)` | `#f76a9f` | 大号数字、重要标签、时间轴圆点 (占 3–5%) |
| **Electric Cyan** | 荧光青蓝 | `rgb(67, 194, 240)` | `#43c2f0` | 章节二级标题背景块、复制按钮 (占 3–5%) |
| **Vibrant Yellow** | 明黄色 | `rgb(255, 222, 0)` | `#ffde00` | Eyebrow 标头、步骤序号圆角块、高亮 Tab (占 4%) |
| **Fresh Green** | 鲜绿强调色 | `rgb(25, 209, 94)` | `#19d15e` | 推荐卡片标签、引用左边条、优势清单 (占 3%) |

### Color Distribution Philosophy

- **55% 亮蓝与 Sunburst 渐变环境** (`#0b45f3`)：营造街机波普青春氛围。
- **25% 浅奶油看板画布** (`#fcf9f2`)：隔离背景干扰，承载长文阅读。
- **12% 纯白与浅黄内层卡片** (`#ffffff`, `#fffde6`)：构建模块层次。
- **8% 高饱和波普四色** (`#f76a9f`, `#43c2f0`, `#ffde00`, `#19d15e`)：信号聚焦与操作反馈。

### CSS Design Tokens

```css
:root {
  /* Base Colors */
  --bg-base: #0b45f3;
  --surface-board: #fcf9f2;
  --surface-card: #ffffff;
  --surface-card-alt: #fffde6;
  --text-main: #111111;
  --text-light: #ffffff;
  --text-muted: #555555;
  
  /* Signal Accent Colors */
  --c-green: #19d15e;
  --c-pink: #f76a9f;
  --c-yellow: #ffde00;
  --c-cyan: #43c2f0;
  
  /* Typography */
  --font-mono: 'Press Start 2P', monospace;
  --font-code: 'JetBrains Mono', Consolas, monospace;
  --font-sans: 'Varela Round', -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  
  /* Borders & Shadows */
  --pop-border-thick: 4px solid var(--text-main);
  --pop-border: 3px solid var(--text-main);
  --pop-border-thin: 2px solid var(--text-main);
  --pop-shadow-lg: 10px 10px 0 var(--text-main);
  --pop-shadow-md: 5px 5px 0 var(--text-main);
  --pop-shadow-sm: 3px 3px 0 var(--text-main);
  
  /* Radii & Layout */
  --radius: 20px;
  --radius-sm: 12px;
  --radius-pill: 100px;
  --container: 1160px;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

生成任何 Pixel Pop 页面时，必须严格遵守以下外层三层结构：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <!-- 字体与 CSS Tokens -->
</head>
<body>

<!-- Layer 0: 全局固定 Sunburst 放射渐变与波点 -->
<div class="global-bg"></div>
<div class="global-dots"></div>

<!-- 装饰性蜡笔滤镜 (仅用于 SVG Decorators) -->
<svg width="0" height="0" style="position:absolute;z-index:-1;">
  <filter id="crayon-filter">
    <feTurbulence type="fractalNoise" baseFrequency="0.4" numOctaves="3" result="noise" />
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="4" xChannelSelector="R" yChannelSelector="G" />
  </filter>
</svg>

<!-- Hero 悬浮于放射背景上 -->
<div class="hero-wrapper">
  <div class="eyebrow"><span class="diamond"></span><span>01 / EXECUTIVE SUMMARY</span></div>
  <h1 class="hero">PIXEL POP<br>WEB SYSTEM</h1>
  <p class="lead">青春高饱和日系波普设计。全屏放射渐变与像素点阵环绕...</p>
</div>

<!-- Layer 1: 正文整体浅奶油看板画布 (所有组件包裹在 main.container 内) -->
<main class="container">
  <!-- 页面各 Section 自上而下排列 -->
</main>

<footer>
  <!-- 页脚元数据 -->
</footer>

</body>
</html>
```

---

## 4. Typography Scale & Rules

### Font Stacks & Type System

- **Display & Interface Text**: `--font-sans` (`'Varela Round', -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif`) — 圆润友好、清晰易读的现代无衬线体。
- **Pixel Display & Badges**: `--font-mono` (`'Press Start 2P', monospace`) — 复古 8-bit 像素字体，用于 Eyebrow、大标题、数字编号、代码指示。
- **Code & API Text**: `--font-code` (`'JetBrains Mono', Consolas, monospace`) — 终端代码与语法高亮。

### Type Hierarchy Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | clamp(32px, 5vw, 64px) | 700 | 1.2 | -0.02em | `--font-mono` | 像素大标题（双层粗黑投影） |
| **Section Title** | `h2.section-title` | clamp(20px, 2.8vw, 28px) | 700 | 1.2 | -0.01em | `--font-mono` | 荧光青底色微倾斜标题块（`-1deg`） |
| **Card Title** | `h3` | 18px~20px | 700 | 1.3 | normal | `--font-sans` | 模块/卡片核心标题 |
| **Lead Paragraph** | `p.lead` | clamp(16px, 1.8vw, 20px) | 400 | 1.7 | normal | `--font-sans` | 导读段落（白色描边阴影） |
| **Body Text** | `p` | 15px | 400 | 1.65~1.7 | normal | `--font-sans` | 正文阅读长文本（次级墨黑） |
| **Eyebrow** | `.eyebrow` | 11px~12px | 700 | 1.0 | 0.06em | `--font-mono` | 明黄胶囊微倾标头（`-2deg`） |
| **Stat Metric** | `.stat-val` | clamp(34px, 4vw, 48px) | 700 | 1.0 | -0.02em | `--font-mono` | 核心量化指标超大数值 |
| **Pill Tag** | `.tag` | 11px | 700 | 1.0 | 0.05em | `--font-mono` | 纯黑描边彩色胶囊标签 |

---

## 5. Component Stylings & Interactive State Matrix

### Interactive State Matrix

| Component / State | Default | Hover | Active / Pressed | Focus (Keyboard) | Disabled |
|---|---|---|---|---|---|
| **Pop Card (`.num-card`, `.feat-card`)** | Bg: `#ffffff`<br>Border: `3px solid #111`<br>Shadow: `5px 5px 0 #111` | Transform: `translateY(-4px)`<br>Shadow: `10px 10px 0 #111` | Transform: `translateY(0)`<br>Shadow: `2px 2px 0 #111` | Outline: `3px solid #ffde00`<br>Outline-Offset: `3px` | Bg: `#eee`<br>Opacity: `0.5`<br>Shadow: `none` |
| **Selected Card (`.selected`)** | Bg: `#fffde6`<br>Border: `3px solid #111`<br>Shadow: `5px 5px 0 #111` | Transform: `translateY(-6px)`<br>Shadow: `10px 10px 0 #111` | Transform: `translateY(0)`<br>Shadow: `2px 2px 0 #111` | Outline: `3px solid #19d15e`<br>Outline-Offset: `3px` | - |
| **Tab Button (`.tab`)** | Bg: `#ffffff`<br>Border: `2px solid #111`<br>Shadow: `3px 3px 0 #111` | Bg: `#fffde6`<br>Transform: `translateY(-2px)`<br>Shadow: `3px 3px 0 #111` | Bg: `#ffde00`<br>Transform: `translate(1px, 1px)`<br>Shadow: `1px 1px 0 #111` | Outline: `2px solid #43c2f0`<br>Outline-Offset: `2px` | Bg: `#f0f0f0`<br>Text: `#999`<br>Shadow: `none` |
| **Active Tab (`.tab.active`)** | Bg: `#ffde00`<br>Transform: `translateY(-2px)`<br>Shadow: `5px 5px 0 #111` | Transform: `translateY(-3px)`<br>Shadow: `6px 6px 0 #111` | - | Outline: `2px solid #111` | - |
| **Copy Button (`.code-copy-btn`)** | Bg: `#43c2f0`<br>Border: `2px solid #111`<br>Text: `#111` | Bg: `#f76a9f`<br>Text: `#ffffff`<br>Transform: `translateY(-2px)` | Transform: `translateY(0)` | Outline: `2px solid #ffde00` | - |

---

## 6. Layout, Spacing & Card Alignment Principles

### Spacing Scale (4px Base Grid)

| Token | Value | Multiplier | Semantic Usage |
|---|---|---|---|
| `--space-1` | 4px | 1x | 微边距、硬阴影精细偏移 |
| `--space-2` | 8px | 2x | 标签内边距、Tab 间隙 |
| `--space-3` | 12px | 3x | 输入框内边距、标题间隙 |
| `--space-4` | 16px | 4x | 标准网格 Gap、移动端边距 |
| `--space-5` | 24px | 6x | 卡片内边距、组件间距 |
| `--space-6` | 32px | 8x | 章节内部模块间距、大卡片内边距 |
| `--space-7` | 48px | 12x | 小章节垂直留白 |
| `--space-8` | 64px | 16x | 标准章节留白 |

### Mandatory Card Alignment & Anti-Clipping Rule (对齐与防截断铁律)

在多列卡片网格（如 `.feat-grid` 与 `.cards-3`）中，不同卡片的段落文字长度必然存在差异（如 1 行与 2 行）。**必须保证同排卡片底部的操作按钮/Tabs与预览框严格水平对齐，且文字绝不截断**：

1. **Flex 垂直占满与段落自适应**：
   - 卡片容器配置 `display: flex; flex-direction: column; height: 100%;`。
   - 段落描述 `<p>` 配置 `flex-grow: 1; margin-bottom: 20px; line-height: 1.65; word-break: break-word; overflow-wrap: break-word;`。
   - 这样段落自动吸收垂直高度差异，将下方的 `.tabs` 和 `.feat-img-frame` 统一定位在相同的底部基准线上。
2. **Tab 按钮组换行与阴影保护**：
   - `.tabs` 必须使用 `display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 16px 0; padding: 2px 2px 6px 2px;`。
   - **严禁在卡片内 `.tabs` 上直接配置 `overflow-x: auto`**，避免 3px 硬阴影因滚动容器被裁切切断。
3. **全局文字换行防护**：
   - 全局对 `p, h1, h2, h3, h4, li, td, th` 注入 `word-break: break-word; overflow-wrap: break-word;`，彻底杜绝英文字符或中文字符溢出容器。

---

## 7. Depth, Elevation & Motion

### Hard Solid Pop Shadow Technique

Pixel Pop 彻底杜绝任何模糊弥散阴影（Blur = 0），使用纯黑实色物理偏移投影：

```css
/* 大容器看板投影 */
box-shadow: 10px 10px 0 var(--text-main);

/* 标准卡片投影 */
box-shadow: 5px 5px 0 var(--text-main);

/* 小标签与按钮投影 */
box-shadow: 3px 3px 0 var(--text-main);
```

### Elevation Scale Table

| Level | Value | Role |
|---|---|---|
| **Pill Tag & Tab** | `3px 3px 0 #111111` | 胶囊标头、未激活 Tab、规格面板 |
| **Standard Card** | `5px 5px 0 #111111` | 数据卡片、特性卡片、流程步骤 |
| **Hover Pop Card** | `10px 10px 0 #111111` | 卡片悬浮状态强化投影 |
| **Main Board** | `10px 10px 0 #111111` | `main.container` 奶油主看板 |

### Motion Tokens

```css
--ease-pop: cubic-bezier(0.175, 0.885, 0.32, 1.275);
--duration-fast: 0.15s;
--duration-normal: 0.25s;
```

---

## 8. Do's and Don'ts

### Do's (7 项金律)

1. **Do 必须在页面外层配置 `.global-bg`（Sunburst 放射渐变）与 `.global-dots`** — 奠定波普活力空间。
2. **Do 正文必须收敛在 `main.container`（浅奶油看板 `#fcf9f2`）中** — 彻底隔绝背景抢焦。
3. **Do 阴影必须是纯黑 3px/5px/10px 偏移硬投影（`box-shadow: 5px 5px 0 #111`）** — 杜绝任何灰色模糊弥散。
4. **Do 边框使用 2px/3px/4px 粗实线** — 传递复古街机波普冲击力。
5. **Do 卡片使用 `flex-direction: column;` 且描述 `<p>` 配置 `flex-grow: 1`** — 确保同排卡片底部按钮严格水平对齐。
6. **Do 卡片悬浮配置弹性跃升动效（`translateY(-4px)` + 阴影放大）** — 带来街机按键般的干脆手感。
7. **Do 核心强调色使用高饱和粉/黄/绿/青经典波普四色** — 纯正热烈。

### Don'ts (7 项红线)

1. **Don't 丢失 Sunburst 放射渐变背景** — 否则退化为普通简陋蓝底网页。
2. **Don't 将奶油看板画布解体为散装裸块** — 长篇阅读必须有整体浅色背景衬底。
3. **Don't 使用任何灰色半透明模糊弥散阴影（blur > 0）** — 必须是纯黑硬阴影。
4. **Don't 在卡片内 `.tabs` 上使用截断阴影的 `overflow-x: auto`** — 必须使用 `flex-wrap: wrap` 确保阴影完整。
5. **Don't 允许同排卡片的操作按钮因文本长短高低错落** — 必须使用 `flex-grow: 1` 保持底部对齐。
6. **Don't 在正文长文本上使用破坏性位移滤镜** — 滤镜严格仅限非文字装饰 SVG（`.decorator`）。
7. **Don't 混入暗黑冷灰配色** — 保持青春明亮的高能日系基调。

---

## 9. Responsive Behavior & Breakpoints

| Breakpoint | Range | Target Device | Layout Adaptation Rules |
|---|---|---|---|
| **Mobile** | `< 640px` | 手机端 | 看板 Padding 降为 `24px 16px`；Hero 字号 `32px~40px`；卡片网格降为 1 列；Tabs 自动折行包裹。 |
| **Tablet** | `640px ~ 1024px` | iPad / 平板 | 看板 Padding `36px 28px`；Hero 字号 `44px~52px`；卡片网格自适应 2 列；保持 5px 经典硬投影。 |
| **Desktop** | `1024px ~ 1400px`| 标准桌面显示器 | 启用完整 `1160px` 版心；Hero 字号 `56px~64px`；3 列卡片与 2 列特性卡片严格对齐。 |
| **Wide** | `> 1400px` | 4K / 超宽大屏 | 版心锁定 `1160px` 居中；全屏 Sunburst 放射光束舒展全屏。 |

---

## 10. 核心特征组件拼装示范 (Signature Component Snippets)

### 1. Eyebrow + Hero Section (标头与像素大标题)

```html
<div class="hero-wrapper">
  <div class="eyebrow">
    <span class="diamond"></span>
    <span>01 / EXECUTIVE SUMMARY</span>
  </div>
  <h1 class="hero">PIXEL POP<br>WEB SYSTEM</h1>
  <p class="lead">青春高饱和日系波普设计。全屏放射渐变与像素点阵环绕，正文区域由浅奶油整体看板包裹。</p>
</div>
```

### 2. Feature Cards with Bottom Aligned Tabs & Media Frame (对齐特性卡片与媒体预览框)

```html
<div class="feat-grid">
  <!-- 卡片 1 (短文本) -->
  <div class="feat-card">
    <div class="tag">// POP MODE</div>
    <h3>日系像素波普画板</h3>
    <p>特性的详细能力和用户体验描述，文字清晰可辨，排版层次分明。</p>
    
    <div class="tabs">
      <div class="tab active">VIEW // 01</div>
      <div class="tab">VIEW // 02</div>
    </div>
    <div class="feat-img-frame">MEDIA PLACEHOLDER FRAME (400×200)</div>
  </div>

  <!-- 卡片 2 (长文本，由于 flex-grow: 1，下方 tabs 与卡片 1 严格水平对齐) -->
  <div class="feat-card">
    <div class="tag">// RETRO ARCADE</div>
    <h3>街机像素渲染流水线</h3>
    <p>8-bit 复古像素与现代矢量排版的有机结合，兼顾趣味性与生产力交付。</p>
    
    <div class="tabs">
      <div class="tab active">SCHEMA</div>
      <div class="tab">CODE</div>
    </div>
    <div class="feat-img-frame">VECTOR CANVAS FRAME (400×200)</div>
  </div>
</div>
```

### 3. Number Cards (带等宽序号与对齐底部胶囊的编号卡片组)

```html
<div class="cards-3">
  <div class="num-card">
    <div class="num">01</div>
    <h3>清晰可读正文</h3>
    <p>移除了正文容器上的位移滤镜，排版保持极致锐利的矢量渲染与舒适阅读感。</p>
    <div class="tag">BASE</div>
  </div>
  <div class="num-card selected">
    <div class="num">02</div>
    <h3>统一看板底色</h3>
    <p>正文区域增加整体浅色背景看板，彻底隔绝背景放射线条的抢焦。</p>
    <div class="tag">RECOMMENDED</div>
  </div>
  <div class="num-card">
    <div class="num">03</div>
    <h3>波普硬阴影</h3>
    <p>纯黑实色 5px 偏移投影，充满复古电子游戏与波普青春冲击力。</p>
    <div class="tag">POP SHADOW</div>
  </div>
</div>
```

### 4. Pop Admonitions (波普粗边彩色提示框)

```html
<div class="admonition info">
  <div class="admonition-title">★ 核心结论 (INFO)</div>
  <p>这是 AI 提取的关键结论高亮框，用于引起读者对核心发现或前置约束的重点关注。</p>
</div>
```

### 5. Mermaid Diagram Injection (在线增强与离线降级)

```html
<div class="mermaid-wrapper">
  <pre class="mermaid">
graph LR
    A["Raw Input<br/>原始需求文本"] --> B["Parser<br/>语义结构提炼"]
    B --> C["Composer<br/>组件装配渲染"]
    C --> D["Pixel Pop HTML<br/>离线单文件交付"]
    
    style A fill:#FFF8D6,stroke:#000000,stroke-width:2px
    style B fill:#43C2F0,stroke:#000000,stroke-width:2px
    style C fill:#FFDE00,stroke:#000000,stroke-width:2px
    style D fill:#19D15E,stroke:#000000,stroke-width:2px
  </pre>
</div>
```

脚手架可以保留上述 Mermaid 源码供在线引擎增强；最终交付前运行 `references/scripts/bundle_offline.py`，由打包器生成静态 SVG fallback。完全断网交付使用 `--strict`，不能把 CDN 运行时当作必要条件。

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配日系像素波普风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: false,
    background: "#FFFFFF",
    primaryColor: "#FFF8D6",
    primaryTextColor: "#000000",
    primaryBorderColor: "#000000",
    lineColor: "#000000",
    secondaryColor: "#FFDE00",
    tertiaryColor: "#FFFFFF",
    fontFamily: '"JetBrains Mono", Consolas, monospace'
  }
});
```
