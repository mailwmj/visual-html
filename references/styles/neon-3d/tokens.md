# 霓虹创意3D风 (Neon 3D) — 设计规范与文本转换 Token

> **风格标识 (Style ID)**: `neon-3d`  
> **显示名称**：霓虹创意3D风 / Neon 3D Creative  
> **核心使命**：**将长篇纯文本转换为具有强烈视觉冲击力、现代潮流感的单文件 HTML 网页与 16:9 PPT 演示文稿。**  
> **视觉气质**：**绝大部分区域保持纯黑底色 (80%+ Pure Pitch Black `#000000`)**，霓虹紫仅在**局部焦点区域**呈现流体光晕（如顶部右上光晕、底部左下极光波浪），全站覆盖微粒胶片噪点纹理（Film Grain Noise Overlay），配合 3D 高光立体卡片与粗体大字号排版。

---

## 1. 长文本转视觉排版映射法则 (Text-to-Visual Rules)

当接收到长篇纯文本时，遵循以下映射规则将其重构为高质量的视觉块：

| 原始长文本类型 | 转换目标视觉组件 | 结构与特征 |
|---|---|---|
| **文章主旨 / 执行摘要** | **Hero 标题 + Lead 导读** | 巨幅大字号超粗标题（中文主动断句）+ 局部右上霓虹紫光斑 + 纯白极简导读 |
| **顶部关键量化指标** | **Stats Grid (核心数据卡片)** | 纯黑中性卡片 + 霓虹紫/粉高光单位 (`span`) + 底部等宽标签 |
| **文中硬件与细节参数** | **Spec Row (指标参数栏)** | 纯黑底 1px 细线指标栏 + 霓虹紫高光数值 + 等宽灰阶单位 |
| **发展史与时间顺序事件** | **Timeline (时间轴流)** | 左侧等宽年份（右对齐与 24px line-height 精准基线对齐）+ 居中霓虹发光圆点 + 右侧深黑卡片 |
| **流程图与架构拓扑** | **Flowchart & Mermaid (流程与架构图)** | 纯黑深底响应式容器 (`#0D0D11`) + 霓虹紫/粉高光主线条 (`#A855F7`)。支持纯 SVG 与 Mermaid 引擎（`darkMode: true`, `lineColor: '#A855F7'`, `primaryBorderColor: '#EC4899'`） |
| **3~4 个并列论点 / 核心能力** | **Cards-3 (三栏编号卡片)** | 纯黑大圆角卡片、霓虹高光描边、选中态展示3D景深与弥散阴影 |
| **核心结论 / 智能提示** | **Admonition (语义高亮提示框)** | 纯黑 3D 卡片 + 内部直立发光光柱 (Accent Bar) + 大写 Mono 标头 |
| **方案选型 / 优劣评估** | **Pros & Cons (红黑榜)** | 左右双分栏纯黑卡片 + 专属霓虹紫/灰阶胶囊标签 + +/- 对齐列表 |
| **操作指引 / 演进阶段 / 路线图** | **Step Flow (多步流程流)** | 局部波浪流光背景 + 霓虹发光圆形数字徽章 + 递进式悬浮卡片 |
| **系统架构 / 界面与功能解构** | **Visual Breakdown & Callout** | 居中设备模型框 + 霓虹定位点（Callout Pin）+ 细折线指向 |
| **方案选型 / 优劣对比** | **Comparison Matrix (暗色对比矩阵)** | 纯边框暗色模块矩阵，推荐列带有霓虹渐变半透明底色 |
| **深度解答 / 常见疑问** | **FAQ (问答卡片组)** | 深黑毛玻璃背景大圆角卡片，问题纯白加粗 |
| **代码片段 / 着色器终端** | **Code Block (多行代码与终端)** | 黑紫 3D 浮雕终端卡片 + 发光霓虹三色圆点 + 洋红 Mono 语言 Badge + 赛博朋克 Token 高亮 |
| **文档分类与出处** | **Top Meta & Footer** | 双端对齐的等宽大写元数据 |

---

## 2. 设计 DNA 与色彩原则

