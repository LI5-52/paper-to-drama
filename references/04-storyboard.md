# P5 剧本 → 资产 → 分镜 → 视频提示词

## 顺序与契约
1. 剧本冻结后抽取 `character_bible/location_bible/prop_bible`；稳定 ID、外形、声线、场景朝向、道具所有权；服装变化要有剧情依据。
2. 每一场景分割成若干**镜头职责清晰**的 shot（例如发现线索、反应、转移注意力），不要把一个故事场景自动视为单个视频镜头。
3. 每镜记录 `shot_id, scene_id, beat_id, purpose, location_ref, character_refs, start_state, main_visible_action, end_state, camera, framing, duration_s, dialogue, voice_sfx_bgm, continuity, keyframe_refs, evidence_refs`。
4. 严格检查位置/视线/手持物/服装/出入场/信息状态；相邻镜头的 `end_state → start_state` 应可解释。
5. 视频模型提示词只由经审查的镜头数据产生；**不要让文本变成长篇抽象感受词堆砌**。镜头应能看见主体动作，限制同时需要完成的复杂转场与转换。
6. 多镜头合并须根据选定生成模型确认时长、镜数、声画支持，不假设一个“多镜头 prompt”在所有平台上有效。
7. 生成后确认镜头与台词关系，再按可用片段剪辑；字幕/精确屏幕文字可根据模型能力选择后期合成。

## 分镜文本示例（虚构）
镜头 S01-SH02：前景女主停止敲击键盘（主体动作），抬头看向屏幕，眼神由高兴变为疑惑（终态）；近景，固定机位缓慢推近；屏幕原文字不强制由视频模型直接渲染，后期叠加“创作者署名”。

## 来源
ZenStory storyboard: https://github.com/zenstory-ai/drama-skills/blob/main/skills/short-drama-storyboard/SKILL.md
小云雀手册（角色场景资产/分镜关联）: https://xyq.jianying.com/tutorials/web-manual
Katalist Story Canvas（剧本自动拆场景和镜头）: https://help.katalist.ai/en/articles/16298583-how-to-build-your-storyboard-and-videos-in-story-canvas
Runway Gen-4 Video Prompt Guide（图像提供静态信息、提示词强调运动）: https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
