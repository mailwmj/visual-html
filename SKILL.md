---
name: visual-html
description: Use when the user asks to turn long-form content into a highly designed single-file Web page or 16:9 PPT, or asks to choose or apply a registered visual style pack.
metadata:
  version: "3.0"
---

# Visual HTML — 模块化视觉设计与长文本排版系统

核心使命：**将长篇纯文本（如调研报告、方案白皮书、产品规划、技术总结、深度案例等）转换为结构清晰、高可读性、高辨识度且极具视觉美感的单文件 HTML 页面与 16:9 PPT 演示文稿**。

本 Skill 采用**插件化风格包（Pluggable Style Packs）**架构，在保证长文本排版骨架高可读性与结构一致性的同时，支持多种独立演进的视觉风格。

---

## 0. 执行路由（必读）

本入口负责共享约束和路由启动，不直接承担所有媒介的完整执行步骤。触发 Skill 后，先读取 [`references/routing.md`](references/routing.md)，根据请求形状选择**恰好一个顶层 route**，再读取该 route 的 authority 和明确触发的支持文档：

- **Generate Web**：读取 [`references/routes/generate-web.md`](references/routes/generate-web.md)。
- **Generate PPT**：读取 [`references/routes/generate-ppt.md`](references/routes/generate-ppt.md)。
- **Extend Style Pack**：读取 [`references/template-extension-guide.md`](references/template-extension-guide.md)。

风格是生成 route 内的 profile，不是新的顶层 route；画廊、离线打包和质量检查是按条件触发的 stage。路由确定后，不读取另一个媒介或生命周期的 authority；缺少前置条件时停在当前 route 并说明原因，不猜测风格、媒介或本地路径。

所有 Skill 路径均相对于包含本文件的目录解析。执行命令前将该目录解析为绝对路径，不以当前工作目录作为 Skill 根目录。

---

## 1. 风格注册表 (Style Registry)

当前系统内置的风格包列表以 `references/styles/registry.json` 为机器可读真相源。每种风格均包含独立的 `design.md`、`scaffold-web.html`、`scaffold-ppt.html`、矢量源文件 `preview.svg`，以及供对话直接渲染的微缩视觉名片 `preview.png`：
> 🎨 **查看全部风格**：按下方流程启动本地画廊后，把命令输出的带 `?key=` URL 作为 [查看全部风格] 链接。点击“使用此风格”会复制选择文本，用户可粘贴到当前对话；画廊运行时读取 `registry.json`，需要通过本地画廊服务打开。

