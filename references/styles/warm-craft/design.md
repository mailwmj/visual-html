# Warm Craft (温润纸感手札风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Warm Craft 将书籍出版物的高级社论排版（Editorial Typography）与温润细腻的手作手账美学升华为界面语言。全站以带有棉纸温度的浅暖米白（`#F7F4EC` / `#FAF7F0`）为画布基底，在全局固定视口层（`body::before`）点缀 4 组柔和的有机暖色呼吸流光斑块（粉彩暖黄、抹茶绿、柔紫、暖橙），彻底告别生硬冷酷的纯白与冰冷灰。

界面的核心魅力在于**古典人文宋体、多彩粉彩便签与扇形对称微倾回弹动效（Editorial Serif, Pastel Stickers & Fan-Tilt Elastic Motion）**：

1. **全局柔和流体光晕背景（`body::before`，纸质手札灵魂）**：
   - 使用 4 组高透光晕（粉彩暖黄、抹茶绿、柔紫、暖橙），配合 `filter: blur(60px)`，使整个视口如同铺在洒满午后阳光的木质书桌上的棉纸。
2. **古典人文宋体大标题**：
   - 大标题采用高阶衬线宋体（`"Newsreader"`, `"Songti SC"`, `"Source Han Serif SC"`），字重 700~800，行高紧凑优雅，散发深厚智识感与出版物格调；正文切换为高可读性现代无衬线体。
3. **多彩粉彩便签（零粗黑边框，温润透亮）**：
   - 卡片采用高雅的粉彩色谱（明黄 `#FEDB71`、暖橙 `#FFA963`、抹茶绿 `#B7D97A`、柔紫 `#AAB7F2`、淡蓝 `#7CB6F8`），搭配纯白高光微边（`rgba(255, 255, 255, 0.8)`）与柔光投影，**绝对禁止使用粗黑边框与生硬阴影**。
4. **扇形镜像对称外展与弹性回弹手感**：
   - 多卡片排列采用双手自然摊开便签般的扇形对称倾角（左卡 `-2deg`、中卡 `0deg`、右卡 `+2deg`）；
   - 鼠标悬浮时**自动回正角度（`rotate(0deg)`）并以弹性曲线（`cubic-bezier(0.175, 0.885, 0.32, 1.275)`）轻盈跃升（`translateY(-10px) scale(1.03)`）**，赋予界面如同捏起桌面便签般的愉悦手感。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (Warm Paper) | `rgb(247, 244, 236)` | `#F7F4EC` | `--bg` | 全局浅暖米白画布底色 |
| Background (Warm Surface) | `rgb(250, 247, 240)` | `#FAF7F0` | `--bg-warm` | 页面局部微高光底色 |
| Background (Deep Paper) | `rgb(237, 231, 218)` | `#EDE7DA` | `--bg-deep` | 代码块/参数栏微深纸底色 |
| Surface (White Card) | `rgb(255, 255, 255)` | `#FFFFFF` | `--surface-card` | 纯白主卡片底色 |
| Surface (Paper Subtle) | `rgb(250, 248, 242)` | `#FAF8F2` | `--surface-card-subtle` | 问答提问底板、嵌套微卡片 |
| Text (Forest Charcoal Ink) | `rgb(30, 35, 27)` | `#1E231B` | `--text-primary` | 宋体大标题、主正文（高对比墨色） |
| Text (Olive Slate Gray) | `rgb(86, 94, 80)` | `#565E50` | `--text-secondary` | 导读段落、次级说明段落 |
| Text (Muted Sand) | `rgb(142, 150, 133)` | `#8E9685` | `--text-muted` | 注释、页脚、等宽元数据标签 |
| Border (Warm Subtle) | `rgba(50, 61, 36, 0.08)` | `rgba(50,61,36,.08)` | `--border` | 1px 柔和分割线、卡片微边框 |
| Border (Strong / Focus) | `rgba(50, 61, 36, 0.16)` | `rgba(50,61,36,.16)` | `--border-strong` | 高对比线、活跃外轮廓 |

### Pastel Sticker & Action Palette

