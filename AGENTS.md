# AGENTS.md

## 项目定位

这是 `visual-html` Skill 资源库，不是常规前端应用。项目把长文本转换为高保真单文件 Web 页面或 16:9 PPT，并通过可注册的视觉风格包承载具体设计语言。

## 必读入口与路由

- 先读 [`SKILL.md`](SKILL.md)，判断用户意图，再按其中的映射为生成或扩展请求选择且只选择一个顶层路由：
  - Web 产物：[`references/routes/generate-web.md`](references/routes/generate-web.md)
  - PPT 产物：[`references/routes/generate-ppt.md`](references/routes/generate-ppt.md)
  - 新增或修改风格包：[`references/routes/extend-style-pack.md`](references/routes/extend-style-pack.md)
- 只浏览或选择现有风格时停留在选择 stage，不加载顶层路由。意图和路由确定后，只加载该路由实际需要的风格规范、脚手架和支持文档；不要把所有风格文件一次性读入上下文。

## 仓库结构与真相源

- `SKILL.md`：Skill 入口、共享执行流程、内容保真和通用验收规则；风格表格由 `sync_registry.py` 自动从 `registry.json` 同步。
- `references/styles/registry.json`：风格发现的唯一机器真相源。
- `references/styles/<style-id>/`：一个风格包，包含 `design.md`（含 Mermaid 主题配置）、`scaffold-web.html`、`scaffold-ppt.html`、`preview.svg`、`preview.png`，可按需包含 `assets/` 或示例目录。
- `references/shared-components.md`：18 个共享语义组件的内容契约和参考 DOM。
- `references/style-gallery.html`：风格画廊；风格卡片由注册表运行时生成，不要手工添加单个风格。
- `references/scripts/`：预览、注册表、自动同步和离线交付校验工具。

## 开发规则

1. 先理解再修改：查看目标文件、直接调用方和相邻风格的约定；有歧义时优先采用已有且经过校验的模式。
2. 保持源文保真：除非用户明确要求摘要，保留原文标题树、论据、参数、代码、引用和限定条件；无法映射为高级组件的内容放入 `.rich-text`，不要用“更多内容”占位。
3. 风格隔离：锁定 `style_id` 后只读取该风格的 `design.md` 和目标媒介脚手架；不要把风格改造成通用白卡片或混入其他风格的视觉语言。
4. 参考图设计使用 [`references/_base-scaffold-web.html`](references/_base-scaffold-web.html) 重新组织，不把参考图当作未经声明的模板来源。
5. 新增/扩展风格时，按 [`references/routes/extend-style-pack.md`](references/routes/extend-style-pack.md) 完整补齐文件、预览和注册表；可使用 `python3 references/scripts/create_style.py <style-id> --name "风格名"` 初始化标准骨架；`style_id` 使用小写连字符格式，更新 `registry.json` 后运行 `python3 references/scripts/sync_registry.py` 同步 `SKILL.md` 和 `style-gallery.html`。
6. 修改某个风格包的模板或视觉实现时，将风格包作为整体同步维护：凡涉及设计语言、布局或组件契约的改动，都要同步更新该风格的 `design.md`、`preview.svg`，并从最新 SVG 重新导出 `preview.png`；不要只改其中一个文件。完成后运行注册表和预览校验脚本。
7. 开发期间临时制作的视觉方案、页面原型或比稿统一放在 Skill 根目录的 `test/` 文件夹内；正式风格包、注册表和交付资源不放入该目录。
8. 默认使用 ASCII 和仓库现有写法；手工编辑使用补丁方式，避免无关重排或生成物噪声。

## 生成与资源约定

- Web 交付必须是可独立打开的单文件 HTML；响应式规则和离线 bundling 以 Web route 为准。
- PPT 使用固定 16:9 舞台（通常 `1280x720`），每页只保留一个核心论点，并实现翻页、全屏和打印规则。
- 本地图片、CSS 和字体使用可解析的相对路径；离线交付时由 bundler 内联。不要把外部资源当作离线运行的必要条件。
- 预览卡片遵守 `preview.svg` 的 `0 0 400 240` 四层坐标契约，并导出 `800x480` 的 `preview.png`。
- `quick-nav` 和 `reading-progress` 默认不启用，只有用户明确要求或超长文档确有需要时才加入。

## 验收命令

在项目根目录执行，或显式传入 `--project-root`：

```bash
python3 references/scripts/sync_registry.py --project-root . --check
python3 references/scripts/validate_registry.py --project-root .
python3 references/scripts/validate_previews.py --project-root .
```

需要离线 Web 时：

```bash
python3 references/scripts/bundle_offline.py <input.html> -o <output.html>
# 完全断网交付再增加 --strict；只检查、不写文件可用 --check
```

需要浏览风格时，使用自带画廊服务：

```bash
references/scripts/style-companion/start-server.sh --project-dir "$(pwd)" --open
references/scripts/style-companion/stop-server.sh <session-dir>
```

完成前必须确认：修改后的文件已写入、对应路由和风格清单已检查、触发的校验命令通过；若未运行某项检查，要明确说明。
