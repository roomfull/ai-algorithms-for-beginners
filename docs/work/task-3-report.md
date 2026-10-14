# Task 3 交付与自审记录

日期：2026-10-14。按已批准的 `docs/implementation-plan.md` 与 `docs/work/task-3.md` 恢复任务；没有修改共享检查器或其他工作包，没有 Git commit。

## 交付

- `chapters/03_preprocessing/README.md`：均值、中位数、缺失填补、稳定去重、Min-Max、总体标准差、训练泄漏、类别不平衡、复制过采样、SMOTE线段与少数类KNN。
- `chapters/04_features/README.md`：TF/df/IDF、平滑与L2零向量、等宽与按秩分组、重复值规则、2×2卡方表、完整合并一轮及后续重算、MAD。
- P023–P038各有 `README.md`、未完成的 `exercise.py`、5个独立 `cases.json` 案例；共16题、80案例。
- `solutions/P023.py`–`P038.py` 是可单文件运行的答案，均只依赖标准库；同名 `.md` 给出思路、关键步骤、样例手算、实现复杂度、易错点与一手来源。
- 保留并使用 `tests/test_preprocessing_features.py`：6个测试方法，含全部80案例及5项独立数学性质；没有通过运行答案来生成期望。
- `tools/build_preprocessing_features.py` 保留原先的手算案例，扩展了分批材料生成。每批2–4题后保存 `task-3-checkpoint.md`；最终一次刷新全部16题的脚手架与解释性注释。

## RED与GREEN证据

先检查已保存的案例和性质测试，确认缺少P023–P038答案，随后实际执行：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_preprocessing_features.py
```

RED输出：`Ran 6 tests`，`FAILED (failures=85)`。80个案例子测试及5项性质均因缺少对应参考解失败，断言为 `solution.is_file()`；原始输出保存于 [task-3-red.txt](task-3-red.txt)。恢复前的RED没有持久证据，因此没有将它算作验收证据。

最终验证命令与结果：

| 命令（仓库根目录，前缀均为 `.\.venv\Scripts\python.exe`） | 结果 | 退出码 |
|---|---|---:|
| `check.py --chapter 03 --solution` | 通过40/40案例，共8题 | 0 |
| `check.py --chapter 04 --solution` | 通过40/40案例，共8题 | 0 |
| `-m unittest discover -s tests -p test_preprocessing_features.py -v` | Ran 6 tests，OK | 0 |
| `check.py P023` | 全部5例标记为“未完成”，NotImplementedError | 1，预期 |

完整命令、stdout/stderr与退出码保存在 [task-3-validation.txt](task-3-validation.txt)。实际运行Python版本3.11.15。默认检查仍指向练习，未用答案覆盖练习。

## 数学与规则审计

| 题目 | 核对项与证据 |
|---|---|
| P023 | 忽略NA有效计数；全缺失列回退0；无缺失、单元素、负值覆盖 |
| P024 | 保留第一次；元组与集合判重、列表保持顺序；不同排列行不混淆 |
| P025 | 逐列min/max；常量列0；正负与小数端点手算案例 |
| P026 | 总体分母n；独立测试输出均值≈0、总体方差≈1，常量列全0 |
| P027 | 仅训练行拟合；下标排列输出；验证100在训练[0,10]范围外变为10，无裁剪 |
| P028 | 两类目标不小于原数；保留原顺序；先补0再补1，循环原列表 |
| P029 | 同λ线段插值；λ=0、1与相同坐标端点覆盖 |
| P030 | 少数类至少2、k至少1；排除自身与多数类；并列原始索引；显式q/λ与循环基点；独立测试多数类更近仍不使用，λ端点正确 |
| P031 | 原始词频；词表字典序；空文档0向量 |
| P032 | df按文档去重；未出现词与空文档；自然对数平滑公式 |
| P033 | TF×IDF后按行L2；norm可选；零向量不除0；独立手算权重和单位范数 |
| P034 | 整数输入精确算边界；内部边界右箱、max最后箱、常量0；k可大于n |
| P035 | 按(值,下标)排序，rank*k//n；同值可拆组；每组数量接近但不伪称总是相等，不与分位数区间策略混淆 |
| P036 | Pearson无Yates修正；行和×列和/总数求期望；0项约定；独立比例表卡方0 |
| P037 | 每轮仅比较相邻、重新计算、合并计数与边界；Fraction精确比较、并列最左；明确教学变体 |
| P038 | MAD为中位绝对偏差；偶数median取平均；MAD=0全0；独立平移不变性质 |

结构审计实际遍历16题，检查文件齐全、80个案例、所有脚手架保留NotImplementedError且不导入答案、全部Python AST可解析、每题三级不同提示、首样例与cases一致、参考解中文解释注释、本地Markdown链接存在。审计通过。发现并修复了P037手算中“区间后紧接括号”被Markdown误识别成链接的问题。

复杂度按实际实现声明：P030逐基点距离表排序而非虚报线性KNN；P037逐轮全邻对扫描与列表删除为O(b²)，Fraction是标准库、有界计数算术；P035、P038排序为O(n log n)。源代码未使用机器学习库。

## 定义与实现证据来源

- [scikit-learn预处理](https://scikit-learn.org/stable/modules/preprocessing.html)：标准化、Min-Max、离散化的定义核对。
- [scikit-learn缺失填补](https://scikit-learn.org/stable/modules/impute.html)：填补概念；本题全缺失列回退独立规定。
- [scikit-learn数据泄漏](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)：先划分再拟合训练统计量。
- [Python集合](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)：集合判重与可散列元素。
- [imbalanced-learn过采样](https://imbalanced-learn.org/stable/over_sampling.html#sample-generation)：少数类邻点插值；[GitHub SMOTE源码](https://github.com/scikit-learn-contrib/imbalanced-learn/blob/master/imblearn/over_sampling/_smote/base.py)的差向量与`基点+steps*diffs`用于核对实现思路，本题生成顺序由题面规定。
- [scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html#tf-idf-term-weighting)：原始TF、平滑IDF及L2定义。
- [SciPy卡方统计量](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.chi2_contingency.html)：期望、Pearson及Yates修正区别；本题没有调用SciPy。
- [SciPy MAD定义](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_abs_deviation.html)：MAD为偏离中位数的绝对偏差中位数；本题不调用SciPy或使用异常阈值。

以上均实际浏览核对，参考代码独立编写。P035按秩拆重复值、P037合并策略、常量/零分母回退均是题面明确的教学约定，没有声称为所有库的默认行为。

任务包已完成自审，待父任务安排独立审查与全库汇总。
