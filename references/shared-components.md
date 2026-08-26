# Visual HTML — 共享组件结构规范 (Shared Components)

> **架构契约说明**
> 本文件仅定义 AI 解析文本后应输出的 **语义化 DOM 结构** 以及 **各组件的适用场景**。
> **严禁在本规范中包含任何视觉层面的定义**（如颜色、字号、列数、对齐方式、间距等）。所有的排版样式、响应式布局及视觉呈现，均交由各风格模板的 CSS 独立接管。

---

## 1. Section Eyebrow (区块索引标头)

```html
<div class="eyebrow">
  <span class="diamond"></span>
  <span>01 / SECTION_TITLE</span>
  <span class="line"></span>
</div>
```

- **语义场景**：用于长页面的段落或章节开头。
- **组件结构**：包含图标占位符、章节编号与标题、装饰线占位符。

---

## 2. Typography Scale (基础文本层级)

```html
<!-- 主页面 Hero 大标题 -->
<h1 class="hero">主标题内容<br>支持主动换行。</h1>
<p class="lead">导读段落，用于提供背景信息与核心纲要。</p>

<!-- 区块标题 -->
<h2 class="section-title">区块二级标题</h2>

<!-- 正文（独立段落） -->
<p class="body">承接在标题后的引言或散装正文。</p>
```

- **语义场景**：用于构建页面的基本标题树和非长文区域的散装段落。

---

## 3. Technical Spec Row (规格参数栏)

```html
<div class="spec-row">
  <div class="spec">
    <div class="val">60×95<em>mm</em></div>
    <div class="unit">SIZE / 尺寸</div>
  </div>
  <div class="spec">
    <div class="val">500<em>mah</em></div>
    <div class="unit">BATTERY / 电池</div>
  </div>
</div>
```

- **语义场景**：提取文章中的核心硬指标、参数、规格进行提炼展示。
- **组件结构**：包含父容器与若干数据单元，每个单元包含数据值（支持 `em` 标记单位）与指标标签。

---

## 4. Number Cards (编号卡片列)

```html
<div class="cards-3">
  <div class="num-card">
    <div class="num">01</div>
    <h3>模块标题</h3>
    <p>该模块的详细描述说明内容。</p>
  </div>
  <!-- 强调/推荐状态使用 .selected -->
  <div class="num-card selected">
    <div class="num">02</div>
    <h3>核心功能</h3>
    <p>重点突出的核心模块描述。</p>
  </div>
</div>
```

- **语义场景**：适用于“三个特点”、“三大步骤”等带有明显次序或并列逻辑的内容区块。
- **组件结构**：包含编号、子标题、段落描述。支持追加 `.selected` 类以传递次级强调语义。

---

## 5. Feature Card & Media Frame (特性卡片与媒体预览框)

```html
<div class="feat-grid">
  <div class="feat-card">
    <div class="tag">// PLAY MODE</div>
    <h3>特性标题</h3>
    <p>特性的详细能力和用户体验描述。</p>
    <div class="frame">MEDIA PLACEHOLDER</div>
  </div>
</div>
```

- **语义场景**：适用于产品核心卖点或需要附带产品图/演示视频说明的段落。
- **组件结构**：包含类别标签、主标题、描述文本，以及用于容纳媒体资源的占位框（`.frame`）。

---

## 6. Process Steps (流程步骤)

```html
<div class="steps">
  <div class="step">
    <div class="idx">01</div>
    <div>
      <h3>步骤标题</h3>
      <p>步骤对应的操作说明或细节描述。</p>
    </div>
  </div>
</div>
```

- **语义场景**：用于说明系统的工作流、操作指南或按部就班的执行计划。
- **组件结构**：包含序号容器与内容容器（含标题及描述）。

---

## 7. Comparison Table (对比矩阵)

```html
<div class="cmp cmp-matrix">
  <div class="row cmp-row head header">
    <div class="cell cmp-cell">对比维度</div>
    <div class="cell cmp-cell">方案 A</div>
    <div class="cell cmp-cell selected-col highlight-col">方案 B (推荐)</div>
  </div>
  <div class="row cmp-row">
    <div class="cell cmp-cell">调度能力</div>
    <div class="cell cmp-cell"><span class="dot"></span> 基础支持</div>
    <div class="cell cmp-cell selected-col highlight-col"><span class="dot"></span> 完整闭环</div>
  </div>
</div>
```

