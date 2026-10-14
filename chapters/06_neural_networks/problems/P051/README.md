# P051 全连接层与 ReLU

矩阵X形状n×d，n是样本数，d是输入维数；W形状d×o，o是输出神经元数；b有o项。先做Z=XW+b，每行都加同一b；再做ReLU(z)=max(0,z)。本题只有前向计算，负数变0，正数保留。

## 输入与约束

第一行 n d o；随后n行X，每行d项；随后d行W，每行o项；最后一行o个偏置。1≤n,d,o≤20，全部有限实数绝对值≤10，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

n行ReLU输出，每行o项。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
2 2 2
1 2
-1 3
1 -1
2 0
0 1
```
输出：
```text
5 0
5 2
```

手算：X两行(1,2)、(-1,3)，W两行(1,-1)、(2,0)，b=(0,1)。第一行Z=(1×1+2×2,1×(-1)+2×0+1)=(5,0)；第二行为(5,2)。ReLU后不变。

## 分级提示

<details><summary>提示 1</summary>

先检查n×d乘d×o会得到n×o。

</details>

<details><summary>提示 2</summary>

每个输出z[i][j]遍历输入维t累加X[i][t]*W[t][j]。

</details>

<details><summary>提示 3</summary>

三层循环算内积，加b[j]一次，再max(0,z)。无需实现矩阵库。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P051/exercise.py
.\.venv\Scripts\python.exe check.py P051
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P051/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P052/README.md) · [题解](../../../../solutions/P051.md)
