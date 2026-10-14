# P020 shape 与 reshape

本题为原创训练题。先修：先完成 P019；本题新概念见下方‘开始前先读’。

## 任务

将一行数据按行优先顺序重排成 r×c 数组；先输出形状，再逐行输出新数组。重排只改变摆放方式，不改变数值或先后顺序。

## 开始前先读

`array.shape` 是形状属性，不加括号；二维数组得到(r,c)，一维数组得到(n,)，尾逗号表明只有一个维度。`array.reshape((r,c))` 按默认C顺序先填满一行再填下一行。形状中的尺寸相乘必须等于元素总数。reshape与转置含义不同，不会自动把数值进行排序。

## 输入输出与约束

第一行整数 r c；第二行恰好 r×c 个实数。第一行输出 r c，其后输出 r 行数组内容。

1 ≤ r,c ≤ 100；输入元素绝对值≤10000；保证元素数量匹配。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `float`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
2 3
1 2 3 4 5 6
```

输出：

```text
2 3
1 2 3
4 5 6
```

手算：1 2 3 4 5 6改为(2,3)：先填第一行1 2 3，再填第二行4 5 6。总数2×3=6不变；改成(3,2)会得到1 2、3 4、5 6，绝不是同一个输出。

## 三级提示

<details><summary>提示1</summary>

先核对 r*c 是否等于一行元素数。

</details>

<details><summary>提示2</summary>

把列表变成一维浮点数组，然后调用 reshape((r,c))。

</details>

<details><summary>提示3</summary>

用 print(*matrix.shape) 输出两个维度，再 for row in matrix 逐行 print(*row)。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/02_math_numpy/problems/P020/exercise.py
.\.venv\Scripts\python.exe check.py P020
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P020.md)。[下一题 P021](../P021/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://numpy.org/doc/stable/user/absolute_beginners.html#can-you-reshape-an-array)。
