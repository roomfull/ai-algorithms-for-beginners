# 来源、采用约定与教学范围

来源用于核对定义、Python/NumPy行为和常见实现思路，课程题面、手算数据与单文件参考解独立编写。每题另有对应来源。联网只用于延伸阅读，作答和检查不需要访问链接；课程仅安装NumPy，不安装下面提到的scikit-learn、SciPy、NetworkX、imbalanced-learn、PyTorch。

核对日期：2026-10-14。官方stable页面和GitHub main可能随后变化；课程接口以Python 3.11.15、NumPy 2.2.6的本地验收为准。正式考试版本、范围、允许库和时限不能从本课程或这些实现推断。

| 专题 | 一手定义/实现来源 | 本课程采用的约定与区别 |
| --- | --- | --- |
| Python语法、输入输出、排序（P001–P014） | [Python3.11教程](https://docs.python.org/3.11/tutorial/)、[排序指南](https://docs.python.org/3.11/howto/sorting.html)、[CPython subprocess](https://github.com/python/cpython/blob/3.11/Lib/subprocess.py) | 标准输入输出单文件练习，稳定排序与题面平票规则明确；检查器另进程运行、UTF-8、超时，练习不输出提示语 |
| 数学/数组（P015–P022） | [NumPy2.2文档](https://numpy.org/doc/2.2/)、[广播](https://numpy.org/doc/2.2/user/basics.broadcasting.html)、[官方教程仓库](https://github.com/numpy/numpy-tutorials) | 总体方差ddof=0；先手算/普通循环再数组；shape、axis、广播方向按题面固定；不用notebook |
| 缺失/缩放/泄漏（P023–P027、M01A） | [缺失填补](https://scikit-learn.org/stable/modules/impute.html)、[StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)、[泄漏说明](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) | 统计量仅训练集拟合；全缺失列和常量列由题面定规则。M01A恒定训练列对查询也置0，区别于StandardScaler常量列scale=1后仍保留查询偏差；距离排序等价忽略常量共同距离项 |
| 过采样/插值（P028–P030） | [imbalanced-learn过采样](https://imbalanced-learn.org/stable/over_sampling.html#sample-generation)、[SMOTE GitHub实现](https://github.com/scikit-learn-contrib/imbalanced-learn/blob/master/imblearn/over_sampling/_smote/base.py) | 显式目标数、基点顺序和插值系数；只在原样本找邻居，平票按原下标；复制不新增独立信息，重采样不等于可靠提升效果 |
| TF-IDF（P031–P033、M02A） | [官方定义](https://scikit-learn.org/stable/modules/feature_extraction.html#tf-idf-term-weighting)、[官方GitHub文档](https://github.com/scikit-learn/scikit-learn/blob/main/doc/modules/feature_extraction.rst)、[实现](https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/feature_extraction/text.py) | 原始词频次数，平滑idf=1+ln((n+1)/(df+1))；不分词、不取sublinear tf；M02A查询不参与df，零范数/无共同词得0，排名键为round(score,12)，原分数输出 |
| 分箱（P034–P035） | [官方离散化](https://scikit-learn.org/stable/modules/preprocessing.html#discretization) | 等宽内部边界归右箱、max归最后箱；等频题按(值,原下标)秩分组，同值可跨组，区别于按数值边界变换的quantile分箱 |
| 卡方/稳健统计（P036–P038） | [SciPy卡方定义](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.chi2_contingency.html)、[MAD定义](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_abs_deviation.html) | 只算未作Yates修正的统计量，不输出p值；期望0项和总数0处理依题面；MAD用原始尺度，不乘正态校准系数，MAD=0特征全0 |
| KNN/K-means/逻辑回归（P039–P047、M01A、M03A） | [numpy-ml实现](https://github.com/ddbourgin/numpy-ml)、[KNN定义](https://scikit-learn.org/stable/modules/neighbors.html)、[KMeans定义](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) | KNN按距离后下标，票数并列取最小标签；显式中心、固定轮数、空簇保留；M03A最后重新分配而不再更新中心；小模型梯度直接实现，不调用库fit |
| CART决策树（P048–P050） | [官方树定义](https://scikit-learn.org/stable/modules/tree.html) | 连续特征候选中点、Gini、明确增益与平票停止规则；贪心不保证解决所有样本结构；深度和阈值依各题，不套库默认值 |
| 全连接/稳定概率/损失/梯度（P051–P054） | [numpy-ml层与损失实现](https://github.com/ddbourgin/numpy-ml/tree/master/numpy_ml/neural_nets) | P051全连接与ReLU，P052减最大值的稳定softmax，P053二分类BCE与多分类交叉熵，P054单层sigmoid网络梯度更新；明确参数与输入，按题面手算，不调用自动微分框架 |
| CNN/池化/转置卷积（P055–P057、M04A） | [Conv2d](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)、[ConvTranspose2d](https://docs.pytorch.org/docs/stable/generated/torch.nn.ConvTranspose2d.html)、[最大池化](https://docs.pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html)、[平均池化](https://docs.pytorch.org/docs/stable/generated/torch.nn.AvgPool2d.html) | P055互相关不翻核，P056卷积+ReLU+最大池化，P057转置卷积为伴随操作而非逆；M04A使用平均池化，无padding、卷积步长1，先ReLU再池化，池化步长p、完整窗口、丢弃余边 |
| GAN（P058） | [GAN原论文](https://arxiv.org/abs/1406.2661) | 标量GAN损失与交替更新：先D后G、非饱和生成器目标，参数使用时点以题面为准，不称作完整图像生成模型 |
| 图/最短路/MST（P059–P067、P070、M01B） | [NetworkX图算法源码](https://github.com/networkx/networkx/tree/main/networkx/algorithms)、[Kruskal源码](https://github.com/networkx/networkx/blob/main/networkx/algorithms/tree/mst.py) | 图方向、重复边、自环及权值依题面；M01B非负成本、允许平行线，断开−1、单点0；最短路不可达的输出标记依具体题 |
| PageRank（P068–P069、M02B） | [NetworkX官方实现](https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html) | 均匀初值，悬挂质量均分，同步更新；P069/M02B精确Fraction、L1≤tol，区别于NetworkX的n*tol；至少1轮，未收敛仍返回末轮概率；M02B精确概率排名平票取下标 |
| 剪枝（P071–P073） | [PyTorch官方教程](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html) | 仅置零与掩码，不验证稀疏算子加速；比例floor从原字符串精确计算；平票按原下标，剪除位置数区别于最终零元素数 |
| 量化（P074–P076、M03B） | [PyTorch量化文档](https://docs.pytorch.org/docs/stable/quantization.html)、[observer GitHub实现](https://github.com/pytorch/pytorch/blob/main/torch/ao/quantization/observer.py) | 普通量化题采用半偶舍入，M03B明确采用半格远离0，两者不能混用；对称Q=2^(b−1)−1，不使用最负码；M03B逐行scale、零行scale1；仿射零点/截断依具体题；不保证硬件加速 |
| 分布式/微批（P077–P080、M04B） | [DDP设计说明](https://docs.pytorch.org/docs/stable/notes/ddp.html)、[官方教程](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)、[GitHub实现](https://github.com/pytorch/pytorch/blob/main/torch/nn/parallel/distributed.py) | 单机数值模拟，局部梯度为样本均值，乘样本数恢复和、统一除总样本数；所有梯度处于同一参数，只更新一次；无通信性能结论，真实DDP损失归约与不均等batch须另核对 |

所有浮点输出由检查器以绝对/相对1e-6比较，形状必须一致；整数标签严格比较。精确边界题从输入原字符串构造`Fraction`，不能先转换float再构造。用于教学的小规模约束与显式确定性规则可能不同于来源库默认设置，请先读具体题面。

[返回课程](../README.md) · [维护规范](MAINTAINING.md)
