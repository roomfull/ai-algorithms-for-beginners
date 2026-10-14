# P066 Kruskal最小生成树

无向加权图的生成树包含全部顶点，恰好n-1条边且无环。Kruskal按权重升序考虑边，用并查集跳过成环边，求最小总权重；若图不连通则不存在生成树。

## 输入与约束

首行 n m；随后m行 u v weight。1≤n≤200，0≤m≤2000；无自环、无重边，weight为[-10000,10000]整数。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

连通时一行最小总权重整数；不连通时一行 DISCONNECTED。单点的空生成树权重为0。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

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

先选权重2的1—2，再选权重4的0—1，已得到n-1=2条边，总权重6；权重5的边会成环。

## 分级提示

<details><summary>提示 1</summary>

最便宜边只有在不成环时才能选。

</details>

<details><summary>提示 2</summary>

并查集判断两端是否已经相连。

</details>

<details><summary>提示 3</summary>

边按(weight,u,v)排序；两端根不同则合并、total+=weight、used+=1；最后检查used==n-1。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P066/exercise.py
.\.venv\Scripts\python.exe check.py P066
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P066/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://github.com/TheAlgorithms/Python/blob/master/graphs/minimum_spanning_tree_kruskal.py)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P066.md) · [下一题](../P067/README.md)
