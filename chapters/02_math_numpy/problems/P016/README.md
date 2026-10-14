# P016 总体方差

本题为原创训练题。先修：先完成 P015；本题新概念见下方‘开始前先读’。

## 任务

计算输入数据的总体方差：先求均值，再把每个数与均值之差平方，最后对这些平方求平均。明确使用分母 n（ddof=0）。

## 开始前先读

方差衡量数据偏离均值的程度。公式为 var=(Σ(xᵢ−μ)²)/n；Σ表示把所有对应项相加，μ是均值，n是个数。`array - mean` 对每个元素减同一个数；`** 2` 对每个差平方；新数组的 mean() 取平均。NumPy 的 `np.var(array, ddof=0)` 与这个定义一致，ddof=1 会改变分母，本题不用。

## 输入输出与约束

输入一行实数。输出一行总体方差。

1–1000个有限实数，绝对值≤10000。把输入当作整个总体，不计算样本方差。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `float`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
1 2 3
```

输出：

```text
0.6666666666666666
```

手算：数据1、2、3均值是2，偏差为-1、0、1，平方是1、0、1，相加为2，再除以3得到2/3。不能除以2，那是另一种定义。单个7的偏差为0，总体方差为0。

## 三级提示

<details><summary>提示1</summary>

先求中心，再求偏差；直接对原始数据平方取平均不是方差。

</details>

<details><summary>提示2</summary>

差值数组写 array-array.mean()，平方后再求 mean。

</details>

<details><summary>提示3</summary>

三步分别保存 mean、difference、squared，然后输出 squared.mean()，分母自然是 n。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/02_math_numpy/problems/P016/exercise.py
.\.venv\Scripts\python.exe check.py P016
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P016.md)。[下一题 P017](../P017/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://numpy.org/doc/stable/reference/generated/numpy.var.html)。
