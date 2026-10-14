# P062 DFS与连通分量

对整个无向简单图做深度优先搜索。连通分量是互相存在路径的一组点；按最小顶点升序给分量编号0,1,...。使用显式栈避免递归深度限制。

## 输入与约束

首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；无自环、无重边。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行分量总数；第二行n个分量编号。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
6 3
0 2
2 3
1 4
```
输出：
```text
3
0 1 0 0 1 2
```

0,2,3通过路径相连，分量编号0；1,4相连，编号1；5孤立，编号2。外层按0到5扫描保证编号确定。

## 分级提示

<details><summary>提示 1</summary>

从尚未标记的点启动一次DFS，就发现一个新分量。

</details>

<details><summary>提示 2</summary>

栈后进先出；发现时立即给邻居标记当前编号。

</details>

<details><summary>提示 3</summary>

扫描root；若label[root]==-1，标记并入栈，反复弹出扩展，结束后count+=1。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P062/exercise.py
.\.venv\Scripts\python.exe check.py P062
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P062/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P062.md) · [下一题](../P063/README.md)
