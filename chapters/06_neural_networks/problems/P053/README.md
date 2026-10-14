# P053 BCE 与多分类交叉熵

输入的是概率。二分类先p←min(1-eps,max(eps,p))，算平均[-y ln p-(1-y)ln(1-p)]。多分类每行真实类别为t，只取它的概率p_t做同样clip，算平均[-ln p_t]；不重新归一化clip后的概率。本题clip上界也用于多分类，真实类概率1会产生很小正损失。

## 输入与约束

第一行 n c eps；随后n行，每行二分类整数标签(0/1)与p；再n行，每行真实整数类别[0,c-1]与c个概率。1≤n≤50，1≤c≤10，1e-12≤eps≤0.01；概率有限且在[0,1]，多分类每行概率和与1误差≤1e-9。概率最多6位小数，eps可用科学记数法。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

一行 平均BCE 平均多分类交叉熵。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
2 2 0.000001
1 0.8
0 0.6
0 0.8 0.2
1 0.25 0.75
```
输出：
```text
0.569717141594 0.255412811883
```

手算：二分类(1,0.8)、(0,0.6)：正确类别概率分别0.8、0.4，BCE=-(ln0.8+ln0.4)/2≈0.569717142。多分类真实类概率0.8、0.75，CE=-(ln0.8+ln0.75)/2≈0.255412812。eps=1e-6未触发clip。

## 分级提示

<details><summary>提示 1</summary>

先clip，再log，别对0取log。

</details>

<details><summary>提示 2</summary>

多分类只取真实类别索引对应概率。

</details>

<details><summary>提示 3</summary>

对n行二分类分别求-y*log(p)-(1-y)*log1p(-p)，平均；多分类累加-log(clip(probs[target]))后除n。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P053/exercise.py
.\.venv\Scripts\python.exe check.py P053
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P053/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P054/README.md) · [题解](../../../../solutions/P053.md)
