# Brutalist Poster (先锋撞色海报风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Brutalist Poster 将先锋艺术书展（Art Book Fair）、酸性设计（Acid Graphic）与瑞士朋克排版（Swiss Punk Typography）升华为一套极具破坏性与视觉张力的界面规范。全站以纯白高对比度画布（`#FFFFFF`）为基底，使用绝对纯黑（`#000000`）构建排版骨架，通过极端悬殊的字号比例与荧光撞色撕裂常规审美。

界面的核心魅力在于**酸性粉绿撞色与破坏性野蛮排版（Brutalist Contrast & Acid Clash）**：
1. **酸性粉（`#FF4591`）与荧光青（`#00E5CC`）的剧烈对抗**：超大号荧光青 Hero 标题叠加在不规则几何粉色色块上，视觉冲击力扑面而来。
2. **破坏性字阶对比**：巨幅大标题（80px~120px，`-0.05em` 紧凑字距，文字甚至溢出当图形使用）与小号精密说明文字形成极端粗暴的比例反差。
3. **原始粗粝质感**：粗黑边框（`2px~3px solid #000`）、8px 纯色硬投影（`8px 8px 0 #00E5CC`）、胶带感反白等宽标签，全无传统 UI 的圆滑讨好，散发前沿独立出版物与艺术海报的先锋锐气。

---

## 2. Color Palette & Roles

### Core Interface Colors

| Role | Value | Hex | CSS Token / Source | Usage |
|---|---|---|---|---|
| Background (Pure Canvas) | `rgb(255, 255, 255)` | `#FFFFFF` | `--bg` | 高对比度纯白画布底色 |
| Text (Absolute Pure Black) | `rgb(0, 0, 0)` | `#000000` | `--text-main` | 正文、粗黑标题、3px 粗外边框 |
| Text (Muted Dark) | `rgb(51, 51, 51)` | `#333333` | `--text-muted` | 次要说明文字、注释段落 |
| Text (Inverse Pure White) | `rgb(255, 255, 255)` | `#FFFFFF` | `--text-inverse` | 胶带标签反白文字、深底文字 |
| Border (Brutalist Black) | `rgb(0, 0, 0)` | `#000000` | `--border-brutal` | 2px/3px 粗黑边框、网格线 |

### Accent & Signal Palette

| Channel | Role | Value | Hex | Token | Usage Boundary |
|---|---|---|---|---|---|
| **Acid Pink** | 酸性亮粉 (Acid Hot Pink) | `rgb(255, 69, 145)` | `#FF4591` | `--signal-pink` | 几何底块、警告贴纸、劣势卡片、强调投影 (占 5–8%) |
| **Fluorescent Cyan** | 荧光青 (Fluorescent Cyan) | `rgb(0, 229, 204)` | `#00E5CC` | `--signal-cyan` | Hero 标题、高亮卡片填充、优势状态、主投影 (占 5–8%) |
| **Raw Black Fill** | 纯黑填色 (Black Block) | `rgb(0, 0, 0)` | `#000000` | `--fill-black` | 胶带反白底座、终端底色 (占 3%) |

### CSS Design Tokens

```css
:root {
  /* 基础色彩 */
  --bg: #FFFFFF;
  --text-main: #000000;
  --text-muted: #333333;
  --text-inverse: #FFFFFF;

  /* 核心酸性撞色通道 */
  --signal-pink: #FF4591;
  --signal-cyan: #00E5CC;

  /* 边框与硬阴影 */
  --border: 3px solid #000000;
  --border-sm: 2px solid #000000;
  --shadow-brutal-cyan: 8px 8px 0px #00E5CC;
  --shadow-brutal-pink: 8px 8px 0px #FF4591;
  --shadow-brutal-black: 6px 6px 0px #000000;

  /* 尺寸与圆角（严格直角） */
  --radius: 0px;
  --radius-sm: 0px;
  --radius-pill: 2px;
  --container: 1200px;

  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 48px; --space-8: 64px;
  --space-9: 96px; --space-10: 128px;

  /* 字体栈 */
  --font-sans: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
  --font-mono: "Courier New", "IBM Plex Mono", Consolas, monospace;
}
```

