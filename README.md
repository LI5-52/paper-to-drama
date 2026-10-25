# Paper-to-Drama Skill｜研究版 V0.1

**定位**：论文不是必须讲完的教学内容，而是可追溯的故事创意源。选一个最有趣且能够发展为戏剧的核心问题，让用户选择三个有明显差异的创作提案中的一种，生成可供视频平台执行的剧本与分镜。

## 目录及职责

```text
paper-to-drama-skill/
├── SKILL.md                         # Skill 元数据、阶段路由与总规则
├── README.md                        # 安装/运行/边界说明
├── RESEARCH_REPORT.md               # 深读后的决策与四缺口方案
├── references/
│   ├── 01-paper-mining.md           # 全文浏览与候选趣味卡
│   ├── 02-seed-and-style.md         # 戏剧种子、一个问题/三个风格
│   ├── 03-screenplay.md             # 故事、节拍、人物与剧本
│   ├── 04-storyboard.md             # 角色资产/分镜/声画
│   ├── 05-fact-boundary.md          # 科学事实—虚构边界
│   ├── 06-quality-and-repair.md     # 跨阶段质检与定点回退
│   ├── 07-model-adapters.md         # 不同模型的输出转换策略
│   ├── 08-evidence-matrix.md        # 论文/平台/Skill 的证据矩阵与链接
│   └── 09-validation-plan.md       # 原定四缺口的验证协议
├── schemas/project.schema.json     # 可校验阶段产物的数据结构
├── examples/papertok-inspired-demo.json # 研究议题虚构改编示范（只示意）
├── evals/cases.json                # 对照与边界用例
└── scripts/validate_project.py    # 本地 JSON 结构和跨引用校验
```

## 使用方法

1. 打开 `SKILL.md`，按其 P0–P6 在支持 Agent Skills 的环境中执行。若当前环境不能直接安装为 Skill，可当工作流规约使用。
2. 在项目执行环境中配置论文解析器、LLM、视频生成服务和状态保存；这些**不包含**在此版框架中。
3. 先验证随附的结构示例：

```bash
python scripts/validate_project.py examples/papertok-inspired-demo.json
```

4. 确认三个风格始终围绕单一 `core_question_id`，参考 `evals/cases.json` 做 A/B/C 方案比较。

## 未完成事项
- 尚无可调用的 PDF-to-text、LLM orchestration、视频 API、语音/字幕/剪辑流水线；这是一份**可用于试跑的文本 Skill 框架**，不是可一键出片的完整软件。
- 没有真实平台出片的结果，因此不声称稳定性/质量已验证。
- 评分阈值、目标时长、题材偏好与成本预算需要样本测试后冻结。

## 工作簿索引
- `短剧机制与创作原则_调研.xlsx`：研究线索、创作原则、套路表（见原工作簿）。
- `短剧生成平台调研.xlsx`：平台信息架构、付费证据、开源项目索引（见原工作簿）。

此目录主要为本项目原创的描述性规则，引用的研究与开源项目均通过参考链接注明。未复制第三方 Skill 的大量正文和软件资源。
