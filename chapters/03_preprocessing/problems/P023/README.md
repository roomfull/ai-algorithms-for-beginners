# P023 均值填补缺失值

逐列计算非 NA 元素的算术均值，用该均值填补本列 NA；整列缺失时填 0。保持行列顺序。

## 输入与约束

首行 n d；随后 n 行，每行 d 个实数或大写 NA。1≤n≤200，1≤d≤20；实数绝对值≤1000000。

## 输出

输出填补后的 n 行 d 列矩阵。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
3 2
1 NA
3 4
NA 8
```
输出：
```text
1 6
3 4
2 8
```

手算：第1列已知1和3，均值2；第2列已知4和8，均值6；只替换 NA。

## 分级提示

<details><summary>提示 1</summary>

按列收集非缺失值。

</details>

<details><summary>提示 2</summary>

均值是总和除以有效个数，不能把 NA 算入分母。

</details>

<details><summary>提示 3</summary>

先求每列均值（空列置0），再逐行用均值替换 NA。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P023/exercise.py
.\.venv\Scripts\python.exe check.py P023
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P023/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/impute.html)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P024/README.md) · [题解](../../../../solutions/P023.md)
