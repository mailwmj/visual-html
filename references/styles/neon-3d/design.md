# Neon Aurora (暗紫流体极光风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Neon Aurora（暗紫流体极光风）将前沿潮酷硬件发布、创意设计工作室与蒸汽波数字艺术质感升华为界面规范。界面拒绝通体泛滥的刺眼紫色，而是奉行**大面积纯黑基座（80%+ Pure Pitch Black `#000000`）搭配克制局部流体极光光晕**的黄金法则。

界面的核心魅力在于**模拟胶片微粒噪点与 3D 浮雕高光的交融**。全站覆盖一层轻量胶片微粒噪点滤镜（Film Grain Noise Overlay，`opacity: 0.045`），赋予纯黑底色与极光真实海报般的物理触感；卡片采用中性深黑 Surface（`#0F0F0F`）配合顶层 1px 纯白高光内阴影（`inset 0 1px 0 rgba(255,255,255,0.12)`），营造出沉甸甸的 3D 悬浮厚度感。主信号霓虹紫（`#A855F7`）与辅助信号霓虹洋红（`#EC4899`）仅在局部焦点精准点亮，呈现出既潮酷前卫又严谨沉着的视觉张力。

---

## 2. Color Palette & Roles

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token / Source | Usage |
|---|---|---|---|---|
| Background (Pure Canvas) | `rgb(0, 0, 0)` | `#000000` | `--bg` | 全局纯黑画布底色（占 80%+ 面积） |
| Background (Deep Pit) | `rgb(0, 0, 0)` | `#000000` | `--bg-deep` | 凹陷面板、终端底座、输入框底色 |
| Surface (Embossed Card)| `rgb(15, 15, 15)` | `#0F0F0F` | `--surface-card` | 中性深黑主卡片（阻断紫色泛滥） |
| Surface (Glass Layer) | `rgba(16, 16, 16, 0.85)`| `rgba(16,16,16,.85)` | `--surface-glass` | 浮动卡片、毛玻璃面板 |
| Text (Primary Pure) | `rgb(255, 255, 255)` | `#FFFFFF` | `--text-primary` | 大标题、核心数据、重点高亮文字 |
| Text (Secondary Zinc) | `rgb(161, 161, 170)` | `#A1A1AA` | `--text-secondary` | 说明正文、导读段落、副标题 |
| Text (Muted Slate) | `rgb(113, 113, 122)` | `#71717A` | `--text-muted` | 注释、分类标签、等宽元数据 |
| Border (Default Subtle) | `rgba(255, 255, 255, 0.10)`| `rgba(255,255,255,.10)`| `--border` | 卡片常规边框、3D 边缘轮廓 |
| Border (Strong / Glow) | `rgba(168, 85, 247, 0.60)` | `rgba(168,85,247,.60)`| `--border-strong` | 选中态卡片、高亮发光描边 |

### Accent & Signal Palette

| Channel | Role | Value | Hex / RGBA | Token | Usage Boundary |
|---|---|---|---|---|---|
| **Primary Signal** | 霓虹紫 (Neon Purple) | `rgb(168, 85, 247)` | `#A855F7` | `--signal-cyan` | Eyebrow 标头、核心数字、选中态描边、CTA (占 3–5%) |
| **Secondary Signal** | 霓虹洋红 (Neon Magenta) | `rgb(236, 72, 153)` | `#EC4899` | `--signal-blue` | 辅助强调标签、渐变修饰 (占 2%) |
| **Deep Fuchsia** | 赛博洋红 (Cyber Magenta) | `rgb(217, 70, 239)` | `#D946EF` | `--signal-blue-deep` | 渐变中继色与高亮节点 |
| **Neon Glow** | 霓虹发光弥散 (Purple Glow) | `rgba(168, 85, 247, 0.40)`| `rgba(168,85,247,.40)`| `--signal-glow` | 核心焦点外发光、悬浮光晕 |

### CSS Design Tokens