| Style ID | 风格名称 | 核心视觉特征 | 推荐场景与关键词 | 微缩预览与风格包 |
|---|---|---|---|---|
| **`industrial-dark`** | **暗黑极客工业风**<br>(Industrial Dark) | 近黑背景 (`#090C0B`) + CAD 极淡网格 + 0–2px 硬边模块 + 信号绿 (`#67E38B`) + 紫色第二通道 | 硬件参数页、产品官网、工程文档、技术说明、极客展示、系统架构 | [预览名片](references/styles/industrial-dark/preview.png)<br>`references/styles/industrial-dark/` |
| **`soft-sky`** | **清透空灵浅蓝风**<br>(Soft Sky) | 浅天蓝渐变背景 + 半透明白色卡片 + 8–16px 柔和圆角 + 同色系高阶蔚蓝 (`#0284C7`) 强调通道 | 包装展示、生活方式产品、消费级硬件、手账/文具、清新雅致向技术页 | [预览名片](references/styles/soft-sky/preview.png)<br>`references/styles/soft-sky/` |
| **`obsidian-cyan`** | **黑曜霓蓝展厅风**<br>(Obsidian Cyan) | 黑曜近黑底色 (`#0B0E14`) + 顶部冷蓝极光 + 悬浮设备模型 + 电光霓蓝 (`#38BDF8`) 信号与标注线 (Callout Pins) + 多步流程徽章 | UI/UX 案例集、移动端 App 展示、数字产品发布、前沿软件功能演示、高科技展厅 | [预览名片](references/styles/obsidian-cyan/preview.png)<br>`references/styles/obsidian-cyan/` |
| **`neon-3d`** | **暗紫流体极光风**<br>(Neon Aurora) | 深邃黑紫底色 + 流体极光光晕 (Fluid Aurora Wave) + 胶片颗粒噪点 (Film Grain) + 3D浮雕高光卡片 + 霓虹紫/洋红通道 (`#A855F7` / `#EC4899`) | 工具集合展示、创意应用、潮酷硬件、潮流设计工作室、流体极光落地页、蒸汽波质感 | [预览名片](references/styles/neon-3d/preview.png)<br>`references/styles/neon-3d/` |
| **`pixel-pop`** | **日系像素波普风**<br>(Pixel Pop) | 青春亮蓝底色 (`#0055ff`) + 浅奶油看板画布 + 粗黑边框与 5px 偏移硬投影 + 悬浮像素碎片与涂鸦 | 青春校园、创意活动、复古游戏、手账拼贴、动漫手绘风展示 | [预览名片](references/styles/pixel-pop/preview.png)<br>`references/styles/pixel-pop/` |
| **`brutalist-acid`** | **先锋撞色海报风**<br>(Brutalist Poster) | 纯白高对比度画布 + 亮粉几何色块 (`#FF4591`) + 荧光青色 (`#00E5CC`) 超大字号标题 + 破坏性排版与紧凑字距 | 艺术展览、独立出版物、实验性排版、先锋设计展示、海报视觉冲击 | [预览名片](references/styles/brutalist-acid/preview.png)<br>`references/styles/brutalist-acid/` |
| **`sunflower-bloom`** | **向日葵暖阳风**<br>(Sunflower Bloom) | 沉静纸质蓝背景 (`#4278A9`) + 米白奶油字 (`#F2EAE0`) + 向日葵明黄 (`#FFC300`) 高亮与强调色 + 粗大排版 | 产品海报、积极向上展示、生机活力传递、纸质文艺风格、团队文化 | [预览名片](references/styles/sunflower-bloom/preview.png)<br>`references/styles/sunflower-bloom/` |
| **`summer-dopamine`** | **夏日多巴胺风**<br>(Summer Dopamine) | 高饱和渐变网格背景 + 毛玻璃大圆角卡片 + 纯白与发光元素点缀 | 夏日活动、创意产品、汽水风格、多巴胺设计、元气海报 | [预览名片](references/styles/summer-dopamine/preview.png)<br>`references/styles/summer-dopamine/` |
| **`warm-craft`** | **温润纸感手札风**<br>(Warm Craft) | 暖米纸质画布 (`#F7F4EC`) + 人文宋体大标题 (Editorial Serif) + 深橄榄绿行动通道 (`#323D24`) + 错落微倾粉彩贴纸 (`-2deg`~`+2deg`) + 手绘涂鸦 | 智能代理、知识沉淀、深度调研、SaaS 产品官网、人文科技、书籍出版物、温润工作流 | [预览名片](references/styles/warm-craft/preview.png)<br>`references/styles/warm-craft/` |
| **`soft-editorial-future`** | **极简未来展厅风**<br>(Future Showroom) | 偏冷质感画布 + 高光悬浮玻璃展柜 + 内部色彩温润晕开的 3D 柔光彩球散布（边缘柔和自然） | 高级展厅、视觉画廊、艺术展落地页、前沿科技、AI产品、高端发布会 | [预览名片](references/styles/soft-editorial-future/preview.png)<br>`references/styles/soft-editorial-future/` |
| **`play-tubular`** | **玩味极客彩管风**<br>(Play Tubular) | 浅暖米白点阵画布 (`#FAF8F3`) + 粗圆鲜活 3D 渐变立体彩管/丝带环绕 + 球头末端与弯折处的 **半调网点 (Halftone Dot Matrix)** 光影 + 现代高对比度工程粗黑体 + 纯白大圆角弹簧动效卡片 | AI/LLM 创新展示、创意产品发布、工程技术白皮书、开发者大会、玩味科技落地页 | [预览名片](references/styles/play-tubular/preview.png)<br>`references/styles/play-tubular/` |
| **`nothing-design-dark`** | **Nothing 极简点阵暗黑风**<br>(Nothing Monochrome Dark) | OLED 纯黑背景 (`#000000`) + 24px 点阵网格 + Doto 点阵字 + 多通道遥测色（珊瑚橙 `#FF5722`、翡翠绿 `#22C55E`、琥珀金 `#F59E0B`）+ 按需语义组件 + 分段刻度条 | 硬件工业设计、前沿数码发布、技术规格书、深度研究白皮书、瑞士排版工程文档、夜间长篇报告 | [预览名片](references/styles/nothing-design-dark/preview.png)<br>`references/styles/nothing-design-dark/` |
| **`nothing-design-light`** | **Nothing 极简点阵亮白风**<br>(Nothing Monochrome Light) | 陶瓷冷白背景 (`#FFFFFF`) + 浅灰点阵网格 + Doto 点阵字 + 纯黑正文 + 多通道功能色（信号红 `#D71921`、翡翠绿 `#16A34A`、琥珀金 `#D97706`）+ 按需语义组件 | 白瓷工业设计、白皮书、现代印刷质感报告、硬件参数发布、极简日间阅读、学术出版物 | [预览名片](references/styles/nothing-design-light/preview.png)<br>`references/styles/nothing-design-light/` |
| **`pixel-crystal`** | **油画粉彩晶光风**<br>(Pixel Crystal) | 温润油画布纹 (`#FDF8F7`) + 莫奈复调渐变 + 晶透苹果图腾 + 点彩星芒 + 珍珠母贝画板 + 熟褐暗茜草墨色正文 (`#3C2836`) | 艺术企划、文化出版、Vtuber、梦幻生活方式、独立游戏、高端少女心与治愈系产品、创意插画案例集 | [预览名片](references/styles/pixel-crystal/preview.png)<br>`references/styles/pixel-crystal/` |
| **`ink-bamboo`** | **青绿水墨竹韵风**<br>(Ink Bamboo) | 古法宣纸暖底 (`#F6F4EE`) + 右侧水墨竹节竿影 + 古典宋体大标题 + 翠竹生青 (`#5A8F43`) + 朱砂印章点睛 (`#C03E2D`) + 矿物青绿色谱 | 中式文化企划、行业深度研报、学术白皮书、东方文创展示、自然生态战略、高端政企汇报 | [预览名片](references/styles/ink-bamboo/preview.png)<br>`references/styles/ink-bamboo/` |
| **`state-governance`** | **国企政务严谨汇报风**<br>(State Governance Blue) | 纯净冷白/微浅蓝画布 + 权威深海蓝 (`#103A71`) + 工信科技蓝 (`#1A56DB`) + 标题贯穿深蓝细线 + 蓝色虚线重点框 + 三箭头推进器 + 多视角流转矩阵 | 国企/央企工作汇报、政府与公共事业规划、政企数字化方案、大型企业管理架构、全生命周期业务推演、供应链韧性策略、党政战略发布会 | [预览名片](references/styles/state-governance/preview.png)<br>`references/styles/state-governance/` |
| **`ink-calligraphy`** | **宣纸泼墨挥毫风**<br>(Ink Calligraphy) | 古法生宣暖底 (`#F5F2EB`) + 自然飞溅墨星 + 苍劲行草大标题 + 朱砂篆刻印章 (`#C23531`) + 墨分五色阶梯 + 飞白扫墨横纹 | 中式传统文化、文人书画研报、艺术大家传记、东方美学白皮书、古典哲学出版物、泼墨意境展示 | [预览名片](references/styles/ink-calligraphy/preview.png)<br>`references/styles/ink-calligraphy/` |

