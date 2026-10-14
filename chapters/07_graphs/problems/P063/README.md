# P063 并查集连接查询

维护一组点的连接关系。操作0 a b表示把a与b所属的两个集合合并；操作1 a b询问两点是否属于同一集合。使用路径压缩与按集合大小合并。

## 输入与约束

首行 n q；随后q行 type a b；type为0或1。1≤n≤1000，1≤q≤5000，保证至少一个查询；允许重复合并及a=b。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

每个查询一行：相连为1，否则0；合并不输出。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
5 7
1 0 1
0 0 1
1 0 1
0 1 2
1 0 2
1 3 4
1 4 4
```
输出：
```text
0
1
1
0
1
```

最初0与1分开，查询得0；合并0,1后查询得1；合并1,2让0,2间接相连；3,4仍分开。

## 分级提示

<details><summary>提示 1</summary>

每个点最初是自己的父节点。

</details>

<details><summary>提示 2</summary>

find沿父指针到根，同时缩短路径。

</details>

<details><summary>提示 3</summary>

若两根不同，把较小集合的根挂到较大根下；查询比较find(a)==find(b)。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P063/exercise.py
.\.venv\Scripts\python.exe check.py P063
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P063/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/reference/algorithms/index.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P063.md) · [下一题](../P064/README.md)
