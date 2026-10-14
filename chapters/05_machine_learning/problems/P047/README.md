# P047 完整逻辑回归梯度下降

从输入初值开始执行steps轮全批量梯度下降。每轮用所有样本在旧参数处计算P046的平均梯度，然后同时更新w←w-lr*g_w、b←b-lr*g_b。学习率lr控制每次沿降低损失方向走多远。执行固定轮数，无正则、无随机、无提前停止。最后输出更新后参数和重新计算的最终损失。

## 输入与约束

第一行 n d steps lr；随后n行 标签(0/1)+d个特征；一行d个初始权重，一行初始偏置。1≤n≤100，1≤d≤10，0≤steps≤200，0<lr≤1；特征与初始参数有限且绝对值≤10，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

第一行d个最终权重，第二行最终偏置，第三行最终平均损失（稳定logit形式）。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
2 1 1 1
0 0
1 2
0
0
```
输出：
```text
0.5
0
0.503204434039
```

手算：沿P046两条样本，初始w=b=0、lr=1、steps=1：g_w=-0.5、g_b=0，更新w=0.5、b=0。最终z=0、1，损失(ln2+ln(1+exp(-1)))/2≈0.503204434。

## 分级提示

<details><summary>提示 1</summary>

每轮先积累整批梯度，再改参数。

</details>

<details><summary>提示 2</summary>

复用同一套稳定sigmoid与softplus公式。

</details>

<details><summary>提示 3</summary>

循环steps次，旧w、b产生整批residual；所有g除n；同时减lr*g。最后再前向算损失。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P047/exercise.py
.\.venv\Scripts\python.exe check.py P047
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P047/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P048/README.md) · [题解](../../../../solutions/P047.md)
