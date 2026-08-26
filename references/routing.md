# Visual HTML 路由规则

本文件是 Visual HTML 的执行路由权威。一次请求先选择一个顶层产物生命周期，再加载该 route 的运行时说明；风格是 route 内的 profile，画廊、离线打包和质量检查是按条件触发的 stage。

## 路由纪律

1. **先路由，后读细节**：先根据请求形状选择 route，再读取对应的 route 文档和已触发的支持文档。
2. **一个请求一个顶层生命周期**：Web、PPT、风格扩展分别拥有自己的输出边界；不要把多个 route 合并成一条未定义流程。
3. **风格不是顶层 route**：已注册风格、参考图逆向和自由设计都属于生成 route 的 style profile。确定 `style_id` 后，只读取目标风格的 `design.md` 和对应脚手架。
4. **辅助流程不是顶层 route**：画廊浏览/选择、离线 bundling、Mermaid fallback 和质量检查只在所属 route 的条件满足时触发。
5. **缺少前置条件就停在该 route**：说明缺少的输入或选择，不用猜测路径、风格或媒介，也不静默换成另一条 route。
6. **路由已确定时不展示实现路径菜单**：只有输入确实无法区分 Web 与 PPT，或用户没有给出必要选择时，才提出一个最小澄清问题。

## 顶层 route 矩阵

| Route | 请求形状 | 前置条件 | 运行时 authority | 输出契约 |
|---|---|---|---|---|
| **Generate Web** | 要求单文件网页、响应式 HTML 或长文网页 | 原文/结构化内容可用；媒介明确为 Web；风格可在进入 route 后通过选择 stage 确定 | [`routes/generate-web.md`](routes/generate-web.md) | 可独立打开的单文件 HTML；需要离线交付时再生成 bundle |
| **Generate PPT** | 要求 16:9 PPT、演示文稿或幻灯片页面 | 原文/结构化内容可用；媒介明确为 PPT；风格可在进入 route 后通过选择 stage 确定 | [`routes/generate-ppt.md`](routes/generate-ppt.md) | 16:9 演示文稿 HTML/PPT 交付物，保留结论、关键指标和出处 |
| **Extend Style Pack** | 明确新增、修改或注册视觉风格包 | 已确认风格目录与完整扩展需求 | [`template-extension-guide.md`](template-extension-guide.md) | 通过校验并注册的完整风格包 |

只想查看或选择风格时，进入现有的风格选择 stage，不生成产物，也不把复制选择文本当作生成完成。相关行为仍由 [`SKILL.md`](../SKILL.md) 的第一步和 [`style-gallery.html`](style-gallery.html) 定义。

## Profile 与 stage

### Style profile

- 已注册风格：从 `references/styles/registry.json` 读取候选；锁定 `style_id` 后读取该目录的 `design.md` 和目标媒介脚手架。
- 参考图：先做色彩、形状、排版和材质解构，再从 [`_base-scaffold-web.html`](_base-scaffold-web.html) 建立新结构；不得把参考图当作未声明的模板路径。
- 自由设计：使用共享语义骨架和 route 约束，不读取无关风格包。

### Conditional stages

| Stage | 触发条件 | 所属 route | 规则来源 |
|---|---|---|---|
| Style selection | 风格未明确，用户需要候选预览或画廊 | Generate Web / Generate PPT | `SKILL.md` 第一步、`style-gallery.html` |
| Offline bundle | Web 需要独立离线交付，或用户明确要求 strict | Generate Web | `routes/generate-web.md`、`scripts/bundle_offline.py` |
| Quality gate | 任何生成或风格扩展即将交付 | 当前 route | `SKILL.md` 质量清单、目标风格 `design.md`、扩展校验脚本 |

## 路径与加载边界

- 文档中的 Skill 资源路径均相对于包含 `SKILL.md` 的 Skill 根目录解析；Markdown 链接仍按链接所在文件的目录解析。执行命令前将资源路径解析为绝对路径，不以当前工作目录推断 Skill 根目录。
- 路由文档只指向它真正需要的支持文档。没有被当前请求触发的媒介、风格或 stage 不进入上下文。
- `registry.json` 是风格发现的唯一机器真相源；目录存在但未注册的风格不出现在候选列表中。
