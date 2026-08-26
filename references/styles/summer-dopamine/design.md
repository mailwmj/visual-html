# Summer Dopamine (夏日多巴胺风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Summer Dopamine（夏日多巴胺风 / Summer Vibe）将夏日汽水、元气运动与高饱和多巴胺色彩升华为界面语言。界面以**高明度高饱和的四色流光渐变网格（粉 `#FF66B2`、蓝 `#0077FF`、绿 `#00E676`、黄 `#FFEA00`）**为全屏背景，搭配**白透大圆角毛玻璃卡片（`rgba(255, 255, 255, 0.88)` + `blur(28px) saturate(140%)`）**，释放极致的元气活力，同时确保深墨文字的高清晰阅读舒适度。

---

## 2. Color Palette & Tokens

### Core Colors

```css
:root {
  --bg-gradient-1: #FF66B2;
  --bg-gradient-2: #0077FF;
  --bg-gradient-3: #00E676;
  --bg-gradient-4: #FFEA00;
  
  --surface-1: rgba(255, 255, 255, 0.22);
  --surface-card: rgba(255, 255, 255, 0.88);
  --glass-blur: blur(28px) saturate(140%);

  --text-primary: #111827;
  --text-hero: #FFFFFF;
  --text-secondary: #374151;
  --text-muted: #6B7280;

  --signal-pink: #FF66B2;
  --signal-blue: #0077FF;
  --signal-green: #00E676;
  --signal-yellow: #FFD600;

  --shadow-glass: 0 16px 40px rgba(0, 50, 150, 0.12), inset 0 1px 1px rgba(255, 255, 255, 0.9);
  --shadow-glass-hover: 0 24px 54px rgba(0, 50, 150, 0.2), inset 0 1px 2px rgba(255, 255, 255, 1);

  --radius: 24px;
  --radius-sm: 14px;
  --radius-pill: 999px;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

生成任何 Summer Dopamine 页面时，必须包含以下 Layer 0 高明度多巴胺流光背景层：

```css
/* 全局固定高明度盛夏四色流光背景 */
body::before {
  content: "";
  position: fixed;
  inset: -60px;
  z-index: -1;
  background: 
    radial-gradient(circle at 10% 20%, #FF66B2 0%, transparent 55%),
    radial-gradient(circle at 90% 15%, #0077FF 0%, transparent 55%),
    radial-gradient(circle at 15% 85%, #00E676 0%, transparent 55%),
    radial-gradient(circle at 85% 90%, #FFEA00 0%, transparent 55%),
    linear-gradient(135deg, #0077FF 0%, #FF66B2 100%);
  filter: blur(50px) saturate(140%);
  opacity: 0.95;
  pointer-events: none;
}
```

---

## 4. Do's and Don'ts

### Do's (7 项金律)

1. **Do 必须使用高明度四色多巴胺渐变网格** — 保持元气明快。
2. **Do 卡片使用白透毛玻璃（`rgba(255, 255, 255, 0.88)` + `blur(28px)`）** — 阻断背景，确保正文字体深邃清晰。
3. **Do 大标题使用纯白粗黑体搭配柔和文字投影**。
4. **Do 保持 24px 饱满大圆角与弹簧回弹动效**。
5. **Do 正文使用深黑墨色（`#111827` / `#374151`）**。

### Don'ts (7 项红线)

1. **Don't 篡改为深色夜景暗黑底**。
2. **Don't 丢失白透毛玻璃的模糊滤镜与内发光边框**。
3. **Don't 在正文上使用低对比度彩色文字**。
4. **Don't 使用生硬直角（0px）**。