| Channel | Role | Value | Hex | Text Color | Usage Boundary |
|---|---|---|---|---|---|
| **Deep Forest Olive** | 深橄榄绿 (Primary Action) | `rgb(50, 61, 36)` | `#323D24` | `#FFFFFF` | 主行动通道、核心状态标头 (占 3–5%) |
| **Pastel Yellow** | 明黄贴纸 (Sticky Card 1) | `rgb(254, 219, 113)` | `#FEDB71` | `#5A3E00` | 编号卡片 1、Info 便签、步骤序号 (占 3%) |
| **Pastel Orange** | 暖橙贴纸 (Sticky Card 2 / Focus)| `rgb(255, 169, 99)` | `#FFA963` | `#542200` | 推荐卡片高光、Warning 便签 (占 3–5%) |
| **Pastel Green** | 抹茶绿贴纸 (Sticky Card 3 / Success)| `rgb(183, 217, 122)`| `#B7D97A` | `#243D06` | 编号卡片 3、决策便签、Pros (占 3%) |
| **Pastel Purple** | 柔紫贴纸 (Subagent Note) | `rgb(170, 183, 242)` | `#AAB7F2` | `#1B2966` | 异步子代理便签、辅助标签 (占 2%) |
| **Pastel Coral** | 珊瑚粉便签 (Cons) | `rgb(252, 165, 152)` | `#FCA598` | `#631C12` | 缺点/约束/风险便签 (占 2%) |

### CSS Design Tokens

```css
:root {
  /* 背景层：暖纸底色与柔和环境色 */
  --bg: #F7F4EC;
  --bg-warm: #FAF7F0;
  --bg-deep: #EDE7DA;
  
  /* 表面层 (Surface) */
  --surface-card: #FFFFFF;
  --surface-card-subtle: #FAF8F2;
  --surface-overlay: rgba(255, 255, 255, 0.85);

  /* 文字层 (深墨绿炭黑 / 暖灰 / 沙岩色) */
  --text-primary: #1E231B;
  --text-secondary: #565E50;
  --text-muted: #8E9685;
  --text-inverse: #FFFFFF;

  /* 核心主行动色 (深橄榄森林绿) */
  --signal-primary: #323D24;
  --signal-primary-hover: #242E18;
  --signal-primary-light: #EBF0E4;

  /* 粉彩贴纸多色通道 */
  --pastel-yellow: #FEDB71;
  --pastel-yellow-text: #5A3E00;
  --pastel-orange: #FFA963;
  --pastel-orange-text: #542200;
  --pastel-green: #B7D97A;
  --pastel-green-text: #243D06;
  --pastel-purple: #AAB7F2;
  --pastel-purple-text: #1B2966;
  --pastel-blue: #7CB6F8;
  --pastel-blue-text: #0B3363;
  --pastel-coral: #FCA598;
  --pastel-coral-text: #631C12;

  /* 边框与阴影 (无粗黑边，温润透亮) */
  --border: rgba(50, 61, 36, 0.08);
  --border-strong: rgba(50, 61, 36, 0.16);
  --shadow-card: 0 6px 24px rgba(45, 40, 25, 0.05), 0 1px 3px rgba(45, 40, 25, 0.03);
  --shadow-card-hover: 0 16px 36px rgba(45, 40, 25, 0.10), 0 3px 8px rgba(45, 40, 25, 0.04);
  --shadow-sticker: 0 8px 24px rgba(50, 45, 30, 0.07), 0 2px 6px rgba(50, 45, 30, 0.03);

  /* 交互与缓动曲线 Tokens (手作弹性动效) */
  --ease-elastic: cubic-bezier(0.175, 0.885, 0.32, 1.275);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-hover: 0.35s;

  /* 尺寸与圆角 */
  --radius: 20px;
  --radius-sm: 12px;
  --radius-pill: 100px;
  --container: 1180px;

  /* 字体栈 (Editorial Serif + Clean Sans + Mono) */
  --font-serif: "Newsreader", "Playfair Display", "Songti SC", "STSong", "Source Han Serif SC", "Noto Serif SC", "SimSun", serif;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", "SFMono-Regular", Consolas, monospace;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

生成任何 Warm Craft 网页时，必须包含以下全局柔和流体光晕背景层，**严禁省略**：

```css
/* 全局固定流体光晕背景层 (4 组柔和呼吸流光) */
body::before {
  content: "";
  position: fixed;
  inset: -40px;
  z-index: -1;
  background: 
    radial-gradient(circle at 12% 12%, rgba(254, 219, 113, 0.28) 0%, transparent 45%),
    radial-gradient(circle at 88% 20%, rgba(183, 217, 122, 0.22) 0%, transparent 40%),
    radial-gradient(circle at 18% 80%, rgba(170, 183, 242, 0.20) 0%, transparent 45%),
    radial-gradient(circle at 82% 88%, rgba(255, 169, 99, 0.22) 0%, transparent 45%);
  background-color: var(--bg);
  filter: blur(60px);
  pointer-events: none;
}
```

---

## 4. Signature Component Patterns (核心特征组件规范)

### 1. Fan-Tilt Pastel Sticker Cards (扇形微倾粉彩便签卡片)

```html
<div class="cards-3">
  <!-- 卡片 1: 粉彩明黄，微倾 -2deg -->
  <div class="num-card" style="background: var(--pastel-yellow); transform: rotate(-2deg) translateY(2px);">
    <div class="num" style="color: var(--pastel-yellow-text);">01</div>
    <h3 style="color: var(--pastel-yellow-text);">知识流式分块沉淀</h3>
    <p style="color: rgba(90, 62, 0, 0.88);">支持自适应分块与层级提炼，将长篇调研转化为清晰易读的结构化手札。</p>
    <div class="tag" style="color: var(--pastel-yellow-text);">BASE NOTE</div>
  </div>

  <!-- 卡片 2: 粉彩暖橙推荐态，居中 0deg，带高能光晕 -->
  <div class="num-card selected" style="background: var(--pastel-orange); transform: rotate(0deg) translateY(-6px) scale(1.01);">
    <div class="num" style="color: var(--pastel-orange-text);">02</div>
    <h3 style="color: var(--pastel-orange-text);">社论级排版引擎</h3>
    <p style="color: rgba(84, 34, 0, 0.88);">结合人文宋体与双手自然摊开的扇形微倾角，悬浮自动回正跃起。</p>
    <div class="tag" style="color: var(--pastel-orange-text); background: #FFFFFF;">RECOMMENDED</div>
  </div>

  <!-- 卡片 3: 粉彩抹茶绿，微倾 +2deg -->
  <div class="num-card" style="background: var(--pastel-green); transform: rotate(2deg) translateY(2px);">
    <div class="num" style="color: var(--pastel-green-text);">03</div>
    <h3 style="color: var(--pastel-green-text);">双模态离线交付</h3>
    <p style="color: rgba(36, 61, 6, 0.88);">单文件自包含 HTML，支持现代浏览器即开即看，告别繁琐部署。</p>
    <div class="tag" style="color: var(--pastel-green-text);">OFFLINE READY</div>
  </div>
