# P074 对称int8量化与反量化

把浮点权重映射到整数[-127,127]。scale=max(abs(x))/127；全零向量规定scale=1。q=clip(round(x/scale),-127,127)，反量化x_hat=q*scale。round使用ties-to-even：恰处两整数中间时选偶数。

## 输入与约束

首行 n；第二行n个权重。1≤n≤1000。用原始小数字符串构造Fraction，精确计算scale和x/scale后round；输出scale与反量化值可转float。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行scale浮点；第二行n个整数q；第三行n个反量化浮点值。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
8
127 -127 0.5 1.5 2.5 -0.5 -1.5 0
```
输出：
```text
1
127 -127 0 2 2 0 -2 0
127 -127 0 2 2 0 -2 0
```

最大绝对值127，scale=1；±127映射原值，0.5→0，1.5→2，2.5→2，-0.5→0，-1.5→-2。ties-to-even不是一律四舍五入远离0。

## 分级提示

<details><summary>提示 1</summary>

先找maxabs，零向量需单独规定scale。

</details>

<details><summary>提示 2</summary>

round(Fraction)可以精确实现ties-to-even；不要先把比值转float。

</details>

<details><summary>提示 3</summary>

scale=maxabs/Fraction(127)或Fraction(1)；q=max(-127,min(127,round(x/scale)))；dequant=q*scale。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/08_compression/problems/P074/exercise.py
.\.venv\Scripts\python.exe check.py P074
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/08_compression/problems/P074/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/docs/stable/quantization.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P074.md) · [下一题](../P075/README.md)
