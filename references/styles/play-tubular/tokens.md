# Play Tubular / 玩味工程彩管风 — Design Tokens & Style Specification

> **Style ID**: `play-tubular`  
> **显示名称**：玩味工程彩管风 / 活力半调彩管 (Play Tubular / Play Engineering)  
> **核心气质**：采用温润米白点阵画布（Warm Cream & Halftone Canvas）、粗壮鲜活的 3D 渐变立体彩管/丝带环绕（Vibrant 3D Gradient Tubes & Ribbon Loops）、在球头末端与弯折高光处融入标志性的**半调网点 (Halftone Dot Matrix / Raster Shading)** 光影质感，搭配高对比度现代工程粗黑体（Neo-Grotesque Sans）、纯白大圆角悬浮卡片与轻快弹性回弹动效（Spring Dynamic Bounce）。将工程架构的严谨理性与创意探索的玩味活力完美融合，极其适用于 AI / LLM 创新产品、工程架构展示、创意技术落地页、前沿算法白皮书与活力开发者大会。

---

## 1. Design DNA & 核心原则

1. **温润米白画布与全局 3D 渐变彩管背景 (Warm Cream Canvas & Ambient 3D Tubular Loops)**：
   - 全局背景为舒适耐看的浅暖米白（`#FAF8F3` / `#F5F2EA`），底层铺设 24px 微型点阵（`radial-gradient(#E2DDD3 1px, transparent 1px)`）。
   - **核心视觉背景层 (`.ambient-tubes-bg` / `.slide-bg-tubes`)**：页面与幻灯片背景必须内置粗壮鲜活的 **3D 渐变立体彩管/丝带环绕回路 (3D Tubular Loops & Noodle Curves)**，跨越右上、左下等区域自然穿插，赋予整个画面如同参考图（Play Engineering ✕ LLM）般极具冲击力的高阶视觉张力。
2. **高能多色能量渐变系统 (Vibrant Multi-Stop Gradients)**：
   - 色彩采用多停点高饱和能量渐变（电光蓝 `#0052FF` ➜ 洋红 `#FF0080`、柑橘烈橙 `#FF4500` ➜ 金黄 `#FFD600`、翠绿 `#00C853` ➜ 霓虹青 `#00E5FF`、珊瑚粉 `#FF6B6B` ➜ 薰衣草紫 `#C77DFF`）。
3. **标志性半调网点光影质感 (Halftone Dot Matrix / Raster Shading)**：
   - 这是该风格最具辨识度的灵魂印记：在背景彩管的圆形球头末端、弯折高光处、卡片角标、时间轴徽标及状态胶囊中，深度融入复古未来感十足的 **Halftone 半调网点渐变 (点阵球头与光影)**。
   - 通过 SVG `<pattern>` 与径向网点渲染，使 3D 渐变具备印刷版画与数字波普交织的高级质感。
4. **工程严谨与玩味活力的字阶排版 (Playful Yet Precise Neo-Grotesque Typography)**：
   - **大标题 (Hero & Section Titles)**：采用粗黑体（`"Plus Jakarta Sans"`, `"Inter"`, `"PingFang SC"`, `"Microsoft YaHei"`, `"微软雅黑"`），字重 800–900，紧凑负字距（`-0.03em`），采用高对比度深黑墨色（`#111111`）。支持使用工程交叉乘号 `✕` 与双斜杠 `//` 增强理工美感。
   - **参数、序号与元数据**：采用精密等宽字体（`"JetBrains Mono"`, `"Fira Code"`），全大写、带高光胶囊底衬。
5. **一体化通体正文承托画布 (Unified Continuous Reading Board - 拒绝切碎分块)**：
   - 为防止背景中粗壮绚丽的 3D 彩管抢占正文注意力，同时**拒绝将页面割裂切碎成一个个孤立浮动的分散小块**，页面主体采用**单一连贯的一体化通体承托画板（`<main class="main-sheet">`，`rgba(255, 255, 255, 0.94)` 搭配 `backdrop-filter: blur(24px)` 与 36px 大圆角）**。
   - 所有章节（Hero、长文、卡片、时间轴、步骤、问答与页脚）在整块连贯画板中自上而下自然流淌，各 Section 之间仅通过 1px 优雅虚线或呼吸感留白过渡，形成“外圈 3D 彩管环绕灵动、内侧通体画板沉浸阅读”的高阶展厅画册质感。
