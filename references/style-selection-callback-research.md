# 风格画廊选择回传调研

## 结论摘要

当前 `references/style-gallery.html` 既可作为普通本地 HTML，也可由本项目的本地 Companion 服务注入同源事件桥接。普通顶层页面仍没有由 Codex/ChatGPT 官方保证的 API 直接向发起它的原对话发送 `style_id`；自定义 URL scheme、`file://` 回调或任意 URL POST 都不是可靠合同。

“在对话里展示候选风格，点击「查看全部风格」进入完整浏览/全屏页面，再点击「使用」把选择回传对话”对应的可靠范式是 **MCP Apps UI（或 Codex 的 visualize 内联组件）**：

1. 组件由 MCP server 作为 UI resource 提供，并由宿主渲染在对话 iframe 中。
2. 组件按钮通过标准 `ui/message`（ChatGPT 兼容别名 `window.openai.sendFollowUpMessage`）发出一条包含 `style_id` 和媒介目标的后续消息。
3. 若只需让模型在后续轮次读取结构化选择，可另发 `ui/update-model-context`；它更新模型上下文，但不保证立即在对话中显示一条可见消息。
4. 组件本身可以请求 `inline` / `fullscreen` / `pip` 展示模式。`openExternal` 是经过宿主审核后打开外部链接的能力，不等同于“打开 Codex 内置浏览器的任意本地文件”。

因此有两条可验证路径：Codex 本地使用 Companion 服务，通过会话事件文件让 Agent 在下一轮继续对话；跨宿主的组件则使用 MCP App/visualize 的 `ui/message`。两者都不要求用户手动安装 MCP，但前者仍需要 Agent 启动本地服务，后者需要 MCP Server 提供 UI resource。

## 已验证的一手事实

### 1. OpenAI Apps SDK：组件可以向对话发后续消息

OpenAI 官方 Apps SDK 的 “Add UI to your MCP server” 文档说明：组件运行在 ChatGPT 的 iframe 中，通过 MCP Apps bridge（JSON-RPC over `postMessage`）与宿主通信；宿主把 MCP server 返回的 UI resource 渲染到对话旁边。文档给出的能力映射包括：

| 目标 | MCP Apps 标准 | ChatGPT 兼容别名 |
| --- | --- | --- |
| 从 UI 调用工具 | `tools/call` | `window.openai.callTool` |
| 向对话发送后续消息 | `ui/message` | `window.openai.sendFollowUpMessage` |
| 更新模型上下文 | `ui/update-model-context` | 通过 MCP Apps bridge |
| 请求全屏展示 | `ui/request-display-mode` | `window.openai.requestDisplayMode` |

官方兼容别名的签名是：

```js
await window.openai.sendFollowUpMessage({
  prompt: `选择风格：${styleId}；目标媒介：${target}`,
  scrollToBottom: true,
});
```

`prompt` 应包含用户点击确定的稳定标识（例如 `play-tubular`）以及“制作成响应式网页 / 16:9 PPT”等目标，避免模型只能看到一个无法追溯的名称。`scrollToBottom` 可选，默认会滚动到底部。新 UI 应优先使用标准 MCP Apps 方法，`window.openai` 仅作为 ChatGPT 兼容扩展。

来源：

