# P077 连续均衡数据分片

把编号0..n-1的样本依次分给workers个worker，形成连续区间。每个worker先得n//workers个，余数n%workers个依次给前面的worker，每个多1；允许空片。这里只模拟分片，不启动进程。

## 输入与约束

一行 n workers。0≤n≤1000000，1≤workers≤1000。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

共workers行，每行 start end，表示半开区间[start,end)。空片start=end；不输出样本本身。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
10 3
```
输出：
```text
0 4
4 7
7 10
```

10//3=3，余数1，所以长度4,3,3，区间[0,4)、[4,7)、[7,10)。end不属于该片。

## 分级提示

<details><summary>提示 1</summary>

除法的商给每人，余数给前面的人。

</details>

<details><summary>提示 2</summary>

每个区间从上一片end开始。

</details>

<details><summary>提示 3</summary>

base,extra=divmod(n,workers)；第i片length=base+(i<extra)，输出start,start+length，再移动start。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/09_distributed/problems/P077/exercise.py
.\.venv\Scripts\python.exe check.py P077
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/09_distributed/problems/P077/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P077.md) · [下一题](../P078/README.md)
