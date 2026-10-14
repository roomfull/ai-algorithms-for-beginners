# P005 if 分数分类

本题为原创训练题。先修：先完成 P004；本题新概念见下方‘开始前先读’。

## 任务

按成绩分类：90 分及以上输出 EXCELLENT；60–89 分输出 PASS；低于 60 分输出 FAIL。

## 开始前先读

比较表达式 `score >= 90` 的值是布尔值 True 或 False。`if 条件:` 在条件为真时执行缩进的语句；`elif` 表示前面的条件没满足时再判断；`else` 接住剩余情况。冒号不可漏。统一用四个空格缩进，同一层对齐。`=` 赋值，`==` 才是相等比较。

## 输入输出与约束

输入一行整数 score。输出一行大写分类文本。

0 ≤ score ≤ 100；边界 60 和 90 包含在较高等级。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `text`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
60
```

输出：

```text
PASS
```

手算：score=60，先比较 60≥90 为假，再比较 60≥60 为真，输出 PASS。score=90 第一项立即成立，输出 EXCELLENT，不会再执行后面的分支。

## 三级提示

<details><summary>提示1</summary>

先判断最高的等级，再判断及格，否则处理不及格。

</details>

<details><summary>提示2</summary>

最高分支使用 >=90，第二个分支使用 >=60，剩余写 else。

</details>

<details><summary>提示3</summary>

三个分支分别只 print 一次；用 if/elif/else 保证只有一条结果。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P005/exercise.py
.\.venv\Scripts\python.exe check.py P005
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P005.md)。[下一题 P006](../P006/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/tutorial/controlflow.html#if-statements)。
