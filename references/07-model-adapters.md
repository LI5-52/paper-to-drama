# 视频生成模型适配：只在 P6 加载

## 通用输出
每镜输出：角色/场景资产引用、画面初始信息、可见动作、运镜、结束画面、预期时长、音频/字幕策略、与上镜接续、目标效果、失败备用方案。对外输出平台无关 JSON；平台适配器作最末级映射。

## 平台策略（以执行日官方文档为准）
- **Runway Gen-4**：图像提供外貌/环境时，文本主要描述主体和摄像机运动。平台文档指定 Gen-4 5 或 10 秒选项；不要强制把所有镜头写成独立 10 秒；不同模型版本可能不同。官方：https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
- **Kling**：API 对多镜头文本有格式约束，写专用转换函数并在调用前核实账号使用的 API 与模型版本。官方：https://kling.ai/document-api/apiReference/model/textToVideo
- **Seedance / Volcengine**：依据所用 API 的最新图像参考、音频、时长、格式限制映射。官方：https://docs.volcengine.com/docs/ark/video-generation-tutorial?lang=zh
- **小云雀/Katalist/LTX**：重点借鉴项目、角色、场景、分镜的资产联动，不能假定其网页内编辑能力可通过公开 API 完整调用。

## 调用安全与状态
此版本不含任何 API key，不向用户声称已连接平台。外部生成器应提供：`submit/status/result/error`、权限、费用、失败重试、资产 URI、clip-id 与 clip-version；只在真实收到成功结果后标记 `video_ready`。
