# AI x Bio 每日情报

> 生成时间 2026-11-20 07:55，由 DeepSeek 精筛。

## 今日重点

### 1. [Nature Computational Science] Generative molecular design needs oracle grounding
**一句话点评**：生成式分子设计的关键瓶颈在于 oracle 与真实实验目标之间的偏差；作者主张用实验诊断并修正 oracle 失败，从而让生成模型不仅发现新分子，还能发现新化学。
原文：https://www.nature.com/articles/s43588-026-01082-x

### 2. [arXiv] Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling
**一句话点评**：针对非高斯源分布（重尾、多峰）的 flow matching 给出有限步 Euler 离散的非渐近收敛理论，直接补上 flow matching 采样保证的一块理论空白。
原文：https://arxiv.org/abs/2611.26407v1

### 3. [arXiv] RL Post-Training in Diffusion Transformers Is Activation Steering
**一句话点评**：发现 diffusion transformer 的 RL 后训练增益很大程度上可由一组输入无关的固定 steering 向量解释，对理解扩散模型后训练机制有直接启发。
原文：https://arxiv.org/abs/2611.26627v1

### 4. [arXiv] Mamba Flow Matching Neural Processes: Linear-Time Inference for Irregularly Observed Spatial Fields
**一句话点评**：用 Mamba 替换自注意力实现 flow matching 神经过程，把不规则观测空间场的联合预测降到线性时间，是 flow matching 与神经过程结合的方法迭代。
原文：https://arxiv.org/abs/2611.26355v1

### 5. [arXiv] Learning from Context: Leave-One-Out Prediction in Jump Diffusions
**一句话点评**：研究离散数据扩散中 jump diffusion 的 leave-one-out 预测，指出坐标自身被破坏的状态会削弱对坐标间依赖的学习，对离散扩散/流模型的训练目标设计有参考价值。
原文：https://arxiv.org/abs/2611.26359v1

### 6. [arXiv] Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions
**一句话点评**：提出无需密度的可逆传输框架，可在仅有样本的分布之间学习可逆映射，属于 normalizing flow 类方法在 sample-only 先验上的扩展。
原文：https://www.nature.com/articles/s43588-026-01080-z

### 7. [Nature Computational Science] Cognitive grounding improves LLM simulation of collective human behavior
**一句话点评**：用人类决策描述对 LLM agent 做认知 grounding，可更好复现集体人类行为，属于 LLM agent 行为建模方向。
原文：https://www.nature.com/articles/s43588-026-01080-z

### 8. [Nature] AI is ditching hallucinated references — and other bad habits
**一句话点评**：分析发现多种不良 LLM 行为在约 16 个月后自行消退，属于 LLM 行为演化的观察性资讯。
原文：https://www.nature.com/articles/d41586-026-03753-1

### 9. [arXiv] World Models Favor Learned Priors over Visual Evidence
**一句话点评**：研究 world model 在跨环境物理规则推断中偏向学习到的先验而非视觉证据，对 world model 的泛化与偏差分析有参考意义。
原文：https://arxiv.org/abs/2611.26366v1

### 10. [arXiv] Beam Model Technical Report
**一句话点评**：501B 总参/23.4B 激活的稀疏 MoE 模型，面向代码、推理与 agentic 负载，含大规模异步 RL 后训练与 1M 上下文两阶段 midtraining，属 LLM 训练/后训练工程参考。
原文：https://arxiv.org/abs/2611.26358v1

### 11. [arXiv] AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher
**一句话点评**：用自然语言 skill 抑制教师 rollout 中的不良行为再做微调，是后训练技巧层面的方法迭代。
原文：https://arxiv.org/abs/2611.26510v1

### 12. [arXiv] Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy
**一句话点评**：揭示 RLVR 的固定 rollout 上限会被模型内化为学习到的约束，限制测试时扩展，属 reasoning model 训练技巧的重要观察。
原文：https://arxiv.org/abs/2611.26172v1

### 13. [arXiv] dLoop: Looped Diffusion Language Models via Recurrent Latent Refinement
**一句话点评**：通过循环潜变量精炼减少 diffusion 语言模型的去噪步数，属扩散生成模型效率方向的技术迭代。
原文：https://arxiv.org/abs/2611.26275v1

### 14. [arXiv] Reward misalignment as an opportunity for materials discovery
**一句话点评**：把奖励错配当作发现机会，用专家成对偏好引导晶体扩散模型寻找被数值奖励忽略的材料，属生成模型+科学发现，方法可迁移到分子生成。
原文：https://arxiv.org/abs/2611.26186v1

### 15. [arXiv] Perfumer: A Large Language Model-based Agentic Framework Accelerating Structural Relaxation and Electronic Band Prediction for First-Principle Calculation
**一句话点评**：LLM agent 耦合 QE 与周期图神经网络做结构弛豫与能带预测，属科学计算 agent + 图神经网络应用，与分子/材料生成方法邻近。
原文：https://arxiv.org/abs/2611.26349v1
