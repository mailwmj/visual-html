# Technical Editorial Dark — Design Tokens & Style Specification

> **Style ID**: `industrial-dark`  
> **显示名称**：暗色工业档案风 / Technical Editorial Dark  
> **核心气质**：像一份高级工业设计手册，冷静、克制、强结构、高精度。

---

## 1. Design DNA & 核心原则

1. **硬边工业感**：圆角 0–2px（最多 4px），1px 细边框，平面 Surface，直线，方形状态标签，大号数字。
   - **禁用**：12–24px 大圆角、毛玻璃拟态、模糊重阴影、软糯渐变、大量 emoji、SaaS Dashboard 模板感。
2. **CAD 技术网格**：近黑底色搭配极淡 CAD 网格（4–8% 不透明度），作为结构标尺，绝不能抢夺文字可读性。
3. **严格控制信号色**：
   - 比例分配：背景 55–65% / 文字 25–35% / 边框网格 5–8% / 信号色 3–7%。
   - **信号绿 (`#67E38B`)**：主信号（section marker / 编号 / active / READY / LIVE / 关键数字 / 小面积 CTA）。
   - **信号紫 (`#8C7CFF`)**：第二状态通道（selected / 推荐态 / 双状态对比），用量不超过绿色的 40%。
   - **警告黄 (`#E7E65D`)**：极少量，用于警告与特殊状态。

---

## 2. CSS Design Tokens

```css
:root {
  /* 背景层 */
  --bg: #090C0B;
  --bg-deep: #060808;
  --surface-1: #0D1110;
  --surface-2: #111615;

  /* 文字层 */
  --text-primary: #F2F3EF;
  --text-secondary: #A8ADA8;
  --text-muted: #6F7672;

  /* 边框与网格 */
  --border: #2A302E;
  --border-strong: #404743;
  --grid-minor: rgba(130, 150, 140, .05);
  --grid-major: rgba(130, 150, 140, .075);

  /* 信号色通道 */
  --signal-green: #67E38B;
  --signal-green-soft: #A0F0B7;
  --signal-violet: #8C7CFF;
  --warning: #E7E65D;

  /* 尺寸与间距 */
  --radius: 2px;
  --container: 1240px;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 96px;
  --space-10: 128px;

  /* 字体栈 */
  --font-display: "Inter", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", "Roboto Mono", monospace;
}
```

---

## 3. 核心组件规范

| 组件 | 实现特征 | 关键类名 / 结构 |
|---|---|---|
| **Section Eyebrow** | `◆ 02 / PLAY ─────`，Mono 字体，信号绿，1px 横线 | `.eyebrow`, `.diamond`, `.line` |
| **Hero Heading** | 64–88px，字重 800–850，行高 0.98–1.05，短句且允许中文主动换行 | `h1.hero` |
| **Spec Row** | 顶部 1px 信号绿贯穿线 + 4列等分 + 大数字 + Mono 单位 | `.spec-row`, `.spec`, `.val`, `.unit` |
| **Number Card** | `01` 第一层 → 标题 → 正文，1px 边框，2px 圆角，深灰 surface | `.num-card`, `.num`, `.tag` |
| **Selected Card** | 紫色边框 + 紫色编号 + 紫色 Tag（第二状态通道） | `.num-card.selected` |
| **Status Label** | 方形，1px 边框，0–2px 圆角，Mono 文本 | `.status`, `.status.violet` |
| **Feature Card** | 硬边 ghost layer 错位阴影（5–8px 硬偏移），禁用模糊投影 | `.feat-card` (`::after` 错位块) |
| **Process Steps** | 硬边框模块，左侧超大 Mono 编号，右侧标题与正文 | `.steps`, `.step`, `.idx` |
| **Metadata Footer** | 顶部 1px 边框，Mono、muted、大写字母元数据 | `footer`, `.meta-foot` |

---

## 4. 专属质量清单 (Industrial Dark Quality Checklist)

- [ ] 背景为 `#090C0B` 近黑底色，网格使用 4–8% 极淡线，绝不影响文字阅读。
- [ ] 所有卡片、按钮、模块圆角严格控制在 0–2px（最多 ≤4px），无大圆角。
- [ ] 无毛玻璃、无扩散模糊投影（选中/强调仅用 1px 边框或硬偏移色块）。
- [ ] 信号绿用于主要焦点与 Eyebrow，信号紫仅作第二状态对比（≤绿色的 40%）。
- [ ] 参数、序号、标签、页脚均使用 Mono 等宽字体。
- [ ] 整体气质像“精密工业档案 / 硬件设计手册”，无 SaaS 模板感或赛博霓虹感。
