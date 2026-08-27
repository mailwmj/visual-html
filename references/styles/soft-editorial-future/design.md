# Soft Editorial Future (极简未来展厅风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Soft Editorial Future（极简未来展厅风 / Apple-Grade Showroom）将高级数字艺术展厅、前沿苹果发布会美学与极简社论排版升华为界面语言。全站以纯净通透的**浅灰蓝高光画板（`#EAEFF4` / `#F0F4F8`）**为画布基底，在全局固定视口层（`body::before`）注入 4 组大椭圆柔和弥散光晕，并在各章节穿插散布**3D 柔润晕染液体彩球（3D Soft Blooming Color Orbs）**，彻底告别沉闷压抑的暗黑夜景风。

界面的核心魅力在于**高光玻璃拟态展柜、3D 柔润液体彩球与通透纯粹的现代排版（Glassmorphism Showroom, Blooming Orbs & Pure Modernism）**：

1. **浅灰蓝高光环境背景（Layer 0: Ambient Light & 3D Blooming Orbs）**：
   - 视口底层铺设 4 组柔和椭圆光晕（粉橙、青翠、淡蓝、柔紫），并在各 section 背景中散布 3D 晕染液体彩球。
   - 彩球内部色彩天然平滑晕开，边缘柔和无生硬轮廓线，营造自然流淌的艺术展厅光影。
2. **高透双层内发光毛玻璃卡片（Layer 2: Glassmorphism Showroom Cards）**：
   - 玻璃卡片采用双层高光边框（`border: 1px solid rgba(255, 255, 255, 0.8)`）配合 28px 饱和度增强磨砂（`blur(28px) saturate(180%)`）与微内发光（`inset 0 1px 1px #fff`），在浅色背景上展现出晶莹剔透的高阶质感。
3. **数码皇家蓝点睛通道（`#0071E3`）**：
   - 核心聚焦项、推荐状态与重要指标使用高阶苹果蓝，形成 3%~5% 的克制点睛。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Canvas (Light Showroom) | `rgb(234, 239, 244)` | `#EAEFF4` | `--canvas-1` | 全局浅灰蓝高光画板底色 |
| Canvas Surface (Subtle) | `rgb(240, 244, 248)` | `#F0F4F8` | `--canvas-2` | 局部高光微过渡底色 |
| Glass Surface (Normal) | `rgba(255, 255, 255, 0.82)` | `linear-gradient(...)` | `--glass-bg` | 高透毛玻璃主卡片底色 |
| Text (Deep Showroom Ink)| `rgb(17, 20, 24)` | `#111418` | `--ink-1` | 主标题、核心数据（深黑墨色） |
| Text (Secondary Slate) | `rgb(74, 85, 104)` | `#4A5568` | `--ink-2` | 正文段落、导读副标题 |
| Text (Muted Soft Blue) | `rgb(130, 146, 161)` | `#8292A1` | `--ink-3` | 占位符、注释、等宽元数据标签 |
| Accent Blue (Apple Blue) | `rgb(0, 113, 227)` | `#0071E3` | `--accent-blue` | 核心聚焦通道、推荐态外框与高亮 |

### CSS Design Tokens

