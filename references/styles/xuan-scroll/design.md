# Xuan Scroll (宣卷留白风) — Design Language Reference

## 1. Visual Theme & Atmosphere

Xuan Scroll is a quiet calligraphic editorial system: one continuous sheet of Xuan paper, one directional brush gesture, and enough untouched space for the argument to breathe. It translates calligraphy through stroke rhythm, pressure, wetness, and composition rather than through decorative ink effects.

The spatial archetype is **Direct Immersive Flow**. Web content sits directly on a warm paper canvas; there is no floating glass board and no stack of generic cards. PPT uses one 16:9 paper page per slide, with an explicit safe area and a single visual thesis.

### Core Visual DNA

1. Low-contrast Xuan paper fibers, curtain grain, and restrained deckled edges.
2. Three authored brush gestures: center-tip hairline, side-tip broad stroke, and dry-brush broken stroke.
3. Asymmetric scroll rhythm: a narrow index rail, a readable text measure, and a quiet annotation margin.
4. Calligraphic display type used for short titles only; Song/serif type carries the body.
5. Cinnabar seals and colophons used as provenance/status marks, not as a universal badge system.
6. Ink expressed as continuous wetness, density, pressure, and speed variables.

### Reference Boundary

- **Preserve:** Xuan paper warmth, brush-written energy, ink value hierarchy, seal culture, long-form fidelity.
- **Adapt:** scroll unfolding becomes section rhythm; colophons become source/metadata rails; ink diffusion becomes authored SVG edge softness.
- **Exclude:** full-page calligraphy photos, WebGL smoke, cursor ink trails, random splatter fields, glassmorphism, and generic rounded white cards.
- **Unknown:** exact paper brand and font availability. The system must remain readable with system fallbacks and should expose paper behavior as qualitative tokens, not physical claims.

## 2. Color Palette & Tokens

The palette is mostly paper and ink. Cinnabar is a small semantic signal; ochre is reserved for archival or secondary annotation. No gradient is needed to communicate ink depth.

| Role | Value | Token | Use |
|---|---|---|---|
| Raw paper canvas | `#F1ECE1` | `--paper` | Full-page background |
| Paper highlight | `#FAF7EF` | `--paper-light` | Local text backing and print fallback |
| Paper wash | `#E6DED0` | `--paper-wash` | Quoted passages and treated-paper strips |
| Focus ink | `#191714` | `--ink` | Titles, body, rules |
| Dense soot | `#514B43` | `--ink-dense` | Lead, labels, chart axes |
| Faded ink | `#91897D` | `--ink-faded` | Captions, metadata, disabled states |
| Cinnabar | `#B83A2E` | `--seal` | One seal, warning, active marker |
| Aged ochre | `#987340` | `--ochre` | Source notes and archival accents |

```css
:root {
  --paper: #F1ECE1;
  --paper-light: #FAF7EF;
  --paper-wash: #E6DED0;
  --paper-deep: #D7CCBA;
  --ink: #191714;
  --ink-dense: #514B43;
  --ink-faded: #91897D;
  --ink-ghost: rgba(25, 23, 20, 0.12);
  --seal: #B83A2E;
  --seal-dark: #8F2C24;
  --ochre: #987340;
  --rule: rgba(25, 23, 20, 0.25);
  --rule-soft: rgba(25, 23, 20, 0.12);
  --shadow-paper: 0 12px 32px rgba(25, 23, 20, 0.06);
  --font-brush: "STKaiti", "KaiTi", "Noto Serif SC", "Songti SC", serif;
  --font-serif: "Noto Serif SC", "Source Han Serif SC", "Songti SC", "STSong", serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  --font-mono: "IBM Plex Mono", "SFMono-Regular", Consolas, monospace;
  --ease-ink: cubic-bezier(0.2, 0.8, 0.2, 1);
}
```

## 3. Style-Owned Layout Contract

### Web Adaptation: Direct Immersive Flow

```html
<body class="xuan-scroll">
  <div class="paper-environment" aria-hidden="true"></div>
  <main class="scroll-flow">
    <aside class="index-rail">01</aside>
    <article class="reading-column">...</article>
    <aside class="colophon-rail">来源 / 日期</aside>
  </main>
</body>
```

The desktop grid is `minmax(72px, 1fr) minmax(0, 7fr) minmax(160px, 2fr)` inside a 1180px measure. The text column is capped at 720px. Sections are separated by a single authored brush line or a paper fold, never by a floating white card. At `max-width: 820px`, rails become inline metadata and the reading column fills the viewport with 20px side padding.

The paper environment uses CSS gradients and a tiny inline SVG texture. It must remain legible when the texture is disabled. Ink marks are positioned in content margins and have `pointer-events: none`.

### PPT Adaptation: Single Page / 16:9

Each `.slide` is `1280px × 720px`, with an 80px safe area. The slide background is paper; the title, one brush gesture, and one semantic emphasis share the same page. Data and comparison pages use fine ink rules and margin annotations instead of card grids. No slide uses a scrolling column or a full-bleed decorative calligraphy image.

## 4. Typography Scale & Rules

