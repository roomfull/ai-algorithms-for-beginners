# P076 量化误差与理论存储字节

给定原值x与反量化值x_hat，计算MSE=Σ(x-x_hat)²/n与最大绝对误差max|x-x_hat|。再按FP32每项4字节、INT8每项1字节计算纯数组理论字节数；不计scale、零点、文件头、Python对象等元数据。

## 输入与约束

首行 n；第二行n个原值；第三行n个反量化值。1≤n≤1000；输入最大绝对值10000。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行 MSE max_abs_error 两个浮点；第二行 FP32_bytes INT8_bytes 两个整数。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
3
1 -2 3
1.5 -1 2
```
输出：
```text
0.75 1
12 3
```

误差[-0.5,-1,1]的平方[0.25,1,1]，MSE=2.25/3=0.75，最大绝对误差1。n=3所以理论数据字节12与3。

## 分级提示

<details><summary>提示 1</summary>

误差绝对值与误差平方是两种统计。

</details>

<details><summary>提示 2</summary>

MSE除以元素数n，不是除以worker数。

</details>

<details><summary>提示 3</summary>

用Fraction计算每项差、平方和/n与最大abs；字节直接4*n和n。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/08_compression/problems/P076/exercise.py
.\.venv\Scripts\python.exe check.py P076
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/08_compression/problems/P076/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/docs/stable/quantization.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P076.md) · [下一章](../../../09_distributed/README.md)
