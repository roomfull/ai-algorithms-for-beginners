# Python 零基础到 AI 科目一练习

这套中文课程从保存、运行第一行 Python 开始，逐步练普通 Python、必要数学与 NumPy、公共 AI 基础和 AI 系统优化。共 **80 道基础练习 + 4 套双题模拟卷 = 88 题、461 个自动检查案例**。题目为原创教学练习，不声称是真题或高频题，也不要求按日历推进。

**第一次学习：[零基础起步](docs/START_HERE.md) → [第01章教程](chapters/01_python/README.md) → [P001 第一行固定输出](chapters/01_python/problems/P001/README.md)。** 如果还分不清终端、编辑器与Python，先从起步教程的第1节开始。

在项目根目录的 PowerShell 执行（已有环境可跳过安装）：

```powershell
.\setup.ps1
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import numpy; print(numpy.__version__)"
.\.venv\Scripts\python.exe check.py --list
.\.venv\Scripts\python.exe check.py P001
```

使用 Python 3.11 与 NumPy 2.2.6，本机验证版本为 Python 3.11.15。`.venv` 为独立环境，以上命令无需激活。首次安装要联网；课程与检查案例安装后均离线运行。安装被脚本策略阻止、换机、离线安装等问题见[起步教程](docs/START_HERE.md)。

第一次检查 P001 会显示“未完成”：这是正常起点。打开 [P001练习](chapters/01_python/problems/P001/exercise.py)，按题面填写代码并替换 `raise NotImplementedError(...)`，保存后再检查。检查器不会自动填答案。

学习时按以下顺序前进。每一章入口都有概念讲解、逐题链接和自测，先理解后动手；“通过”之后，还应能解释算法和边界。

| 章 | 内容与教程入口 | 题号 / 数量 | 先修 | 掌握标准 |
| --- | --- | --- | --- | --- |
| 01 | [Python与输入输出](chapters/01_python/README.md) | P001–P014 / 14 | 无 | 独立读输入、写循环/条件、正确return与print，处理多组数据 |
| 02 | [数学与NumPy](chapters/02_math_numpy/README.md) | P015–P022 / 8 | 01 | 手算均值/总体方差/距离/点积，写出矩阵与广播形状 |
| 03 | [预处理](chapters/03_preprocessing/README.md) | P023–P030 / 8 | 01–02 | 处理缺失/去重/归一化，解释训练统计量与数据泄漏，区分复制与插值 |
| 04 | [特征工程](chapters/04_features/README.md) | P031–P038 / 8 | 01–03 | 手算TF-IDF、分箱、卡方与稳健统计，明确分母与边界 |
| 05 | [传统机器学习](chapters/05_machine_learning/README.md) | P039–P050 / 12 | 01–04 | KNN平票、K-means空簇、逻辑回归梯度和决策树分裂，能追踪完整更新 |
| 06 | [神经网络](chapters/06_neural_networks/README.md) | P051–P058 / 8 | 01–05 | 逐步计算前向、反向、卷积/转置卷积与GAN小模型更新，独立完成P058 |
| 07 | [图算法](chapters/07_graphs/README.md) | P059–P070 / 12 | 01–02；建议先完成06 | 建模有向/无向图，解释BFS、并查集、最短路、MST和悬挂PageRank |
| 08 | [模型压缩](chapters/08_compression/README.md) | P071–P076 / 6 | 01–02、06 | 区分阈值/比例剪枝，精确半格量化，报告重构误差及局限 |
| 09 | [分布式数值模拟](chapters/09_distributed/README.md) | P077–P080 / 4 | 01–02、05–06 | 解释分片、按样本加权、微批次累积与一次同步SGD |

可在根目录执行 `.\.venv\Scripts\python.exe check.py --chapter 01` 按章检查。学习过程中用 [进度表](PROGRESS.md) 手动标记，不把题解通过当作自己已掌握；错题用 [具体例子与模板](docs/MISTAKES.md) 记录。

答题流程是：读输入与输出 → 手算首样例 → 写清数组形状/状态变化 → 编辑该题 `exercise.py` → 保存 → 检查 → 对照失败案例修复 → 隔一次学习后不看答案重做。卡住时逐级展开题面提示，避免一次跳到完整解。

| 检查结果 | 如何处理 |
| --- | --- |
| 未完成 | 找到并替换练习中的NotImplementedError |
| 答案错误 | 看案例输入、期望、实际输出；先核对行数与每行元素，再核对边界/数值 |
| 语法/运行错误 | 从报错行和异常末行定位；检查括号、缩进、转换、下标与除零 |
| 缺少模块 | 确认使用本项目`.venv`，依起步教程安装requirements |
| 超时 | 每案例默认5秒；检查循环终止和算法复杂度 |
| 环境问题 | 确认文件、路径和解释器；退出码2表示参数/元数据/环境问题 |

文本允许换行制式与行尾空白差异，但不允许多出提示语或调试行。整数严格要求十进制整数，不能输出`1.0`；浮点行允许绝对/相对误差1e-6，拒绝NaN/inf；混合题按每行指定模式检查。输出形状同样必须正确。退出码0=全通过，1=学习代码未通过，2=参数/环境问题。[完整说明](docs/START_HERE.md#6-看懂检查结果)。

完成九章后进入模拟卷，每卷两道组合题，需要自己完成输入输出。可用计时器记录实际用时，再复盘；本课程不规定正式考试时长或评分。

| 模拟卷 | 组合题 |
| --- | --- |
| [M01](exams/mock01/README.md) | 训练集Z-score后KNN / 网络布线MST |
| [M02](exams/mock02/README.md) | TF-IDF余弦排名 / 含悬挂网页的PageRank |
| [M03](exams/mock03/README.md) | 固定初值聚类、SSE与查询 / 逐行量化与MSE |
| [M04](exams/mock04/README.md) | 卷积+ReLU+平均池化 / 多worker不同微批的加权更新 |

```powershell
.\.venv\Scripts\python.exe check.py --chapter M01
```

教学环境默认CPU、合法标准输入、只用标准库与NumPy、无外部数据、无GPU、无网络服务；显式输入初值和系数消除随机性。小规模Fraction题用于精确边界教学，真实系统通常使用浮点张量。本课程没有验证剪枝/量化/分布式方法的实际加速比。你的正式考试环境、可用库、输入规则、时限与题型仍须依实际考试说明核对。

<details><summary>作答后再打开：独立题解、参考解与维护核验</summary>

题解分别保存于`solutions/题号.md`，参考程序于`solutions/题号.py`，每份可独立运行。入口示例：[P001题解](solutions/P001.md)、[M01A题解](solutions/M01A.md)。普通检查默认运行练习，`--solution`才运行参考解。

```powershell
.\.venv\Scripts\python.exe check.py P001 --solution
.\.venv\Scripts\python.exe check.py --all --solution
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

[来源与教学约定](docs/REFERENCES.md) · [维护与真实验收统计](docs/MAINTAINING.md)。不要用答案覆盖自己的练习。

</details>
