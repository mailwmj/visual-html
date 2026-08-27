# Play Tubular (玩味极客彩管风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Play Tubular（玩味极客彩管风 / Play Engineering）将顶级前沿 AI/LLM 架构展示、开发者大会发布会与玩味创意工程学升华为一套极具视觉辨识度的设计系统。界面以温润耐看的浅暖米白点阵画布（`#FAF8F3` / `#F4F0E6`，底层铺设 32px 微型半调点阵）为底，穿插粗壮鲜活的 **3D 渐变立体彩管回路（3D Tubular Loops & Noodle Curves）**，赋予画面充沛的高能视觉张力。

界面的核心魅力在于**全屏 3D 渐变彩管环境背景、半调网点光影、通体连贯承托画板与弹簧动力学动效（Ambient 3D Tubes SVG, Halftone Matrix, Continuous Main Sheet & Spring Dynamics）**：

1. **核心环境背景（`<div class="ambient-tubes-bg">`，灵魂图层，绝对强制）**：
   - 页面背景固定内嵌全屏 SVG 矢量图层，包含 5 组高阶多停点能量渐变（电光彩虹、日落金黄、极光青绿、绯红珊瑚、春日青翠）、3D 弥散悬浮阴影（`feDropShadow`）与半调网点云。
   - 巨型日落大圆环（Sunset Giant Torus Loop）与电光长管穿插纵深回旋，构成标志性视觉空间。
2. **一体化通体正文承托画布（`<main class="main-sheet">`，拒绝切碎分散）**：
   - 为确保长文本阅读的高清晰度与舒适性，所有正文章节与组件全部收敛承托于单一连贯的一体化画板内（`background: rgba(255, 255, 255, 0.94)`，搭配 `backdrop-filter: blur(24px)` 与 36px 超大圆角）。
   - 背景 3D 彩管穿透环绕在画板两侧与上下，形成“悬浮于能量管道之上的现代工程展台”。
3. **高能玩味组件细节（Vibrant Engineering Details）**：
   - **数据卡片（`.stat-card`）**：蓝/橙/绿微透底色搭配能量渐变裁剪文字（`-webkit-background-clip: text`）。
   - **数字卡片（`.num-card`）**：顶部 44px 悬浮药丸彩条（`::before`）+ 渐变大号等宽数字。
   - **流程步骤（`.step .idx`）**：52×52px、18px 倒角的高能渐变发光序号方块。
   - **现代工程粗黑体与弹簧动效**：Neo-Grotesque 粗黑体（字重 900，`-0.035em` 紧凑字距）；交互配置弹簧回弹手感（`cubic-bezier(0.34, 1.56, 0.64, 1)`），悬浮轻盈跃升。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (Warm Cream) | `rgb(250, 248, 243)` | `#FAF8F3` | `--bg` | 全局浅暖米白点阵画布底色 |
| Background (Subtle Tint) | `rgb(244, 240, 230)` | `#F4F0E6` | `--bg-subtle` | 局部点阵背景微过渡、次级背景 |
| Board Surface (Main Sheet) | `rgba(255, 255, 255, 0.94)`| `rgba(255,255,255,.94)`| `--bg-plate` | 一体化通体正文承托画板 |
| Surface (Crisp White Card) | `rgb(255, 255, 255)` | `#FFFFFF` | `--bg-card` | 内部纯白大圆角卡片底色 |
| Surface (Card Subtle) | `rgb(250, 249, 246)` | `#FAF9F6` | `--bg-card-subtle` | 表格表头、次级卡片底色 |
| Text (High-Contrast Ink) | `rgb(17, 17, 17)` | `#111111` | `--text-primary` | 粗黑主标题、核心文字（深黑墨色） |
| Text (Secondary Charcoal) | `rgb(74, 74, 72)` | `#4A4A48` | `--text-secondary` | 正文段落、导读副标题 |
| Text (Muted Warm Gray) | `rgb(126, 126, 122)` | `#7E7E7A` | `--text-muted` | 占位符、注释、等宽元数据标签 |
| Border (Warm Subtle) | `rgba(17, 17, 17, 0.08)` | `rgba(17,17,17,.08)` | `--border` | 1px 卡片边框、模块分割线 |
| Border (Strong / Active) | `rgb(37, 99, 235)` | `#2563EB` | `--border-active` | 活跃推荐卡片边框、高亮轮廓 |

### Vibrant Multi-Stop Master Gradients

