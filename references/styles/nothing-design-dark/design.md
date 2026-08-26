# Nothing Design Dark (Nothing 极简点阵暗黑风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Nothing Design 将瑞士国际主义排版风格（Swiss Typography）与现代工业硬件设计（Dieter Rams / Braun、Teenage Engineering、Nothing Phone / Nothing OS）深度融合，升华为一套纯粹、克制、高可读性且极具辨识度的长篇技术排版与出版级文档设计语言。

全站以深邃极致的 **OLED 纯黑底色 (`#000000`)** 与深灰物理表面（`#111111` / `#161616`）为画布基底，卡片内微弱铺设 16–24px 极淡点阵网格（Dot Matrix Lattice，2.5%~4% 不透明度），构建出如同精密物理规格书与硬件工程文档般的秩序骨架。

界面的核心哲学为 **“Subtract, don't add. Structure is ornament.”（极度克制，以骨架为装饰，以数据为色彩）**：
1. **三层视觉层级律 (The Three-Layer Rule)**：每个页面与长文区块严格划分为 **Primary（Doto 点阵超大视觉焦点与标题）**、**Secondary（Space Grotesk 高清晰度长文正文与副标）**、**Tertiary（Space Mono 全大写等宽仪器元数据与标签）** 三层，杜绝平庸折中的中间态。
2. **多通道功能遥测色谱 (Vibrant Functional Telemetry Palette)**：拒绝无意义的大面积彩色涂抹，将色彩严格绑定于语义状态与数据遥测：
   - **Nothing 珊瑚信号橙/红 (`#FF5722` / `#D71921`)**：用于 Eyebrow 红点 LED、主焦点指标单位、音频/波形折线、选中态高亮与重要警告（用量 ≤ 4%）。
   - **遥测翡翠绿 (`#22C55E`)**：用于通过状态、健康指标、高电量分段条、Pro 正向清单与运行正常指示灯。
   - **遥测琥珀金 (`#F59E0B`)**：用于中度分类分段槽、待确认状态、Warning 警示框与次级指标。
   - **电气霓蓝 (`#38BDF8`)**：用于网络数据流、接口参数与代码语法高亮。
   - **纯粹高对比白 (`#FFFFFF`)**：用于 Doto 点阵数码、主进度条与白标卡片。
3. **硬件级长文组件质感**：
   - **点阵宏观数据卡片 (Stats Grid)**：Doto 变量点阵字 + 彩色分段式刻度槽 (`.seg-meter`)。
   - **仪器规格参数栏 (Spec Row)**：等宽数值 + 单位 + 1px 精密发丝边框。
   - **硬件提示框 (Admonitions with LED)**：珊瑚橙 / 翡翠绿 / 琥珀金顶栏与发光 LED 点。
   - **0-shadow 物理平面**：剔除所有软糯模糊阴影，依靠 1px 细线框（`#222222`）与深黑面板划分层级。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (OLED Black) | `rgb(0, 0, 0)` | `#000000` | `--bg` | 全局 OLED 纯黑画布基底 |
| Surface (Matte Deck) | `rgb(17, 17, 17)` | `#111111` | `--surface-1` | 实体卡片、模块底座（平坦物理阻断） |
| Surface (Elevated / Panel) | `rgb(22, 22, 22)` | `#161616` | `--surface-2` | 悬浮卡片、交互高亮区、次级面板 |
| Surface (Track / Inset) | `rgb(30, 30, 30)` | `#1E1E1E` | `--surface-track`| 仪表轨道、分段底槽、输入框底色 |
| Surface (Subtle Pill) | `rgb(34, 34, 34)` | `#222222` | `--surface-pill` | 标签背景、次级胶囊按键底色 |
| Text (Display / Hero) | `rgb(255, 255, 255)` | `#FFFFFF` | `--text-display` | Doto 点阵标题、超大数值、反白胶囊文本 |
| Text (Primary Body) | `rgb(232, 232, 232)` | `#E8E8E8` | `--text-primary` | 正文段落、主标题、高对比阅读文本 |
| Text (Secondary Context) | `rgb(153, 153, 153)` | `#999999` | `--text-secondary` | 导读副标题、表格内容、辅助解释 |
| Text (Tertiary / Muted) | `rgb(102, 102, 102)` | `#666666` | `--text-muted` | Space Mono 等宽仪器标签、时间戳、元数据 |
| Border (Default Hairline) | `rgb(34, 34, 34)` | `#222222` | `--border` | 1px 极细卡片外框、模块分割线 |
| Border (Strong / Wireframe) | `rgb(48, 48, 48)` | `#303030` | `--border-strong` | 活跃线框、输入框边框、表格外框 |
| Dot Grid Line | `rgba(255, 255, 255, 0.08)` | `rgba(255,255,255,.08)` | `--dot-grid` | 纯黑背景清晰点阵纹理 (1px 点径) |

