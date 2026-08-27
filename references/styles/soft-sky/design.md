# Soft Sky (清透空灵浅蓝风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Soft Sky 将现代生活方式产品与雅致出版物美学融为一体。视觉基调如同破晓时分的天空，纯净、通透、空灵，充满秩序感与温润的呼吸感。全局以浅天蓝流光渐变（`#EAF6FC` → `#F5FBFE` → `#D8EEF8`）为视口固定画布，摈弃生硬显眼的网格线与刺眼杂色，完全依靠高阶流光弥散与纯白半透明玻璃质感构建轻盈开阔的空间感。

界面的核心魅力在于**同色系的纯净层级（Monochromatic Contrast）**。卡片采用半透明纯白 Surface（`rgba(255, 255, 255, 0.82)`）配合微高光内阴影与极淡清透阴影；文字以高可读性的深蓝灰（`#2A3F54`）沉淀重心；信号系统全线依托同色系演进：天蓝（`#4A9FD4`）担当常规索引与标号，高阶蔚蓝（`#0284C7`）担当推荐态与行动高光。整体呈现出如高级纸质包装手册与现代数码杂志般的清雅与从容。

---

## 2. Color Palette & Roles

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token / Source | Usage |
|---|---|---|---|---|
| Background (Canvas Base) | `rgb(234, 246, 252)` | `#EAF6FC` | `--bg` | 页面全局固定渐变底色 |
| Background (Deep Tint) | `rgb(216, 238, 248)` | `#D8EEF8` | `--bg-deep` | 底部沉淀色、凹陷卡片底色 |
| Surface (Glass Card) | `rgba(255, 255, 255, 0.82)` | `rgba(255,255,255,.82)` | `--surface-1` | 半透明纯白主卡片、阅读容器 |
| Surface (Subtle Glass) | `rgba(255, 255, 255, 0.55)` | `rgba(255,255,255,.55)` | `--surface-2` | 规格子格、次级嵌套面板 |
| Text (Primary Ink) | `rgb(42, 63, 84)` | `#2A3F54` | `--text-primary` | 大标题、核心数值、主阅读文字 |
| Text (Secondary) | `rgb(93, 122, 140)` | `#5D7A8C` | `--text-secondary` | 导读段落、次级说明、副标题 |
| Text (Muted) | `rgb(144, 168, 184)` | `#90A8B8` | `--text-muted` | 注释、页脚、等宽元数据标签 |
| Border (Default Glass) | `rgba(93, 179, 232, 0.28)` | `rgba(93,179,232,.28)` | `--border` | 卡片柔和外边框、模块分割线 |
| Border (Strong / Focus) | `rgba(93, 179, 232, 0.48)` | `rgba(93,179,232,.48)` | `--border-strong` | 悬浮高亮外边框、加粗划分线 |

### Accent & Signal Palette

| Channel | Role | Value | Hex / RGBA | Token | Usage Boundary |
|---|---|---|---|---|---|
| **Base Signal** | 天蓝 (Index & Base Accent) | `rgb(74, 159, 212)` | `#4A9FD4` | `--signal-blue` | Eyebrow 标头、常规编号、细边框线 (占 3–5%) |
| **High Accent** | 蔚蓝 / 极光蓝 (Highlight CTA) | `rgb(2, 132, 199)` | `#0284C7` | `--signal-accent` | 推荐卡片高光、实心 Tag、关键 CTA 按钮 (占 2–3%) |
| **Subtle Tint** | 水青 (Soft Glow) | `rgb(127, 194, 234)` | `#7FC2EA` | `--signal-blue-soft` | 局部微光晕与弱交互过渡点缀 |
| **Accent Bg** | 蔚蓝微光底衬 | `rgba(2, 132, 199, 0.06)` | `rgba(2,132,199,.06)` | `--signal-accent-bg` | 推荐列/高亮卡片微光浅底 |

