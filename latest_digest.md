# AI x Bio 每日情报

> 生成时间 2026-11-16 07:28，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] CARVE: A glycan-specific framework for assessing protein-glycan binding-pose quality
**一句话点评**：针对蛋白-糖结合构象预测质量评估的专用框架，用拓扑感知的糖链解析替代固定 RMSD 阈值，直接服务于结合模式评价与结构预测下游验证。
原文：https://arxiv.org/abs/2611.18259v1

### 2. [arXiv] Deciphering multiple binding modes in large protein complexes via Enhanced Sampling and beta-VAE: the CYFIP1-eIF4E case
**一句话点评**：增强采样 + β-VAE 解析大蛋白复合物的多结合模式，是生成式表示学习用于 binding mode 发现的典型案例，方法可迁移到多肽-蛋白界面建模。
原文：https://arxiv.org/abs/2611.18236v1

### 3. [arXiv] Score-based neural ordinary differential equations for reaction-diffusions
**一句话点评**：把反应-扩散方程重写为 score 驱动的输运方程并用 Neural ODE 学习，是 score-based 生成模型向带源项动力学推广的技术迭代，值得关注其与 flow matching 框架的潜在结合。
原文：https://arxiv.org/abs/2611.18467v1

### 4. [arXiv] Graph diffusion transformer for interpretable generation and inverse design of disordered atomic structures
**一句话点评**：图扩散 Transformer + 动态周期图做无序原子结构生成与逆向设计，采样加速两个数量级；几何扩散生成的方法论对分子/材料生成有直接参考价值。
原文：https://arxiv.org/abs/2611.18420v1

### 5. [arXiv] On numerical issues of divergences between nearly equal distributions
**一句话点评**：指出 KL、JSD、蒙特卡洛 KL 估计与熵在近等分布下的数值不稳定问题，直接影响扩散/流匹配训练目标与蒸馏损失的实现正确性，属于容易被忽视但很实用的技术细节。
原文：https://arxiv.org/abs/2611.18511v1

### 6. [arXiv] COPASI Skills: Agent Skills for COPASI analyses through Basico
**一句话点评**：把生化反应网络建模工具 COPASI 封装为 Agent Skills，是 Agent 框架与系统生物学建模结合的实用接口，对虚拟细胞/动力学建模工作流有参考意义。
原文：https://arxiv.org/abs/2611.18115v1

### 7. [arXiv] Training Reasoning Models in Simulation to Natively Use Real Robots
**一句话点评**：纯仿真 RL 训练开源 27B 推理模型原生操控真实机器人，无需示范；reasoning model + 具身闭环的训练范式对 world model / agent 方向有借鉴价值。
原文：https://arxiv.org/abs/2611.18562v1

### 8. [arXiv] WeatherDreamer: Learning a World Model from Multimodal Earth Observations
**一句话点评**：从多源观测端到端学习含递归滤波循环的潜状态 world model，绕开传统资料同化，是 world model 在科学观测场景的一个较扎实实例。
原文：https://arxiv.org/abs/2611.18393v1

### 9. [arXiv] Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination
**一句话点评**：用机制可解释性工具定位 LLM Agent 的网页元素幻觉失败，属于 LLM 行为/可解释性研究，对理解 agent 失效模式有方法学意义。
原文：https://arxiv.org/abs/2611.18514v1

### 10. [arXiv] Muon Attains O(ε⁻³) Iteration Complexity under Shuffling
**一句话点评**：给出 Muon 在 shuffle 采样下的迭代复杂度理论保证，是 LLM 训练优化器方向的理论进展，对大规模训练实践有间接指导。
原文：https://arxiv.org/abs/2611.18124v1

### 11. [arXiv] Folding Language Models into Themselves
**一句话点评**：用教师自身权重折叠构造学生（相邻 N 层折叠为共享块 + 低秩校正 + per-token gate），是知识蒸馏/模型压缩的训练技巧创新。
原文：https://arxiv.org/abs/2611.18113v1

### 12. [arXiv] Neural Classifiers as Error-Correcting Codes
**一句话点评**：把 softmax 分类统一为 Shannon 意义下的纠错码解码，并将 Neural Collapse 与 LeJEPA 几何解释为最优码字星座，涉及 JEPA 表示几何，理论视角较新颖。
原文：https://arxiv.org/abs/2611.18239v1

### 13. [arXiv] Right Token, Right Time: From Per-Token Gating to Trajectory-Aware Activation Steering
**一句话点评**：把 SAE 激活引导重构为固定预算下的 per-token 分配问题，是 LLM 行为控制/后训练干预的技巧性改进。
原文：https://arxiv.org/abs/2611.18274v1

### 14. [arXiv] ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL
**一句话点评**：把 agentic RL 中的 harness 从手写固定脚手架改为可学习、随训练演化的程序，属于 Agent 框架与 RL 训练结合的方向。
原文：https://arxiv.org/abs/2611.18533v1

### 15. [arXiv] Agent-as-a-Judge
**一句话点评**：系统讨论 LLM-as-a-Judge 在需要外部证据时的局限并提出 Agent 化评审范式，对 agent 评测与后训练反馈管线有参考价值。
原文：https://arxiv.org/abs/2611.18067v1
