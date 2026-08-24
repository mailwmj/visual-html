# Soft Sky / 柔空浅蓝 — Design Tokens & Style Specification

> **Style ID**: `soft-sky`  
> **显示名称**：柔空浅蓝风 / Soft Sky Editorial  
> **核心气质**：像一份温柔的包装说明页与生活方式手册，柔和、温暖、明亮，但保留清晰的结构化骨架。

---

## 1. Design DNA & 核心原则

1. **柔和圆润但不失结构**：圆角 8–16px，卡片使用白色/半透明 Surface 搭配极淡阴影。保留细线网格作为结构锚点，结合浅蓝渐变背景与柔和光晕建立温暖氛围。
   - **禁用**：厚重投影、长拖影、强烈深色弥散阴影、高饱和渐变、emoji 堆砌、拟物糖果风。
2. **氛围色块只作背景**：浅蓝渐变背景 + 局部 radial blur（淡蓝/淡粉/薄荷）只允许出现在最底层作为环境光，绝不能覆盖文字或抢夺主体。文字必须保持极高可读性。
3. **克制信号色**：
   - 比例分配：浅蓝背景 50–60% / 白色卡片 20–30% / 文字 15–20% / 边框网格 4–6% / 信号色 3–5% / 氛围粉与薄荷 <3%。
   - **主信号色 天蓝 (`#4A9FD4`)**：Eyebrow 标头、编号、选中态指示、关键数据、小面积 CTA。
   - **第二状态色 珊瑚粉 (`#E8927C`)**：Selected 推荐态 / 重点卡片高亮，用量不超过天蓝的 40%。
   - **点缀色 淡粉 (`#F4AFCF`) & 薄荷绿 (`#9EE6C8`)**：仅作背景光晕氛围点缀，严禁直接作为正文或主按钮颜色。

---

## 2. CSS Design Tokens

```css
:root {
  /* 背景层与渐变 */
  --bg: #EAF6FC;
  --bg-deep: #D8EEF8;
  --surface-1: rgba(255, 255, 255, .86);
  --surface-2: rgba(255, 255, 255, .55);

  /* 文字层 (深蓝灰/灰蓝) */
  --text-primary: #2A3F54;
  --text-secondary: #5D7A8C;
  --text-muted: #90A8B8;

  /* 边框与网格 */
  --border: rgba(93, 179, 232, .28);
  --border-strong: rgba(93, 179, 232, .48);
  --grid-minor: rgba(93, 179, 232, .08);
  --grid-major: rgba(93, 179, 232, .14);

  /* 信号色通道 */
  --signal-blue: #4A9FD4;
  --signal-blue-soft: #7FC2EA;
  --signal-coral: #E8927C;
  --accent-pink: #F4AFCF;
  --accent-mint: #9EE6C8;

  /* 阴影 */
  --shadow-card: 0 4px 20px rgba(74, 159, 212, .06);
  --shadow-card-hover: 0 8px 28px rgba(74, 159, 212, .10);

  /* 尺寸与圆角 */
  --radius: 14px;
  --radius-sm: 8px;
  --radius-pill: 20px;
  --container: 1180px;

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

  /* 字体栈 (圆润 Display + 精确 Mono) */
  --font-display: "Nunito", "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", monospace;
}
```

---

## 3. 核心组件规范

| 组件 | 实现特征 | 关键类名 / 结构 |
|---|---|---|
| **Section Eyebrow** | `◆ 02 / PLAY ─────`，Mono 字体，天蓝色，diamond 带有 2px 圆角 | `.eyebrow`, `.diamond`, `.line` |
| **Hero Heading** | 58–78px，字重 800，行高 1.02–1.08，颜色为 `#2A3F54`（柔和深蓝灰） | `h1.hero` |
| **Spec Row** | 顶部 1px 天蓝色细线 + 4列等分 + 深蓝灰大数字 + Mono 单位 | `.spec-row`, `.spec`, `.val`, `.unit` |
| **Number Card** | 白色半透明卡片、14px 圆角、极淡阴影，天蓝大编号 | `.num-card`, `.num`, `.tag` |
| **Selected Card** | 珊瑚粉边框 + 珊瑚粉编号 + 珊瑚粉 Tag + 淡珊瑚底色 | `.num-card.selected` |
| **Status Label** | 圆角 20px (pill 胶囊状)，天蓝/珊瑚粉 1px 细边框，Mono 文本 | `.status`, `.status.coral` |
| **Feature Card** | 14px 圆角白色卡片，浅蓝渐变 Frame 预览框，柔和 hover 位移 | `.feat-card`, `.frame` |
| **Process Steps** | 白色圆角模块，左侧深蓝灰 Mono 编号，天蓝标号点缀 | `.steps`, `.step`, `.idx` |
| **Metadata Footer** | 浅灰蓝边框，Mono 字体，颜色为 `#90A8B8`，大写字母 | `footer`, `.meta-foot` |

---

## 4. 专属质量清单 (Soft Sky Quality Checklist)

- [ ] 背景为浅天蓝渐变（`#EAF6FC` → `#F5FBFE` → `#D8EEF8`），卡片为半透明白色（`rgba(255,255,255,.86)`）。
- [ ] 卡片与模块圆角在 8–16px，阴影极淡（`rgba(74,159,212,.06–.10)`），杜绝黑灰重投影。
- [ ] 信号色为天蓝 `#4A9FD4`，第二推荐态使用珊瑚粉 `#E8927C`。
- [ ] 淡粉/薄荷仅作底层背景的光晕点缀（<3%），未直接用于文字、边框或主按钮。
- [ ] 细线网格存在但柔和清晰，不干扰正文文字的阅读对比度。
- [ ] 整体气质温柔、明亮但结构规整，没有退化成营销糖果页或低质拟物电商页。
