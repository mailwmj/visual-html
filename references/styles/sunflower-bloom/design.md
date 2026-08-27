# Sunflower Bloom (向日葵暖阳风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Sunflower Bloom 将大自然向阳而生的生机活力与现代高质量纸质海报排版完美结合。全站以沉静雅致的纸质中度蓝（`#4278A9` / `#4578A6`）为全局画布基底，搭配温润明亮的米白/奶油白（`#F2EAE0`）作为主文本与实体卡片底色，构建出如阳光洒在蓝布与厚纸之上的温暖质感。

界面的核心魅力在于**明朗的向日葵黄焦点与纸面叠加层级（Sunlit Contrast & Paper Layering）**：
1. **向日葵明黄（`#FFC300`）高光点睛**：作为唯一的最高优先级信号通道，点亮关键数据、步骤连接线与核心标题，注入蓬勃向上的生命力；点缀极少许沉稳的茎叶绿（`#6B8E23`）。
2. **纸质扁平叠加与 4px 利落圆角**：卡片采用实色米白（`#F2EAE0`）实体色块打破蓝色背景的单调，配以深蓝墨色文字（`#2A455C`），杜绝厚重模糊阴影，依靠 1px 半透明米白细线（`rgba(242, 234, 224, 0.3)`）建立清晰的纸张叠放层次。
3. **超大字号生机排版**：大标题（Hero Text）采用极大字号与紧凑行高，充满自信与鼓舞人心的力量。

---

## 2. Color Palette & Roles

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token / Source | Usage |
|---|---|---|---|---|
| Background (Denim Blue Canvas) | `rgb(69, 120, 166)` | `#4578A6` | `--bg-primary` | 全局沉静纸质蓝画布底色 |
| Surface (Cream Paper Card) | `rgb(242, 234, 224)` | `#F2EAE0` | `--bg-surface` | 实体米白卡片底色（打破单调） |
| Surface (Pure Hover) | `rgb(255, 255, 255)` | `#FFFFFF` | `--bg-surface-hover` | 卡片悬浮状态纯白提亮 |
| Text (Cream Primary on Blue) | `rgb(242, 234, 224)` | `#F2EAE0` | `--text-primary` | 蓝底上的大标题与正文 |
| Text (Cream Secondary) | `rgba(242, 234, 224, 0.7)` | `rgba(242,234,224,.7)` | `--text-secondary` | 蓝底上的辅助说明与等宽元数据 |
| Text (Deep Ink on Cream) | `rgb(42, 69, 92)` | `#2A455C` | `--text-inverse` | 米白卡片内部深蓝高对比正文 |
| Text (Muted Ink on Cream) | `rgb(83, 117, 147)` | `#537593` | `--text-inverse-muted` | 米白卡片内部辅助说明 |
| Border (Paper Line) | `rgba(242, 234, 224, 0.3)` | `rgba(242,234,224,.3)` | `--border-color` | 1px 半透明米白分割线、卡片边框 |

### Accent & Signal Palette

| Channel | Role | Value | Hex / RGBA | Token | Usage Boundary |
|---|---|---|---|---|---|
| **Sunflower Yellow** | 向日葵明黄 (Core Focal Signal)| `rgb(255, 195, 0)` | `#FFC300` | `--signal-yellow` | 关键指标数字、Eyebrow 方块、高光连接线 (占 3–5%) |
| **Yellow Dim** | 柔黄微底 (Subtle Tint) | `rgba(255, 195, 0, 0.2)`| `rgba(255,195,0,.2)` | `--signal-yellow-dim` | 推荐卡片高光浅底、表格高光列 (占 2%) |
| **Stem Green** | 茎叶绿 (Natural Stem Accent) | `rgb(107, 142, 35)` | `#6B8E23` | `--signal-green` | 极少量成功指示与自然点缀 (占 < 1%) |

### CSS Design Tokens

