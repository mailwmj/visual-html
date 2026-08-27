# Visual HTML 路由规则

本文件是 Visual HTML 的执行路由权威。一次请求先选择一个顶层产物生命周期，再加载该 route 的运行时说明；风格是 route 内的 profile，画廊、离线打包和质量检查是按条件触发的 stage。

## 路由纪律

1. **先按输出生命周期路由，后读细节**：先判断用户最终要的是 Web、PPT，还是一个可复用风格包，再读取对应 route 和已触发的支持文档。图片、截图或 PPT/PPTX 作为输入材料时不决定 route。
2. **一个请求一个顶层生命周期**：Web、PPT、风格扩展分别拥有自己的输出边界；不要把多个 route 合并成一条未定义流程。
3. **显式扩展意图优先**：只要用户明确要求创建、修改、扩展或注册视觉风格包，就进入 Extend Style Pack；参考材料只是该 route 的输入，不得因为附件是 PPT 而改走 Generate PPT，也不得因为附件是图片而改走 Generate Web。
4. **生成风格不是顶层 route**：在 Generate Web / Generate PPT 内，已注册风格、参考材料和自由设计都只是 style profile。确定 `style_id` 后，只读取目标风格的 `design.md` 和对应脚手架。
5. **辅助流程不是顶层 route**：画廊浏览/选择、参考提炼、离线 bundling、Mermaid fallback 和质量检查只在所属 route 的条件满足时触发。
6. **在当前 route 内补齐信息**：Extend route 可以在 Intake 中提议名称、`style_id`、类别和参考边界；这些信息缺失时不得静默换成 Generate route。只有缺失选择会实质改变范围或行为时才询问用户。
7. **路由已确定时不展示实现路径菜单**：只有输入确实无法区分 Web 与 PPT，或用户没有给出必要选择时，才提出一个最小澄清问题。

## 顶层 route 矩阵

| Route | 请求形状 | 前置条件 | 运行时 authority | 输出契约 |
|---|---|---|---|---|
| **Generate Web** | 要求单文件网页、响应式 HTML 或长文网页 | 原文/结构化内容可用；媒介明确为 Web；风格可在进入 route 后通过选择 stage 确定 | [`routes/generate-web.md`](routes/generate-web.md) | 可独立打开的单文件 HTML；需要离线交付时再生成 bundle |
| **Generate PPT** | 要求 16:9 PPT、演示文稿或幻灯片页面 | 原文/结构化内容可用；媒介明确为 PPT；风格可在进入 route 后通过选择 stage 确定 | [`routes/generate-ppt.md`](routes/generate-ppt.md) | 16:9 演示文稿 HTML/PPT 交付物，保留结论、关键指标和出处 |
| **Extend Style Pack** | 明确创建、修改、扩展或注册视觉风格包；输入可为文字、图片、截图或 PPT/PPTX | 已有可解释的视觉方向或参考材料；名称、`style_id` 和类别可在 Intake 中提议并确认 | [`routes/extend-style-pack.md`](routes/extend-style-pack.md) | 经 Style Brief、代表性小样、双媒介实现和质量门验证后注册的完整风格包 |

只想查看或选择风格时，进入现有的风格选择 stage，不生成产物，也不把复制选择文本当作生成完成。相关行为仍由 [`SKILL.md`](../SKILL.md) 的第一步和 [`style-gallery.html`](style-gallery.html) 定义。

## Profile 与 stage

### Style profile

- 已注册风格：从 `references/styles/registry.json` 读取候选；锁定 `style_id` 后读取该目录的 `design.md` 和目标媒介脚手架。
- 参考材料单次生成：仅当用户要当前 Web/PPT 产物时使用；默认提炼可迁移的视觉规律，不复制原内容、品牌资产或一次性构图。Web 从 [`_base-scaffold-web.html`](_base-scaffold-web.html) 建立新结构，PPT 遵循 Generate PPT route。
- 自由设计：使用原文优先的语义组件映射和 route 约束，不读取无关风格包。

### Conditional stages

| Stage | 触发条件 | 所属 route | 规则来源 |
|---|---|---|---|
| Style selection | 风格未明确，用户需要候选预览或画廊 | Generate Web / Generate PPT | `SKILL.md` 第一步、`style-gallery.html` |
| Reference extraction | Extend 请求包含图片、截图或 PPT/PPTX，或用户明确要求从参考材料提炼风格 | Extend Style Pack | `routes/extend-style-pack.md`、`style-reference-extraction.md` |
| Offline bundle | Web 需要独立离线交付，或用户明确要求 strict | Generate Web | `routes/generate-web.md`、`scripts/bundle_offline.py` |
| Quality gate | 任何生成或风格扩展即将交付 | 当前 route | `SKILL.md` 质量清单、目标风格 `design.md`、扩展校验脚本 |

## 路径与加载边界

- 文档中的 Skill 资源路径均相对于包含 `SKILL.md` 的 Skill 根目录解析；Markdown 链接仍按链接所在文件的目录解析。执行命令前将资源路径解析为绝对路径，不以当前工作目录推断 Skill 根目录。
- 路由文档只指向它真正需要的支持文档。没有被当前请求触发的媒介、风格或 stage 不进入上下文。
- `registry.json` 是风格发现的唯一机器真相源；目录存在但未注册的风格不出现在候选列表中。
