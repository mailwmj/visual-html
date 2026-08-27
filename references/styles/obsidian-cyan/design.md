# Obsidian Cyan (黑曜霓蓝展厅风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Obsidian Cyan 将顶级数字产品发布会与科技展厅的视觉冲击力融入长文本排版与演示系统。全站以深邃纯净的黑曜夜色（`#0B0E14` / `#07090E`）为底座，在全局固定视口层（`body::before`）渲染微弱内敛的电光冷蓝极光光晕（`rgba(56, 189, 248, 0.08~0.14)`），奠定沉浸、冷峻且极具未来感的数字展厅基调。

界面的核心魅力在于**高对比度的电光信号系统与悬浮解构美学**。深色毛玻璃卡片（`rgba(19, 25, 36, 0.78)` 配合 `blur(16px)`）悬浮于夜色中，通过电光霓蓝（`#38BDF8`）信号通道点亮关键焦点。独有的**发光定位点（Callout Pins）**、**细折线引出标注**与**醒目的实心电光蓝发光圆形步骤徽章（`❶ ❷ ❸ ❹`）**，将枯燥的长文本转化为极具可读性与观赏性的交互式架构展板。

---

## 2. Color Palette & Roles

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token / Source | Usage |
|---|---|---|---|---|
| Background (Canvas Base) | `rgb(11, 14, 20)` | `#0B0E14` | `--bg` | 全局黑曜画布底色 |
| Background (Deep Pit) | `rgb(7, 9, 14)` | `#07090E` | `--bg-deep` | 凹陷面板、终端底座、输入框底色 |
| Surface (Glass Card) | `rgba(19, 25, 36, 0.78)`| `rgba(19,25,36,.78)` | `--surface-glass` | 磨砂玻璃主卡片、阅读容器 |
| Surface (Solid Card) | `rgb(21, 29, 42)` | `#151D2A` | `--surface-card` | 实体容器底色（阻断背景干扰） |
| Text (Primary Pure) | `rgb(255, 255, 255)` | `#FFFFFF` | `--text-primary` | 大标题、核心数值、高亮重点正文 |
| Text (Secondary Slate) | `rgb(148, 163, 184)` | `#94A3B8` | `--text-secondary` | 导读段落、正文说明、次要文本 |
| Text (Muted Muted) | `rgb(82, 96, 113)` | `#526071` | `--text-muted` | 注释、分类标签、等宽元数据 |
| Border (Default Subtle) | `rgba(255, 255, 255, 0.08)`| `rgba(255,255,255,.08)`| `--border` | 卡片常规边框、微弱分割线 |
| Border (Glow Cyan) | `rgba(56, 189, 248, 0.45)` | `rgba(56,189,248,.45)`| `--border-strong` | 选中态卡片、高亮聚焦发光边框 |

### Accent & Signal Palette

| Channel | Role | Value | Hex / RGBA | Token | Usage Boundary |
|---|---|---|---|---|---|
| **Primary Signal** | 电光青蓝 (Electric Cyan) | `rgb(56, 189, 248)` | `#38BDF8` | `--signal-cyan` | 标头徽章、发光定位点、选中态描边、步骤徽章 (占 3–5%) |
| **Secondary Signal** | 深海电光蓝 (Ocean Blue) | `rgb(14, 165, 233)` | `#0EA5E9` | `--signal-blue` | 主操作按钮、重要胶囊背景、次级高光 (占 2%) |
| **Deep Accent** | 皇家深蓝 (Deep Blue) | `rgb(37, 99, 235)` | `#2563EB` | `--signal-blue-deep` | 渐变暗部过渡与深色按钮 |
| **Cyan Glow** | 电光发光弥散 (Cyan Glow) | `rgba(56, 189, 248, 0.35)` | `rgba(56,189,248,.35)`| `--signal-glow` | 核心焦点外发光、悬浮光晕 |

### CSS Design Tokens

