# AI x Bio 每日情报

> 生成时间 2026-11-21 07:53，由 DeepSeek 精筛。

## 今日重点

### 1. [Nature Computational Science] Generative molecular design needs oracle grounding
**一句话点评**：生成式分子设计领域的重要观点文章，指出 oracle（计算代理目标）容易被模型“钻空子”，主张用实验反馈来诊断和修正 oracle 失效，直接关系到分子生成与药物设计的评估范式。
原文：https://www.nature.com/articles/s43588-026-01082-x

### 2. [arXiv] Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling
**一句话点评**：为 flow matching 在非高斯源分布（重尾、多峰）下的 Euler 离散化建立了非渐近收敛理论，是 flow matching 采样理论的重要补充。
原文：https://arxiv.org/abs/2611.26407v1

### 3. [arXiv] Mamba Flow Matching Neural Processes: Linear-Time Inference for Irregularly Observed Spatial Fields
**一句话点评**：将 flow matching 与 Mamba 结合用于神经过程，实现不规则观测空间场的线性时间推理，是 flow matching 在科学场建模上的架构迭代。
原文：https://arxiv.org/abs/2611.26355v1

### 4. [arXiv] Learning from Context: Leave-One-Out Prediction in Jump Diffusions
**一句话点评**：研究离散数据扩散模型中 jump diffusion 的 leave-one-out 预测，分析坐标自身状态如何削弱对坐标间依赖的学习，对离散扩散建模有方法学价值。
原文：https://arxiv.org/abs/2611.26359v1

### 5. [arXiv] Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions
**一句话点评**：提出无需密度的可逆传输框架，可在仅有样本的先验（如模拟器、黑盒生成模型输出）与数据分布间学习可逆映射，与 normalizing flow / 生成建模直接相关。
原文：https://arxiv.org/abs/2611.26187v1

### 6. [arXiv] Reward misalignment as an opportunity for materials discovery
**一句话点评**：用成对比较学习专家偏好来引导晶体扩散模型，把 reward misalignment 转化为发现新材料的信号；其“生成模型 + 偏好引导”思路对分子/材料生成有借鉴意义。
原文：https://arxiv.org/abs/2611.26186v1

### 7. [Nature Machine Intelligence] Enabling lab autonomy with reward functions and executable workflows
**一句话点评**：讨论自驱动实验室中 LLM 假设生成需与自底向上的优化结合、把假设转化为可执行工作流，属于 Agent + 科学发现交叉方向。
原文：https://www.nature.com/articles/s42256-026-01339-0

### 8. [Nature Computational Science] System of agentic AI for the discovery of metal–organic frameworks
**一句话点评**：MOFGen 多智能体系统加速可合成 MOF 的发现，是 Agent 框架用于材料/化学生成设计的代表性工作。
原文：https://www.nature.com/articles/s43588-026-01058-x

### 9. [arXiv] RL Post-Training in Diffusion Transformers Is Activation Steering
**一句话点评**：揭示扩散 Transformer 的 RL 后训练增益很大程度上可由输入无关的激活引导（固定 steering 向量）解释，对 diffusion 模型后训练机理有启发。
原文：https://arxiv.org/abs/2611.26627v1

### 10. [arXiv] dLoop: Looped Diffusion Language Models via Recurrent Latent Refinement
**一句话点评**：通过循环潜变量精炼减少扩散语言模型的去噪步数，属于 diffusion 生成模型的技术迭代。
原文：https://arxiv.org/abs/2611.26275v1

### 11. [arXiv] World Models Favor Learned Priors over Visual Evidence
**一句话点评**：研究世界模型在跨环境预测中偏向学习到的先验而非视觉证据，属于 world model 方向的可推送内容。
原文：https://arxiv.org/abs/2611.26366v1

### 12. [arXiv] Beam Model Technical Report
**一句话点评**：501B 总参 / 23.4B 激活的稀疏 MoE 模型，面向代码、推理与 agentic 负载，含大规模异步 RL 后训练细节，属 LLM 训练/后训练技巧。
原文：https://arxiv.org/abs/2611.26358v1

### 13. [arXiv] AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher
**一句话点评**：用自然语言“技能”抑制教师轨迹中的不良习惯并做自主后训练，属 LLM 后训练技巧。
原文：https://arxiv.org/abs/2611.26510v1

### 14. [arXiv] Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy
**一句话点评**：发现 RLVR 的 rollout 上限会被模型内化为学习到的约束、限制测试时扩展，对 reasoning model 训练有直接启示。
原文：https://arxiv.org/abs/2611.26172v1

### 15. [arXiv] How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents
**一句话点评**：从 agent 自身轨迹中挖掘“经验教训”并整合为指南的记忆管理方法，属 Agent 框架方向。
原文：https://arxiv.org/abs/2611.26361v1
