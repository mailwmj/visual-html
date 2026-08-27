# Nothing Design Light (Nothing 极简点阵亮白风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Nothing Design Light 是 Nothing 设计语言的白瓷工程版（White Ceramic Edition），灵感源自 Nothing Phone 白色版、Braun 经典白净工业品（Dieter Rams SK4 音响 / ET66 计算器）以及 Teenage Engineering OP-1 Field。

全站以纯粹通透的 **陶瓷冷白底色 (`#FFFFFF` / `#F8F8F8`)** 与浅灰物理表面（`#F4F4F4` / `#EFEFEF`）为画布基底，卡片内铺设 16–24px 极淡暗色点阵网格（Dark Dot Matrix Lattice，2.5%~4% 不透明度），构建如同高精度工程蓝图与包豪斯纸质白皮书般的严谨骨架。

界面的核心哲学依然是 **“Subtract, don't add. Structure is ornament.”（极度克制，以骨架为装饰，以数据为色彩）**：
1. **三层视觉层级律 (The Three-Layer Rule)**：每个页面与长文区块严格划分为 **Primary（Doto 点阵超大纯黑数码与标题）**、**Secondary（Space Grotesk 高对比度深灰正文与副标）**、**Tertiary（Space Mono 全大写等宽仪器元数据与标签）** 三层。
2. **多通道功能遥测色谱（亮白高对比调校）**：
   - **Nothing 标志性信号红/珊瑚橙 (`#D71921` / `#E03E15`)**：用于 Eyebrow 标头红点、重点指标单位、选中态高亮与重要警示（用量 ≤ 4%）。
   - **遥测翡翠绿 (`#16A34A`)**：用于成功状态 `[ NOMINAL ]`、Pro 正向清单、健康分段刻度条。
   - **遥测琥珀金 (`#D97706`)**：用于 Warning 警示框、次级分类分段槽、待确认状态。
   - **电气深蓝 (`#0284C7`)**：用于网络数据流、接口参数与代码语法高亮。
   - **实体纯黑 (`#000000`)**：用于 Doto 点阵超大数码、主进度分段条与硬朗线框。
3. **白瓷硬件级长文组件质感**：
   - **点阵宏观数据卡片 (Stats Grid)**：Doto 变量点阵字 + 纯黑与彩色分段式刻度槽 (`.seg-meter`)。
   - **仪器规格参数栏 (Spec Row)**：等宽数值 + 单位 + 1px 极细发丝边框 (`#E5E5E5`)。
   - **硬件提示框 (Admonitions with LED)**：白瓷底色 + 信号红 / 翡翠绿 / 琥珀金发光 LED 状态点。
   - **0-shadow 物理平面**：剔除所有弥散阴影，依靠 1px 细线框（`#E5E5E5` / `#D4D4D4`）与浅灰底座划分层级。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (Ceramic White) | `rgb(255, 255, 255)` | `#FFFFFF` | `--bg` | 全局高洁陶瓷白画布基底 |
| Surface (Matte Deck) | `rgb(244, 244, 244)` | `#F4F4F4` | `--surface-1` | 实体卡片、模块底座（平坦物理阻断） |
| Surface (Elevated / Panel) | `rgb(238, 238, 238)` | `#EEEEEE` | `--surface-2` | 悬浮卡片、交互高亮区、次级面板 |
| Surface (Track / Inset) | `rgb(228, 228, 228)` | `#E4E4E4` | `--surface-track`| 分段刻度底槽、输入框底色 |
| Surface (Subtle Pill) | `rgb(235, 235, 235)` | `#EBEBEB` | `--surface-pill` | 标签背景、次级胶囊按键底色 |
| Text (Display / Hero) | `rgb(0, 0, 0)` | `#000000` | `--text-display` | Doto 点阵标题、超大数值、反白文本 |
| Text (Primary Body) | `rgb(26, 26, 26)` | `#1A1A1A` | `--text-primary` | 正文段落、主标题、高对比阅读文本 |
| Text (Secondary Context) | `rgb(102, 102, 102)` | `#666666` | `--text-secondary` | 导读副标题、表格内容、辅助解释 |
| Text (Tertiary / Muted) | `rgb(140, 140, 140)` | `#8C8C8C` | `--text-muted` | Space Mono 等宽仪器标签、时间戳、元数据 |
| Border (Default Hairline) | `rgb(229, 229, 229)` | `#E5E5E5` | `--border` | 1px 极细卡片外框、模块分割线 |
| Border (Strong / Wireframe) | `rgb(204, 204, 204)` | `#CCCCCC` | `--border-strong` | 活跃线框、输入框边框、表格外框 |
| Dot Grid Line | `rgba(0, 0, 0, 0.08)` | `rgba(0,0,0,.08)` | `--dot-grid` | 亮白背景清晰雅致点阵纹理 (1px 点径) |