### CSS Design Tokens

```css
:root {
  /* 背景层与渐变 */
  --bg: #EAF6FC;
  --bg-deep: #D8EEF8;
  --surface-1: rgba(255, 255, 255, .82);
  --surface-2: rgba(255, 255, 255, .55);

  /* 文字层 (深蓝灰/灰蓝) */
  --text-primary: #2A3F54;
  --text-secondary: #5D7A8C;
  --text-muted: #90A8B8;

  /* 边框与网格 */
  --border: rgba(93, 179, 232, .28);
  --border-strong: rgba(93, 179, 232, .48);
  --grid-minor: rgba(93, 179, 232, .07);
  --grid-major: rgba(93, 179, 232, .13);

  /* 信号色通道（全同色系演进） */
  --signal-blue: #4A9FD4;
  --signal-blue-soft: #7FC2EA;
  --signal-accent: #0284C7;
  --signal-accent-bg: rgba(2, 132, 199, .06);
  --signal-accent-border: rgba(2, 132, 199, .45);

  /* 阴影与景深 */
  --shadow-card: 0 4px 20px rgba(74, 159, 212, .06), inset 0 1px 0 rgba(255, 255, 255, .95);
  --shadow-card-hover: 0 12px 32px rgba(74, 159, 212, .12), inset 0 1px 0 rgba(255, 255, 255, 1);
  --shadow-card-selected: 0 14px 36px rgba(2, 132, 199, .18), inset 0 1px 0 rgba(255, 255, 255, 1);

  /* 尺寸与圆角 */
  --radius: 14px;
  --radius-sm: 8px;
  --radius-pill: 20px;
  --container: 1180px;

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

  /* 字体栈 (圆润 Display + 精确 Mono) */
  --font-display: "Nunito", -apple-system, BlinkMacSystemFont, "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", monospace;
}
```

### Color Distribution Philosophy

- **55% 浅天蓝渐变基底** (`#EAF6FC` → `#D8EEF8`)：铺设如清晨晴空般的纯净大气层。
- **25% 半透明纯白卡片** (`rgba(255,255,255,0.82)`)：营造轻盈悬浮的纸感毛玻璃。
- **15% 深蓝灰文字与冷蓝描边** (`#2A3F54`, `rgba(93,179,232,0.28)`)：确保清晰雅致的排版对比。
- **5% 同色系蔚蓝信号色** (`#0284C7`, `#4A9FD4`)：精妙点睛，杜绝任何杂色污染。

---

## 3. Typography Rules

### Font Stacks & Type System

- **Display & Interface Text**: `--font-display` (`"Nunito", "PingFang SC", "HarmonyOS Sans SC", sans-serif`)
- **Code, Specs, Numbers & Units**: `--font-mono` (`"IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", monospace`)

### Type Hierarchy Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 56px~76px | 800 | 1.05 (59~80px) | **-0.03em** | `--font-display` | 页面第一视觉主标题（优雅圆润） |
| **Section Title** | `h2.section-title` | 30px~38px | 700 | 1.2 (36~46px) | -0.015em | `--font-display` | 章节二级大标题 |
| **Card Title** | `h3`, `.card-title`| 18px~20px | 700 | 1.35 (24~27px)| normal | `--font-display` | 模块/卡片核心标题 |
| **Lead Paragraph** | `.lead` | 17px~18px | 400 | 1.68 (28~30px)| normal | `--font-display` | 导读段落（雅致通透） |
| **Body Text** | `p`, `.body` | 14px~15px | 400 | 1.7 (24~26px) | normal | `--font-display` | 正文阅读长文本 |
| **Section Eyebrow**| `.eyebrow` | 12px~13px | 600 | 1.0 (12~13px) | **0.06em** | `--font-mono` | 章节大写索引标头（`◆ 02 / STORY`） |
| **Stat Metric** | `.stat-val` | 46px~54px | 800 | 1.0 (46~54px) | -0.02em | `--font-display` | 核心量化指标大数字 |
| **Spec Unit / Tag**| `.unit`, `.tag` | 11px~12px | 600 | 1.2 (14px) | **0.05em** | `--font-mono` | 规格单位、胶囊药丸标签 |
| **Code Snippet** | `code`, `pre` | 13px | 500 | 1.55 (20px) | normal | `--font-mono` | 终端代码、参数高亮 |