```css
:root {
  /* 背景层 */
  --bg: #0B0E14;
  --bg-deep: #07090E;
  --surface-1: #131924;
  --surface-2: #1B2433;
  --surface-glass: rgba(19, 25, 36, 0.78);
  --surface-card: #151D2A;

  /* 文字层 */
  --text-primary: #FFFFFF;
  --text-secondary: #94A3B8;
  --text-muted: #526071;

  /* 边框与光晕 */
  --border: rgba(255, 255, 255, 0.08);
  --border-subtle: rgba(56, 189, 248, 0.16);
  --border-strong: rgba(56, 189, 248, 0.45);
  --border-glow: 0 0 16px rgba(56, 189, 248, 0.25);

  /* 信号色通道（电光霓蓝） */
  --signal-cyan: #38BDF8;
  --signal-cyan-soft: rgba(56, 189, 248, 0.12);
  --signal-blue: #0EA5E9;
  --signal-blue-deep: #2563EB;
  --signal-glow: rgba(56, 189, 248, 0.35);
  --accent-gradient: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%);
  --accent-gradient-subtle: linear-gradient(180deg, rgba(56, 189, 248, 0.15) 0%, rgba(14, 165, 233, 0.03) 100%);

  /* 阴影与景深 */
  --shadow-card: 0 8px 32px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.06);
  --shadow-card-hover: 0 14px 40px rgba(0, 0, 0, 0.55), 0 0 20px rgba(56, 189, 248, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.12);
  --shadow-card-selected: 0 16px 44px rgba(0, 0, 0, 0.6), 0 0 28px rgba(56, 189, 248, 0.26), inset 0 1px 0 rgba(56, 189, 248, 0.3);
  --shadow-mockup: 0 24px 64px rgba(0, 0, 0, 0.75), 0 0 36px rgba(56, 189, 248, 0.14);

  /* 尺寸与圆角 */
  --radius-sm: 8px;
  --radius: 16px;
  --radius-lg: 24px;
  --radius-device: 36px;
  --radius-pill: 999px;
  --container: 1220px;

  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 48px; --space-8: 64px;
  --space-9: 96px; --space-10: 128px;

  /* 字体栈 */
  --font-display: "Inter", -apple-system, BlinkMacSystemFont, "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", "SFMono-Regular", monospace;
}
```

### Color Distribution Philosophy

- **65% 黑曜基底** (`#0B0E14`, `#131924`)：营造深沉大气的专业科技展厅基调。
- **20% 纯白与冷石板灰文字** (`#FFFFFF`, `#94A3B8`)：提供极致清澈的信息展示。
- **10% 幽蓝边框与微光层** (`rgba(56,189,248,0.16)`)：勾勒组件物理轮廓。
- **5% 高纯度电光青蓝** (`#38BDF8`)：作为核心信号通道，精准聚焦用户视线。

---

## 3. Typography Rules

### Font Stacks & Type System

- **Display & Interface Text**: `--font-display` (`"Inter", "PingFang SC", "HarmonyOS Sans SC", sans-serif`)
- **Code, Numbers, Timelines & Metadata**: `--font-mono` (`"JetBrains Mono", "IBM Plex Mono", "SFMono-Regular", monospace`)