```css
:root {
  /* 背景层：保持纯黑中性底色 */
  --bg: #000000;
  --bg-deep: #000000;
  --surface-1: #0A0A0A;
  --surface-2: #121212;
  --surface-glass: rgba(16, 16, 16, 0.85);
  --surface-card: #0F0F0F;

  /* 文字层 */
  --text-primary: #FFFFFF;
  --text-secondary: #A1A1AA;
  --text-muted: #71717A;

  /* 边框与光晕 */
  --border: rgba(255, 255, 255, 0.10);
  --border-subtle: rgba(168, 85, 247, 0.22);
  --border-strong: rgba(168, 85, 247, 0.60);
  --border-glow: 0 0 20px rgba(168, 85, 247, 0.40);

  /* 信号色通道（霓虹紫、洋红） */
  --signal-cyan: #A855F7;
  --signal-cyan-soft: rgba(168, 85, 247, 0.16);
  --signal-blue: #EC4899;
  --signal-blue-deep: #D946EF;
  --signal-glow: rgba(168, 85, 247, 0.50);
  --accent-gradient: linear-gradient(135deg, #A855F7 0%, #EC4899 50%, #06B6D4 100%);
  --accent-gradient-subtle: linear-gradient(180deg, rgba(168, 85, 247, 0.20) 0%, rgba(236, 72, 153, 0.04) 100%);

  /* 阴影与景深 (3D感与局部霓虹弥散) */
  --shadow-card: 0 16px 40px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(255, 255, 255, 0.12);
  --shadow-card-hover: 0 24px 56px rgba(0, 0, 0, 0.95), 0 0 30px rgba(168, 85, 247, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.2);
  --shadow-card-selected: 0 28px 64px rgba(0, 0, 0, 0.95), 0 0 35px rgba(168, 85, 247, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.25);
  --shadow-mockup: 0 30px 80px rgba(0, 0, 0, 0.95), 0 0 50px rgba(168, 85, 247, 0.25);

  /* 尺寸与圆角 */
  --radius-sm: 12px;
  --radius: 24px;
  --radius-lg: 32px;
  --radius-device: 48px;
  --radius-pill: 999px;
  --container: 1220px;

  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 48px; --space-8: 64px;
  --space-9: 96px; --space-10: 128px;

  /* 字体栈 */
  --font-display: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", "SFMono-Regular", monospace;
}
```

### Color Distribution Philosophy

- **80% 纯黑夜色底座** (`#000000`, `#0F0F0F`)：保证页面彻底纯净，杜绝全屏大面积刺眼紫光。
- **15% 纯白与中性冷灰** (`#FFFFFF`, `#A1A1AA`)：保证长文本阅读的极佳清晰度。
- **5% 霓虹紫与洋红信号色** (`#A855F7`, `#EC4899`)：仅在局部光弧、序号胶囊与发光描边上点缀。

---

## 3. Typography Rules

### Font Stacks & Type System

- **Display & Interface Text**: `--font-display` (`"Inter", "PingFang SC", "HarmonyOS Sans SC", sans-serif`)
- **Code, Numbers, Timelines & Metadata**: `--font-mono` (`"JetBrains Mono", "IBM Plex Mono", "SFMono-Regular", monospace`)

### Type Hierarchy Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 64px~84px | 900 | 1.0 (64~84px) | **-0.04em** | `--font-display` | 潮酷大字号主标题（力量感十足） |
| **Section Title** | `h2.section-title` | 32px~42px | 800 | 1.15 (37~48px) | **-0.025em**| `--font-display` | 章节二级大标题 |
| **Card Title** | `h3`, `.card-title`| 18px~22px | 700 | 1.3 (24~28px) | -0.01em | `--font-display` | 模块/卡片核心标题 |
| **Lead Paragraph** | `.lead` | 18px | 400 | 1.65 (29.7px) | normal | `--font-display` | 核心摘要导读段落 |
| **Body Text** | `p`, `.body` | 14px~15px | 400 | 1.7 (24~26px) | normal | `--font-display` | 正文阅读长文本 |
| **Section Eyebrow**| `.eyebrow` | 12px~13px | 600 | 1.0 (12~13px) | **0.08em** | `--font-mono` | 章节大写索引标头（`◆ 01 / WAVE`） |
| **Stat Metric** | `.stat-val` | 48px~58px | 900 | 1.0 (48~58px) | -0.03em | `--font-display` | 核心量化指标超大数值 |
| **Spec Unit / Tag**| `.unit`, `.tag` | 11px~12px | 600 | 1.2 (14px) | **0.06em** | `--font-mono` | 规格单位、等宽霓虹胶囊标签 |
| **Code Snippet** | `code`, `pre` | 13px | 500 | 1.55 (20px) | normal | `--font-mono` | 终端代码与着色器 Token 高亮 |

---

