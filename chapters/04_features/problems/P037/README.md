# P037 相邻卡方合并分箱

给定按数值递增的初始箱，每箱有0类和1类计数。对每对相邻箱构成2×2列联表，按P036的未修正Pearson公式算χ²，期望为0项贡献0。每轮合并χ²最小的一对；精确相等时选最左一对。合并后左界取左箱左界，右界取右箱右界，两类计数相加；重新计算所有邻对，直到剩 t 箱。这是明确定义的教学变体，不宣称任何库的唯一默认算法。

## 输入与约束

首行 b t；随后 b 行：value count0 count1。1≤b≤200，1≤t≤b；value为严格递增互异整数，绝对值≤1000000；两类计数为0到1000000的整数。初始左右界均为value。

## 输出

按从左到右输出 t 行：left right count0 count1，四个整数；不输出箱数。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
3 2
1 1 1
2 2 2
3 8 0
```
输出：
```text
1 2 3 3
3 3 8 0
```

手算：箱1计数(1,1)，箱2(2,2)，箱3(8,0)。邻对1/2的期望等于观察，χ²=0；邻对2/3行和4、8，列和10、2，总数12，四格贡献8/15、8/3、4/15、4/3，合计24/5=4.8。合并最左对后箱为边界 `[1,2]`、计数(3,3)，以及边界 `[3,3]`、计数(8,0)，已到2箱，输出这两行。

## 分级提示

<details><summary>提示 1</summary>

用 [left,right,count0,count1] 保存一个箱。

</details>

<details><summary>提示 2</summary>

每轮扫描所有相邻对，严格小于当前最优时更新位置，等于时不更新。

</details>

<details><summary>提示 3</summary>

借用2×2公式但在同一文件独立实现；用Fraction保持并列精确，合并列表中best与best+1，下一轮重新扫描。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P037/exercise.py
.\.venv\Scripts\python.exe check.py P037
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P037/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.chi2_contingency.html)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P038/README.md) · [题解](../../../../solutions/P037.md)
