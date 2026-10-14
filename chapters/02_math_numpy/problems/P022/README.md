# P022 axis 行列聚合

本题为原创训练题。先修：先完成 P021；本题新概念见下方‘开始前先读’。

## 任务

对矩阵分别求行和与列和，验收你对 axis 的理解。第一行输出每一行的和，第二行输出每一列的和。

## 开始前先读

二维形状(r,c)的axis=0对应行位置，axis=1对应列位置。沿某个axis求和，消掉的就是那个维度：sum(axis=0)把多行合并，留下c个列和；sum(axis=1)把每行的列合并，留下r个行和。不要只背‘axis0竖着’，请从输出剩下哪个维度推导。

## 输入输出与约束

第一行 r c；随后 r 行，每行c个实数。输出恰好两行：r个行和、c个列和。

1 ≤ r,c ≤ 100，元素绝对值≤10000。单行、单列、全零均合法。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `float`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
2 3
1 2 3
4 5 6
```

输出：

```text
6 15
5 7 9
```

手算：A=[[1,2,3],[4,5,6]]。行和：1+2+3=6，4+5+6=15，长度2。列和：1+4=5、2+5=7、3+6=9，长度3。先输出6 15，再输出5 7 9。

## 三级提示

<details><summary>提示1</summary>

先根据题目推断输出长度：第一行r个，第二行c个。

</details>

<details><summary>提示2</summary>

行和要合并列维度，所以axis=1；列和合并行维度，所以axis=0。

</details>

<details><summary>提示3</summary>

分别调用 a.sum(axis=1)、a.sum(axis=0)，用print(*结果)避免数组方括号。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/02_math_numpy/problems/P022/exercise.py
.\.venv\Scripts\python.exe check.py P022
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P022.md)。[下一章：预处理与特征工程](../../../03_preprocessing/README.md)（完成后再前往）；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://numpy.org/doc/stable/user/absolute_beginners.html#basic-array-operations)。
