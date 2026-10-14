# P075 仿射uint8量化与截断

给定正scale和整数zero_point，把权重量化到[0,255]：先求round(x/scale)（ties-to-even），再加zero_point，最后截断。反量化为(q-zero_point)*scale。顺序是本题契约，不能改成round(x/scale+zero_point)，奇数zero_point时半格结果可能不同。

## 输入与约束

首行 n scale zero_point；第二行n个权重。1≤n≤1000，0<scale≤10000，0≤zero_point≤255。从原小数字符串用Fraction计算x/scale和round。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行n个整数q；第二行n个反量化浮点值。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
5 0.5 128
-1 -0.5 0 0.5 1
```
输出：
```text
126 127 128 129 130
-1 -0.5 0 0.5 1
```

scale=0.5，zero_point=128；比值[-2,-1,0,1,2]加128变成[126,127,128,129,130]，均未截断，反量化还原输入。

## 分级提示

<details><summary>提示 1</summary>

反量化先减zero_point。

</details>

<details><summary>提示 2</summary>

小于0设0，大于255设255。

</details>

<details><summary>提示 3</summary>

q=max(0,min(255,round(Fraction(x)/Fraction(scale))+zp))，再算(q-zp)*scale。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/08_compression/problems/P075/exercise.py
.\.venv\Scripts\python.exe check.py P075
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/08_compression/problems/P075/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/docs/stable/quantization.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P075.md) · [下一题](../P076/README.md)