### Multi-Channel Functional Telemetry Palette (Light Mode)

| Channel | Role | Hex | RGBA Token | UI Application |
|---|---|---|---|---|
| **Signal Coral / Red** | 核心信号色 (Primary Signal) | `#D71921` / `#E03E15` | `--signal-coral` | Eyebrow 红点 LED、主数值单位、波形折线、选中态 (用量 ≤ 4%) |
| **Telemetry Green** | 遥测翡翠绿 (Nominal / Success) | `#16A34A` | `--signal-green` | 成功状态 `NOMINAL`、Pro 正向清单、健康分段槽 |
| **Telemetry Amber** | 遥测琥珀金 (Category / Warning) | `#D97706` | `--signal-amber` | Warning 提示框、次级分类分段槽、待确认状态 |
| **Telemetry Deep Blue** | 电气深蓝 (Data / Stream) | `#0284C7` | `--signal-cyan` | 网络通道、数据流向、代码高亮 |
| **High-Contrast Black** | 实体纯黑 (Primary Track) | `#000000` | `--signal-black` | Doto 点阵数码、主进度分段条、主标题 |

### CSS Design Tokens

```css
:root {
  /* 背景层与表面 (Light Mode) */
  --bg: #FFFFFF;
  --surface-1: #F4F4F4;
  --surface-2: #EEEEEE;
  --surface-track: #E4E4E4;
  --surface-pill: #EBEBEB;

  /* 文字层 */
  --text-display: #000000;
  --text-primary: #1A1A1A;
  --text-secondary: #666666;
  --text-muted: #8C8C8C;

  /* 边框与点阵 */
  --border: #E5E5E5;
  --border-strong: #CCCCCC;
  --dot-grid: rgba(0, 0, 0, 0.08);

  /* 多通道功能色谱 */
  --signal-coral: #D71921;
  --signal-red: #D71921;
  --signal-green: #16A34A;
  --signal-amber: #D97706;
  --signal-cyan: #0284C7;
  --signal-black: #000000;

  --accent: var(--signal-coral);
  --accent-subtle: rgba(215, 25, 33, 0.08);

  /* 尺寸与圆角规范 */
  --radius: 12px;
  --radius-sm: 8px;
  --radius-xs: 4px;
  --radius-pill: 999px;
  --container: 1240px;

  /* 间距刻度 (4px 阶梯) */
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 48px; --space-8: 64px;

  /* 字体栈规范 */
  --font-dot: "Doto", "Space Mono", monospace;
  --font-body: "Space Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "HarmonyOS Sans SC", sans-serif;
  --font-mono: "Space Mono", "SFMono-Regular", Consolas, monospace;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

本风格属于 **直铺沉浸型 (Direct Immersive Flow)**。长篇文档正文直接平铺于全景点阵画布上，严禁在章节间添加横贯全屏的粗暴横线分割，纯依靠段落留白与章节 Eyebrow 标头建立节奏。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>NOTHING LIGHT // DOCUMENT_TITLE</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Doto:wght@400;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet" />
<style>
  body {
    background-color: #FFFFFF;
    background-image: radial-gradient(rgba(0, 0, 0, 0.08) 1px, transparent 1px);
    background-size: 20px 20px;
    color: #1A1A1A;
    font-family: var(--font-body);
    margin: 0;
    padding: 0;
  }
  .wrap { max-width: 1240px; margin: 0 auto; padding: 0 32px; }
  section { padding: 64px 0; }
</style>
</head>
<body>
  <!-- 实际页面保留原文结构并按需选用组件；新风格脚手架才按 Phase 1 至 Phase 5 完整展示 18 项组件。 -->
</body>
</html>
```

