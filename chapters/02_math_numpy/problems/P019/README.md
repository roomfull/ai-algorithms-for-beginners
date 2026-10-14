# P019 矩阵乘法

本题为原创训练题。先修：先完成 P018；本题新概念见下方‘开始前先读’。

## 任务

手写三层循环计算矩阵乘法 A×B。A 为 r×k，B 为 k×c，输出 r×c 的乘积。允许 NumPy 存储数据，但不能直接用 @、dot 或 matmul 替代求和循环。

## 开始前先读

矩阵是按行列排列的数表。二维 NumPy 数组用 `a[i,j]` 取第i行第j列，位置从0开始。乘积 C 的形状是(r,c)，`np.zeros((r,c), dtype=float)` 创建全0数组。Cᵢⱼ=ΣₜAᵢₜBₜⱼ：选A的一行、B的一列，沿共同长度k做点积。`print(*row)` 中星号将一行数拆成多个参数，print默认用空格分隔；这只用于输出。

## 输入输出与约束

第一行三个整数 r k c；后 r 行是 A，每行 k 个数；再后 k 行是 B，每行 c 个数。输出 r 行，每行 c 个数，空格分隔。

1 ≤ r,k,c ≤ 30，元素为绝对值≤100的实数。维度总是匹配。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `float`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
2 3 2
1 2 3
4 5 6
7 8
9 10
11 12
```

输出：

```text
58 64
139 154
```

手算：A第一行(1,2,3)，B第一列(7,9,11)：C₀₀=1×7+2×9+3×11=58。B第二列(8,10,12)给64。第二行得到4×7+5×9+6×11=139，以及4×8+5×10+6×12=154。

## 三级提示

<details><summary>提示1</summary>

先写出输出形状(r,c)，共同维度k会被求和消掉。

</details>

<details><summary>提示2</summary>

外两层选择输出位置i,j，第三层t从0到k-1累加 a[i,t]*b[t,j]。

</details>

<details><summary>提示3</summary>

每个i,j先 total=0.0；内部t循环完才把 total 存入 result[i,j]，最后按行 print(*row)。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/02_math_numpy/problems/P019/exercise.py
.\.venv\Scripts\python.exe check.py P019
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P019.md)。[下一题 P020](../P020/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)。