- **语义场景**：将文本中的多方案优劣对比、版本差异转化为矩阵化结构。
- **组件结构**：包含表头行与数据行，使用标记类（`.dot`, `.dash` 等）或纯文本表示状态，支持列级的强调语义（`.selected-col` / `.highlight-col`）。兼容 `.cmp` 与 `.cmp-matrix` 两套主流命名。

---

## 8. Metadata Footer (技术页脚)

```html
<footer>
  <div class="wrap">
    <div class="meta-foot">
      <span>SYSTEM METADATA</span>
      <span>BUILD VERSION</span>
      <span>DOCUMENT TYPE</span>
    </div>
  </div>
</footer>
```

- **语义场景**：页面底部，用于标注系统信息、生成时间和文档属性。

---

## 9. Admonitions (智能语义提示框)

```html
<div class="admonition info">
  <div class="admonition-title">核心结论</div>
  <p>这是 AI 总结出的一段重要文字说明，用于结论高亮。</p>
</div>
<!-- 语义变体支持: .info, .warning, .success, .error -->
```

- **语义场景**：从长文中提取出的关键警告、总结性陈述或前置提醒。
- **组件结构**：容器（附带语义分类标示类）、标题行与提示正文。

---

## 10. Timeline (时间轴)

```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-marker">2023</div>
    <div class="timeline-content">
      <h3>立项阶段</h3>
      <p>特定时间节点发生的核心事件描述。</p>
    </div>
  </div>
</div>
```

- **语义场景**：遇到包含年份、日期或顺序发展史的长文时，自动转化为时间轴结构。
- **组件结构**：包含时间节点标记（`.timeline-marker`）与该节点的详细内容区块。

---

## 11. Pros & Cons (优劣势红黑榜)

```html
<div class="pros-cons">
  <div class="pro-card">
    <div class="tag">PROS / 优势</div>
    <ul>
      <li>正向特性与优势一</li>
      <li>正向特性与优势二</li>
    </ul>
  </div>
  <div class="con-card">
    <div class="tag">CONS / 劣势</div>
    <ul>
      <li>负向特性与限制一</li>
    </ul>
  </div>
</div>
```

- **语义场景**：分析报告中的双面评估、方案利弊拆解。
- **组件结构**：正向容器（`.pro-card`）与负向容器（`.con-card`），内含标签及无序列表。

---

## 12. Stats Grid (核心数据卡片)

```html
<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-val">300<span>%</span></div>
    <div class="stat-label">ANNUAL GROWTH</div>
  </div>
</div>
```

- **语义场景**：提炼商业报告或总结陈词中的爆炸性核心数据。
- **组件结构**：包含数值部分（支持分离的单位 `span`）与数据解释标签。

---

## 13. Flowchart & Diagrams (流程图、系统架构与 Mermaid 图表引擎)

本系统提供**原生纯矢量 SVG** 与 **Mermaid 动态图表引擎** 双轨架构，由 AI 根据长文本的复杂程度自主决策选用：

### A. 方式一：原生纯矢量 SVG (适合 3~5 步简单线性流程，100% 离线零依赖)

