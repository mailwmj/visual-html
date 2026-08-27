# Extend Style Pack Route

本文件是创建、修改、扩展和注册 Visual HTML 风格包的运行时 authority。它同时定义生命周期与最终风格包契约；参考材料的详细提炼方法按条件加载 [`../style-reference-extraction.md`](../style-reference-extraction.md)。

## 0. 路由边界与加载集合

- 用户要求的最终结果是可复用风格包时进入本 route。图片、截图或 PPT/PPTX 是输入材料，不决定输出媒介。
- 用户只要求当前 Web/PPT 参考某种视觉方向时，不进入本 route，使用对应 Generate route 的单次参考 profile。
- 创建新风格时读取本文件；只有存在参考材料时再读取 `style-reference-extraction.md`。
- Style Brief 获得确认或用户明确授权跳过确认后，读取 [`../shared-components.md`](../shared-components.md)、[`../_base-scaffold-web.html`](../_base-scaffold-web.html)、[`../_base-scaffold-ppt.html`](../_base-scaffold-ppt.html) 和共享 [`../ppt-output-contract.md`](../ppt-output-contract.md)。不得为了实现双媒介 scaffold 而加载另一个顶层 route authority。
- 修改已有风格时，确认 `style_id` 后只额外读取该风格的 `design.md`、目标 scaffold 和直接相关资源，不读取其他风格实现来拼贴样式。

默认参考模式是 `Inspiration`：目标是创造与参考材料属于同一视觉家族的独立设计系统，而非逐像素、逐页或逐构图复刻。只有用户明确要求高保真适配时才提高参考强度。

## 1. 生命周期与状态门

| Stage | 核心产物 | 允许进入下一阶段的条件 |
|---|---|---|
| 1. Intake | 请求类型、参考输入、范围和拟议元数据 | 已确定创建/修改/注册意图与参考模式 |
| 2. Reference Extraction | Style Brief 草案 | 观察、推演、未知和排除项可区分 |
| 3. Brief Confirmation | 已确认 Style Brief | 用户确认或明确授权跳过此确认门 |
| 4. Style Architecture | Core Visual DNA 与双媒介转译规则 | 风格规则可脱离参考内容独立成立 |
| 5. Representative Proofs | Web 代表区块与 PPT 代表页 | 小样覆盖主要视觉基因和常见内容类型 |
| 6. Visual Confirmation | 已确认视觉方向 | 用户确认或明确授权跳过此确认门 |
| 7. Full Package | 完整风格目录 | 五类必需文件和双媒介契约齐备 |
| 8. Quality Gate | 结构、运行、视觉和泛化证据 | 所有适用检查通过，无未声明重大风险 |
| 9. Registration | Registry 与人类可读目录更新 | 仅在 Stage 8 通过后执行 |

状态必须单向推进：`brief-draft → brief-approved → proof-approved → package-built → validated → registered`。不得先写入 `registry.json` 再补设计文件、确认或视觉验收。

## 2. 分阶段执行契约

### Stage 1 — Intake

1. 判断是新建、修改已有风格，还是仅补齐未注册目录。
2. 记录参考输入：文字方向、图片/截图、PPT/PPTX，或它们的组合。
3. 默认采用 `Inspiration`；用户已经说“仅供参考”“不必一致”时，不重复询问相似度。
4. 收集用户明确要求保留或排除的视觉元素。Logo、真实文案、人物、照片、专有插画、专有字体和一次性构图默认不进入风格包。
5. 名称、`style_id` 和类别缺失时可以提出合理候选；在展示 Brief 前只读取 `registry.json` 的 ID/元数据，确认 `style_id` 使用小写连字符且未重复。此时不读取现有 scaffold，避免风格提炼被既有实现锚定。
6. 保持现有双媒介契约：注册风格包默认同时包含 Web 与 PPT scaffold。用户明确要求改变该能力边界时，先说明这会改变当前 registry 契约。

### Stage 2 — Reference Extraction

存在参考材料时完整读取并执行 [`../style-reference-extraction.md`](../style-reference-extraction.md)。

