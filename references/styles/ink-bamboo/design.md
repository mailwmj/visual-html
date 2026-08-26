# Ink Bamboo (青绿水墨竹韵风) — Design Language Reference

## 1. Visual Theme & Atmosphere

青绿水墨竹韵风（Ink Bamboo）深度融合东方传统青绿水墨插画美学与现代高阶社论排版（Oriental Editorial Typography）。全站以带有古法手工宣纸温度的米白暖调（`#F6F4EE` / `#FAF8F3`）为视口底色，在全局视口层全幅铺展 **2750×1536 原始超清青绿水墨竹画**（`assets/bamboo-bg.jpg` / 内嵌 Base64），实现整屏水墨无缝流淌与沉浸式东方意境。

界面的核心视觉特征包括：

1. **全幅无缝水墨竹韵空间（Layer 0 & Layer 1）**：
   - 全局视口（`body`）采用全屏铺展（`background-size: cover; background-position: right top; background-attachment: fixed;`），整幅画作的古法宣纸底色与右侧翠竹、节环、斜向飞白刷纹及枝头青翠竹叶浑然一体，彻底消除任何局部裁切或生硬矩形边界；
   - 正文收敛于 `<main class="main-sheet">` 通体素宣画板（`rgba(255, 255, 255, 0.92)` 搭配 `backdrop-filter: blur(8px)`），居中从容漂浮于水墨背景之上，右侧竹枝与青翠竹叶自然破框而出，搭配 1px 竹青微透边缘与水墨漫射阴影。
2. **古典宋体大标题与高阶罗马衬线排版**：
   - 标题采用典雅端庄的宋体（`"Noto Serif SC"`, `"Source Han Serif SC"`, `"Songti SC"`, `"STSong"`），行高紧凑自然；
   - 英文副标与参数单位采用大写罗马衬线体（`"Cinzel"`, `"Playfair Display"`）并配合超宽字距（`letter-spacing: 0.15em ~ 0.3em`）；正文使用高清晰度无衬线屏显字体，行高设定为 `1.85`。
3. **朱砂印章点睛（Vermilion Seal Accent）**：
   - 模块 Eyebrow 标头、章节索引、拍板决策回执与推荐徽章采用古典朱砂印章红色调（`#C03E2D` / `#D14533`），通过方正的印泥边框与朱文/白文印章质感提神醒脑，克制点缀于整体青绿素宣之中（控制在 3%~5% 视觉面积）。
4. **竹节分段与青绿多通道色谱**：
   - 容器卡片顶栏带有竹节顶环与飞白拉丝微光；列表项目采用竹叶形态修饰标记；
   - 颜色阶梯严格取自传统青绿山水矿物色：翠竹生青（`#5A8F43`）、深松墨绿（`#2B4E24`）、松石青绿（`#3C7A68`）、嫩竹浅草（`#E1EED9`）、泥金赭石（`#B88B4A`）与松烟焦墨（`#1C241B`）。

---

## 2. Color Palette & Tokens

### Core Interface Colors

| Role | Value | Hex / RGBA | CSS Token | Usage |
|---|---|---|---|---|
| Background (Xuan Paper) | `rgb(246, 244, 238)` | `#F6F4EE` | `--bg` | 全局古法宣纸米白画布底色 |
| Background (Paper Warm) | `rgb(250, 248, 243)` | `#FAF8F3` | `--bg-warm` | 页面局部宣纸高光微白底色 |
| Background (Ink Wash) | `rgb(237, 232, 222)` | `#EDE8DE` | `--bg-wash` | 代码块、参数栏与底栏微深水墨洗底色 |
| Surface (White Xuan Card)| `rgb(255, 255, 255)` | `#FFFFFF` | `--surface-card` | 素白宣纸主卡片底色 |
| Surface (Bamboo Tint) | `rgb(243, 247, 240)` | `#F3F7F0` | `--surface-card-subtle` | 浅竹绿晕底板、嵌套问答底板 |
| Surface (Celadon Wash) | `rgb(234, 242, 230)` | `#EAF2E6` | `--surface-bamboo` | 推荐卡片底色、优势卡片底板 |
| Text (Deep Pine Ink) | `rgb(28, 36, 27)` | `#1C241B` | `--text-primary` | 宋体大标题、主正文（高对比松烟焦墨） |
| Text (Sage Slate Ink) | `rgb(74, 86, 70)` | `#4A5646` | `--text-secondary` | 导读段落、次级说明文字 |
| Text (Muted Cloud Ink) | `rgb(130, 142, 126)` | `#828E7E` | `--text-muted` | 注释、页脚、等宽元数据标签 |
| Border (Bamboo Subtle) | `rgba(43, 78, 36, 0.12)` | `rgba(43,78,36,.12)` | `--border` | 1px 竹青微边框、标准分割线 |
| Border (Bamboo Strong) | `rgba(43, 78, 36, 0.24)` | `rgba(43,78,36,.24)` | `--border-strong` | 高对比线、活跃外轮廓 |
| Border (Vermilion Seal) | `rgba(192, 62, 45, 0.28)` | `rgba(192,62,45,.28)` | `--border-vermilion` | 朱砂印章与警示边框 |

