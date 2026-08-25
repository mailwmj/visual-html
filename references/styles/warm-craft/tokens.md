# Warm Craft / 暖纸手作与温润社论 — Design Tokens & Style Specification

> **Style ID**: `warm-craft`  
> **显示名称**：暖纸手作/温润社论风 (Warm Craft Editorial)  
> **核心气质**：采用温润米白纸质画布、古典人文宋体大标题（Editorial Serif）、深橄榄绿核心行动通道、轻微错落微倾斜的多彩贴纸卡片（Pastel Sticker Cards，零生硬黑边）与灵动手绘涂鸦、高光划线及轻快弹性交互回弹（Elastic Hover Dynamics）。散发自然亲和、智序并存的温润匠心感，特别适合智能代理、知识沉淀、深度调研与人文科技型产品落地页。

---

## 1. Design DNA & 核心原则

1. **温润米白暖纸画布 (Warm Oatmeal Paper Canvas)**：
   - 全局背景为带有细腻纸质温度的浅暖米白（`#F7F4EC` / `#FAF7F0`），绝不使用刺眼的纯冷白或冰冷灰。
   - 背景点缀极淡的有机流体光晕斑块（暖黄 `#FFF5D6`、抹茶绿 `#EEF6DE`、柔紫 `#F0EEF8`），置于全局固定层 (`body::before`)，滚动时不产生任何断层。
2. **古典人文宋体与多平台排版栈 (Editorial Serif + Native Songti SC)**：
   - **大标题 (Hero & Section Titles)**：采用高阶人文衬线宋体（`"Newsreader"`, `"Playfair Display"`, `"Songti SC"`, `"STSong"`, `"Source Han Serif SC"`, `"Noto Serif SC"`, `"SimSun"`），字重 700–900，行高紧凑优雅（1.12–1.18），呈现出书籍出版物般的沉稳与智识美感。
   - **正文与辅助信息**：采用高可读性现代无衬线字体（`"Inter"`, `"PingFang SC"`, `"HarmonyOS Sans SC"`, `"Microsoft YaHei"`, `"微软雅黑"`），保证小字号下的极佳辨识度。
   - **参数、序号与 Eyebrow**：采用工整的 Mono 等宽字体。
3. **多色粉彩贴纸（零生硬黑边）与扇形对称外展 (Pastel Sticker Notes & Symmetric Fan Tilts)**：
   - 核心功能卡片与标签采用清新高雅的粉彩色谱（明黄 `#FEDB71`、暖橙 `#FFA963`、抹茶绿 `#B7D97A`、柔紫 `#AAB7F2`、晴空蓝 `#7CB6F8`）。
   - **边框与阴影规范**：卡片采用极淡的同色系半透明边框或纯白高光微边（`border: 1px solid rgba(0, 0, 0, 0.04)` 或 `border: 1px solid rgba(255, 255, 255, 0.7)`），**绝对禁止在选中态使用生硬厚重的深色/黑色粗描边**。高亮态通过彩色柔光多层阴影与微上浮呈现。
   - 卡片在排列时采用**扇形镜像对称外展微倾角**（如左卡 `rotate(-2deg) translateY(2px)`、中卡 `rotate(0deg)` 居中回正微浮、右卡 `rotate(2deg) translateY(2px)` 镜像对称），模拟书桌双手自然摊开 3 张手账便签的优美弧形张力，杜绝单边倾斜失衡。
4. **轻快弹性动效与交互手感 (Elastic Motion & Hover Dynamics)**：
   - 鼠标悬浮在便签卡片上时，卡片自动**回正角度（`rotate(0deg)`）**并配合**弹性曲线（`cubic-bezier(0.175, 0.885, 0.32, 1.275)`）**轻盈上浮（`translateY(-10px) scale(1.03)`），彩色弥散投影扩散，赋予页面如同从桌面捏起卡片般的愉悦触感。
   - 选中卡片（`.selected`）在 `:hover` 时具备专属高升动效（`translateY(-14px) scale(1.05)`），确保交互反馈鲜明清晰。
5. **文字效果与手绘划线 (Typography Effects & Marker Highlights)**：
   - 支持马克笔半透明高光底纹（`.marker-highlight`，黄/橙/绿渐变），用于强调核心关键词。
   - 大号古典开闭双引号（`“ ... ”`）装点 Blockquote 引言段落。
6. **深橄榄绿核心行动色 (Deep Forest Olive Accent)**：
   - 核心按钮、关键状态与重点聚焦使用深沉内敛的深橄榄森林绿（`#323D24` / `#2D3920`），与米白底色和粉彩贴纸形成极高雅的对比。

---