```css
:root {
  /* 基础色彩 */
  --bg-primary: #4578A6;
  --bg-surface: #F2EAE0;
  --bg-surface-hover: #FFFFFF;
  
  /* 文本色彩 */
  --text-hero: #F2EAE0;
  --text-primary: #F2EAE0;
  --text-secondary: rgba(242, 234, 224, 0.7);
  --text-inverse: #2A455C;
  --text-inverse-muted: #537593;
  
  /* 信号色与强调色 */
  --signal-yellow: #FFC300;
  --signal-yellow-dim: rgba(255, 195, 0, 0.2);
  --signal-green: #6B8E23;
  
  /* 边框与阴影 */
  --border-color: rgba(242, 234, 224, 0.3);
  --border-strong: rgba(242, 234, 224, 0.6);
  --shadow-paper: 0 4px 16px rgba(18, 38, 63, 0.15);
  --shadow-paper-hover: 0 8px 24px rgba(18, 38, 63, 0.25);
  
  /* 尺寸与圆角 */
  --border-radius: 4px;
  --radius-sm: 2px;
  --radius-pill: 20px;
  --container: 1180px;

  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 48px; --space-8: 64px;
  --space-9: 96px; --space-10: 128px;
  
  /* 字体栈 */
  --font-sans: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "Fira Code", "JetBrains Mono", Consolas, monospace;
}
```

---

## 3. Typography Rules

### Font Stacks & Type System

- **Display & Interface Text**: `--font-sans` (`"Helvetica Neue", Helvetica, Arial, "PingFang SC", sans-serif`) — 扎实粗壮的无衬线体。
- **Code, Specs & Metadata**: `--font-mono` (`"Fira Code", "JetBrains Mono", Consolas, monospace`) — 规范等宽字体。

### Type Hierarchy Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 58px~80px | 900 | 1.05 (61~84px) | **-0.03em** | `--font-sans` | 生机勃勃的大字号主标题 |
| **Section Title** | `h2.section-title` | 32px~40px | 800 | 1.15 (37~46px) | -0.015em | `--font-sans` | 章节二级大标题（带黄色左侧粗标） |
| **Card Title** | `h3`, `.card-title`| 18px~20px | 700 | 1.3 (24~26px) | normal | `--font-sans` | 模块/卡片核心标题 |
| **Lead Paragraph** | `.lead` | 18px | 400 | 1.65 (29.7px) | normal | `--font-sans` | 导读段落（米白半透） |
| **Body Text** | `p`, `.body` | 14px~15px | 400 | 1.7 (24~26px) | normal | `--font-sans` | 正文阅读长文本 |
| **Section Eyebrow**| `.eyebrow` | 12px~13px | 600 | 1.0 (12~13px) | **0.06em** | `--font-mono` | 章节黄色方块索引标头 |
| **Stat Metric** | `.stat-val` | 50px~64px | 900 | 1.0 (50~64px) | -0.025em | `--font-sans` | 向日葵黄核心量化指标大字 |
| **Spec Unit / Tag**| `.unit`, `.tag` | 11px~12px | 600 | 1.2 (14px) | **0.05em** | `--font-mono` | 规格单位、等宽大写胶囊 |

---

## 4. Component Stylings & Interaction Matrix

### Interactive State Matrix

| Component / State | Default | Hover | Active / Pressed | Focus (Keyboard) | Disabled |
|---|---|---|---|---|---|
| **Paper Card (`.num-card`)** | Bg: `#F2EAE0`<br>Text: `#2A455C`<br>Border: `1px solid rgba(242,234,224,.3)` | Bg: `#FFFFFF`<br>Transform: `translateY(-3px)`<br>Shadow: `var(--shadow-paper-hover)` | Bg: `#EDE3D5`<br>Transform: `translateY(0)` | Box-Shadow: `0 0 0 2px #4578A6, 0 0 0 4px #FFC300` | Bg: `rgba(242,234,224,.4)`<br>Opacity: `0.5` |
| **Selected Card (`.selected`)** | Bg: `#FFFFFF`<br>Border: `2px solid #FFC300`<br>Shadow: `var(--shadow-paper)` | Bg: `#FFFFFF`<br>Transform: `translateY(-4px)`<br>Shadow: `0 12px 28px rgba(255,195,0,.25)` | Transform: `none` | Box-Shadow: `0 0 0 2px #4578A6, 0 0 0 4px #FFC300` | - |
| **Sunflower Button (`.btn-primary`)** | Bg: `#FFC300`<br>Text: `#2A455C`<br>Font: 700 Sans | Bg: `#FFD033`<br>Box-Shadow: `0 4px 14px rgba(255,195,0,.4)` | Bg: `#E6B000`<br>Transform: `scale(0.98)` | Outline: `2px solid #FFFFFF`<br>Outline-Offset: `2px` | Bg: `rgba(255,195,0,.3)`<br>Text: `#777`<br>Cursor: `not-allowed` |
| **Form Input (`input`)** | Bg: `rgba(242,234,224,.15)`<br>Border: `1px solid rgba(242,234,224,.4)`<br>Text: `#F2EAE0` | Border: `rgba(242,234,224,.8)` | - | Bg: `#F2EAE0`<br>Text: `#2A455C`<br>Border: `1px solid #FFC300` | Opacity: `0.4` |

