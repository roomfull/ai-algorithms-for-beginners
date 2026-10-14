# P056 CNN 前向：卷积、ReLU、最大池化

先按P055做互相关并加标量偏置b，逐元素做ReLU，然后最大池化。池化窗口ph×pw，移动ps格，只取窗口最大数，不乘权重，不padding。卷积尺寸H,W同P055；池化输出高(H-ph)//ps+1、宽(W-pw)//ps+1。只计算前向，不训练。

## 输入与约束

第一行 h w kh kw s p ph pw ps（整数）；随后h行输入、kh行核，最后一行偏置b。卷积范围同P055，1≤ph,pw,ps≤4；保证H≥ph,W≥pw；b有限且绝对值≤10，其他数值范围同P055。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

只输出最终池化矩阵，不输出中间矩阵或尺寸。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
2 2 1 1 1 0 2 2 2
-1 2
3 -4
1
0
```
输出：
```text
3
```

手算：输入[[-1,2],[3,-4]]，1×1核为1，偏置0，卷积原样；ReLU得到[[0,2],[3,0]]；2×2池化取max(0,2,3,0)=3。

## 分级提示

<details><summary>提示 1</summary>

先做完整卷积矩阵，再做激活和池化。

</details>

<details><summary>提示 2</summary>

ReLU在池化之前，偏置在ReLU之前。

</details>

<details><summary>提示 3</summary>

pool[i][j]=max(relu[i*ps+a][j*ps+b])，a范围ph、b范围pw；卷积stride s与池化stride ps分别使用。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P056/exercise.py
.\.venv\Scripts\python.exe check.py P056
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/06_neural_networks/problems/P056/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P057/README.md) · [题解](../../../../solutions/P056.md)
