# AI x Bio 每日情报

> 生成时间 2026-11-04 07:06，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] iGC: Antibody Optimization via Reinforcement Learning over a Learned Somatic Hypermutation Prior
**一句话点评**：把体细胞超突变（SHM）先验与抗原特异性选择结合，用两阶段强化学习做抗体亲和力成熟，直接对应抗体设计与结合优化。
原文：https://arxiv.org/abs/2611.05270v1

### 2. [arXiv] Molecular Prior Networks
**一句话点评**：将 Prior-data Fitted Networks（表格基础模型）引入小分子-蛋白亲和力预测，针对小样本药物发现场景，属于 binding affinity 与分子表示学习交叉方向。
原文：https://arxiv.org/abs/2611.05103v1

### 3. [arXiv] Multi-Objective Generative Optimization via Expected Hypervolume Fine-Tuning
**一句话点评**：面向 flow / diffusion 生成器的多目标微调，以期望超体积为奖励，明确以分子多性质权衡（如亲和力 vs 可合成性）为例，是分子生成与生成模型技术迭代的结合点。
原文：https://arxiv.org/abs/2611.05207v1

### 4. [arXiv] Ablating Design Choices for Protein Ensemble Generators Across Structural Regimes
**一句话点评**：用最小 Cα flow-matching 模型系统消融蛋白构象集合生成的设计选择，覆盖有序/无序/多域等结构区间，对蛋白生成与 flow matching 都有参考价值。
原文：https://arxiv.org/abs/2611.05055v1

### 5. [arXiv] Empirical Bayes Flow Matching for Continuous Cryo-EM Heterogeneity
**一句话点评**：用经验贝叶斯 + flow matching 从含噪 2D 投影中学习高维构象先验，是 flow matching 在结构生物学逆问题上的方法学推进。
原文：https://arxiv.org/abs/2611.05202v1

### 6. [arXiv] NovoCRF: Globally Normalized De Novo Peptide Sequencing on a Prefix-Mass Lattice
**一句话点评**：以 prefix-mass 为状态的 CRF 做全局归一化 de novo 多肽测序，属于多肽/质谱 AI 方法，与蛋白组学建模相关。
原文：https://arxiv.org/abs/2611.05260v1

### 7. [arXiv] GSBR: Geometric Support Behavior Regularization for Online RL
**一句话点评**：针对以 diffusion / flow-matching 模仿学习得到的基座策略做在线 RL 正则，避免过度约束，属于 flow/diffusion 策略在 RL 中的技术迭代（非生物但方法可迁移）。
原文：https://arxiv.org/abs/2611.05295v1

### 8. [arXiv] DreamX: Video Diffusion Model is a Universal Latent Action Learner
**一句话点评**：复用预训练视频扩散模型学习通用潜在动作表示，属于 diffusion 表征学习与 world model 相邻方向。
原文：https://arxiv.org/abs/2611.05377v1

### 9. [arXiv] UniFlow: Unified Multi-Scale Flow Matching for Time Series Generation
**一句话点评**：多尺度 flow matching 生成框架，属 flow matching 技术迭代，虽应用在时间序列，但方法本身可关注。
原文：https://arxiv.org/abs/2611.04825v1

### 10. [arXiv] Adversarial Speculative Reasoning Improves Long Horizon Agents
**一句话点评**：指出投机解码在长程 agent 推理中会改变输出分布，提出对抗式投机推理，属 Agent / reasoning model 训练技巧。
原文：https://arxiv.org/abs/2611.05345v1

### 11. [arXiv] MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution
**一句话点评**：用多视角蒸馏把技能记忆内化进策略，属 Agent 自进化与 on-policy 自蒸馏训练技巧。
原文：https://arxiv.org/abs/2611.05313v1

### 12. [arXiv] Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning
**一句话点评**：利用逐轮文本反馈做 on-policy 自蒸馏式定向引导，属 Agent RL 后训练方法。
原文：https://arxiv.org/abs/2611.05306v1

### 13. [arXiv] You don't need long context
**一句话点评**：通过频繁压缩维持短上下文，提出 semantic state space models 概念，对长程 agent 与上下文管理有启发。
原文：https://arxiv.org/abs/2611.05306v1

### 14. [arXiv] Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment
**一句话点评**：发现用模型自认为错误但无害的数据微调也会诱发广泛失准，属 LLM 行为与对齐研究。
原文：https://arxiv.org/abs/2611.05287v1

### 15. [arXiv] Suppressing Misaligned Behaviors in Language Models, Durably
**一句话点评**：构建窄触发/宽触发失准模型生物，研究失准行为的持久抑制，属 LLM 行为与后训练安全。
原文：https://arxiv.org/abs/2611.05358v1
