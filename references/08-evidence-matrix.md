# 2026-10-25 文献和平台精读矩阵｜真实证据与迁移边界

此文档记录原始资料公开支持的**方法**，与本项目提出的**推导性规则**分开；文献中报告的提升不等于在 Paper-to-Drama 项目中已证实有效。

| 来源/年份/类型 | 研究任务与原文可定位方法 | 可复用到本项目 | **不应直接迁移/局限** |
|---|---|---|---|
| PaperTok, CHI 2026（N=8 形成性访谈；N=18 研究者使用；N=100 观众） | §4.2.1：四个具象且切身相关的发现 → 四种创意策略（contradiction / surprise-irony / personal-stakes / curiosity）→ 15 英文词以内问句 Hook，按 engagement/relevance/emotional appeal 审查；§4.2.2：围绕 Hook 写八场、约 45 秒的研究传播叙事；§6：创作者想要更多精细控制 | 发散→筛选、Hook 兑现、来源清晰、提高内容具体性 | 不是完整角色剧情短剧；八场、45 秒、15 英文词是原系统设置，不是本项目通用规则；没有线下实际传播有效性证明 |
| Audience in the Loop, CHI 2026（28 位短剧创作者访谈） | §4.1–4.3：创作者综合观看量、完成率、评论/弹幕、分享等信号修改题材、角色、节奏和情节 | 研究观众期待、创意迭代数据的类型；未来收集弃看点/情绪反应 | 属质性研究，不能将“3 秒一反转”等商业建议视为经控制试验验证；初版上传→生成没有实时受众数据 |
| One Sentence, One Drama, 2026 arXiv | 附录 C：约 300 剧本→剧本 Pattern Bank/Logic Bank；以 Fact/Logic/Pattern 三类素材支持新故事；场景的外部压力线、主角反应线、解决线、情绪线、观众/角色知识线；多个评审维度，问题聚合/仲裁/局部补丁；图像和 BGM/转场阶段也审查 | 事实/逻辑/套路分层；知识状态；Hook 持续与定点修复 | 论文没有证明这些规则对“学术论文启发的短剧”最优；多前沿模型与 3D 搭建成本很高，不适合照搬为 V0.1 必须项 |
| DramaBench, 2025 arXiv | §4.2：6 维（格式、叙事效率、角色一致、情感深度、逻辑一致、冲突处理）。把故事节拍标成 driver/static/redundant；按具体标签统计，而非只问模型一个总分。188 剧本人类对照、5维中3维达到中等至较高一致性；尤其叙事效率与角色一致性两项人—模型相关不显著 | 剧本审查清单、事件级定位和解释性评分 | 研究目标是续写而非从论文自动原创短剧；文中的经验阈值不能机械用于短时实验 |
| DramaChain Bench, 2026 arXiv | §3.1：F 输入忠实、C 内部一致、P 生成可行、Q 视觉技术质量、E 影视表现 5 轴在 6 个生产阶段复用，63 细项；三位专业标注者做时空位置定位；上游缺陷传播 | 错误从源头跟踪、各阶段统一 ID、阶段审查和局部修复 | 是长链视频 benchmark，不能用它说明我们「趣味点选择」的真实性或用户阅读论文意愿 |
| DramaAgent, 2026 arXiv | §3：故事规划→常驻角色条件→场景逐段生成→反思修复；附录 B：依据身份、语义、时间和音画最弱项选择修复路线 | 角色连续性约束、单镜定向重试 | 原文特定 K=3、阈值 τ=.8、R=2 是其系统经验值，不是本 Skill 硬标准 |
| Preacher, ICCV 2025 | Top-down 论文拆解与 reformulate key-scene；bottom-up 合成视频摘要、渐进规划 | 全文预处理与视觉中间产物 | 完整学术信息摘要导向，不应驱动我们依据论文顺序叙事 |
| Anthropic Skill Creator, GitHub | SKILL.md YAML frontmatter、简洁路由、references 懒加载、scripts、evals、定性及客观测试 | 主 Skill 入口简洁、规则分拆、测试工程结构 | 它不是短剧理论或叙事证据，只是 Skill 组织经验 |
| ZenStory Drama Skills, GitHub MIT | 主路由与 develop/write/assets/storyboard/video-prompts/review 独立阶段；stage-contract 将规则划分 structural_invariant / reviewed_invariant / craft_default / taste_option | 模块边界、四级规则、固定 ID 和审查对象 | 长篇小说/多集短剧前提不同；不能照搬 11 个子 Skill 的全部复杂度 |
| 小云雀官方手册 | 剧本上传→需求确认→角色与场景全局资产→分镜编辑/引用角色和场景→视频/导出 | asset bible 与镜头引用；单镜修订 | 商业平台网页流程不等于其后端全部真实结构或可用 API |
| Katalist Story Canvas 官方帮助 | 导入剧本→Script Sidebar 自动划分 scenes 和 shots→放入 Story Canvas | 场景与镜头分层；导入剧本而非直接电影生成 | 需要人工编辑，平台操作不意味着其自动分镜完全准确 |
| Runway Gen-4 Prompt Guide | 入图 + 文字视频；提示词聚焦主体、环境、镜头运动，减少过多同时动作 | 统一 Shot 数据之后再映射模型特定生成描述 | 是 Gen-4 当时的官方建议，其他平台/版本不直接适用 |

## 官方 / 原文链接
- PaperTok：https://arxiv.org/html/2601.18218
- Audience in the Loop：https://arxiv.org/html/2602.14045v1
- One Sentence, One Drama：https://arxiv.org/html/2605.22144
- DramaBench：https://arxiv.org/html/2512.19012
- DramaChain Bench：https://arxiv.org/html/2609.00646
- DramaAgent：https://arxiv.org/html/2610.00097
- Preacher：https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Preacher_Paper-to-Video_Agentic_System_ICCV_2025_paper.html
- ZenStory：https://github.com/zenstory-ai/drama-skills
- Anthropic Skill Creator：https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- 小云雀：https://xyq.jianying.com/tutorials/web-manual
- Katalist：https://help.katalist.ai/en/articles/16298583-how-to-build-your-storyboard-and-videos-in-story-canvas
- Runway：https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide

## 未来调研需避免的过度结论
- 有论文讲「效果更好」并不等于已经证明本 Skill 能提高趣味性。
- 标准剧本格式/特定反转套路不应阻碍合适的不同叙事风格。
- 观众短剧偏好随群体、文化和平台改变；后续试验需要固定目标受众。
- 学术事实核对和科学误导风险不同；后者需要观众理解测量而不是只有 AI 事实审核。

- 科研 PDF 解析候选：GROBID https://github.com/grobidOrg/grobid 和 Marker https://github.com/datalab-to/marker；需要在真实上传样本上测误读率。
- 2026 年 10 月 Kling 官方开发平台已展示 4.0 Preview，但此框架保留以有明确 API 文档的 3.0 作为*适配格式示例*，不是声称其最新或最佳。 https://kling.ai/dev/api
