# P060 有向图入度与出度

有向边u→v只给u增加出度，给v增加入度；统计每个顶点的两个计数。自环给同一点同时增加入度和出度。

## 输入与约束

首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；允许自环，不允许重复同向边；两个反向边可以共存。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

共n行，第i行输出 indegree[i] outdegree[i]，无需输出顶点编号。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
3 3
0 1
0 2
2 1
```
输出：
```text
0 2
2 0
1 1
```

0→1与0→2让0出度为2；2→1让1入度为2、2入出度各1。

## 分级提示

<details><summary>提示 1</summary>

区分“指向我”与“从我出发”。

</details>

<details><summary>提示 2</summary>

准备长度n的两个计数数组。

</details>

<details><summary>提示 3</summary>

每次只执行 outdegree[u]+=1 与 indegree[v]+=1。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P060/exercise.py
.\.venv\Scripts\python.exe check.py P060
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P060/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P060.md) · [下一题](../P061/README.md)
