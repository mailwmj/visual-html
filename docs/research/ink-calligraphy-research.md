# 中国毛笔书法与宣纸美学：数字视觉转译研究

> 研究目的：为 `ink-calligraphy` 的重构提供可观察、可验证的视觉规则。本文把来源事实、设计推演和仍需实测的问题分开。访问日期统一为 2026-08-27。

## 结论先行

建议把新风格的核心从“泼墨效果集合”改为 **一张可阅读的纸 + 一次有方向的用笔 + 被保留下来的空处**。数字系统应模拟笔墨关系（速度、压力、含水量、笔锋方向、字距/行气），而不是同时叠加 WebGL 烟雾、飞溅、巨大狂草和半透明卡片。印章、题跋和纸边应成为少量的秩序标记；正文仍应是最稳定、最清晰的阅读层。

## 1. 可观察规律：笔法、墨法、章法、留白

### 1.1 笔法（事实）

- 毛笔是可变形的软笔：用笔尖或笔侧会产生二维或三维的不同笔触；速度与落笔压力共同改变笔画效果。快速行笔可形成“腾跃”的动势，缓慢用笔传达端正、克制的姿态。[Metropolitan Museum of Art, “Chinese Calligraphy”](https://www.metmuseum.org/essays/chinese-calligraphy)
- 含墨量与墨液浓度不是固定色值：蘸墨多/少、让笔锋接近枯竭后再蘸墨，会造成由湿润到干涩的连续变化；Met 以“岩雨、露珠”等自然意象描述这种差异。[Met, “Chinese Calligraphy”](https://www.metmuseum.org/essays/chinese-calligraphy)
- 书写遵循笔顺和经过训练的动作编排，因此“秩序”与“个人活力”同时存在；规则不是随机涂抹的替代品。[Met, “Chinese Calligraphy”](https://www.metmuseum.org/essays/chinese-calligraphy)

### 1.2 墨法（事实 → 推演）

- 墨锭在砚上加水研磨，书写者可通过水量和研墨量控制墨液厚薄；笔中载墨量也会在行进过程中改变。[Met, “Chinese Calligraphy”](https://www.metmuseum.org/essays/chinese-calligraphy)
- 《书谱》原文中“带燥方润，将浓遂枯”“留不常迟，遣不恒疾”把干湿、浓淡、迟速写成需要互相制衡的连续关系。台北故宫的《唐孙过庭书谱卷》典藏记录收录上述句子及“违而不犯，和而不同”等段落。[National Palace Museum Digital Archive, 《唐孫過庭書譜卷》](https://digitalarchive.npm.gov.tw/Collection/Detail?id)（该站的搜索结果会截断查询参数；可用题名检索）
- **数字推演**：把墨色做成“连续变量”比预设五个平行色块更接近原理：`wetness`（湿润度）、`density`（浓度）、`pressure`（压力）、`speed`（速度）四个参数驱动笔画宽度、边缘扩散、透明度和局部干裂。颜色阶梯只能作为无障碍/信息层级的离散映射，不应宣称是传统“墨分五色”的物理复刻。

### 1.3 章法与行气（事实）

- 传统文字常以自右向左的竖列组织；每个字内部也要求平衡、比例和骨架，笔顺保证连贯的节奏。[Met, “Chinese Calligraphy”](https://www.metmuseum.org/essays/chinese-calligraphy)
- 孙过庭《书谱》的“**一点成一字之规，一字乃终篇之准**”将局部落笔与整篇节奏关联；故宫典藏记录同样收录此句。[National Palace Museum Digital Archive, 《唐孫過庭書譜卷》](https://digitalarchive.npm.gov.tw/Collection/Detail?id)
- 普林斯顿大学艺术博物馆所藏《书谱》摹本为 14 开册页、墨于黄色纸，说明书法作品本身可以是册页/页间节奏，而不是只能铺满一张连续背景。[Princeton University Art Museum, “Transcription of Sun Guoting's ‘Manual On Calligraphy’”](https://artmuseum.princeton.edu/art/collections/objects/36378)
- **数字推演**：Web 采用“短段落/列宽受控/段间有呼吸”的阅读章法；PPT 采用单幅纸面、少量纵向锚点和明确的起首/收束。不要把所有模块都做成同等权重的卡片网格。

### 1.4 留白（事实 → 推演）

- Met 对中国书画的说明强调以线条和笔墨提炼“内在精神”，而不是用不透明色块覆盖错误；作品的力量来自经济的线与墨。[Met, “Chinese Painting”](https://www.metmuseum.org/essays/chinese-painting)
- 手卷观看是逐段展开、在不同段落停留或快速略过的时间过程；形式本身制造了间隔、期待和节奏。[Met, “Chinese Handscrolls”](https://www.metmuseum.org/essays/chinese-handscrolls)
- **数字推演**：留白不是空的装饰层，而是承载阅读节奏的“可用空间”。正文区保持不被纹理/墨迹穿过；背景纹理在内容边缘衰减；大字或引文只占一个视觉焦点，其余区域留给纸面呼吸。

## 2. 生宣、熟宣、半生熟：材料差异及数字含义

### 2.1 可确认事实

- UNESCO 将宣纸定义为以青檀（Tara Wing-Celtis/blue sandalwood）树皮与稻草手工制成；其特征是强韧、表面平滑、能吸水并润墨，且可反复折叠不易破损。传统工艺包括浸泡、清洗、发酵、漂白、制浆、晒纸、裁切等百余道步骤。[UNESCO ICH, “Traditional handicrafts of making Xuan paper”](https://ich.unesco.org/en/RL/traditional-handicrafts-of-making-xuan-paper-00201)
- 北京大学人文社会科学研究院实地考察记录：泾县宣纸使用青檀皮和沙田稻草及当地水，原料到成纸逾百道手工工序；按加工与功能分为生宣和熟宣，生宣是未经加工的原纸，熟宣是经染色、洒金/银、印花、涂蜡、砑光、施矾等加工的宣纸。该记录还指出棉料适宜书法，特种净皮适宜泼墨/大写意。[PKU IHSS, “书法的物质性与历史研究”工作坊（安徽场二）](http://www.ihss.pku.edu.cn/gzf1/articles/1373713227099279360.html)
- 中国宣纸股份有限公司（红星）将青檀皮描述为长纤维、稻草为短纤维，二者交织形成“存水导墨”的结构；其产品说明把棉料（青檀约 30–40%）列为适宜书法、净皮（约 60–70%）列为书画兼用、特净皮（>80%）列为泼墨山水/大写意。[中国宣纸股份有限公司《非遗介绍丨宣纸传统制作技艺》](http://www.hongxingxuanpaper.com.cn/index.php/hongxingpinpai/xuanzhizhishi/1391.html)
- 红星另一份材料说明把生宣定义为出槽晾干后未经处理，熟宣为加矾水等处理，半生熟为较少的矾水处理；质感由柔软到挺脆，吸墨/湿染由强到弱，半生熟居中。该页面是生产者的定性说明，不是实验室测量。[中国宣纸股份有限公司《通俗易懂：了解生宣纸、熟宣纸和半生半熟宣纸》](http://www.hongxingxuanpaper.com.cn/hongxingpinpai/xuanzhizhishi/1401.html)
- **半生熟的证据边界**：红星给出“介于”关系，但未给统一的国际吸水率、配方或跨厂家标准；不同厚度、施胶/施矾程度、墨液、压力、湿度和保存状态都会改变结果。因此不应把“半生熟”当成可由单一 CSS 值代表的确定材料（推演，需实物测试）。

### 2.2 对数字视觉的可靠转译

| 材料隐喻 | 视觉/交互表现 | 不应做成 |
| --- | --- | --- |
| 生宣：吸水、润墨、边缘自然扩散 | 大字或主引文表现“深色墨核 + 不均匀柔晕 + 少量方向性纤维尾”；扩散只在落笔时刻出现 | 全屏永久烟雾、无方向的随机墨斑；把生宣绝对化为模糊 |
| 熟宣：经施胶/施矾等加工，吸墨相对弱（定性事实） | 细字、注释、图表线条用更稳定的硬边和浅表沉积；纸面仍保持哑光纤维感 | 把熟宣做成塑料白卡或玻璃拟态 |
| 半生熟：吸墨/湿染介于两者之间（生产者定性事实） | 作为默认正文纸性：中等边缘变化，保证小字号可读；用主题变量表达连续度 | 宣称所有半生熟都“既不洇又不散” |

## 3. 印章、落款、纸张边界的克制转译

### 3.1 史料与馆藏观察

- 中国画/书法作品常在后世流传中不断增加题跋与收藏印；Met 说明题跋多位于画面边缘、手卷或册页的衬纸，印章大小不一且表达作者/收藏者的署名或所有权。[Met, “Chinese Painting”](https://www.metmuseum.org/essays/chinese-painting)
- 手卷中的题跋通常位于画面之后的附加纸/绢上；印章以不同大小的红色印记出现，作品因此同时成为图像和传承记录。[Met, “Chinese Handscrolls”](https://www.metmuseum.org/essays/chinese-handscrolls)
- 普林斯顿藏《书谱》摹本记录了前后多位题跋、年代和装帧信息，显示落款/题跋是对象历史的一部分，而不是随机贴纸。[Princeton University Art Museum](https://artmuseum.princeton.edu/art/collections/objects/36378)

### 3.2 转译规则（推演）

1. **印章**：每个页面最多一个主印（品牌/章节状态），必要时一个小副印；使用不完全规则的方形、低饱和朱砂、轻微压印纹理。不要把所有按钮、标签都做成红印章。
2. **落款**：将作者/日期/来源放在正文收束处或纸边，字号小于正文，不抢标题；信息型页面只保留可确认的元数据。
3. **纸边**：用可见但克制的边界（窄边、轻微裁切不齐、局部露出底色）提示“纸张承载物”。边界不应成为圆角卡片外框；正文和交互控件仍需遵守可访问的对比度、焦点和点击尺寸。
4. **题跋/来源**：把参考文献、注释或附录做成“后接纸页/边栏”节奏，而不是在主内容上叠印，避免历史上“后世追加”的概念被误读为装饰噪声。

## 4. 对当前 `ink-calligraphy` 的诊断

以下是基于现有 `references/styles/ink-calligraphy/design.md` 与 `scaffold-web.html` 的设计审计（推演，不是书法史事实）：

- **效果堆叠过量**：动态 WebGL 烟岚、鼠标扩散、巨幅狂草飞白、墨滴微星、纸纤维和半透明载板同时存在，视觉焦点会从“用笔/纸面”转向“特效层”。
- **现代容器压过纸面**：`main-sheet` 使用 10px 圆角、`backdrop-filter` 和悬浮阴影，形成玻璃卡片语法；它削弱了册页/手卷的连续纸面，也与“边界和留白”原则冲突。
- **把传统术语离散化**：把“墨分五色”直接做成固定色阶和 UI 信号通道，容易把动态的干湿浓淡关系误读成五种平行品牌色；应改为连续墨性变量，必要时再做语义映射。
- **书法字体承担过多信息**：Hero 使用在线字体与“狂草/榜书”语气，若正文标题、统计数字、按钮也重复使用，会降低可读性并让页面像书法海报而非可阅读文档。
- **朱砂与飞溅的语义泛化**：现有规范要求多个位置使用朱砂印章、墨滴和飞溅；建议把朱砂限于署名/状态，把飞溅限于一次“落笔事件”，其余用纸面留白承担层级。

## 5. 建议的新风格方向（供方案评审）

暂名：**`xuan-scroll` / 宣卷留白**。

- **一句话**：一张有纤维和边缘的宣纸，承载一条有速度、有收笔的墨线；信息像册页一样被展开，而不是被卡片包围。
- **视觉基因**：温白/微灰宣纸底；焦墨正文；一条主笔触或局部字迹；朱砂仅作署名/状态；边缘露纸；低频帘纹而非高对比噪点。
- **布局**：Web 为纵向长卷，章节像“接纸”自然续接；PPT 为单张册页，标题、正文、图表共用一张纸面；默认不启用全屏 WebGL 和跟随鼠标的特效。
- **参数化墨性**：用 `wetness / density / pressure / speed` 生成少量背景笔触和引用标记；正文文字不做动态扩散。
- **验收信号**：缩小到手机或 PPT 缩略图时仍先读到标题和论点；关闭动效后仍成立；无外网字体时字阶和布局不崩；印章数量、纹理对比度和墨迹覆盖面积均有上限。

## 6. 未知与下一步验证

- 需要实物或扫描样本验证不同品牌生宣、熟宣、半生熟的扩散半径、干燥后边缘和显示器压缩后的可读性；现有一手来源没有统一参数。
- 需要确认目标用户是否要“书法作品展示”还是“长文/PPT 阅读”。前者可承受更强的单幅笔触，后者应优先纸面连续性和信息密度。
- 新风格定稿前应做两个最小原型：同一篇内容分别用“生宣主视觉”和“半生熟正文纸性”，在桌面与手机截图上比较标题识别、正文对比度、印章干扰和滚动节奏。

## 参考来源（均为一手/机构来源）

1. Metropolitan Museum of Art, Dawn Delbanco, “Chinese Calligraphy” (2008), https://www.metmuseum.org/essays/chinese-calligraphy
2. Metropolitan Museum of Art, “Chinese Painting”, https://www.metmuseum.org/essays/chinese-painting
3. Metropolitan Museum of Art, “Chinese Handscrolls”, https://www.metmuseum.org/essays/chinese-handscrolls
4. UNESCO Intangible Cultural Heritage, “Traditional handicrafts of making Xuan paper” (inscribed 2009), https://ich.unesco.org/en/RL/traditional-handicrafts-of-making-xuan-paper-00201
5. 北京大学人文社会科学研究院, “书法的物质性与历史研究”工作坊（安徽场二）(2017-09-05), http://www.ihss.pku.edu.cn/gzf1/articles/1373713227099279360.html
6. Princeton University Art Museum, “Transcription of Sun Guoting's ‘Manual On Calligraphy’”, object no. 1998-124 a-n, https://artmuseum.princeton.edu/art/collections/objects/36378
7. 中国宣纸股份有限公司（红星）, 《非遗介绍丨宣纸传统制作技艺》(2024-02-27), http://www.hongxingxuanpaper.com.cn/index.php/hongxingpinpai/xuanzhizhishi/1391.html
8. 中国宣纸股份有限公司（红星）, 《通俗易懂：了解生宣纸、熟宣纸和半生半熟宣纸》(2024-03-02), http://www.hongxingxuanpaper.com.cn/hongxingpinpai/xuanzhizhishi/1401.html
9. 國立故宮博物院數位典藏, 《唐孫過庭書譜卷》, https://digitalarchive.npm.gov.tw/Collection/Detail?id （按题名检索；查询参数由搜索接口截断）
