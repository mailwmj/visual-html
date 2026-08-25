# 霓虹创意3D风 (Neon 3D) — 设计规范与文本转换 Token

> **风格标识 (Style ID)**: `neon-3d`  
> **显示名称**：霓虹创意3D风 / Neon 3D Creative  
> **核心使命**：**将长篇纯文本转换为具有强烈视觉冲击力、现代潮流感的单文件 HTML 网页与 16:9 PPT 演示文稿。**  
> **视觉气质**：极暗深邃纯黑底、高纯度霓虹色渐变（紫、洋红、青蓝）、3D形态的高光质感、夸张的大字号粗体排版、圆润且流动的几何卡片。

---

## 1. 长文本转视觉排版映射法则 (Text-to-Visual Rules)

当接收到长篇纯文本时，遵循以下映射规则将其重构为高质量的视觉块：

| 原始长文本类型 | 转换目标视觉组件 | 结构与特征 |
|---|---|---|
| **文章主旨 / 执行摘要** | **Hero 标题 + Lead 导读** | 巨幅大字号超粗标题（中文主动断句）+ 纯白极简导读 |
| **顶部关键量化指标** | **Stats Grid (核心数据卡片)** | 纯黑 3D 浮雕大圆角卡片 + 霓虹紫/粉高光单位 (`span`) + 底部等宽标签 |
| **文中硬件与细节参数** | **Spec Row (指标参数栏)** | 3D浮雕卡片 + 霓虹紫/洋红渐变发光数值 + 等宽灰阶单位 |
| **发展史与时间顺序事件** | **Timeline (时间轴流)** | 左侧等宽年份（右对齐与 24px line-height 精准基线对齐）+ 居中霓虹发光圆点 + 右侧 3D 卡片 |
| **流程图与架构拓扑** | **Flowchart (矢量流程图)** | 纯黑深底响应式容器 + 自定义霓虹紫/粉 marker 箭头 + 3D 圆角胶囊节点 |
| **3~4 个并列论点 / 核心能力** | **Cards-3 (三栏编号卡片)** | 纯黑大圆角卡片、霓虹高光描边、选中态展示3D景深与弥散阴影 |
| **核心结论 / 智能提示** | **Admonition (语义高亮提示框)** | 左侧 4px 霓虹紫发光竖条 + 大写 Mono 标头 |
| **方案选型 / 优劣评估** | **Pros & Cons (红黑榜)** | 左右双分栏，顶部 3px 霓虹紫（优势）/ 灰阶（劣势）横线，纯黑大圆角卡片 |
| **操作指引 / 演进阶段 / 路线图** | **Step Flow (多步流程流)** | 3D质感霓虹发光圆形数字徽章 + 递进式悬浮卡片 |
| **系统架构 / 界面与功能解构** | **Visual Breakdown & Callout** | 居中3D设备模型框 + 霓虹定位点（Callout Pin）+ 细折线指向 |
| **方案选型 / 优劣对比** | **Comparison Matrix (暗色对比矩阵)** | 纯边框暗色模块矩阵，推荐列带有霓虹渐变半透明底色 |
| **深度解答 / 常见疑问** | **FAQ (问答卡片组)** | 深色毛玻璃背景大圆角卡片，问题纯白加粗 |
| **文档分类与出处** | **Top Meta & Footer** | 双端对齐的等宽大写元数据 |

---

## 2. 设计 DNA 与色彩原则

1. **纯黑沉浸底色**：
   - 背景采用深邃无底的黑色 (`--bg: #000000`)。
2. **高纯度霓虹渐变通道**：
   - **主信号色 霓虹紫 (`#A855F7`)**：用于主要按钮、高亮强调、数字标头。
   - **辅信号色 霓虹洋红 (`#EC4899`) 与 亮青蓝 (`#06B6D4`)**：常结合紫色形成 `linear-gradient`，产生流光溢彩的3D光晕。
3. **3D高光与浮雕质感**：
   - 卡片大量使用深灰色 (`#111111`)，配合内部高光边（`inset 0 1px 0 rgba(255,255,255,0.15)`）和霓虹色外阴影，模拟出圆柱体、3D字母的体积感。
4. **夸张粗体与大圆角**：
   - 标题字体采用极粗字重（`800` 或 `900`）。
   - 卡片圆角偏大（24px - 32px），具有柔和的弧度，胶囊按钮完全为圆形（999px）。

---

## 3. CSS Design Tokens 变量定义

```css
:root {
  /* 背景层 */
  --bg: #000000;
  --bg-deep: #050505;
  --surface-1: #0A0A0A;
  --surface-2: #111111;
  --surface-glass: rgba(17, 17, 17, 0.85);
  --surface-card: #151515;

  /* 文字层 */
  --text-primary: #FFFFFF;
  --text-secondary: #A3A3A3;
  --text-muted: #737373;

  /* 边框与光晕 */
  --border: rgba(255, 255, 255, 0.12);
  --border-subtle: rgba(168, 85, 247, 0.2);
  --border-strong: rgba(168, 85, 247, 0.6);
  --border-glow: 0 0 20px rgba(168, 85, 247, 0.4);

  /* 信号色通道（霓虹紫、洋红、青蓝） */
  --signal-cyan: #A855F7; /* 复用cyan变量名以兼容HTML，但实质为霓虹紫 */
  --signal-cyan-soft: rgba(168, 85, 247, 0.15);
  --signal-blue: #EC4899; /* 实质为洋红 */
  --signal-blue-deep: #D946EF;
  --signal-glow: rgba(168, 85, 247, 0.5);
  --accent-gradient: linear-gradient(135deg, #A855F7 0%, #EC4899 50%, #06B6D4 100%);
  --accent-gradient-subtle: linear-gradient(180deg, rgba(168, 85, 247, 0.2) 0%, rgba(236, 72, 153, 0.05) 100%);

  /* 阴影与景深 (3D感) */
  --shadow-card: 0 10px 40px rgba(0, 0, 0, 0.8), inset 0 2px 4px rgba(255, 255, 255, 0.08);
  --shadow-card-hover: 0 20px 50px rgba(0, 0, 0, 0.9), 0 0 30px rgba(168, 85, 247, 0.3), inset 0 2px 4px rgba(255, 255, 255, 0.12);
  --shadow-card-selected: 0 24px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(236, 72, 153, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.2);
  --shadow-mockup: 0 30px 80px rgba(0, 0, 0, 0.9), 0 0 50px rgba(168, 85, 247, 0.2);

  /* 尺寸与圆角 */
  --radius-sm: 12px;
  --radius: 24px;
  --radius-lg: 32px;
  --radius-device: 48px;
  --radius-pill: 999px;
  --container: 1220px;

  /* 字体栈 */
  --font-display: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", Consolas, "Cascadia Code", monospace;
}
```

---

## 4. 专属长文本生成质检清单 (Quality Checklist)

- [ ] **信息层级分明**：全文有且仅有一个 Hero 主标题（极粗体大字号），各章节有专属的 Eyebrow 标头。
- [ ] **拒绝纯文字堆砌**：长篇文字被合理提炼拆解为「大圆角卡片、指标参数、聚焦卡片、多步流程」等模块。
- [ ] **背景与色彩克制**：背景为 `#000000` 纯黑，只在核心操作与高亮卡片上使用高纯度的霓虹紫/洋红渐变。
- [ ] **立体高光效果**：卡片边缘必须保留 `inset` 内阴影，制造出 3D 悬浮与厚度感。
- [ ] **等宽字体规范**：所有数据数值、时间、编号、分类标签统一使用等宽字体（`--font-mono`）。
