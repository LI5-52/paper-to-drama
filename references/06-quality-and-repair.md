# 全链路质量控制与定点修复

## 区分 3 种判断
- `structural`：字段、引用、状态、模型输入参数等可机器检查（必要时阻断）。
- `semantic`：语义理解、因果、事实暗示、Hook 兑现等需要依据的审查。
- `taste`：好笑、审美、反转强度、镜头审美等表达偏好；不能靠模型自评冒充观众效果。

## 关键节点和修复定位
| 失败示例 | 从何处查起 | 修改粒度 |
|---|---|---|
| 将研究假设写成实验已证明 | paper card / fact ledger | 关联的素材卡与受影响剧情 |
| 三种风格只是换了时代背景 | style proposals | 只重写不合格的提案 |
| 开头承诺的谜题完全没回应 | beats / screenplay | 相关铺垫与结尾节拍 |
| 人物突然知道此前未发生的信息 | knowledge-state line | 断裂的节拍或过渡场景 |
| 道具凭空从右手跳到另一角色 | asset/shot continuity | 状态定义与受影响镜头 |
| 同一镜头要完成四个场景切换 | storyboard | 分镜拆分与时长分配 |
| 视频里人物外貌漂移 | character references / generated shot | 对应角色条件与单镜重生成 |
| 语音与人物口型不同步 | adapter / audio timing | 对应音画片段 |

## 独立标注，而不是一句“评分 8/10”
每个问题记录：`stage, item_id, issue_type, severity=blocker|major|minor|preference, concrete_evidence, responsible_stage, proposed_patch, status`。人工或模型可给备选修复，但程序根据 ID 决定需重生的依赖节点。最大重试次数需要在运行环境设定。

## 剧本审查简表
- DramaBench 六轴：`format`, `narrative_efficiency`, `character_consistency`, `emotional_depth`, `logic_consistency`, `conflict_handling`。
- 本项目额外三项：`hook_payoff_alignment`, `paper_anchor_accuracy`, `dramatic_interest`（最后一项必须经观众验证）。
- 可用事件标注计算 `driver / static / redundant`；不把 static 比例当硬门禁，氛围、反应、幽默停顿有其价值。

## 方法证据
DramaBench：https://arxiv.org/html/2512.19012 （剧本续写 benchmark，与短剧创作并非同任务）
DramaChain Bench：https://arxiv.org/html/2609.00646 （五轴：输入忠实度 F、内部一致性 C、生成可行性 P、视听画质 Q、电影表现力 E；上游缺陷传播）
DramaAgent：https://arxiv.org/html/2610.00097 （依据身份/语义/时间/音画最弱项路由局部修复；文中参数是其特定实验设置，禁止通用硬编码）
One Sentence, One Drama：https://arxiv.org/html/2605.22144 （评审汇总+有争议问题仲裁+最小 patch 修复）
