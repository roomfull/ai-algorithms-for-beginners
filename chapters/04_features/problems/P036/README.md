# P036 二分类列联表卡方值

输入2×2列联表，行是两组，列是标签0和1；各格 O 为样本数。总数 N、行和 R、列和 C；期望 E=R*C/N。计算 Pearson χ²=Σ(O-E)²/E，不做连续性（Yates）修正。N=0时输出0，E=0的项约定贡献0。本题只算统计量，不求p值或判断显著性。

## 输入与约束

两行，每行两个非负整数，表示对应组的0类和1类数量；每个数≤1000000。

## 输出

一行一个卡方统计量。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
10 0
0 10
```
输出：
```text
20
```

手算：表[[10,0],[0,10]]：N=20，两行和、两列和都是10，各E=5；四格各贡献(10-5)²/5或(0-5)²/5=5，总和20。

## 分级提示

<details><summary>提示 1</summary>

先计算总数、两行和、两列和。

</details>

<details><summary>提示 2</summary>

每格期望由所在行和×所在列和/总数给出。

</details>

<details><summary>提示 3</summary>

遍历4格并累加(O-E)²/E；N=0直接0，E=0跳过；参考解用Fraction计算精确有理数，最后转浮点输出。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P036/exercise.py
.\.venv\Scripts\python.exe check.py P036
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P036/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.chi2_contingency.html)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P037/README.md) · [题解](../../../../solutions/P036.md)