> 💡 **未来扩展**：新增风格只需在 `references/styles/<style_id>/` 目录下添加设计规范、脚手架、矢量源文件 `preview.svg` 与对话预览 `preview.png`，并在 `registry.json` 中注册；画廊卡片会自动生成。

---

## 2. 标准执行工作流 (Standard Workflow)

```mermaid
flowchart LR
    A["1. 意图分析与匹配"] --> B["2. 对话内嵌视觉预览并确认风格"]
    B --> C["3. 按需读取专属规范与模版"]
    C --> D["4. 结构化代码生成"]
    D --> E["5. 双层质量清单验收"]
```

### 第一步：意图分析与交互确认（视觉卡片推荐）

本 Skill 触发后，**不要直接生成全部代码**。首先分析用户需求与偏好：

1. **已明确指定**：若用户已明确指定风格（如“用浅蓝风”、“Industrial Dark”、“Play Tubular”），直接锁定对应 `style_id`。
2. **基于图像参考（多模态设计逆向工程）**：如果用户提供了一张**设计参考图**，请先执行解构分析：
   - 提取全局底色（背景）。
   - 提取核心信号色（品牌色、高光色、渐变色）。
   - 提取形状特征（圆角大小、卡片阴影质感、3D或扁平）。
   - 提取排版特征（字重、留白、边框风格）。
   - **完成分析后，严格遵守“Clean Room Design”法则，不要继承旧模板，直接从 `references/_base-scaffold-web.html` 读取基座并在其上编写全新 CSS**，以防止硬编码污染。