### Type Hierarchy Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 60px~80px | 800 | 1.02 (61~82px) | **-0.035em** | `--font-display` | 展厅主标题（极具科技冲击力） |
| **Section Title** | `h2.section-title` | 32px~40px | 700 | 1.18 (38~47px) | **-0.02em** | `--font-display` | 章节二级大标题 |
| **Card Title** | `h3`, `.card-title`| 18px~20px | 600 | 1.35 (24~27px) | -0.01em | `--font-display` | 模块/卡片核心标题 |
| **Lead Paragraph** | `.lead` | 18px | 400 | 1.65 (29.7px) | normal | `--font-display` | 导读段落（50~58 字符宽度） |
| **Body Text** | `p`, `.body` | 14px~15px | 400 | 1.68 (23~25px)| normal | `--font-display` | 正文阅读长文本 |
| **Section Eyebrow**| `.eyebrow` | 12px~13px | 600 | 1.0 (12~13px) | **0.08em** | `--font-mono` | 章节大写索引标头（`◆ 01 / SHOWCASE`） |
| **Stat Metric** | `.stat-val` | 48px~56px | 800 | 1.0 (48~56px) | -0.025em | `--font-display` | 核心量化指标超大数值 |
| **Step Badge** | `.step-badge` | 14px | 700 | 1.0 (14px) | normal | `--font-mono` | 圆形电光蓝步骤徽章（`❶ ❷ ❸`） |
| **Spec Unit / Tag**| `.unit`, `.tag` | 11px~12px | 500 | 1.2 (14px) | **0.05em** | `--font-mono` | 规格单位、等宽大写胶囊标签 |
| **Code Snippet** | `code`, `pre` | 13px | 500 | 1.55 (20px) | normal | `--font-mono` | 终端代码与 API 参数高亮 |

---

## 4. Component Stylings & Interaction Matrix

### Interactive State Matrix

| Component / State | Default | Hover | Active / Pressed | Focus (Keyboard) | Disabled |
|---|---|---|---|---|---|
| **Glass Card (`.num-card`)** | Bg: `var(--surface-glass)`<br>Border: `1px solid var(--border)`<br>Shadow: `var(--shadow-card)` | Bg: `rgba(21, 29, 42, 0.9)`<br>Border: `1px solid var(--border-subtle)`<br>Shadow: `var(--shadow-card-hover)`<br>Transform: `translateY(-3px)` | Bg: `var(--surface-glass)`<br>Transform: `translateY(0)` | Box-Shadow: `0 0 0 2px #0B0E14, 0 0 0 4px #38BDF8` | Bg: `rgba(11, 14, 20, 0.4)`<br>Opacity: `0.45`<br>Border: `1px solid rgba(255,255,255,0.04)` |
| **Selected Card (`.selected`)** | Bg: `rgba(21, 29, 42, 0.95)`<br>Border: `1px solid #38BDF8`<br>Shadow: `var(--shadow-card-selected)` | Bg: `#192333`<br>Transform: `translateY(-4px)`<br>Shadow: `0 20px 50px rgba(0,0,0,0.7), 0 0 36px rgba(56,189,248,0.35)` | Bg: `var(--surface-card)`<br>Transform: `none` | Box-Shadow: `0 0 0 2px #0B0E14, 0 0 0 4px #38BDF8` | - |
| **Action Button (`.btn-primary`)** | Bg: `var(--accent-gradient)`<br>Text: `#FFFFFF`<br>Font: 600 Inter | Bg: `linear-gradient(135deg, #0EA5E9 0%, #0284C7 100%)`<br>Box-Shadow: `0 4px 20px rgba(56,189,248,0.4)` | Transform: `scale(0.98)` | Outline: `2px solid #38BDF8`<br>Outline-Offset: `2px` | Bg: `#1B2433`<br>Text: `#526071`<br>Cursor: `not-allowed` |
| **Callout Pin (`.callout-pin`)** | Bg: `#38BDF8`<br>Box-Shadow: `0 0 12px #38BDF8` | Transform: `scale(1.25)`<br>Box-Shadow: `0 0 20px #38BDF8` | - | - | - |
| **Form Input (`input`)** | Bg: `#07090E`<br>Border: `1px solid var(--border)`<br>Text: `#FFFFFF` | Border: `1px solid var(--border-subtle)` | - | Border: `1px solid #38BDF8`<br>Box-Shadow: `0 0 0 1px #38BDF8, 0 0 12px rgba(56,189,248,0.25)` | Bg: `#0B0E14`<br>Text: `#526071` |

### Signature Patterns

#### 1. Electric Neon Double-Ring Focus (霓蓝双环聚焦)
```css
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px #0B0E14, 0 0 0 4px var(--signal-cyan);
  border-radius: 16px;
}
```

