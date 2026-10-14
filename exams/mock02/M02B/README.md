# M02B 带悬挂网页的 PageRank 排名

由均匀概率p_i=1/n开始，按给定有向链接同步迭代。悬挂网页（无出边）的全部概率均分给所有网页；每条出边分到来源概率/出度。新概率q_i=(1−alpha)/n+alpha*(悬挂质量/n+入边概率份额之和)。每轮更新后算L1=Σ|q_i−p_i|，L1≤tol即收敛，否则最多max_iter轮。始终至少迭代1轮。按最后概率精确降序排名，精确平票按网页下标升序。alpha、tol直接由原十进制字符串构造Fraction，全流程用有理数计算，不加epsilon。

## 输入与约束

首行 n m alpha tol max_iter；接着 m 行 u v。1≤n≤20，0≤m≤100，0≤alpha<1，0<tol≤1，1≤max_iter≤200；小数最多6位。允许自环，无重复有向边。输入合法。小图限制用于精确边界教学，不模拟大图运行性能。

## 输出

第一行实际轮数及是否收敛（1/0）；第二行所有网页排名下标；第三行按原网页下标排列的最后概率（并非按排名排列）。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
2 1 0.8 0.1 10
0 1
```
输出：
```text
3 1
1 0
0.348 0.652
```

手算：网页1悬挂，alpha=0.8。三轮概率为(0.3,0.7)、(0.38,0.62)、(0.348,0.652)，L1为0.4、0.16、0.064。第3轮≤0.1，标记1；网页1高于0，所以排名1 0；概率仍输出原顺序0.348 0.652。

## 分级提示

<details><summary>提示 1</summary>

出度为0时均分，不丢掉概率。

</details>

<details><summary>提示 2</summary>

p和q必须分开；先精确算L1，再用q替换p。

</details>

<details><summary>提示 3</summary>

Fraction读原字符串；判断delta<=tol，按(-p[i],i)排序；只有最终打印概率才转float。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock02/M02B/exercise.py
.\.venv\Scripts\python.exe check.py M02B
.\.venv\Scripts\python.exe check.py --chapter M02
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock02/M02B/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M02B.md)
