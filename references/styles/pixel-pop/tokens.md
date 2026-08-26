# Pixel Pop (日系手绘像素波普) - Design Tokens

## 1. 核心设计理念 (Core Concept)
结合**纯正的日系青春校园风（如《放学后可尔必思》视觉）**与波普艺术，呈现高饱和青春感。风格以纯正的亮蓝、鲜绿、西瓜粉、亮黄为主色调。
视觉核心在于：
1. **层次清晰的背景系统**：全屏高能量辐射光芒（Sunburst）与像素点阵负责全局氛围，正文区域采用**整体浅奶油色看板画布（`--surface-board`）**包裹，隔绝背景噪点，确保长文阅读的专注与舒适。
2. **文字高保真可读性**：正文、标题、数据等所有文字一律采用清晰锐利的抗锯齿矢量排版；**蜡笔滤镜（Crayon Texture）与手绘位移效果严格收敛于点缀要素**（如背景浮动涂鸦、贴纸、装饰线与角标）。

## 2. 色彩字典 (Color Dictionary)
*   **--bg-base**: 青春亮蓝 `#0b45f3` (全屏背景底色)
*   **--surface-board**: 整体看板浅奶油色 `#fcf9f2` (正文区域整体背景容器，隔绝背景干扰)
*   **--surface-card**: 纯白卡片 `#ffffff` (正文内部各组件卡片底色)
*   **--surface-card-alt**: 浅黄高亮 `#fffde6` (选中态/推荐态卡片底色)
*   **--text-main**: 纯黑 `#111111` (正文与粗边框)
*   **--text-light**: 纯白 `#ffffff`
*   **--text-muted**: 次级灰色 `#555555`
*   **--c-green**: 像素鲜绿 `#19d15e` (用于数据、成功提示、重点区块)
*   **--c-pink**: 蜡笔西瓜粉 `#f76a9f` (用于徽章、卡片高光、强调投影)
*   **--c-yellow**: 亮黄 `#ffde00` (用于 Eyebrow、便签条、Tag)
*   **--c-cyan**: 荧光青色 `#43c2f0` (用于局部点缀、边框高光)

## 3. 字体栈 (Typography)
*   **--font-mono**: 像素等宽字体，如 `'Press Start 2P', monospace`（用于短序号 `01`、英文 Eyebrow、短标签与元数据）。
*   **--font-sans**: 清晰圆润的无衬线体，如 `'Varela Round', -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', sans-serif`（用于所有长篇正文、段落与标题，保证 100% 清晰可读）。

## 4. 形状与特有视觉元素 (Shapes & Specific Elements)
*   **正文整体背景看板 (Main Content Canvas)**：`.container` 配备统一的 `--surface-board` 浅色底、`4px` 黑色边框与 `14px 14px 0 #111` 粗实线投影，顶部点缀胶带/便签徽章。
*   **点缀要素专用蜡笔效果 (Crayon Accents Only)**：`filter: url(#crayon-filter)` **严禁**直接作用在包含正文的卡片父容器上；仅用于纯 SVG 涂鸦、背景浮动装饰线（`.decorator`）与装饰笔刷。
*   **波普卡片投影 (Pop Offset Shadows)**：卡片使用 `3px solid #111` 边框与 `5px 5px 0 #111` 或粉/绿色彩色实色偏移投影，营造纯正日系拼贴层级感。
*   **轻微倾斜角标 (Tilted Badges)**：Eyebrow、卡片序号 `num`、标签 `tag` 采用 `-2deg` 到 `-8deg` 的微倾斜，注入青春动感。

## 5. 16项组件视觉契约表 (16 Components Visual Contract)

