# M03A 指定初值聚类、误差与查询分配

给定k个初始中心，恰好执行T轮Lloyd更新：先按旧中心给每个训练样本分配最近中心，再同时以簇内均值替换各中心。空簇保留旧中心。距离平方数学上平票时取中心下标较小者。执行完T轮后，按最终中心重新分配全部训练样本，计算SSE=Σ样本到所属最终中心的距离平方，再把查询分配给最近的最终中心；最后重分配不再更新中心。所有十进制坐标由原字符串构造Fraction，保持精确距离平票与均值。

## 输入与约束

首行 n d k T；接着n行训练坐标，每行d个十进制数；接着k行初始中心；最后一行查询坐标。1≤n≤30，1≤d≤8，1≤k≤5，1≤T≤30；坐标绝对值≤100，最多3位小数；初值可重复。输入合法。

## 输出

第一行n个最终训练标签（中心下标0起）；接着k行最终中心（每行d个浮点数）；然后一行SSE；最后一行查询整数标签。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
4 1 2 2
0
2
8
10
0
10
5
```
输出：
```text
0 0 1 1
1
9
4
0
```

手算：初始中心0、10，第一轮点0、2归0，点8、10归1，均值变为1、9；第二轮不变。最终标签0 0 1 1，SSE=1+1+1+1=4；查询5离两个中心都为4，精确平票选0。

## 分级提示

<details><summary>提示 1</summary>

分配与更新分成两步，各轮用全部旧中心。

</details>

<details><summary>提示 2</summary>

空簇不改；新中心为逐维和/簇大小。

</details>

<details><summary>提示 3</summary>

执行T次更新后再调用一次分配；SSE使用最终标签与最终中心，查询独立分配，不加入训练均值。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock03/M03A/exercise.py
.\.venv\Scripts\python.exe check.py M03A
.\.venv\Scripts\python.exe check.py --chapter M03
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock03/M03A/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M03A.md)
