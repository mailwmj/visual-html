# Generate PPT Route

本文件只在顶层 route 已确定为 **Generate PPT** 时读取。通用意图分析、风格选择和语义组件规则由 [`SKILL.md`](../../SKILL.md) 负责；大纲提炼与叙事方法由 [`../ppt/outline-framework.md`](../ppt/outline-framework.md) 负责；演讲者模式契约由 [`../ppt/presenter-mode.md`](../ppt/presenter-mode.md) 负责；舞台、交互和打印契约由 [`../ppt/output-contract.md`](../ppt/output-contract.md) 负责。

---

## 核心原则与执行防线

1. **禁止直接跳入写代码**：无论输入是模糊主题还是万字长文，**严禁在未产出大纲并与用户对齐前直接编写 HTML 幻灯片**。
2. **拒绝 Word 投影版**：长文转 PPT 必须经过提炼与降维，主屏只保留单一核心论点与核心图表，论述细节归入演讲提词，密集参数归入附录。
3. **时长约束与 90% 缓冲**：总页数与建议时长严格匹配演讲场景，单页建议时长总和不超过总时长的 90%。

---

## 执行流水线 (5-Stage Pipeline)

```mermaid
flowchart LR
    A["Stage 1<br>输入诊断与澄清"] --> B["Stage 2<br>大纲规划与用户确认"]
    B --> C["Stage 3<br>风格匹配与规范读取"]
    C --> D["Stage 4<br>16:9 HTML 幻灯片编写"]
    D --> E["Stage 5<br>双层质量验收"]
```

### Stage 1: 输入诊断与需求澄清 / 长文提炼
读取并执行 [`../ppt/outline-framework.md`](../ppt/outline-framework.md)：
- **分支 A（仅有主题/模糊想法）**：通过 7 问清单收敛受众场景、分享时长、素材要求与硬约束；按时长推算合理页数（如 15min ≈ 8-10页）。
- **分支 B（已有完整长文/研报）**：执行 4 项降维确认（受众定位、重点章节 vs 略讲章节、时长控制、附录剥离边界）。

### Stage 2: 场景结构匹配与大纲交付确认（强制防线）
1. 从 5 大场景骨架（商业路演、管理层汇报、技术架构、培训教学、原文自由流）中匹配或由用户指定结构模式。
2. 按照 [`../ppt/outline-framework.md`](../ppt/outline-framework.md) 的标准模板输出 Markdown 大纲（包含：页码、`data-slide-id`、章节、页面目的、观众可见大屏要点、演讲者 3-5 条提词要点、建议时长）。
3. **向用户交付大纲并等待确认**。用户提出调整时修改大纲，确认通过后方可进入 Stage 3。

### Stage 3: 风格锁定与规范按需加载
1. **风格确定**：
   - 用户已明确风格时直接锁定 `style_id`；
   - 未指定风格时，结合大纲内容特征推荐 **最契合的 3～5 套风格**，并在同一条回复中通过绝对路径展示 `preview.png` 图片供用户选择。
2. **精准读取目标规范（严禁载入无关风格）**：
   - **已注册风格**：读取目标 `style_id` 的 `design.md` 和 `scaffold-ppt.html`。
   - **参考材料单次生成**：读取 [`../ppt/base-scaffold.html`](../ppt/base-scaffold.html)，按 Inspiration 边界提炼可迁移规则。
   - **自由设计**：读取 [`../ppt/base-scaffold.html`](../ppt/base-scaffold.html)，按原文语义定义新视觉。
3. 所有 profile 均需读取 [`../ppt/output-contract.md`](../ppt/output-contract.md) 与 [`../ppt/presenter-mode.md`](../ppt/presenter-mode.md)。

### Stage 4: 16:9 HTML 幻灯片生成
- 严格按照 Stage 2 确认的大纲逐页生成，单页只保留一个核心论点。
- 遵循 16:9 舞台（`1280×720`）与 5–7% 内容安全区。
- 为每个 `.slide` 赋予对应的 `data-slide-id`，并按需注入 `data-duration` 与 `data-presenter-notes` 元数据。
- 遇到复杂长参数、大段代码或次要清单，一律放入末尾的附录页（`data-slide-id="appendix-*"`）。

### Stage 5: 双层质量验收
1. **PPT 契约验收**：按 [`../ppt/output-contract.md`](../ppt/output-contract.md) 检查舞台安全区、无文字溢出裁切、`ArrowLeft`/`ArrowRight`/`Space`/`F` 快捷键、打印无边距横向 16:9 独立成页。
2. **大纲与提炼验收**：检查是否落实了确认大纲的所有页面、是否包含 `data-slide-id`、大屏文字是否克制。
3. **风格专属验收**：执行目标风格 `design.md` 中的专属视觉清单。

---

## 完成条件

只有在以下条件全部满足时，Generate PPT 路由才算完成：
1. 大纲已在 Stage 2 得到确认；
2. 单文件 16:9 HTML 幻灯片代码已写入；
3. 共享 PPT 输出契约、通用清单与风格专属清单均通过验证。