---

## 3. Typography Rules

### Font Stacks & Type System

- **Display & Interface Text**: `--font-sans` (`"Helvetica Neue", Helvetica, Arial, "PingFang SC", sans-serif`) — 极冷淡瑞士无衬线粗黑体。
- **Tape Badges, Code & Metadata**: `--font-mono` (`"Courier New", "IBM Plex Mono", monospace`) — 打字机等宽字体。

### Type Hierarchy Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 76px~110px | 900 | 0.92 (70~101px)| **-0.05em** | `--font-sans` | 极度夸张荧光青大标题（文字即图形） |
| **Section Title** | `h2.section-title` | 36px~48px | 900 | 1.05 (38~50px) | **-0.03em** | `--font-sans` | 章节纯黑巨幅标题 |
| **Card Title** | `h3`, `.card-title`| 20px~24px | 800 | 1.2 (24~29px) | -0.01em | `--font-sans` | 模块核心标题 |
| **Lead Paragraph** | `.lead` | 18px~20px | 500 | 1.6 (28~32px) | normal | `--font-sans` | 导读段落（大反差排版） |
| **Body Text** | `p`, `.body` | 14px~15px | 400 | 1.65 (23~25px)| normal | `--font-sans` | 正文阅读文本 |
| **Tape Eyebrow** | `.eyebrow` | 12px~13px | 700 | 1.0 (12~13px) | **0.1em** | `--font-mono` | 胶带式反白索引标头 |
| **Stat Metric** | `.stat-val` | 64px~80px | 900 | 0.95 (60~76px) | -0.04em | `--font-sans` | 无限放大的酸性粉/青核心数值 |
| **Typewriter Tag**| `.tag`, `.num` | 11px~12px | 700 | 1.1 (12~13px) | **0.08em** | `--font-mono` | 打字机全大写标签、编号 |

---

## 4. Component Stylings & Interaction Matrix

### Interactive State Matrix

| Component / State | Default | Hover | Active / Pressed | Focus (Keyboard) | Disabled |
|---|---|---|---|---|---|
| **Brutalist Card (`.num-card`)** | Bg: `#ffffff`<br>Border: `3px solid #000`<br>Shadow: `8px 8px 0 #00E5CC` | Bg: `#ffffff`<br>Transform: `translate(-3px, -3px)`<br>Shadow: `12px 12px 0 #FF4591` | Transform: `translate(4px, 4px)`<br>Shadow: `2px 2px 0 #000` | Outline: `3px solid #FF4591`<br>Outline-Offset: `3px` | Bg: `#eee`<br>Opacity: `0.5`<br>Shadow: `none` |
| **Selected Card (`.selected`)** | Bg: `#00E5CC`<br>Border: `3px solid #000`<br>Shadow: `8px 8px 0 #FF4591`<br>Text: `#000` | Transform: `translate(-3px, -3px)`<br>Shadow: `12px 12px 0 #000` | Transform: `translate(4px, 4px)`<br>Shadow: `2px 2px 0 #000` | Outline: `3px solid #000`<br>Outline-Offset: `3px` | - |
| **Acid Button (`.btn-primary`)** | Bg: `#FF4591`<br>Text: `#ffffff`<br>Border: `3px solid #000`<br>Shadow: `6px 6px 0 #000` | Bg: `#00E5CC`<br>Text: `#000000`<br>Transform: `translate(-2px, -2px)`<br>Shadow: `8px 8px 0 #FF4591` | Transform: `translate(4px, 4px)`<br>Shadow: `none` | Outline: `3px solid #00E5CC`<br>Outline-Offset: `3px` | Bg: `#ccc`<br>Text: `#777`<br>Shadow: `none` |
| **Tape Badge (`.tag`)** | Bg: `#000`<br>Text: `#fff`<br>Font: Mono | Bg: `#FF4591`<br>Text: `#fff` | - | - | - |
| **Form Input (`input`)** | Bg: `#ffffff`<br>Border: `3px solid #000`<br>Shadow: `4px 4px 0 #000` | Shadow: `6px 6px 0 #00E5CC` | - | Border: `3px solid #FF4591`<br>Shadow: `6px 6px 0 #00E5CC` | Bg: `#eee`<br>Text: `#888` |