```html
<div class="flowchart">
  <svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor" />
      </marker>
    </defs>
    <!-- 节点 1 -->
    <g class="node">
      <rect x="20" y="25" width="150" height="70" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-width="1.5" />
      <text x="35" y="52" fill="currentColor" font-size="10" opacity="0.6">01 / INPUT</text>
      <text x="35" y="74" fill="currentColor" font-size="14" font-weight="700">输入节点</text>
    </g>
    <line x1="170" y1="60" x2="220" y2="60" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.4" />
    <!-- 节点 2 -->
    <g class="node">
      <rect x="225" y="25" width="150" height="70" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-width="1.5" />
      <text x="240" y="52" fill="currentColor" font-size="10" opacity="0.6">02 / PROCESS</text>
      <text x="240" y="74" fill="currentColor" font-size="14" font-weight="700">处理逻辑</text>
    </g>
    <line x1="375" y1="60" x2="425" y2="60" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.4" />
    <!-- 节点 3 (高亮态) -->
    <g class="node active">
      <rect x="430" y="25" width="150" height="70" rx="4" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="2" />
      <text x="445" y="52" fill="currentColor" font-size="10">03 / CORE</text>
      <text x="445" y="74" fill="currentColor" font-size="14" font-weight="700">核心引擎</text>
    </g>
    <line x1="580" y1="60" x2="630" y2="60" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.4" />
    <!-- 节点 4 -->
    <g class="node">
      <rect x="635" y="25" width="145" height="70" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-width="1.5" />
      <text x="650" y="52" fill="currentColor" font-size="10" opacity="0.6">04 / OUTPUT</text>
      <text x="650" y="74" fill="currentColor" font-size="14" font-weight="700">成果交付</text>
    </g>
  </svg>
</div>
```

---

### B. 方式二：Mermaid 动态图表引擎 (适合复杂分支拓扑、时序调用、状态机、类图与思维导图)

```html
<div class="flowchart mermaid-wrapper">
  <pre class="mermaid">
flowchart LR
    A[01 / INPUT<br><b>原始输入</b>] --> B[02 / EXTRACT<br><b>AI 语义提取</b>]
    B --> C{架构决策<br><b>Native SVG 或 Mermaid?</b>}
    C -->|简单 3-5 步| D[纯矢量 SVG<br><b>零依赖秒开</b>]
    C -->|复杂拓扑/时序| E[Mermaid 引擎<br><b>自动清洗与风格渲染</b>]
    D --> F[成果交付]
    E --> F
  </pre>
</div>
```

#### 1. 适用场景与支持图表类型：
- **复杂流程图 (Flowchart)**：`flowchart LR`, `flowchart TD`，多分支判断、循环流转；
- **时序交互图 (Sequence Diagram)**：`sequenceDiagram`，展示多服务、Agent 之间的请求响应与调用链；
- **状态机图 (State Diagram)**：`stateDiagram-v2`，展示系统生命周期与状态转移；
- **类图与数据模型 (Class / ER Diagram)**：`classDiagram` 或 `erDiagram`；
- **思维导图与架构树 (Mindmap)**：`mindmap`；
- **版本演进与分支 (Git Graph)**：`gitGraph`。

#### 2. 页面底部必须注入的标准清洗与渲染脚本 (ESM 模版)：
当页面包含 `.mermaid` 容器时，必须在 `</body>` 前引入以下自动化脚本：

```html
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

  // 1. 语法容错清洗：自动剥离 // MERMAID, /* MERMAID */ 等非标准前缀注释
  document.querySelectorAll('.mermaid').forEach(el => {
    el.textContent = el.textContent
      .replace(/^\s*\/\/\s*MERMAID/i, '')
      .replace(/^\s*\/\*[\s\S]*?\*\//, '')
      .trim();
  });

  // 2. 根据当前页面风格注入对应的 themeVariables（确保与风格包浑然一体）
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
      /* 按照各风格包配置对应的色彩字典，例如 industrial-dark: */
      darkMode: true,
      background: '#0D1110',
      primaryColor: '#131924',
      primaryTextColor: '#F2F3EF',
      primaryBorderColor: '#67E38B',
      lineColor: '#67E38B',
      secondaryColor: '#1B2433',
      tertiaryColor: '#090C0B',
      fontFamily: '"IBM Plex Mono", Consolas, monospace'
    }
  });
</script>
```

#### 3. 11 款视觉风格专属 Mermaid `themeVariables` 字典对照表：

