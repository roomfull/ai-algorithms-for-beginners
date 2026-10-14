# P052 稳定 softmax

把每行c个分数变成类别概率：p_j=exp(z_j-m)/Σexp(z_t-m)，m=max(z)。减同一个常数不改变概率，但避免直接exp(1000)溢出。每行各自归一化，概率和为1。

## 输入与约束

第一行 n c；随后n行，每行c个logit分数。1≤n≤50，1≤c≤20；有限实数绝对值≤1000，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

n行概率矩阵，每行c项。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
2 2
0 1
999 1000
```
输出：
```text
0.26894142137 0.73105857863
0.26894142137 0.73105857863
```

手算：第一行z=(0,1)，减最大值得(-1,0)，exp值(e^-1,1)，概率约(0.26894142137,0.73105857863)。第二行(999,1000)减最大值后完全相同。

## 分级提示

<details><summary>提示 1</summary>

每行先取最大值。

</details>

<details><summary>提示 2</summary>

对减最大值后的分数取指数，再求指数总和。

</details>

<details><summary>提示 3</summary>

每行e=[exp(v-max(row))]，输出各e/sum(e)，不要把整矩阵一起归一化。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P052/exercise.py
.\.venv\Scripts\python.exe check.py P052
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P052/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P053/README.md) · [题解](../../../../solutions/P052.md)