### Signature Patterns

#### 1. Tape-Like Negative Eyebrow (反白胶带标头)
```html
<div class="eyebrow" style="display: inline-block; background: #000000; color: #FFFFFF; padding: 4px 12px; font-family: var(--font-mono); font-weight: 700; border: 2px solid #000000; box-shadow: 4px 4px 0px #00E5CC;">
  // 01 ARCHIVE POSTER //
</div>
```

#### 2. Hero Clashing Background Polygon (酸性几何撞色底块)
```css
.hero-clip-bg {
  background: var(--signal-pink);
  clip-path: polygon(0 0, 100% 4%, 96% 100%, 2% 96%);
  padding: 32px 40px;
}
.hero-clip-bg h1 {
  color: var(--signal-cyan);
  text-shadow: 4px 4px 0px #000000;
}
```

### Border Radius Scale

| Token / Value | Usage |
|---|---|
| `0px` (`--radius`) | **严格直角**：所有卡片、按钮、输入框、表格、步骤条（核心默认值） |
| `2px` (Max) | 仅在极少数内嵌微标签中使用 |

---

## 5. Layout & Spacing Principles

### Spacing Scale (4px Base Grid)

| Token | Value | Multiplier | Semantic Usage |
|---|---|---|---|
| `--space-1` | 4px | 1x | 微边距、硬阴影紧密偏移 |
| `--space-2` | 8px | 2x | 标签内边距、标准 8px 硬投影 |
| `--space-3` | 12px | 3x | 输入框内边距、模块紧凑间距 |
| `--space-4` | 16px | 4x | 标准网格 Gap、移动端内边距 |
| `--space-5` | 24px | 6x | 桌面端卡片内边距、组件间距 |
| `--space-6` | 32px | 8x | 章节内部模块间距、海报色块 Padding |
| `--space-7` | 48px | 12x | 小章节垂直留白 |
| `--space-8` | 64px | 16x | 标准章节间距 |
| `--space-9` | 96px | 24x | Hero 区域上下留白 |
| `--space-10` | 128px | 32x | 巨幅海报断章留白 |

### Page Layout Dimension Tokens

| Dimension | Value | Role |
|---|---|---|
| `--container` | `1200px` | 页面正文最大宽度（桌面端版心） |
| Page Horizontal Margin | `24px` (桌面端) / `16px` (移动端) | 视口两侧安全外边距 |

---

## 6. Depth, Elevation & Motion

### Hard Acid Shadow Technique

Brutalist Poster 彻底抛弃柔和阴影，采用 **3px 纯黑粗边 + 8px 荧光青/酸性粉纯色硬偏移**：

```css
box-shadow: 8px 8px 0px #00E5CC;
```

### Shadow Elevation Scale

| Level | Value | Role |
|---|---|---|
| **Tape Badge** | `4px 4px 0px #00E5CC` | 胶带标签、小按钮 |
| **Standard Card**| `8px 8px 0px #00E5CC` | 默认卡片、规格面板 |
| **Hover Pop** | `12px 12px 0px #FF4591` | 悬浮状态激发粉色大硬投影 |
| **Selected Card**| `8px 8px 0px #FF4591` | 推荐卡片高光硬投影 |

### Motion Tokens

```css
--ease-brutal: steps(2, jump-none);
--duration-fast: 0.1s;
```

---

## 7. Do's and Don'ts

### Do's (7 项金律)

