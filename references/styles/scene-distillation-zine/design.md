# Scene Distillation Zine (手作刊物风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Scene Distillation Zine 将摄影影像与长篇文献**蒸馏为极具文学质感与独立手作刊物美学（Indie Zine & Risograph Aesthetics）的版面系统**。全站以带有棉浆触觉温度的浅暖米白（`#F5EFEB` / `#FAF6EE`）为纸张基底，配合微弱的孔版半调网点微底纹与纸浆纤维噪点，彻底脱离商业广告的塑料白与死板灰。

界面的核心魅力在于**孔版钴青单色油墨（Risograph Cobalt Blue）、撕纸纤维毛边（Torn-Fiber Deckle Edge）、打字机题记与古法矿物朱砂印泥点睛（Cinnabar Seal Accent）**：

1. **全局棉纸纹理与孔版微底纹（Layer 0: Ambient Paper Canvas）**：
   - 采用触觉棉纸暖底（`#F5EFEB`），辅以 `radial-gradient` 极淡半调网点与 SVG 纸浆噪点滤镜，营造平整扫描、手工印制的真实纸质感。
2. **孔版钴青蓝主油墨体系（Risograph Cobalt & Indigo Ink）**：
   - 线条、图解、重点标题与主标头采用经典孔版印刷钴青蓝（`#1E4870`），正文采用熟褐炭黑（`#2B2825`），次级文字为铅笔灰（`#625D56`）。
3. **沉稳矿物朱砂印泥点睛（Mineral Cinnabar Seal Accent）**：
   - 摒弃生硬刺眼的工业亮橘，采用带陶土矿物感与古籍印泥温度的**古法朱砂陶土红（`#A84335`）**，仅在关键印章徽记、章节编号、数据重点处克制出现（占全图 0.8%–2%）。
4. **四大边缘过渡语法（Transition Edge Director）**：
   - 风格内建 4 种具象过渡：**撕纸毛边（Torn-fiber deckle）**、**层叠灰阶（Layered Grayscale）**、**网点消解（Stippled Dissolution）** 与 **自然孤立轮廓（Natural Isolated Contour）**。
5. **打字机与人文衬线排版（Typewriter & Humanist Serif）**：
   - 大标题采用高阶衬线体（`"Newsreader"`, `"Noto Serif SC"`, `"Songti SC"`）；刊头、编目元数据、代码与图章采用打字机等宽体（`"Courier Prime"`, `"Courier New"`）。
6. **大面积静谧留白（68%–85% Negative Space）**：
   - 版面以瑞士杂志与独立手刊的不对称网格排布，保持大比例纸面呼吸空间，提供引人深思的阅读节奏与“阐释缺口”。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (Cotton Paper) | `rgb(245, 239, 235)` | `#F5EFEB` | `--paper-base` | 全局棉纸画布底色 |
| Background (Warm Surface) | `rgb(250, 246, 238)` | `#FAF6EE` | `--paper-warm` | 拼贴画板、Hero 与卡片微高光底色 |
| Background (Deep Paper) | `rgb(237, 229, 216)` | `#EDE5D8` | `--paper-dark` | 代码块/引言框微深纸底色 |
| Surface (Paper Card) | `rgb(252, 250, 246)` | `#FCFAF6` | `--paper-card` | 纸感主卡片与模块底色 |
| Primary Ink (Riso Cobalt Blue) | `rgb(30, 72, 112)` | `#1E4870` | `--ink-blue` | 核心标题、重点线条、图表与图章 |
| Ink Tint (Riso Blue Tint) | `rgb(228, 236, 244)` | `#E4ECF4` | `--ink-blue-tint` | 半调浸润背景、微卡片浅底色 |
| Ink Muted (Muted Cobalt) | `rgb(72, 110, 145)` | `#486E91` | `--ink-blue-muted` | 标头前缀、次级图表线条 |
| Text (Graphite Charcoal Ink) | `rgb(43, 40, 37)` | `#2B2825` | `--ink-charcoal` | 正文主墨色（高可读性熟褐炭黑） |
| Text (Pencil Slate Gray) | `rgb(98, 93, 86)` | `#625D56` | `--ink-gray` | 导读段落、次要说明 |
| Text (Muted Sand) | `rgb(142, 136, 126)` | `#8E887E` | `--ink-muted` | 注释、页脚、打字机元数据 |
| Accent (Cinnabar Seal Red) | `rgb(168, 67, 53)` | `#A84335` | `--accent-seal` | 矿物朱砂印章、高亮标头、警示 (0.8–2%) |
| Accent Bg (Seal Tint) | `rgba(168, 67, 53, 0.08)` | `rgba(168,67,53,0.08)` | `--accent-seal-bg` | 朱砂印章浅底色与警示底板 |
| Border (Ink Stroke) | `rgba(30, 72, 112, 0.20)` | `rgba(30,72,112,0.20)` | `--border-ink` | 钴蓝油墨刻线、虚线框 |
| Border (Hairline) | `rgba(43, 40, 37, 0.12)` | `rgba(43,40,37,0.12)` | `--border-hairline` | 极细纸张接触线 |