| 风格 ID (`style_id`) | `darkMode` | `background` | `primaryColor` | `primaryTextColor` | `lineColor` | `primaryBorderColor` |
|---|---|---|---|---|---|---|
| **`industrial-dark`** | `true` | `#0D1110` | `#131924` | `#F2F3EF` | `#67E38B` | `#67E38B` |
| **`soft-sky`** | `false` | `#FFFFFF` | `#EAF6FC` | `#2A3F54` | `#0284C7` | `#0284C7` |
| **`obsidian-cyan`** | `true` | `#151D2A` | `#131924` | `#FFFFFF` | `#38BDF8` | `#38BDF8` |
| **`play-tubular`** | `false` | `#FAF8F3` | `#FFFFFF` | `#111111` | `#0052FF` | `#0052FF` |
| **`warm-craft`** | `false` | `#F7F4EC` | `#EDE8DC` | `#242724` | `#323D24` | `#323D24` |
| **`neon-3d`** | `true` | `#0D0D11` | `#16121E` | `#FFFFFF` | `#A855F7` | `#EC4899` |
| **`pixel-pop`** | `false` | `#FFFFFF` | `#FFF8D6` | `#000000` | `#000000` | `#000000` |
| **`brutalist-acid`** | `false` | `#FFFFFF` | `#00E5CC` | `#000000` | `#000000` | `#FF4591` |
| **`sunflower-bloom`** | `true` | `#1E3A5F` | `#2A455C` | `#F2EAE0` | `#FFC300` | `#FFC300` |
| **`summer-dopamine`** | `true` | `rgba(15,23,42,0.85)` | `rgba(255,255,255,0.15)` | `#FFFFFF` | `#00E676` | `#FF66B2` |
| **`soft-editorial-future`** | `true` | `#0C131F` | `#162032` | `#F8FAFC` | `#38BDF8` | `#38BDF8` |

---

## 14. References (参考文献与脚注)

```html
<div class="references">
  <h3>REFERENCES / 参考文献</h3>
  <ol>
    <li id="ref-1">文献名称或链接 <a href="#fnref-1">↩</a></li>
  </ol>
</div>
```

- **语义场景**：长文末尾的引用来源声明。
- **组件结构**：带有锚点支持的有序列表。

---

## 15. Rich Text (长文本正文模块)

```html
<div class="rich-text">
  <h3>结构化正文标题</h3>
  <p>这是标准的正文模块容器。遇到无法归类到上述高级组件（如时间轴、数据卡片等）的常规段落时，统一放入此容器中。</p>
  
  <p>在这个模块中，允许使用标准的 <strong>Markdown 内联语法</strong>，包括 <em>斜体</em>、<code>代码标识</code> 以及超链接。</p>
  
  <blockquote>
    长篇大论中引用的原话、名人名言或强调段落，应转换为 Blockquote 结构。
  </blockquote>
  
  <h4>子列表支持</h4>
  <ul>
    <li>这是无序列表项目一</li>
    <li>这是无序列表项目二</li>
  </ul>
</div>
```

- **语义场景**：无法映射为特殊组件的大段常规 Markdown 文本。
- **组件结构**：一个安全的沙盒容器，其内部支持标准的 HTML 文本元素（`h3`, `h4`, `p`, `ul`, `ol`, `blockquote`, `strong`, `em`, `code`, `a`）。

---

## 16. FAQ / Q&A List (问答列表)

```html
<div class="faq">
  <div class="faq-item">
    <div class="q">核心问题内容？</div>
    <div class="a">针对该问题的详细解答。</div>
  </div>
</div>
```

- **语义场景**：采访记录、常见问题解答、文档末尾的疑难排解。
- **组件结构**：问答对容器，分别包裹问题（`.q`）与答案（`.a`）。

---

## 17. Sticky Quick Nav & Progress Bar (长文档悬浮目录与进度条 - 可选增强)

```html
<!-- 顶部阅读进度条 -->
<div class="reading-progress" id="reading-progress"></div>

<!-- 悬浮快捷目录 (适用于多章节长文，必须配置隐藏原生滚动条并支持自适应居中折行) -->
<nav class="quick-nav">
  <a href="#section-1">01 / 摘要</a>
  <a href="#section-2">02 / 核心参数</a>
  <a href="#section-3">03 / 系统架构</a>
</nav>
```

- **语义场景**：当生成的 Web 页面包含 4 个以上大章节时，在顶部添加极简悬浮胶囊目录与平滑进度条，提升长文阅读的定位效率。
- **排版契约**：必须隐藏浏览器原生横向滚动条（`scrollbar-width: none;` 及 `::-webkit-scrollbar { display: none; }`），容器必须居中自适应（`max-width: fit-content; margin: 0 auto;`），严禁在药丸下方出现灰色滚动条轨道。