#### 2. Callout Pin with Leader Line (设备解构定位点)
```html
<div class="callout-wrapper">
  <div class="callout-pin"></div>
  <div class="callout-line"></div>
  <div class="callout-label">CORE NEURAL ENGINE</div>
</div>
```

### Border Radius Scale

| Token / Value | Usage |
|---|---|
| `8px` (`--radius-sm`) | 内部微卡片、代码块、输入框、小胶囊 |
| `16px` (`--radius`) | 标准黑曜卡片、问答卡片、对比矩阵（核心默认值） |
| `24px` (`--radius-lg`) | 外层大容器、展示展板 |
| `36px` (`--radius-device`) | 悬浮设备模型（Mockup Frame）外壳 |
| `999px` (`--radius-pill`) | 胶囊药丸标签、圆形步骤徽标（`size: 28px`） |

---

## 5. Layout & Spacing Principles

### Spacing Scale (4px Base Grid)

| Token | Value | Multiplier | Semantic Usage |
|---|---|---|---|
| `--space-1` | 4px | 1x | 微边距、指示点边距 |
| `--space-2` | 8px | 2x | 标签内边距、紧凑垂直间隙 |
| `--space-3` | 12px | 3x | 输入框内边距、卡片内微元素间距 |
| `--space-4` | 16px | 4x | 标准栅格 Gap、移动端内边距 |
| `--space-5` | 24px | 6x | 桌面端卡片内边距、组件间距 |
| `--space-6` | 32px | 8x | 章节内部模块间距、统计栏间距 |
| `--space-7` | 48px | 12x | 小章节垂直留白 |
| `--space-8` | 64px | 16x | 标准章节间距 |
| `--space-9` | 96px | 24x | Hero 区域上下呼吸间距 |
| `--space-10` | 128px | 32x | 宽幅展示展板留白 |

### Page Layout Dimension Tokens

| Dimension | Value | Role |
|---|---|---|
| `--container` | `1220px` | 页面正文最大宽度（桌面端版心） |
| Global Cyan Aurora | `fixed; inset: 0; z-index: -1` | `body::before` 视口固定层极光微光 |
| Page Horizontal Margin | `24px` (桌面端) / `16px` (移动端) | 视口两侧安全外边距 |

---

## 6. Depth, Elevation & Motion

### Multi-Layer Dark Glow Technique

Obsidian Cyan 结合 **深色毛玻璃（`rgba(19, 25, 36, 0.78)`）**、**顶层微内高光（`inset 0 1px 0 rgba(255,255,255,0.06)`）** 与 **电光霓蓝外发光（`0 0 28px rgba(56, 189, 248, 0.26)`）** 建立深邃科技感：

```css
box-shadow: 0 16px 44px rgba(0, 0, 0, 0.6), 0 0 28px rgba(56, 189, 248, 0.26), inset 0 1px 0 rgba(56, 189, 248, 0.3);
```

### Shadow Elevation Scale

| Level | Value | Role |
|---|---|---|
| **Base Glass** | `0 8px 32px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.06)` | 默认卡片、规格面板 |
| **Hover Float**| `0 14px 40px rgba(0, 0, 0, 0.55), 0 0 20px rgba(56, 189, 248, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.12)` | 卡片悬浮状态 |
| **Selected Lift**| `0 16px 44px rgba(0, 0, 0, 0.6), 0 0 28px rgba(56, 189, 248, 0.26), inset 0 1px 0 rgba(56, 189, 248, 0.3)` | 推荐卡片高光浮层 |
| **Device Mockup**| `0 24px 64px rgba(0, 0, 0, 0.75), 0 0 36px rgba(56, 189, 248, 0.14)` | 悬浮设备模型 |
| **Modal / Dialog**| `0 32px 80px rgba(0, 0, 0, 0.9), 0 0 40px rgba(56, 189, 248, 0.2)` | 模态弹窗与大浮层 |

