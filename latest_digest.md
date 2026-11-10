# AI x Bio 每日情报

> 生成时间 2026-11-10 07:54，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] Kolmogorov-Chapman Maps: Trajectory-Free Learning for Simulating Molecular Dynamics
**一句话点评**：用神经网络直接学习 SDE 的 Kolmogorov-Chapman 半群映射，把百万步分子动力学积分摊销为单次前向，属于生成模型/随机过程与分子模拟交叉的方法迭代，值得关注。
原文：https://arxiv.org/abs/2611.12880v1

### 2. [arXiv] What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching
**一句话点评**：从 patch-wise PCA 角度解释像素空间 flow matching 中 v-prediction 训练困难的带宽瓶颈，并指向 x-prediction，直接命中 flow matching 技术迭代。
原文：https://arxiv.org/abs/2611.12852v1

### 3. [arXiv] stMIND: Learning multiscale interaction dynamics from spatial-temporal transcriptomics
**一句话点评**：基于 interacting mean-field neural SDE 框架，从时空转录组学习多尺度细胞邻域相互作用与状态转移，属于虚拟细胞/细胞状态建模方向。
原文：https://arxiv.org/abs/2611.12228v1

### 4. [arXiv] The balance between feature learning and collapse in dynamical systems-based generative models
**一句话点评**：从学习理论角度分析 normalizing flow / diffusion 等连续时间生成模型的特征学习与 mode collapse 隐式偏置，属于生成模型理论迭代。
原文：https://arxiv.org/abs/2611.12156v1

### 5. [arXiv] Two-Phase Rapid Simulation-Based Inference with Differentiable Simulators
**一句话点评**：基于 Schrödinger Bridge 扩散采样的变分推断方法，用可微模拟器提供代理似然实现高效 one-shot 后验采样，属 diffusion/score-based 方法迭代。
原文：https://arxiv.org/abs/2611.12422v1

### 6. [arXiv] SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery
**一句话点评**：面向闭环科学发现的多智能体递归自改进框架，用共享证据图与组件编辑器协调角色，属 Agent/多智能体框架方向。
原文：https://arxiv.org/abs/2611.12552v1

### 7. [arXiv] WanderBench: Can World Models Explore Dynamic Worlds from Video?
**一句话点评**：针对视频条件世界模型探索动态场景的基准，评估主体一致性、事件推进与场景一致性，属 world model 方向。
原文：https://arxiv.org/abs/2611.12557v1

### 8. [arXiv] $Σ$-LeWM: Learning World Models via S-Information for Robot Control
**一句话点评**：在无解码器的 JEPA/LeWorldModel 式世界模型上引入额外潜变量损失以稳定表示学习，直接涉及 JEPA 与 world model。
原文：https://arxiv.org/abs/2611.12732v1

### 9. [arXiv] How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time
**一句话点评**：在 ARC-AGI-3 上量化世界模型学习新机制所需曝光次数，提出 MechEval，属 world model 能力评估。
原文：https://arxiv.org/abs/2611.12324v1

### 10. [arXiv] Learning to Act with World Models by Valuing What Comes Next
**一句话点评**：WM-PPO 用世界模型预测状态转移并估计成功概率以缓解稀疏终端奖励，属 world model + RL 方法。
原文：https://arxiv.org/abs/2611.12200v1

### 11. [arXiv] Is Persona Generalization Predictable?
**一句话点评**：发现微调引发的 persona 泛化在域内外呈近似 probit 线性关系且跨模型族共享，属 LLM 行为/后训练研究。
原文：https://arxiv.org/abs/2611.12864v1

### 12. [arXiv] Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks
**一句话点评**：指出 GRPO 训练中丢弃的 checkpoint 可组成免费教师池，用 on-policy distillation 恢复已遗忘的 agent 能力，属 LLM 后训练技巧。
原文：https://arxiv.org/abs/2611.12799v1

### 13. [arXiv] WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems
**一句话点评**：把多智能体系统运行时自行编排可执行工作流的能力形式化为独立能力并给出基准，属 Agent 框架评估。
原文：https://arxiv.org/abs/2611.12856v1

### 14. [arXiv] Good Views Are Not Enough: Global Counterexamples for Gaussian-Regularized JEPAs
**一句话点评**：给出高斯正则化 JEPA 全局最优解的反例，说明好视图不足以保证场景不变性与唯一性，属 JEPA 理论分析。
原文：https://arxiv.org/abs/2611.12137v1

### 15. [arXiv] Mitigating Agentic Deception via Evaluation-Side Partially Observable Games
**一句话点评**：将 agent 欺骗行为归因于评估侧部分可观测性，并提出基于部分可观测博弈的缓解方法，属 LLM 行为/Agent 安全研究。
原文：https://arxiv.org/abs/2611.12835v1