### CSS Design Tokens

```css
:root {
  /* 纸张与材质画布色系 */
  --paper-base: #F5EFEB;
  --paper-warm: #FAF6EE;
  --paper-card: #FCFAF6;
  --paper-dark: #EDE5D8;
  --paper-shadow: rgba(45, 38, 30, 0.08);

  /* 油墨体系 (Risograph & Charcoal Inks) */
  --ink-blue: #1E4870;
  --ink-blue-tint: #E4ECF4;
  --ink-blue-muted: #486E91;
  --ink-charcoal: #2B2825;
  --ink-gray: #625D56;
  --ink-muted: #8E887E;

  /* 专属矿物点睛色 (朱砂印泥色) */
  --accent-seal: #A84335;
  --accent-seal-bg: rgba(168, 67, 53, 0.08);
  --accent-seal-border: rgba(168, 67, 53, 0.35);

  /* 边框与刻线 */
  --border-ink: rgba(30, 72, 112, 0.20);
  --border-hairline: rgba(43, 40, 37, 0.12);
  --border-dashed: 1px dashed rgba(30, 72, 112, 0.32);

  /* 字体栈 */
  --font-display: "Newsreader", "Noto Serif SC", "Songti SC", "Source Han Serif SC", Georgia, serif;
  --font-mono: "Courier Prime", "Courier New", "SFMono-Regular", Consolas, monospace;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;

  /* 阴影：扁平压印与微接触阴影，绝不用 3D 浮夸阴影 */
  --shadow-paper: 0 2px 0 rgba(43, 40, 37, 0.04), 0 6px 20px rgba(43, 40, 37, 0.06);
  --shadow-deckle: 0 4px 14px rgba(35, 30, 25, 0.08);

  /* 尺寸与容器 */
  --container: 1080px;
  --radius: 0px; /* 纸质刊物以平直裁切与有机撕纸为主 */
}
```

---

## 3. Style-Owned Layout Contract

### 空间形态原型：直铺瑞士杂志流 (Direct Swiss Editorial Flow)
Scene Distillation Zine 属于 **直铺沉浸型与瑞士杂志版式 (Direct Immersive / Swiss Editorial Flow)**：长文直接在全景棉纸（Layer 0）上流式展开，版面通过不对称双栏、撕纸拼贴画板与打字机网格构建节奏。

### Web Adaptation (长文网页契约)
- 全局居中版心宽度最大 `1080px`，两侧保留至少 `28px`（移动端 `18px`）呼吸留白。
- 顶部固定刊物编目刊头（Masthead），包含期号、分类与归档编号。
- 移动端自适应为单栏折叠排布，撕纸毛边效果平滑降级为虚线微裁切。

### PPT Adaptation (16:9 演示文稿契约)
- 固定 16:9 舞台（`1280x720`），内边距 `54px 72px 48px`。
- 单页聚焦一个核心论点（封面、章节三柱、量化数据、对比表格）。
- 支持全键盘翻页（`←` / `→` / `Space`）、全屏与打印样式。

---

## 4. Typography Scale & Rules

| Element | Tag / Class | Font Family | Size | Weight | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| **Masthead Meta** | `.zine-meta-left` | `--font-mono` | `11px` | 700 | 1.5 | `0.12em` | 刊头期号与归档标签 |
| **Hero Title** | `h1.hero-title` | `--font-display` | `42px` | 600 | 1.2 | `-0.02em` | 首屏诗意主标题 |
| **Section Title** | `h2.section-title` | `--font-display` | `26px` | 600 | 1.3 | `-0.01em` | 一级章节标题 |
| **Subsection / Card**| `h3.card-title` | `--font-display` | `20px` | 600 | 1.35 | `0` | 卡片与子模块标题 |
| **Body Text** | `p, .rich-text` | `--font-sans` | `15px` | 400 | 1.75 | `0` | 深度阅读正文 |
| **Typewriter Notes** | `code, .card-tag` | `--font-mono` | `11px` | 400 / 700 | 1.5 | `0.08em` | 打字机标注与参数 |
| **Stat Metric** | `.stat-num` | `--font-mono` | `38px` | 700 | 1.0 | `-0.02em` | 关键量化数据指标 |

---

## 5. Signature Component Patterns

