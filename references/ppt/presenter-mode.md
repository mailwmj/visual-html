# PPT Presenter Mode & Speaker Notes Contract (演讲者模式与提词契约)

本文件定义 Generate PPT 路由中关于**演讲者视角、提词卡（Speaker Notes）、时长节奏控制及幻灯片元数据标识**的标准契约。

---

## 1. 核心定位：大屏与讲台的双重协同

一份优秀的演示文稿包含两个视角的协同：
- **大屏（观众可见）**：极简、大字号、图表化、强视觉冲击、单一论点；
- **讲台（演讲者提词）**：结构化提示、口头论据补充、转场衔接、时间提醒。

严禁把演讲稿全文搬到幻灯片屏幕上；所有的展开论述、案例细节和口语过渡均属于**演讲者提词（Speaker Notes）**。

---

## 2. 页面 ID (`data-slide-id`) 命名契约

每一张 `.slide` 容器必须具备全局唯一的 `data-slide-id` 属性，用于状态定位、演讲者提词索引与外部联动：

- **格式要求**：使用小写字母、数字与连字符（kebab-case），如 `data-slide-id="arch-overview"`。
- **命名语义**：
  - 封面页：`cover`
  - 目录/概览：`agenda` 或 `roadmap`
  - 核心论点/正文页：反映页面核心主张，如 `perf-benchmark`、`core-architecture`、`cost-tradeoff`
  - 总结/行动页：`takeaway` 或 `action-plan`
  - 附录备查页：以 `appendix-` 为前缀，如 `appendix-metrics`、`appendix-raw-code`

---

## 3. 演讲者提词（Speaker Notes）内容契约

在大纲阶段和 HTML 注释/元数据中维护提词内容时，必须遵守以下规则：

1. **要点式提示（Bullet Points）**：
   - 默认每页提供 **3 ~ 5 条**短句提词；
   - **严禁写大段逐字念白**，只记录核心关键词、论据支撑、设问与核心金句。
2. **转场提示（Transitions）**：
   - 最后一项提词建议包含下页转场引导语（如：“引出下一个核心瓶颈：内存爆炸”）。
3. **时长缓冲控制（90% 规则）**：
   - 各页规划时长之和不得超过总可用时长的 90%；
   - 留出 10% 冗余用于现场停顿、观众互动、设备延迟与即兴答疑。
4. **现场未提供信息不瞎猜**：
   - 用户未提供的信息（如具体嘉宾名单、特定场地）不凭空编造，大纲中保留占位或隐藏。

---

## 4. HTML 代码中的数据承载契约

在编写 `scaffold-ppt.html` 时，可通过数据属性与语义注释将提词信息注入 DOM，供未来扩展的演讲者视图解析：

```html
<section 
  class="slide" 
  data-slide-id="arch-overview" 
  data-duration="120"
  data-presenter-notes="1. 强调三层架构的解耦价值; 2. 指出网关层的限流保护机制; 3. 引用上周压测 50k QPS 数据; 4. [转场] 接下来看存储层的热点处理"
>
  <!-- 观众可见的 16:9 高保真大屏内容 -->
  <div class="eyebrow"><span class="dot"></span> ARCHITECTURE OVERVIEW <span class="line"></span></div>
  <h2 class="s">高并发网关与异步解耦架构</h2>
  ...
</section>
```

- **打印与大屏展示隔离**：`data-presenter-notes` 仅作为元数据存在，在大屏播放和打印导出时完全静默，绝不侵入视觉安全区。