```css
:root {
  /* Canvas & Surface Colors (浅灰蓝高光展厅) */
  --canvas-1: #EAEFF4;
  --canvas-2: #F0F4F8;
  --canvas-deep: #DDE5ED;
  
  /* Ink & Typography Colors */
  --ink-1: #111418;
  --ink-2: #4A5568;
  --ink-3: #8292A1;
  --ink-muted: #9BAEC1;

  /* Accent & Signal Colors */
  --accent-blue: #0071E3;
  --accent-blue-soft: rgba(0, 113, 227, 0.08);
  --accent-blue-border: rgba(0, 113, 227, 0.35);
  
  --signal-success: #34C759;
  --signal-success-bg: rgba(52, 199, 89, 0.08);
  --signal-warning: #FF9500;
  --signal-warning-bg: rgba(255, 149, 0, 0.08);
  --signal-error: #FF3B30;
  --signal-error-bg: rgba(255, 59, 48, 0.08);

  /* Typography Stack */
  --font-display: "SF Pro Display", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-ui: "SF Pro Text", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-mono: "IBM Plex Mono", "SF Mono", "JetBrains Mono", "Cascadia Code", Consolas, monospace;

  /* Glassmorphism Variables */
  --glass-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.82) 0%, rgba(255, 255, 255, 0.46) 100%);
  --glass-bg-hover: linear-gradient(135deg, rgba(255, 255, 255, 0.90) 0%, rgba(255, 255, 255, 0.55) 100%);
  --glass-bg-selected: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(235, 245, 255, 0.65) 100%);
  --glass-border: rgba(255, 255, 255, 0.8);
  --glass-border-subtle: rgba(255, 255, 255, 0.45);
  --glass-blur: blur(28px) saturate(180%);
  --glass-shadow: 0 16px 40px -8px rgba(18, 38, 63, 0.05), inset 0 1px 1px 0 rgba(255, 255, 255, 0.95), inset 0 0 0 1px rgba(255, 255, 255, 0.5);
  --glass-shadow-hover: 0 22px 48px -10px rgba(18, 38, 63, 0.09), inset 0 1px 2px 0 rgba(255, 255, 255, 1), inset 0 0 0 1px rgba(255, 255, 255, 0.7);
  --glass-shadow-selected: 0 20px 44px -8px rgba(0, 113, 227, 0.16), inset 0 1px 2px 0 rgba(255, 255, 255, 1), inset 0 0 0 1.5px rgba(0, 113, 227, 0.4);

  /* Layout & Spacing */
  --container: 1160px;
  --radius-lg: 24px;
  --radius-md: 18px;
  --radius-sm: 12px;
  --radius-pill: 999px;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

生成任何 Soft Editorial Future 页面时，必须严格包含以下环境光晕层与柔光彩球规范，**严禁使用暗黑背景**：

```css
/* 全局浅灰蓝环境光晕 */
body::before {
  content: "";
  position: fixed;
  inset: -80px;
  z-index: -2;
  pointer-events: none;
  background:
    radial-gradient(ellipse 650px 500px at 15% 15%, rgba(138, 196, 255, 0.25) 0%, transparent 65%),
    radial-gradient(ellipse 600px 500px at 85% 20%, rgba(255, 208, 168, 0.20) 0%, transparent 65%),
    radial-gradient(ellipse 700px 550px at 10% 65%, rgba(217, 210, 255, 0.18) 0%, transparent 65%),
    radial-gradient(ellipse 650px 550px at 90% 85%, rgba(158, 228, 182, 0.18) 0%, transparent 65%),
    linear-gradient(180deg, #EAEFF4 0%, #F0F4F8 50%, #DDE5ED 100%);
  filter: blur(60px);
}
```

---

## 4. Do's and Don'ts

### Do's (7 项金律)

1. **Do 必须使用浅灰蓝高光画板（`#EAEFF4` / `#F0F4F8`）** — 保持苹果展厅级明亮通透。
2. **Do 必须在卡片上应用双层内发光毛玻璃（`blur(28px) saturate(180%)` + `inset 0 1px 1px #fff`）** — 呈现剔透质感。
3. **Do 背景穿插散布 3D 柔润液体彩球** — 内部色彩天然晕开，边缘平滑无生硬黑线。
4. **Do 大标题使用现代无衬线粗体（字重 800，紧凑字距 `-0.03em`）** — 呈现极致前沿纯粹。
5. **Do 正文字色使用高对比墨色（`#111418` / `#4A5568`）** — 确保完美的阅读可读性。
6. **Do 使用数码皇家蓝（`#0071E3`）作为核心点睛通道**。
7. **Do 保持圆角在 18px~24px 的优雅大圆角**。

### Don'ts (7 项红线)

1. **Don't 篡改为暗黑黑底背景（如 `#0C131F`）** — 必须保持浅灰蓝未来展厅明亮基调。
2. **Don't 丢失毛玻璃的 `backdrop-filter` 与双层高光边框** — 否则退化为普通扁平灰色块。
3. **Don't 使用生硬生涩的人工高斯模糊失焦点阵** — 保持 3D 彩球的自然柔光渐变。
4. **Don't 使用沉闷肮脏的重黑阴影** — 阴影必须是浅蓝微透柔光（`rgba(18, 38, 63, 0.05)`）。
5. **Don't 使用低对比度的浅灰文字** — 正文必须清晰深邃。
6. **Don't 堆砌刺眼杂乱的多彩霓虹** — 强调色仅限苹果蓝与红黄绿三色语义信号。
7. **Don't 使用生硬直角（0px）**。

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配极简未来展厅风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: true,
    background: "#0C131F",
    primaryColor: "#162032",
    primaryTextColor: "#F8FAFC",
    primaryBorderColor: "#38BDF8",
    lineColor: "#38BDF8",
    secondaryColor: "#111827",
    tertiaryColor: "#0C131F",
    fontFamily: ""SF Pro Display", "Inter", sans-serif"
  }
});
```
