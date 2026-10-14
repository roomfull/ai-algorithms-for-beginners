# P065 所有连通分量二分图判断

二分图可以把所有点分成两组，让每条边的两端处于不同组。用BFS双色标记检查整个无向简单图；每个孤立点也能合法染色。

## 输入与约束

首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；无自环、无重边。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行一个整数：整个图可二分输出1，否则0。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
4 4
0 1
1 2
2 3
3 0
```
输出：
```text
1
```

四边形交替染色0,1,0,1，回边3—0也连接异色点，因此输出1。

## 分级提示

<details><summary>提示 1</summary>

每条边要求两端颜色不同。

</details>

<details><summary>提示 2</summary>

从每个未染色点启动一次搜索。

</details>

<details><summary>提示 3</summary>

color初始-1；根设0，邻居设1-color[u]；若已染色且相同就失败。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P065/exercise.py
.\.venv\Scripts\python.exe check.py P065
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P065/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P065.md) · [下一题](../P066/README.md)
