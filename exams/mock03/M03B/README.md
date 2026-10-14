# M03B 逐行对称权重量化与重构误差

权重矩阵每行代表一个输出通道。用b位有符号对称量化，Q=2^(b−1)−1，只使用整数区间[−Q,Q]（不使用−2^(b−1)）。每行amax=max|w|，非零行scale=amax/Q，全零行scale=1。计算w/scale，四舍五入到最近整数，精确半格向远离0方向舍入，再裁剪到[−Q,Q]。反量化w_hat=q*scale；报告每行MSE=Σ(w−w_hat)²/c。原十进制字符串构造Fraction后精确计算比例与半格，不能用Python内置round的半偶规则。

## 输入与约束

首行 r c b；接着r行，每行c个十进制权重。1≤r≤20，1≤c≤20，2≤b≤8；权重绝对值≤100，最多3位小数。输入合法。仅单机数值模拟，不声称量化一定加速。

## 输出

第一行r个scale；接着r行量化整数（每行c个）；最后一行r个反量化MSE。整数矩阵行必须严格整数。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
2 3 3
-3 0 3
-1 0 1
```
输出：
```text
1 0.3333333333333333
-3 0 3
-3 0 3
0 0
```

手算：b=3，所以Q=3。第1行amax=3、scale=1，量化(−3,0,3)；第2行amax=1、scale=1/3，量化同为(−3,0,3)。两行反量化完全还原，MSE都是0。精确±0.5半格在其他案例中分别变为±1。

## 分级提示

<details><summary>提示 1</summary>

每行单独找amax并算scale。

</details>

<details><summary>提示 2</summary>

对绝对比例floor(t+1/2)，再恢复符号，避免负数向零截断。

</details>

<details><summary>提示 3</summary>

Fraction比例的分子p、分母q可用(2*p+q)//(2*q)实现非负半格向上；MSE用反量化值与原权重的平方差均值。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock03/M03B/exercise.py
.\.venv\Scripts\python.exe check.py M03B
.\.venv\Scripts\python.exe check.py --chapter M03
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock03/M03B/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://github.com/pytorch/pytorch/blob/main/torch/ao/quantization/observer.py)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M03B.md)
