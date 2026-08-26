# Summer Dopamine / 汽水镇的夏天 — Design Tokens & Style Specification

> **Style ID**: `summer-dopamine`
> **显示名称**：多巴胺夏日风 / Summer Dopamine
> **核心气质**：色彩缤纷、高饱和度多巴胺渐变背景（粉红、亮蓝、翠绿、明黄），配合极高磨砂玻璃质感（Glassmorphism）、大圆角、白色粗体无衬线字体，传递出活泼、清凉、夏日汽水般的元气与生命力。

---

## 1. Design DNA & 核心原则

1. **高饱和多巴胺渐变网格背景**：背景不再是单色，而是由多个高饱和度的发光点（Pink, Cyan, Yellow, Lime）组成的流体或静态渐变网格（Mesh Gradient），必须置于全局固定层（`body::before` with `position: fixed; z-index: -1`），不可随页面滚动而断层。
2. **极高磨砂玻璃质感（Glassmorphism）**：
   - 所有的模块、卡片、图表容器均采用高斯模糊（`backdrop-filter: blur(20px) saturate(120%)`）。
   - 卡片背景必须为半透明白色（例如 `rgba(255,255,255, 0.25)`），并在边缘保留 1px 的白色半透明描边（`border: 1px solid rgba(255, 255, 255, 0.5)`）以模拟玻璃切边反光。
   - 阴影使用高弥散度、低透明度的柔和色彩或纯白光晕，避免沉闷的黑灰阴影。
3. **大圆角与药丸形（Pill Shape）**：整体几何语言必须极其圆润，卡片基础圆角 24px-32px，按钮或标头使用全圆角（100px）。
4. **纯白与高对比度排版**：标题、大段文字及核心数据应优先使用纯白色（`#ffffff`），在必要时可使用高饱和对比色（如粉红、翠绿）。中文字体推荐使用圆体或粗体无衬线字体。

---

## 2. CSS Design Tokens

```css
:root {
  /* 背景层：多巴胺渐变底色定义见 body::before */
  --bg-gradient-1: #FF66B2; /* 汽水粉 */
  --bg-gradient-2: #0077FF; /* 冰镇蓝 */
  --bg-gradient-3: #00E676; /* 薄荷绿 */
  --bg-gradient-4: #FFEA00; /* 柠檬黄 */
  
  /* 玻璃拟物层 (Glassmorphism) */
  --surface-1: rgba(255, 255, 255, 0.15); /* 降低白底不透明度，追求极致通透 */
  --surface-2: rgba(255, 255, 255, 0.25);
  --glass-blur: blur(24px) saturate(120%);

  /* 文字层 */
  --text-primary: #FFFFFF;
  --text-secondary: rgba(255, 255, 255, 0.85);
  --text-muted: rgba(255, 255, 255, 0.65);
  --text-inverse: #1F2937;

  /* 边框与网格 */
  --border: rgba(255, 255, 255, 0.3);
  --border-strong: rgba(255, 255, 255, 0.6);

  /* 信号色通道 */
  --signal-pink: #FF66B2;
  --signal-blue: #0077FF;
  --signal-green: #00E676;
  --signal-yellow: #FFEA00;

  /* 阴影与景深 */
  --shadow-glass: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
  --shadow-glass-hover: 0 12px 40px 0 rgba(31, 38, 135, 0.25);

  /* 尺寸与圆角 */
  --radius: 24px;
  --radius-sm: 16px;
  --radius-pill: 100px;
  --container: 1180px;

  /* 字体栈 (圆润 Display + 精确 Mono) */
  --font-display: "Arial Rounded MT Bold", "Varela Round", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "Fira Code", "JetBrains Mono", "SFMono-Regular", monospace;
}
```

---

## 3. 核心组件视觉契约

根据 `shared-components.md`，以下 16 个核心组件的呈现规则：

1. **Section Eyebrow**: 纯白半透明胶囊背景（Pill Shape），白色 Mono 字体，左右无横线，通过 `rgba(255,255,255,0.2)` 背景框住。
2. **Typography Scale**: Hero Heading 超大字号（64-80px），纯白色，文字带轻微文字发光（`text-shadow`）。
3. **Technical Spec Row**: 玻璃态卡片容器，列与列之间用半透明白色细线分隔，数据值纯白色。
4. **Number Cards**: 24px 大圆角玻璃卡片，左上角大字号半透明白色编号，Hover 时边框与透明度增加。
5. **Feature Card & Media Frame**: 极高透明度背景，内部 Media 占位框使用 `.surface-2` 甚至带有内阴影的微凸起质感。
6. **Process Steps**: 纵向排布的彩色发光圆点，连接线为白色半透明虚线，右侧为玻璃卡片。
7. **Comparison Table**: 放弃传统网格表格，采用圆角玻璃斑马纹行。推荐列高亮背景为 `--surface-2`，带 1px 白边。
8. **Metadata Footer**: 页面底部居中排布，全大写，文字透明度 60% 的白色，无多余边框。
9. **Admonitions**: 不同状态使用多巴胺色的渐变边框或半透明彩色背景。如 `.info` 用薄荷绿微透，`.warning` 用柠檬黄微透。
10. **Timeline**: 白色的垂直粗线，年份在胶囊状彩色渐变气泡中，内容节点为标准玻璃卡片。
11. **Pros & Cons**: 左右两栏，优势卡片带一点薄荷绿背景光晕，劣势卡片带汽水粉背景光晕。
12. **Stats Grid**: 超大纯白数字（80px+），背景为高度模糊的圆形或胶囊态斑块。
13. **Flowchart & Mermaid**: SVG 线条为白色或高饱和粉蓝色，节点为 16px 圆角玻璃框。支持纯 SVG 与 Mermaid 引擎（`darkMode: true`, `background: 'rgba(15,23,42,0.85)'`, `lineColor: '#00E676'`, `primaryBorderColor: '#FF66B2'`）。
14. **References**: 半透明玻璃底色的无序列表，链接颜色使用亮蓝色 `--signal-blue`。
15. **Rich Text**: 标准 Markdown 内容包裹在 24px 圆角的毛玻璃大容器中，保持高对比度阅读。
16. **FAQ / Q&A List**: 手风琴或堆叠卡片，问题为纯白色加粗大字号，答案为 `text-secondary`。
17. **Code Block (多行代码块与毛玻璃终端)**: 极高模糊深色毛玻璃卡片（`rgba(15, 23, 42, 0.85)`）+ 多巴胺糖果三色圆点 + 柠檬黄 Mono 语言 Badge + 元气马卡龙色系语法 Token 高亮。

---

## 4. 专属质量清单 (Summer Dopamine Quality Checklist)

- [ ] 背景为全局固定无缝多巴胺色块网格（粉、蓝、绿、黄的组合渐变），滚动时不随内容断开。
- [ ] 所有卡片 100% 具备 `backdrop-filter: blur(...)` 属性，且边框为半透明白色（1px solid rgba(255,255,255,0.4)）。
- [ ] 卡片圆角必须非常大（至少 24px，部分胶囊为 100px），没有尖锐的直角。
- [ ] 字体必须优先使用高对比度白色，并避免深黑色文字出现在透明度较低的背景上。
- [ ] 摒弃传统的冷酷商务阴影，全面拥抱高饱和度的发光（glow）或透明色投影。
