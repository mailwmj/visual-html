# PPT Master 导航结构分析

> 研究日期：2026-08-26  
> 上游基线：`hugohe3/ppt-master` 提交 `ebd74d1f1d61a686f0f80e10abde5029fc4beeca`（浅克隆核对）  
> 研究范围：入口 `SKILL.md`、`workflows/routing.md`、`workflows/index.md`、失败恢复治理，以及当前 `visual-html` 工作树的导航/注册/验收文档。本文不把上游实现当作当前项目已实现能力。

## 结论摘要

PPT Master 值得借鉴的是一层**执行编排协议**，而不是它的 PPT 专用文件数量：

1. 用一个单独的路由权威文件把“请求形状 → 唯一顶层生命周期 → 前置条件 → 输出契约”写成矩阵，避免模型在已经确定意图后继续提供实现路径菜单。
2. 把顶层 route、profile、stage、governance 分层；入口只做 bootstrap 和选择，具体步骤由被选中的 runtime 负责。
3. 用触发条件驱动按需加载，并把加载集合登记到可审计 manifest；索引只负责发现，不让运行时扫描目录或模糊猜路径。
4. 将阻塞门、失败恢复和 resume pointer 写成持久化契约，失败时回到拥有该产物的阶段，而不是静默降级。

当前 `visual-html` 已经具备注册表、五步工作流、目标风格按需读取和质量清单；最有价值的增量是补一份轻量 `routing.md` 与阶段状态/恢复约定。无需复制 PPT Master 的全量 `workflows/`、角色系统或大型审计 manifest。

## 上游导航设计（有源码证据）

### 1. 单入口先固定路径，再固定运行时

