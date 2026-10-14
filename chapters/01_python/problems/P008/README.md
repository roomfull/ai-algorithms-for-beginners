# P008 列表筛选

本题为原创训练题。先修：先完成 P007；本题新概念见下方‘开始前先读’。

## 任务

筛选一行整数中严格大于 0 的数，保持原顺序和重复次数。输出它们，彼此用一个空格隔开；没有正数则输出 EMPTY。

## 开始前先读

列表是有顺序的容器，`[]` 是空列表，`append(x)` 把 x 放到末尾。`input().split()` 将一行按空白拆成字符串列表，for 能逐个访问这些字符串。`len(items)` 返回元素个数。索引从0开始，`items[0]` 是第一个元素。`' '.join(parts)` 把字符串列表按空格接成一行；所以筛选后可保存原来的文字 token。这里只用普通循环，不用列表推导式。

## 输入输出与约束

输入一行空格分隔的整数。输出一行筛选结果或 EMPTY。

1–1000 个整数，每个数在 [-10000,10000]；0 不属于正数。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `text`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
1 -2 3 0 -4
```

输出：

```text
1 3
```

手算：输入1 -2 3 0 -4：先保留1，-2跳过，再保留3，0和-4跳过，结果列表为['1','3']，连接成1 3。输入2 2 -3 1时两个2都要保留。

## 三级提示

<details><summary>提示1</summary>

用空列表保存通过条件的元素，遍历时保持顺序。

</details>

<details><summary>提示2</summary>

比较时将 token 转成 int；保存时仍可保存字符串 token，方便 join。

</details>

<details><summary>提示3</summary>

每遇到 int(token)>0 就 append(token)，最后按列表长度决定 join 或 EMPTY。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P008/exercise.py
.\.venv\Scripts\python.exe check.py P008
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P008.md)。[下一题 P009](../P009/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/tutorial/datastructures.html#more-on-lists)。