### Signature Patterns

#### 1. Sunflower Square Eyebrow (向日葵黄方块标头)
```html
<div class="eyebrow">
  <span class="diamond" style="background: #FFC300; width: 8px; height: 8px; border-radius: 2px;"></span>
  <span style="color: rgba(242, 234, 224, 0.8);">02 // BLOOM GROWTH</span>
  <span class="line" style="background: rgba(242, 234, 224, 0.3);"></span>
</div>
```

#### 2. Clean Paper Layering Rule (纸面叠放法则)
```css
.paper-card {
  background: var(--bg-surface);
  color: var(--text-inverse);
  border-radius: var(--border-radius);
  border: 1px solid var(--border-color);
  box-shadow: var(--shadow-paper);
  transition: all 0.2s ease;
}
```

### Border Radius Scale

| Token / Value | Usage |
|---|---|
| `2px` (`--radius-sm`) | 内部微标签、向日葵黄色标、小方块 |
| `4px` (`--border-radius`) | **核心默认值**：纸面卡片、输入框、代码块、对比表格 |
| `20px` (`--radius-pill`) | 全圆角胶囊药丸标签、主行动按钮 |

---

## 5. Layout & Spacing Principles

### Spacing Scale (4px Base Grid)

| Token | Value | Multiplier | Semantic Usage |
|---|---|---|---|
| `--space-1` | 4px | 1x | 微边距、色标微间距 |
| `--space-2` | 8px | 2x | 标签内边距、紧凑垂直间距 |
| `--space-3` | 12px | 3x | 输入框内边距、卡片紧凑间隙 |
| `--space-4` | 16px | 4x | 标准网格 Gap、移动端内边距 |
| `--space-5` | 24px | 6x | 桌面端卡片内边距、组件间距 |
| `--space-6` | 32px | 8x | 章节内部模块间距、统计栏间距 |
| `--space-7` | 48px | 12x | 小章节垂直留白 |
| `--space-8` | 64px | 16x | 标准章节间距 |
| `--space-9` | 96px | 24x | Hero 区域上下呼吸间距 |
| `--space-10` | 128px | 32x | 宽幅展示段落留白 |

### Page Layout Dimension Tokens

| Dimension | Value | Role |
|---|---|---|
| `--container` | `1180px` | 页面正文最大宽度（桌面端版心） |
| Page Horizontal Margin | `24px` (桌面端) / `16px` (移动端) | 视口两侧安全外边距 |

---

## 6. Depth, Elevation & Motion

### Paper Surface Layering Technique

Sunflower Bloom 拒绝复杂的模糊重阴影，依靠 **沉静蓝底与米白厚纸的色块对撞 + 极轻柔的纸面微投影** 表达层级：

```css
box-shadow: 0 4px 16px rgba(18, 38, 63, 0.15);
```

### Shadow Elevation Scale

| Level | Value | Role |
|---|---|---|
| **Base Paper** | `0 4px 16px rgba(18, 38, 63, .15)` | 默认米白卡片、规格面板 |
| **Hover Float**| `0 8px 24px rgba(18, 38, 63, .25)` | 卡片悬浮状态轻微上浮 |
| **Selected Lift**| `0 12px 28px rgba(255, 195, 0, .25)`| 推荐卡片黄色微光浮层 |

### Motion Tokens

```css
--ease-natural: cubic-bezier(0.16, 1, 0.3, 1);
--duration-normal: 0.2s;
```

---

## 7. Do's and Don'ts

### Do's (7 项金律)

