# Soft Editorial Future (温润社论未来风) — Design Tokens & 视觉契约

> **Style ID**: `soft-editorial-future`  
> **显示名称**：温润社论未来风 (Soft Editorial Future)  
> **核心气质**：基于高级 Showroom 的现代玻璃拟态视觉系统，兼具人文社论的排版秩序与未来科技感。全站大量运用极致打磨的高光高透玻璃容器（Glassmorphism），搭配细腻的斜向渐变光泽、1px 纯白高光内阴影与多层弥散柔光。背景深层散布内部色彩温润晕开的 3D 柔光彩球（3D Soft Blooming Color Orbs），内部由核心向外层平滑自然渐变晕开，边缘柔和无生硬边线，在磨砂玻璃折射下呈现出空灵通透、温润典雅、毫无晕眩感的高级展厅质感。

---

## 1. 核心设计理念 (Core Philosophy)

1. **高阶磨砂玻璃容器 (Refined Glassmorphism)**：
   - 所有的卡片、面板与阅读区均采用 `backdrop-filter: blur(28px) saturate(180%)`，配合 `linear-gradient(135deg, rgba(255, 255, 255, 0.82) 0%, rgba(255, 255, 255, 0.46) 100%)`。
   - 边缘带有 1px 的纯白高光内阴影与半透明外边框，营造真实厚度与水晶般的通透质感。
2. **温润晕染柔光彩球 (3D Soft Blooming Color Orbs)**：
   - 这是该风格的核心装饰符号，分布在 `hero`、`cards`、`steps`、`timeline`、`flowchart`、`faq` 等关键区块底层。
   - 摒弃人工模糊滤镜，采用天然平滑的多段径向渐变（冰蓝 `#85C2FF`、蜜桃暖橙 `#FFBE8A`、薰衣草紫 `#D4C7FF`、薄荷春绿 `#9EE4B6`），从球体偏心核心向外层平滑晕开并过渡至纯白与画布底色，搭配内阴影纯白高光，呈现色彩在圆内自然晕开、边缘柔和无生硬描边线、完全不晕眩的 Showroom 展厅质感。
3. **典雅克制的社论排版体系 (Editorial Typographic Hierarchy)**：
   - 大标题采用紧凑优雅的现代几何无衬线与 Apple 字体栈（`"SF Pro Display"`, `"Inter"`, `"PingFang SC"`），大字号加粗配合微负字距（`letter-spacing: -0.02em ~ -0.03em`）。
   - 正文采用舒适行距（1.65~1.8），深灰黑墨（`#111418` / `#4A5568`）主导，层级井然有序。
4. **蔚蓝点睛信号色 (Apple Blue Accent)**：
   - 核心高亮、选中态卡片、时间轴节点与步骤编号统一使用高纯度未来蔚蓝（`#0071E3`），搭配柔和的淡蓝光晕。

---

## 2. 核心变量 (Design Tokens)