## 4. Component Stylings & Interaction Matrix

### Interactive State Matrix

| Component / State | Default | Hover | Active / Pressed | Focus (Keyboard) | Disabled |
|---|---|---|---|---|---|
| **3D Card (`.num-card`)** | Bg: `#0F0F0F`<br>Border: `1px solid var(--border)`<br>Shadow: `var(--shadow-card)` | Bg: `#141414`<br>Border: `1px solid var(--border-subtle)`<br>Shadow: `var(--shadow-card-hover)`<br>Transform: `translateY(-4px)` | Bg: `#0F0F0F`<br>Transform: `translateY(0)` | Box-Shadow: `0 0 0 2px #000000, 0 0 0 4px #A855F7` | Bg: `#0A0A0A`<br>Opacity: `0.4`<br>Border: `1px solid rgba(255,255,255,0.05)` |
| **Selected Card (`.selected`)** | Bg: `#14121A`<br>Border: `1px solid #A855F7`<br>Shadow: `var(--shadow-card-selected)` | Bg: `#1A1624`<br>Transform: `translateY(-6px)`<br>Shadow: `0 32px 70px rgba(0,0,0,0.95), 0 0 45px rgba(168,85,247,0.45)` | Bg: `#14121A`<br>Transform: `none` | Box-Shadow: `0 0 0 2px #000000, 0 0 0 4px #A855F7` | - |
| **Action Button (`.btn-primary`)** | Bg: `var(--accent-gradient)`<br>Text: `#FFFFFF`<br>Font: 700 Inter | Bg: `linear-gradient(135deg, #C084FC 0%, #F472B6 100%)`<br>Box-Shadow: `0 4px 24px rgba(168,85,247,0.45)` | Transform: `scale(0.98)` | Outline: `2px solid #A855F7`<br>Outline-Offset: `2px` | Bg: `#1F1F24`<br>Text: `#71717A`<br>Cursor: `not-allowed` |
| **Pill Tag (`.tag`)** | Bg: `rgba(168,85,247,.12)`<br>Text: `#A855F7`<br>Border: `1px solid rgba(168,85,247,.3)` | Bg: `rgba(168,85,247,.22)` | - | - | - |
| **Form Input (`input`)** | Bg: `#0A0A0A`<br>Border: `1px solid var(--border)`<br>Text: `#FFFFFF` | Border: `1px solid var(--border-subtle)` | - | Border: `1px solid #A855F7`<br>Box-Shadow: `0 0 0 1px #A855F7, 0 0 16px rgba(168,85,247,0.3)` | Bg: `#000000`<br>Text: `#71717A` |

### Signature Patterns

#### 1. Neon Aurora Double-Ring Focus (霓虹双环聚焦)
```css
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px #000000, 0 0 0 4px var(--signal-cyan);
  border-radius: 24px;
}
```

#### 2. Film Grain Noise Overlay (全站胶片噪点层)
```css
body::after {
  content: "";
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.045'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 999;
}
```

### Border Radius Scale

| Token / Value | Usage |
|---|---|
| `12px` (`--radius-sm`) | 内部微卡片、代码块、表单输入框 |
| `24px` (`--radius`) | 标准 3D 浮雕卡片、问答折叠框、对比矩阵（核心默认值） |
| `32px` (`--radius-lg`) | 外层大容器、展示展板 |
| `48px` (`--radius-device`) | 悬浮设备模型（Mockup Frame）外壳 |
| `999px` (`--radius-pill`) | 胶囊药丸标签、主行动按钮 |

---

## 5. Layout & Spacing Principles

### Spacing Scale (4px Base Grid)

| Token | Value | Multiplier | Semantic Usage |
|---|---|---|---|
| `--space-1` | 4px | 1x | 微边距、高光点微隙 |
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
| Localized Hero Glow | `width: 600px; height: 600px; top: -100px; right: -100px;` | 仅在 Hero 右上方点缀流体紫光 |
| Page Horizontal Margin | `24px` (桌面端) / `16px` (移动端) | 视口两侧安全外边距 |

---

## 6. Depth, Elevation & Motion

### The 3D Inset Highlight Technique

Neon Aurora 采用 **深黑中性底色 + 顶层 1px 纯白高光内阴影 + 局部霓虹外弥散** 塑造实体浮雕质感：

```css
box-shadow: 0 16px 40px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(255, 255, 255, 0.12);
```

