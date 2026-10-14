# P013 二维列表行和

本题为原创训练题。先修：先完成 P012；本题新概念见下方‘开始前先读’。

## 任务

把 r 行整数存成二维列表，再计算并逐行输出每一行的和。所有行长度相同，目标是理解一张表由行列表组成。

## 开始前先读

二维列表就是列表里面放列表。`matrix[0]` 取得第一行；`matrix[0][1]` 再从该行取第二个元素。不要写成 matrix[0,1]，那是之后 NumPy 的写法。构建每行时重新写 `row=[]`，转换每个 token 再 append；把完成的 row 放入 matrix。嵌套循环中，内层负责一行，外层负责各行。

## 输入输出与约束

第一行整数 r；随后 r 行，每行 c 个整数。输出 r 行，各为对应行的整数和。c 由数据行长度确定，不另输入。

1 ≤ r,c ≤ 100；元素在 [-10000,10000]；所有行长度相同。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `int`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
2
1 2 3
4 5 6
```

输出：

```text
6
15
```

手算：表为[[1,2,3],[4,5,6]]。外层先拿到[1,2,3]，内层从0累加成1、3、6，输出6；新的一行重新从0累加成4、9、15，输出15。

## 三级提示

<details><summary>提示1</summary>

先完成一个 row，再把它 append 到 matrix。

</details>

<details><summary>提示2</summary>

输出阶段的 total 应在每次开始新行时重置。

</details>

<details><summary>提示3</summary>

外层 for row in matrix，内层 for value in row 累加，内层结束后打印一行总和。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P013/exercise.py
.\.venv\Scripts\python.exe check.py P013
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P013.md)。[下一题 P014](../P014/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/tutorial/introduction.html#lists)。