---

## 4. Component Stylings & Interaction Matrix

### Interactive State Matrix

| Component / State | Default | Hover | Active / Pressed | Focus (Keyboard) | Disabled |
|---|---|---|---|---|---|
| **Glass Card (`.num-card`)** | Bg: `rgba(255,255,255,.82)`<br>Border: `1px solid rgba(93,179,232,.28)`<br>Shadow: `var(--shadow-card)` | Bg: `rgba(255,255,255,.94)`<br>Transform: `translateY(-3px)`<br>Shadow: `var(--shadow-card-hover)` | Bg: `rgba(255,255,255,.85)`<br>Transform: `translateY(0)` | Box-Shadow: `0 0 0 2px #EAF6FC, 0 0 0 4px #0284C7` | Bg: `rgba(255,255,255,.35)`<br>Opacity: `0.5`<br>Border: `1px solid rgba(93,179,232,.1)` |
| **Selected Card (`.selected`)** | Bg: `rgba(255,255,255,.95)`<br>Border: `1px solid #0284C7`<br>Shadow: `var(--shadow-card-selected)` | Bg: `#FFFFFF`<br>Transform: `translateY(-4px)`<br>Shadow: `0 18px 42px rgba(2,132,199,.22)` | Bg: `rgba(255,255,255,.92)`<br>Transform: `none` | Box-Shadow: `0 0 0 2px #EAF6FC, 0 0 0 4px #0284C7` | - |
| **Action Button (`.btn-primary`)** | Bg: `#0284C7`<br>Text: `#FFFFFF`<br>Font: 600 Nunito | Bg: `#0369A1`<br>Box-Shadow: `0 4px 14px rgba(2,132,199,.3)` | Bg: `#075985`<br>Transform: `scale(0.98)` | Outline: `2px solid #0284C7`<br>Outline-Offset: `2px` | Bg: `rgba(93,179,232,.25)`<br>Text: `#90A8B8`<br>Cursor: `not-allowed` |
| **Pill Tag (`.tag`)** | Bg: `rgba(2,132,199,.08)`<br>Text: `#0284C7`<br>Border: `1px solid rgba(2,132,199,.2)` | Bg: `rgba(2,132,199,.15)` | - | - | - |
| **Form Input (`input`, `textarea`)** | Bg: `rgba(255,255,255,.65)`<br>Border: `1px solid rgba(93,179,232,.3)` | Bg: `rgba(255,255,255,.85)`<br>Border: `rgba(93,179,232,.5)` | - | Bg: `#FFFFFF`<br>Border: `1px solid #0284C7`<br>Box-Shadow: `0 0 0 3px rgba(2,132,199,.15)` | Bg: `rgba(255,255,255,.3)`<br>Text: `#90A8B8` |

### Signature Patterns

#### 1. Soft Atmospheric Double-Ring Focus (清透双环聚焦)
```css
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px #EAF6FC, 0 0 0 4px var(--signal-accent);
  border-radius: 14px;
}
```

#### 2. Section Eyebrow with Rounded Diamond
```html
<div class="eyebrow">
  <span class="diamond" style="border-radius: 2px; background: #4A9FD4;">◆</span>
  <span>02 / LIFESTYLE</span>
  <span class="line" style="background: rgba(93, 179, 232, 0.28);"></span>
</div>
```

### Border Radius Scale