</div>
```

### 2. Admonitions with Sticky Paper Tones (手作便签提示框)

```html
<div class="admonition info">
  <div class="admonition-title">核心结论 (INFO)</div>
  <p>这是 AI 提取的关键结论便签，采用暖黄便签纸底色与加粗左便签条。</p>
</div>
```

### 3. Timeline with Pill Capsule Markers (手作胶囊时间轴)

```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-marker">2024</div>
    <div class="timeline-content">
      <h3>立项与人文手札体系探索</h3>
      <p>确定以纸质温润感与社论宋体为核心，完成首版手札系统构建。</p>
    </div>
  </div>
</div>
```

### 4. Editorial Headings with Fluorescent Marker Highlights (人文宋体标题与荧光马克笔高亮)

在 Warm Craft 风格中，**文章主标题（Hero Title / 封面大标题）必须包含荧光马克笔高亮（Marker Highlight）**，确立出版手札的核心视觉锚点；而**其他二级标题、小标题与正文段落保持克制，仅根据场景与关键结论按需添加**，严禁在所有标题上泛滥堆砌：

```html
<!-- 1. 文章主标题 (Hero Title)：必须包含 1~2 处核心关键词高亮 -->
<h1 class="hero">温润纸感手札美学。<br>全组件<span class="marker-highlight">排版规范</span>预览集。</h1>

<!-- 2. 二级标题 (Section Title)：默认保持纯净宋体，仅在关键结论/核心论点处按需选用 -->
<h2 class="section-title">核心论述与参数栏</h2>
<h2 class="section-title">手作便签卡片与提示框</h2>
<!-- 遇到强烈结论或转折性命题时可适度点缀: -->
<!-- <h2 class="section-title">三项核心支柱，构建<span class="marker-highlight-orange">复利体系</span></h2> -->