- 单图只能证明当前画面的可见规律；响应式、动效、复杂组件和其他页面类型必须标记为 `Inferred` 或 `Unknown`。
- PPT/PPTX 必须检查整套页面、主题、母版和重复版式。优先使用环境中的演示文稿读取/渲染能力生成全页联系表，并区分跨页规律与单页特例；不得只看封面或第一页。
- 多个参考相互冲突时，分别记录证据和冲突，不自行混成一个无依据的折中风格。
- 此阶段只产出 Style Brief，不创建正式风格目录、完整 scaffold、preview 或 registry 记录。

没有视觉附件时，根据用户的文字方向生成同结构的 Style Brief，并将无法从材料观察的结论标记为 `Inferred`。

### Stage 3 — Style Brief Confirmation

向用户展示精简确认摘要：

- 一句 Style Essence。
- 3–6 个 Core Visual DNA。
- `Preserve / Adapt / Exclude / Unknown`。
- 关键推演与置信度。
- 拟议名称、`style_id` 和类别。

用户确认后才进入完整实现。若用户在请求中明确授权自主完成或跳过中间确认，可以继续，但仍必须保留 Style Brief 和参考边界，不能把“无需确认”解释为“允许复刻”。

### Stage 4 — Style Architecture

将已确认 Style Brief 转换为媒介无关的设计系统：

1. `Core Visual DNA`：Web/PPT 共享的颜色角色、字体气质、形状、材质、密度与标志性图形语法。
2. `Web Adaptation`：长文流、响应式网格、环境层、承托层、交互和移动端降级。
3. `PPT Adaptation`：16:9 安全区、封面/章节/正文/数据/对比等页型、投影可读性、翻页、全屏和打印。
4. `Reference Boundary`：原始内容和资产不进入模板；推演出的规则必须可以解释且可被新内容复用。

完成洁净提炼后才与 `registry.json` 中的现有风格摘要比较。若新方向与现有风格高度重合，说明差异并判断应修改已有风格还是建立新 `style_id`；不得先读某个既有 scaffold 再反向套到参考材料上。

### Stage 5 — Representative Proofs

在扩展完整组件前制作低成本方向小样：

- Web：至少包含 Hero、长正文和一个数据/比较类组件的代表区块，并展示桌面与移动端行为。
- PPT：至少包含封面页、正文页和数据页，固定为 16:9。
- 使用与参考材料主题无关的示例内容，验证风格可以泛化，而不是只适配原图或原 PPT。
- 小样只验证方向，不要求此时完成 18 个语义组件，也不得提前注册。

### Stage 6 — Visual Confirmation

确认以下四点后再扩展完整风格包：

1. 小样与参考材料属于同一视觉家族，但没有逐页或逐构图复刻。
2. Web 与 PPT 共享 Core Visual DNA，同时各自符合媒介规律。
3. 字体气质、色彩比例、密度、材质和装饰强度符合预期。
4. 替换为无关内容后，视觉语言仍稳定且可读。

用户明确授权跳过此确认门时可以继续，但 Stage 8 仍必须执行视觉 QA，不得以自动化脚本代替视觉判断。

### Stage 7 — Full Package Generation

按本文第 4 节实现完整 `design.md`、Web/PPT scaffold 和 preview。Web scaffold 用 18 项语义组件验证覆盖能力；实际生成页面仍按原文结构按需选用。不得从参考材料或其他风格包复制整页 DOM/CSS 后换色冒充新风格。

### Stage 8 — Quality Gate

质量门包含四层，任何一层都不能由另一个层次替代：

1. **结构检查**：必需文件、`design.md` 模块、Web 18 组件、PPT 页型和拟议 registry 元数据完整。
2. **运行检查**：Web 响应式与离线资源可用；PPT 满足 16:9、键盘翻页、全屏、打印和安全边距。
3. **视觉检查**：渲染桌面/移动 Web 与 PPT 代表页，检查文字溢出、遮挡、对比度、资源缺失和视觉层级。
4. **泛化与参考边界**：使用无关内容验证可复用性，并检查未带入原文、Logo、品牌资产、专有插画或一次性构图。