### CSS Design Tokens

```css
:root {
  /* 背景层：古法宣纸与水墨洗底 */
  --bg: #F6F4EE;
  --bg-warm: #FAF8F3;
  --bg-wash: #EDE8DE;
  
  /* 表面层 (Surface) */
  --surface-card: #FFFFFF;
  --surface-card-subtle: #F3F7F0;
  --surface-bamboo: #EAF2E6;
  --surface-overlay: rgba(255, 255, 255, 0.92);

  /* 文字层 (松烟焦墨 / 苍石墨 / 云烟淡墨) */
  --text-primary: #1C241B;
  --text-secondary: #4A5646;
  --text-muted: #828E7E;
  --text-inverse: #FFFFFF;

  /* 核心主行动色 (翠竹生青与深翠竹节) */
  --signal-bamboo: #5A8F43;
  --signal-bamboo-hover: #4A7A36;
  --signal-bamboo-dark: #2B4E24;
  --signal-bamboo-light: #E1EED9;

  /* 朱砂印章多色通道 */
  --signal-vermilion: #C03E2D;
  --signal-vermilion-hover: #A83324;
  --signal-vermilion-light: #FBEAE7;
  --signal-vermilion-text: #7A1E14;

  /* 矿物辅助多色通道 */
  --signal-jade: #3C7A68;
  --signal-jade-light: #E2F0EC;
  --signal-ocher: #B88B4A;
  --signal-ocher-light: #F6EFE2;

  /* 边框与阴影 (宣纸微光与水墨晕染) */
  --border: rgba(43, 78, 36, 0.12);
  --border-strong: rgba(43, 78, 36, 0.24);
  --border-vermilion: rgba(192, 62, 45, 0.28);
  --shadow-card: 0 4px 20px rgba(32, 50, 28, 0.05), 0 1px 3px rgba(32, 50, 28, 0.03);
  --shadow-card-hover: 0 14px 36px rgba(32, 50, 28, 0.10), 0 2px 6px rgba(32, 50, 28, 0.04);
  --shadow-seal: 0 2px 8px rgba(192, 62, 45, 0.18);

  /* 交互与缓动 */
  --ease-ink: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-hover: 0.3s;

  /* 尺寸与圆角 (中式温润微圆角) */
  --radius: 12px;
  --radius-sm: 8px;
  --radius-xs: 4px;
  --radius-pill: 100px;
  --container: 1080px;

  /* 字体栈 (Songti Serif + Clean Sans + Mono) */
  --font-serif: "Noto Serif SC", "Source Han Serif SC", "Songti SC", "STSong", "SimSun", "Cinzel", "Playfair Display", serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans SC", "Microsoft YaHei", "Inter", sans-serif;
  --font-mono: "IBM Plex Mono", "JetBrains Mono", "SFMono-Regular", Consolas, monospace;
}
```

---

## 3. Mandatory Skeleton Contract (强制结构契约)

```html
<!-- Layer 0: Body 直接挂载全幅无缝 2750 原画超清竹画背景 -->
<!-- Layer 1: Carrier Board (居中通体素宣水墨画板) -->
<main class="main-sheet">
  <!-- Layer 2: All Semantic Components go here -->
</main>
```