### Shadow Elevation Scale

| Level | Value | Role |
|---|---|---|
| **Base 3D Card** | `0 16px 40px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(255, 255, 255, 0.12)` | 默认卡片、规格面板 |
| **Hover Float** | `0 24px 56px rgba(0, 0, 0, 0.95), 0 0 30px rgba(168, 85, 247, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.2)` | 卡片悬浮状态 |
| **Selected Lift**| `0 28px 64px rgba(0, 0, 0, 0.95), 0 0 35px rgba(168, 85, 247, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.25)` | 推荐卡片高光浮层 |
| **Mockup Device**| `0 30px 80px rgba(0, 0, 0, 0.95), 0 0 50px rgba(168, 85, 247, 0.25)` | 悬浮设备模型 |

### Motion Tokens

```css
--ease-swift: cubic-bezier(0.16, 1, 0.3, 1);
--duration-fast: 0.2s;
--duration-normal: 0.35s;
```

---

## 7. Do's and Don'ts

### Do's (7 项金律)

1. **Do 保持 80%+ 纯黑底色 (`#000000`)** — 严禁全屏通体泛滥刺眼紫光，紫色仅限局部光晕。
2. **Do 为全站叠加胶片微粒噪点层 (`opacity: 0.045`)** — 赋予黑底与光晕真实海报微粒质感。
3. **Do 在卡片顶层保留 1px 纯白高光内阴影** — 营造精致立体的 3D 浮雕悬浮感。
4. **Do 使用纯白（`#FFFFFF`）作为主标题与核心数字** — 在纯黑底色上提供最强可读性。
5. **Do 保持 24px 现代大圆角** — 搭配 3D 阴影展现潮酷硬件质感。
6. **Do 将流光严格限制在 Hero 右上侧与流程左下侧** — 形成对角线呼吸构图。
7. **Do 在大标题中进行中文主动语义断句** — 配合 900 超粗字重展现先锋冲击力。

### Don'ts (7 项红线)

1. **Don't 让全站背景通体变成亮紫色或深紫色** — 背景必须是纯黑（`#000000`）。
2. **Don't 出现导致正文看不清的低对比度深紫文字** — 正文字色必须为高清晰度的锌白（`#A1A1AA`）。
3. **Don't 使用生硬直角（0px）或小圆角（2–4px）** — 保持 24px 的圆润 3D 质感。
4. **Don't 使用黄色或暖绿杂色进行状态混搭** — 保持霓虹紫、洋红与纯黑的潮酷纯粹性。
5. **Don't 忽视顶层白高光内阴影** — 失去 `inset 0 1px 0` 将导致卡片扁平失去 3D 感。
6. **Don't 堆砌大量彩色 emoji** — 使用现代等宽字符与霓虹 Badge 替代。
7. **Don't 在卡片悬浮时添加失真的夸张形变** — 保持平滑克制的 `translateY(-4px)` 与发光扩展。

---

## 8. Responsive Behavior & Breakpoints

### Breakpoint Groups

| Breakpoint | Range | Target Device | Layout Adaptation Rules |
|---|---|---|---|
| **Mobile** | `< 640px` | 手机端 | 页面边距 `16px`；Hero 字号 `38px~46px`；卡片组降为 1 列；局部极光尺寸缩小至 `300px`；圆角微调至 `16px`。 |
| **Tablet** | `640px ~ 1024px` | iPad / 平板 | 页面边距 `24px`；Hero 字号 `50px~60px`；卡片组 2 列（推荐卡片自适应展开）；极光居中轻微弥散。 |
| **Desktop** | `1024px ~ 1400px`| 标准桌面显示器 | 启用完整 `1220px` 版心；Hero 字号 `64px~76px`；3 列卡片优雅并排；展示完整右上局部流体光晕。 |
| **Wide** | `> 1400px` | 4K / 超宽大屏 | 版心锁定 `1220px` 居中；全屏黑底衬托对角线极光波浪。 |

---

## 9. 核心特征组件拼装示范 (Signature Component Snippets)

### Quick Reference Tokens