注册前使用 `python3 references/scripts/validate_previews.py --style-dir references/styles/<style_id>` 验证草稿 preview。`validate_registry.py` 是注册后的全局一致性检查，不能在未注册目录上提前运行。所有机械脚本都不验证 scaffold 行为、跨媒介一致性或视觉质量，因此不能单独作为完成证据。

### Stage 9 — Registration

只有 Stage 8 全部通过后才执行注册集成：在 `registry.json` 中写入新风格条目（含 `visualTraits` 与 `scenarios`），并运行 `python3 references/scripts/sync_registry.py` 自动同步 `SKILL.md` 风格表。Mermaid 主题配置已完全内聚在自身 `design.md` 与 `scaffold-web.html` 中，无需手动修改全局 `shared-components.md`。画廊从注册表自动生成卡片，不手工向 `style-gallery.html` 添加单个风格。随后运行全局 `validate_registry.py` 与 `validate_previews.py`；任何失败都表示注册未完成，必须修正后再交付。

## 3. 常见失败模式

| 错误 | 正确处理 |
|---|---|
| 因输入是 PPT 就进入 Generate PPT | 根据最终产物路由；创建风格包始终进入 Extend |
| 把“参考”理解为复刻 | 默认 Inspiration，提炼可迁移规则并明确 Exclude |
| 只看单图或 PPT 首页就定义完整系统 | 标记未知；PPT 检查跨页重复规律和母版/主题 |
| 先生成 18 组件再让用户看方向 | 先确认 Style Brief 和代表性小样 |
| Web CSS 直接缩放成 PPT | 共享 Core DNA，分别定义 Web/PPT Adaptation |
| 在注册前运行只支持全局 registry 的校验 | Stage 8 用单目录 preview 与本地检查；Stage 9 集成后跑全局校验 |
| 两个 validator 通过就宣布完成 | 机械校验之外还要完成运行、视觉和泛化检查 |

## 4. 风格包实现规范

> **核心哲学：双轨制设计架构（Dual-Track Design Architecture）**
> 1. **统一的是信息语义能力（Shared Semantic DNA）**：所有风格共享一套 18 个语义组件（Hero, Stats, Admonition, Flowchart, Timeline, FAQ 等）。创建新风格时，脚手架必须按标准 5 阶段顺序完整展示这些组件，以验证风格覆盖能力；实际页面生成则保留原文结构，按内容语义选用组件，不要求固定阶段、顺序或组件组合。Quick Nav/Progress 是可选增强。
> 2. **强制具象化的是风格灵魂（Strict Concrete Visual Contracts）**：杜绝“过度抽象塌陷”。每种风格必须明确其专属的**空间纵深架构**、**环境背景层规则**、**材质色谱**与**强制结构契约**，绝不允许 AI 在生成时发生偷懒与机械降级。

---

### 4.1 风格空间纵深架构与四大形态原型 (Architectural Archetypes)