| Token / Value | Usage |
|---|---|
| `8px` (`--radius-sm`) | 内部次级微卡片、代码块、表单输入框 |
| `14px` (`--radius`) | 标准毛玻璃主卡片、对比表格外框、问答折叠框（核心默认值） |
| `20px` (`--radius-pill`) | 胶囊药丸标签、Eyebrow 底框、主行动按钮 |
| `50%` | 时间轴圆点、头像、状态指示灯 |

---

## 5. Layout & Spacing Principles

### Spacing Scale (4px Base Grid)

| Token | Value | Multiplier | Semantic Usage |
|---|---|---|---|
| `--space-1` | 4px | 1x | 微边距、图标与文字微隙 |
| `--space-2` | 8px | 2x | 药丸标签 Padding、输入框垂直边距 |
| `--space-3` | 12px | 3x | 卡片内紧凑间隙、小段落间距 |
| `--space-4` | 16px | 4x | 移动端内边距、标准元素间隙 |
| `--space-5` | 24px | 6x | 桌面端卡片内边距、组件间距 |
| `--space-6` | 32px | 8x | 模块垂直间距、统计栏间隙 |
| `--space-7` | 48px | 12x | 小章节垂直留白 |
| `--space-8` | 64px | 16x | 标准章节间距 |
| `--space-9` | 96px | 24x | Hero 区域上下呼吸间距 |
| `--space-10` | 128px | 32x | 宽幅展示段落留白 |

### Page Layout Dimension Tokens

| Dimension | Value | Role |
|---|---|---|
| `--container` | `1180px` | 页面正文最大宽度（桌面端版心） |
| Global Aurora Canvas | `fixed; inset: 0; z-index: -1` | `body::before` 视口固定层极光渐变 |
| Page Horizontal Margin | `24px` (桌面端) / `16px` (移动端) | 视口两侧安全外边距 |

---

## 6. Depth, Elevation & Motion

### Pure Light Elevation Technique

Soft Sky 杜绝黑灰重投影，采用 **冷调半透明彩色阴影 + 顶层 1px 纯白高光内阴影** 营造通透水晶纸感：

```css
box-shadow: 0 4px 20px rgba(74, 159, 212, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.95);
```

### Shadow Elevation Scale

| Level | Value | Role |
|---|---|---|
| **Base Glass** | `0 4px 20px rgba(74, 159, 212, .06), inset 0 1px 0 rgba(255, 255, 255, .95)` | 默认卡片、规格面板 |
| **Hover Float**| `0 12px 32px rgba(74, 159, 212, .12), inset 0 1px 0 rgba(255, 255, 255, 1)` | 卡片悬浮状态轻盈上浮 |
| **Selected Lift**| `0 14px 36px rgba(2, 132, 199, .18), inset 0 1px 0 rgba(255, 255, 255, 1)` | 推荐卡片高亮浮层 |
| **Dropdown Menu**| `0 16px 40px rgba(74, 159, 212, .16), inset 0 1px 0 #FFFFFF` | 下拉菜单与浮层 |
| **Modal Dialog**| `0 24px 60px rgba(42, 63, 84, .18), inset 0 1px 0 #FFFFFF` | 模态弹窗面板 |

### Motion Tokens

```css
--ease-soft: cubic-bezier(0.16, 1, 0.3, 1);
--duration-hover: 0.25s;
```

---

## 7. Do's and Don'ts

### Do's (7 项金律)

