# Soft Sky / 柔空浅蓝 — Design Tokens & Style Specification

> **Style ID**: `soft-sky`  
> **显示名称**：柔空浅蓝风 / Soft Sky Editorial  
> **核心气质**：像一份清透雅致的包装说明页与生活方式手册，纯净、明亮、柔和，保留清晰优雅的同色系结构骨架。

---

## 1. Design DNA & 核心原则

1. **柔和圆润但不失结构**：圆角 8–16px，卡片使用半透明毛玻璃 Surface (`rgba(255,255,255,.82)`) 搭配顶层微高光与极淡冷调阴影。结合全局平滑天蓝渐变与多重纯净流光极光建立清透、空灵、层次丰富的视觉氛围。
   - **禁用**：显眼厚重的背景网格线、厚重深色投影、长拖影、高饱和杂色渐变、emoji 堆砌、拟物糖果风、与冷蓝冲突的燥热色（如橘红、荧光紫）。
2. **全局纯净流体弥散极光画布（Global Atmospheric Canvas）**：
   - **视口全局固定**：流光渐变**必须置于全局固定层 (`body::before` with `position: fixed; inset: 0; z-index: -1`)**，滚动时浑然一体且零断层。
   - **零网格干扰**：背景不使用生硬显眼的网格线，完全依靠纯净的多点高阶流光弥散与毛玻璃折射来表现空间层次。
   - **多点流光弥散**：顶部宽幅晨光 (`#7DD3FC`) + 左侧蔚蓝 (`#38BDF8`) + 右侧冰青微光 (`#A7F3D0`) + 底部深邃淡蓝，形成呼吸感极强的自然冷光晕。
   - **严禁在章节（`<section>`）局部重复添加径向光斑**，杜绝长页面上下拼接时的割裂分块感。
3. **同色系高阶信号色（Monochromatic Contrast）**：
   - 比例分配：浅蓝背景 50–60% / 白色卡片 20–30% / 深灰蓝文字 15–20% / 边框网格 4–6% / 信号色 3–5%。
   - **基础信号色 天蓝 (`#4A9FD4`)**：Eyebrow 标头、常规编号、细边框线、小面积指示。
   - **高亮重点色 蔚蓝 / 极光蓝 (`#0284C7`)**：Selected 推荐态 / 重点卡片高亮 / 实心胶囊标签 / 关键核心数据，以更高纯度与对比度拉开焦点。
   - **微光点缀 水青 (`#7FC2EA`) & 冰蓝 (`#B9E6FE`)**：仅作背景光晕与弱交互过渡点缀。

---

## 2. CSS Design Tokens

```css
:root {
  /* 背景层与渐变 */
  --bg: #EAF6FC;
  --bg-deep: #D8EEF8;
  --surface-1: rgba(255, 255, 255, .82);
  --surface-2: rgba(255, 255, 255, .55);

  /* 文字层 (深蓝灰/灰蓝) */
  --text-primary: #2A3F54;
  --text-secondary: #5D7A8C;
  --text-muted: #90A8B8;

  /* 边框与网格 */
  --border: rgba(93, 179, 232, .28);
  --border-strong: rgba(93, 179, 232, .48);
  --grid-minor: rgba(93, 179, 232, .07);
  --grid-major: rgba(93, 179, 232, .13);

  /* 信号色通道（全同色系演进） */
  --signal-blue: #4A9FD4;
  --signal-blue-soft: #7FC2EA;
  --signal-accent: #0284C7;
  --signal-accent-bg: rgba(2, 132, 199, .06);
  --signal-accent-border: rgba(2, 132, 199, .45);

  /* 阴影与景深 */
  --shadow-card: 0 4px 20px rgba(74, 159, 212, .06), inset 0 1px 0 rgba(255, 255, 255, .95);
  --shadow-card-hover: 0 12px 32px rgba(74, 159, 212, .12), inset 0 1px 0 rgba(255, 255, 255, 1);
  --shadow-card-selected: 0 14px 36px rgba(2, 132, 199, .18), inset 0 1px 0 rgba(255, 255, 255, 1);

  /* 尺寸与圆角 */
  --radius: 14px;
  --radius-sm: 8px;
  --radius-pill: 20px;
  --container: 1180px;

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

  /* 字体栈 (圆润 Display + 精确 Mono) */
  --font-display: "Nunito", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", monospace;
}
```