```css
:root {
  /* Canvas & Surface Colors */
  --canvas-1: #EAEFF4;           /* 偏冷浅灰底色，用于衬托白色玻璃容器 */
  --canvas-2: #F0F4F8;
  --canvas-deep: #DDE5ED;
  
  /* Ink & Typography Colors */
  --ink-1: #111418;              /* 主标题与重点文字 */
  --ink-2: #4A5568;              /* 正文与副段落 */
  --ink-3: #8292A1;              /* 辅助说明与 Mono 标签 */
  --ink-muted: #9BAEC1;

  /* Accent & Signal Palette */
  --accent-blue: #0071E3;        /* 核心行动与高亮蔚蓝 */
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

  /* Typography Scale */
  --fs-hero: clamp(38px, 5.5vw, 68px);
  --fs-display: clamp(28px, 3.8vw, 44px);
  --fs-h1: 22px;
  --fs-h2: 18px;
  --fs-body-lg: 18px;
  --fs-body: 15px;
  --fs-caption: 13px;

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

## 3. 16项完整组件视觉契约 (Component Visual Contracts)

1. **Section Eyebrow (`.eyebrow`)**: 胶囊状微型磨砂玻璃标签，内置 45° 旋转的蔚蓝菱形图标（`.diamond`）与等宽字距大写文本，附带极淡内发光和 1px 细线。
2. **Typography Scale**: 标题字体采用 `-0.02em` 紧凑字距，大字号黑字主导；导读段落（`.lead`）居中舒展，行高 1.65。
3. **Technical Spec Row (`.spec-row`, `.spec`)**: 嵌套于玻璃卡片内的次级玻璃小格（`rgba(255,255,255,0.55)`），大字号加粗数值配合 Mono 等宽小单位标签。
4. **Number Cards (`.cards-3`, `.num-card`)**: 大圆角（24px）磨砂玻璃卡片。顶部包含底部带细腻分割线的超大蔚蓝数字序号，底部配备药丸状专属 Tag。选中态（`.selected`）触发蔚蓝高光描边、纯白底色微上浮与实心蔚蓝胶囊标签。
5. **Feature Card & Frame (`.feat-grid`, `.feat-card`, `.frame`)**: 悬浮玻璃卡片，支持 `:hover` 轻微上浮；内部 `.frame` 具备精致内阴影与半透明设备边框。
6. **Process Steps (`.steps`, `.step`)**: 步骤卡片独立包裹在磨砂玻璃容器中，数字序号巨大并带有下划分割线，说明文字排版精炼清晰。
7. **Comparison Table (`.cmp-matrix-wrapper`, `.cmp`)**: 统一装载在无边框溢出的整块磨砂玻璃面板内。表头带有浅灰底色，数据行支持 `:hover` 高亮；高亮列（`.highlight-col` / `.selected-col`）呈现整列淡蓝微光与专属强调。支持圆点（`.dot`）与破折号（`.dash`）状态。
8. **Metadata Footer (`footer`, `.meta-foot`)**: 双端对齐的等宽工业级元数据底栏，包含系统版本与文档标识。
9. **Admonitions (`.admonition`)**: 统一采用纯白高透 Showroom 磨砂玻璃展柜容器，彻底告别突兀的彩色描边与生硬贴边竖条。标题前端嵌套 45° 旋转的精致发光菱形微徽标（`.diamond` 语义变体：蔚蓝/暖橙/春绿/绯红），与 `.eyebrow` 菱形徽标完美呼应，整体清透克制、典雅通透。
10. **Timeline (`.timeline`, `.timeline-item`)**: 连续纵向渐变连接线，左侧右对齐年份 Mono 标记配合带光晕的空心节点圆点，右侧为独立悬浮磨砂玻璃内容卡片。
11. **Pros & Cons (`.pros-cons`, `.pro-card`, `.con-card`)**: 统一采用纯白高透 Showroom 磨砂玻璃容器，告别彩色外边框与单调有色平涂底色。通过卡片内部精致克制的 Mono 药丸标签（`.tag`）与带柔和微底色的 `✓` / `✕` 圆形微徽章进行语义区分，与底层背景彩球折射完美共融。
12. **Stats Grid (`.stats-grid`, `.stat-card`)**: 极简大气的玻璃数字面板，超大字体（48~76px）数字搭配蔚蓝单位与 Mono 大写指标标签。
13. **Flowchart (`.flowchart`)**: 磨砂玻璃大展板，内部 SVG 流程图采用圆角卡片节点（12px 圆角）、现代浅灰细线与高亮蔚蓝激活节点（带发光投影）。
14. **FAQ (`.faq`, `.faq-item`)**: 独立圆角玻璃条目，问题前置蔚蓝方块 `Q` 徽标，答案文字优雅缩进。
15. **Rich Text (`.rich-text`)**: 正文承载于居中的大面积磨砂玻璃阅读板内，支持左侧蔚蓝边框的精致引用块（`blockquote`）与淡蓝代码高亮（`code`）。
16. **References (`.references`)**: 底部收尾的磨砂文献面板，包含带下划线的大写 Mono 标题与规范序号列表。

