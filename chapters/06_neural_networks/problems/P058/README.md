# P058 标量 GAN 损失与交替更新

生成器G(z)=a*z+g，判别器D(x)=sigmoid(w*x+b)。一条真实样本xr与一条噪声z。先固定G，用L_D=-ln D(xr)-ln(1-D(G(z)))=softplus(-u_r)+softplus(u_f)训练D（两项求和，不除2）。g_w=(p_r-1)*xr+p_f*G(z)，g_b=p_r-1+p_f；w,b同时减lrD乘梯度。然后固定新D，采用非饱和生成器损失L_G=-ln D_new(G(z))=softplus(-u_f_new)，g_a=(p_f_new-1)*w_new*z，g_g=(p_f_new-1)*w_new，再同时更新a,g。标准minimax生成器目标ln(1-D(G(z)))仅作概念比较，本题不采用它。

## 输入与约束

一行 xr z a g w b lrD lrG 共8个有限实数；前6项绝对值≤2，0<lrD,lrG≤1，最多6位小数。所有概率用稳定sigmoid，损失用softplus(t)=max(t,0)+ln(1+exp(-|t|))；不clip。不要求处理无效输入。

## 输出

第一行 L_D（D更新前） L_G（D更新后、G更新前）；第二行 a_new g_new w_new b_new。只执行一轮D→G。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
1 1 0 0 0 0 1 1
```
输出：
```text
1.38629436112 0.69314718056
0.25 0.25 0.5 0
```

手算：xr=z=1，a=g=w=b=0，学习率均1。fake=0，p_r=p_f=0.5，L_D=2ln2。D梯度g_w=-0.5,g_b=0，新w=0.5,b=0。新D在fake0的概率仍0.5，L_G=ln2；G梯度g_a=g_g=-0.25，所以新a=g=0.25。用旧w=0会错误地让G不更新。

## 分级提示

<details><summary>提示 1</summary>

D步中fake当作固定输入，不能顺便更新G。

</details>

<details><summary>提示 2</summary>

D同时更新后重新算fake的判别概率，再算G梯度。

</details>

<details><summary>提示 3</summary>

先保存old_fake=a*z+g；求D梯度并更新w,b；p_new=sigmoid(w_new*old_fake+b_new)，再算G梯度与更新。两个损失输出的计算时点不同。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P058/exercise.py
.\.venv\Scripts\python.exe check.py P058
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P058/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://arxiv.org/abs/1406.2661)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [后续学习路线](../../../../README.md) · [题解](../../../../solutions/P058.md)
