# P038 中位数与 MAD 鲁棒特征

求中位数 M：排序后奇数个取中间值，偶数个取中间两值平均。求 MAD=median(|x-M|)，即中位绝对偏差。输出鲁棒特征 (x-M)/MAD；MAD=0时本题约定所有特征输出0。使用原始MAD，不乘正态校准系数，不检测异常阈值。

## 输入与约束

一行 n 个实数（无需单独输入n），1≤n≤200，绝对值≤1000000。 数值使用普通十进制写法（不使用指数），小数点后最多12位。

## 输出

第一行 M MAD；第二行 n 个鲁棒特征，按原始顺序。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
1 2 3 100
```
输出：
```text
2.5 1
-1.5 -0.5 0.5 97.5
```

手算：排序1、2、3、100，中位数(2+3)/2=2.5；绝对偏差1.5、0.5、0.5、97.5，排序0.5、0.5、1.5、97.5，中位数1。减2.5后除1，得-1.5、-0.5、0.5、97.5。

## 分级提示

<details><summary>提示 1</summary>

先用Fraction(原始数值字符串)保存十进制精度，不能先转float。写一个排序取中间的median函数，可调用两次。

</details>

<details><summary>提示 2</summary>

第二次median的输入是每个元素到第一次median的绝对距离。

</details>

<details><summary>提示 3</summary>

减法、统计量及除法均保留Fraction，只在最终输出时转float。先求M，再求abs(x-M)的中位数；MAD>0时逐项除MAD，否则造全0；不能用偏差的平均数代替中位数。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P038/exercise.py
.\.venv\Scripts\python.exe check.py P038
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P038/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_abs_deviation.html)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../../README.md) · [题解](../../../../solutions/P038.md)
