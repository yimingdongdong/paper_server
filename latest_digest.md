# AI x Bio 每日情报

> 生成时间 2026-11-12 07:52，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents
**一句话点评**：蛋白-配体 pose 排序基准（1500 对 pose），专家化学家接近随机水平，凸显 cofolding 模型生成后排序环节的关键瓶颈，直接命中 docking/虚拟筛选方向。
原文：https://arxiv.org/abs/2611.14511v1

### 2. [arXiv] Emergent Biological Capabilities in a Foundation Model for Molecular Interactions
**一句话点评**：Bonbon 在 3.2T token 的蛋白-配体配对序列上训练，零样本涌现出作用机制、结合位点定位（含正/别构区分）、共价/非共价判别等能力，是分子相互作用基础模型的重要进展。
原文：https://arxiv.org/abs/2611.14504v1

### 3. [arXiv] ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening
**一句话点评**：从蛋白序列到候选 binder 排序的端到端开源虚拟筛选流程，结合 ColabFold 构象系综与 AF2-RAVE 短 MD 采样，解决 apo/单模型缺失结合构象的痛点。
原文：https://arxiv.org/abs/2611.14287v1

### 4. [arXiv] Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without High-Order Approximation
**一句话点评**：证明随机扩散采样器即使高阶近似仍为一阶收敛（给出上下界），并提出前向值离散化加速，是 diffusion 采样理论+实践的双重贡献。
原文：https://arxiv.org/abs/2611.14328v1

### 5. [arXiv] An Energy-Based Perspective on Machine Learning
**一句话点评**：Bo Dai 与 Yilun Du 的 EBM 教程，用能量、推断、学习三要素统一串联生成模型与表示学习，对理解 diffusion/score-based 的理论根基有参考价值。
原文：https://arxiv.org/abs/2611.14383v1

### 6. [arXiv] Normalizing Flows for Classical Simulation of Quantum Circuits in Phase Space
**一句话点评**：将酉门参数化为相空间分布间的 normalizing flow，属于 normalizing flow 技术在新领域的迭代应用，方法层面可迁移。
原文：https://arxiv.org/abs/2611.14006v1

### 7. [arXiv] BioXArena-Pro: a research-grade benchmark for autonomous biomedical machine learning agents
**一句话点评**：64 个研究级生物医学建模任务、22 种 agent 配置，最佳仅 55.1 分且 scaffold 影响几乎与模型相当，是生物医学 Agent 能力评估的重要基准。
原文：https://arxiv.org/abs/2611.13994v1

### 8. [arXiv] A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets
**一句话点评**：从理论上刻画 RL 后训练中的 coverage collapse 现象，指出 REINFORCE/PPO/GRPO 可能压低最优响应概率，并提出 coverage-preserving 算法框架，对 LLM 后训练有直接指导意义。
原文：https://arxiv.org/abs/2611.14467v1

### 9. [arXiv] AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
**一句话点评**：把 RLVR 中被压缩成单一标量的训练经验转化为自适应 scaffold，减少人工设计 hint/strategy 的依赖，属于 LLM 训练技巧方向的可复用思路。
原文：https://arxiv.org/abs/2611.14515v1

### 10. [arXiv] Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning
**一句话点评**：检验五个 LLM 能否把自然语言情境生成为部分可观测随机博弈形式的世界模型，并质疑“机械有效性”是否等于“忠实表征”，切中 world model 评估核心问题。
原文：https://arxiv.org/abs/2611.14419v1

### 11. [arXiv] Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations
**一句话点评**：用互斥完备的对比假设集替代单假设检验，让 LLM agent 在证据拒绝某解释时能定位到支持哪个替代解释，是科学发现 Agent 的方法改进。
原文：https://arxiv.org/abs/2611.14514v1

### 12. [arXiv] Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models
**一句话点评**：块扩散语言模型中并行精炼相邻两块以突破“最慢 token”瓶颈，属于 diffusion 在语言建模上的效率迭代。
原文：https://arxiv.org/abs/2611.14387v1

### 13. [arXiv] Accurate predictions of properties of energetic materials with tabular foundation models
**一句话点评**：TabPFN 在含能材料的三项分子性质预测上无需调参即超越已发表最优模型与 Chemprop 表示，对小分子性质预测/ADMET 类任务有方法借鉴价值。
原文：https://arxiv.org/abs/2611.14462v1

### 14. [arXiv] Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents
**一句话点评**：指出 agent 外部记忆会导致“记忆诱发退化”，提出带证据链接的 WikiTrace 让 agent 可核查经验来源，是 Agent 记忆机制的重要反思。
原文：https://arxiv.org/abs/2611.14320v1

### 15. [arXiv] When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents
**一句话点评**：用可验证的证伪门控决定经验是否写入持久记忆，与上一条互补，共同回应 Agent 自演化中“局部成功≠可复用知识”的问题。
原文：https://arxiv.org/abs/2611.14326v1
