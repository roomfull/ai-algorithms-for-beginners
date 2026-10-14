# P039 KNN 近邻排序

每一行是一个样本，每一列是一个特征。对查询向量计算欧氏距离的平方 Σ(x_j-q_j)²；不必开根号，因为非负数开根号不改变大小顺序。按(距离平方, 原始下标)升序取前k个。下标从0开始。

## 输入与约束

第一行 n d k；接着n行，每行d个整数特征；最后一行d个整数查询特征。1≤k≤n≤100，1≤d≤10，特征绝对值≤10000。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

一行k个整数近邻下标，按距离从小到大排列。 输出使用十进制整数，不可带小数点。

## 样例

输入：
```text
3 2 2
1 0
-1 0
0 2
0 0
```
输出：
```text
0 1
```

手算：查询(0,0)到三点(1,0)、(-1,0)、(0,2)的距离平方是1、1、4。前两点平局按下标0、1；k=2，输出0 1。

## 分级提示

<details><summary>提示 1</summary>

先逐维作差并平方。

</details>

<details><summary>提示 2</summary>

给每个距离配上原始下标。

</details>

<details><summary>提示 3</summary>

排序键是(distance,index)，取排序列表[:k]，输出其中的index。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P039/exercise.py
.\.venv\Scripts\python.exe check.py P039
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P039/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P040/README.md) · [题解](../../../../solutions/P039.md)
