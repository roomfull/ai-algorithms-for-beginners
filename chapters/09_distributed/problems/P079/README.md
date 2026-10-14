# P079 不同样本数的加权梯度

各worker输入一个样本数count和局部平均梯度向量。全局平均=Σ(count_w*g_w)/Σcount_w；count=0的worker忽略，即使其占位梯度非零也不贡献。总样本数保证大于0。

## 输入与约束

首行 workers dims；随后workers行 count g1 ... gd。1≤workers,dims≤100，0≤count≤1000000，count为整数且总和>0。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行dims个样本加权全局平均梯度。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
2 2
1 1 3
3 5 -1
```
输出：
```text
4 0
```

worker0有1样本梯度(1,3)，worker1有3样本梯度(5,-1)。全局=(1*(1,3)+3*(5,-1))/4=(4,0)，不是简单平均(3,1)。

## 分级提示

<details><summary>提示 1</summary>

局部平均乘count才能还原局部梯度和。

</details>

<details><summary>提示 2</summary>

先累加梯度和与样本数，最后统一除总样本数。

</details>

<details><summary>提示 3</summary>

numerator[j]+=count*g[j]；total+=count；global[j]=numerator[j]/total。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/09_distributed/problems/P079/exercise.py
.\.venv\Scripts\python.exe check.py P079
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/09_distributed/problems/P079/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P079.md) · [下一题](../P080/README.md)
