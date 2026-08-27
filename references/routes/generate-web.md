# Generate Web Route

本文件只在顶层 route 已确定为 **Generate Web** 时读取。通用意图分析、风格选择和语义组件规则仍由 [`SKILL.md`](../../SKILL.md) 负责。

## 前置条件

- 已有长文本或可转换为长文结构的用户内容。
- 输出媒介已确定为 Web；若同时要求 Web 和 PPT，先询问一个媒介区分问题。
- 风格已明确时锁定一个 `style_id`；风格未明确时，先运行现有风格选择 stage，再读取目标风格文件。用户也可以明确选择自由设计或参考材料启发的单次生成；若用户要求创建或注册可复用风格包，应返回路由层进入 Extend Style Pack。

## 加载集合

根据已确定的 style profile 选择**恰好一个**加载分支：

- **已注册风格**：读取目标 `style_id` 的 `design.md` 和 `scaffold-web.html`；不要读取目标 PPT 脚手架或其他风格规范。
- **参考材料单次生成**：读取 [`../web/base-scaffold.html`](../web/base-scaffold.html) 建立洁净结构，不读取任何已注册风格 scaffold；根据 `SKILL.md` 的 Inspiration 边界只转译可迁移视觉规律。
- **自由设计**：读取 [`../web/base-scaffold.html`](../web/base-scaffold.html)，按原文语义和本 route 约束建立新视觉系统，不读取无关风格包。

需要共享 DOM 语义时读取 [`shared-components.md`](../shared-components.md)。只有离线交付或 Mermaid fallback 被触发时，读取并运行 [`scripts/bundle_offline.py`](../scripts/bundle_offline.py)。

## 生成契约

- 使用目标风格声明的 Layer 0/Layer 1 骨架；页面顺序以原文结构为准，按内容语义选择组件，不套用固定阶段顺序。
- 除非用户明确要求摘要，否则保留原文核心论据、参数、代码和出处；无法映射到特殊组件的内容放入 `rich-text`。
- 默认不加入 `quick-nav` 或 `reading-progress`；只有长文条件或用户明确要求时才启用。
- 容器使用 `.wrap` 限制最大宽度（通常为 `1080px`–`1200px`）并水平居中；移动端在 `@media (max-width: 768px)` 下将网格折叠为单列，对比矩阵提供横向滚动保护。
- 文档超过 4 个章节时，可按用户需求加入阅读进度条和目录导航；导航不是默认组件。
- 交付物必须是可独立打开的单文件 HTML。离线交付运行：

  ```text
  <SKILL_DIR>/references/scripts/bundle_offline.py <input.html> -o <output.html>
  ```

  `SKILL_DIR` 表示包含 `SKILL.md` 的绝对目录；实际执行时用已解析的绝对路径替换它。

- 默认 bundle 使用 hybrid 模式：在线尝试字体/Mermaid，失败时使用系统字体和静态 SVG fallback。
- 完全断网交付使用 `--strict`；需要品牌字体时通过 `--font-map <fonts.json>` 按需内置 WOFF/WOFF2，默认不捆绑字体以控制文件体积。

## 完成条件

只有同时满足以下条件才算 route 完成：输出 HTML 已写入、目标风格专属清单已检查、通用质量清单已检查；触发离线交付时，bundle 命令成功且输出可独立打开。
