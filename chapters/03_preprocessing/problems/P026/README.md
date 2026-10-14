# P026 总体 Z-score 标准化

逐列求均值 μ 与总体标准差 σ=sqrt(Σ(x-μ)²/n)，输出 (x-μ)/σ。常量列输出0。

## 输入与约束

首行 n d；随后 n 行，每行 d 个实数。1≤n≤200，1≤d≤20；绝对值≤1000000。 数值使用普通十进制写法（不使用指数），小数点后最多12位。

## 输出

输出 n 行 d 列标准化结果。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
2 2
2 8
4 8
```
输出：
```text
-1 0
1 0
```

手算：第1列均值3，平方偏差为1和1，总体方差1，标准差1，所以-1、1。第2列常量8，输出0。

## 分级提示

<details><summary>提示 1</summary>

先用Fraction(原始数值字符串)保存十进制精度，不能先转float。先计算每列均值。

</details>

<details><summary>提示 2</summary>

用精确均值和平方偏差求总体方差v；v=0输出0。

</details>

<details><summary>提示 3</summary>

以Fraction求均值μ和总体方差v；v=0直接输出0；否则令delta=x-μ，先精确算delta²/v，再取平方根并恢复delta的正负号。仅在开平方与输出时转float。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P026/exercise.py
.\.venv\Scripts\python.exe check.py P026
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P026/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/preprocessing.html)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P027/README.md) · [题解](../../../../solutions/P026.md)
