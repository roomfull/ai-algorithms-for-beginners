# P007 while 计数

本题为原创训练题。先修：先完成 P006；本题新概念见下方‘开始前先读’。

## 任务

用 while 循环统计 1 到 n 中偶数的个数。每轮访问下一个正偶数，训练循环条件和更新。

## 开始前先读

`while 条件:` 在每轮开始前检查条件，条件为真就执行缩进的语句。与 for 不同，下一步如何前进由你安排。设 `current=2`，每访问一次便把 count 加1，再令 current 增加2。`<=` 表示小于或等于。只要更新能让 current 最终超过 n，循环就会结束。

## 输入输出与约束

输入一行非负整数 n。输出一行偶数数量。

0 ≤ n ≤ 100000；0 不在本题区间 1 到 n 内。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `int`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
7
```

输出：

```text
3
```

手算：n=7：current 依次是2、4、6，count 依次变1、2、3；current 更新成8后条件8≤7为假，退出并输出3。n=1 时第一轮条件就为假，输出0。

## 三级提示

<details><summary>提示1</summary>

从最小正偶数 2 开始，不必逐个检查奇数。

</details>

<details><summary>提示2</summary>

循环条件是 current <= n，每轮计数加 1，current 加 2。

</details>

<details><summary>提示3</summary>

初始 count=0、current=2；while 内同时更新两个变量，循环后打印 count。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P007/exercise.py
.\.venv\Scripts\python.exe check.py P007
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P007.md)。[下一题 P008](../P008/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/tutorial/introduction.html#first-steps-towards-programming)。