3. **智能推荐机制（输出 3～5 款设计风格）**：
   - 当用户提供了长文或排版需求但未锁定风格，或者意图较为宽泛时，分析文本特征并挑选 **最契合的 3～5 套风格**。
   - **对话内嵌视觉预览（强制）**：在同一条推荐回复中，用 Markdown 图片直接展示每个候选风格的 `preview.png`，然后再给出文字说明。用户必须能在对话流中看见实际色彩、构图和组件质感后再选择。
     - 从当前 `SKILL.md` 所在目录解析每个候选的绝对路径：`references/styles/<style_id>/preview.png`。
     - 使用绝对本地路径的 Markdown 图片语法，路径含空格时包裹在尖括号内：`![<style_id> 风格预览](</绝对路径/references/styles/<style_id>/preview.png>)`。
     - **不得**改用 `preview.svg`、`file://` 链接、相对路径、纯文字卡片、Artifact 或浏览器画廊来替代该图片。画廊只能作为查看全部风格的补充入口。
     - 仅当当前客户端明确无法显示本地 Markdown 图片时，才降级为文字卡片和画廊链接；需明确说明“当前客户端无法内嵌本地预览”，不能假称已经展示预览。
   - **每项说明**：每张预览图下保留风格名称、`style_id`、一句视觉基因和一句推荐理由，便于用户依据预览与场景共同决策：
     ```markdown
     ### 1. 玩味极客彩管风 (`play-tubular`)
     ![玩味极客彩管风预览](</绝对路径/references/styles/play-tubular/preview.png>)
     - **视觉基因**：浅暖米白点阵画布 + 3D 渐变立体彩管 + 半调网点光影。
     - **推荐理由**：适合 AI/LLM 架构与技术白皮书，兼顾工程感与活力。
| **`state-governance`** | **国企政务严谨汇报风**<br>(State Governance Blue) | 纯净冷白/微浅蓝画布 + 权威深海蓝 (`#103A71`) + 工信科技蓝 (`#1A56DB`) + 标题贯穿深蓝细线 + 蓝色虚线重点框 + 三箭头推进器 + 多视角流转矩阵 | 国企/央企工作汇报、政府与公共事业规划、政企数字化方案、大型企业管理架构、全生命周期业务推演、供应链韧性策略、党政战略发布会 | [预览名片](references/styles/state-governance/preview.png)<br>`references/styles/state-governance/` |
| **`ink-calligraphy`** | **宣纸泼墨挥毫风**<br>(Ink Calligraphy) | 古法生宣暖底 (`#F5F2EB`) + 自然飞溅墨星 + 苍劲行草大标题 + 朱砂篆刻印章 (`#C23531`) + 墨分五色阶梯 + 飞白扫墨横纹 | 中式传统文化、文人书画研报、艺术大家传记、东方美学白皮书、古典哲学出版物、泼墨意境展示 | [预览名片](references/styles/ink-calligraphy/preview.png)<br>`references/styles/ink-calligraphy/` |

