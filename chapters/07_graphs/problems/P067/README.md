# P067 Prim最小生成树

从顶点0开始，维护已加入的点集；每次选跨越该点集与外部的最便宜边。用最小堆实现Prim，与Kruskal应得到相同最小总权重。

## 输入与约束

首行 n m；随后m行 u v weight。1≤n≤200，0≤m≤2000；无自环、无重边，weight为[-10000,10000]整数。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

连通时一行最小总权重整数；不连通时一行 DISCONNECTED。单点权重0。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
3 3
0 1 4
1 2 2
0 2 5
```
输出：
```text
6
```

从0选0—1的权重4；可选边中1—2权重2比0—2权重5便宜，再选它；总权重6。

## 分级提示

<details><summary>提示 1</summary>

堆里保存可以把新点加入树的候选边。

</details>

<details><summary>提示 2</summary>

同一个点可能有多个候选，出堆时跳过已经加入的点。

</details>

<details><summary>提示 3</summary>

堆初始(0,0)，弹出(w,u)；若未访问则加入、加权并推入邻边；最后检查访问点数为n。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P067/exercise.py
.\.venv\Scripts\python.exe check.py P067
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P067/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P067.md) · [下一题](../P068/README.md)
