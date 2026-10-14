# P042 K-means 分配样本

聚类没有已知类别标签；这里只给定c个中心，把每个点分配给距离平方最小的中心。先求最小距离m，再从小索引到大选第一个distance≤m+1e-12的中心。距离与1e-12均按精确数值比较；这是近距离平票规则，也包含严格等距。

## 输入与约束

第一行 n d c；随后n行d个实数样本，再c行d个实数中心。1≤n≤100，1≤d≤10，1≤c≤10；有限实数绝对值≤100，输入最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

一行n个整数中心编号，从0开始。 输出使用十进制整数，不可带小数点。

## 样例

输入：
```text
3 1 2
0
2
5
0
4
```
输出：
```text
0 0 1
```

手算：点0、2、5；中心0、4。距离平方依次(0,16)、(4,4)、(25,1)，点2平局取中心0，得到0 0 1。

## 分级提示

<details><summary>提示 1</summary>

用Fraction(原始字符串)读样本和中心，每个点分别到所有中心算精确平方距离。

</details>

<details><summary>提示 2</summary>

先拿到最小距离，不能在逐个扫描时累积容差误差。

</details>

<details><summary>提示 3</summary>

min_dist=min(distances)，用next找第一个dist≤min_dist+Fraction("1e-12")的索引；不要先转float，也不能改成只判断严格相等。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P042/exercise.py
.\.venv\Scripts\python.exe check.py P042
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P042/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P043/README.md) · [题解](../../../../solutions/P042.md)
