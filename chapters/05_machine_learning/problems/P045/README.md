# P045 逻辑回归 sigmoid 预测

权重w与偏置b已经给定；先算分数z=Σw_j x_j+b，再算p=1/(1+exp(-z))，表示类别1概率；p≥0.5预测1，否则0。此题只预测，不训练。为防exp溢出，z≥0用常见式，z<0用exp(z)/(1+exp(z))。

## 输入与约束

第一行 n d；随后n行d个实数特征，一行d个权重，最后一行偏置。1≤n≤100，1≤d≤10；特征、权重、偏置均有限且绝对值≤10，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

共2n行；每个样本先单独一行概率p，再单独一行整数预测标签，按样本顺序。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。 整数标签/索引单独一行，严格输出十进制整数。

## 样例

输入：
```text
3 1
0
1
-1
1
0
```
输出：
```text
0.5
1
0.73105857863
1
0.26894142137
0
```

手算：w=1，b=0。x=0、1、-1给z=0、1、-1，p分别0.5、约0.73105857863、约0.26894142137。0.5也归标签1。

## 分级提示

<details><summary>提示 1</summary>

先算内积并加偏置。

</details>

<details><summary>提示 2</summary>

sigmoid要分正负分支，尤其z=-1100。

</details>

<details><summary>提示 3</summary>

z≥0返回1/(1+exp(-z))；否则e=exp(z)后返回e/(1+e)，用p≥0.5判断标签。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P045/exercise.py
.\.venv\Scripts\python.exe check.py P045
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P045/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P046/README.md) · [题解](../../../../solutions/P045.md)