> 💡 **未来扩展**：新增风格只需在 `references/styles/<style_id>/` 目录下添加设计规范、脚手架、矢量源文件 `preview.svg` 与对话预览 `preview.png`，并同步在 `style-gallery.html` 与本表中注册即可。

---

## 3. 标准执行工作流 (Standard Workflow)

```mermaid
flowchart LR
    A["1. 意图分析与匹配"] --> B["2. 对话内嵌视觉预览并确认风格"]
    B --> C["3. 按需读取专属规范与模版"]
    C --> D["4. 结构化代码生成"]
    D --> E["5. 双层质量清单验收"]
```

### 第一步：意图分析与交互确认（视觉卡片推荐）

本 Skill 触发后，**不要直接生成全部代码**。首先分析用户需求与偏好：

1. **已明确指定**：若用户已明确指定风格（如“用浅蓝风”、“Industrial Dark”、“Play Tubular”），直接锁定对应 `style_id`。
2. **基于图像参考（多模态设计逆向工程）**：如果用户提供了一张**设计参考图**，请先执行解构分析：
   - 提取全局底色（背景）。
   - 提取核心信号色（品牌色、高光色、渐变色）。
   - 提取形状特征（圆角大小、卡片阴影质感、3D或扁平）。
   - 提取排版特征（字重、留白、边框风格）。
   - **完成分析后，严格遵守“Clean Room Design”法则，不要继承旧模板，直接从 `references/_base-scaffold-web.html` 读取基座并在其上编写全新 CSS**，以防止硬编码污染。