### Multi-Channel Functional Telemetry Palette

| Channel | Role | Hex | RGBA Token | UI Application |
|---|---|---|---|---|
| **Signal Coral / Red** | 核心信号色 (Primary Signal) | `#FF5722` / `#D71921` | `--signal-coral` | Eyebrow 红点 LED、主数值单位、波形折线、选中态 (用量 ≤ 4%) |
| **Telemetry Green** | 遥测翡翠绿 (Nominal / Success) | `#22C55E` | `--signal-green` | 成功状态 `CONNECTED`、Pro 正向清单、健康分段槽 |
| **Telemetry Amber** | 遥测琥珀金 (Category / Warning) | `#F59E0B` | `--signal-amber` | Warning 提示框、次级分类分段槽、待确认状态 |
| **Telemetry Cyan** | 电气霓蓝 (Data / Stream) | `#38BDF8` | `--signal-cyan` | 网络通道、数据流向、代码高亮 |
| **Crisp White** | 高光纯白 (Primary Track) | `#FFFFFF` | `--signal-white` | Doto 点阵数码、主进度分段条、主标题高光 |

### CSS Design Tokens

```css
:root {
  /* 背景层与表面 */
  --bg: #000000;
  --surface-1: #111111;
  --surface-2: #161616;
  --surface-track: #1E1E1E;
  --surface-pill: #222222;

  /* 文字层 */
  --text-display: #FFFFFF;
  --text-primary: #E8E8E8;
  --text-secondary: #999999;
  --text-muted: #666666;

  /* 边框与点阵 */
  --border: #222222;
  --border-strong: #303030;
  --dot-grid: rgba(255, 255, 255, 0.08);

  /* 多通道功能色谱 */
  --signal-coral: #FF5722;
  --signal-red: #D71921;
  --signal-green: #22C55E;
  --signal-amber: #F59E0B;
  --signal-cyan: #38BDF8;
  --signal-white: #FFFFFF;

  --accent: var(--signal-coral);
  --accent-subtle: rgba(255, 87, 34, 0.12);

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

本风格属于 **直铺沉浸型 (Direct Immersive Flow)**。长篇文档正文直接平铺于 OLED 全景点阵画布上，严禁在章节间添加横贯全屏的粗暴横线分割，纯依靠段落留白与章节 Eyebrow 标头建立节奏。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>NOTHING // DOCUMENT_TITLE</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Doto:wght@400;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet" />
<style>
  body {
    background-color: #000000;
    background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
    background-size: 20px 20px;
    color: #E8E8E8;
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

### Type Scale Table

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Family | Role |
|---|---|---|---|---|---|---|---|
| **Hero Headline** | `h1.hero` | 56px~76px | 700 | 1.05 | -0.03em | `--font-body` | 页面第一视觉主标题（支持中文主动分行） |
| **Section Title** | `h2.section-title` | 28px~36px | 700 | 1.15 | -0.02em | `--font-body` | 章节二级大标题 |
| **Card Title** | `h3`, `.card-title` | 17px~19px | 600 | 1.3 | -0.01em | `--font-body` | 模块与卡片核心标题 |
| **Lead Paragraph** | `.lead` | 17px~19px | 300 | 1.6 | 0 | `--font-body` | 核心摘要导读段落（轻盈通透） |
| **Body Text** | `p`, `.body` | 15px~16px | 400 | 1.7 | 0 | `--font-body` | 长篇正文与解析说明 |
| **Section Eyebrow** | `.eyebrow` | 11px~12px | 700 | 1.0 | **0.12em** | `--font-mono` | 章节大写索引标头（`● 01 / SPECIFICATION`） |
| **Stat Metric** | `.stat-val` | 44px~56px | 800 | 1.0 | -0.02em | `--font-dot` | 核心量化指标点阵超大数值 |
| **Spec Unit / Label**| `.unit`, `.tag`, `.label` | 10px~11px | 700 | 1.2 | **0.08em** | `--font-mono` | 规格单位、大写状态标签、Badge |
| **Code Block** | `code`, `pre` | 13px | 400 | 1.55 | 0 | `--font-mono` | 代码块、终端命令、API 参数 |
| **Metadata Footer** | `footer .meta` | 11px~12px | 400 | 1.4 | 0.08em | `--font-mono` | 底部对齐的硬件系统元数据 |

---

## 5. Signature Component Patterns (18 项标准组件的 Nothing 硬件化呈现)

### 1. Stats Grid 数据卡片（Doto 点阵数码 + 多色分段进度条）

```html
<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-head">
      <span>[ STAT // 01 ]</span>
      <span class="pill-badge coral">CRITICAL</span>
    </div>
    <div class="stat-val">99.8<span class="unit" style="color:var(--signal-coral);">%</span></div>
    <div class="stat-label">BENCHMARK ACCURACY</div>
    <div class="seg-meter">
      <span class="seg fill-white"></span><span class="seg fill-white"></span><span class="seg fill-white"></span>
      <span class="seg fill-white"></span><span class="seg fill-white"></span><span class="seg fill-coral"></span>
      <span class="seg fill-coral"></span><span class="seg"></span><span class="seg"></span><span class="seg"></span>
    </div>
  </div>
</div>
```

### 2. Admonitions 语义提示框（带 LED 状态灯的机械顶栏）

```html
<div class="admonition info">
  <div class="ad-bar">
    <span class="ad-led"></span>
    <span>SYSTEM NOTICE // ARCHITECTURE</span>
    <span class="ad-code">[ CORE_RULE ]</span>
  </div>
  <div class="ad-content">
    <p>核心发现：系统在极限带宽下仍能保持 0.42ms 的端到端响应，架构具备高度抗压冗余。</p>
  </div>
</div>
```

### 3. Comparison Table 对比矩阵（硬边框 + 珊瑚橙高亮推荐列）

```html
<div class="cmp">
  <div class="row head">
    <div class="cell">DESIGN PARAMETER</div>
    <div class="cell coral-col">NOTHING DESIGN</div>
    <div class="cell">GENERIC DARK</div>
  </div>
  <div class="row">
    <div class="cell">Canvas Base</div>
    <div class="cell coral-col"><span class="dot-ind coral"></span>&nbsp;&nbsp;OLED #000000</div>
    <div class="cell">Slate #0F172A</div>
  </div>
</div>
```

---

## 6. Do's and Don'ts (7 项金律与 7 项严禁红线)

### ✅ 7 项核心金律 (Do's)
1. **必须保留原文的正文、章节逻辑与重点信息，并按需选用语义组件**：严禁将文章退化为单纯的 OS 控制中心或无正文仪表盘。完整 18 项组件的固定顺序只用于新风格脚手架的覆盖测试。
2. **必须将多通道功能色谱赋予语义组件**：珊瑚橙（主焦点/推荐/警告）、翡翠绿（成功/健康/Pro）、琥珀金（分类/Con/次级）。
3. **必须使用 OLED 纯黑基底 (`#000000`) 与 1px 细发丝边框**。
4. **必须使用 Doto 点阵字渲染宏观统计数据中的数值与重点数字**。
5. **必须使用分段式刻度条 (`.seg-meter`) 与方括号等宽状态标签 `[ ACTIVE ]`**。
6. **必须保持 0-shadow 物理硬朗平面**：通过平坦深灰卡片（`#111111`）与细线划分空间。
7. **必须保持 Space Mono 全大写等宽仪器标签与 0.08em~0.12em 宽字距**。

### ❌ 7 项严禁红线 (Don'ts)
1. **严禁脱离原文内容与层级**：严禁把网页变成只展示时间、Wi-Fi 开关的设备小组件堆砌，或为了凑齐组件而虚构内容。
2. **严禁大面积平涂无语义的渐变色彩**：所有色彩必须承担明确的遥测/状态功能。
3. **严禁使用软糯模糊重阴影**（如 iOS 毛玻璃大弥散阴影）。
4. **严禁将分段刻度条退化为普通实心条或白框**。
5. **严禁用 Doto 点阵字排版整段正文**（正文一律使用 Space Grotesk）。
6. **严禁在暗色背景上使用低对比度文字**。
7. **严禁省略 Google Fonts 导入**。
