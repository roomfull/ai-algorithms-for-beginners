# P071 绝对值阈值剪枝

把权重向量中绝对值严格小于阈值t的项置0；等于阈值的项保留。剪枝只是改变数值，普通稠密存储的元素数量仍是n。

## 输入与约束

首行 n t；第二行n个权重。1≤n≤1000，0≤t≤10000。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

一行n个剪枝后的浮点权重，位置不变。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
5 1
0.5 -1 1 2 -0.2
```
输出：
```text
0 -1 1 2 0
```

阈值1：|0.5|和|-0.2|小于1置0；-1和1恰等阈值保留；2也保留。

## 分级提示

<details><summary>提示 1</summary>

先取绝对值再比较。

</details>

<details><summary>提示 2</summary>

判断是严格小于，不能写成小于等于。

</details>

<details><summary>提示 3</summary>

依次输出0 if abs(x)<t else x；用Fraction从原始字符串读入可让小数边界精确。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/08_compression/problems/P071/exercise.py
.\.venv\Scripts\python.exe check.py P071
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/08_compression/problems/P071/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P071.md) · [下一题](../P072/README.md)
