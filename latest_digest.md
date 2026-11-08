# AI x Bio 每日情报

> 生成时间 2026-11-08 06:50，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] On the limitations of molecular representations
**一句话点评**：系统评估了当前分子表示（指纹与学习嵌入）在捕捉图结构、3D 形状和 ADMET 端点相似性上的能力，发现现有 SOTA 分子嵌入模型均不如简单基线，对虚拟筛选与分子生成中的表示选择有直接警示意义。
原文：https://arxiv.org/abs/2611.08420v1

### 2. [arXiv] Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking
**一句话点评**：基于 DiffDock 研究扩散对接的后训练监督策略，发现聚焦“几何相关”误差的监督并不优于广覆盖的 score field 训练，对 diffusion-based docking 的后训练设计有方法学价值。
原文：https://arxiv.org/abs/2611.08249v1

### 3. [arXiv] FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning
**一句话点评**：将 RL 后训练目标系统适配到少步扩散模型（变换—分解—适配三阶段），解决少步模型建模区间平均速度与现有瞬时速度 RL 目标不匹配的问题，属于 diffusion/flow 生成模型技术迭代。
原文：https://arxiv.org/abs/2611.08240v1

### 4. [Nature] An open structure-guided RNA foundation model for generalizable prediction
**一句话点评**：structRFM 在 2100 万序列–结构对上预训练，融合多模态表示提升 RNA 二级/三级结构预测与零样本泛化，是结构引导基础模型在核酸领域的延伸，与蛋白/RNA 结构建模方法互通。
原文：https://www.nature.com/articles/d41586-026-11210-2

### 5. [arXiv] MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation
**一句话点评**：从 DNA 序列出发联合建模染色质可及性与基因表达，保留 DNA 级与细胞级分辨率，属于单细胞基因调控/细胞状态建模方向。
原文：https://arxiv.org/abs/2611.08086v1

### 6. [arXiv] Towards Multiscale Molecular Representation Learning through Geometry-Based Fragmentation for Polymer Property Prediction
**一句话点评**：用几何驱动的自适应碎片化替代预定义化学规则，构建多尺度分子表示用于聚合物性质预测，属于分子表示学习与几何深度学习交叉方向。
原文：https://arxiv.org/abs/2611.07998v1

### 7. [arXiv] La-JEPA: Compact Robot Policies with Latent World Modeling
**一句话点评**：在 V-JEPA 2.1 特征空间中从头训练紧凑 world-action 策略，联合预测未来特征与动作，是 JEPA/world model 方向的新进展。
原文：https://arxiv.org/abs/2611.08156v1

### 8. [arXiv] SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization
**一句话点评**：数百个低成本 agent 在潜空间内推理、通过 KV cache 传递信息进行进化搜索，避免长文本 CoT 解码开销，属于多智能体框架与 LLM 推理效率方向。
原文：https://arxiv.org/abs/2611.08483v1

### 9. [arXiv] SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains
**一句话点评**：面向掩码扩散语言模型的免训练投机采样器，在保持精确连续时间采样分布的同时减少逐 token 串行评估，属于 diffusion 生成模型推理技术迭代。
原文：https://arxiv.org/abs/2611.08362v1

### 10. [arXiv] Measured Coupling for Parallel Decoding in Diffusion Language Models
**一句话点评**：用前向传播内的廉价探针直接测量 token 提交间的耦合强度，替代 mean-field 代理，减少扩散语言模型并行解码步数，属 diffusion 解码方法改进。
原文：https://arxiv.org/abs/2611.08307v1

### 11. [arXiv] Learning Dynamics of On-Policy Distillation
**一句话点评**：对 on-policy distillation 的反馈回路做机制性分析，区分蒸馏信号转参数更新与分布广播两阶段，属于 LLM 后训练技巧研究。
原文：https://arxiv.org/abs/2611.08016v1

### 12. [arXiv] CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation
**一句话点评**：通过学生–教师几何插值与投机解码的最大耦合生成 rollout，弥补 on-policy 蒸馏中教师可达但学生未覆盖状态的监督盲区，属 LLM 后训练方法。
原文：https://arxiv.org/abs/2611.07959v1

### 13. [arXiv] Towards interpreting any residual stream direction by scaling activation inversion
**一句话点评**：用最大化激活示例元模型（MAEM）将残差流方向映射到强激活文本，以无标签 RL 目标扩展可解释性方法，属 LLM 行为/可解释性研究。
原文：https://arxiv.org/abs/2611.08465v1

### 14. [arXiv] Same Answer, Different Future: Matched Predictions Do Not Imply Matched Belief Updating in Language Models
**一句话点评**：在贝叶斯推断任务中发现预测一致并不代表信念更新一致，揭示 LLM 内部信念状态与输出解耦，属 LLM 行为研究。
原文：https://arxiv.org/abs/2611.07913v1

### 15. [arXiv] ChemE-as-Code: An Open-Source Platform for Agentic AI in Chemical Engineering
**一句话点评**：面向化学工程的 agentic AI 开源平台，计算在 LLM 外执行并记录数值来源，虽偏流程工程，但其“可核查 agent + 化学计算工具”范式对药物设计/分子工作流 agent 化有参考价值。
原文：https://arxiv.org/abs/2611.07947v1
