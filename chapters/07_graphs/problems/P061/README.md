# P061 BFS最短层次

在无向简单图中，从起点s开始用队列执行广度优先搜索。每条边的代价都是1，输出最少经过几条边到每个点；不可达为-1。

## 输入与约束

首行 n m s；随后m行 u v。1≤n≤1000，0≤m≤5000，0≤s<n；无自环、无重边。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行n个距离，按顶点编号排列。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
5 4 0
0 1
0 2
1 3
2 3
```
输出：
```text
0 1 1 2 -1
```

起点0距离0；1和2一条边可达，距离1；3经过0→1→3距离2；4不可达为-1。

## 分级提示

<details><summary>提示 1</summary>

BFS需要先进先出的队列。

</details>

<details><summary>提示 2</summary>

首次发现邻居时就标记距离，避免重复入队。

</details>

<details><summary>提示 3</summary>

dist[s]=0；弹出u，若dist[v]==-1，则赋dist[v]=dist[u]+1并入队。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P061/exercise.py
.\.venv\Scripts\python.exe check.py P061
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P061/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P061.md) · [下一题](../P062/README.md)
