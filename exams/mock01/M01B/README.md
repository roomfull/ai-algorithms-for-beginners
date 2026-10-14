# M01B 机房网络布线的最小总成本

多个机房需要接成一个连通网络，备选无向线路各有非负整数成本。求连接所有机房的最小总成本；无法连通时输出−1。允许自环和多条同端点线路，自环不能连接两个组件。采用Kruskal：成本相同的线路按输入下标处理。

## 输入与约束

首行 n m；后续 m 行 u v w，顶点0..n−1。1≤n≤100，0≤m≤500，0≤w≤10000。输入合法。

## 输出

一行一个整数：最小生成树总成本，断开时−1；只有一个机房时为0。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
4 5
0 1 4
1 2 1
2 3 2
0 3 9
0 2 3
```
输出：
```text
6
```

手算：按成本选线路1(1→2,1)、2(2→3,2)、4(0→2,3)，连接4个机房，总成本1+2+3=6。线路0会形成环，线路3更贵。

## 分级提示

<details><summary>提示 1</summary>

连通n个点只需n−1条树边。

</details>

<details><summary>提示 2</summary>

并查集判断两个端点是否已经连通。

</details>

<details><summary>提示 3</summary>

按(w,输入下标)排序；根不同则合并并累加；选中数不足n−1则输出−1。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock01/M01B/exercise.py
.\.venv\Scripts\python.exe check.py M01B
.\.venv\Scripts\python.exe check.py --chapter M01
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock01/M01B/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://github.com/networkx/networkx/blob/main/networkx/algorithms/tree/mst.py)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M01B.md)
