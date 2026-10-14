# P068 PageRank单轮概率流

在有向图中，一轮PageRank由旧概率p同时计算新概率：q[v]=(1-alpha)/n+alpha*(Σ_{u→v}p[u]/outdegree[u]+dangling_mass/n)。无出边点的概率均匀分给全部点。不得边计算边覆盖旧p。

## 输入与约束

首行 n m alpha；随后m行 u v；最后一行n个初始概率p。1≤n≤200，0≤m≤2000，0≤alpha<1；无重复有向边，允许自环；p≥0且总和为1（输入舍入误差≤1e-6）。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行n个新概率，按顶点顺序。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
2 1 0.8
0 1
0.6 0.4
```
输出：
```text
0.26 0.74
```

alpha=0.8，旧p=(0.6,0.4)，只有0→1。传送基础每点0.1；悬挂点1贡献0.8×0.4/2=0.16；0再把0.48传给1，因此新p=(0.26,0.74)。

## 分级提示

<details><summary>提示 1</summary>

先算没有出边的概率总质量。

</details>

<details><summary>提示 2</summary>

把传送项和悬挂均分项加入每个新概率。

</details>

<details><summary>提示 3</summary>

q=[(1-alpha)/n+alpha*dangling/n]*n；每条u→v再给q[v]加alpha*p[u]/outdegree[u]。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P068/exercise.py
.\.venv\Scripts\python.exe check.py P068
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P068/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P068.md) · [下一题](../P069/README.md)