“三层画布架构”是**空间关系与职责解耦的认知模型**，而非千篇一律的固定模具。它赋予新风格 100% 的创意自由，新风格可以根据美学诉求自由选择以下 4 大空间形态之一：

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ Layer 0: Ambient Canvas (环境背景层 - 视口环境与情绪张力)                    │
│ • 可繁复：全屏 3D 管道 SVG / 呼吸流光 / Sunburst 射线 / 极光粒子           │
│ • 可极简：纯色留白 (Flat Void) / 1px 极淡点阵 / 细线网格                  │
├─────────────────────────────────────────────────────────────────────────┤
│ Layer 1: Carrier Board (承托画板层 - 长文与环境的交互关系)                  │
│ • 悬浮画板型：磨砂玻璃通体画板 (<main class="main-sheet">) / 奶油看板     │
│ • 直铺沉浸型：Direct Canvas (无额外画板，正文直接平铺于全景背景)          │
│ • 分栏便当盒型：Sticky 侧边栏 + Bento 模块化网格                          │
│ • 无界杂志型：大跨度流体非对称版面                                       │
├─────────────────────────────────────────────────────────────────────────┤
│ Layer 2: Semantic Components (具象组件层 - 差异化材质与排版)                │
│ • 贴纸便签 / 3D 展柜 / 粗野线框 / 瑞士极简排版 / 高透毛玻璃                │
│ • 严格根据该风格专属语言渲染，严禁 AI 私自漂白为通用白卡片                  │
└─────────────────────────────────────────────────────────────────────────┘
```

### 📐 常见空间形态原型示例：
1. **浮动展台型 (Suspended Carrier)**：如 `play-tubular`、`pixel-pop`、`warm-craft`。背景有极强的视觉张力（3D 彩管/流光/波普光芒），正文收敛在 Layer 1 的一体化画板中，兼顾冲击力与阅读专注。
2. **直铺沉浸型 (Direct Immersive Flow)**：如 `industrial-dark`、`brutalist-acid`。Layer 0 与 Layer 1 合一，长文直接平铺在全景暗黑 CAD 网格或纯白纸面，**无需强制包裹额外的悬浮白板**。
3. **分栏便当盒型 (Split / Bento Grid)**：如 `cyber-bento`。Layer 1 演化为左侧固定导航看板 + 右侧 Bento 盒流式排布。
4. **瑞士平面与无界杂志型 (Swiss Editorial)**：追求极致排版与巨大字阶，Layer 0 为纯白/纯黑极简，Layer 1 为无界版面，依靠极致的排版韵律与网格构建秩序。

> **核心原则**：你可以把 Layer 1 声明为 `Direct Flow (直铺无画板)`，也可以把 Layer 0 声明为 `Flat Solid (纯色留白)`。**关键在于这是你在 `design.md` 中主动做出的美学声明，而不是被 AI 偷懒阉割遗漏！**

---

### 4.2 模板目录标准结构

在 `references/styles/` 下创建以风格命名的子目录（小写中划线，如 `references/styles/cyber-bento/`）。该目录下必须包含：

1. **`design.md`**：该风格的完整设计语言规范，必须严格遵循本文第 4.4 节的标准架构，包含不可剥离的 **“风格自有布局契约（Style-Owned Layout Contract）”**。
2. **`scaffold-web.html`**：该风格的 Web 单文件全组件脚手架，必须按标准 5 阶段顺序完整展示空间架构与 18 个语义组件，以验证风格覆盖能力；实际交付按原文语义选用，不要求全量出现。
3. **`scaffold-ppt.html`**：该风格的 16:9 演示文稿脚手架，必须满足共享 [`../ppt-output-contract.md`](../ppt-output-contract.md) 的舞台、翻页、全屏和打印契约。
4. **`preview.svg`**：该风格专属的 `400×240` 严格 4 层隔离坐标系矢量源文件。
5. **`preview.png`**：由 `preview.svg` 导出的 `800×480` 高清位图，用于对话卡片内嵌预览与画廊展示。

---

### 4.3 脚手架构建与防退化法则 (Anti-Degradation Rules)

创建新风格脚手架时，必须遵循以下铁律：

1. **完整组件覆盖（模板契约底线）**：
   - 新风格脚手架必须完整覆盖 `references/shared-components.md` 中定义的 18 个语义组件，并按其标准 5 阶段参考顺序展示，绝不允许删除任何组件；第 19 项 Quick Nav/Progress 仅按需启用。该要求只适用于创建或扩展风格的脚手架，不是实际文章的内容清单。
2. **明确声明空间架构**：
   - 若风格采用“浮动展台型”，必须在 `<body>` 顶部提供 Layer 0 背景代码，并包裹 Layer 1 画板；
   - 若风格采用“直铺沉浸型”或“瑞士杂志型”，必须在 CSS 中明确声明全景平铺规则与排版网格。
3. **严禁机械漂白材质**：
   - 严禁将每种风格独特的卡片材质（如多彩便签、半透明磨砂、彩色微透底、深浅交替面板、粗野黑框）抹杀为千篇一律的普通纯白方块（`#FFFFFF`）。

---

### 4.4 制定核心 Design 规范 (design.md 必须包含的标准模块)

编写新风格的 `design.md` 时，必须严格遵循以下结构，绝不允许敷衍简写或缺失关键具象代码：