| Element | Class / Tag | Size | Weight | Line Height | Letter Spacing | Font Stack | Role |
|---|---|---:|---:|---:|---:|---|---|
| Eyebrow | `.eyebrow` | 11px | 700 | 1.4 | 0.12em | `var(--font-mono)` | Section index |
| Hero title | `h1.hero` | clamp(38px, 6vw, 78px) | 400 | 1.12 | 0 | `var(--font-brush)` | One short brush title |
| Lead | `.lead` | 18px | 400 | 1.8 | 0 | `var(--font-serif)` | Editorial opening |
| Section title | `h2.section-title` | 28px | 600 | 1.35 | 0 | `var(--font-serif)` | Chapter heading |
| Card/subtitle | `h3` | 18px | 600 | 1.45 | 0 | `var(--font-serif)` | Local heading |
| Body | `.rich-text`, `p.body` | 16px | 400 | 1.95 | 0 | `var(--font-serif)` | Long-form reading |
| Data value | `.stat-val` | 38px | 600 | 1.1 | 0 | `var(--font-serif)` | Quantitative emphasis |
| Meta | `.meta`, `footer` | 11px | 600 | 1.5 | 0.08em | `var(--font-mono)` | Source and build info |

Use brush type only for short display phrases. Never set a paragraph, table, button, or multi-line data block in the brush face. Chinese headings may break at semantic pauses (`、`, `·`, `与`, `之`) but never split a number and its unit.

## 5. Signature Component Patterns

### A. Ink Measure (stats)

```html
<div class="ink-measure">
  <div class="measure-item"><strong>72%</strong><span>完成度</span></div>
  <div class="measure-line" aria-hidden="true"></div>
  <div class="measure-item"><strong>4.8</strong><span>评分</span></div>
</div>
```

```css
.ink-measure { display: grid; grid-template-columns: auto 1fr auto; gap: 18px; align-items: end; border-bottom: 1px solid var(--rule); padding: 18px 0 10px; }
.measure-line { height: 6px; background: linear-gradient(90deg, var(--ink), var(--ink-dense) 55%, transparent); clip-path: polygon(0 28%, 58% 0, 100% 42%, 82% 100%, 0 76%); }
.measure-item strong { font: 600 38px/1 var(--font-serif); color: var(--ink); }
.measure-item span { display: block; margin-top: 5px; color: var(--ink-faded); font: 11px/1.4 var(--font-mono); }
```

### B. Seal Admonition (conclusion/warning)

```html
<aside class="seal-note warning">
  <span class="seal-stamp" aria-hidden="true">戒</span>
  <div><h3>边界条件</h3><p>保留原始统计口径，不将推演结果写成事实。</p></div>
</aside>
```

The seal is a square 28–34px mark with slight irregularity; the note body stays on paper and uses a single side rule.

### C. Scroll Timeline (history/evolution)

```html
<ol class="scroll-timeline">
  <li><time>2022</time><div><h3>观察</h3><p>建立原始样本。</p></div></li>
  <li><time>2024</time><div><h3>转折</h3><p>进入规模化验证。</p></div></li>
</ol>
```

```css
.scroll-timeline { list-style: none; padding: 0; margin: 28px 0; border-left: 2px solid var(--ink-dense); }
.scroll-timeline li { display: grid; grid-template-columns: 96px 1fr; gap: 20px; position: relative; padding: 0 0 28px 24px; }
.scroll-timeline li::before { content: ""; position: absolute; left: -6px; top: 5px; width: 10px; height: 10px; border: 2px solid var(--paper); background: var(--seal); border-radius: 50%; }
.scroll-timeline time { font: 700 12px/1.4 var(--font-mono); color: var(--seal); }
```

### D. Colophon Reference (sources/metadata)

```html
<div class="colophon">
  <span class="colophon-mark">题</span>
  <p><strong>来源</strong> National Palace Museum Digital Archive<br><small>访问日期 · 2026-08-27</small></p>
</div>
```

Colophons sit after the argument or in the annotation rail. They never overlay body text.

### E. Paper Comparison (comparison/pros and cons)

```html
<div class="paper-diptych">
  <section><h3>生宣</h3><p>吸水快，边缘柔，适合表现湿润变化。</p></section>
  <section><h3>熟宣</h3><p>边缘稳，信息密度高时更易保持清晰。</p></section>
</div>
```

The diptych is separated by one vertical brush rule, not two cards. A highlighted column may use a thin cinnabar underline, never a colored fill.

## 6. Do's and Don'ts

### Do's

1. Do keep one continuous paper field across a Web page or slide.
2. Do use authored SVG brush marks with a clear direction and end point.
3. Do reserve brush type for short titles and display phrases.
4. Do keep body text at a generous measure and line height.
5. Do use cinnabar for one meaningful seal, status, or source mark.
6. Do expose wetness, density, pressure, and speed as qualitative style tokens.
7. Do verify the style with unrelated content, mobile screenshots, and offline rendering.

### Don'ts

1. Don't add WebGL smoke, cursor trails, or continuously moving ink clouds.
2. Don't use a photographic calligraphy background as the page's primary structure.
3. Don't turn every semantic component into a rounded white card.
4. Don't use random splatters or decorative marks behind readable text.
5. Don't treat five ink tones as five unrelated brand colors.
6. Don't set long paragraphs, tables, or controls in a brush font.
7. Don't use seals as generic bullets, badges, or button replacements.

## Mermaid Theme Configuration

```js
mermaid.initialize({
  startOnLoad: true,
  theme: 'base',
  themeVariables: {
    darkMode: false,
    background: '#F1ECE1',
    primaryColor: '#E6DED0',
    primaryTextColor: '#191714',
    primaryBorderColor: '#514B43',
    lineColor: '#514B43',
    secondaryColor: '#FAF7EF',
    tertiaryColor: '#D7CCBA',
    fontFamily: '"Noto Serif SC", "Songti SC", serif'
    fontSize: '13px'
  }
});
```
