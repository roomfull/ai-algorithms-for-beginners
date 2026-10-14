# P028 确定性类别过采样

二分类标签为0或1。保留全部原样本，再先补标签0、后补标签1到指定目标数。每类从其原始样本列表的第一个开始循环复制，不使用新复制的样本作为循环列表。

## 输入与约束

首行 n d target0 target1；随后 n 行：标签与 d 个整数特征。2≤n≤200，1≤d≤20；两类都至少1条；各 target 在该类原始数到500之间，特征绝对值≤1000000。

## 输出

首行输出总数 target0+target1，其后输出原样本及按规则追加的样本，每行先标签再特征。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
3 1 3 2
0 10
1 20
0 30
```
输出：
```text
5
0 10
1 20
0 30
0 10
1 20
```

手算：原0类有10和30，目标3，追加10；原1类有20，目标2，追加20。先输出原3行，再追加0 10和1 20，共5行。

## 分级提示

<details><summary>提示 1</summary>

分别记录两类原样本，保持各自输入顺序。

</details>

<details><summary>提示 2</summary>

还需增加 target-原数 条；第 r 条复制原列表 r % 原数 位置。

</details>

<details><summary>提示 3</summary>

先复制原输出列表，再按类0、类1循环补足；首行输出最终行数。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P028/exercise.py
.\.venv\Scripts\python.exe check.py P028
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/03_preprocessing/problems/P028/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://imbalanced-learn.org/stable/over_sampling.html#sample-generation)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P029/README.md) · [题解](../../../../solutions/P028.md)
