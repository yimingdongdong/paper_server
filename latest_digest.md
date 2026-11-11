# AI x Bio 每日情报

> 生成时间 2026-11-11 07:23，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents
**一句话点评**：针对共折叠模型生成的多候选构象难以可靠排序这一小分子药物发现核心瓶颈，构建了 1500 对蛋白-配体 pose 配对排序基准，并揭示专家化学家结合 3D 可视化与物理打分也仅接近随机水平，凸显自动化排序的挑战与价值。
原文：https://arxiv.org/abs/2611.14511v1

### 2. [arXiv] Emergent Biological Capabilities in a Foundation Model for Molecular Interactions
**一句话点评**：Bonbon 在约 3.2 万亿 token 的蛋白-配体配对序列上训练，单一表示空间即零样本涌现出作用机制、结合位点定位（含正/别构区分）与共价/非共价键判断等分层能力，是分子相互作用基础模型的重要进展。
原文：https://arxiv.org/abs/2611.14504v1

### 3. [arXiv] ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening
**一句话点评**：开源端到端虚拟筛选框架，从蛋白序列出发，用 reduced-MSA 子采样构建构象集合、AF2-RAVE 短 MD 采样结合 competent 态，再集成筛选输出候选结合物排序，直击无配体晶体结构靶点的筛选难题。
原文：https://arxiv.org/abs/2611.14287v1

### 4. [arXiv] Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without High-Order Approximation
**一句话点评**：证明随机扩散采样器即便用高阶近似仍只有一阶收敛（给出匹配上下界），据此提出前向值离散化以更少 NFE 达到可比采样质量，是对 diffusion 采样理论的重要修正。
原文：https://arxiv.org/abs/2611.14328v1

### 5. [arXiv] An Energy-Based Perspective on Machine Learning
**一句话点评**：以能量模型为统一视角串联表示、采样/推理与学习三要素的教程，对理解 score-based / diffusion 与生成建模的理论根基有参考价值。
原文：https://arxiv.org/abs/2611.14383v1

### 6. [arXiv] Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models
**一句话点评**：针对块扩散语言模型中“块内最慢 token 拖累、块间串行”的效率瓶颈，提出两块并行去噪的 B3 方法，属于 diffusion 生成技术迭代。
原文：https://arxiv.org/abs/2611.14387v1

### 7. [arXiv] BioXArena-Pro: a research-grade benchmark for autonomous biomedical machine learning agents
**一句话点评**：64 个来自八个生物医学领域、重建自已发表研究的研究级建模任务，多数留出整类生物单元（物种/队列）以防泄漏，评估自主生物医学建模 Agent，最佳配置仅 55.1/100，且 scaffold 影响几乎与模型相当。
原文：https://arxiv.org/abs/2611.13994v1

### 8. [arXiv] Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning
**一句话点评**：考察五个 LLM 能否将开放式自然语言情境生成为部分可观测随机博弈形式的世界模型，并质疑“机械有效性”是否足以保证忠实表示，属 world model 方向。
原文：https://arxiv.org/abs/2611.14419v1

### 9. [arXiv] A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets
**一句话点评**：从理论上刻画后训练策略优化，提出 coverage-preserving 算法框架，指出 REINFORCE/PPO/GRPO 可能导致“覆盖坍塌”，属 LLM 后训练技巧的理论进展。
原文：https://arxiv.org/abs/2611.14467v1

### 10. [arXiv] AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
**一句话点评**：将 RLVR 中被压缩为单一结果奖励的训练经验转化为自适应训练脚手架，减少人工领域定制，属 LLM 训练技巧。
原文：https://arxiv.org/abs/2611.14515v1

### 11. [arXiv] Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations
**一句话点评**：用“对比集”（互斥且完备的竞争解释）替代单假设逐点检验，使 LLM 科学发现 Agent 在否定假设后能定位证据支持的替代解释，属 Agent 框架方法创新。
原文：https://arxiv.org/abs/2611.14514v1

### 12. [arXiv] When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents
**一句话点评**：以验证器为锚、将经验教训表示为带前置条件与预期效果的结构化假设并做证伪门控，决定何时写入持久记忆，属 Agent 自演化框架。
原文：https://arxiv.org/abs/2611.14326v1

### 13. [arXiv] Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents
**一句话点评**：指出外部记忆会导致“记忆诱发退化”，提出将教训与其来源轨迹证据链接的 WikiTrace，属 Agent 记忆机制改进。
原文：https://arxiv.org/abs/2611.14320v1

### 14. [arXiv] Accurate predictions of properties of energetic materials with tabular foundation models
**一句话点评**：用 TabPFN 表格基础模型在无调参下预测含能材料的撞击感度、分解温度与晶体密度，全面超越已发表最优模型，属小分子性质预测/ADMET 邻近方向。
原文：https://arxiv.org/abs/2611.14462v1

### 15. [arXiv] Normalizing Flows for Classical Simulation of Quantum Circuits in Phase Space
**一句话点评**：将酉门参数化为相空间概率分布间的 normalizing flow 以做量子线路经典模拟，是 normalizing flow 技术在新领域的应用，与主方向关联较弱但属生成模型技术。
原文：https://arxiv.org/abs/2611.14006v1
