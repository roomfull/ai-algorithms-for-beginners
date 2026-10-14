# P011 排序与平票

本题为原创训练题。先修：先完成 P010；本题新概念见下方‘开始前先读’。

## 任务

将学生成绩按分数从高到低排列；分数相同时按姓名的字典序从小到大排列。输出全部记录。使用两次稳定排序即可，无需 lambda 或尚未学过的自定义函数。

## 开始前先读

`sorted(items)` 返回升序的新列表；`list.sort()` 原地修改列表。Python 排序是稳定的：排序键相等时保留原先相对顺序。先把记录写成 `[name, score]`，默认排序依次比较姓名再比较分数。`row[0]`、`row[1]` 取两个位置。`key` 参数指定比较依据，`operator.itemgetter(1)` 表示按位置1取分数；`reverse=True` 表示降序。`from operator import itemgetter` 导入标准库提供的工具，学完函数后再考虑自己写 key。

## 输入输出与约束

第一行人数 n，后面 n 行各为姓名和整数分数，空格分隔。每条输出为姓名、一个空格、分数。

1 ≤ n ≤ 1000；姓名为1–20个小写/大写英文字母且互异，分数0–100。字典序按 Python 字符串顺序，大小写不同；示例平票使用同一大小写。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `text`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
3
Bob 80
Amy 90
Zoe 90
```

输出：

```text
Amy 90
Zoe 90
Bob 80
```

手算：Bob80、Amy90、Zoe90；先按姓名得到Amy90、Bob80、Zoe90，再按分数降序；两个90保持Amy在Zoe前，最终Amy90、Zoe90、Bob80。

## 三级提示

<details><summary>提示1</summary>

平票规则可以先确定，再进行稳定的主键排序。

</details>

<details><summary>提示2</summary>

先对 [姓名,分数] 的列表默认排序，建立姓名升序。

</details>

<details><summary>提示3</summary>

第二次按 itemgetter(1) 排分数并 reverse=True；稳定性会保留同分姓名顺序。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P011/exercise.py
.\.venv\Scripts\python.exe check.py P011
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P011.md)。[下一题 P012](../P012/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/howto/sorting.html#sort-stability-and-complex-sorts)。