1. **大面积纯黑基座与克制局部流光 (Pure Black Base & Localized Glows)**：
   - 全局 80% 以上区域保持深邃沉静的**纯黑底色 (`--bg: #000000`)**，严禁整个页面通体被紫色污染。
   - **紫色仅作局部光晕点缀 (Localized Glows)**：
     - **顶部区**：仅在 Hero 区域右上侧点缀柔和的霓虹紫光弧。
     - **底部区**：仅在流程/路线图区域左下角点缀斜向流体极光波浪。
     - **中间大部分内容区**：保持彻底纯净的深黑底色（`#000000`）。
2. **全画布微粒胶片噪点 (Film Grain Noise Texture)**：
   - 覆盖层使用轻量纯 CSS/SVG 微粒噪点滤镜（`opacity: 0.045`），为纯黑底色与局部紫光带来高级模拟胶片与实体海报的微粒质感。
3. **高纯度霓虹信号色通道**：
   - **主信号色 霓虹紫 (`#A855F7`)**：仅用于局部高亮光斑、序号标签、核心按钮与选中小卡片。
   - **辅信号色 霓虹洋红 (`#EC4899`)**：用于渐变细节修饰。
4. **深黑卡片与 3D 高光内阴影**：
   - 卡片使用中性深黑 (`#0F0F0F` / `rgba(16, 16, 16, 0.85)`)，配合微弱内高光（`inset 0 1px 0 rgba(255,255,255,0.12)`），避免卡片底色偏紫。

---

## 3. CSS Design Tokens 变量定义

```css
:root {
  /* 背景层：保持纯黑中性底色 */
  --bg: #000000;
  --bg-deep: #000000;
  --surface-1: #0A0A0A;
  --surface-2: #121212;
  --surface-glass: rgba(16, 16, 16, 0.85);
  --surface-card: #0F0F0F;

  /* 文字层 */
  --text-primary: #FFFFFF;
  --text-secondary: #A1A1AA;
  --text-muted: #71717A;

  /* 边框与光晕 */
  --border: rgba(255, 255, 255, 0.10);
  --border-subtle: rgba(168, 85, 247, 0.22);
  --border-strong: rgba(168, 85, 247, 0.60);
  --border-glow: 0 0 20px rgba(168, 85, 247, 0.40);

  /* 信号色通道（霓虹紫、洋红） */
  --signal-cyan: #A855F7; /* 核心高亮主信号（霓虹紫） */
  --signal-cyan-soft: rgba(168, 85, 247, 0.16);
  --signal-blue: #EC4899; /* 辅助信号（霓虹洋红） */
  --signal-blue-deep: #D946EF;
  --signal-glow: rgba(168, 85, 247, 0.50);
  --accent-gradient: linear-gradient(135deg, #A855F7 0%, #EC4899 50%, #06B6D4 100%);
  --accent-gradient-subtle: linear-gradient(180deg, rgba(168, 85, 247, 0.20) 0%, rgba(236, 72, 153, 0.04) 100%);

  /* 阴影与景深 (3D感与局部霓虹弥散) */
  --shadow-card: 0 16px 40px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(255, 255, 255, 0.12);
  --shadow-card-hover: 0 24px 56px rgba(0, 0, 0, 0.95), 0 0 30px rgba(168, 85, 247, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.2);
  --shadow-card-selected: 0 28px 64px rgba(0, 0, 0, 0.95), 0 0 35px rgba(168, 85, 247, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.25);
  --shadow-mockup: 0 30px 80px rgba(0, 0, 0, 0.95), 0 0 50px rgba(168, 85, 247, 0.25);

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

- [ ] **大面积纯黑背景**：页面绝大部分（80%+）为深邃纯黑（`#000000`），无全局性紫光泛滥。
- [ ] **紫色仅限局部光斑**：仅在 Hero 右上方与页面底端左下方等特定区块出现局部流体光晕。
- [ ] **胶片微粒噪点覆盖**：全站覆盖 `opacity: 0.045` 的胶片颗粒噪点层，赋予黑底与光晕真实触感。
- [ ] **信息层级分明**：全文有且仅有一个 Hero 主标题（极粗体大字号），各章节有专属的 Eyebrow 标头。
- [ ] **立体高光效果**：卡片边缘保留 `inset` 内阴影与中性纯黑底色，制造出 3D 悬浮厚度感。
- [ ] **等宽字体规范**：所有数据数值、时间、编号、分类标签统一使用等宽字体（`--font-mono`）。
