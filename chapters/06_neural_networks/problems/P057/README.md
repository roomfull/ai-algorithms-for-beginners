# P057 二维转置卷积：散射累加

输出先全0；每个输入X[i,j]把X[i,j]K[a,b]加到输出(i*s-p+a,j*s-p+b)，越界项丢弃。重叠位置必须累加。输出高H=(h-1)s-2p+kh，宽W=(w-1)s-2p+kw；本题dilation=1、output_padding=0、无偏置。它是同核互相关线性算子的转置，在尺寸匹配时满足内积恒等式；一般不是卷积逆运算。

## 输入与约束

第一行 h w kh kw s p（整数）；接着h行输入、kh行核。1≤h,w≤20，1≤kh,kw≤7，1≤s≤4，0≤p≤3；保证H,W≥1；输入与核有限且绝对值≤10，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

H行输出，每行W个数，不另写尺寸。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
2 2 2 2 1 0
1 2
3 4
1 2
3 4
```
输出：
```text
1 4 4
6 20 16
9 24 16
```

手算：输入[[1,2],[3,4]]、核[[1,2],[3,4]]、s=1,p=0，输出3×3。中心收到1×4+2×3+3×2+4×1=20。四角分别1、4、9、16；其余累加得到[[1,4,4],[6,20,16],[9,24,16]]。

## 分级提示

<details><summary>提示 1</summary>

先按公式建输出，不能照抄普通卷积输出尺寸。

</details>

<details><summary>提示 2</summary>

遍历输入，把一个缩放的核散射到输出。

</details>

<details><summary>提示 3</summary>

r=i*s-p+a，c=j*s-p+b；若0≤r<H且0≤c<W，out[r][c]+=x[i][j]*kernel[a][b]。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P057/exercise.py
.\.venv\Scripts\python.exe check.py P057
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P057/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://docs.pytorch.org/docs/stable/generated/torch.nn.ConvTranspose2d.html)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P058/README.md) · [题解](../../../../solutions/P057.md)