## 2. CSS Design Tokens

```css
:root {
  /* 背景层：暖纸底色与柔和环境色 */
  --bg: #F7F4EC;
  --bg-warm: #FAF7F0;
  --bg-deep: #EDE7DA;
  
  /* 表面层 (Surface) */
  --surface-card: #FFFFFF;
  --surface-card-subtle: #FAF8F2;
  --surface-overlay: rgba(255, 255, 255, 0.85);

  /* 文字层 (深墨绿炭黑 / 暖灰 / 沙岩色) */
  --text-primary: #1E231B;       /* 主标题与高对比度文字 */
  --text-secondary: #565E50;     /* 正文与次要段落 */
  --text-muted: #8E9685;         /* 占位符、辅助脚注与 Mono 标签 */
  --text-inverse: #FFFFFF;       /* 深色按钮与深底文字 */

  /* 核心主行动色 (深橄榄森林绿) */
  --signal-primary: #323D24;
  --signal-primary-hover: #242E18;
  --signal-primary-light: #EBF0E4;

  /* 粉彩贴纸多色通道 (Pastel Sticker Palette) */
  --pastel-yellow: #FEDB71;
  --pastel-yellow-text: #5A3E00;
  --pastel-yellow-border: rgba(236, 197, 85, 0.5);

  --pastel-orange: #FFA963;
  --pastel-orange-text: #542200;
  --pastel-orange-border: rgba(232, 142, 68, 0.5);

  --pastel-green: #B7D97A;
  --pastel-green-text: #243D06;
  --pastel-green-border: rgba(158, 194, 94, 0.5);

  --pastel-purple: #AAB7F2;
  --pastel-purple-text: #1B2966;
  --pastel-purple-border: rgba(141, 157, 224, 0.5);

  --pastel-blue: #7CB6F8;
  --pastel-blue-text: #0B3363;
  --pastel-blue-border: rgba(94, 156, 230, 0.5);

  --pastel-coral: #FCA598;
  --pastel-coral-text: #631C12;
  --pastel-coral-border: rgba(229, 134, 119, 0.5);

  /* 边框与阴影 (无粗黑边，温润透亮) */
  --border: rgba(50, 61, 36, 0.08);
  --border-strong: rgba(50, 61, 36, 0.16);
  --shadow-card: 0 6px 24px rgba(45, 40, 25, 0.05), 0 1px 3px rgba(45, 40, 25, 0.03);
  --shadow-card-hover: 0 16px 36px rgba(45, 40, 25, 0.10), 0 3px 8px rgba(45, 40, 25, 0.04);
  --shadow-sticker: 0 8px 24px rgba(50, 45, 30, 0.07), 0 2px 6px rgba(50, 45, 30, 0.03);

  /* 交互与缓动曲线 Tokens (Motion & Curves) */
  --ease-elastic: cubic-bezier(0.175, 0.885, 0.32, 1.275);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-hover: 0.35s;

  /* 尺寸与圆角 */
  --radius: 20px;
  --radius-sm: 12px;
  --radius-pill: 100px;
  --container: 1180px;

  /* 字体栈 (Editorial Serif + Clean Sans + Mono) */
  --font-serif: "Newsreader", "Playfair Display", "Songti SC", "STSong", "Source Han Serif SC", "Noto Serif SC", "Noto Serif CJK SC", "SimSun", "STFangsong", "FangSong", "Georgia", serif;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans SC", "Microsoft YaHei", "微软雅黑", sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", "SFMono-Regular", Consolas, monospace;
}
```

---

## 3. 交互动效与手感规范 (Motion & Interactive Hover Dynamics)

