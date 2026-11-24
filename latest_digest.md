# AI x Bio 每日情报

> 生成时间 2026-11-24 10:34，由 DeepSeek 精筛。

## 今日重点

### 1. [Nature Computational Science] Generative molecular design needs oracle grounding
**一句话点评**：生成式分子设计领域的一篇观点文章，指出 oracle（计算代理目标）容易被生成模型“钻空子”，主张用实验反馈来诊断和修正 oracle 失效，这对分子生成与虚拟筛选的评估范式有直接指导意义。
原文：https://www.nature.com/articles/s43588-026-01082-x

### 2. [Nature Computational Science] Richer data improve predictions of T cell receptor binding to specific antigens
**一句话点评**：发布 Hi-TPH 大规模层级 TCR–抗原结合数据集，基于该数据训练的蛋白质语言模型在外部队列上超越现有工具，属于蛋白语言模型 + binding 预测方向的实质性数据/方法工作。
原文：https://www.nature.com/articles/s43588-026-01109-3

### 3. [arXiv] LeCellModel: Interpretable Density Estimation over the Gene Expression Manifold
**一句话点评**：把单细胞表示学习的目标从“捕获细胞类型”转为“建模基因表达流形上的细胞状态分布”，统一了密度估计、稀有状态检测、扰动打分与基因归因，契合虚拟细胞/单细胞扰动建模方向。
原文：https://arxiv.org/abs/2611.30955v1

### 4. [arXiv] Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching
**一句话点评**：揭示现有前向扩散 RL 方法本质上是带符号的 reward-weighted regression，并指出 CFG rollout 下策略速度与行为边际速度不一致的问题，属于 diffusion 对齐/训练技术迭代。
原文：https://arxiv.org/abs/2611.30986v1

### 5. [arXiv] Analyzing and Improving FlowMap Distillation of Autoregressive Video Models
**一句话点评**：分析 AR 视频生成中 FlowMap 蒸馏的瓶颈，提出 anti-drifting guidance 等两种引导机制，是 flow matching 蒸馏技术的直接迭代（虽为视频域，方法可迁移）。
原文：https://arxiv.org/abs/2611.31164v1

### 6. [arXiv] DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers
**一句话点评**：通过权重共享循环 + 稀疏专家复用参数来加深 DiT，属于 diffusion transformer 架构层面的效率/容量技术迭代。
原文：https://arxiv.org/abs/2611.30844v1

### 7. [arXiv] LeJEPA Features Are Not Isotropic, and Should Not Be
**一句话点评**：证明 LeJEPA 的 SIGReg 各向同性正则实际无法达成目标，并论证自监督编码器本就不该有各向同性特征，对 JEPA 类表示学习有直接的方法论修正价值。
原文：https://arxiv.org/abs/2611.31216v1

### 8. [arXiv] Lorentz symmetry in self-supervised representation learning
**一句话点评**：将洛伦兹等变几何代数 Transformer（L-GATr-slim）与 LeJEPA 框架结合，是等变网络 + 自监督表示学习的技术融合，几何深度学习方向可参考。
原文：https://arxiv.org/abs/2611.31011v1

### 9. [arXiv] World Models as Native Latent Action Models
**一句话点评**：把预训练视频 world model 直接当作 latent action model 使用，从稠密纠缠表示中提取动力学，属于 world model 方向有信息量的思路。
原文：https://arxiv.org/abs/2611.30898v1

### 10. [arXiv] DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation
**一句话点评**：从点云演示中学习连续 latent action 的 3D world model，支持跨具身零样本操作，属 world model + 表示学习方向。
原文：https://arxiv.org/abs/2611.30907v1

### 11. [arXiv] From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems
**一句话点评**：提出 REPA 结构模型，把局部响应与系统级误差传播联系起来，是多智能体框架可靠性分析中较扎实的一项工作。
原文：https://arxiv.org/abs/2611.31063v1

### 12. [arXiv] Can Latent Reasoning Drive LLM Outputs Without a Trace?
**一句话点评**：探讨完全隐式推理（CLR）能否支撑隐藏目标而不留 CoT 痕迹，触及 LLM 可监控性与对齐行为研究，属 LLM 行为方向。
原文：https://arxiv.org/abs/2611.31015v1

### 13. [arXiv] Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ
**一句话点评**：系统评估不确定性 token 的“原地自监控”与“下游纠错引导”两种能力，发现模型能被引导却无法真实自省，对 reasoning model 的置信度机制有参考价值。
原文：https://arxiv.org/abs/2611.31228v1

### 14. [arXiv] Beyond Self-Consistency: Recursive Self-Improvement at Test Time
**一句话点评**：指出自一致性投票会强化错误多数，提出利用历史推理进行递归自改进的测试时方法，属 LLM 推理/后训练技巧。
原文：https://arxiv.org/abs/2611.30965v1

### 15. [arXiv] Unlocking the Power of Loops in Pretrained LLMs with Loop Residuals
**一句话点评**：用 LoopRes 让预训练 LLM 的循环层直接关注早期循环输出，把“循环”从边际增益变成稳定收益，属 LLM 训练技巧。
原文：https://arxiv.org/abs/2611.31094v1
