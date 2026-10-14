# P048 熵与 Gini 不纯度

标签比例p_c=count_c/n。熵H=-Σp_c log2(p_c)，Gini=1-Σp_c²。熵这里用以2为底的对数，而交叉熵题用自然对数。纯标签集合两者都是0；越混杂通常数值越大，但两者数值不能直接混用。只遍历实际出现的标签，0 log0按0处理。

## 输入与约束

一行n个整数标签，无单独n。1≤n≤200，标签[-100,100]。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

一行 熵H Gini。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
0 0 1 1
```
输出：
```text
1 0.5
```

手算：0 0 1 1中两类各一半。H=-2×(1/2)log2(1/2)=1；Gini=1-2×(1/2)²=0.5。

## 分级提示

<details><summary>提示 1</summary>

先计每类数量。

</details>

<details><summary>提示 2</summary>

用n把计数转为比例，math.log2求熵。

</details>

<details><summary>提示 3</summary>

只枚举counts.values()中的正计数，累加-p*log2(p)，再算1-Σp²。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P048/exercise.py
.\.venv\Scripts\python.exe check.py P048
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P048/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P049/README.md) · [题解](../../../../solutions/P048.md)
