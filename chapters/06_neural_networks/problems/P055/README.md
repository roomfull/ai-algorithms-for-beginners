# P055 二维卷积：不翻转核的互相关

本题采用深度学习常用的互相关：核不翻转。输入四周补p层0，核每次移动s格。输出位置(i,j)为ΣX_padded[i*s+a,j*s+b]K[a,b]。只有一个输入通道与一个核，无偏置，无dilation。输出高H=(h+2p-kh)//s+1，宽W=(w+2p-kw)//s+1。

## 输入与约束

第一行 h w kh kw s p（全为整数）；接着h行输入，每行w项；接着kh行核，每行kw项。1≤h,w≤20，1≤kh,kw≤7，1≤s≤4，0≤p≤3，保证h+2p≥kh且w+2p≥kw；数据有限，绝对值≤10，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

H行输出矩阵，每行W个数；不另写尺寸。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
3 3 2 2 1 0
1 2 3
4 5 6
7 8 9
1 2
3 4
```
输出：
```text
37 47
67 77
```

手算：输入1..9排成3×3，核[[1,2],[3,4]]。左上=1×1+2×2+4×3+5×4=37；右上=47，左下=67，右下=77。核翻转会给另一个答案，因此必须保留核方向。

## 分级提示

<details><summary>提示 1</summary>

先算输出尺寸并创建零填充输入。

</details>

<details><summary>提示 2</summary>

输出位置(i,j)对应填充输入起点(i*s,j*s)。

</details>

<details><summary>提示 3</summary>

四重循环i,j,a,b累加padded[i*s+a][j*s+b]*kernel[a][b]，不要把kernel倒序。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P055/exercise.py
.\.venv\Scripts\python.exe check.py P055
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P055/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P056/README.md) · [题解](../../../../solutions/P055.md)
