# Ink Calligraphy (宣纸泼墨挥毫风) — Design Language Reference

## 1. Visual Theme & Atmosphere

宣纸泼墨挥毫风（Ink Calligraphy）深度融合中国传统大字榜书/狂草书法美学与现代高阶社论排版（Oriental Calligraphic Editorial）。设计灵感源自古代文人墨客在案头挥毫泼墨的生动场景：粗粝天然的古法生宣纸、行笔疾书时笔锋自然甩落的墨滴微星（Natural Ink Splatters）、枯笔飞白的力道张力，以及画龙点睛的朱砂篆刻方印。

界面的核心视觉特征包括：

1. **粗粝古法生宣背景与自然落墨微星（Layer 0: Ambient Xuan Canvas）**：
   - 视口基底选用温润古朴的古法生宣米黄调（`#F5F2EB` / `#FAF7F0`），叠加微观皮纸植物纤维杂质与帘纹糙面滤镜（Rough Mulberry Fiber Grain），彻底摆脱工业纯白与冷光屏幕的冰冷感；
   - 页面背景与标题周围点缀自然行笔时甩落的**有机墨滴与墨星（Ink Droplets & Splatters）**，大小从 1~3px 的微观墨星到 4~8px 的落墨水晕，模拟真实书法创作时的自然偶得与淋漓墨趣。
2. **苍劲狂草/榜书大标题与古典宋体正文系统（Typography Scale）**：
   - Hero 主标题与章节大标题引入苍劲流畅的行草/榜书毛笔体（`"Ma Shan Zheng"`, `"Long Cang"` 或书法回退栈），笔势雄浑，气贯长虹；
   - 副标题与卡片标题使用骨力挺拔的高阶古典宋体（`"Noto Serif SC"`, `"Source Han Serif SC"`, `"Songti SC"`）；
   - 正文使用高清晰度无衬线屏显字体，行高设定为 `1.85`，留白透气，深具文人墨卷的雅致秩序。
3. **朱砂篆刻印章点睛（Vermilion Cinnabar Seal）**：
   - 模块 Eyebrow 标头、章节索引、拍板决策（Approved）与推荐徽章采用古典矿物朱砂红（`#C23531` / `#D43825`），以方圆篆刻印泥边框与朱文/白文印章形式点缀，控制在 3%~5% 的视觉面积，达到提神醒脑的平衡效果。
4. **中国画“墨分五色”阶梯谱系（Five Shades of Ink）**：
   - 颜色阶梯严格取自传统墨法：焦墨（`#141312`）、浓墨（`#2B2927`）、重墨（`#524E48`）、淡墨（`#7E7972`）、清墨洗底（`#EBE6DC`）与温润古赭（`#B37D36`）。
5. **毛笔飞白扫墨横纹与撕边质感（Dry Brush Dividers）**：
   - 章节过渡与数据卡片采用枯笔飞白拉丝的横向墨线，取代机械单调的普通灰色实线。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (Xuan Canvas) | `rgb(245, 242, 235)` | `#F5F2EB` | `--bg` | 全局古法生宣纸画布底色 |
| Background (Paper Warm) | `rgb(250, 247, 240)` | `#FAF7F0` | `--bg-warm` | 页面局部宣纸高光微白底色 |
| Background (Ink Wash) | `rgb(235, 230, 220)` | `#EBE6DC` | `--bg-wash` | 代码块、参数栏与引文微深水墨洗底色 |
| Surface (White Xuan Board)| `rgba(255, 253, 248, 0.94)` | `rgba(255,253,248,0.94)` | `--surface-card` | 素宣悬浮主卡片底色 |
| Surface (Paper Subtle) | `rgb(247, 244, 238)` | `#F7F4EE` | `--surface-card-subtle` | 问答底板、嵌套微卡片 |
| Surface (Wash Tint) | `rgb(240, 235, 224)` | `#F0EBE0` | `--surface-wash` | 优势推荐卡片、重点提炼底板 |
| Text (Burnt Pine Ink / 焦墨) | `rgb(20, 19, 18)` | `#141312` | `--text-primary` | 毛笔大标题、核心统计数字、主正文 |
| Text (Dense Ink / 浓重墨) | `rgb(82, 78, 72)` | `#524E48` | `--text-secondary` | 导读段落、次级说明文字 |
| Text (Muted Ink / 淡墨) | `rgb(126, 121, 114)` | `#7E7972` | `--text-muted` | 注释、页脚、等宽元数据标签 |
| Border (Ink Subtle) | `rgba(20, 19, 18, 0.10)` | `rgba(20,19,18,.10)` | `--border` | 1px 柔和淡墨微边框、标准分割线 |
| Border (Ink Strong) | `rgba(20, 19, 18, 0.22)` | `rgba(20,19,18,.22)` | `--border-strong` | 高对比焦墨边线、活跃外轮廓 |
| Signal (Vermilion Seal / 朱砂) | `rgb(194, 53, 49)` | `#C23531` | `--signal-seal` | 朱砂篆刻印章、核心状态点睛 |
| Signal (Seal Light / 印泥微晕) | `rgb(253, 238, 236)` | `#FDEEEC` | `--signal-seal-light` | 印章背景浅晕、警告/重点徽章底色 |
| Signal (Ocher Mineral / 赭石) | `rgb(179, 125, 54)` | `#B37D36` | `--signal-ocher` | 暖金古朴辅助通道、次要标记 |