| Gradient Name | CSS Value | Usage |
|---|---|---|
| `--grad-blue-magenta` | `linear-gradient(135deg, #2563EB 0%, #7928CA 50%, #FF0080 100%)` | 经典蓝紫洋红主能量渐变 |
| `--grad-orange-gold` | `linear-gradient(135deg, #FF4500 0%, #FF8A00 50%, #FFD600 100%)` | 烈橙暖金日落能量渐变 |
| `--grad-emerald-cyan` | `linear-gradient(135deg, #00C853 0%, #00E5FF 100%)` | 翡翠青翠极光渐变 |
| `--grad-coral-purple` | `linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 50%, #C77DFF 100%)` | 珊瑚粉紫能量渐变 |
| `--grad-cobalt-lime` | `linear-gradient(135deg, #2563EB 0%, #06B6D4 50%, #84CC16 100%)` | 钴蓝青柠檬能量渐变 |
| `--grad-electric-flow` | `linear-gradient(135deg, #1D4ED8 0%, #5500FF 22%, #D000FF 48%, #FF0066 72%, #FF5500 88%, #FFD000 100%)` | 6 停点核心高能流动渐变 |

### CSS Design Tokens

```css
:root {
  /* 背景层：暖米白底色与点阵质感 */
  --bg: #FAF8F3;
  --bg-subtle: #F4F0E6;
  --bg-card: #FFFFFF;
  --bg-card-subtle: #FAF9F6;

  /* 文字墨色层 */
  --text-primary: #111111;
  --text-secondary: #4A4A48;
  --text-muted: #7E7E7A;
  --text-inverse: #FFFFFF;

  /* 核心多停点能量渐变 */
  --grad-blue-magenta: linear-gradient(135deg, #2563EB 0%, #7928CA 50%, #FF0080 100%);
  --grad-orange-gold: linear-gradient(135deg, #FF4500 0%, #FF8A00 50%, #FFD600 100%);
  --grad-emerald-cyan: linear-gradient(135deg, #00C853 0%, #00E5FF 100%);
  --grad-coral-purple: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 50%, #C77DFF 100%);
  --grad-cobalt-lime: linear-gradient(135deg, #2563EB 0%, #06B6D4 50%, #84CC16 100%);
  --grad-electric-flow: linear-gradient(135deg, #1D4ED8 0%, #5500FF 22%, #D000FF 48%, #FF0066 72%, #FF5500 88%, #FFD000 100%);

  /* 单一高饱和点睛色 */
  --accent-blue: #2563EB;
  --accent-orange: #FF5500;
  --accent-yellow: #FFD600;
  --accent-green: #00C853;
  --accent-magenta: #FF0080;
  --accent-purple: #7928CA;

  /* 边框与阴影 */
  --border: rgba(17, 17, 17, 0.08);
  --border-strong: rgba(17, 17, 17, 0.16);
  --border-active: #2563EB;
  
  --shadow-card: 0 8px 24px rgba(17, 17, 17, 0.04), 0 1px 3px rgba(17, 17, 17, 0.02);
  --shadow-card-hover: 0 16px 36px rgba(37, 99, 235, 0.12), 0 4px 12px rgba(255, 69, 0, 0.08);
  --shadow-pop: 0 20px 48px rgba(37, 99, 235, 0.18), 0 6px 16px rgba(255, 0, 128, 0.10);

  /* 交互动效与缓动 (Spring Bounce Motion) */
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 0.25s;
  --duration-normal: 0.35s;

  /* 尺寸与圆角规范 */
  --radius: 24px;
  --radius-sm: 14px;
  --radius-pill: 999px;
  --container: 1180px;

  /* 字体栈 */
  --font-display: "Plus Jakarta Sans", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", "SFMono-Regular", Consolas, monospace;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

生成任何 Play Tubular 网页时，必须严格遵守以下外层三层结构，**严禁省略或拆散**：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <!-- 字体与 CSS Tokens -->
</head>
<body>

<!-- 1. 全局固定 3D 彩管与半调网点环境背景 (Ambient 3D Tubular Noodle Canvas Layer) -->
<div class="ambient-tubes-bg" aria-hidden="true">
  <svg viewBox="0 0 1600 1200" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="pt-grad-rainbow-u" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0047FF" />
        <stop offset="25%" stop-color="#5500FF" />
        <stop offset="50%" stop-color="#C800FF" />
        <stop offset="72%" stop-color="#FF0077" />
        <stop offset="88%" stop-color="#FF5500" />
        <stop offset="100%" stop-color="#FFC700" />
      </linearGradient>

      <linearGradient id="pt-grad-sunset-gold" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FF1E00" />
        <stop offset="26%" stop-color="#FF7300" />
        <stop offset="54%" stop-color="#FFAE00" />
        <stop offset="80%" stop-color="#FFD600" />
        <stop offset="100%" stop-color="#76FF03" />
      </linearGradient>

      <linearGradient id="pt-grad-aurora-mint" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00FF88" />
        <stop offset="35%" stop-color="#00E5FF" />
        <stop offset="70%" stop-color="#0055FF" />
        <stop offset="100%" stop-color="#7928CA" />
      </linearGradient>

      <linearGradient id="pt-grad-scarlet-coral" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FF1A00" />
        <stop offset="50%" stop-color="#FF4800" />
        <stop offset="100%" stop-color="#FF8A00" />
      </linearGradient>

      <linearGradient id="pt-grad-spring-lime" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00E676" />
        <stop offset="50%" stop-color="#00F5A0" />
        <stop offset="100%" stop-color="#A3E635" />
      </linearGradient>

      <pattern id="pt-halftone-cloud" x="0" y="0" width="14" height="14" patternUnits="userSpaceOnUse">
        <circle cx="7" cy="7" r="2.2" fill="#111111" opacity="0.10" />
      </pattern>

      <filter id="pt-shadow-3d" x="-20%" y="-20%" width="150%" height="150%">
        <feDropShadow dx="0" dy="28" stdDeviation="24" flood-color="#0A0A16" flood-opacity="0.17" />
      </filter>
      <filter id="pt-shadow-soft" x="-20%" y="-20%" width="150%" height="150%">
        <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#0A0A16" flood-opacity="0.10" />
      </filter>
    </defs>

    <rect x="940" y="60" width="480" height="480" rx="220" fill="url(#pt-halftone-cloud)" />
    <rect x="60" y="640" width="380" height="380" rx="160" fill="url(#pt-halftone-cloud)" />

    <!-- 1. 左上方流体组 -->
    <g filter="url(#pt-shadow-soft)" opacity="0.90">
      <path d="M -60 140 C 120 90, 320 120, 480 240" stroke="url(#pt-grad-scarlet-coral)" stroke-width="72" stroke-linecap="round" fill="none" />
      <path d="M -40 280 C 140 260, 220 400, 160 560 C 100 700, -20 780, -60 840" stroke="url(#pt-grad-rainbow-u)" stroke-width="76" stroke-linecap="round" fill="none" />
    </g>

    <!-- 2. 右上方主视觉群：巨型日落大圆环 + 电光长管穿插 + 极光弧 -->
    <g filter="url(#pt-shadow-3d)" opacity="0.95">
      <path d="M 1100 -50 C 1360 60, 1540 300, 1340 520 C 1140 700, 940 520, 1080 340 C 1180 200, 1420 180, 1560 280" stroke="url(#pt-grad-sunset-gold)" stroke-width="78" stroke-linecap="round" fill="none" />
      <path d="M 720 -80 C 680 160, 860 320, 1140 460 C 1380 580, 1520 820, 1380 1040" stroke="url(#pt-grad-rainbow-u)" stroke-width="74" stroke-linecap="round" fill="none" />
      <path d="M 1520 360 C 1360 420, 1240 620, 1380 800 C 1500 940, 1640 920, 1720 1060" stroke="url(#pt-grad-aurora-mint)" stroke-width="60" stroke-linecap="round" fill="none" />
    </g>

    <!-- 3. 底部笑脸大弧管与极光穿插 -->
    <g filter="url(#pt-shadow-soft)" opacity="0.88">
      <path d="M -80 720 C 140 740, 280 920, 200 1120" stroke="url(#pt-grad-spring-lime)" stroke-width="64" stroke-linecap="round" fill="none" />
      <path d="M -30 960 C 200 910, 400 1020, 520 1200" stroke="url(#pt-grad-aurora-mint)" stroke-width="52" stroke-linecap="round" fill="none" />
    </g>
  </svg>
</div>

<!-- 2. 一体化通体正文承托画布 (所有 section 都包裹在 main.main-sheet 内) -->
<main class="main-sheet">
  <!-- 页面各 Section 自上而下流淌 -->
</main>

</body>
</html>
```

