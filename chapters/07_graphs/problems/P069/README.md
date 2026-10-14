# P069 PageRank迭代至收敛

从均匀概率p[i]=1/n开始，重复P068的同步更新（包括悬挂点均分）。每轮更新后计算L1变化量Σ|q[i]-p[i]|；≤tol即停止并标记收敛，最多max_iter轮。所有概率与L1用Fraction精确有理数计算，alpha与tol直接从原始十进制字符串构造Fraction，输出时才转float。输出最后已完成的q。此处直接使用tol，不采用某些库的n*tol阈值。

## 输入与约束

首行 n m alpha tol max_iter；随后m行 u v。1≤n≤20，0≤m≤100，0≤alpha<1，0<tol≤1，1≤max_iter≤200；允许自环，无重复有向边。限定小图是为了直观、精确地验证收敛边界；大图通常用浮点迭代，本题不模拟其性能。 保证输入合法。 顶点编号为0..n-1。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行 实际轮数 是否收敛（1/0）；第二行n个最后概率。即使初始分布已经是固定点，也先做一轮再判断。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
2 1 0.8 0.1 10
0 1
```
输出：
```text
3 1
0.348 0.652
```

均匀初值(0.5,0.5)，alpha=0.8，0→1。前3轮分别为(0.3,0.7)、(0.38,0.62)、(0.348,0.652)。L1依次0.4,0.16,0.064；第3轮≤0.1，输出3 1。

## 分级提示

<details><summary>提示 1</summary>

从原字符串构造Fraction(alpha)、Fraction(tol)，均匀初值用Fraction(1,n)。

</details>

<details><summary>提示 2</summary>

所有概率流与delta保持Fraction，先求delta再用q替换p；输出时才转float。

</details>

<details><summary>提示 3</summary>

for step in 1..max_iter：精确构造q；delta=sum(abs(q[i]-p[i]))；p=q；若delta<=tol则标记并break。不加epsilon。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/07_graphs/problems/P069/exercise.py
.\.venv\Scripts\python.exe check.py P069
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/07_graphs/problems/P069/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P069.md) · [下一题](../P070/README.md)