3. **智能推荐机制（输出 3～5 款设计风格）**：
   - 当用户提供了长文或排版需求但未锁定风格，或者意图较为宽泛时，分析文本特征并挑选 **最契合的 3～5 套风格**。
   - **对话内嵌视觉预览（强制）**：在同一条推荐回复中，用 Markdown 图片直接展示每个候选风格的 `preview.png`，然后再给出文字说明。用户必须能在对话流中看见实际色彩、构图和组件质感后再选择。
     - 从当前 `SKILL.md` 所在目录解析每个候选的绝对路径：`references/styles/<style_id>/preview.png`。
     - 使用绝对本地路径的 Markdown 图片语法，路径含空格时包裹在尖括号内：`![<style_id> 风格预览](</绝对路径/references/styles/<style_id>/preview.png>)`。
     - **不得**改用 `preview.svg`、`file://` 链接、相对路径、纯文字卡片、Artifact 或浏览器画廊来替代该图片。画廊只能作为查看全部风格的补充入口。
     - 仅当当前客户端明确无法显示本地 Markdown 图片时，才降级为文字卡片和画廊链接；需明确说明“当前客户端无法内嵌本地预览”，不能假称已经展示预览。
   - **每项说明**：每张预览图下保留风格名称、`style_id`、一句视觉基因和一句推荐理由，便于用户依据预览与场景共同决策：
     ```markdown
     ### 1. 玩味极客彩管风 (`play-tubular`)
     ![玩味极客彩管风预览](</绝对路径/references/styles/play-tubular/preview.png>)
     - **视觉基因**：浅暖米白点阵画布 + 3D 渐变立体彩管 + 半调网点光影。
     - **推荐理由**：适合 AI/LLM 架构与技术白皮书，兼顾工程感与活力。

     ### 2. 暗黑极客工业风 (`industrial-dark`)
     ![暗黑极客工业风预览](</绝对路径/references/styles/industrial-dark/preview.png>)
     - **视觉基因**：近黑背景 + CAD 网格 + 信号绿与紫色通道 + 硬边模块。
     - **推荐理由**：适合硬核技术规格与系统参数展示。
     ```
   - **画廊补充入口**：在推荐内容末尾附带本次本地画廊服务返回的带 `?key=` URL，链接文字固定为“查看全部风格”。用户可在 Codex 内置浏览器对比全部已注册风格的完整动态效果与配色；点击“使用此风格”后，页面复制包含中文风格名与 `style_id` 的选择文本，并显示“风格已复制”。
   - **条件式确认**：风格和媒介都已明确时直接生成；只明确风格时只询问媒介；只明确媒介时推荐 3–5 款风格；两者都不明确时才推荐 3–5 款并询问媒介。不要重复确认用户已经明确的选择。

   - **本地画廊（默认选择路径）**：当用户需要浏览并选择风格时，自动运行 `references/scripts/style-companion/start-server.sh --project-dir <当前项目根> --open`。这是 Skill 自带的本地 Node 服务，不需要用户安装 MCP server、浏览器插件或额外依赖。命令会返回带会话 key 的 URL、`state_dir` 和会话目录；把完整 URL（包括 `?key=`）作为“查看全部风格”链接，并在当前客户端支持时用内置浏览器打开。
     - 在 Codex 中直接运行该命令并保留前台终端会话，然后使用内置 Browser 将返回的 URL 导航到画廊；不要依赖操作系统的默认浏览器，也不要用命令替换吞掉会话。启动脚本会检测 Codex 环境，确保服务跨对话轮次持续运行。
     - 点击“使用此风格”只复制选择文本并显示“风格已复制”；不向对话发送消息、不创建本地选择事件，也不注入对话桥接。
     - 用户将复制文本粘贴到对话后，使用其中的 `style_id` 锁定风格，并继续询问“想制作成网页还是 PPT”。用户未在对话中明确风格时不得从画廊操作猜测。
     - 服务不可用时，明确说明原因并保留已展示的对话内预览；画廊本身需要通过本地服务读取注册表。完成流程后可运行 `references/scripts/style-companion/stop-server.sh <session_dir>` 停止服务。


### 第二步：按需精准读取 (On-Demand Loading)

确定风格与输出媒介后，读取**且仅读取**目标风格的规范与脚手架，绝不把全部无关风格载入上下文：

  - **读取目标设计规范**：`references/styles/<style_id>/design.md`（包含视觉主题、Tokens、字阶量化表、组件状态、间距/海拔与动效、Do's/Don'ts、响应式和可访问性规则）
- **读取目标脚手架**：
  - Web 场景：`references/styles/<style_id>/scaffold-web.html`
  - PPT 场景：`references/styles/<style_id>/scaffold-ppt.html`
- **通用组件参考（可选）**：`references/shared-components.md`

### 第三步：代码生成优先级与动态组装 (Dynamic Assembly)

动手生成前必须遵循以下原则，**严禁被脚手架“模板化”**：

#### 1. 原文优先的语义组件映射 (Source-First Semantic Mapping)
先识别原文的标题层级、论证顺序和章节间关系；如果结构已经清晰，保持其顺序并仅做必要的排版与局部结构化。只有用户明确要求重构，或原文确实缺少可读的章节、顺序或逻辑衔接时，才用最小必要改动整理结构。以下 18 项是按需选用的组件目录，不是固定阶段、固定顺序或必须凑齐的清单：

