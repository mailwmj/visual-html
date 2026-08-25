# Visual HTML Style Tokens: Sunflower Bloom

## 1. 设计理念与特征 (Design Concept & Features)
- **风格名称**：向日葵生机风 (Sunflower Bloom)
- **核心关键词**：生机、温暖、向上的力量、积极、成长、大字号排版、色彩对比。
- **视觉特征**：
  - **背景 (Background)**：带有纸质纹理感的沉静中度蓝 (`#4278A9` 左右)。
  - **色彩 (Color)**：大量使用米白色/奶油白 (`#F2EAE0`) 作为主文本和主标题颜色，配合高饱和度的向日葵明黄 (`#FFC300`) 作为视觉焦点和信号色，点缀少许茎叶绿 (`#6B8E23`)。
  - **排版 (Typography)**：极大字号的无衬线标题（Hero Text），强调紧凑的行高。正文采用清晰易读的无衬线字体，字距适中。
  - **结构 (Structure)**：细线分割 (1px 实线，米白色，带一定透明度)，极简的卡片设计（不使用复杂的阴影或圆角，偏向扁平和纸面叠加感）。

## 2. 核心 CSS 变量 (Design Tokens)
```css
:root {
  /* 基础色彩 */
  --bg-primary: #4578A6; /* 沉静的背景蓝 */
  --bg-surface: #F2EAE0; /* 不透明米白卡片背景，打破整体蓝色的单调感 */
  --bg-surface-hover: #FFFFFF; 
  
  /* 文本色彩 */
  --text-hero: #F2EAE0; /* 米白/奶油白 - 大标题 */
  --text-primary: #F2EAE0; /* 米白 - 正文首选 */
  --text-secondary: rgba(242, 234, 224, 0.7); /* 半透米白 - 辅助文本 */
  --text-inverse: #2A455C; /* 深蓝色文本，用于米白色卡片背景上 */
  --text-inverse-muted: #537593; /* 辅助深色文本 */
  
  /* 信号色与强调色 */
  --signal-yellow: #FFC300; /* 向日葵黄 - 视觉核心点 */
  --signal-yellow-dim: rgba(255, 195, 0, 0.2); 
  --signal-green: #6B8E23; /* 茎叶绿 - 补充点缀 */
  
  /* 边框与线条 */
  --border-color: rgba(242, 234, 224, 0.3); /* 半透明米白线条 */
  --border-radius: 4px; /* 极小圆角，偏向利落的纸质感 */
  
  /* 字体栈 */
  --font-sans: "Helvetica Neue", Helvetica, Arial, "微软雅黑", "Microsoft YaHei", sans-serif;
  --font-mono: "Fira Code", "JetBrains Mono", Consolas, monospace;
}
```

## 3. 16项核心组件视觉契约 (Component Visual Contracts)

1. **Section Eyebrow (区块索引标头)**: 采用 `--signal-yellow` 颜色的小方块作为前缀，编号和标题使用 `--text-secondary`，全大写，右侧跟随一条 1px 的 `--border-color` 细线。注意 `<section>` 本身不再带有全局底边框，以维持画面的干净与连续。
2. **Typography Scale (基础文本层级)**: `.hero` 极具视觉冲击力，字号超大（如 4rem+），紧凑行高（1.1），颜色 `--text-hero`。`.section-title` 醒目，带有下划线或左侧黄色强调线。
3. **Technical Spec Row (规格参数栏)**: 上下边框 1px `--border-color` 划分，`.val` 极具分量的数字使用 `--signal-yellow` 强调，`.unit` 使用全大写 Mono 字体。
4. **Number Cards (编号卡片列)**: 采用实色米白 (`--bg-surface`) 背景的卡片设计，内部文字为深蓝色，以大面积对比色块打破背景的单调感。`.num` 为 `--signal-yellow`，悬浮时卡片上浮并带有轻微阴影。
5. **Feature Card & Media Frame (特性卡片与媒体预览框)**: 卡片外边框 1px 实线，`.tag` 标签使用带边框的米白色。`.frame` 占位框背景为更深的蓝色或半透明白。
6. **Process Steps (流程步骤)**: 左侧具有连贯的黄色细线，节点为黄色实心圆圈。
7. **Comparison Table (对比矩阵)**: 极简的线条表格，仅保留行间下边框。强调列（`.selected-col`）带有非常淡的黄色背景。`.dot` 为向日葵黄。
8. **Metadata Footer (技术页脚)**: 分散对齐，Mono 字体，`--text-secondary` 颜色，顶部 1px 细线分隔。
9. **Admonitions (智能语义提示框)**: 左侧带有 4px 粗的色条（Info 为黄色），背景为 `--bg-surface`，结构利落。
10. **Timeline (时间轴)**: 粗旷的左侧刻度，年份使用超大字号和 `--signal-yellow`。
11. **Pros & Cons (优劣势红黑榜)**: Pros 的标题颜色为 `--signal-yellow`，Cons 为 `--text-secondary`，采用两列并排。
12. **Stats Grid (核心数据卡片)**: 巨大的数字 `.stat-val` 使用米白色，单位 `.stat-label` 使用黄色，无卡片边框。
13. **Flowchart (流程图)**: 节点边框为米白色，线条米白色，激活节点（`.active`）边框和文字为向日葵黄色。
14. **References (参考文献)**: 小字号，颜色淡，链接带下划线，悬浮变黄。
15. **Rich Text (长文本正文模块)**: 行高 1.7，适于阅读。引用（Blockquote）左侧带黄色粗边框。
16. **FAQ / Q&A List (问答列表)**: 展开式设计，问题使用加粗米白，答案使用半透米白，每个 Q&A 底部有分隔线。

## 4. 专属质检项 (QA Checklist)
- [ ] 页面背景是否为纸质感的沉静蓝？
- [ ] 大标题是否足够大且紧凑，视觉冲击力强？
- [ ] 高光色是否仅使用了向日葵黄，没有引入其他多余的信号色？
- [ ] 线条是否为半透明米白细线，避免了厚重的阴影？