上游入口要求保留宿主提供的绝对 `SKILL_DIR`，命令按绝对路径执行；随后依次读取入口、运行完整性守卫、读取 `workflows/routing.md`、选择**恰好一个**顶层 route/profile，最后只读该 runtime 及其触发的支持文档。[`SKILL.md` 第 25–41 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/SKILL.md#L25-L41)

这使导航顺序成为可验证的不变量：先解析路径，后执行命令；先路由，后加载细节；未选中的 runtime 不应进入上下文。

### 2. 路由矩阵以 artifact lifecycle 为边界

`routing.md` 把“一次请求只进入一个 artifact lifecycle”定义为硬规则，并明确支持文档不是顶层 route；前置条件缺失时报告并停止该 route；只有真正歧义时才问一个 discriminator 问题；已被矩阵确定的请求禁止展示 route-choice 菜单。[`routing.md` 第 15–25 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/workflows/routing.md#L15-L25)

顶层矩阵进一步同时记录请求形状、权威文件、前置条件、mutation model 和 output contract；生成 PPTX 下再以 profile/stage 条件细分 image-to-pptx、beautify、quick、topic-research、chart/visual review 等分支。[`routing.md` 第 29–80 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/workflows/routing.md#L29-L80)

### 3. Route、profile、stage、registry 的职责分离

`workflows/index.md` 明确自己是 maintainer-only inventory，运行时不消费；它单列四个顶层 route，再单列 profile、template child workflow、research/quality/editor/post-processing stage 和 governance 文件，并要求维护时同步 `prompt_audit_manifest.json` 的 load sets。[`workflows/index.md` 第 5–8、9–46 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/workflows/index.md#L5-L46)

这种目录不是“把所有文档都放平”，而是让每个文件有单一拥有者：route 拥有生命周期，profile 处理同一生命周期内的变体，stage 处理可复用步骤，governance 处理跨 route 的停止/恢复规则。

### 4. 索引驱动发现，禁止运行时目录扫描和模糊解析

模板选择边界要求默认 UI/chat 只读取四个机器索引（Brand/Style/Layout/Deck），不得扫描目录补全目录；裸模板名不解析成本地路径，未注册 workspace 必须由用户提供精确根路径。[`routing.md` 第 141–172 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/workflows/routing.md#L141-L172)

这项约束同时解决可预测性和授权边界：目录存在不等于可选，catalog 中的根路径才是可发现对象。

### 5. 全局停止规则与拥有源恢复

入口的全局纪律要求串行执行、每步先验前置条件、阻塞门必须等待显式确认、禁止跨未关闭阶段捆绑、禁止 speculative execution，并要求失败时修复/重生成拥有源后从声明的指针恢复。[`SKILL.md` 第 61–69 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/SKILL.md#L61-L69)

失败治理文件把规则落到矩阵：必需产物失败会阻塞下一门，方便表面失败可回退到 canonical channel；矩阵记录失败点、是否阻塞、自动恢复、是否需要用户介入和 resume entry；新会话/上下文压缩时只重读完整 Design Spec、lock 和受触发的输入，不重新发明计划。[`failure-recovery.md` 第 7–9、13–29、50–88 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/workflows/governance/failure-recovery.md#L7-L29)

### 6. 按需加载可以被审计，而不只是口头约定

`scripts/prompt_audit_manifest.json` 把 bootstrap 路由集合（入口 + routing）、各 route 的累计集合、条件 stage 的增量集合和 token ceiling 结构化登记，并将维护用索引/README 标记为 runtime exempt。[`prompt_audit_manifest.json` 第 1–16、48–57、967–981 行](https://github.com/hugohe3/ppt-master/blob/ebd74d1f1d61a686f0f80e10abde5029fc4beeca/skills/ppt-master/scripts/prompt_audit_manifest.json#L1-L16)

这不是运行时路由本身，但它让“只加载必要上下文”可被检查，避免文档增多后发生隐性全量读取。

## 与当前 `visual-html` 的对照

以下事实来自当前工作树（存在用户未提交修改；本研究未修改这些文件）：

| 能力 | 当前证据 | 判断 |
|---|---|---|
| 机器可读风格目录 | [`SKILL.md` 第 15–18、38 行](../SKILL.md#L15-L18)；[`references/styles/registry.json`](styles/registry.json) | 已有，且 `registry.json` 已被定义为真相源；可继续强化“索引只负责发现”的边界。 |
| 主流程导航 | [`SKILL.md` 第 55–63 行](../SKILL.md#L55-L63) | 已有五步（意图→预览确认→按需读取→生成→验收），但没有独立的 route matrix 和每路由 mutation/output contract。 |
| 交互确认与条件分支 | [`SKILL.md` 第 65–102 行](../SKILL.md#L65-L102) | 风格推荐、预览、画廊和媒介询问规则较完整；可把“哪些输入跳过哪些确认”提取成路由表，减少长段落中的条件遗漏。 |
| 按需读取 | [`SKILL.md` 第 105–113 行](../SKILL.md#L105-L113) | 已明确只读目标风格 `design.md`/脚手架；尚无可审计的 load-set manifest。 |
| 语义装配与验收 | [`SKILL.md` 第 119–176 行](../SKILL.md#L119-L176) | 已有组件决策树、内容保真契约、骨架契约和双层质量清单；可增加失败点到恢复入口的映射。 |
| 模板扩展 | [`SKILL.md` 第 197–206 行](../SKILL.md#L197-L206) | 已有 SOP 和 registry/preview 验证命令；可将“注册、验证、交付”作为独立 stage，而不是继续堆在入口文件。 |

## 建议借鉴顺序

### P0：新增轻量路由权威

在 `references/` 下新增 `routing.md`（或等价命名），只包含：

| 顶层 route | 触发请求 | 前置条件 | 主要输出 |
|---|---|---|---|
| Web 单文件 | 明确要响应式 HTML | 文本/素材可用 | 单文件 HTML，必要时离线 bundle |
| PPT 16:9 | 明确要 16:9 PPT | 文本/素材可用 | 16:9 页面/PPT 交付物 |
| 风格扩展 | 明确新增/修改风格包 | 遵守 template-extension SOP | 注册后的完整风格包 |
| 风格浏览/选择 | 只想查看或选择风格 | 画廊/Companion 可用 | 选择文本或页面状态，不伪装成生成完成 |

“风格浏览/选择”是交互支持流程，不应与生成 route 互相竞争；若用户已经明确媒介和风格，应直接进入对应生成 route，不再展示 route 菜单。

### P1：把现有五步拆成可引用 stage

保持现有行为不变，只把长篇入口拆为 `intent-match`、`preview-confirm`、`load-style`、`assemble-output`、`quality-gate` 五个 stage 文档。每个 stage 写清输入、产物、阻塞条件、成功状态和下一 stage；入口只负责选择和串联。这样能保留当前简单模型，同时获得 PPT Master 的“单一拥有者”边界。

### P1：为失败和恢复加最小状态契约

无需复制 PPT Master 的复杂项目系统，先为每次生成记录一个小型状态文件（例如 `.visual-html/run-state.json`）：`route`、`style_id`、`medium`、`stage`、`status`、`artifact_paths`、`last_error`。质量校验失败时回到拥有该产物的 stage；上下文中断时从 `stage` 和现有产物恢复，不重新猜测风格或媒介。状态文件应位于项目运行目录，不能成为风格 registry 的第二真相源。

### P2：把目录发现和加载审计结构化

当前 `registry.json` 已适合作为风格 catalog。可增加一个小型 `load-manifest.json` 或验证脚本，检查：入口默认只加载 `SKILL.md` 与 routing；确定 `style_id` 后只加载对应 `design.md`/脚手架；Mermaid、shared-components、Quick Nav 等仅在触发条件满足时加载。验证应报告“加载集合”和“未授权路径”，而不是扫描目录后自动扩展候选。

## 不建议照搬的部分

- PPT Master 的四个顶层 route、多个 profile、角色定义、海量 references 和 token budget 是其 PPTX/OOXML 复杂度的产物；对当前单文件 Web/PPT Skill 会增加导航成本。
- `attribution_guard.py` 这类上游特有完整性门只有在当前项目确实有分发/来源完整性需求时才值得引入；不要因为形式相似而增加启动阻塞。
- 持久化状态应先采用当前项目已有的 `.visual-html/` 运行目录约定，不能未经授权引入新的项目库、模板库或跨项目扫描。

## 验收标准（若落地上述借鉴）

- 相同输入在一次路由判断中只选择一个顶层 route；已明确 route 时不出现实现路径菜单。
- 路由表能列出每个 route 的前置条件、输出和失败恢复入口；缺前置条件会停止并说明原因。
- 未确定风格前不读取全部风格细节；确定后只读取目标风格文件及明确触发的共享模块。
- registry/catalog 是唯一发现入口，裸名称不会被猜成任意本地目录。
- 验收失败不会静默降级；状态能指出当前 stage 和拥有源，恢复后继续同一路由。
- 现有 `SKILL.md` 的风格预览、内容保真、离线 bundle 和风格专属校验行为保持不变。