| 组件 / 状态 | 默认静止态 (Rest State) | 悬浮微交互态 (`:hover`) | 交互手感设计意图 |
|---|---|---|---|
| **常规贴纸卡片 (`.num-card`)** | 扇形镜像微倾斜 (左 `rotate(-2deg) translateY(2px)` / 中 `rotate(0deg)` / 右 `rotate(2deg) translateY(2px)`)，低悬浮投影 | 角度平滑回正 (`rotate(0deg)`)，弹性上浮 `translateY(-10px) scale(1.03)`，阴影扩散，层级升至 `z-index: 10`，内部标签轻微浮起 | 模拟将书桌上自然铺开的便签纸轻轻捏起查看的手账质感 |
| **选中/推荐卡片 (`.num-card.selected`)** | 居中回正上浮 `rotate(0deg) translateY(-6px) scale(1.01)`，高光白边与彩色柔光投影 | 进一步弹性跃升 `translateY(-14px) scale(1.05)`，强光晕扩散 `box-shadow: 0 26px 54px rgba(255, 169, 99, 0.42)`，层级升至 `z-index: 12` | 确保推荐卡片始终具备最高层级响应与视觉锚点，杜绝被其他卡片遮挡 |
| **核心数据卡片 (`.stat-card`)** | 纯白卡片底座，柔和边框与微阴影 | 平滑上浮 `translateY(-4px)`，阴影深度加深 (`var(--shadow-card-hover)`) | 呈现稳定且沉着的参数反馈 |
| **流程步骤卡片 (`.step`)** | 纵向规整排列，圆形彩色编号徽标 | 向右轻微平移 `translateX(6px)`，序号徽标微幅旋转放大 | 引导用户视线沿着工作流顺序向下探索 |
| **常见问答条目 (`.faq-item`)** | 纯白圆角条目 | 微上浮 `translateY(-2px)`，边框微高光 | 提示可交互性 |
| **超链接与引用文献** | 带有深橄榄绿下划线 | 下划线偏移增加，文字平滑变为暖橙色 (`var(--pastel-orange-text)`) | 温暖亲和的文本引导 |

---

## 4. 18 项核心组件视觉契约 (Component Visual Contracts)

依据全局规范 `shared-components.md`，以下 18 个标准组件在 `warm-craft` 风格下的具体呈现规则：

1. **Section Eyebrow (区块索引标头)**:
   - 采用深橄榄绿文字 + 暖橙色 45° 旋转菱形标（`.diamond`），搭配 Mono 大写等宽编号，右侧跟随一条淡暖灰 1px 细线（`--border-strong`）。
2. **Typography Scale (基础文本层级与文字效果)**:
   - `h1.hero`：采用 `--font-serif` 高阶宋体，大字号（38–64px），字重 800，行高紧凑优雅（1.15），支持使用 `.marker-highlight` 添加手绘马克笔黄色/橙色底纹高亮。
   - `h2.section-title`：同样采用 `--font-serif`，字号 28–42px。
   - `.lead`：采用 `--font-sans`，字号 17–20px，颜色为 `--text-secondary`，行高 1.68。
3. **Technical Spec Row (规格参数栏)**:
   - 纯白悬浮圆角卡片底座，内部划分为多列规格网格，中间以 1px `--border` 细线分割。数值 `.val` 采用深橄榄绿加粗 Serif 字体呈现，单位 `.unit` 采用全大写 Mono 字体。
4. **Number Cards (编号卡片列 - 核心粉彩贴纸群，严禁粗黑描边，支持扇形对称与弹性回弹动效)**:
   - 卡片采用粉彩贴纸色谱（黄、橙、绿依次分色），圆角 20px，排列采用扇形对称外展微倾角（左卡 `-2deg translateY(2px)`、中卡 `0deg`、右卡 `+2deg translateY(2px)`）。
   - 编号 `.num` 采用大号 Mono 字体，卡片底部带有浅白底胶囊标签 `.tag`。
   - **交互动效**：鼠标悬浮时回正角度（`rotate(0deg)`）并触发弹性上浮（`translateY(-10px) scale(1.03)`）。
   - **选中与推荐态 `.selected`**：禁止使用黑色粗边框，采用高光白边（`border: 1px solid rgba(255, 255, 255, 0.7)`）与暖橙色弥散强投影，居中回正并微浮 `rotate(0deg) translateY(-6px) scale(1.01)`，Hover 时深度跃升至 `translateY(-14px)`。
5. **Feature Card & Media Frame (特性卡片与媒体预览框)**:
   - 纯白大圆角卡片，内嵌媒体占位框 `.frame`，使用浅暖米色底（`--surface-card-subtle`）搭配精致手绘虚线边框或微渐变阴影。
6. **Process Steps (流程步骤)**:
   - 步骤卡片依次错落排布，序号 `.idx` 使用粉彩圆形徽章包裹（如明黄/暖橙/抹茶绿），Hover 时右移 `translateX(6px)`。
7. **Comparison Table (对比矩阵)**:
   - 纯白大圆角全封闭卡片表格，表头使用浅暖米灰底色（`--bg-deep`），推荐列（`.highlight-col` 或 `.selected-col`）采用淡暖橙色背景高亮（`rgba(255, 169, 99, 0.12)`）与深橄榄色标点，温暖清晰。
8. **Metadata Footer (技术页脚)**:
   - 浅暖纸底色，顶部 1px 细线分隔，左右两端对齐，Mono 字体大写，字号 12px，颜色 `--text-muted`。
