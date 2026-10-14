# P029 SMOTE 线段插值

给定同一类别的基点 x、邻点 z 和系数 λ，计算新样本 x+λ(z-x)，即线段插值。本题只做插值，不查找邻居。

## 输入与约束

首行维数 d；第2行 d 个实数 x；第3行 d 个实数 z；第4行 λ。1≤d≤20，0≤λ≤1，特征绝对值≤1000000。

## 输出

一行 d 个新样本特征，不输出标签。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
2
1 3
5 7
0.25
```
输出：
```text
2 4
```

手算：λ=0.25，差向量(4,4)，乘系数得(1,1)，加基点(1,3)得(2,4)。

## 分级提示

<details><summary>提示 1</summary>

逐坐标处理，所有坐标使用同一个 λ。

</details>

<details><summary>提示 2</summary>

差向量是邻点减基点，方向别反过来。

</details>

<details><summary>提示 3</summary>

使用 [x[j]+λ*(z[j]-x[j]) for j in range(d)]；λ=0返回x，λ=1返回z。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P029/exercise.py
.\.venv\Scripts\python.exe check.py P029
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P029/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://imbalanced-learn.org/stable/over_sampling.html#sample-generation)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P030/README.md) · [题解](../../../../solutions/P029.md)