6. **纯白大圆角卡片与弹性动效 (Crisp White Floating Cards & Spring Dynamics)**：
   - 卡片采用纯白底色（`#FFFFFF`）配合 24px 大圆角与柔和暖调外边框（`rgba(0, 0, 0, 0.06)`）。
   - 交互具备弹簧回弹手感（`cubic-bezier(0.34, 1.56, 0.64, 1)`），悬浮时轻盈上浮并激发多色渐变光晕与半调微光。

---

## 2. CSS Design Tokens

```css
:root {
  /* 背景层：暖米白画布与点阵背景 */
  --bg: #FAF8F3;
  --bg-subtle: #F4F1EA;
  --bg-plate: rgba(255, 255, 255, 0.92);  /* 正文承托底板 */
  --bg-card: #FFFFFF;
  --bg-card-subtle: #FAF9F6;

  /* 文字墨色层 (高对比深黑 / 次级炭灰 / 辅助暖灰) */
  --text-primary: #111111;       /* 主标题与核心字 */
  --text-secondary: #4A4A48;     /* 正文段落与导读 */
  --text-muted: #7E7E7A;         /* 占位符、注释与 Mono 标签 */
  --text-inverse: #FFFFFF;       /* 深色按钮与反白文字 */

  /* 核心行动与高能 5-6 停点渐变通道 (Vibrant Multi-Stop Master Gradients) */
  --grad-electric-flow: linear-gradient(135deg, #0038FF 0%, #5500FF 22%, #D000FF 48%, #FF0066 72%, #FF5500 88%, #FFD000 100%);
  --grad-sunset-burst: linear-gradient(135deg, #FF1A00 0%, #FF7300 28%, #FFB800 55%, #FFE600 82%, #76FF03 100%);
  --grad-aurora-cyan: linear-gradient(135deg, #00FF88 0%, #00E5FF 35%, #0055FF 70%, #8000FF 100%);
  --grad-cyber-berry: linear-gradient(135deg, #7B00FF 0%, #FF0077 32%, #FF4800 68%, #FFCC00 100%);
  --grad-blue-magenta: linear-gradient(135deg, #0052FF 0%, #7928CA 50%, #FF0080 100%);
  --grad-orange-gold: linear-gradient(135deg, #FF4500 0%, #FF8A00 50%, #FFD600 100%);
  --grad-emerald-cyan: linear-gradient(135deg, #00C853 0%, #00E5FF 100%);

  /* 单一纯色通道 (Solid Accents) */
  --accent-blue: #0052FF;
  --accent-orange: #FF5500;
  --accent-yellow: #FFD600;
  --accent-green: #00C853;
  --accent-magenta: #FF0080;
  --accent-purple: #7928CA;

  /* 半调网点通道 (Halftone Dot Matrix Tokens) */
  --halftone-dot-color: rgba(17, 17, 17, 0.18);
  --halftone-accent-blue: rgba(0, 82, 255, 0.25);
  --halftone-accent-yellow: rgba(255, 214, 0, 0.35);

  /* 边框与微光投影 (Refined Borders & Multi-Glow Shadows) */
  --border: rgba(17, 17, 17, 0.08);
  --border-strong: rgba(17, 17, 17, 0.16);
  --border-active: #0052FF;
  
  --shadow-card: 0 8px 24px rgba(17, 17, 17, 0.04), 0 1px 3px rgba(17, 17, 17, 0.02);
  --shadow-card-hover: 0 16px 36px rgba(0, 82, 255, 0.12), 0 4px 12px rgba(255, 69, 0, 0.08);
  --shadow-pop: 0 20px 48px rgba(0, 82, 255, 0.18), 0 6px 16px rgba(255, 0, 128, 0.10);

  /* 交互曲线与动效 (Spring Bounce Motion) */
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 0.25s;
  --duration-normal: 0.4s;

  /* 尺寸与圆角规范 */
  --radius: 24px;
  --radius-sm: 14px;
  --radius-pill: 999px;
  --container: 1180px;

  /* 字体栈 (Modern Geometric / Neo-Grotesque + Precision Mono) */
  --font-display: "Plus Jakarta Sans", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", "SFMono-Regular", Consolas, monospace;
}
```