---

## 3. 核心组件规范

| 组件 | 实现特征 | 关键类名 / 结构 |
|---|---|---|
| **Section Eyebrow** | `◆ 02 / PLAY ─────`，Mono 字体，天蓝色，diamond 带有 2px 圆角 | `.eyebrow`, `.diamond`, `.line` |
| **Hero Heading** | 58–78px，字重 800，行高 1.02–1.08，颜色为 `#2A3F54`（柔和深蓝灰） | `h1.hero` |
| **Stats Grid (顶部核心数据)** | 半透明纯白圆角卡片 + 48–52px 深蓝灰大数字 + 高阶蔚蓝单位 (`span`) + 底部等宽标签 | `.stats-grid`, `.stat-card`, `.stat-val`, `.stat-label` |
| **Timeline (发展史与步骤)** | 左侧天蓝 Mono 年份（右对齐与 24px line-height 精准基线对齐）+ 居中圆点徽标 + 右侧白色卡片 | `.timeline`, `.timeline-item`, `.timeline-marker`, `.timeline-content` |
| **Flowchart (矢量流程图)** | 纯白半透明柔和圆角容器 + 天蓝/蔚蓝箭头 + 圆角矩形节点 | `.flowchart` (内嵌响应式 SVG / `.node`) |
| **Number Card** | 白色半透明卡片、14px 圆角、极淡阴影，天蓝大编号 | `.num-card`, `.num`, `.tag` |
| **Selected Card** | 蔚蓝边框 (`#0284C7`) + 蔚蓝编号 + 实心蔚蓝胶囊 Tag (`#0284C7` 底白字) + 微上浮投影 | `.num-card.selected` |
| **Admonition (语义提示框)** | 白色毛玻璃卡片，左侧 4px 天蓝/琥珀黄/绿边框，柔和阴影 | `.admonition`, `.admonition.info`, `.admonition.warning` |
| **Pros & Cons (红黑榜)** | 左右双分栏，顶部 3px 天蓝（优势）/ 灰阶（劣势）横线，白色圆角卡片 | `.pros-cons`, `.pro-card`, `.con-card` |
| **Spec Row (硬件规格栏)** | 顶部 1px 天蓝色细线 + 4列等分 + 深蓝灰大数字 + Mono 单位 | `.spec-row`, `.spec`, `.val`, `.unit` |
| **Process Steps** | 白色圆角模块，左侧深蓝灰 Mono 编号，天蓝标号点缀 | `.steps`, `.step`, `.idx` |
| **Comparison Table** | 极简白色圆角表格，推荐列 `.head.selected-col` 带天蓝微底色与圆点 | `.cmp`, `.row`, `.selected-col` |
| **FAQ List (常见问答)** | 白色圆角毛玻璃卡片，深蓝灰问题加粗，答案柔和排版 | `.faq`, `.faq-item`, `.q`, `.a` |
| **Metadata Footer** | 浅灰蓝边框，Mono 字体，颜色为 `#90A8B8`，大写字母 | `footer`, `.meta-foot` |

---

## 4. 专属质量清单 (Soft Sky Quality Checklist)

- [ ] 背景为全局固定无缝浅天蓝渐变（`#EAF6FC` → `#F5FBFE` → `#D8EEF8`），未在 `<section>` 局部重复添加断层光斑。
- [ ] 卡片为半透明纯白 Surface（`rgba(255,255,255,.86)`），圆角 8–16px，阴影清透（`rgba(74,159,212,.06–.12)`），杜绝黑灰重投影。
- [ ] 强调与选中态严格采用同色系高纯度蔚蓝（`#0284C7`）搭配实心 Tag，杜绝与冷蓝冲突的橘色、暖红或紫色杂色。
- [ ] 细线网格存在但柔和清晰，不干扰正文文字的阅读对比度。
- [ ] 整体气质清透、纯净且结构规整，具备高水准的现代杂志排版与生活方式质感。
