# Generate PPT Route

本文件只在顶层 route 已确定为 **Generate PPT** 时读取。通用意图分析、风格选择和语义组件规则仍由 [`SKILL.md`](../../SKILL.md) 负责；舞台、交互和打印的共享契约位于 [`../ppt-output-contract.md`](../ppt-output-contract.md)。

## 前置条件

- 已有长文本或可转换为演示结构的用户内容。
- 输出媒介已确定为 16:9 PPT；若同时要求 Web 和 PPT，先询问一个媒介区分问题。
- 风格已明确时锁定一个 `style_id`；风格未明确时，先运行现有风格选择 stage，再读取目标风格文件。用户也可以明确选择自由设计或参考材料启发的单次生成；若用户要求创建或注册可复用风格包，应返回路由层进入 Extend Style Pack。

## 加载集合

根据已确定的 style profile 选择**恰好一个**加载分支：

- **已注册风格**：读取目标 `style_id` 的 `design.md` 和 `scaffold-ppt.html`；不要读取目标 Web 脚手架或其他风格规范。
- **参考材料单次生成**：读取 [`_base-scaffold-ppt.html`](../_base-scaffold-ppt.html) 建立洁净 16:9 舞台结构，不读取任何已注册风格 scaffold；根据 `SKILL.md` 的 Inspiration 边界和本 route 的 16:9 契约转译可迁移视觉规律。
- **自由设计**：读取 [`_base-scaffold-ppt.html`](../_base-scaffold-ppt.html)，按原文语义和本 route 约束建立新视觉系统，不读取无关风格包。

所有 profile 都必须读取并执行 [`ppt-output-contract.md`](../ppt-output-contract.md)。需要共享 DOM 语义时读取 [`shared-components.md`](../shared-components.md)。若内容包含 Mermaid，仍按 `SKILL.md` 的共享离线 fallback 契约触发对应 bundler。

## 生成契约

- 执行共享 `ppt-output-contract.md`，并使用目标 profile 的视觉骨架；单页只保留一个核心论点。
- 可以压缩版面，但必须保留结论、关键指标和出处；被压缩的细节放入附录、备注或详细页。
- 生成完成后按 [`SKILL.md`](../../SKILL.md) 的通用质量清单和目标风格专属清单验收。

## 完成条件

只有在所有幻灯片均已生成、共享 PPT 输出契约、通用质量清单与风格专属清单均通过后，才算 route 完成。