---

## 3. 交互手感规范 (Motion & Micro-interactions)

| 组件 / 状态 | 默认静止态 (Rest State) | 悬浮微交互态 (`:hover`) | 交互手感设计意图 |
|---|---|---|---|
| **常规卡片 (`.num-card`, `.feat-card`)** | 纯白底座，1.5px 浅暖灰边框，44px 悬浮药丸彩条与大号能量渐变序号 | 弹性上浮 `translateY(-6px) scale(1.015)`，激发双色多巴胺渐变发光投影 | 传递出充满弹性与活力的现代软件界面交互感 |
| **推荐卡片 (`.num-card.selected`)** | 专属电光蓝高亮微边，高光药丸胶囊 | 进一步弹性跃升 `translateY(-10px) scale(1.03)`，彩管高光光斑展开，层级升至顶层 | 确保关键方案与推荐项绝对聚焦 |
| **核心数据卡片 (`.stat-card`)** | 微透彩光底衬，全环绕同色精致边框，大号纯黑数字与渐变单位 | 平滑上浮 `translateY(-4px)`，激发同色系轻柔彩光发光投影 | 兼顾工程严谨与数字趣味 |
| **流程步骤 (`.step`)** | 渐变圆角数字徽标，整齐纵向排列 | 向右轻弹 `translateX(8px)`，序号徽标微旋转缩放 | 引导视线顺畅流动 |
| **胶囊标签与按钮 (`.tag`, `button`)** | 彩管渐变圆角药丸底衬 | 弹性缩放 `scale(1.06)`，伴随半调网点微动态闪烁 | 增强点击欲与探索乐趣 |

---

## 4. 16 项核心组件视觉契约 (Component Visual Contracts)

依据全局规范 `shared-components.md`，以下 16 个标准组件在 `play-tubular` 风格下的具体呈现规则：

1. **Section Eyebrow (区块索引标头)**:
   - 采用精致的药丸状白底胶囊外壳，内置渐变色圆形半调点阵图标（`.diamond`），文字为 Mono 大写等宽，右侧延伸出带有双色渐变（电光蓝到金黄）的 2px 细线。
2. **Typography Scale (基础文本层级)**:
   - `h1.hero`：采用 `--font-display` 粗黑体，字号 44–76px，字重 900，行高 1.08，紧凑负字距，支持以渐变色高亮重点词；副标题以工程乘号 `✕` 优雅连接。
   - `h2.section-title`：字号 32–48px，字重 800，紧随 Eyebrow 下方。
   - `.lead`：字号 18–22px，颜色为 `--text-secondary`，行高 1.65。
3. **Technical Spec Row (规格参数栏)**:
   - 纯白大圆角卡片底座，内部以纵向 1px 细线分隔，数值 `.val` 采用超粗现代字体配合渐变色强调，单位 `.unit` 采用大写 Mono 字体并带浅底半调胶囊徽章。
4. **Number Cards (编号卡片列 - 核心彩管微模块)**:
   - 3 列纯白大圆角卡片（24px），卡片顶部内置一条 44px 独立悬浮药丸彩条（橙红、蓝紫、翠绿依次分色）。
   - 编号 `.num` 采用大号粗体 Mono（32px）配合专属能量渐变文字渲染；选中态（`.selected`）具备彩光多层投影与专属彩管标签。
5. **Feature Card & Media Frame (特性卡片与媒体预览框)**:
   - 纯白卡片内嵌浅米色媒体占位框 `.frame`，内部绘制 3D 渐变彩管与半调网点示例矢量图形，充满创意张力。
6. **Process Steps (流程步骤)**:
   - 步骤序号 `.idx` 使用渐变色 3D 球形徽标包裹，表面带有细致的半调网点光影；卡片间以 3px 渐变虚线管身相互串联。
7. **Comparison Table (对比矩阵 - 玩味工程卡片风格)**:
   - 纯白大圆角封闭面板，表头采用干净明快的浅暖灰底色（`--bg-card-subtle`），推荐列（`.highlight-col`）采用极淡微光底色并配置 **RECOMMENDED** 高能渐变胶囊徽标，文字保持深墨黑高对比排版，整体具有强烈的现代软件产品矩阵感。
