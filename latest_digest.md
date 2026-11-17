# AI x Bio 每日情报

> 生成时间 2026-11-17 08:41，由 DeepSeek 精筛。

## 今日重点

### 1. [arXiv] Classical structural priors improve neural molecular representations in molecule language models
**一句话点评**：提出 SAGA，用 CKA 将分子语言模型的嵌入空间与指纹 Tanimoto 相似度对齐，无需额外参数或推理期指纹，直接改善分子-文本检索与结构感知表示，属于分子表示学习与药物设计基础工具链的实用改进。
原文：https://arxiv.org/abs/2611.21276v1

### 2. [arXiv] Emergent Steering Beyond Endpoint Alignment in Chemical Reaction Models
**一句话点评**：UniRxnAxis 将正/逆合成统一为共享隐空间中的方向条件端点重分布，并做方向性审计，超越端点准确率来刻画反应模型的隐空间几何，对分子生成与反应预测的可解释建模有参考价值。
原文：https://arxiv.org/abs/2611.21423v1

### 3. [arXiv] Comments on "Deep Fréchet Regression"
**一句话点评**：以 conditional flow matching 直接在响应空间学习协变量依赖的传输，绕开流形学习+逆映射两步走，是 flow matching 在条件分布建模上的一个简洁技术视角，可迁移到分子/细胞条件生成。
原文：https://arxiv.org/abs/2611.21454v1

### 4. [arXiv] SADL: On the Demand-Supply Geometry of Representation Collapse
**一句话点评**：针对 JEPA 类架构的表示坍缩，指出投影器后正则无法纠正编码器层面的共享分量主导，提出直接在编码器上约束的 SADL，属于 JEPA/表示学习方向值得跟进的技术诊断。
原文：https://arxiv.org/abs/2611.21596v1

### 5. [arXiv] The Price of Not Planning: Parallel Sampling Depth Peaks at the Reconstruction Threshold
**一句话点评**：分析 masked diffusion 并行采样中“先规划后填充”何时省轮次、规划需多细，给出与重建阈值相关的下界，对 diffusion 采样策略设计有理论指导意义。
原文：https://arxiv.org/abs/2611.21285v1

### 6. [arXiv] Stream of Belief: Eliciting Collective Intelligence through Latent Belief Dynamics
**一句话点评**：将多智能体推理建模为隐信念动力学的集体均衡求解，智能体维护连续隐信念并迭代通信/反思，属于多智能体框架与推理模型交叉的新视角。
原文：https://arxiv.org/abs/2611.21250v1

### 7. [arXiv] Latent Lattice Language Models
**一句话点评**：通过每层横向隐流（Lattice of Latents）沿时间递归扩展残差流，增加模型维持的活跃计算状态数，是 LLM 架构层面（非单纯训练技巧）的值得关注变体。
原文：https://arxiv.org/abs/2611.21608v1

### 8. [arXiv] Turing Agent: Agentic Formal Verification for Mathematical Research
**一句话点评**：面向研究级数学的形式化验证 agent harness，双尺度架构整合定理证明与 agent 编排，属于 Agent 框架在形式化推理上的系统性工程实践。
原文：https://arxiv.org/abs/2611.21299v1

### 9. [arXiv] Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers
**一句话点评**：复现并扩展前沿 LLM 直接写出小网络权重、读取原始权重的能力，属于 LLM 行为/能力边界的有趣实证，对理解模型内部表示有间接价值。
原文：https://arxiv.org/abs/2611.21449v1

### 10. [arXiv] Benchleaking Is Accelerating: Benchmark contamination has worsened sharply in the past month
**一句话点评**：记录基准污染从后训练蔓延到预训练基座模型的加速趋势，对评估方法学与 LLM 训练数据治理有警示意义。
原文：https://arxiv.org/abs/2611.21315v1

### 11. [arXiv] Language-model agents' beliefs can be manipulated via truthful evidence in open channel
**一句话点评**：提出 Generative Montage，用真实片段编排误导性叙事使 agent 产生“叙事过拟合”，属于 LLM/Agent 行为与多智能体信息传播的实证研究。
原文：https://arxiv.org/abs/2611.21235v1

### 12. [arXiv] SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents
**一句话点评**：首个结合 agent 自主设计实验、故意有缺陷的模拟器与校准区间评分的科学判断基准，对自主实验 agent 评估有方法学贡献。
原文：https://arxiv.org/abs/2611.21541v1

### 13. [arXiv] Heteroscedastic Gaussian Process Q-learning for Sample Efficient Experimentation
**一句话点评**：用 GP 直接学 Q 函数并证明其后验给出 Q-learning 学习率（Kalman 增益等价），面向自驱动实验室的少样本实验优化，与实验设计/主动学习相关。
原文：https://arxiv.org/abs/2611.21249v1

### 14. [arXiv] How VLMs Plan What's Next
**一句话点评**：刻画 VLM 描述图像时的“先看哪里”规划机制（binding heads、进度游标），属于模型机制可解释性研究，对多模态表示学习有参考价值。
原文：https://arxiv.org/abs/2611.21600v1

### 15. [arXiv] Representational Change Under Self-Consuming Training: A Sparse Autoencoder Analysis
**一句话点评**：用 SAE 分析自消耗训练多代后内部表示漂移及 SAE 可靠性，属于 LLM 训练动态与表示分析，对理解模型演化有间接意义。
原文：https://arxiv.org/abs/2611.21348v1