- [OpenAI Apps SDK：Add UI to your MCP server / build a ChatGPT UI](https://developers.openai.com/plugins/build/chatgpt-ui)（“Start with MCP Apps”及 `window.openai` component bridge 表）。
- 可复核的官方聚合文档：[developers.openai.com/apps-sdk/llms-full.txt](https://developers.openai.com/apps-sdk/llms-full.txt)（“Add UI to your MCP server”、“window.openai component bridge”）。

### 2. MCP Apps 标准：`ui/message` 是“发给宿主聊天界面”的协议

MCP Apps 官方规范定义了 View -> Host 的 `ui/message` 请求：

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "ui/message",
  "params": {
    "role": "user",
    "content": {
      "type": "text",
      "text": "选择风格：play-tubular；目标媒介：Web"
    }
  }
}
```

规范要求成功响应为 JSON-RPC result；宿主 **SHOULD** 将消息加入会话上下文，并允许宿主在需要时要求用户同意。因此它是“点击后回到会话”的正式协议路径，而不是页面自行读写父窗口。

同一规范定义 `ui/update-model-context`。它覆盖之前由 View 发出的上下文，宿主可以延迟到下一条用户消息（包括 `ui/message`）再发送给模型，也可以不把它作为可见聊天消息展示。因此它适合保存结构化选择，不应单独替代 `ui/message` 来满足“回传到对话中”。

来源：

- [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview)：iframe 隔离、双向数据流及 `postMessage` 通信说明。
- [MCP Apps specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx)：`ui/message`、`ui/update-model-context` 和宿主行为约定（Requests 小节）。

### 3. 安全边界：独立 tab 与 MCP App iframe 不是同一个运行面

MCP Apps 规范明确指出：View 在 sandboxed iframe 中运行，不能访问宿主页面的 DOM、cookie 或 localStorage；View 与 Host 的所有通信必须走 JSON-RPC `postMessage`。这意味着：

- `window.parent.postMessage` 只有在宿主确实嵌入该 View 时才有意义。
- 普通顶层 `file://.../style-gallery.html` 没有 MCP Apps Host，不会凭空获得 `ui/message` 或 `window.openai`。
- 自定义 `codex://` / `chatgpt://` URL scheme、修改地址栏 query、写入 localStorage 等方式没有官方“回到原对话”合同，不能作为可靠实现。

来源：[MCP Apps overview - Security model](https://modelcontextprotocol.io/extensions/apps/overview#security-model)。

### 4. 本地官方 `visualize` skill 已有同类回传模式

当前安装的官方 visualize skill 对“在对话内的可视化中选择数据并让 Codex 继续处理”写得更直接：交互动作应调用
`await window.openai.sendFollowUpMessage({ prompt, title })`，并把选中的值和请求写进 `prompt`；同一文件还明确指出，导出成 standalone HTML 之前必须替换 `window.openai` 这种 host-only interaction。

这说明“组件内点击 -> 对话后续消息”是已采用的产品模式，同时也反向证明普通独立 HTML 不能假定存在该桥。

来源（本机随 Codex 安装的官方 skill）：

- `/Users/mir/.codex/plugins/cache/openai-bundled/visualize/1.0.22/skills/visualize/SKILL.md`，`Composition` 与 `Exporting an existing visualization` 小节。

### 5. Superpowers 的本地 Companion 模式

`obra/superpowers` 的 `brainstorming` Skill 不依赖 MCP。它随 Skill 提供 `start-server.sh`、`server.cjs` 和浏览器端 `helper.js`：启动脚本创建带随机 key 的 localhost 会话并输出 URL；服务监听 WebSocket/HTTP 事件并将选择写入 `state/events`；Agent 在下一轮读取该文件，再把选择带回对话。`--open` 只是调用平台的 URL launcher，浏览器本身没有访问原对话的权限。

本项目已采用同一数据流的最小实现：

- `references/scripts/style-companion/start-server.sh` 创建会话目录、启动服务并可打开画廊。
- `references/scripts/style-companion/server.cjs` 只允许同源、带会话 key 的事件提交，并写入 `state/events`。
- `style-gallery.html` 检测注入的 `window.visualHtmlCompanion.send`，成功后显示“已提交选择”；未注入时仍使用 MCP bridge 或剪贴板降级。

## 对本项目的落地建议

### 推荐方案：MCP App/visualize 组件作为交互层

保留目前对话里的 PNG 候选预览，同时让“查看全部风格”指向同一个组件的详细视图：

1. 用 MCP server 注册画廊 UI resource（例如 `ui://widget/style-gallery.html`），工具 descriptor 通过 `_meta.ui.resourceUri` 关联它；兼容 ChatGPT 的旧字段是 `_meta["openai/outputTemplate"]`。
2. 组件初始以 inline/carousel 展示 3–5 个候选；“查看全部风格”请求 `ui/request-display-mode` 的 `fullscreen`，或在组件路由中进入完整 11 款画廊。
3. 每张卡片的“使用”按钮先写入本地组件状态，再发 `ui/message`：

   ```js
   async function useStyle(styleId, target) {
     const prompt = `我选择风格 ${styleId}，请制作成${target === "web" ? "响应式网页" : "16:9 PPT 幻灯片"}。`;
     if (window.openai?.sendFollowUpMessage) {
       await window.openai.sendFollowUpMessage({ prompt, scrollToBottom: true });
       return;
     }
     // 兼容其他 MCP Apps host：实现 JSON-RPC ui/message request。
     await rpcRequest("ui/message", {
       role: "user",
       content: { type: "text", text: prompt },
     });
   }
   ```

4. 可选地同时发送：

   ```js
   await rpcRequest("ui/update-model-context", {
     structuredContent: { selectedStyleId: styleId, target },
   });
   ```

   但业务真值仍应由后续工具输入或 MCP server 保存，不能只依赖 widget state/context。
5. 在没有 `window.openai` 的 host 中，保留页面内已选态和可复制的 `style_id`，不要伪装成已经回传对话；对话内确认仍由用户手动发送。

### 暂不推荐：继续使用独立本地 `style-gallery.html`

它可以继续承担“查看全部风格”的浏览器画廊，但只能做到：

- 通过页面内 JS 维护选中风格；
- 在页面上显示 `style_id`，让用户复制/回聊天确认；
- 由 agent/browser 工具在已打开的 tab 中读取页面状态（这是 agent 主动读取，不是页面主动回传）。

当前 Browser skill 文档公开的是 `goto`、tab DOM/Playwright/CUA 操作、WebMCP page-defined tools 等浏览器控制能力；没有把普通网页按钮绑定到“原对话发送消息”的接口。WebMCP 也需要 agent 调用页面声明的工具，不能由普通页面点击自动生成一条会话消息。

来源：

- [Codex in-app Browser skill](https://github.com/openai/codex)（本机安装文档：`/Users/mir/.codex/plugins/cache/openai-bundled/browser/26.818.61809/skills/control-in-app-browser/SKILL.md`）。
- 本机 Browser skill 的 [WebMCP 文档](/Users/mir/.codex/plugins/cache/openai-bundled/browser/26.818.61809/docs/webmcp.md)：页面工具通过 `tab.capabilities.get("webmcp")` 获取并由 agent `tools.call(...)` 调用。

## 验收标准（实现时）

- 对话首条推荐消息仍直接嵌入 `preview.png`，不改成 SVG。
- 文案询问的是“制作成响应式网页还是 16:9 PPT”，而不是“使用 Web 还是 PPT”。
- “查看全部风格”在 Companion 会话中打开带 key 的本地画廊；没有 Companion 时降级为普通画廊，不能声称自动回传。
- 点击“使用”后，Companion 会话将包含稳定 `style_id` 的 `style-selected` 事件写入 `state/events`；MCP Apps 宿主则收到 `ui/message` / `sendFollowUpMessage`。
- 选择回传失败时，页面显示可复制的 `style_id` 和原因，不静默丢失选择。