### CSS Design Tokens

```css
:root {
  /* 背景层：古法生宣与水墨洗底 */
  --bg: #F5F2EB;
  --bg-warm: #FAF7F0;
  --bg-wash: #EBE6DC;
  
  /* 表面层 (Surface) */
  --surface-card: rgba(255, 253, 248, 0.94);
  --surface-card-subtle: #F7F4EE;
  --surface-wash: #F0EBE0;
  --surface-overlay: rgba(255, 253, 248, 0.96);

  /* 文字层 (墨分五色：焦墨 / 浓墨 / 重墨 / 淡墨) */
  --text-primary: #141312;
  --text-secondary: #524E48;
  --text-muted: #7E7972;
  --text-subtle: #A39E96;
  --text-inverse: #FAF7F0;

  /* 核心主行动色 (朱砂印泥红) */
  --signal-seal: #C23531;
  --signal-seal-hover: #A82A27;
  --signal-seal-dark: #7A1A17;
  --signal-seal-light: #FDEEEC;
  --signal-seal-border: rgba(194, 53, 49, 0.28);

  /* 矿物辅助色通道 (古赭石 & 石青花青) */
  --signal-ocher: #B37D36;
  --signal-ocher-light: #F8F2E6;
  --signal-cyan: #325B6C;
  --signal-cyan-light: #E8F0F4;

  /* 边框与阴影 (焦墨微痕与水墨漫射柔影) */
  --border: rgba(20, 19, 18, 0.10);
  --border-strong: rgba(20, 19, 18, 0.22);
  --border-seal: rgba(194, 53, 49, 0.32);
  --shadow-card: 0 4px 20px rgba(20, 19, 18, 0.04), 0 1px 3px rgba(20, 19, 18, 0.02);
  --shadow-card-hover: 0 14px 36px rgba(20, 19, 18, 0.08), 0 2px 6px rgba(20, 19, 18, 0.03);
  --shadow-seal: 0 2px 8px rgba(194, 53, 49, 0.20);

  /* 交互与缓动 */
  --ease-ink: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-hover: 0.3s;

  /* 尺寸与圆角 (中式温润微圆角) */
  --radius: 10px;
  --radius-sm: 6px;
  --radius-xs: 3px;
  --radius-pill: 999px;
  --container: 1080px;

  /* 字体栈 (Ma Shan Zheng Calligraphy + Noto Serif + Sans + Mono) */
  --font-calligraphy: "Ma Shan Zheng", "Long Cang", "Zhi Mang Xing", "STKaiti", "KaiTi", "Songti SC", cursive, serif;
  --font-serif: "Noto Serif SC", "Source Han Serif SC", "Songti SC", "STSong", "SimSun", "Cinzel", "Playfair Display", serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans SC", "Microsoft YaHei", "Inter", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", Consolas, monospace;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

```html
<!-- Layer 0: Ambient Xuan Paper Texture with Mulberry Fibers & Organic Ink Splatters -->
<div class="ambient-xuan-bg" aria-hidden="true">
  <!-- SVG Filter for Xuan Paper Grain & Rough Texture -->
  <svg class="paper-texture-filter" width="0" height="0">
    <filter id="xuan-grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" result="noise" />
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0.035 0" />
      <feComposite in2="SourceGraphic" in="gl" operator="in" />
    </filter>
  </svg>
  
  <!-- Organic Ink Splatters & Drops (自然飞溅墨滴) -->
  <div class="ink-splatter ink-sp-1"></div>
  <div class="ink-splatter ink-sp-2"></div>
  <div class="ink-splatter ink-sp-3"></div>
  <div class="ink-splatter ink-sp-4"></div>
  <div class="ink-splatter ink-sp-5"></div>
</div>

