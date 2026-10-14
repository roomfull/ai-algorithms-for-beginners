# P017 欧氏距离

本题为原创训练题。先修：先完成 P016；本题新概念见下方‘开始前先读’。

## 任务

计算两个同维向量之间的欧氏距离：对应坐标相减、平方求和，再开平方。

## 开始前先读

向量可以先理解为一排按位置对应的数。二维点(0,0)到(3,4)的距离来自勾股定理；n维时同样计算 sqrt(Σ(aᵢ-bᵢ)²)。`np.sqrt(value)` 求非负平方根。数组减法要求坐标按同一顺序对应，不能先各自排序；求和后的结果是单个数。

## 输入输出与约束

输入两行，各是相同个数的实数坐标。输出一行非负距离。

向量维数1–1000，坐标绝对值≤10000；两行长度相等。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `float`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
0 0
3 4
```

输出：

```text
5
```

手算：a=(0,0)、b=(3,4)，差为(-3,-4)，平方为(9,16)，和为25，平方根为5。a=(0,0,0)、b=(1,2,2)时平方和为1+4+4=9，距离3。

## 三级提示

<details><summary>提示1</summary>

先逐坐标做差，距离与各自坐标总和之差不同。

</details>

<details><summary>提示2</summary>

用差数组 **2 后 sum，再对结果开平方。

</details>

<details><summary>提示3</summary>

difference=a-b；输出 np.sqrt((difference**2).sum())，保持括号包住平方与求和。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/02_math_numpy/problems/P017/exercise.py
.\.venv\Scripts\python.exe check.py P017
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P017.md)。[下一题 P018](../P018/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)。
