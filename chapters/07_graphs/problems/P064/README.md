# P064 无向简单图三角形计数

三角形是三个不同顶点，两两之间都有边。每组三点只统计一次；同一三角形的六种排列不重复计数。

## 输入与约束

首行 n m；随后m行 u v。1≤n≤120，0≤m≤n(n-1)/2；无自环、无重边。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行一个整数：三角形数。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
4 4
0 1
1 2
2 0
2 3
```
输出：
```text
1
```

三点0,1,2的三条边齐全，构成1个三角形；额外边2—3不能构成另一组三角形。

## 分级提示

<details><summary>提示 1</summary>

只枚举a<b<c。

</details>

<details><summary>提示 2</summary>

用邻接集合快速判断一条边是否存在。

</details>

<details><summary>提示 3</summary>

若b在adj[a]、c在adj[a]且c在adj[b]，计数加一。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P064/exercise.py
.\.venv\Scripts\python.exe check.py P064
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P064/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P064.md) · [下一题](../P065/README.md)
