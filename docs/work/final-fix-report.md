# 最终统一数值修复报告

2026-10-14，完成final-review.md列出的两项P2。范围为P025/P026/P027/P038/P042/P044及必要生成源、独立测试、03/04/05章相关教程。没有修改check.py、其他题材料、历史task-6报告或日志；没有Git操作。使用现有Python 3.11环境，未引入第三方依赖。

## 实际结果

- 88题，477/477案例通过；本轮增加16例，原461例保留。
- unittest discover：112个方法通过；原105方法增加7个。
- 六题实现先观察独立RED，再定向GREEN；原始证据见[RED](final-fix-red.log)、[GREEN](final-fix-green.log)。
- 28份可生成文件临时重建与实际字节一致，见[生成核对](final-fix-generation.log)。401个受保护文件哈希不变，见[范围核对](final-fix-scope.log)。基线哈希在新增回归测试后、实现修改前保存，测试文件本就属于授权修改范围。

## 数值修复与约束依据

P025/P027/P038从原始字符串创建Fraction，排序、最小最大值、中位数、减法及比值均精确计算，仅最终格式化转float。P025的大偏移中间值恢复0.5，P027验证值恢复0.5且仍不裁剪，P038等间距三点恢复-1、0、1。

P026精确求均值和总体方差v。v=0输出0；否则令δ=x-μ，精确算δ²/v，再取sqrt并按δ符号恢复正负。因为v是所有δ²的平均，0≤δ²/v≤n。先转成无量纲比值，避免将极小原始方差先转float发生下溢；大偏移三点恢复±sqrt(1.5)和0。

P025–P027/P038原先没有小数位上限，本轮明确普通十进制写法、无指数、最多12位小数，保留原绝对值≤10^6、n≤200和其他尺寸约束。全部六位小数审查输入仍合法。这个限制同时约束输入位成本及可输出的有限值：

- 令h=10^-12，P027非零训练范围至少h，分子绝对值≤2×10^6，输出绝对值≤2×10^18。
- P038非零MAD至少h/2（整数网格中位数至多产生半格），偏差≤2×10^6，特征绝对值≤4×10^18。
- P026非零δ至少h/n，使用保守上界v≤4×10^12，δ²/v至少1/(4×10^36×n²)≥6.25×10^-42，至多n≤200；在浮点正常可表示范围内。

P042/P044保持已有规则：先求精确最小平方距离m，再取首个distance≤m+Fraction("1e-12")的中心。严格等距与相差恰好1e-12都平票，超过阈值不平票，没有扩大判题误差或改成仅精确相等。P044均值中心、坐标变化、tol判停和最终重分配都保持Fraction，只打印中心时转float。坐标原有最多6位小数约束保持；tol新增普通十进制最多12位小数限制。中心每轮是原样本均值，其分母由输入网格和簇大小决定，不随迭代轮数无限增长。

题面、分级提示、未完成脚手架、题解和章节教程均同步；练习继续抛NotImplementedError。复杂度明确区分有理数运算次数与位成本：每个数B位，存储还需乘B，每步精确算术包含大整数运算及最大公约数约分，不能视为任意精度O(1)。

