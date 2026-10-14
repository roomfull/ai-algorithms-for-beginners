# P070 图综合验收

对同一个无向简单图输出三个统计量：连通分量总数、整个图是否二分、三角形总数。必须独立判断二分图；没有三角形仍可能存在五边奇环。

## 输入与约束

首行 n m；随后m行 u v。1≤n≤120，0≤m≤n(n-1)/2；无自环、无重边。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行三个整数：components bipartite triangles。二分标记为1或0。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
5 4
0 1
1 2
2 0
3 4
```
输出：
```text
2 0 1
```

0,1,2形成三角，3—4形成另一分量。共有2分量；三角是奇环所以二分为0；三角总数1。

## 分级提示

<details><summary>提示 1</summary>

分量搜索、染色与三角统计共享邻接结构。

</details>

<details><summary>提示 2</summary>

染色冲突不要提前终止全部搜索，否则分量数会不完整。

</details>

<details><summary>提示 3</summary>

每个未访问根增加分量并完成双色搜索，冲突只设flag=0；另枚举a<b<c统计三角。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P070/exercise.py
.\.venv\Scripts\python.exe check.py P070
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P070/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P070.md) · [下一章](../../../08_compression/README.md)