```
Background:        #000000 (Pure Black Base), #0F0F0F (3D Surface Card)
Overlay:           Film Grain Noise (opacity: 0.045)
Text primary:      #FFFFFF (Pure White)
Text secondary:    #A1A1AA (Zinc Gray)
Text muted:        #71717A
Primary Signal:    #A855F7 (Neon Purple, Eyebrow, Key Metrics)
Secondary Signal:  #EC4899 (Neon Magenta, Accent)
Border:            rgba(255, 255, 255, 0.10) (Default), rgba(168, 85, 247, 0.60) (Glow)
Radius:            24px (Cards), 48px (Mockup), 999px (Pill Tag)
Fonts:             Display: Inter, PingFang SC (900 for Hero, 400 for Body)
                   Mono: JetBrains Mono (500)
```

### 1. 3D Embossed Card Grid with Neon Glow (3D 浮雕高光卡片组)

```html
<div class="cards-3">
  <div class="num-card">
    <div class="tag">NEURAL 01</div>
    <h3>着色器超分引擎</h3>
    <p>自研实时空间采样与光线步进算法，在端侧以极低算力开销呈现电影级光影。</p>
  </div>
  
  <!-- 推荐状态使用 .selected 激发霓虹紫强光晕 -->
  <div class="num-card selected">
    <div class="tag">FLAGSHIP CORE</div>
    <h3>多维极光流体动力学</h3>
    <p>深度融合 Navier-Stokes 方程与神经拟合场，实现毫秒级高保真烟雾与极光波浪解算。</p>
  </div>
  
  <div class="num-card">
    <div class="tag">AUDIO 03</div>
    <h3>空间音频环境声场</h3>
    <p>根据三维网格几何与材质反射系数动态构建卷积混响，实现 360° 沉浸声场定位。</p>
  </div>
</div>
```

### 2. Cyber Shader Code Terminal (赛博着色器终端窗口)

```html
<div class="code-block">
  <div class="code-header">
    <div class="controls">
      <span class="ctrl-dot" style="background: #A855F7; box-shadow: 0 0 8px #A855F7;"></span>
      <span class="ctrl-dot" style="background: #EC4899; box-shadow: 0 0 8px #EC4899;"></span>
      <span class="ctrl-dot" style="background: #06B6D4; box-shadow: 0 0 8px #06B6D4;"></span>
    </div>
    <div class="code-title">aurora-raymarch.glsl</div>
    <div class="code-badge">GLSL</div>
  </div>
  <pre><code class="language-glsl"><span class="token-comment">// 3D 极光光线步进核心着色器</span>
<span class="token-keyword">vec4</span> raymarchAurora(<span class="token-keyword">vec3</span> ro, <span class="token-keyword">vec3</span> rd) {
  <span class="token-keyword">vec4</span> col = <span class="token-keyword">vec4</span>(0.0);
  <span class="token-keyword">float</span> t = 0.1;
  <span class="token-keyword">for</span>(<span class="token-keyword">int</span> i = 0; i &lt; 64; i++) {
    <span class="token-keyword">vec3</span> p = ro + rd * t;
    <span class="token-keyword">float</span> den = densityField(p);
    col.rgb += neonColor(p) * den * 0.05;
    t += max(0.02, 0.01 * t);
  }
  <span class="token-keyword">return</span> col;
}</code></pre>
</div>
```

### 3. Pure Black Hero Section with Localized Aurora (纯黑视口与局部右上流体光弧)

```html
<section class="hero-section" style="position: relative; overflow: hidden; background: #000000; padding: 96px 0;">
  <!-- 局部右上流光弧 -->
  <div class="hero-aurora-glow" style="position: absolute; top: -120px; right: -100px; width: 650px; height: 650px; background: radial-gradient(circle, rgba(168, 85, 247, 0.35) 0%, rgba(236, 72, 153, 0.15) 40%, transparent 70%); border-radius: 50%; filter: blur(48px); pointer-events: none;"></div>
  
  <div class="eyebrow">
    <span class="diamond">◆</span>
    <span>01 // CREATIVE HORIZON</span>
  </div>
  <h1 class="hero">重塑数字感官的<br>先锋创意引擎。</h1>
  <p class="lead">在纯黑画布上谱写流体极光与胶片微粒的现代视觉交响乐。</p>
</section>
```

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配暗紫流体极光风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: true,
    background: "#0D0D11",
    primaryColor: "#16121E",
    primaryTextColor: "#FFFFFF",
    primaryBorderColor: "#EC4899",
    lineColor: "#A855F7",
    secondaryColor: "#20162B",
    tertiaryColor: "#0A0A0F",
    fontFamily: '"Inter", sans-serif'
  }
});
```
