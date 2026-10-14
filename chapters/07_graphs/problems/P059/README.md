# P059 无向图邻接表

把无向简单图的每条边分别登记到两端的邻居表；同一个顶点的邻居按编号升序输出。无向边(u,v)意味着u能到v且v能到u。

## 输入与约束

首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；无自环、无重边。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

共n行，第i行依次输出 i、邻居个数、所有邻居；孤立点只输出 i 0。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
4 2
0 2
0 1
```
输出：
```text
0 2 1 2
1 1 0
2 1 0
3 0
```

边0—2给0增加邻居2，给2增加邻居0；边0—1同理。因此0的邻居升序为1,2，3没有邻居。

## 分级提示

<details><summary>提示 1</summary>

先为每个点建立一个空列表。

</details>

<details><summary>提示 2</summary>

每条边执行两次append，再排序各行。

</details>

<details><summary>提示 3</summary>

遍历i=0..n-1，输出 [i,len(adj[i])]+sorted(adj[i])。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P059/exercise.py
.\.venv\Scripts\python.exe check.py P059
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P059/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P059.md) · [下一题](../P060/README.md)
