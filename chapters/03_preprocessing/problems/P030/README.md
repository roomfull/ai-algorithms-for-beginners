# P030 小型确定性 SMOTE

实现完整小型 SMOTE 的确定性教学版。少数类是原始样本数较少的类别（本题禁止并列）。按其输入顺序列为 minority。对每个少数类基点，只在其余少数类原样本内求平方欧氏距离；按 (距离, 原始输入下标) 升序取前 k 个邻居。第 r 条新样本以 minority[r % m] 为基点，使用该条输入的邻居名次 q（0起）和 λ 做 x+λ(z-x)。新样本不加入邻居搜索。

## 输入与约束

首行 n d k g；随后 n 行：0/1标签及 d 个实数特征；再有 g 行：q λ。5≤n≤200，1≤d≤20，1≤g≤200；两类均存在且样本数不等；少数类数 m≥2；1≤k≤m-1，0≤q<k，0≤λ≤1，特征绝对值≤1000000。

## 输出

只输出生成的 g 行特征，每行 d 个数，不输出原样本、行数或标签。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
5 1 1 2
1 0
0 1
1 10
0 2
0 3
0 0.5
0 0.25
```
输出：
```text
5
7.5
```

手算：少数类为1，其点按输入顺序是0、10；k=1时互为唯一邻居。第0条以0为基点，λ=0.5得5；第1条以10为基点，λ=0.25得7.5。多数类1、2、3不参与。

## 分级提示

<details><summary>提示 1</summary>

统计两类数目，取少数类，保留原始下标用于距离并列。

</details>

<details><summary>提示 2</summary>

针对每个少数类基点排序其他少数类点；不需要开平方，平方距离的顺序相同。

</details>

<details><summary>提示 3</summary>

预存每个基点前 k 个邻居；第 r 条使用 r % m 基点与输入 q 邻居，再做统一系数插值。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P030/exercise.py
.\.venv\Scripts\python.exe check.py P030
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P030/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://imbalanced-learn.org/stable/over_sampling.html#sample-generation)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../../README.md) · [题解](../../../../solutions/P030.md)