1. **Do 使用视口全局固定极光画布** — 极光渐变必须置于 `body::before` 全局固定层，确保滚动时不产生断层。
2. **Do 使用半透明纯白 Surface 与顶层白高光** — 维持卡片 `rgba(255,255,255,.82)` 与 `inset 0 1px 0 #FFF` 带来的清透呼吸感。
3. **Do 严格采用同色系演进** — 仅使用天蓝（`#4A9FD4`）和高阶蔚蓝（`#0284C7`）表达层级，杜绝任何杂色冲突。
4. **Do 保持圆角在 8–16px 之间** — 营造温润、生活方式向的柔和轮廓。
5. **Do 在对比矩阵中使用蔚蓝推荐列** — 推荐列带有 `rgba(2, 132, 199, 0.06)` 淡微光底色与蔚蓝发光标点。
6. **Do 使用深蓝灰（`#2A3F54`）作为主文字墨色** — 替代纯黑，与天蓝画布产生和谐典雅的视觉共鸣。
7. **Do 在大标题中进行中文主动语义换行** — 控制短句结构，保持诗意与通透感。

### Don'ts (7 项红线)

1. **Don't 在 `<section>` 局部重复堆叠径向光斑** — 这会导致长页面上下滚动时出现生硬的割裂分块。
2. **Don't 使用黑灰色或重泥土色重阴影** — 阴影必须是极淡的冷调蓝色散（`rgba(74,159,212,.06)`）。
3. **Don't 引入与冷蓝冲突的热烈杂色（如暖红、亮粉、荧光紫）** — 保持纯净如洗的蓝白天光感。
4. **Don't 在圆角毛玻璃卡片中使用粗硬单边实色条（如 `border-left: 4px` 或 `border-top: 3px`）** — 严禁破坏卡片的整体圆角与通透感，必须依靠整体柔和描边、微渐变浅底与专属精致胶囊徽章（Badge）表达语义。
5. **Don't 使用锐利直角（0px）或过于夸张的 32px 巨型圆角** — 14px 为最舒适的平衡点。
6. **Don't 堆砌大量彩色 emoji** — 保持如无印良品、现代生活方式画册般的典雅与克制。
7. **Don't 使用过于狂暴的弹簧跳跃动效** — 悬浮动效必须是平滑轻柔的微上浮（`translateY(-3px)`）。

---

## 8. Responsive Behavior & Breakpoints

### Breakpoint Groups

| Breakpoint | Range | Target Device | Layout Adaptation Rules |
|---|---|---|---|
| **Mobile** | `< 640px` | 手机端 | 页面内边距 `16px`；Hero 字号 `36px~42px`；卡片组降为 1 列；参数栏 2 列；圆角微降至 `10px`。 |
| **Tablet** | `640px ~ 1024px` | iPad / 平板 | 页面内边距 `24px`；Hero 字号 `46px~54px`；卡片组 2 列（第 3 张卡片居中自适应）；参数栏 4 列紧凑。 |
| **Desktop** | `1024px ~ 1400px`| 笔记本 / 桌面显示器 | 启用完整 `1180px` 版心；Hero 字号 `56px~68px`；3 列卡片优雅并排；展示完整极光渐变层次。 |
| **Wide** | `> 1400px` | 4K / 大屏 | 版心锁定 `1180px` 居中；两侧舒展完整浅天蓝呼吸感天幕。 |

---

## 9. 核心特征组件拼装示范 (Signature Component Snippets)

### Quick Reference Tokens

```
Background:        #EAF6FC -> #D8EEF8 (Fixed Aurora Canvas)
Surface Card:      rgba(255, 255, 255, 0.82)
Text primary:      #2A3F54 (Deep Slate Blue)
Text secondary:    #5D7A8C (Muted Cyan Gray)
Text muted:        #90A8B8
Base Signal:       #4A9FD4 (Sky Blue, Eyebrow, Borders)
High Accent:       #0284C7 (Vibrant Azure, Recommended, CTA)
Border:            rgba(93, 179, 232, 0.28)
Radius:            14px (Cards), 20px (Pill Tag), 8px (Small)
Fonts:             Display: Nunito, PingFang SC (800 for Hero, 400 for Body)
                   Mono: IBM Plex Mono (600 for Specs)
```

### 1. Section Eyebrow + Lifestyle Spec Grid (圆润天蓝标头与生活方式规格栏)

