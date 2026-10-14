# M04B 不同 worker 与 microbatch 的加权更新

给定多个worker，每个worker有若干大小可能不同的microbatch（微批次）。每条微批次提供样本数s以及以样本为单位求平均后的梯度g。所有梯度已在同一初始参数w处计算。全局梯度G=Σ(s*g)/Σs（求和遍历所有worker的全部微批次），然后仅做一次SGD更新w_new=w−lr*G。不直接平均微批次平均值，也不等权平均worker平均值。此为单机数值模拟，无实际通信、多进程或性能保证。

## 输入与约束

首行 worker数量 W、参数维数 d、学习率 lr；第二行d个初始参数；随后对每个worker：一行微批次数t，然后t行，每行先给样本数s，再给d个平均梯度。1≤W≤8，1≤d≤10，1≤t≤8，1≤s≤100，0≤lr≤10；参数/梯度绝对值≤100，最多3位小数。输入合法。

## 输出

第一行d个全局平均梯度；第二行d个更新后的参数。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
2 2 0.1
1 2
2
1 2 4
3 0 0
1
2 3 6
```
输出：
```text
1.3333333333333333 2.6666666666666667
0.8666666666666667 1.7333333333333333
```

手算：worker0两批：(s=1,g=(2,4))和(s=3,g=(0,0))；worker1一批：(s=2,g=(3,6))。总样本6，总梯度和(8,16)，G=(4/3,8/3)。lr=0.1，从(1,2)更新为(13/15,26/15)。

## 分级提示

<details><summary>提示 1</summary>

输入梯度是平均值，先乘该批样本数还原梯度和。

</details>

<details><summary>提示 2</summary>

跨所有worker累加总样本数及每一维梯度和。

</details>

<details><summary>提示 3</summary>

全部读完后才除总样本数，再作一次更新；不要每读一批就更新w。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock04/M04B/exercise.py
.\.venv\Scripts\python.exe check.py M04B
.\.venv\Scripts\python.exe check.py --chapter M04
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock04/M04B/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://pytorch.org/docs/stable/notes/ddp.html)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M04B.md)
