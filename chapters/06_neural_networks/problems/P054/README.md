# P054 单层 sigmoid 网络梯度更新

一个输出神经元z=w·x+b，激活p=sigmoid(z)，损失用未clip的稳定logit BCE。链式规则把损失对p的导数乘p对z的导数，得到∂L/∂z=p-y；再乘z对w_j的导数x_j得到权重梯度。用整批平均梯度执行一次w←w-lr*g_w、b←b-lr*g_b，所有参数同时更新。

## 输入与约束

第一行 n d lr；随后n行，每行整数标签y(0/1)+d个实数特征；再一行d个初始权重、一行初始偏置。1≤n≤100，1≤d≤10，0<lr≤1，特征和初始参数有限且绝对值≤10，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

第一行更新前的平均损失，第二行d个更新后权重，第三行更新后偏置。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
1 2 0.1
1 2 -4
0 0
0
```
输出：
```text
0.69314718056
0.1 -0.2
0.05
```

手算：一条正样本x=(2,-4)，旧w=(0,0)、b=0，p=0.5，损失ln2。残差-0.5，权重梯度(-1,2)，偏置梯度-0.5；lr=0.1更新w=(0.1,-0.2)、b=0.05。

## 分级提示

<details><summary>提示 1</summary>

这个单层网络与逻辑回归数学相同。

</details>

<details><summary>提示 2</summary>

先用旧参数计算所有梯度，全部平均。

</details>

<details><summary>提示 3</summary>

dw[j]=Σ((p-y)*x[j])/n，db=Σ(p-y)/n；返回旧损失和w-lr*dw、b-lr*db。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P054/exercise.py
.\.venv\Scripts\python.exe check.py P054
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P054/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P055/README.md) · [题解](../../../../solutions/P054.md)