8. **Metadata Footer (技术页脚)**:
   - 底部通栏两端对齐，浅暖纸底衬与 1px 顶部细线，Mono 字体大写，点缀工程版本号与 `✕` 标志。
9. **Admonitions (智能语义提示框)**:
   - 模块化圆角卡片，左侧内置 5px 独立内嵌全圆角 3D 纵向胶囊指示条，`.info` 使用电光蓝渐变、`.warning` 使用柑橘橙金渐变、`.success` 使用翡翠青绿渐变，两端圆润不裁切，标题文字干净纯粹左对齐，去除多余符号。
10. **Timeline (时间轴)**:
    - 纵向主轴为 4px 双色渐变粗线，时间节点 `.timeline-marker` 采用外圈带有半调点阵的渐变球形徽标，右侧内容为纯白悬浮圆角卡片。
11. **Pros & Cons (优劣势红黑榜)**:
    - 左右双圆角卡片：Pros 采用微透翠绿底色与翠绿全边框；Cons 采用微透珊瑚粉底色与珊瑚粉全边框，结构通透整洁。
12. **Stats Grid (核心数据卡片 - 微透彩光与全环绕精致边框)**:
    - 采用分色微透彩光底衬（蓝/橙/绿 `rgba(..., 0.025)`）搭配全包围同色精致边框（`rgba(..., 0.16)`），数值 `.stat-val` 使用超大粗体字，单位 `span` 采用对应能量渐变渲染，悬浮激发生动彩光投影。
13. **Flowchart & Mermaid (流程图与系统架构拓扑)**:
    - 纯白大面板，4 个节点均采用统一规格的 **16px 大圆角轻量卡片**，内置精致的 Monospace 步骤药丸徽标。支持纯 SVG 与 Mermaid 引擎（`darkMode: false`, `background: '#FAF8F3'`, `lineColor: '#0052FF'`），连接线采用轻快干练的细箭头管道，整体轻盈透亮、视觉平衡。
14. **References (参考文献与脚注)**:
    - 纯白圆角面板包裹，有序列表带有大写 Mono 序号徽章，链接带电光蓝下划线，悬浮呈现橙色渐变。
15. **Rich Text (长文本正文模块 - 块级引用)**:
    - 纯白圆角阅读面板，正文行距 1.75，支持粗体、行内代码与引用块（`blockquote`：采用微透橙金底色 `rgba(255, 85, 0, 0.025)`、`1.5px` 精致边框与 24px 全圆角，内嵌全圆角 3D 纵向胶囊条，彻底告别直角泥褐底色）。
16. **FAQ / Q&A List (问答列表)**:
    - 独立折叠条目，问题 `.q` 前置渐变色圆形 `Q` 徽标，Hover 时轻微弹起并呈现半调渐变外边框。
17. **Code Block (多行代码块与终端窗口)**:
    - 深墨黑（`#18181B`）大圆角悬浮终端卡片，顶栏配备弹簧缩放 Mac 活力三色圆点与高能多停点渐变（`--grad-electric-flow`）语言胶囊徽章，代码区包含平滑滚动条与生动现代的语法 Token 着色。

---

## 5. 专属质量清单 (Play Tubular QA Checklist)

- [ ] 全局背景是否为自然舒适的浅暖米白（`#FAF8F3` / `#F5F2EA`），并带有 24px 微型半调点阵纹理？
- [ ] 是否在 Hero 与关键容器中成功融入粗壮鲜活的 **3D 渐变立体彩管/丝带环绕** 视觉符号？
- [ ] 关键徽标、球头末端或高光角标处是否体现了标志性的 **Halftone 半调网点 (点阵光影)** 质感？
- [ ] 主标题是否采用粗壮有力的 Neo-Grotesque 字体（字重 800–900，`-0.03em` 紧凑字距），并配有现代工程连接符（如 `✕`、`//`）？
- [ ] 卡片是否为纯白大圆角（24px），且悬浮交互是否具备轻快生动的**弹簧回弹动效（`cubic-bezier(0.34, 1.56, 0.64, 1)`）**？
- [ ] 推荐态/选中态（`.selected`）是否拥有专属 3D 彩管色条、渐变边框与高亮跃升层级？
- [ ] 整体质感是否兼顾了严谨的工程理工美感与高能量的玩味探索活力？