<!-- Layer 1: Carrier Board (素宣悬浮长卷画板) -->
<main class="main-sheet">
  <!-- Layer 2: All Semantic Components go here -->
</main>
```

```css
/* Xuan Paper Ambient Layer */
body {
  background-color: var(--bg);
  background-image: 
    radial-gradient(ellipse at 85% 10%, rgba(179, 125, 54, 0.04), transparent 50%),
    radial-gradient(ellipse at 15% 80%, rgba(20, 19, 18, 0.03), transparent 60%);
  color: var(--text-primary);
  font-family: var(--font-sans);
  line-height: 1.85;
  padding: 40px 24px 80px;
  position: relative;
  min-height: 100vh;
}

/* Rough Xuan Paper Noise Overlay */
.ambient-xuan-bg::before {
  content: "";
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.045'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
}

/* Organic Ink Splatters (挥毫墨滴微星) */
.ink-splatter {
  position: fixed;
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
  background: radial-gradient(circle, rgba(20, 19, 18, 0.85) 0%, rgba(20, 19, 18, 0.35) 70%, transparent 100%);
}
.ink-sp-1 { width: 5px; height: 5px; top: 7%; right: 12%; opacity: 0.55; }
.ink-sp-2 { width: 3px; height: 3px; top: 14%; right: 9%; opacity: 0.40; }
.ink-sp-3 { width: 7px; height: 6px; top: 22%; left: 8%; opacity: 0.45; transform: rotate(25deg); }
.ink-sp-4 { width: 2px; height: 2px; top: 48%; right: 6%; opacity: 0.35; }
.ink-sp-5 { width: 4px; height: 4px; bottom: 18%; left: 11%; opacity: 0.40; }

/* Main Carrier Board */
.main-sheet {
  max-width: var(--container);
  margin: 0 auto;
  background: var(--surface-card);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: 0 16px 48px rgba(20, 19, 18, 0.05), 0 1px 4px rgba(20, 19, 18, 0.02);
  padding: 56px 48px;
  position: relative;
  z-index: 1;
}
```

---

## 4. Typography Scale & Rules

### 全字阶量化表

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Stack | Role |
|---|---|---|---|---|---|---|---|
| **Eyebrow Tag** | `.eyebrow` | `11px` | `700` | `1.4` | `0.18em` | `var(--font-mono)` | 章节大写索引、朱砂印章标头 |
| **Hero Title** | `h1.hero` | `clamp(34px, 4.5vw, 48px)` | `400` | `1.25` | `0.02em` | `var(--font-calligraphy)` | 页面唯一主标题，书法榜书，支持主动语义分行 |
| **Lead Paragraph**| `.lead` | `16px` | `400` | `1.85` | `0.01em` | `var(--font-sans)` | 导读段落，文人雅致从容 |
| **Section Title** | `h2.section-title` | `24px` | `700` | `1.35` | `0` | `var(--font-serif)` | 阶段大标题，宋体端庄 |
| **Card Title** | `h3` | `17px` | `700` | `1.4` | `0` | `var(--font-serif)` | 模块/卡片标题 |
| **Sub Section** | `h4` | `14px` | `600` | `1.5` | `0.02em` | `var(--font-sans)` | 子章节小标题 |
| **Body Text** | `p`, `.rich-text` | `14.5px` | `400` | `1.85` | `0.01em` | `var(--font-sans)` | 正文长篇论述，行距疏朗 |
| **Stat Number** | `.stat-val` | `42px` | `800` | `1.1` | `-0.02em` | `var(--font-serif)` | 宏观统计数值 |
| **Spec Value** | `.spec .val` | `20px` | `700` | `1.2` | `0` | `var(--font-serif)` | 参数规格数值 |
| **Mono Metadata** | `.unit`, `footer` | `11px` | `600` | `1.4` | `0.12em` | `var(--font-mono)` | 英文大写单位与页脚元数据 |

---

## 5. Signature Component Patterns (特征组件规范)

### 1. 朱砂篆刻印章标头 (Vermilion Seal Eyebrow)
```html
<div class="eyebrow">
  <span class="seal-mark">墨</span>
  <span>01 / CALLIGRAPHIC_ESSENCE</span>
  <span class="brush-trail"></span>
</div>
```
```css
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: var(--signal-seal);
  margin-bottom: 16px;
}
.seal-mark {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  background: var(--signal-seal);
  color: #FAF7F0;
  font-family: var(--font-calligraphy);
  font-size: 11px;
  border-radius: 2px;
  box-shadow: 0 1px 4px rgba(194, 53, 49, 0.25);
}
.brush-trail {
  width: 28px;
  height: 1.5px;
  background: linear-gradient(90deg, var(--signal-seal) 0%, transparent 100%);
}
```

### 2. 飞白水墨横向分割线 (Dry Brush Stroke Divider)
```html
<div class="brush-divider" aria-hidden="true">
  <svg viewBox="0 0 1000 12" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0 6C150 5 300 8 500 6C700 4 850 7 1000 6" stroke="rgba(20, 19, 18, 0.18)" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="8 3 14 2 20 4 3 2"/>
  </svg>