```html
<div class="eyebrow">
  <span class="diamond">◆</span>
  <span>01 / PRODUCT PHILOSOPHY</span>
  <span class="line"></span>
</div>

<div class="spec-row">
  <div class="spec">
    <div class="val">180<em>g</em></div>
    <div class="unit">ULTRA LIGHTWEIGHT / 极致轻盈</div>
  </div>
  <div class="spec">
    <div class="val">32<em>hrs</em></div>
    <div class="unit">BATTERY LIFE / 续航时长</div>
  </div>
  <div class="spec">
    <div class="val">0.02<em>%</em></div>
    <div class="unit">DISTORTION RATE / 低失真率</div>
  </div>
  <div class="spec">
    <div class="val">IPX8</div>
    <div class="unit">WATERPROOF / 防水等级</div>
  </div>
</div>
```

### 2. Frosted Feature Cards with Highlight State (半透毛玻璃卡片组与蔚蓝高光)

```html
<div class="cards-3">
  <div class="num-card">
    <div class="num">01</div>
    <h3>原生纸感触控</h3>
    <p>采用微米级防眩光磨砂玻璃表面，模拟真实纸张书写阻尼感，温润细腻不反光。</p>
  </div>
  
  <!-- 推荐状态使用 .selected 激活蔚蓝高阶强调 -->
  <div class="num-card selected">
    <div class="tag">FEATURED</div>
    <div class="num">02</div>
    <h3>全天候极光同步</h3>
    <p>内置环境色温自适应传感阵列，根据昼夜自然光照平滑微调屏幕暖蓝光谱平衡。</p>
  </div>
  
  <div class="num-card">
    <div class="num">03</div>
    <h3>超低功耗待机</h3>
    <p>双核协处理器维持离线静止画布状态，长达 4 周无需反复充电。</p>
  </div>
</div>
```

### 3. Air Minimalist Admonitions (极简空气感提示框)

```html
<div class="admonition info">
  <div class="admonition-head">
    <span class="icon">✦</span>
    <span class="admonition-title">核心结论 // INFO</span>
  </div>
  <p>去除厚重药丸框与多余渐变，回归纯白晶透毛玻璃卡片与轻盈单行标头，保持空灵、通透、低负担的雅致调性。</p>
</div>
```

### 4. Dual Evaluation / Pros & Cons (优劣势对比卡片)

```html
<div class="pros-cons">
  <div class="pro-card">
    <div class="pc-head">
      <span class="dot"></span>
      <span>PROS / 核心优势</span>
    </div>
    <ul>
      <li>架构极其稳定，支持超大规模长文结构化解析</li>
      <li>15 款设计风格无缝插拔，数据协议标准统一</li>
    </ul>
  </div>
  <div class="con-card">
    <div class="pc-head">
      <span class="dot"></span>
      <span>CONS / 考量权衡</span>
    </div>
    <ul>
      <li>初期学习曲线较陡峭，需掌握底层语义契约</li>
    </ul>
  </div>
</div>
```

### 5. Elegant Q&A Item (雅致折叠问答条目)

```html
<div class="faq">
  <div class="faq-item">
    <div class="q">
      <span class="q-icon">Q</span>
      <h4>屏幕表面是否容易残留指纹或划痕？</h4>
    </div>
    <div class="a">
      <p>外层覆盖高硬度防指纹疏油涂层，耐磨等级达莫氏 7 级，日常擦拭即可恢复清透如新的纯净视界。</p>
    </div>
  </div>
</div>
```

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配清透空灵浅蓝风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: false,
    background: "#FFFFFF",
    primaryColor: "#EAF6FC",
    primaryTextColor: "#2A3F54",
    primaryBorderColor: "#0284C7",
    lineColor: "#0284C7",
    secondaryColor: "#EAF6FC",
    tertiaryColor: "#FFFFFF",
    fontFamily: '"Nunito", -apple-system, sans-serif'
  }
});
```
