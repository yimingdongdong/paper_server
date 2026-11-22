# AI x Bio 每日情报

> 生成时间 2026-11-22 07:38，由 DeepSeek 精筛。

## 今日重点

### 1. [Nature Computational Science] Generative molecular design needs oracle grounding
**一句话点评**：生成式分子设计领域的重要观点文章，指出 oracle（计算代理目标）会被模型利用，主张用实验诊断并修正 oracle 失败，让生成模型不仅发现新分子还能发现新化学。
原文：https://www.nature.com/articles/s43588-026-01082-x

### 2. [arXiv] Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling
**一句话点评**：为非高斯（重尾、多峰）源分布的 flow matching 建立有限步 Euler 离散的非渐近收敛理论，直接对应 flow matching 采样效率的理论迭代。
原文：https://arxiv.org/abs/2611.26407v1

### 3. [arXiv] Mamba Flow Matching Neural Processes: Linear-Time Inference for Irregularly Observed Spatial Fields
**一句话点评**：用 Mamba 替代自注意力构建 flow matching 神经过程，实现不规则观测空间场的线性时间联合预测，是 flow matching 与神经过程结合的方法迭代。
原文：https://arxiv.org/abs/2611.26355v1

### 4. [arXiv] Learning from Context: Leave-One-Out Prediction in Jump Diffusions
**一句话点评**：研究离散数据扩散模型中 jump diffusion 的 leave-one-out 预测，分析坐标自身损坏状态如何削弱对坐标间依赖的学习，对离散扩散建模有直接方法意义。
原文：https://arxiv.org/abs/2611.26359v1

### 5. [arXiv] Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions
**一句话点评**：提出无需密度的可逆映射框架，在仅有样本的先验与数据分布间学习 normalizing flow，对科学模拟器/黑盒生成模型作为先验的场景有实用价值。
原文：https://arxiv.org/abs/2611.26187v1

### 6. [arXiv] Reward misalignment as an opportunity for materials discovery
**一句话点评**：把奖励错位视为发现机会，用成对比较学习专家偏好来引导晶体扩散模型，属于生成模型 + 科学发现的方法论，思路可迁移到分子生成。
原文：https://arxiv.org/abs/2611.26186v1

### 7. [arXiv] RL Post-Training in Diffusion Transformers Is Activation Steering
**一句话点评**：揭示扩散 Transformer 的 RL 后训练增益很大程度上可由输入无关的固定 steering 向量解释，对 diffusion 模型后训练机制有启发。
原文：https://arxiv.org/abs/2611.26627v1

### 8. [arXiv] dLoop: Looped Diffusion Language Models via Recurrent Latent Refinement
**一句话点评**：通过循环潜变量精炼减少扩散语言模型的去噪步数，属于 diffusion 生成效率的技术迭代。
原文：https://arxiv.org/abs/2611.26275v1

### 9. [Nature Machine Intelligence] Enabling lab autonomy with reward functions and executable workflows
**一句话点评**：主张自驱动实验室中 LLM 假设生成需配合自底向上的优化，把假设翻译为可执行工作流，属于 Agent + 科学自动化的框架性讨论。
原文：https://www.nature.com/articles/s42256-026-01339-0

### 10. [Nature Computational Science] System of agentic AI for the discovery of metal–organic frameworks
**一句话点评**：MOFGen 多智能体系统加速可合成 MOF 发现，是 Agent 框架用于材料/分子发现的代表性工作。
原文：https://www.nature.com/articles/s43588-026-01058-x

### 11. [arXiv] Beam Model Technical Report
**一句话点评**：501B 总参/23.4B 激活的稀疏 MoE 模型，面向代码、推理与 agentic 负载，含大规模异步 RL 后训练与 1M 上下文，属 reasoning/agent 基座模型的重要技术报告。
原文：https://arxiv.org/abs/2611.26358v1

### 12. [arXiv] World Models Favor Learned Priors over Visual Evidence
**一句话点评**：研究世界模型在跨环境预测中偏向学习到的先验而非视觉证据，对 world model 的泛化与偏差分析有参考价值。
原文：https://arxiv.org/abs/2611.26366v1

### 13. [arXiv] One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning
**一句话点评**：复用预训练视频 DiT 同时提供逆动力学与正动力学先验做潜动作学习，是 video diffusion 用于 world model/动力学建模的方法迭代。
原文：https://arxiv.org/abs/2611.26617v1

### 14. [arXiv] AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher
**一句话点评**：用自然语言 skill 抑制教师 rollout 中的不良行为并自主动态后训练，属 LLM 后训练技巧的实用迭代。
原文：https://arxiv.org/abs/2611.26510v1

### 15. [arXiv] Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy
**一句话点评**：发现 RLVR 的 rollout 上限会被模型内化为学习到的约束、限制测试时扩展，对 reasoning model 训练策略有直接警示意义。
原文：https://arxiv.org/abs/2611.26172v1
