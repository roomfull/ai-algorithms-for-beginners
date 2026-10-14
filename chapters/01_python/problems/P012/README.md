# P012 函数与 return

本题为原创训练题。先修：先完成 P011；本题新概念见下方‘开始前先读’。

## 任务

定义函数 square(x)，用 return 返回 x 的平方。读取两行整数，分别调用函数并逐行输出结果；函数内部不负责输出。

## 开始前先读

函数是给一段可重复执行的代码取名字。`def square(x):` 定义名称 square，x 是形参，调用 `square(3)` 时 x 收到3。缩进的函数体在调用时才运行。`return` 把值交还调用处并结束本次调用；`print` 只往屏幕写文字，不能代替返回值。函数定义后空一行，再写顶层输入代码。

## 输入输出与约束

输入两行整数 a、b。输出两行，分别为 a² 和 b²。

-10000 ≤ a,b ≤ 10000。必须定义 square 并在两次计算中调用。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `int`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
3
4
```

输出：

```text
9
16
```

手算：square(3) 内部计算3×3=9，并把9返回给 print；square(4) 返回16，最终两行9和16。square(-2) 计算(-2)×(-2)=4，平方不会保留负号。

## 三级提示

<details><summary>提示1</summary>

平方就是一个数与自身相乘；把这个规则写进函数。

</details>

<details><summary>提示2</summary>

函数体写 return x*x，在函数外读取和输出。

</details>

<details><summary>提示3</summary>

先定义 square，后面两个 print 分别调用 square(a) 和 square(b)。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P012/exercise.py
.\.venv\Scripts\python.exe check.py P012
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P012.md)。[下一题 P013](../P013/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/tutorial/controlflow.html#defining-functions)。