### Motion Tokens

```css
--ease-swift: cubic-bezier(0.16, 1, 0.3, 1);
--duration-fast: 0.2s;
--duration-normal: 0.35s;
```

---

## 7. Do's and Don'ts

### Do's (7 项金律)

1. **Do 使用视口全局固定冷蓝极光** — 极光必须置于 `body::before`，长页面滚动时浑然一体，绝不在 `<section>` 局部重复添加断层光斑。
2. **Do 使用电光霓蓝（`#38BDF8`）作为唯一主信号色** — 确保科技聚焦通道纯净统一。
3. **Do 在步骤流程中使用圆形霓蓝数字徽章（`❶ ❷ ❸`）** — 强化工作流与架构演进的辨识度。
4. **Do 使用纯白（`#FFFFFF`）作为主标题与核心数字颜色** — 在黑曜底色上营造最高对比度的纯净质感。
5. **Do 为设备模型与解构图配置发光定位点（Callout Pins）** — 增强软硬件架构解构的互动感。
6. **Do 使用深色毛玻璃卡片（`blur(16px)`）搭配微内高光** — 营造悬浮展柜的晶莹厚度。
7. **Do 在大标题中进行中文主动语义换行** — 保持 800 字重主标题的冲击力与呼吸节奏。

### Don'ts (7 项红线)

1. **Don't 引入刺眼的高饱和暖色杂色（如暖红、荧光黄）** — 保持纯粹深邃的黑曜冷蓝夜色。
2. **Don't 让局部光斑产生刺眼的白内障眩光** — 极光不透明度严格控制在 8%~14% 之间。
3. **Don't 使用生硬浅灰色实心卡片** — 卡片必须使用深色半透明表面（`rgba(19, 25, 36, 0.78)`）。
4. **Don't 在对比矩阵中使用红绿杂色混搭** — 统一使用电光霓蓝高光列与微光圆点。
5. **Don't 使用锐利直角（0px）作为常规卡片圆角** — 保持 14–18px 的现代科技圆角。
6. **Don't 堆砌大量彩色 emoji** — 使用现代等宽字符、SVG 定位点与科技 Badge 替代。
7. **Don't 在卡片悬浮时触发过度变形** — 保持平滑克制的微上浮（`translateY(-3px)`）与发光扩散。

---

## 8. Responsive Behavior & Breakpoints

### Breakpoint Groups

| Breakpoint | Range | Target Device | Layout Adaptation Rules |
|---|---|---|---|
| **Mobile** | `< 640px` | 手机端 | 页面边距 `16px`；Hero 字号 `36px~44px`；卡片组降为 1 列；设备解构框居中自适应；定位点标注折线转为纵向列表。 |
| **Tablet** | `640px ~ 1024px` | iPad / 平板 | 页面边距 `24px`；Hero 字号 `48px~56px`；卡片组 2 列（推荐卡片自适应展开）；流程步骤保持紧凑横排。 |
| **Desktop** | `1024px ~ 1400px`| 标准桌面显示器 | 启用完整 `1220px` 版心；Hero 字号 `60px~72px`；3 列卡片自适应排布；展现完整设备模型与标注引出线。 |
| **Wide** | `> 1400px` | 4K / 超宽大屏 | 版心锁定 `1220px` 居中；全局黑曜冷蓝极光舒展全屏。 |

---

## 9. 核心特征组件拼装示范 (Signature Component Snippets)

### Quick Reference Tokens

```
Background:        #0B0E14 (Canvas), #151D2A (Surface Card), #07090E (Deep Pit)
Surface Glass:     rgba(19, 25, 36, 0.78) + backdrop-filter: blur(16px)
Text primary:      #FFFFFF (Pure White)
Text secondary:    #94A3B8 (Slate Gray)
Text muted:        #526071
Primary Signal:    #38BDF8 (Electric Cyan, Eyebrow, Callout Pin, Step Badges)
Secondary Signal:  #0EA5E9 (Ocean Blue, CTA)
Border:            rgba(255, 255, 255, 0.08) (Default), rgba(56, 189, 248, 0.45) (Glow)
Radius:            16px (Cards), 36px (Device Mockup), 999px (Pill Tag)
Fonts:             Display: Inter, PingFang SC (800 for Hero, 400 for Body)
                   Mono: JetBrains Mono (500)
```

