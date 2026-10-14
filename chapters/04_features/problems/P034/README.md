# P034 等宽分箱

把 [min,max] 分成 k 个等宽箱，编号0到k-1。非最后箱左闭右开，最后箱包含max；内部边界上的值归右箱。常量数据全部归0号箱。

## 输入与约束

首行 n k；第2行 n 个整数。1≤n≤200，1≤k≤200，值绝对值≤1000000。k可以大于n，因此空箱合法。

## 输出

一行 n 个箱号，按原输入顺序。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
5 2
0 1 2 3 4
```
输出：
```text
0 0 1 1 1
```

手算：min=0,max=4,k=2，宽度2；箱0为[0,2)，箱1为[2,4]，故0、1归0，2、3、4归1。

## 分级提示

<details><summary>提示 1</summary>

求最小、最大值，先处理全部相等情况。

</details>

<details><summary>提示 2</summary>

可用整数计算 floor((x-min)*k/(max-min))，最大值的结果k要改成k-1。

</details>

<details><summary>提示 3</summary>

每个整数x的箱号是 min(k-1,(x-low)*k//(high-low))；常量时全0。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P034/exercise.py
.\.venv\Scripts\python.exe check.py P034
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P034/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/preprocessing.html#discretization)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P035/README.md) · [题解](../../../../solutions/P034.md)
