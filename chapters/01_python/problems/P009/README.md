# P009 字典词频

本题为原创训练题。先修：先完成 P008；本题新概念见下方‘开始前先读’。

## 任务

统计一行单词的出现次数，并输出指定查询单词的次数。区分大小写；单词按空白分开。必须先建立词频字典，再查询。

## 开始前先读

字典把键映射到值，例如 `{'cat': 2}` 表示 cat 出现2次。`{}` 是空字典。`word in counts` 判断键是否存在。`counts[word]` 读取或写入该键的值；不存在时直接读取会报 KeyError。因此第一次见单词先设0，再加1。字典与列表的区别是键可以是单词，不必是从0开始的整数位置。

## 输入输出与约束

第一行一个或多个单词，第二行一个查询单词。输出一行非负整数。

第一行 1–1000 个单词；每词1–30个英文字母；查询词可能未出现。

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `int`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
cat dog cat
cat
```

输出：

```text
2
```

手算：cat dog cat：初始{}；读cat变{'cat':1}；读dog新增dog:1；再次读cat将其增为2。查询cat得到2，若查询bird则没这个键，输出0。

## 三级提示

<details><summary>提示1</summary>

每个不同单词作为一个键，次数作为对应的值。

</details>

<details><summary>提示2</summary>

加1前先检查键是否存在，未出现时初始化为0。

</details>

<details><summary>提示3</summary>

遍历单词建立 counts；查询时用 if 判断存在，否则打印0。

</details>

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\.venv\Scripts\python.exe chapters/01_python/problems/P009/exercise.py
.\.venv\Scripts\python.exe check.py P009
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/P009.md)。[下一题 P010](../P010/README.md)；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料](https://docs.python.org/3.11/tutorial/datastructures.html#dictionaries)。