9. **Admonitions (智能语义提示框)**:
   - 模拟手账贴纸便签（Sticky Note），左侧带有 6px 粗暖色条（Info 为明黄色 `#FEDB71`、Warning 为暖橙色 `#FFA963`、Success 为抹茶绿 `#B7D97A`），整体带温润背景色与柔和内阴影。
10. **Timeline (时间轴)**:
    - 垂直连线为 2px 虚线，时间节点 `.timeline-marker` 为带有微倾角的彩色药丸徽标，右侧内容采用纯白圆角便签卡片。
11. **Pros & Cons (优劣势红黑榜)**:
    - 左右双卡片：Pros 优势卡片使用浅抹茶绿底（`#F2F7E8`）配深绿勾选符；Cons 劣势卡片使用浅蜜桃粉底（`#FCF1EE`）配柔和短横线。
12. **Stats Grid (核心数据卡片)**:
    - 采用纯白大圆角卡片，数字 `.stat-val` 使用大号 Serif 字体（48–64px），单位 `span` 自然上浮，下方配 Mono 风格说明标签。
13. **Flowchart (流程图与系统架构)**:
    - SVG 流程图采用深橄榄线条与圆润箭头，节点为圆角矩形，核心活跃节点（`.active`）使用暖橙或明黄背景填色。
14. **References (参考文献与脚注)**:
    - 纯白卡片包裹，有序列表项文字小巧精致，链接采用深橄榄绿下划线，悬浮时变暖橙色。
15. **Rich Text (长文本正文模块)**:
    - 纯白圆角大卡片，内部 `h3/h4` 采用 Serif 宋体，正文行高 1.8，引用 `blockquote` 左侧带 4px 深橄榄线条、大号引号装饰 `“` 与浅米色底衬。
16. **FAQ / Q&A List (问答列表)**:
    - 模块化纯白圆角折叠条目，问题 `.q` 采用 Serif 加粗排版与深橄榄色前缀符号 `Q`，答案 `.a` 使用温润无衬线正文。
17. **Editorial Interview & Walkthrough Rounds (社论访谈录 / 轮次推演卡片)**:
    - 纯白纸质大圆角底座（`.round-card`），顶部带有深橄榄色胶囊标头（`.round-badge`）与 Mono 状态指示。
    - **提问卡区 (`.ai-questions-block`)**：采用浅米白纸底（`--surface-card-subtle`），序号为 Mono 方形印章（`.q-badge`），问题为 Serif 宋体加粗。
    - **推荐答案便签 (`.q-recom-note`)**：采用淡暖橙底色（`#FFF8EE`）与微圆角贴纸，带有 `✦ 推荐方案` Mono 胶囊徽标，消除生硬左粗边。
    - **异步子代理便签 (`.q-subagent-note`)**：采用淡柔紫底色（`#F3F1FB`），传递优雅的后台工程状态。
    - **用户拍板决策便签 (`.user-decision-note`)**：采用淡抹茶绿底色（`#F2F7E8`）与圆圈对勾徽标（`✓ DECISION`），与上方 AI 提问形成清晰、温润、出版物级别的问答层次对撞。
18. **Sticky Quick Nav (纯净无滚动条胶囊导航)**:
    - 悬浮毛玻璃药丸（`.quick-nav`），配置 `scrollbar-width: none;` 与 `::-webkit-scrollbar { display: none; }` 隐藏原生滚动条轨道，居中自适应折行。

---

## 5. 专属质量清单 (Warm Craft QA Checklist)

- [ ] 全局背景是否为自然温润的浅暖米白（`#F7F4EC` / `#FAF7F0`），避免冷白和生硬冷灰？
- [ ] 主标题（Hero）与区块标题（Section Titles）是否严格采用原生 Songti / Serif 衬线体，字号大、行高紧凑优雅？
- [ ] 卡片边框是否柔和通透，**彻底消除了粗重生硬的黑色/深色描边**？
- [ ] 贴纸卡片是否具备**平滑回正 + 弹性上浮（`cubic-bezier(0.175, 0.885, 0.32, 1.275)`）**的生动手感？
- [ ] 推荐态/选中态（`.selected`）在 `:hover` 时是否具备专属深度跃升动效（`translateY(-14px)`），且层级优先级最高？
- [ ] 访谈/推演对话是否严格采用 **社论访谈录格式 (`.round-card`)**，杜绝通用即时通讯粗边气泡与生硬嵌套？
- [ ] 悬浮快速目录 (`.quick-nav`) 是否彻底隐藏了原生灰色横向滚动条？
- [ ] 是否具备手绘划线高亮（`.marker-highlight`）与典雅大引号等文字质感装饰？
- [ ] 整体质感是否兼具书籍出版物的典雅智序与手作手账的灵动温度？