### 1. Hero Torn-Paper Collage Board (撕纸拼贴画板)
```html
<section class="hero-zine-board">
  <div class="hero-content">
    <div class="hero-eyebrow">EDITORIAL PROPOSITION · 01 / DISTILL</div>
    <h1 class="hero-title">
      where stone meets sky.
      <span class="italic-sub">当坚硬的石质轮廓，在孔版墨色中融入苍穹。</span>
    </h1>
    <p class="hero-lead">将真实世界的繁复影像，蒸馏为诗意的纸感图画。</p>
    <div class="hero-stamp-row">
      <div class="zine-stamp">★ 独立手作刊物审美</div>
      <div class="stamp-circle">v1.5</div>
    </div>
  </div>
  <div class="hero-visual-panel">
    <div class="halftone-screen"></div>
    <div class="engraving-art">
      <div class="art-header"><span>PLATE NO. 04</span><span>RISO INK</span></div>
      <div class="art-illustration-placeholder">
        <div class="distill-cross">✚</div>
        <div class="distill-text">SEMANTIC NUCLEUS</div>
      </div>
    </div>
  </div>
</section>
```

### 2. Paper Spec Card with Index & Tag (纸感规范卡片)
```html
<div class="zine-card featured">
  <div>
    <div class="card-index">
      <span style="color: var(--accent-seal); font-weight: 700;">RULE / 02 ★</span>
      <span>[ MATERIAL ]</span>
    </div>
    <h3 class="card-title">孔版孔印与撕纸边缘</h3>
    <p class="card-desc">采用 Risograph 钴青蓝油墨与温润棉纸底色，结合物理撕纸毛边。</p>
  </div>
  <span class="card-tag">TACTILE RISOGRAPH</span>
</div>
```

### 3. Typewriter Poetry Quote Box (打字机诗意引言框)
```html
<div class="poetry-box">
  <div class="poetry-line">“Treat the photo as semantic evidence and creative stimulus.”</div>
  <div class="poetry-source">— Zeejay0 · Scene Distillation Manifesto</div>
</div>
```

### 4. Mineral Cinnabar Admonition (朱砂印泥提示框)
```html
<div class="admonition-zine warning">
  <div class="admonition-title"><span>⚠</span> 关键执行禁令 (Hard Avoids)</div>
  <div class="admonition-body">绝对禁止在最终画面中保留任何真实照片像素、照片裁切窗口或写实渐变渲染。</div>
</div>
```

---

## 6. Mermaid Theme Configuration

在线增强时，在 `</body>` 前注入以下匹配手作刊物风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```javascript
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  themeVariables: {
    darkMode: false,
    background: '#FAF6EE',
    primaryColor: '#E4ECF4',
    primaryTextColor: '#2B2825',
    primaryBorderColor: '#1E4870',
    lineColor: '#1E4870',
    secondaryColor: '#FCFAF6',
    tertiaryColor: '#EDE5D8',
    fontFamily: '"Courier Prime", "Newsreader", "Noto Serif SC", Georgia, monospace'
  }
});
```

---

## 7. Do's and Don'ts

### 7 项核心金律 (Do's)
1. **Do 保持棉纸暖白底色（`#F5EFEB`）与钴青单色油墨（`#1E4870`）的核心基调** — 奠定孔版印刷与手作出版物的温润质感。
2. **Do 严格使用古法朱砂陶土红（`#A84335`）作为克制点睛色** — 占全图 0.8%–2%，担当视觉锚点与印章印泥。
3. **Do 大标题使用人文衬线体（`"Newsreader"`, `"Noto Serif SC"`），元数据与代码使用打字机等宽体（`"Courier Prime"`）** — 保持清晰的社论字阶层级。
4. **Do 在主要构图与卡片中应用撕纸毛边（Torn-fiber deckle edge）或半调网点** — 传递扁平手工扫描质感。
5. **Do 保持 68%–85% 的静谧呼吸留白** — 杜绝信息拥挤，赋予观者凝视与思考空间。
6. **Do 代码块采用深墨炭色（`#242220`）并配置打字机等宽字体与朱砂红状态指示点**。
7. **Do 必须实现完整 18 项语义组件与 16:9 PPT 舞台翻页契约**。

### 7 项严禁红线 (Don'ts)
1. **Don't 使用生硬刺眼的工业亮橘或高饱和荧光色** — 点睛色必须保持矿物陶土朱砂的温润沉稳。
2. **Don't 将纸感卡片漂白为冷酷千篇一律的纯白卡片（`#FFFFFF`）** — 必须使用暖纸底色与孔版微底纹。
3. **Don't 使用厚重的 3D 浮夸拟真阴影** — 阴影仅允许扁平压印与极微纸张接触阴影（`rgba(45, 38, 30, 0.08)`）。
4. **Don't 在圆角卡片顶部叠加热键矩形直条（No unclipped top accent bars）** — 保持卡片纯粹一体。
5. **Don't 丢失打字机刊头（Masthead）与编目元数据** — 必须维持独立手作刊物的刊头标识。
6. **Don't 引入真实照片图层、照片截图或写实渐变渲染** — 最终输出必须由纯粹手绘、纸纹与排版构成。
7. **Don't 将 Web 样式机械缩放为 PPT** — PPT 需按固定 16:9 舞台与单页单焦点独立实现。
