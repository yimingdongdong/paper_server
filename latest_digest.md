# AI x Bio 每日情报

> 生成时间 2026-11-02 06:59，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] General-purpose foundation models surpass specialized ones on chemical property prediction tasks
**一句话点评**：通用基础模型（GPT-6 Astra、Claude Opus 5.5）在化学性质预测上超过 ChemBERTa、MoLFormer 等专用分子基础模型，直接挑战“领域专用预训练”的默认假设，对分子表示学习路线选择有参考价值。
原文：https://arxiv.org/abs/2610.41899v1

### 2. [arXiv] WASABI: Wasserstein Sampling via Bridge Interpolants
**一句话点评**：用 Wasserstein 梯度流训练扩散模型，从能量函数采样 Boltzmann 分布，面向物理/化学/生物采样问题，属于 diffusion 采样与科学计算交叉的方法迭代。
原文：https://arxiv.org/abs/2610.41958v1

### 3. [arXiv] Asynchronous Flow Map Language Models
**一句话点评**：把 token 预测顺序编码进 flow map，实现一步并行语言建模，是 flow matching 在离散序列生成上的新变体，技术路线值得跟踪。
原文：https://arxiv.org/abs/2610.42018v1

### 4. [arXiv] A Better Critic Matters for Distribution Matching Distillation
**一句话点评**：系统分析 DMD 中 critic 的容量与信息需求，提出 teacher-critic 联合 scaling 防止训练崩溃，对少步扩散蒸馏的实践有直接指导意义。
原文：https://arxiv.org/abs/2610.42135v1

### 5. [arXiv] Learning Clean Generative Processes from Noisy Measurements
**一句话点评**：仅用噪声观测学习干净数据生成模型，给出 Noise2Noise 与一致性约束下的可学习性条件，属于 diffusion/score-based 训练理论层面的推进。
原文：https://arxiv.org/abs/2610.42036v1

### 6. [arXiv] Locality-Controlled Out-of-Distribution Guidance for Robust Regulatory DNA Sequence Design
**一句话点评**：用扩散模型做调控 DNA 序列的条件生成，揭示单奖励评估下的 reward hacking，并分解为活性/新颖性/合理性三目标，属于生物序列生成设计方向。
原文：https://arxiv.org/abs/2610.41736v1

### 7. [arXiv] Do LLMs Know When They Are Wrong About Molecules? In-Context Property Prediction with Self-Reported Uncertainty
**一句话点评**：评估 7 个前沿 LLM 在分子性质预测中的上下文学习与自报不确定性，并做训练数据污染筛查，对“LLM 直接做分子性质预测”这一路线有校准价值。
原文：https://arxiv.org/abs/2610.41745v1

### 8. [arXiv] Hierarchical World Models with Implicit Dynamics
**一句话点评**：LeCun 组出品，解耦状态可达性与局部控制的分层 world model，缓解长程规划中的累积误差，属于 world model 方向的重点工作。
原文：https://arxiv.org/abs/2610.42146v1

### 9. [arXiv] CausalWAM: Learning the Causes of Actions in World Action Models
**一句话点评**：从因果角度分离动作相关隐变量与 nuisance 变量，提升 world action model 的动作生成可靠性，与 world model / 因果表示学习交叉。
原文：https://arxiv.org/abs/2610.42096v1

### 10. [arXiv] BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion
**一句话点评**：仅用 LoRA 把 Gemma、Llama、Qwen、Mistral 等 AR 模型转成扩散语言模型，参数占比 4–6%，是 diffusion LM 低成本迁移的实用配方。
原文：https://arxiv.org/abs/2610.41574v1

### 11. [arXiv] RangeSWA: Training-Free Length Extrapolation for Continuous Diffusion Language Models
**一句话点评**：针对连续扩散语言模型的长文本退化（重复、语义漂移）提出免训练外推方法，属于 diffusion LM 的推理期改进。
原文：https://arxiv.org/abs/2610.42084v1

### 12. [arXiv] CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness
**一句话点评**：用打乱 CoT 构造因果奖励，解决 RLVR 只奖励结果正确、不保证推理链真正起作用的问题，属于 reasoning model 后训练技巧。
原文：https://arxiv.org/abs/2610.42054v1

### 13. [arXiv] Flide: Accelerating Decision Inference with Exact State Forking
**一句话点评**：针对 decision model（System One 式 LLM agent 推理）的精确推理引擎，消除前缀重算并保持输出概率不失真，属于 Agent 推理基础设施。
原文：https://arxiv.org/abs/2610.42148v1

### 14. [arXiv] SecPO: Principled Adversarial Training for Prompt Injection Security
**一句话点评**：指出 DPO 式防御因锚定无防御参考模型而失效，提出近似 injection-invariant oracle 的对抗训练，是 Agent 安全方向较扎实的一篇。
原文：https://arxiv.org/abs/2610.41998v1

### 15. [arXiv] EMFF-MACE: Shock Loading Accesses Reaction Pathways beyond Accelerated Thermolysis
**一句话点评**：面向 C/H/N/O 含能材料的反应性机器学习势，统一热解与冲击模拟，属于 ML force field / 分子模拟方法，与药物设计间接相关但方法可迁移。
原文：https://arxiv.org/abs/2610.41955v1
