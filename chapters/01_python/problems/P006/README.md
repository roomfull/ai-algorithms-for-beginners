# P006 for 累加

本题为原创训练题。先修：先完成 P005；本题新概念见下方‘开始前先读’。

## 任务

用 for 循环计算从 1 到 n（包含 n）的整数和。本题要求练习逐步累加，不用等差数列公式替代循环。

## 开始前先读

`for i in range(1, n + 1):` 表示依次让 i 取 1、2、…、n。range 的右边界不包含在内，所以写 n+1。循环体缩进，循环结束后的 print 恢复到左边。累加器先设为 0；`total = total + i` 是先取旧 total 加上 i，再存回名字 total。

## 输入输出与约束

输入一行非负整数 n。输出一行整数总和。

0 ≤ n ≤ 100000，n=0 时没有待累加的数，总和定义为 0。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `int`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
4
```

输出：

```text
10
```

手算：n=4，初始 total=0；i=1 后为1，i=2 后为3，i=3 后为6，i=4 后为10。循环完只输出10。n=0 时 range(1,1) 没有数，total 仍是0。

## 三级提示

<details><summary>提示1</summary>

需要一个起点为 0 的总和变量。

</details>

<details><summary>提示2</summary>

range 的结束值不包含在内，目标循环到 n 应写 n+1。

</details>

<details><summary>提示3</summary>

循环内更新 total = total + i；循环外输出 total，避免输出每一步。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P006/exercise.py
.\.venv\Scripts\python.exe check.py P006
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P006.md)。[下一题 P007](../P007/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/tutorial/controlflow.html#for-statements)。