1. **Do 使用沉静中度蓝（`#4578A6`）作为全局纸质画布** — 营造稳重温和的底色。
2. **Do 使用米白卡片（`#F2EAE0`）搭配深蓝文字（`#2A455C`）** — 保证卡片内部极佳阅读对比度。
3. **Do 严格使用向日葵明黄（`#FFC300`）作为核心高光信号色** — 传递向阳生机。
4. **Do 保持 4px 利落纸质小圆角** — 强化整洁有力的纸张边缘感。
5. **Do 使用 1px 半透明米白细线进行模块划分** — 维持画面的干净与连续。
6. **Do Hero 大标题使用 900 粗字重并进行中文主动换行** — 展现积极向上的气势。
7. **Do 在流程步骤中使用黄色实心节点与连接线** — 引导视线顺畅流动。

### Don'ts (7 项红线)

1. **Don't 引入与向日葵黄冲突的刺眼冷紫或高饱和荧光红** — 保持暖阳蓝调的纯净性。
2. **Don't 在卡片上使用厚重漆黑的脏阴影** — 必须使用偏蓝的纸面轻柔阴影。
3. **Don't 使用 16px 以上的大圆角** — 避免破坏纸张海报的干练利落感。
4. **Don't 让米白卡片内部文字使用纯黑（`#000000`）** — 必须使用深蓝墨色（`#2A455C`）。
5. **Don't 在 `<section>` 底部添加生硬的全局分割横线** — 依靠呼吸留白划分章节。
6. **Don't 堆砌大量彩色 emoji** — 使用黄色几何色标与等宽字符替代。
7. **Don't 在卡片悬浮时触发过度夸张的旋转与变形** — 保持 `translateY(-3px)` 的克制上浮。

---

## 8. Responsive Behavior & Breakpoints

### Breakpoint Groups

| Breakpoint | Range | Target Device | Layout Adaptation Rules |
|---|---|---|---|
| **Mobile** | `< 640px` | 手机端 | 页面边距 `16px`；Hero 字号 `36px~44px`；卡片组降为 1 列；参数栏 2 列紧凑排布。 |
| **Tablet** | `640px ~ 1024px` | iPad / 平板 | 页面边距 `24px`；Hero 字号 `48px~56px`；卡片组 2 列自适应；保留 4px 纸质圆角。 |
| **Desktop** | `1024px ~ 1400px`| 标准桌面显示器 | 启用完整 `1180px` 版心；Hero 字号 `58px~72px`；3 列米白厚纸卡片自适应排布。 |
| **Wide** | `> 1400px` | 4K / 超宽大屏 | 版心锁定 `1180px` 居中；两侧舒展完整沉静蓝天幕。 |

---

## 9. 核心特征组件拼装示范 (Signature Component Snippets)

### Quick Reference Tokens

```
Background Canvas: #4578A6 (Denim Paper Blue)
Surface Paper:     #F2EAE0 (Cream White Card)
Text on Blue:      #F2EAE0 (Cream White)
Text on Cream:     #2A455C (Deep Ink Blue)
Accent Yellow:     #FFC300 (Sunflower Bright Yellow)
Accent Green:      #6B8E23 (Stem Green)
Border:            rgba(242, 234, 224, 0.3)
Radius:            4px (Crisp Paper Edge), 20px (Pill Tag)
Fonts:             Sans: Helvetica Neue, PingFang SC (900 for Hero, 400 for Body)
                   Mono: Fira Code, JetBrains Mono (600)
```

### 1. Sunflower Eyebrow + Denim Blue Hero (向日葵黄标头与沉静蓝 Hero)

```html
<section style="background: #4578A6; padding: 64px 0;">
  <!-- 黄色方块索引标头 -->
  <div class="eyebrow">
    <span class="diamond" style="background: #FFC300; width: 8px; height: 8px; border-radius: 2px; display: inline-block;"></span>
    <span style="color: rgba(242, 234, 224, 0.8); font-family: var(--font-mono); font-size: 12px; font-weight: 600;">01 // LIFE BLOOM</span>
    <span class="line" style="background: rgba(242, 234, 224, 0.3); height: 1px; flex: 1;"></span>
  </div>
  
  <h1 class="hero" style="font-size: 64px; font-weight: 900; line-height: 1.05; color: #F2EAE0; margin-top: 20px;">
    向下扎根<br>向阳生长的力量。
  </h1>
  <p class="lead" style="color: rgba(242, 234, 224, 0.8); font-size: 18px; line-height: 1.65; max-width: 680px; margin-top: 16px;">
    以沉静蓝布与暖阳明黄为笔触，记录团队每一阶段的蓬勃成长。
  </p>
</section>
```