| 文本特征 / 逻辑类型 | 语义交付 | 内容契约 |
|---|---|---|
| **章节索引与标头装饰** | 章节标识 | 传达原有章节标题与层级；编号和装饰仅在原文或目标风格需要时使用 |
| **基础字阶与主副标题** | 标题层级与导读 | 保留原有标题树；导读只在原文已有或用户要求摘要时生成 |
| **爆炸性宏观数据 / KPI 统计** | 定量重点 | 保留数值、单位、含义、范围和限定条件，不编造指标 |
| **核心指标 / 关键硬件或系统参数** | 规格组 | 保留原有规格、单位、适用条件与数据来源 |
| **核心结论 / 重要警示 / 前置提醒** | 提示与结论 | 保留结论、适用范围与依据；不凭空提高内容的警示等级 |
| **长篇论述 / 深度背景 / 引用与列表** | 正文 | 完整承载段落、引用、列表与内联语义，是无法归类内容的保真容器 |
| **代码片段 / 终端指令 / 配置参数 / API** | 代码与命令 | 保留代码、语言/上下文与可复制文本；其容器、标记与交互由风格决定 |
| **并列功能 / 核心卖点** | 并列特性组 | 保留各项的标题、说明和原有的并列或优先关系，不预设数量或卡片形式 |
| **图文特性 / 媒体演示说明** | 带媒体的特性说明 | 保留特性主张、说明及已有媒体上下文；没有媒体时不创建虚假占位内容 |
| **系统架构 / 状态机 / 数据流 / 复杂拓扑** | 图解 | 保留节点、关系、方向和标签；选择 SVG、Mermaid 或其他表达由复杂度和风格决定 |
| **分步工作流 / 操作指南 / 执行计划** | 步骤序列 | 保留步骤顺序、条件、操作和结果 |
| **时间跨度 / 发展演进 / 历史版本** | 时间序列 | 保留时间点、事件、顺序与不确定性说明 |
| **多方案对比 / 版本差异 / 性能评测** | 对比 | 保留可比维度、各方数据与证据；没有原始依据时不标记推荐项 |
| **双面评估 / 利弊分析 / 优劣榜** | 双向评估 | 保留正反两面的条件和依据，不伪造平衡或结论 |
| **多轮访谈 / 需求推演 / 智能体人机协同** | 对话与决策记录 | 清晰区分提问、分析、建议和用户决策，保留轮次关系 |
| **问答记录 / 疑难排解 / FAQ** | 问答 | 保留问题与答案的对应关系；没有问答内容时不生成 |
| **参考文献 / 引用来源 / 学术出处** | 引用与出处 | 保留来源、链接/标识和原有引用关系 |
| **系统元数据 / 版本号 / 交付页脚** | 元数据 | 只呈现可确认的文档类型、版本、时间等信息 |
| **可选外挂 (默认不生成)** | 阅读辅助 | 仅在用户明确要求或文档确有需要时加入；位置、交互与形态由风格决定 |

#### 2. 信息完整度与防偷懒契约 (Content Fidelity Contract)
- **严禁信息恶意损耗**：除非用户明确要求“摘要 / 提炼 / TL;DR”，否则必须保留原文所有的核心论据、技术细节、参数规格、代码示例与逻辑段落，严禁大幅删减 70% 原文内容。
- **严禁虚假生成与省略占位符**：绝对禁止在生成的 HTML 中输出 `<!-- 此处省略其余章节 -->` 或 `<!-- 更多内容 -->`。遇到无法归类到特殊卡片的长文本，**一律放入 `.rich-text` 正文容器中完整呈现**。
- Web 输出遵循完整保真；PPT 输出允许压缩版面，但必须保留结论、关键指标、论据出处，并把未展示的技术细节放入附录或“详细内容”页，不得无声明丢弃。