1. **Do 使用酸性粉（`#FF4591`）与荧光青（`#00E5CC`）剧烈撞色** — 形成先锋艺术海报的核心视觉张力。
2. **Do 保持纯白底色（`#FFFFFF`）与绝对纯黑文字（`#000000`）** — 构筑高对比度骨架。
3. **Do 严格使用 0px 直角** — 绝对禁止出现圆滑柔和的圆角。
4. **Do 使用 3px 粗黑实线边框与 8px 纯色硬投影** — 打造纯正的粗野主义拼贴质感。
5. **Do Hero 标题采用紧凑负字距（`-0.05em`）并允许文字溢出/断行** — 强化文字即图形的张力。
6. **Do 使用打字机等宽字体制作胶带感反白标签** — 营造街头独立出版物的先锋感。
7. **Do 在按下态（Active）使用纯物理位移反馈** — `translate(4px, 4px)` 配合阴影完全消失。

### Don'ts (7 项红线)

1. **Don't 使用任何圆角（Border-radius > 2px）** — 圆角会直接瓦解野蛮主义的硬朗骨骼。
2. **Don't 使用任何模糊虚化阴影（Blur > 0）** — 阴影必须是 100% 实心纯色色块。
3. **Don't 使用温和沉闷的低饱和莫兰迪色系** — 必须使用极度纯正的高能酸性荧光色。
4. **Don't 使用 500 以下的细体做大标题** — 标题字重必须是 900 极粗体。
5. **Don't 丢失 3px 粗黑边框** — 缺少黑边会导致撞色色块丧失版画印刷边界。
6. **Don't 堆砌圆滑的拟物渐变与彩色 emoji** — 用粗粝打字机字符与几何多边形替代。
7. **Don't 使用平滑缓慢的贝塞尔动效** — 交互应瞬间切换或使用极快步进（`0.1s`）。

---

## 8. Responsive Behavior & Breakpoints

### Breakpoint Groups

| Breakpoint | Range | Target Device | Layout Adaptation Rules |
|---|---|---|---|
| **Mobile** | `< 640px` | 手机端 | 页面边距 `12px`；Hero 字号 `44px~56px`；卡片降为 1 列；硬阴影偏移降至 `5px 5px 0`。 |
| **Tablet** | `640px ~ 1024px` | iPad / 平板 | 页面边距 `20px`；Hero 字号 `60px~76px`；卡片 2 列错落排布；保留 8px 经典硬投影。 |
| **Desktop** | `1024px ~ 1400px`| 标准桌面显示器 | 启用完整 `1200px` 版心；Hero 字号 `76px~100px`；3 列卡片先锋拼贴对齐。 |
| **Wide** | `> 1400px` | 4K / 超宽大屏 | 版心锁定 `1200px` 居中；两侧纯白画布衬托中央剧烈撞色。 |

---

## 9. 核心特征组件拼装示范 (Signature Component Snippets)

### Quick Reference Tokens

```
Background:        #FFFFFF (Pure White Canvas)
Text Main:         #000000 (Pure Black)
Accent Pink:       #FF4591 (Acid Hot Pink)
Accent Cyan:       #00E5CC (Fluorescent Cyan)
Border:            3px solid #000000
Shadow Cyan:       8px 8px 0px #00E5CC
Shadow Pink:       8px 8px 0px #FF4591
Radius:            0px (Strict Sharp Rectangles)
Fonts:             Display: Helvetica Neue, PingFang SC (900 for Hero, 400 for Body)
                   Mono: Courier New, IBM Plex Mono (700)
```

### 1. Tape-Style Eyebrow + Clashing Hero Section (胶带标头与酸性几何撞色大标题)

