# M04A 卷积、ReLU 与平均池化特征

单通道图像先与方形核作valid互相关（CNN惯例的“卷积”，不翻转核）：步长1，无padding，结果加给定标量偏置；逐元素ReLU=max(0,z)；再作p×p平均池化，池化步长p，无padding，只保留完整窗口，多余的下边与右边丢弃。平均池化以ReLU后的全部p²个元素为分母，零也计入。输出最终特征矩阵。

## 输入与约束

首行 h w s p；接着h行图像（每行w个数）；接着s行核（每行s个数）；最后一行偏置。1≤h,w≤20，1≤s≤min(h,w)，1≤p≤min(h−s+1,w−s+1)；数值绝对值≤100，最多3位小数。输入合法。

## 输出

第一行最终行数 floor((h−s+1)/p) 和列数 floor((w−s+1)/p)，严格整数；随后按行输出池化浮点矩阵。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
3 3 2 2
1 2 3
4 5 6
7 8 9
1 0
0 -1
5
```
输出：
```text
1 1
1
```

手算：核左上1、右下−1，valid四个位置都是左上值减右下值=−4。加偏置5得到四个1，ReLU仍为1；p=2，四值平均为1，最终尺寸1 1。

## 分级提示

<details><summary>提示 1</summary>

先算valid结果大小h−s+1、w−s+1。

</details>

<details><summary>提示 2</summary>

每个窗口按原核顺序点乘累加，加偏置后立即ReLU。

</details>

<details><summary>提示 3</summary>

对池化输出位置(i,j)，取激活矩阵起点(i*p,j*p)的p×p窗口，求和除p*p。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock04/M04A/exercise.py
.\.venv\Scripts\python.exe check.py M04A
.\.venv\Scripts\python.exe check.py --chapter M04
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock04/M04A/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M04A.md)