### 1. `## 1. Visual Theme & Atmosphere` (视觉哲学与空间维度)
- 核心设计哲学、空间隐喻、情绪基调。
- 详细说明所选取的空间形态原型（浮动展台 / 直铺沉浸 / 分栏便当 / 瑞士杂志）。
- 记录经确认的 3–6 个 Core Visual DNA，以及参考驱动风格的 `Preserve / Adapt / Exclude` 边界；规范不得依赖原始文案或资产才能成立。

### 2. `## 2. Color Palette & Tokens` (色彩体系与专属色谱)
- 核心界面色表（Canvas, Surface, Text, Border）。
- 专属多色通道表（如 Play Tubular 的 5 大能量渐变、Warm Craft 的 6 种粉彩便签名册、Obsidian Cyan 的电光冷蓝）。
- 完整的 CSS `:root` 变量代码块。

### 3. `## 3. Style-Owned Layout Contract` (风格自有布局契约)
- **必须提供可直接执行的顶层结构说明与 HTML/SVG/CSS 示例**，或明确声明采用 `Direct Flow` / 无环境层等无额外容器结构。
- 若风格使用 Layer 0 环境层或 Layer 1 顶层容器，给出完整代码；若不使用，也必须明确声明，避免生成时被通用模板补入画板或背景。
- 分别声明 `Web Adaptation` 与 `PPT Adaptation`：二者共享 Core Visual DNA，但空间结构、密度、响应式和固定 16:9 页型按媒介实现，不做机械缩放。

### 4. `## 4. Typography Scale & Rules` (排版规范与全字阶量化表)
- 字体栈规范（Display / Serif / Sans / Mono）。
- 全字阶量化表格（包含 `Element`, `Class / Tag`, `Size`, `Weight`, `Line Height`, `Letter Spacing`, `Role`）。
- 标题排版规则（如负字距收紧、中文主动语义折行等）。

### 5. `## 5. Signature Component Patterns` (核心特征组件规范与具象 DOM)
- 给出 3~5 个最具风格辨识度的真实组件 HTML/CSS 代码片段（如带渐变单位的数据卡片、带顶部悬浮彩条的数字卡片、扇形微倾便签、专属时间轴胶囊、特色提示框等）。
- **必须包含具象的内联/类名样式**，避免 AI 在生成时发生“抽象塌陷”。
- 组件必须重新构图并可承载无关内容，不得复用参考材料的原始文案、Logo、插画或单页几何。

### 6. `## 6. Mermaid Theme Configuration` (在线增强与离线降级专属配置)
- 给出该风格专属的 `mermaid.initialize({ theme: 'base', themeVariables: { ... } })` 完整代码块。
- 必须与风格的 Color Tokens（画布底色、卡片主色、主文字色、边框色与主信号线色）严格对齐，禁止直接使用 Mermaid 默认主题。