### 1. UI/UX Device Breakdown with Callout Pins (设备解构与发光标注点)

```html
<div class="showcase-breakdown">
  <div class="mockup-frame">
    <!-- 发光定位点与引出标注 -->
    <div class="callout-wrapper" style="top: 25%; left: 35%;">
      <div class="callout-pin"></div>
      <div class="callout-line"></div>
      <div class="callout-card">
        <h5>NEURAL PIPELINE</h5>
        <p>集成片上 32 核神经网络加速单元，端侧实时运行百亿大模型推理。</p>
      </div>
    </div>
    
    <div class="callout-wrapper" style="top: 65%; left: 60%;">
      <div class="callout-pin"></div>
      <div class="callout-line"></div>
      <div class="callout-card">
        <h5>ZERO-LATENCY BUS</h5>
        <p>提供 800GB/s 超高带宽片间互联，消除多节点分布式状态同步瓶颈。</p>
      </div>
    </div>
  </div>
</div>
```

### 2. Step Flow with Cyan Circular Badges (电光蓝圆形徽章步骤流)

```html
<div class="steps">
  <div class="step">
    <div class="idx">❶</div>
    <div class="step-content">
      <h4>拓扑初始化与探活</h4>
      <p>自动扫描接入集群的边缘计算节点，完成零信任密钥协商与全链路心跳检测。</p>
    </div>
  </div>
  
  <div class="step active">
    <div class="idx">❷</div>
    <div class="step-content">
      <h4>动态状态快照注入</h4>
      <p>依托极速分布式缓存完成内存镜像增量同步，无缝承接实时生产流量。</p>
    </div>
  </div>
  
  <div class="step">
    <div class="idx">❸</div>
    <div class="step-content">
      <h4>智能流量切分收敛</h4>
      <p>多目标优化器根据各节点算力水位与延迟热力图自适应分配请求负载。</p>
    </div>
  </div>
</div>
```

### 3. Obsidian Dark Comparison Matrix (黑曜展厅对比矩阵)

```html
<div class="cmp cmp-matrix">
  <div class="row head">
    <div class="cell">核心特性与能力</div>
    <div class="cell">社区开源版</div>
    <div class="cell selected-col">ENTERPRISE PRO</div>
    <div class="cell">私有化专有云</div>
  </div>
  <div class="row">
    <div class="cell">端侧神经网络加速</div>
    <div class="cell"><span class="dot"></span></div>
    <div class="cell selected-col"><span class="dot cyan"></span></div>
    <div class="cell"><span class="dot"></span></div>
  </div>
  <div class="row">
    <div class="cell">跨区域零丢包状态同步</div>
    <div class="cell"><span class="dash">—</span></div>
    <div class="cell selected-col"><span class="dot cyan"></span></div>
    <div class="cell"><span class="dot"></span></div>
  </div>
  <div class="row">
    <div class="cell">7×24 专属架构师保障</div>
    <div class="cell"><span class="dash">—</span></div>
    <div class="cell selected-col"><span class="dot cyan"></span></div>
    <div class="cell"><span class="dot"></span></div>
  </div>
</div>
```

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配黑曜霓蓝展厅风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: true,
    background: "#151D2A",
    primaryColor: "#131924",
    primaryTextColor: "#FFFFFF",
    primaryBorderColor: "#38BDF8",
    lineColor: "#38BDF8",
    secondaryColor: "#1E293B",
    tertiaryColor: "#0B0E14",
    fontFamily: ""JetBrains Mono", "Inter", sans-serif"
  }
});
```
