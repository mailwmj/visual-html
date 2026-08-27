# State Governance Blue (国企政务严谨汇报风) — Design Language Reference

## 1. Visual Theme & Atmosphere

国企政务严谨汇报风（State Governance Blue）专为**中国国企、央企、政务信息化规划、大型集团战略汇报、数字化转型方案以及严肃白皮书研报**打造。它立足于中国政企商务汇报的核心审美范式：**权威稳重、逻辑严密、层级井然、图表化叙事与极高可读性**。

全站以纯净通透的冷白（`#FFFFFF`）配合微冷浅灰蓝（`#F4F7FB`）为画布底色，以**国企经典深海蓝（`#103A71`）与工信科技蓝（`#1A56DB`）**为主行动色，辅以冰霜浅蓝（`#F0F6FF`）卡片底衬与蓝色虚线焦点框，彻底摒弃花哨浮夸的弥散光晕与霓虹噪点，将视觉焦点完全聚焦于**业务逻辑、指标关系与推演架构**。

界面的核心视觉特征包括：

1. **贯穿性深蓝标题锚点（Anchor Headline & Primary Line）**：
   - 每一个章节或幻灯片标题下方，贯穿一条坚实洗练的 **1.5px~2px 权威深蓝基线**（`#103A71`），在全屏建立极强的第一视觉锚点；
   - 标题支持关键核心词汇（如“PPT”、“数字化”、“生命周期”）深蓝加粗强调，主副标题层级分明。
2. **双轨容器材质与蓝色虚线聚焦框（Dashed Focus Container）**：
   - 基础卡片采用 **冰霜浅蓝底衬（`#F0F6FF`）** 与纯白卡片（`#FFFFFF`）交替布局，搭配 6px~10px 严谨微圆角与极淡结构细线（`1px solid #CBD5E1`）；
   - 针对“工作开展详情”、“核心策略重点”与“关键诊断指标”，采用专属的 **蓝色虚线重点框（`1.5px dashed #2563EB`）**，形成清晰有力的视觉聚焦点。
3. **图表化叙事结构（Diagram-First Structured Storytelling）**：
   - 拒绝大段无条理的散装文本，大量使用**同心气泡数据云（Bubble Cluster）、生命周期环形切片（Lifecycle Ring Slice）、三箭头推进器（`>>>` Chevron Stream）、多视角业务流转矩阵（Multi-Perspective Flow）与八维雷达策略对比图（8-Axis Radar）**。
4. **多视角胶囊徽章与严谨排版（Perspective Badges & Strict Hierarchy）**：
   - 支持多级纵向视角（用户视角、关键指标、商家视角）的深蓝/浅蓝胶囊标签；
   - 数字指标、公式换算（`转化率 = 成交人数 / 进房人数`）与版本元数据均采用等宽清晰排版。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (Canvas) | `rgb(255, 255, 255)` | `#FFFFFF` | `--bg` | 全局纯白主画布底色 |
| Background (Subtle Blue) | `rgb(244, 247, 251)` | `#F4F7FB` | `--bg-subtle` | 视口外层背景、隔行对比衬底 |
| Background (Stage Canvas) | `rgb(238, 242, 248)` | `#EEF2F8` | `--bg-stage` | PPT 16:9 舞台外层沉浸灰底 |
| Surface (White Card) | `rgb(255, 255, 255)` | `#FFFFFF` | `--surface-card` | 纯白核心主卡片、数据浮动板 |
| Surface (Ice Blue Tint) | `rgb(240, 246, 255)` | `#F0F6FF` | `--surface-card-subtle` | 浅蓝功能面板、步骤流转卡片底板 |
| Surface (Highlight Blue) | `rgb(224, 237, 253)` | `#E0EDFD` | `--surface-highlight` | 选定高亮项、关键标签底色 |
| Surface (Navy Dark Card) | `rgb(16, 58, 113)` | `#103A71` | `--surface-navy` | 深蓝重要表头、反白徽章卡片 |
| Text (Primary Slate) | `rgb(15, 23, 42)` | `#0F172A` | `--text-primary` | 大标题、正文（高对比严谨深墨） |
| Text (Secondary Slate) | `rgb(51, 65, 85)` | `#334155` | `--text-secondary` | 导读段落、次级说明文字 |
| Text (Muted Slate) | `rgb(100, 116, 139)` | `#64748B` | `--text-muted` | 注释、页脚、规格参数等宽标签 |
| Text (Brand Navy) | `rgb(16, 58, 113)` | `#103A71` | `--text-navy` | 强调标题、核心数值、高亮短语 |
| Border (Light Slate) | `rgb(226, 232, 240)` | `#E2E8F0` | `--border` | 1px 浅灰微边框、标准分割线 |
| Border (Structure Blue) | `rgb(191, 219, 254)` | `#BFDBFE` | `--border-blue` | 浅蓝卡片描边、表格横线 |
| Border (Dashed Accent) | `rgb(37, 99, 235)` | `#2563EB` | `--border-dashed` | 1.5px 蓝色虚线重点强调框 |
| Border (Primary Navy Line)| `rgb(16, 58, 113)` | `#103A71` | `--border-navy` | 1.5px~2px 标题下贯穿分割主线 |