```css
body {
  background-color: var(--bg);
  background-image: url('assets/bamboo-bg.jpg'); /* 或内嵌 Base64 */
  background-repeat: no-repeat;
  background-position: right top;
  background-size: cover;
  background-attachment: fixed;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: high-quality;
  padding: 40px 24px 80px;
}

.main-sheet {
  max-width: 1080px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: 0 20px 60px rgba(32, 50, 28, 0.08), 0 2px 10px rgba(32, 50, 28, 0.03);
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
| **Hero Title** | `h1.hero` | `clamp(32px, 4vw, 44px)` | `800` | `1.28` | `-0.01em` | `var(--font-serif)` | 页面唯一主标题，支持主动语义分行 |
| **Lead Paragraph**| `.lead` | `16px` | `400` | `1.85` | `0.01em` | `var(--font-sans)` | 导读段落，典雅从容 |
| **Section Title** | `h2.section-title` | `24px` | `700` | `1.35` | `0` | `var(--font-serif)` | 阶段大标题 |
| **Card Title** | `h3` | `17px` | `700` | `1.4` | `0` | `var(--font-serif)` | 模块/卡片标题 |
| **Sub Section** | `h4` | `14px` | `600` | `1.5` | `0.02em` | `var(--font-sans)` | 子章节小标题 |
| **Body Text** | `p`, `.rich-text` | `14px` | `400` | `1.85` | `0.01em` | `var(--font-sans)` | 正文长篇论述，行距宽松透气 |
| **Stat Number** | `.stat-val` | `42px` | `800` | `1.1` | `-0.02em` | `var(--font-serif)` | 宏观统计数值 |
| **Spec Value** | `.spec .val` | `20px` | `700` | `1.2` | `0` | `var(--font-serif)` | 参数规格数值 |
| **Mono Metadata** | `.unit`, `footer` | `11px` | `600` | `1.4` | `0.12em` | `var(--font-mono)` | 英文大写单位与页脚元数据 |

---

## 5. Do's and Don'ts

### 7 项核心金律 (Do's)
1. **Do** 必须使用全幅无缝背景铺展（`background-size: cover; background-attachment: fixed;`），使宣纸与竹画自然相融，杜绝硬切硬断；
2. **Do** 主画板必须优雅居中，搭配微透宣纸质感（`rgba(255, 255, 255, 0.92)` 与轻微模糊），使背景水墨在周围自然流淌；
3. **Do** 大标题、章节标题与数据卡片必须优先使用高阶古典宋体（`"Noto Serif SC"`, `"Songti SC"`）；
4. **Do** 标头、推荐态与拍板确认必须点缀朱砂印章红色调（`#C03E2D`），营造古典篆刻点睛之笔；
5. **Do** 严格使用矿物青绿色谱（翠竹 `#5A8F43`、深竹 `#2B4E24`、松石 `#3C7A68`、浅草 `#E1EED9`）表达层级与状态；
6. **Do** 英文参数、单位、页脚与标签必须使用 Mono 等宽字体配合超宽字距（`letter-spacing: 0.12em+`）；
7. **Do** 100% 完整保留长文细节，所有未经特殊卡片归类的长篇段落一律放入 `.rich-text` 中完整呈现。

### 7 项严禁红线 (Don'ts)
1. **Don't** 严禁出现局部贴图造成的硬边缘矩形方块（Hard rectangular clip edges）；
2. **Don't** 严禁使主画板偏移过度导致左侧突兀留空失衡；
3. **Don't** 严禁使用有损低质素材，必须保持 2750 原画超清源；
4. **Don't** 严禁出现未经裁切的顶部悬浮直角色条（Anti-Pattern: Unclipped top accent bars）；
5. **Don't** 严禁在标题与卡片之间压缩间距导致文字下延笔画（Descender）被裁切；
6. **Don't** 严禁在生成的 HTML 中输出任何 `<!-- 更多内容省略 -->` 等偷懒占位符；
7. **Don't** 严禁随意使用现代无序 Emoji（如 🚀, 💡, 🔥），应用朱砂印记（`印` / `卷` / `◆` / `✦`）或中式标点（`「 」`, `【 】`）替代。

---

## 6. Mermaid Theme Configuration (在线增强与离线降级)

在线增强时，在 `</body>` 前注入以下匹配青绿水墨竹韵风的 `themeVariables`；最终交付仍需使用 `references/scripts/bundle_offline.py` 生成静态 SVG fallback：

```js
mermaid.initialize({
  startOnLoad: true,
  theme: 'base',
  themeVariables: {
    darkMode: false,
    background: '#FAF8F3',
    primaryColor: '#EAF2E6',
    primaryTextColor: '#1C241B',
    primaryBorderColor: '#5A8F43',
    lineColor: '#2B4E24',
    secondaryColor: '#F3F7F0',
    tertiaryColor: '#FFFFFF',
    fontFamily: '"Noto Serif SC", "Songti SC", serif',
    fontSize: '13px'
  }
});
```

---

## 7. Quality Checklist

- [ ] **全幅无缝背景**：是否全屏铺展且与宣纸底色自然一体，无生硬边缘？
- [ ] **居中通体素宣画板**：主画板是否居中且具微透水墨漫射质感？
- [ ] **宋体字体栈**：大标题与卡片标题是否已正确应用古典宋体字体栈？
- [ ] **朱砂印章点睛**：标头与推荐项是否具备精致克制的朱砂印章点缀（面积 3%~5%）？
- [ ] **青绿山水色谱**：色彩是否严格基于翠竹、深竹、松石与素宣，无粗黑边与荧光色干扰？
- [ ] **信息完整度**：原文 18 项语义骨架与全部长文细节是否 100% 完整保留？
- [ ] **离线交付**：是否运行离线打包器；断网时是否使用系统字体、静态 SVG 和已内联的本地资源？
