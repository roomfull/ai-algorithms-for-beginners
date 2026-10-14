# P046 二分类交叉熵与一轮梯度

损失衡量预测与标签差距。二分类交叉熵L=平均[-y ln p-(1-y)ln(1-p)]；ln为自然对数。为避免p舍入成0/1，直接用等价的logit公式：每样本softplus(z)-y z，其中softplus(z)=max(z,0)+ln(1+exp(-|z|))。梯度g_w=平均[(p-y)x]，g_b=平均[p-y]。只求当前损失和梯度，不更新。

## 输入与约束

第一行 n d；随后n行，每行整数标签y(0/1)+d个实数特征；一行d个权重，最后一行偏置。尺寸及实数范围同P045。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

第一行平均损失L，第二行d个权重梯度，第三行偏置梯度。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
2 1
0 0
1 2
0
0
```
输出：
```text
0.69314718056
-0.5
0
```

手算：两条样本(y,x)=(0,0)、(1,2)，w=b=0，所以p均0.5，L=ln2。残差p-y为0.5、-0.5；g_w=(0.5×0-0.5×2)/2=-0.5；g_b=0。

## 分级提示

<details><summary>提示 1</summary>

对每行算z、p和残差p-y。

</details>

<details><summary>提示 2</summary>

所有样本的损失和梯度都要除n。

</details>

<details><summary>提示 3</summary>

用稳定softplus计算损失；g_w[j]=Σ(residual*x[j])/n，g_b=Σresidual/n。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P046/exercise.py
.\.venv\Scripts\python.exe check.py P046
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P046/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P047/README.md) · [题解](../../../../solutions/P046.md)