### CSS Design Tokens

```css
:root {
  /* 背景层与画布 */
  --bg: #FFFFFF;
  --bg-subtle: #F4F7FB;
  --bg-stage: #EEF2F8;
  
  /* 表面层 (Surface) */
  --surface-card: #FFFFFF;
  --surface-card-subtle: #F0F6FF;
  --surface-highlight: #E0EDFD;
  --surface-navy: #103A71;
  --surface-navy-dark: #0A254A;

  /* 文字层 */
  --text-primary: #0F172A;
  --text-secondary: #334155;
  --text-muted: #64748B;
  --text-navy: #103A71;
  --text-inverse: #FFFFFF;

  /* 核心主行动色与国企政务蓝色谱 */
  --signal-primary: #103A71;       /* 权威国企深海蓝 */
  --signal-brand: #1A56DB;         /* 工信科技蓝 */
  --signal-sky: #3B82F6;           /* 蔚蓝 */
  --signal-light: #EFF6FF;         /* 冰霜浅蓝高亮底 */
  --signal-hover: #0C2B54;         /* 悬停深海蓝 */

  /* 功能语义点缀色 (克制严谨) */
  --signal-accent-red: #D32F2F;    /* 印章红 / 警示红 */
  --signal-accent-green: #16A34A;  /* 松柏绿 / 达标绿 */
  --signal-accent-amber: #D97706;  /* 沉稳金 / 待办黄 */

  /* 边框与分割线 */
  --border: #E2E8F0;
  --border-strong: #CBD5E1;
  --border-blue: #BFDBFE;
  --border-dashed: #2563EB;
  --border-navy: #103A71;

  /* 投影系统 (微弱干净，拒绝厚重弥散) */
  --shadow-sm: 0 1px 3px rgba(16, 58, 113, 0.05);
  --shadow-card: 0 4px 16px rgba(16, 58, 113, 0.06), 0 1px 3px rgba(16, 58, 113, 0.04);
  --shadow-card-hover: 0 8px 24px rgba(16, 58, 113, 0.10);
  --shadow-navy: 0 4px 14px rgba(16, 58, 113, 0.20);

  /* 尺寸与圆角 (政企严谨微圆角) */
  --radius: 8px;
  --radius-sm: 4px;
  --radius-pill: 999px;
  --container: 1140px;

  /* 字体栈 (标准黑体 + 清晰等宽) */
  --font-sans: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", "Noto Sans CJK SC", "Noto Sans SC", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: "Cascadia Mono", Consolas, "SFMono-Regular", "Liberation Mono", Menlo, monospace;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

```html
<!-- 国企政务严谨汇报风必须在每个页面或 Section 顶层包含：
     1. 带有贯穿深蓝细线的 Section 标题栏
     2. 保持浅蓝与纯白交替的结构化卡片材质
     严禁省略标题下划线，严禁将虚线重点框与浅蓝卡片漂白为单一纯白无边框块 -->

<div class="wrap">
  <!-- 标题与贯穿线结构 -->
  <div class="section-head">
    <div class="eyebrow">
      <span class="diamond">◆</span>
      <span>01 / 战略部署</span>
      <span class="line"></span>
    </div>
    <h2 class="section-title">产业大模型<span class="highlight-navy">生命周期与全覆盖体系</span></h2>
  </div>

  <!-- 具象内容卡片容器 -->
  <div class="content-body">
    <!-- 各语义组件 -->
  </div>
