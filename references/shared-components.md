# Visual HTML — 共享组件结构规范 (Shared Components)

本规范定义所有风格共享的 HTML 结构骨架。无论切换何种风格主题，DOM 结构保持一致，通过 CSS 变量和风格专属类名实现视觉定制。

---

## 1. Section Eyebrow (区块索引标头)

```html
<div class="eyebrow">
  <span class="diamond"></span>
  <span>01 / SECTION_TITLE</span>
  <span class="line"></span>
</div>
```

- **结构语义**：由菱形标识、等宽大写编号/英文、细线横杠组成。
- **作用**：标明当前章节编号与阅读锚点，建立技术档案感。

---

## 2. Typography Scale (排版层级)

```html
<!-- 主页面 Hero 大标题 -->
<h1 class="hero">短小有力的主标题，<br>支持中文主动换行。</h1>
<p class="lead">导读段落：解释主标题，字号适中，控制行宽 (max-width: 50~54ch)。</p>

<!-- 区块标题 -->
<h2 class="section-title">区块二级标题。</h2>

<!-- 正文 -->
<p class="body">正文解释性文字，行高 1.7~1.75，具有良好的可读性与留白。</p>
```

---

## 3. Technical Spec Row (规格参数栏)

```html
<div class="spec-row">
  <div class="spec">
    <div class="val">60×95<em>mm</em></div>
    <div class="unit">SIZE / 尺寸</div>
  </div>
  <div class="spec">
    <div class="val">500<em>mah</em></div>
    <div class="unit">BATTERY / 电池</div>
  </div>
  <div class="spec">
    <div class="val">USB-C</div>
    <div class="unit">INTERFACE / 接口</div>
  </div>
  <div class="spec">
    <div class="val">12<em>s</em></div>
    <div class="unit">INSTALL / 安装</div>
  </div>
</div>
```

- **结构语义**：顶部有 1px 强调信号线，4 列等分，数值为加粗大字号（带 Mono 单位），下方为大写 Mono 标签。

---

## 4. Number Cards (三栏编号卡片)

```html
<div class="cards-3">
  <div class="num-card">
    <div class="num">01</div>
    <div class="tag">READY</div>
    <h3>模块标题</h3>
    <p>详细描述说明，字号适中，行高宽松。</p>
  </div>
  <!-- 选中/推荐态使用 .selected -->
  <div class="num-card selected">
    <div class="num">02</div>
    <div class="tag">SELECTED</div>
    <h3>推荐核心功能</h3>
    <p>第二状态通道高亮显示，建立视觉层级焦点。</p>
  </div>
  <div class="num-card">
    <div class="num">03</div>
    <div class="tag">LOCAL</div>
    <h3>辅助功能</h3>
    <p>次要说明内容。</p>
  </div>
</div>
```

---

## 5. Feature Card (错位/质感特性卡片)

```html
<div class="feat-grid">
  <div class="feat-card">
    <div class="tag">// PLAY MODE</div>
    <h3>特性一标题</h3>
    <p>特性的详细能力和用户体验描述。</p>
    <div class="frame">PRODUCT RENDER · 4:3</div>
  </div>
  <div class="feat-card">
    <div class="tag">// FOCUS MODE</div>
    <h3>特性二标题</h3>
    <p>特性的详细能力和用户体验描述。</p>
    <div class="frame">PRODUCT RENDER · 4:3</div>
  </div>
</div>
```

---

## 6. Process Steps (流程步骤)

```html
<div class="steps">
  <div class="step">
    <div class="idx">01</div>
    <div>
      <h3>步骤一标题</h3>
      <p>步骤说明内容，突出流程递进。</p>
    </div>
  </div>
  <div class="step">
    <div class="idx">02</div>
    <div>
      <h3>步骤二标题</h3>
      <p>步骤说明内容。</p>
    </div>
  </div>
  <div class="step">
    <div class="idx">03</div>
    <div>
      <h3>步骤三标题</h3>
      <p>步骤说明内容。</p>
    </div>
  </div>
</div>
```

---

## 7. Comparison Table (对比模块 - 非 Excel 样式)

```html
<div class="cmp">
  <div class="row head">
    <div class="cell">对比维度</div>
    <div class="cell">方案 A</div>
    <div class="cell">方案 B</div>
    <div class="cell selected-col">方案 C (推荐)</div>
  </div>
  <div class="row">
    <div class="cell">调度能力</div>
    <div class="cell"><span class="dot"></span></div>
    <div class="cell"><span class="dot"></span></div>
    <div class="cell selected-col"><span class="dot"></span></div>
  </div>
  <div class="row">
    <div class="cell">全流程闭环</div>
    <div class="cell"><span class="dash">—</span></div>
    <div class="cell"><span class="dot"></span></div>
    <div class="cell selected-col"><span class="dot"></span></div>
  </div>
</div>
```

---

## 8. Metadata Footer (技术页脚)

```html
<footer>
  <div class="wrap">
    <div class="meta-foot">
      <span>PRODUCT SYSTEM // 2026</span>
      <span>BUILD 02 / PROTOTYPE</span>
      <span>FRAMEFLOW // TECHNICAL NOTE</span>
    </div>
  </div>
</footer>
```
