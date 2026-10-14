# P035 按秩等频分组

本题采用按秩分组的等频教学规则：按 (值, 原始下标) 升序稳定排序；从0开始的秩 r 分到 floor(r*k/n) 号组；再恢复输入顺序。重复值按原始下标打破并列，同值可分到不同组，因此这不是只由数值边界决定的区间分箱。每组数量最多相差1，不保证完全相等。

## 输入与约束

首行 n k；第2行 n 个整数。1≤n≤200，1≤k≤n，值绝对值≤1000000。

## 输出

一行 n 个组号（0到k-1），顺序与原数据相同。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
5 2
5 1 3 2 4
```
输出：
```text
1 0 0 0 1
```

手算：排序后的(值,下标)为(1,1),(2,3),(3,2),(4,4),(5,0)；秩0、1、2归0，秩3、4归1；恢复后得到1 0 0 0 1。

## 分级提示

<details><summary>提示 1</summary>

排序时保留原始位置。

</details>

<details><summary>提示 2</summary>

组号由秩决定，不是直接由值决定；重复值也有不同秩。

</details>

<details><summary>提示 3</summary>

排序 enumerate(values) 为 (value,index) 顺序；对秩r把 r*k//n 写入结果的原始index。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P035/exercise.py
.\.venv\Scripts\python.exe check.py P035
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P035/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/preprocessing.html#discretization)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P036/README.md) · [题解](../../../../solutions/P035.md)