### 2. Solid Cream Paper Cards with Deep Ink (米白厚纸卡片组与深蓝墨字)

```html
<div class="cards-3">
  <div class="num-card" style="background: #F2EAE0; color: #2A455C; border-radius: 4px; padding: 24px; box-shadow: 0 4px 16px rgba(18, 38, 63, 0.15);">
    <div class="num" style="font-size: 36px; font-weight: 900; color: #FFC300;">01</div>
    <h3 style="color: #2A455C; font-size: 18px; font-weight: 700; margin: 8px 0;">暖阳生长内核</h3>
    <p style="color: #537593; font-size: 14px; line-height: 1.65;">实色厚纸色块打破背景的单调感，提供清晰沉稳的阅读承托。</p>
  </div>
  
  <!-- 推荐状态使用 .selected 激发黄色实线高光边框 -->
  <div class="num-card selected" style="background: #FFFFFF; color: #2A455C; border-radius: 4px; border: 2px solid #FFC300; padding: 24px; box-shadow: 0 12px 28px rgba(255, 195, 0, 0.25);">
    <div class="tag" style="background: #FFC300; color: #2A455C; font-family: var(--font-mono); font-size: 10px; font-weight: 700; display: inline-block; padding: 2px 8px; border-radius: 20px;">RECOMMENDED</div>
    <div class="num" style="font-size: 36px; font-weight: 900; color: #FFC300; margin: 8px 0;">02</div>
    <h3 style="color: #2A455C; font-size: 18px; font-weight: 700;">蓬勃协同网络</h3>
    <p style="color: #2A455C; font-size: 14px; line-height: 1.65; font-weight: 500;">跨团队信息节点自适应连接，像向日葵花盘般汇聚全员智慧。</p>
  </div>
  
  <div class="num-card" style="background: #F2EAE0; color: #2A455C; border-radius: 4px; padding: 24px; box-shadow: 0 4px 16px rgba(18, 38, 63, 0.15);">
    <div class="num" style="font-size: 36px; font-weight: 900; color: #FFC300;">03</div>
    <h3 style="color: #2A455C; font-size: 18px; font-weight: 700; margin: 8px 0;">深耕知识沉淀</h3>
    <p style="color: #537593; font-size: 14px; line-height: 1.65;">将每一份文档转化为具备长久生命力与审美价值的数字出版物。</p>
  </div>
</div>
```

### 3. Paper Code Terminal (纸质深蓝配置终端)

```html
<div class="code-block" style="background: #1E3A5F; border: 1px solid rgba(242, 234, 224, 0.3); border-radius: 4px; padding: 20px;">
  <div class="code-header" style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(242, 234, 224, 0.2); padding-bottom: 12px; margin-bottom: 16px;">
    <div style="color: #F2EAE0; font-family: var(--font-mono); font-size: 12px;">sunflower-manifest.yaml</div>
    <div style="color: #FFC300; font-family: var(--font-mono); font-size: 11px; font-weight: 700;">YAML</div>
  </div>
  <pre><code class="language-yaml"><span style="color: #FFC300;">project</span>: <span style="color: #F2EAE0;">"Sunflower Bloom Editorial"</span>
<span style="color: #FFC300;">theme</span>:
  <span style="color: #FFC300;">canvas</span>: <span style="color: #F2EAE0;">"#4578A6"</span>
  <span style="color: #FFC300;">sunflower_yellow</span>: <span style="color: #F2EAE0;">"#FFC300"</span>
  <span style="color: #FFC300;">leaf_green</span>: <span style="color: #6B8E23;">"#6B8E23"</span></code></pre>
</div>
```

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配向日葵暖阳风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: true,
    background: "#1E3A5F",
    primaryColor: "#2A455C",
    primaryTextColor: "#F2EAE0",
    primaryBorderColor: "#FFC300",
    lineColor: "#FFC300",
    secondaryColor: "#162C46",
    tertiaryColor: "#0F2035",
    fontFamily: '"JetBrains Mono", monospace'
  }
});
```
