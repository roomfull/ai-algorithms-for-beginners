# P024 按首次出现稳定去重

把每行当作一个整数样本，删除重复行，保留各不同样本第一次出现的位置顺序。

## 输入与约束

首行 n d；随后 n 行，每行 d 个整数。1≤n≤200，1≤d≤20，整数绝对值≤1000000。

## 输出

首行输出不同样本数，再输出保留的样本，每行 d 个整数。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
5 2
2 1
1 2
2 1
1 2
3 3
```
输出：
```text
3
2 1
1 2
3 3
```

手算：2 1 和 1 2 第二次出现时跳过，保留第1、2、5行，共3行。

## 分级提示

<details><summary>提示 1</summary>

准备一个已见集合和一个结果列表。

</details>

<details><summary>提示 2</summary>

列表不能直接放入 set，可把每行转成 tuple。

</details>

<details><summary>提示 3</summary>

按输入顺序遍历；行元组未见过才加入集合与结果列表。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P024/exercise.py
.\.venv\Scripts\python.exe check.py P024
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P024/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P025/README.md) · [题解](../../../../solutions/P024.md)