<!-- 3. 正文段落 (Rich Text)：在重点段落中以 <strong> 局部高亮关键短语 -->
<p>这是标准的正文段落。支持 <strong class="marker-highlight">荧光马克笔高亮</strong> 与 <code>内联代码</code> 等元素。</p>
```

```css
/* 荧光马克笔高亮笔触 Tokens */
.marker-highlight {
  background: linear-gradient(180deg, transparent 52%, rgba(254, 219, 113, 0.75) 52%, rgba(254, 219, 113, 0.75) 94%, transparent 94%);
  padding: 0 4px;
  border-radius: 3px;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  display: inline;
}
.marker-highlight-orange {
  background: linear-gradient(180deg, transparent 52%, rgba(255, 169, 99, 0.75) 52%, rgba(255, 169, 99, 0.75) 94%, transparent 94%);
  padding: 0 4px;
  border-radius: 3px;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  display: inline;
}
.marker-highlight-green {
  background: linear-gradient(180deg, transparent 52%, rgba(183, 217, 122, 0.75) 52%, rgba(183, 217, 122, 0.75) 94%, transparent 94%);
  padding: 0 4px;
  border-radius: 3px;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  display: inline;
}
.marker-highlight-purple {
  background: linear-gradient(180deg, transparent 52%, rgba(170, 183, 242, 0.75) 52%, rgba(170, 183, 242, 0.75) 94%, transparent 94%);
  padding: 0 4px;
  border-radius: 3px;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  display: inline;
}
.marker-highlight-coral {
  background: linear-gradient(180deg, transparent 52%, rgba(252, 165, 152, 0.75) 52%, rgba(252, 165, 152, 0.75) 94%, transparent 94%);
  padding: 0 4px;
  border-radius: 3px;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  display: inline;
}
```

### 5. High-Readability Code Block & Terminal (高可读性深墨绿深炭代码窗口)

代码块采用高对比度深墨绿深炭色底（`#1F241C`），与暖米白页面形成明暗韵律反差，并配置粉彩三色 macOS 控制点与高饱和暖色语法高亮：

```html
<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <span class="code-lang">PYTHON / KNOWLEDGE ENGINE</span>
    <button class="code-copy-btn" onclick="navigator.clipboard.writeText(this.closest('.code-block').querySelector('code').innerText); this.innerText='COPIED!'; setTimeout(()=>this.innerText='COPY', 2000)">COPY</button>
  </div>
  <pre><code><span class="token-comment"># 初始化 Warm Craft 知识流式编排器</span>
<span class="token-keyword">from</span> warm_craft <span class="token-keyword">import</span> EditorialStream, PaperBinder

<span class="token-keyword">def</span> <span class="token-function">bind_knowledge_document</span>(doc_id: <span class="token-string">str</span>) -> PaperBinder:
    binder = PaperBinder(paper_tone=<span class="token-string">"#F7F4EC"</span>, font_serif=<span class="token-string">"Newsreader"</span>)
    <span class="token-keyword">return</span> binder.render_rich_editorial(doc_id)</code></pre>
</div>
```