---

## 18. Editorial Interview & Dialogue Rounds (社论访谈录 / 交互推演轮次)

```html
<div class="interview-rounds">
  <div class="round-card">
    <div class="round-header">
      <span class="round-badge">ROUND 01 / 阶段标头</span>
      <span class="round-status">STATUS // 前沿与依赖状态</span>
    </div>
    <div class="round-body">
      <!-- AI 提问卡组 -->
      <div class="ai-questions-block">
        <div class="ai-block-head">
          <span class="dot"></span>
          <span>AI 访谈助手 · 第 1 轮前沿提问</span>
        </div>
        <div class="q-deck">
          <div class="q-item">
            <div class="q-badge">01</div>
            <div class="q-title">核心决策问题内容？</div>
            <div class="q-recom-note">
              <strong>✦ 推荐方案</strong>针对该问题的最优建议与详细论证说明。
            </div>
          </div>
          <div class="q-item">
            <div class="q-badge">02</div>
            <div class="q-title">事实排查或次级衍生问题？</div>
            <div class="q-subagent-note">
              <strong>📡 异步子代理排查中</strong>正在后台静默检索客观事实，报告返回前不阻塞主线程交互...
            </div>
          </div>
        </div>
      </div>

      <!-- 用户决策拍板便签 -->
      <div class="user-decision-note">
        <div class="user-decision-head">
          <span class="check-badge">✓</span>
          <span>DECISION // 你的拍板反馈</span>
        </div>
        <div class="user-decision-text">“用户针对本轮问题的确认或调整结果。”</div>
      </div>
    </div>
  </div>
</div>
```

- **语义场景**：多轮需求访谈、AI Agent 人机协同推演、复杂系统阶段性决策审查与步骤答辩。
- **组件结构**：轮次大卡片（`.round-card`）包含阶段标头、AI 前沿提问卡组（`.ai-questions-block`，内含问题项 `.q-item`、推荐方案便签 `.q-recom-note`、异步子代理排查条 `.q-subagent-note`）以及独立的用户拍板决策便签（`.user-decision-note`）。
- **排版原则**：严禁使用通用即时聊天工具的生硬粗边框或廉价对话气泡；必须按照社论访谈录 / 手账便签卡片的典雅格式排版。

---

## 19. Code Block (多行代码块与终端窗口)

```html
<div class="code-block">
  <div class="code-header">
    <div class="code-dots">
      <span></span><span></span><span></span>
    </div>
    <span class="code-lang">BASH / SHELL</span>
    <button class="code-copy-btn" onclick="navigator.clipboard.writeText(this.closest('.code-block').querySelector('code').innerText); this.innerText='COPIED!'; setTimeout(()=>this.innerText='COPY', 2000)">COPY</button>
  </div>
  <pre><code><span class="token-comment"># 启动高可用推理集群并挂载模型权重</span>
<span class="token-keyword">export</span> CLUSTER_ENV=production
<span class="token-keyword">export</span> WORKER_THREADS=32

<span class="token-function">curl</span> -fsSL https://engine.internal.net/install.sh | <span class="token-keyword">bash</span>
systemctl enable --now worker-engine.service</code></pre>
</div>
```

- **语义场景**：展示命令行终端指令、配置文件（YAML/JSON/TOML）、核心算法片段、API 接口调用及多行工程代码。
- **组件结构**：
  - 外部窗口容器（`.code-block`），内嵌顶栏标头（`.code-header`）与代码展示区（`pre` & `code`）。
  - 顶栏标头包含：装饰控制圆点（`.code-dots`）、大写 Mono 语言指示徽标（`.code-lang`）以及轻量交互复制按钮（`.code-copy-btn`）。
  - 语法标记支持标准语义 Token 类：`.token-comment`（注释）、`.token-keyword`（关键字/控制流）、`.token-string`（字符串）、`.token-function`（函数/指令名）、`.token-number`（数字/参数）、`.token-operator`（运算符）。
- **优雅降级契约**：在 `.rich-text` 中直接出现的原生 `<pre><code>...</code></pre>` 同样由各风格 CSS 提供一体化的背景容器、等宽字体与平滑横向滚动兜底保护。

