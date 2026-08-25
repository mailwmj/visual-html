# Technical Editorial Dark — Design Tokens & Style Specification

> **Style ID**: `industrial-dark`  
> **显示名称**：暗色工业档案风 / Technical Editorial Dark  
> **核心气质**：像一份高级工业设计手册，冷静、克制、强结构、高精度。

---

## 1. Design DNA & 核心原则

1. **硬边工业感**：圆角 0–2px（最多 4px），1px 细边框，实心深黑 Surface (`#0D1110`) 阻断背景网格线，直线，方形状态标签，大号数字。
   - **禁用**：12–24px 大圆角、毛玻璃拟态、模糊重阴影、软糯渐变、大量 emoji、SaaS Dashboard 模板感。
2. **极淡 CAD 技术网格**：近黑底色搭配极淡 CAD 网格（2.5–4.5% 不透明度，32px/128px 步长），作为结构标尺。卡片与内容块必须带有实体 Surface 背景，网格线严禁穿透干扰文字阅读。
3. **严格控制信号色**：
   - 比例分配：背景 55–65% / 文字 25–35% / 边框网格 5–8% / 信号色 3–7%。
   - **信号绿 (`#67E38B`)**：主信号（section marker / 编号 / active / READY / LIVE / 关键数字 / 小面积 CTA）。
   - **信号紫 (`#8C7CFF`)**：第二状态通道（selected / 推荐态 / 双状态对比），用量不超过绿色的 40%。
   - **警告黄 (`#E7E65D`)**：极少量，用于警告与特殊状态。

---

## 2. CSS Design Tokens

```css
:root {
  /* 背景层 */
  --bg: #090C0B;
  --bg-deep: #060808;
  --surface-1: #0D1110;
  --surface-2: #111615;

  /* 文字层 */
  --text-primary: #F2F3EF;
  --text-secondary: #A8ADA8;
  --text-muted: #6F7672;

  /* 边框与网格 */
  --border: #2A302E;
  --border-strong: #404743;
  --grid-minor: rgba(130, 150, 140, .025);
  --grid-major: rgba(130, 150, 140, .045);

  /* 信号色通道 */
  --signal-green: #67E38B;
  --signal-green-soft: #A0F0B7;
  --signal-violet: #8C7CFF;
  --warning: #E7E65D;

  /* 尺寸与间距 */
  --radius: 2px;
  --container: 1240px;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 96px;
  --space-10: 128px;

  /* 字体栈 */
  --font-display: "Inter", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", "Roboto Mono", monospace;
}
```

---

## 3. 核心组件规范

| 组件 | 实现特征 | 关键类名 / 结构 |
|---|---|---|
| **Section Eyebrow** | `◆ 02 / PLAY ─────`，Mono 字体，信号绿，1px 横线 | `.eyebrow`, `.diamond`, `.line` |
| **Hero Heading** | 64–88px，字重 800–850，行高 0.98–1.05，短句且允许中文主动换行 | `h1.hero` |
| **Stats Grid (顶部核心数据)** | 深灰实体 Surface 封闭卡片 + 48–52px 大数字 + 紫色高光单位 (`span`) + 底部等宽标签 | `.stats-grid`, `.stat-card`, `.stat-val`, `.stat-label` |
| **Timeline (发展史与步骤)** | 左侧 Mono 年份（右对齐与 24px line-height 精准基线对齐）+ 居中 45° 旋转菱形点 + 右侧内容 | `.timeline`, `.timeline-item`, `.timeline-marker`, `.timeline-content` |
| **Flowchart (矢量流程图)** | 深黑底色响应式容器 + 自定义 marker 工业级箭头 + 硬边圆角节点 | `.flowchart` (内嵌响应式 SVG / `.node`) |
| **Number Card** | `01` 第一层 → 标题 → 正文，1px 边框，2px 圆角，深灰 surface | `.num-card`, `.num`, `.tag` |
| **Selected Card** | 紫色边框 + 紫色编号 + 紫色 Tag（第二状态通道） | `.num-card.selected` |
| **Admonition (语义提示框)** | 深灰 Surface，左侧 4px 信号绿/紫/黄粗边，大写 Mono 标头 | `.admonition`, `.admonition.info`, `.admonition.warning` |
| **Pros & Cons (红黑榜)** | 左右双分栏，顶部 2px 信号绿（优势）/ 灰阶（劣势）横线 | `.pros-cons`, `.pro-card`, `.con-card` |
| **Spec Row (硬件规格栏)** | 顶部 1px 信号绿贯穿线 + 4列等分 + 大数字 + Mono 单位 | `.spec-row`, `.spec`, `.val`, `.unit` |
| **Process Steps** | 硬边框模块，实体 Surface 背景，左侧超大 Mono 编号 | `.steps`, `.step`, `.idx` |
| **Comparison Table** | 硬边框表格，推荐列 `.cell.violet`（全列统一紫色表头 + 边框 + 紫色圆点 + 微紫底色） | `.cmp`, `.row`, `.cell.violet` |
| **FAQ List (常见问答)** | 深灰 Surface 边框卡片，问题加粗高亮，答案清晰排版 | `.faq`, `.faq-item`, `.q`, `.a` |
| **Metadata Footer** | 顶部 1px 边框，Mono、muted、大写字母元数据 | `footer`, `.meta-foot` |

---

## 4. 专属质量清单 (Industrial Dark Quality Checklist)

- [ ] 背景为 `#090C0B` 近黑底色，网格使用 2.5–4.5% 极淡线，步长 32px/128px，绝不干扰文字。
- [ ] 卡片、模块（`.step`、`.faq-item` 等）均设置实心 Surface 背景（`#0D1110`），阻断背景网格线穿透。
- [ ] 所有卡片、按钮、模块圆角严格控制在 0–2px（最多 ≤4px），无大圆角。
- [ ] 无毛玻璃、无扩散模糊投影（选中/强调仅用 1px 边框或硬偏移色块）。
- [ ] 信号绿用于主要焦点与 Eyebrow，信号紫仅作第二状态对比（≤绿色的 40%）。
- [ ] 对比表中推荐列使用紫色时，列内圆点、文字、边框统一为紫色，杜绝紫绿混搭。
- [ ] 参数、序号、标签、页脚均使用 Mono 等宽字体。
- [ ] 整体气质像“精密工业档案 / 硬件设计手册”，无 SaaS 模板感或赛博霓虹感。
