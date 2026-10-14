# P015 求和与均值双实现

本题为原创训练题。先修：先完成 P014；本题新概念见下方‘开始前先读’。

## 任务

对同一组数，先用普通 Python 循环计算总和及均值，再用 NumPy 数组计算同样两个量，输出两行结果用于对照。

## 开始前先读

`import numpy as np` 导入 NumPy 并用简称 np。`np.array(values, dtype=float)` 把列表转成所有元素同为浮点数的数组。数组提供 `.sum()` 求和、`.mean()` 求平均；小括号表示调用计算。`len(values)` 是元素数。均值是总和除以个数；它能概括中心位置，但不表示数据一定接近中心。

## 输入输出与约束

输入一行实数。输出两行，每行两个数：总和、均值。第一行来自普通循环，第二行来自 NumPy。

1–1000 个有限实数，绝对值不超过10000。均值分母为元素个数，不是元素总和。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `float`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
1 2 3 4
```

输出：

```text
10 2.5
10 2.5
```

手算：输入1 2 3 4，总和1+2+3+4=10，共4个数，所以均值10/4=2.5。普通循环与NumPy应各输出一行10 2.5。输入只有5时，和为5、均值也为5。

## 三级提示

<details><summary>提示1</summary>

先保存数字列表，普通循环累加时仍使用0作为起点。

</details>

<details><summary>提示2</summary>

第一行的第二个数是 total/len(values)，不是除以最后一个值。

</details>

<details><summary>提示3</summary>

将列表转换为 NumPy 数组；第二行输出 array.sum() 和 array.mean()。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/02_math_numpy/problems/P015/exercise.py
.\.venv\Scripts\python.exe check.py P015
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P015.md)。[下一题 P016](../P016/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://numpy.org/doc/stable/user/absolute_beginners.html#basic-array-operations)。
