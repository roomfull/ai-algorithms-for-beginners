# P025 Min-Max 列缩放

逐列计算 (x-min)/(max-min)，把每列缩放到 [0,1]；常量列（max=min）所有输出均为0。

## 输入与约束

首行 n d；随后 n 行，每行 d 个实数。1≤n≤200，1≤d≤20；绝对值≤1000000。 数值使用普通十进制写法（不使用指数），小数点后最多12位。

## 输出

输出 n 行 d 列缩放结果。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
3 2
0 7
5 7
10 7
```
输出：
```text
0 0
0.5 0
1 0
```

手算：第1列 min=0,max=10，得到0、0.5、1；第2列全是7，得到0。

## 分级提示

<details><summary>提示 1</summary>

先用Fraction(原始数值字符串)保存十进制精度，不能先转float。列最大值与最小值分别计算。

</details>

<details><summary>提示 2</summary>

分母是最大值减最小值；若为0，直接输出0。

</details>

<details><summary>提示 3</summary>

减法、统计量及除法均保留Fraction，只在最终输出时转float。缓存各列 min/max，再逐元素套公式，常量分支避免除0。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P025/exercise.py
.\.venv\Scripts\python.exe check.py P025
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P025/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/preprocessing.html)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P026/README.md) · [题解](../../../../solutions/P025.md)
