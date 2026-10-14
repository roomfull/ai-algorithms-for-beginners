# P040 单样本 KNN 多数投票

分类是根据带标签的训练样本预测类别。先按P039规则选择k个邻居，再统计整数标签的票数。票数相等时取数值最小的标签，不按最近邻标签决胜。

## 输入与约束

第一行 n d k；接着n行，每行先整数标签，再d个整数特征；最后d个查询特征。1≤k≤n≤100，1≤d≤10，特征绝对值≤10000，标签为[-100,100]整数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

一行一个整数预测标签。 输出使用十进制整数，不可带小数点。

## 样例

输入：
```text
3 1 2
9 1
2 -1
9 3
0
```
输出：
```text
2
```

手算：到0的三个点是1、-1、3，距离平方1、1、9，标签分别9、2、9。k=2选下标0和1，各一票，较小标签2胜出。

## 分级提示

<details><summary>提示 1</summary>

选择邻居与投票是两个步骤。

</details>

<details><summary>提示 2</summary>

字典counts[label]保存票数。

</details>

<details><summary>提示 3</summary>

在出现的标签中最小化(-counts[label],label)。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P040/exercise.py
.\.venv\Scripts\python.exe check.py P040
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P040/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P041/README.md) · [题解](../../../../solutions/P040.md)