### 7. `## 7. Do's and Don'ts` (7 项金律与 7 项严禁红线)
- **7 项核心金律 (Do's)**：必须做到的标志性手法（如必须保留专属空间骨架、必须使用专属动效、必须保持高清晰度正文等）。
- **7 项严禁红线 (Don'ts)**：明确列出绝对禁止的退化反模式（如严禁私自删除背景图层、严禁将多彩便签漂白为纯白卡片、严禁混淆暗黑与浅色基调等）。

---

### 4.5 绘制专属微缩视觉名片 (preview.svg + preview.png)

为确保用户在对话流中直观感知风格的真实质感，必须严格遵循 **4 层隔离坐标系（400 × 240）**：

```text
┌─────────────────────────────────────────────────────────────┐ (0, 0)
│ [背景画布] <rect width="400" height="240" rx="8" ... />     │
│                                                             │
│ ─── Tier 1: Eyebrow 标头层 (y: 12 ~ 30) ─────────────────── │
│ • 胶囊高度 18px, 文本基线 y=12..13                           │
│                                                             │
│ ─── Tier 2: 风格大标题层 (y: 44 ~ 60, 基线固定 y=58) ──────── │
│ • 中文标题 font-size="16", 英文副标 font-size="9"           │
│                                                             │
│ ─── Tier 3: 灵魂组件卡片层 (y: 72 ~ 192, 固定高度 120px) ───── │
│ • 展示该风格最具辨识度的卡片（如 3D彩管、粉彩便签、高光玻璃等）│
│                                                             │
│ ─── Tier 4: 页脚与色盘层 (y: 206 ~ 226, 基线固定 y=220) ─────── │
│ • Style ID 与 14px 专属色盘圆点                             │
└─────────────────────────────────────────────────────────────┘ (400, 240)
```

### 🚫 Preview SVG 核心避坑红线 (Anti-Patterns)
在绘制 `preview.svg` 时，严禁出现以下破坏视觉层级与导致渲染破损的常见失误：
1. **严禁在圆角卡片顶部叠加热键矩形直条（No unclipped top accent bars）**：
   - 严禁使用 `<rect x="0" y="0" width="364" height="2~3" ... />` 直接贴在 `rx > 0` 的圆角卡片顶端。
   - **后果**：直角切圆角会导致两端突兀溢出，且顶条与内部内容之间留白过大，在视觉上极其容易被用户误认为是**未完成的进度条（Progress Bar）或悬浮滚动条**。
   - **正确做法**：卡片质感依靠整体 `stroke` 边框、外层柔和 `filter` 投影或内缩的高光微线（如 `line x1="16" x2="348"`）呈现，保持卡片干净一体。
2. **严禁标题基线与卡片顶部安全间距不足（Safe vertical clearance >= 12px）**：
   - Tier 2 Title 基线（推荐 `y=56~58`）与 Tier 3 Card 起始（`y=72`）之间必须预留至少 12~16px 的净空。
   - **后果**：间距不足时，中文字体渲染时的 Descender（下延笔画）会直接与卡片或其投影发生碰撞，导致标题文字底部被横向切掉一截。

### ⚡ 强制执行的自动化验证
生成新风格的 `preview.svg` 后，导出 `800×480` 的 `preview.png`，并运行验证脚本：
```bash
python3 references/scripts/validate_previews.py
```
验证脚本已内置 AST 结构检查、坐标范围校验、标题与卡片安全间距检查、PNG 尺寸检查以及“圆角卡片未裁切顶条”反模式检测。注册前使用 `python3 references/scripts/validate_previews.py --style-dir references/styles/<style_id>` 检查草稿；完成注册集成后再运行全局 `validate_registry.py` 与 `validate_previews.py`。机械脚本不能替代浏览器渲染、PPT 行为、视觉一致性和泛化检查。

### 离线资源契约

- scaffold 可以保留在线字体和 Mermaid 增强，但不得把它们当作离线运行的必要条件。
- 交付前运行 `python3 references/scripts/bundle_offline.py <input.html> -o <output.html>`，将本地图片/CSS 内联，并为 Mermaid 生成静态 SVG fallback。
- 默认 hybrid 模式在线尝试完整字体和 Mermaid；`--strict` 模式移除外部增强，只保留系统字体和静态图表。
- 默认使用系统字体 fallback；如需固定品牌字体，准备 JSON 字体映射并传入 `--font-map`，按需内置 WOFF/WOFF2 以控制包体大小。例如：`{"IBM Plex Mono":[{"path":"fonts/IBMPlexMono-Regular.woff2","weight":400}]}`。

---

## 5. 最终并网注册 (Final Registration)

1. **注册前提**：Style Brief 与代表性小样已确认（或用户明确授权跳过确认），完整风格包已经通过 Stage 8 的四层质量门和单目录 preview 校验。
2. **注册集成**：在 `references/styles/registry.json` 中添加新风格的 `id`、名称、目录、分类、核心视觉特征（`visualTraits`）与推荐场景（`scenarios`），并运行 `python3 references/scripts/sync_registry.py` 自动同步 `SKILL.md` 风格表。Mermaid 配置已内聚于 `design.md`，无需维护全局映射表。
3. **画廊来源**：画廊从注册表自动生成卡片、预览链接和“使用此风格”的复制内容；不得手工修改 `references/style-gallery.html` 添加单个风格。
4. **全局复验**：运行 `validate_registry.py` 与不带 `--style-dir` 的 `validate_previews.py`。只有两项通过且 Stage 8 的视觉证据仍成立时，注册才完成。