方案依据：[Python 3.11 Fraction文档](https://docs.python.org/3.11/library/fractions.html)区分字符串精确输入和float构造；[CPython fractions.py](https://github.com/python/cpython/blob/3.11/Lib/fractions.py)显示整数算术和gcd约分。另核对[scikit-learn K-means实现](https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/cluster/_kmeans.py)结束时重做分配以使标签对应最终中心的做法；本题容差、空簇和判停仍按自己的既有教学契约，不宣称与库全部默认行为一致。

## 独立预期与RED/GREEN

新增案例按题分布：P025 +2、P026 +3、P027 +2、P038 +2、P042 +3、P044 +4，共16。

预期直接来自等间距、训练范围、两次中位数和距离平方手算，不从参考答案生成。等间距三个数的方差为2h²/3，Z-score为±sqrt(1.5)、0；K-means大距离两项均为2×99.9²=19960.02；容差边界两项差分别10^-12、4×10^-12。另保留常量列、最小合法尺度、空簇和tol等号边界。

RED/GREEN用同一7个方法，在tests工作目录由仓库解释器执行`-m unittest -v`，方法名如下：

```text
test_preprocessing_features.PreprocessingFeatureTests.test_scaling_preserves_decimal_gaps_at_large_offset
test_preprocessing_features.PreprocessingFeatureTests.test_zscore_large_offset_and_small_scale
test_preprocessing_features.PreprocessingFeatureTests.test_mad_preserves_decimal_gaps
test_preprocessing_features.PreprocessingFeatureTests.test_small_scale_training_range_and_constant_columns
test_ml_neural.MLNeuralTests.test_kmeans_large_exact_distance_tie
test_ml_neural.MLNeuralTests.test_kmeans_exact_tolerance_boundary
test_ml_neural.MLNeuralTests.test_kmeans_exact_center_update_and_stopping_boundary
```

原始结果：RED `Ran 7 tests in 0.773s`，`FAILED (failures=6)`，退出码1；6个失败子场景分别覆盖六题。常量/小尺度/已有容差等对照场景不要求原实现失败。GREEN `Ran 7 tests in 1.236s`，`OK`，退出码0。

## 最终全库执行

所有跨章节实现及教材修改完成后，仅执行了一轮以下两个命令（不调整默认5秒超时、不调整误差）：

```powershell
.\.venv\Scripts\python.exe check.py --all --solution
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

实际全解输出末行：`通过 477/477 个案例，共 88 题`，退出码0，命令耗时30.081秒。实际单测：`Ran 112 tests in 25.190s`、`OK`，退出码0，命令耗时25.352秒。命令由Python subprocess启动，子进程PYTHONIOENCODING=utf-8，stdout/stderr直接合并写入二进制日志，没有过滤原始输出。见[全解原始日志](final-solutions.log)、[单测原始日志](final-unittest.log)、[执行元数据](final-fix-validation.json)。命令完成后仅补写验收统计和本报告，没有再次改实现或重跑全库。

旧[task-6报告](task-6-report.md)、[旧全解日志](task-6-solutions.log)、[旧单测日志](task-6-unittest.log)和[上一轮修复日志](task-6-repair-1.log)保留为历史证据，不与本轮477/112混用。

## 生成器一致性与有限性能检查

仅定向调用以下函数生成授权材料，没有全量覆盖其他题：

```python
import tools.build_preprocessing_features as pre
import tools.build_ml_neural as ml
pre.write_cases([25, 26, 27, 38])
pre.write_materials([25, 26, 27, 38], checkpoint=False)
ml.write_materials([42, 44])
```

一致性核验在docs/work内临时目录创建solutions目录，将两模块ROOT指向该目录，执行相同函数，把每个生成文件与仓库相对路径逐字节比较：28/28相同。预处理生成器生成4题各5份文件；机器学习生成器原设计只生成题面/案例/脚手架/题解，故生成2题各4份，P042/P044独立参考代码直接维护。生成器新增可选ID过滤；预处理可关闭旧任务检查点写入，避免改写历史记录。临时目录自动清理。

有限性能检查由`.\.venv\Scripts\python.exe -`运行subprocess与perf_counter：固定n=100,d=10,c=10,max_iter=100,tol=0，样本坐标为`((i*137+j*73)%199999999-99999999)/1000000`格式化6位小数，初始中心为`-99+i*0.01+j*0.000001`格式化6位小数。单次完整P044程序退出0，用时0.128904秒；同尺寸数据直接调用assign十次用时0.197215秒，101次分配线性估计1.991866秒。这是有限测量及估计，不是所有输入/机器的性能证明；未观察到需要缩小原100轮上限的依据。见[性能日志](final-fix-performance.log)。

残余限制：输出仍采用允许误差的float格式化，Fraction仅用于这些小规模教学题；普通十进制位数约束是明确的题目边界。有限测试不能证明所有输入正确，但本轮已覆盖全部审查复现、容差边界及独立性质，没有扩大到无关算法审查。下一步由原最终审查者对本轮修复做一次范围复核。