---

## 4. Typography Scale & Rules

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | clamp(38px, 6vw, 68px) | 900 | 1.06 | **-0.035em** | `--font-display` | 现代工程粗黑大标题 |
| **Section Title** | `h2.section-title` | clamp(26px, 3.8vw, 42px) | 850 | 1.15 | **-0.025em** | `--font-display` | 章节二级标题 |
| **Lead Paragraph** | `.lead` | clamp(16px, 1.8vw, 20px) | 500 | 1.65 | normal | `--font-sans` | 导读段落（温暖深墨） |
| **Eyebrow** | `.eyebrow` | 13px | 700 | 1.0 | **0.08em** | `--font-mono` | 药丸白底带有橙金渐变球标头 |
| **Stat Metric** | `.stat-val` | clamp(44px, 5vw, 64px) | 900 | 1.0 | -0.03em | `--font-display` | 核心量化指标超大数值（单位渐变裁剪） |
| **Card Title** | `h3` | 20px~22px | 800 | 1.3 | -0.02em | `--font-display` | 模块/卡片核心标题 |

---

## 5. Signature Component Patterns (核心特征组件规范)

### 1. Stats Grid (带有微透色底与渐变单位的数据卡片)

```html
<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-val">300<span>%</span></div>
    <div class="stat-label">ANNUAL GROWTH</div>
  </div>
  <div class="stat-card">
    <div class="stat-val">1.2<span>M</span></div>
    <div class="stat-label">ACTIVE USERS</div>
  </div>
</div>
```

