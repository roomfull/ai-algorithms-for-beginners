# P027 先划分再拟合训练统计量

按给定下标排列样本：前 t 个为训练集，余下为验证集。仅用训练集逐列 min/max 做 Min-Max；训练常量列在两集合中都输出0。验证值不裁剪，可小于0或大于1。

## 输入与约束

首行 n d t；随后 n 行 d 个实数；最后一行 n 个互异下标，恰好是0到n-1的排列。2≤n≤200，1≤d≤20，1≤t<n；实数绝对值≤1000000。

## 输出

按给定排列输出全部 n 行，先训练后验证，无标签或空行。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
4 1 2
0
10
100
5
0 1 2 3
```
输出：
```text
0
1
10
0.5
```

手算：排列0 1 2 3，训练值0和10给出 min=0,max=10；验证100变成10，验证5变成0.5。若先用100求最大值，就泄漏了验证集信息。

## 分级提示

<details><summary>提示 1</summary>

按照下标排列，取前 t 行作为训练。

</details>

<details><summary>提示 2</summary>

只在训练行上求统计量，但把同一组统计量应用到全部行。

</details>

<details><summary>提示 3</summary>

缓存训练 min/max；遍历排列逐行缩放，常量列输出0，验证结果不裁剪。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P027/exercise.py
.\.venv\Scripts\python.exe check.py P027
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P027/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P028/README.md) · [题解](../../../../solutions/P027.md)