| 组件名称 | 视觉呈现规则 | 关键类名 / 结构 |
|---|---|---|
| **1. Section Eyebrow** | 亮黄底色便签条或黑粗边胶囊，像素等宽序号，微倾斜 `-3deg` | `.eyebrow`, `.diamond`, `.line` |
| **2. Typography Scale** | 纯黑大字号粗体标题，紧凑行高，正文清晰抗锯齿无滤镜 | `.hero`, `.lead`, `.section-title`, `.body` |
| **3. Technical Spec Row** | 奶油色边框模块，3px 黑实边，大号黑色数值 + 像素等宽单位 | `.spec-row`, `.spec`, `.val`, `.unit` |
| **4. Number Cards** | 纯白卡片，3px 黑色实边 + 5px 西瓜粉/鲜绿实色偏移投影 | `.cards-3`, `.num-card`, `.num`, `.selected` |
| **5. Feature Card** | 纯白卡片 + 鲜绿/西瓜粉 Tag 胶囊 + 媒体预览框（3px 黑色虚线或网点） | `.feat-grid`, `.feat-card`, `.tag`, `.frame` |
| **6. Process Steps** | 纯白卡片，左侧亮黄/粉红大方块序号，右侧标题与正文 | `.steps`, `.step`, `.idx` |
| **7. Comparison Table** | 波普拼贴表格，黑色实线网格，推荐列高亮浅黄底色 + 像素圆点 | `.cmp cmp-matrix`, `.row`, `.cell`, `.selected-col` |
| **8. Metadata Footer** | 顶部 3px 黑色粗线，Mono 字体大写元数据，复古游戏底栏感 | `footer`, `.meta-foot` |
| **9. Admonition** | 浅黄/浅粉实心背景，3px 黑粗边 + 6px 硬投影，左上角波普角标 | `.admonition`, `.admonition.info`, `.admonition.warning` |
| **10. Timeline** | 亮蓝/鲜绿垂直实线，时间节点使用波普彩色像素方块徽章 | `.timeline`, `.timeline-item`, `.timeline-marker` |
| **11. Pros & Cons** | 优势卡片使用鲜绿硬投影，劣势卡片使用西瓜粉硬投影 | `.pros-cons`, `.pro-card`, `.con-card` |
| **12. Stats Grid** | 大号鲜绿/西瓜粉实色数字（48–56px），底部纯黑加粗等宽标签 | `.stats-grid`, `.stat-card`, `.stat-val`, `.stat-label` |
| **13. Flowchart & Mermaid** | 3px 黑色粗边框节点，纯色填充，粗连线。支持纯 SVG 与 Mermaid 引擎（`darkMode: false`, `background: '#FFFFFF'`, `lineColor: '#000000'`, `primaryBorderColor: '#000000'`） | `.flowchart`, `.mermaid-wrapper`, `.node`, `.mermaid` |
| **14. References** | 浅米底色有序列表，等宽复古数字，内嵌回溯锚点 | `.references`, `<ol>`, `<li>` |
| **15. Rich Text** | 纯黑正文，加粗文字使用亮黄/西瓜粉高光马克笔底色划线 | `.rich-text`, `p`, `blockquote`, `ul` |
| **16. FAQ List** | 纯白卡片，3px 黑边，问题加粗带亮黄色 Q 徽章，答案清晰折叠/平铺 | `.faq`, `.faq-item`, `.q`, `.a` |
| **17. Code Block** | 复古街机深蓝底座（`#111424`）+ 3px 黑粗边硬投影 + 亮黄色等宽语言 Badge + 像素明亮语法 Token 高亮 | `.code-block`, `.code-header`, `pre`, `code` |

---

## 6. 专属质检项 (Style Checklist)
*   [ ] 正文区域是否被整体浅色看板容器（`.container`）包裹，有效隔绝背景辐射线条的干扰？
*   [ ] 所有正文、段落、列表、表格文字是否极致清晰，没有任何位移失真滤镜干扰？
*   [ ] 蜡笔与涂鸦滤镜是否严格限制在点缀与装饰性图形上？
*   [ ] 整体是否保留了“亮蓝辐射背景 + 奶油看板 + 高清正文 + 蜡笔像素点缀”的青春日系波普感？