```css
/* 代码块容器与头部 */
.code-block {
  background: #1F241C;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius);
  margin: 28px 0;
  overflow: hidden;
  box-shadow: 0 10px 32px rgba(30, 35, 27, 0.14), 0 2px 6px rgba(30, 35, 27, 0.06);
}
.code-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  background: #181C15;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}
.code-dots { display: flex; gap: 7px; }
.code-dots span { width: 9px; height: 9px; border-radius: 50%; }
.code-dots span:nth-child(1) { background: #FCA598; }
.code-dots span:nth-child(2) { background: #FEDB71; }
.code-dots span:nth-child(3) { background: #B7D97A; }
.code-lang {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #E2DEC9;
  text-transform: uppercase;
}
.code-copy-btn {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  padding: 4px 12px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-sm);
  color: #E2DEC9;
  cursor: pointer;
  transition: all 0.2s ease;
}
.code-copy-btn:hover {
  background: #F7F4EC;
  color: #1E231B;
  border-color: #F7F4EC;
}

/* 预格式化区域与语法高亮（高对比度 + 严格样式隔离） */
.code-block pre, .rich-text > pre {
  margin: 0;
  padding: 22px 24px;
  background: #1F241C;
  overflow-x: auto;
  font-family: var(--font-mono);
  font-size: 13.5px;
  line-height: 1.7;
  color: #F7F4EC;
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 255, 255, 0.2) transparent;
}
/* 必须清除 pre 内 code 的内联浅色背景，防止背景破碎 */
.code-block pre code,
.rich-text pre code,
pre code {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  border-radius: 0 !important;
  color: inherit !important;
  font-size: inherit;
  font-family: inherit;
  box-shadow: none !important;
  display: block;
}
.token-comment { color: #9AA593; font-style: italic; }
.token-keyword { color: #FEDB71; font-weight: 700; }
.token-string { color: #FFA963; }
.token-function { color: #B7D97A; }
.token-number { color: #7CB6F8; }
.token-operator { color: #E2DEC9; }
.token-variable, .token-property { color: #AAB7F2; }
.token-type, .token-class { color: #FCA598; }

/* 内联代码：严格限定在非 pre 作用域 */
.rich-text :not(pre) > code,
.rich-text p > code,
.rich-text li > code,
.rich-text blockquote > code,
.rich-text td > code {
  font-family: var(--font-mono);
  font-size: 0.88em;
  background: var(--bg-deep);
  color: var(--signal-primary);
  padding: 2px 7px;
  border-radius: 6px;
  border: 1px solid var(--border);
  font-weight: 600;
}
```

---

## 5. Do's and Don'ts

### Do's (8 项金律)

1. **Do 在 `body::before` 中使用 4 组柔和呼吸流光（暖黄、抹茶绿、柔紫、暖橙）搭配 `blur(60px)`** — 奠定棉纸在阳光下的温润空间底色。
2. **Do 在 3 张核心编号卡片上应用专属粉彩底色（明黄、暖橙、抹茶绿）** — 传递极具活力的手作手账感。
3. **Do 对卡片应用双手自然摊开般的扇形微倾角（-2° / 0° / +2°）** — 鼠标悬浮时必须配置回正角度（`rotate(0deg)`）与弹性跃升动效。
4. **Do 大标题使用高阶人文宋体（`"Newsreader"`, `"Songti SC"`，字重 700~800）** — 呈现出版级社论格调。
5. **Do 在文章主标题（Hero Title / 封面大标题）中必须使用荧光马克笔高亮核心关键词，其他二级标题与正文保持克制按需选用** — 确立全篇视觉锚点并增强手作批注亲切感，杜绝泛滥堆砌。
6. **Do 使用深橄榄绿（`#323D24`）作为核心主行动与状态标头颜色** — 保持沉稳雅致的书卷气息。
7. **Do 保持阴影温润透亮（`rgba(45, 40, 25, 0.05)`）** — 杜绝死板黑影。
8. **Do 确保代码块采用深墨绿深炭底色（`#1F241C`）与高对比度语法高亮 Token，并严格隔离内联代码与多行代码块样式（避免 `pre code` 继承内联标签底色导致背景破碎）**。

### Don'ts (8 项红线)

1. **Don't 将粉彩便签卡片漂白为单调的普通纯白卡片** — 必须保留明黄/暖橙/抹茶绿的个性化粉彩底色。
2. **Don't 丢失卡片的扇形微倾角与悬浮回正跃升手感** — 缺少微倾角会导致手札风格严重退化。
3. **Don't 使用生硬冷酷的纯黑或粗黑边框** — 边框必须是温润透明的浅色线（`rgba(50, 61, 36, 0.08)`）。
4. **Don't 将背景流光删除并替换为冷酷点阵** — 必须保留 4 组流光呼吸层。
5. **Don't 在大标题中使用生硬冰冷的黑体** — 必须保持人文宋体（Serif）的大标题。
6. **Don't 使用生硬直角（0px）** — 卡片保持 20px 圆角，标签使用胶囊圆角。
7. **Don't 使用高饱和荧光刺眼色彩** — 卡片色彩必须是温和低刺激的粉彩色系（Pastel Tones）。
8. **Don't 让 `.rich-text code` 浅色内联样式污染多行 `<pre><code>` 代码块** — 严禁出现灰白底色碎块包裹深色代码块中语法文字的低对比度错误。
