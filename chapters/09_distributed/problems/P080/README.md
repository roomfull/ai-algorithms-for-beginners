# P080 Microbatch累积与同步SGD

各worker把局部数据分成microbatch。每个microbatch提供样本数c与局部平均梯度g；把全部worker的全部microbatch累加Σc*g，再除全局样本总数一次，得到global_grad。所有梯度都在同一个旧参数theta上计算，最后只执行一次同步SGD：theta_new=theta-lr*global_grad。

## 输入与约束

首行 workers dims lr；第二行dims个旧参数theta。随后按worker顺序：先一行该worker的microbatch数b，再b行 count g1 ... gd。1≤workers,dims≤100，0≤b≤100，0≤count≤1000000，0<lr≤1；全局count总和>0；允许b=0与count=0。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行dims个全局平均梯度；第二行dims个更新后的参数。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
2 1 0.1
10
2
1 2
3 4
1
2 8
```
输出：
```text
5
9.5
```

worker0的两批为1样本梯度2与3样本梯度4，worker1的一批2样本梯度8。加权和=2+12+16=30，总样本6，全局梯度5；theta=10，lr=0.1，只更新一次得到9.5。

## 分级提示

<details><summary>提示 1</summary>

不能按microbatch个数简单平均，因为每批大小可能不同。

</details>

<details><summary>提示 2</summary>

跨worker仍用样本总数作分母，不能再次除worker数。

</details>

<details><summary>提示 3</summary>

对所有批积累count*grad和total_count，末尾global=sum/total，new=theta-lr*global。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/09_distributed/problems/P080/exercise.py
.\.venv\Scripts\python.exe check.py P080
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/09_distributed/problems/P080/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P080.md) · [模拟卷与学习路线](../../../../README.md)
