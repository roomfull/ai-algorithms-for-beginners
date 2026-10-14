# P078 等样本worker梯度平均

每个worker给出相同参数位置的局部平均梯度向量，且题面保证各worker样本数相等。逐参数求worker梯度的简单平均，这时也等于全体样本平均梯度。

## 输入与约束

首行 workers dims；随后workers行，每行dims个局部平均梯度。1≤workers,dims≤100；各worker处理的样本数相等且正数。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行dims个全局平均梯度。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
2 2
1 3
5 -1
```
输出：
```text
3 1
```

两个worker梯度(1,3)和(5,-1)，逐坐标平均得到((1+5)/2,(3-1)/2)=(3,1)。

## 分级提示

<details><summary>提示 1</summary>

每个参数坐标分别聚合，不能先把向量变成标量。

</details>

<details><summary>提示 2</summary>

所有worker相同样本数时，每个worker权重相同。

</details>

<details><summary>提示 3</summary>

sum_grad[j]=sum(g[w][j] for w in workers)，最后除以workers一次。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/09_distributed/problems/P078/exercise.py
.\.venv\Scripts\python.exe check.py P078
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/09_distributed/problems/P078/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P078.md) · [下一题](../P079/README.md)