</div>
```

```css
/* 贯通性标题锚点样式契约 */
.section-head {
  margin-bottom: 28px;
  padding-bottom: 12px;
  border-bottom: 1.5px solid var(--border-navy);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.section-head .eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 700;
  color: var(--signal-brand);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.section-head .eyebrow .diamond {
  color: var(--signal-primary);
  font-size: 11px;
}

.section-head .section-title {
  font-size: 26px;
  font-weight: 800;
  color: var(--text-primary);
  letter-spacing: -0.01em;
  line-height: 1.3;
}

.section-head .section-title .highlight-navy {
  color: var(--signal-primary);
  font-weight: 900;
}
```

---

## 4. Typography Scale & Rules

### 全字阶量化表

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|
| **Display Hero** | `h1.hero` | `36px ~ 44px` | `800 / Bold` | `1.25` | `-0.02em` | 页面最高冲击力主标题（支持语义断行） |
| **Section Title** | `h2.section-title` | `24px ~ 28px` | `750 / Bold` | `1.3` | `-0.01em` | 章节与幻灯片核心标题（下方带贯通蓝线） |
| **Subsection** | `h3.sub-title` | `18px ~ 20px` | `700` | `1.4` | `0` | 模块小标题、卡片组头部 |
| **Card Title** | `.card-title` | `16px ~ 17px` | `650` | `1.45` | `0` | 卡片与表格内二级功能标题 |
| **Lead / Summary** | `p.lead` | `16px ~ 17px` | `500` | `1.65` | `0` | 章节导读、执行摘要段落 |
| **Body Paragraph** | `p.body`, `.rich-text p`| `15px` | `400` | `1.75` | `0` | 标准长篇正文，字字清晰 |
| **Stat Big Value** | `.stat-val` | `38px ~ 48px` | `800` | `1.1` | `-0.02em` | 核心宏观数据看板与数字指标 |
| **Spec Mono Label** | `.spec .val`, `code` | `14px ~ 15px` | `600` | `1.4` | `0.02em` | 参数规格、等宽代码与数据单位 |
| **Perspective Tag** | `.perspective-pill` | `12px ~ 13px` | `700` | `1` | `0.04em` | 视角药丸、三箭头徽章 |

---

## 5. Signature Component Patterns (核心特征组件规范)

### Pattern 1: 蓝色虚线重点强调卡片 (`.dashed-focus-box`)
用于展示重要工作开展详情、核心战略指标或重点诊断分析：

```html
<div class="dashed-focus-box">
  <div class="focus-box-header">
    <span class="focus-dot"></span>
    <h3 class="focus-title">2024 年工作开展详情</h3>
  </div>
  <div class="focus-box-content">
    <p>2024 年，在公司党委、经营方圆统筹下，围绕全周期精细化管理推进各项目标落地，实现重点指标稳健增长 69%。</p>
    <div class="focus-metric-pill">重点考核：合规率 99.8% | 结算完成率 100%</div>
  </div>
</div>
```

```css
.dashed-focus-box {
  background: var(--surface-card);
  border: 1.5px dashed var(--border-dashed);
  border-radius: var(--radius);
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: var(--shadow-sm);
}

.focus-box-header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.focus-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--signal-brand);
}

.focus-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--signal-primary);
}

.focus-box-content p {
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.7;
}

.focus-metric-pill {
  margin-top: 8px;
  display: inline-block;
  padding: 6px 14px;
  background: var(--surface-card-subtle);
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  color: var(--signal-primary);
  border: 1px solid var(--border-blue);
}
```

---

### Pattern 2: 三箭头推进卡片流 (`.chevron-stream-card`)
用于业务全覆盖、功能全覆盖与数据全覆盖等并列多层流转结构：

```html
<div class="chevron-stream-list">
  <div class="stream-item">
    <div class="stream-badge">
      <span class="chevron">›››</span>
      <span class="badge-text">功能全覆盖</span>
    </div>
    <div class="stream-content">
      <div class="pill-group">
        <span class="pill">规范申报</span>
        <span class="pill">考核规则管理</span>
        <span class="pill">项目合作</span>
        <span class="pill">合作变更</span>
        <span class="pill">投诉违规管理</span>
        <span class="pill">结算单核对</span>
      </div>
    </div>
  </div>
</div>
```

```css
.chevron-stream-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.stream-item {
  display: grid;
  grid-template-columns: 160px 1fr;
  align-items: center;
  background: var(--surface-card-subtle);
  border: 1px solid var(--border-blue);
  border-radius: var(--radius);
  padding: 16px 20px;
  gap: 20px;
}

.stream-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--surface-navy);
  color: var(--text-inverse);
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-weight: 700;
}