#### 3. 页面组装与三层画布架构契约 (3-Tier Canvas & Skeleton Contract)
- **执行目标风格的布局契约（Style-Owned Layout Contract）**：动手生成前读取目标风格的 `design.md`，并采用它声明的结构。风格可使用 Layer 0 环境层、Layer 1 通体画板、直铺流式版面或明确声明的其他结构；不得因通用模板而额外注入背景、画板或卡片形态。
- **执行目标风格的材质与色彩语言**：色彩、阴影、渐变、3D、图形密度和卡片材质均由目标风格决定。不得把目标风格机械改成通用外观，也不得以通用规则压制风格原本需要的视觉元素。
- **原文优先装配 (Source-First Assembly)**：以原有章节树、论证顺序、时间顺序和因果关系为页面顺序。结构清晰时只做轻量排版与局部组件映射；用户要求重构或原文逻辑混乱时，才提出并采用与内容相称的结构。不得为了套用组件而虚构章节、重排论点或补出不存在的 FAQ、对比和结论。
- **Quick Nav / 进度条默认不启用**：`quick-nav` 和 `reading-progress` 是可选外挂增强，**常规页面默认不添加**；若用户明确要求或针对超长篇文档引入时，其位置与形态不应写死，可根据设计风格自由布局为顶部悬浮、左侧粘性侧栏或右侧浮动锚点。
- **信息层级**：让读者能辨识原文标题树、重点与内容关系；标题尺度、焦点数量和强调方式由内容类型与目标风格共同决定。
- **Mermaid 在线增强与离线降级**：生成复杂图表时可保留 Mermaid 源码；交付前必须运行 `python3 references/scripts/bundle_offline.py <input.html> -o <output.html>`。在线时尝试加载完整 Mermaid 和远程字体，离线或加载失败时显示静态 SVG fallback 和系统字体。完全断网交付使用 `--strict`。

---

### 第四步：双层质量清单校验 (Checklist)

生成完成后，按以下清单逐项验证：

#### 通用基础质检项：
- [ ] **信息保真度**：原文核心论据、参数与技术细节是否 100% 完整保留，无恶意删减与偷懒省略占位符？
- [ ] **原文结构**：结构清晰时是否保留原有标题层级、论证/时间顺序和章节关系？如进行了重构，是否仅因用户要求或原文确实混乱，且改动可说明？
- [ ] **层级可读性**：原文标题树、重点和内容关系是否清晰，且没有被视觉呈现掩盖？
- [ ] **风格一致性**：页面是否符合目标风格自己的布局、字体、材质、色彩、装饰与动效规则？不以通用规则限制渐变、阴影、3D、图形、卡片、信号色或焦点数量。
- [ ] **图表与 Mermaid 完备性**：复杂 Mermaid 是否保留在线增强并具备静态 SVG fallback？最终交付是否已运行 `bundle_offline.py`，且断网时图表仍可读？
- [ ] **离线交付**：本地图片、CSS 和字体 fallback 是否可用；`--strict` 交付是否不含外部资源请求？

#### 风格专属质检项：
- 执行从目标风格 `references/styles/<style_id>/design.md` 中读取的专属质量清单（如 Industrial Dark 的 0–2px 硬圆角校验、Soft Sky 的 8–16px 柔和圆角校验、Warm Craft 的宋体排版与无粗黑边便签回正校验、或 Play Tubular 的暖米白半调点阵底纹、3D 渐变彩管与半调网点光影质感校验）。

---

## 4. Route-specific execution

媒介和生命周期的具体执行规则已移到 route authority，避免入口在一次任务中加载无关分支：

- Web 响应式布局、离线 bundle、字体内联和单文件交付：读取 [`references/routes/generate-web.md`](references/routes/generate-web.md)。
- PPT 16:9 舞台、单页聚焦、翻页/打印导出和演示交付：读取 [`references/routes/generate-ppt.md`](references/routes/generate-ppt.md)。
- 新增或扩展风格包的目录、预览、注册和验证 SOP：读取 [`references/template-extension-guide.md`](references/template-extension-guide.md)。

route 文档与本入口的共享质量清单共同构成验收标准；route 文档未声明的行为不从其他 route 推断。