```html
<section style="background: #FFFFFF; padding: 64px 0;">
  <!-- 反白胶带感索引标头 -->
  <div class="eyebrow" style="display: inline-block; background: #000000; color: #FFFFFF; padding: 4px 12px; font-family: var(--font-mono); font-weight: 700; border: 2px solid #000000; box-shadow: 4px 4px 0px #00E5CC;">
    // ISSUE 01 // ACID MANIFESTO
  </div>
  
  <!-- 不规则酸性几何背景色块 -->
  <div style="background: #FF4591; clip-path: polygon(0 0, 100% 3%, 97% 100%, 3% 97%); padding: 40px 32px; margin-top: 24px; border: 3px solid #000000; box-shadow: 8px 8px 0px #00E5CC;">
    <h1 class="hero" style="color: #00E5CC; font-size: 72px; font-weight: 900; line-height: 0.95; letter-spacing: -0.05em; text-shadow: 4px 4px 0px #000000; margin: 0;">
      野蛮主义<br>破坏性排版宣言。
    </h1>
  </div>
</section>
```

### 2. Acid Clashing 3-Card Grid (酸性撞色直角卡片组)

```html
<div class="cards-3">
  <div class="num-card" style="background: #FFFFFF; border: 3px solid #000000; box-shadow: 8px 8px 0px #00E5CC; padding: 24px;">
    <div class="tag" style="background: #000000; color: #FFFFFF; font-family: var(--font-mono); display: inline-block; padding: 2px 8px;">TYPE // 01</div>
    <div class="num" style="font-size: 40px; font-weight: 900; color: #000000; margin: 12px 0;">01</div>
    <h3 style="font-size: 20px; font-weight: 900; color: #000000;">瑞士朋克网格</h3>
    <p style="font-size: 14px; color: #333333; line-height: 1.6;">极端悬殊的字阶比例，彻底撕裂平庸温和的常规界面布局。</p>
  </div>
  
  <!-- 推荐状态使用 .selected 填充荧光青实色与亮粉硬阴影 -->
  <div class="num-card selected" style="background: #00E5CC; border: 3px solid #000000; box-shadow: 8px 8px 0px #FF4591; padding: 24px;">
    <div class="tag" style="background: #000000; color: #00E5CC; font-family: var(--font-mono); font-weight: 700; display: inline-block; padding: 2px 8px;">RECOMMENDED</div>
    <div class="num" style="font-size: 40px; font-weight: 900; color: #000000; margin: 12px 0;">02</div>
    <h3 style="font-size: 20px; font-weight: 900; color: #000000;">先锋出版物美学</h3>
    <p style="font-size: 14px; color: #000000; line-height: 1.6; font-weight: 500;">高饱和荧光色块剧烈对抗，直角硬轮廓传递出不可妥协的锐利态度。</p>
  </div>
  
  <div class="num-card" style="background: #FFFFFF; border: 3px solid #000000; box-shadow: 8px 8px 0px #00E5CC; padding: 24px;">
    <div class="tag" style="background: #000000; color: #FFFFFF; font-family: var(--font-mono); display: inline-block; padding: 2px 8px;">TYPE // 03</div>
    <div class="num" style="font-size: 40px; font-weight: 900; color: #000000; margin: 12px 0;">03</div>
    <h3 style="font-size: 20px; font-weight: 900; color: #000000;">破坏性视觉冲击</h3>
    <p style="font-size: 14px; color: #333333; line-height: 1.6;">打字机等宽字体与纯色物理硬投影，还原纯粹原始的地下书展质感。</p>
  </div>
</div>
```

### 3. Street Poster Admonition (街头警告贴纸提示框)

```html
<div class="admonition" style="background: #FFFFFF; border: 3px solid #000000; box-shadow: 8px 8px 0px #FF4591; padding: 20px 24px; margin: 32px 0;">
  <div style="background: #FF4591; color: #FFFFFF; font-family: var(--font-mono); font-weight: 900; padding: 4px 10px; display: inline-block; border: 2px solid #000000;">
    ⚠ WARNING: BRUTALIST OVERDRIVE
  </div>
  <p style="margin-top: 12px; font-size: 15px; font-weight: 700; color: #000000; line-height: 1.6;">
    本章节采用极限对比度排版，文字即图形，请确保在纯白画布上维持纯黑与荧光色块的绝对张力。
  </p>
</div>
```