.stream-badge .chevron {
  color: #93C5FD;
  font-weight: 900;
  letter-spacing: -2px;
}

.pill-group {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.pill-group .pill {
  background: var(--surface-card);
  border: 1px solid var(--border);
  padding: 6px 14px;
  border-radius: var(--radius-pill);
  font-size: 13px;
  color: var(--text-primary);
  font-weight: 500;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}
```

---

### Pattern 3: 多视角流转矩阵与算式公式卡 (`.perspective-matrix`)
用于展现“用户视角 / 关键指标 / 商家视角”的多维度对照以及转换率计算逻辑：

```html
<div class="perspective-container">
  <div class="perspective-row">
    <div class="perspective-tag tag-navy">
      <div class="tag-icon">👤</div>
      <div class="tag-title">用户视角</div>
    </div>
    <div class="flow-steps">
      <div class="step-bubble">看到直播间</div>
      <div class="step-arrow">→</div>
      <div class="step-bubble">进入直播间</div>
      <div class="step-arrow">→</div>
      <div class="step-bubble">点击商品卡</div>
      <div class="step-arrow">→</div>
      <div class="step-bubble active">成功下单</div>
    </div>
  </div>

  <div class="perspective-row">
    <div class="perspective-tag tag-blue">
      <div class="tag-icon">📊</div>
      <div class="tag-title">关键指标</div>
    </div>
    <div class="formula-cards-grid">
      <div class="formula-card">
        <div class="formula-name">进房率</div>
        <div class="formula-calc">
          <span class="numerator">直播间进房人数</span>
          <span class="divider"></span>
          <span class="denominator">直播间曝光人数</span>
        </div>
      </div>
      <div class="formula-card">
        <div class="formula-name">商品转化率</div>
        <div class="formula-calc">
          <span class="numerator">成交人数</span>
          <span class="divider"></span>
          <span class="denominator">商品点击人数</span>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 6. Do's and Don'ts

### 7 项核心金律 (Do's)
1. **必须保留标题贯通深蓝分割线**：每一个主章节与幻灯片标题下方必须带有 1.5px~2px 权威深蓝线（`#103A71`），维持强烈的锚点秩序。
2. **必须使用严谨的国企深蓝色谱**：以权威深蓝（`#103A71`）、工信蓝（`#1A56DB`）和冰霜浅蓝（`#F0F6FF`）为主基调。
3. **必须善用蓝色虚线聚焦框**：在工作重点、核心方案、指标透视区域应用 `1.5px dashed var(--border-dashed)`。
4. **必须将大段文本图表化**：优先提炼为气泡图、流程卡、药丸标签组、对比矩阵与公式框。
5. **必须保持等宽对齐与参数精确度**：百分比、时间戳、考核指标与参数单位统一使用 Mono 字体。
6. **必须保持 100% 原文信息保真**：保留所有方案细节、技术论据与合规要求，拒绝偷懒省略。
7. **必须支持一键 16:9 无边距打印与全屏演示**：PPT 脚手架必须内置全屏 `F` 快捷键与 `@media print` 样式。

### 7 项严禁红线 (Don'ts)
1. **严禁使用浮夸的弥散高光与赛博朋克霓虹**：杜绝暗紫极光、流体光晕与粗黑波普描边。
2. **严禁将所有浅蓝/虚线卡片漂白为千篇一律的纯白无边框块**。
3. **严禁省略标题下方的深蓝分割线与 Eyebrow 菱形标号**。
4. **严禁在正式汇报中使用不规范的网络表情符号 (Emoji)**，仅允许使用规范严谨的线性图标或 SVG。
5. **严禁使用低对比度的浅灰文字**，正文必须达到 WCAG AA 级以上高对比度清晰度。
6. **严禁把 16:9 PPT 做成超长竖向滚动条页面**，PPT 每页必须单屏自适应收敛。
7. **严禁破坏 4 层隔离坐标系的 Preview 结构**，杜绝顶条切角与文字重叠。

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配国企政务严谨汇报风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: "base",
  themeVariables: {
    darkMode: false,
    background: "#FFFFFF",
    primaryColor: "#F0F6FF",
    primaryTextColor: "#103A71",
    primaryBorderColor: "#1A56DB",
    lineColor: "#103A71",
    secondaryColor: "#E0EDFD",
    tertiaryColor: "#FFFFFF",
    fontFamily: ""SF Pro Display", "Inter", sans-serif"
  }
});
```