</div>
```

### 3. 朱批手札提示框 (Vermilion Inscribed Admonition)
```html
<div class="admonition admonition-tip">
  <div class="admonition-seal">批</div>
  <div class="admonition-content">
    <h4>古法笔意提示</h4>
    <p>计白当黑，知白守黑。页面留白不是空无，而是气韵流转之所在。</p>
  </div>
</div>
```

---

## 6. Do's and Don'ts

### 7 项核心金律 (Do's)
1. **Do** 必须保持古法生宣米黄温润底色与微观粗糙纤维噪点，杜绝冷光刺眼的无质感白底；
2. **Do** 视口与大标题周围必须有克制、自然的飞溅墨滴微星（Ink Splatters），营造真实案头落墨之美；
3. **Do** Hero 主标题与阶段标题优先采用苍劲毛笔书法体（`"Ma Shan Zheng"`）或高阶古典宋体；
4. **Do** 标头、推荐卡片与拍板确认必须点缀朱砂印章红色调（`#C23531`），面积控制在 3%~5%；
5. **Do** 严格遵循“墨分五色”（焦、浓、重、淡、清）的明度秩序传达信息层级；
6. **Do** 必须在容器与卡片间保持充裕疏朗的“计白当黑”留白空间，行高不低于 1.85；
7. **Do** 100% 完整保留长篇长文本细节，所有未经特殊卡片归类的长篇论述一律放入 `.rich-text` 中完整呈现。

### 7 项严禁红线 (Don'ts)
1. **Don't** 严禁大面积铺洒黑色形成脏乱污迹，墨滴飞溅必须精巧微观（1~8px），严禁遮挡任何文字；
2. **Don't** 严禁使用生硬现代的荧光高亮色（如荧光绿、电光紫），只能使用矿物朱砂、古赭与石青；
3. **Don't** 严禁出现未经裁切的顶部悬浮直角色条（Anti-Pattern: Unclipped top accent bars）；
4. **Don't** 严禁在标题与卡片之间压缩间距导致文字下延笔画（Descender）被裁切；
5. **Don't** 严禁在生成的 HTML 中输出任何 `<!-- 更多内容省略 -->` 等偷懒占位符；
6. **Don't** 严禁随意使用现代无序 Emoji（如 🚀, 💡, 🔥），应用朱砂印记（`印` / `卷` / `批` / `◆` / `✦`）或中式标点（`「 」`, `【 】`）替代；
7. **Don't** 严禁将卡片漂白为生硬的冷白矩形，必须保留宣纸微透（`rgba(255, 253, 248, 0.94)`）与淡墨边框。

---

## 7. Mermaid Theme Configuration

在线增强时，在 `</body>` 前注入以下匹配宣纸泼墨挥毫风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: 'base',
  themeVariables: {
    darkMode: false,
    background: '#FAF7F0',
    primaryColor: '#F0EBE0',
    primaryTextColor: '#141312',
    primaryBorderColor: '#141312',
    lineColor: '#524E48',
    secondaryColor: '#F7F4EE',
    tertiaryColor: '#FFFFFF',
    fontFamily: '"Noto Serif SC", "Songti SC", serif',
    fontSize: '13px'
  }
});
```

---

## 8. Quality Checklist

- [ ] **古法宣纸粗糙底色**：是否具备生宣纸温润底色与微观纤维颗粒感，杜绝生硬纯白？
- [ ] **自然落墨飞溅墨星**：视口四周与重点区域是否有点缀克制自然的有机墨滴（Ink Splatters）？
- [ ] **毛笔书法字体栈**：大标题是否正确应用书法体（`Ma Shan Zheng`）及宋体/楷体回退栈？
- [ ] **朱砂印章点睛**：标头与关键推荐项是否具备方正精致的朱砂印章点缀（面积 3%~5%）？
- [ ] **墨分五色色谱**：色彩层级是否清晰严谨（焦墨标题、浓墨正文、重墨导读、淡墨注释）？
- [ ] **信息完整度**：原文 18 项语义骨架与全部长文细节是否 100% 完整保留？
- [ ] **离线交付**：断网时是否使用系统字体、静态 SVG 和已内联的本地资源？