### 2. Number Cards with Floating Pill (带顶部悬浮药丸彩条的数字卡片)

```html
<div class="cards-3">
  <div class="num-card">
    <div class="num">01</div>
    <h3>模块一核心功能</h3>
    <p>模块基础能力与运行逻辑描述。</p>
    <div class="tag">BASE</div>
  </div>
  <div class="num-card selected">
    <div class="num">02</div>
    <h3>推荐核心功能</h3>
    <p>这是推荐项，带有数码皇家蓝高亮轮廓与多色渐变高能浮层。</p>
    <div class="tag">RECOMMENDED</div>
  </div>
</div>
```

### 3. Step Badge (高能渐变大圆角方块序号)

```html
<div class="steps">
  <div class="step">
    <div class="idx">01</div>
    <div>
      <h3>意图识别与解析</h3>
      <p>分析用户输入的长篇文本与目标场景，提取关键信息与数据骨架。</p>
    </div>
  </div>
</div>
```

---

## 6. Do's and Don'ts

### Do's (7 项金律)

1. **Do 必须在 `<body>` 顶部内嵌完整全屏 3D 渐变彩管 SVG 图层（`<div class="ambient-tubes-bg">`）** — 它是 Play Tubular 风格最核心的灵魂视觉。
2. **Do 正文全部收敛在一体化通体画板（`<main class="main-sheet">`）内** — 确保磨砂白板在中央承载长文，背景彩管在外层自然环绕。
3. **Do 在卡片与数字上使用高能多停点渐变** — 如数据单位渐变裁剪、数字卡片顶部 44px 悬浮彩条、步骤 52×52px 渐变发光方块。
4. **Do 大标题使用 Neo-Grotesque 粗黑体（字重 900，`-0.035em` 字距）** — 呈现兼具工程严谨与潮玩张力的视觉。
5. **Do 卡片使用 24px 大圆角与弹簧动效（`cubic-bezier(0.34, 1.56, 0.64, 1)`）** — 营造轻快回弹手感。
6. **Do 推荐态（`.selected`）配置数码皇家蓝边框与多色渐变投影（`var(--shadow-pop)`）** — 确保焦点绝对突出。
7. **Do 保持正文使用深黑高清晰墨色（`#111111` / `#4A4A48`）** — 确保极致的阅读可读性。

### Don'ts (7 项红线)

1. **Don't 丢失 `<div class="ambient-tubes-bg">` 矢量背景** — 缺少 3D 彩管背景会导致风格退化为普通简陋的 SaaS 网页。
2. **Don't 将页面切碎成一段段孤立的裸 `<section>`** — 必须全部承托在 `<main class="main-sheet">` 内。
3. **Don't 丢掉数据卡片与数字卡片的彩条、渐变剪裁与微透底色** — 否则会丧失玩味工程的质感。
4. **Don't 将步骤序号降级为单薄的淡色小圆圈** — 必须使用 52×52px、18px 倒角的高能渐变序号方块。
5. **Don't 使用沉闷肮脏的纯黑重阴影** — 阴影必须是多色渐变微透柔光（如 `rgba(37, 99, 235, 0.12)`）。
6. **Don't 使用生硬直角（0px）或极小圆角** — 卡片必须保持 24px 圆润大圆角。
7. **Don't 堆砌杂乱的彩色 Emoji** — 使用矢量半调标头与工程符号替代。

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配玩味极客彩管风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: false,
    background: "#FAF8F3",
    primaryColor: "#FFFFFF",
    primaryTextColor: "#111111",
    primaryBorderColor: "#2563EB",
    lineColor: "#2563EB",
    secondaryColor: "#FFF1EB",
    tertiaryColor: "#FAF8F3",
    fontFamily: '"Plus Jakarta Sans", -apple-system, sans-serif'
  }
});
```