---

## 4. Typography Scale & Rules

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 56px~76px | 700 | 1.05 | -0.03em | `--font-body` | 页面第一视觉纯黑主标题 |
| **Section Title** | `h2.section-title` | 28px~36px | 700 | 1.15 | -0.02em | `--font-body` | 章节二级大标题 |
| **Card Title** | `h3`, `.card-title` | 17px~19px | 600 | 1.3 | -0.01em | `--font-body` | 模块与卡片核心标题 |
| **Lead Paragraph** | `.lead` | 17px~19px | 300 | 1.65 | 0 | `--font-body` | 核心摘要导读段落（雅致通透） |
| **Body Text** | `p`, `.body` | 15px~16px | 400 | 1.7 | 0 | `--font-body` | 长篇正文与解析说明 |
| **Section Eyebrow** | `.eyebrow` | 11px~12px | 700 | 1.0 | **0.12em** | `--font-mono` | 章节大写索引标头（`● 01 / SPECIFICATION`） |
| **Stat Metric** | `.stat-val` | 44px~56px | 800 | 1.0 | -0.02em | `--font-dot` | 核心量化指标点阵超大数值 |
| **Spec Unit / Label**| `.unit`, `.tag`, `.label` | 10px~11px | 700 | 1.2 | **0.08em** | `--font-mono` | 规格单位、大写状态标签、Badge |
| **Code Block** | `code`, `pre` | 13px | 400 | 1.55 | 0 | `--font-mono` | 代码块、终端命令、API 参数 |
| **Metadata Footer** | `footer .meta` | 11px~12px | 400 | 1.4 | 0.08em | `--font-mono` | 底部对齐的硬件系统元数据 |

---

## 5. Do's and Don'ts

### ✅ 7 项核心金律 (Do's)
1. **必须保持白瓷高洁底色 (`#FFFFFF`) 与 1px 浅灰发丝边框 (`#E5E5E5`)**。
2. **必须使用 Doto 点阵字渲染宏观统计数据中的数值与重点数字**。
3. **必须保留原文结构并按内容语义选用组件**；完整 18 项组件及其 5 阶段顺序只用于新风格脚手架的覆盖测试。
4. **必须使用高对比度纯黑正文 (`#1A1A1A`) 与深灰副标 (`#666666`)**，严格符合 WCAG AAA 级别。
5. **必须使用分段式刻度条 (`.seg-meter`)** 结合黑色与功能色。
6. **必须保持 0-shadow 物理硬朗平面**。
7. **必须保持 Space Mono 全大写等宽仪器标签与 0.08em~0.12em 宽字距**。

### ❌ 7 项严禁红线 (Don'ts)
1. **严禁在亮色背景下使用浅灰色不可读文字**。
2. **严禁使用软糯弥散模糊阴影**。
3. **严禁大面积平涂无语义的亮色渐变**。
4. **严禁脱离原文的正文、章节逻辑与信息层级，或为了凑齐组件而虚构内容**。
5. **严禁用 Doto 点阵字排版整段正文**。
6. **严禁省略 Google Fonts 导入**。
7. **严禁滥用 emoji 替代精密硬件字符标头**。

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配 Nothing 极简点阵亮白风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: false,
    background: "#FFFFFF",
    primaryColor: "#F5F5F5",
    primaryTextColor: "#000000",
    primaryBorderColor: "#D71921",
    lineColor: "#D71921",
    secondaryColor: "#EEEEEE",
    tertiaryColor: "#FFFFFF",
    fontFamily: '"Doto", "Space Mono", monospace'
  }
});
```
