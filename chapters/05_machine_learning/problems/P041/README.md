# P041 多查询 KNN 分类

对q个查询分别做近邻排序与多数投票，训练数据保持不变；查询没有已知标签，也不能加入训练集。距离平局按下标，投票平局取最小整数标签。

## 输入与约束

第一行 n d k q；随后n行标签+d个整数特征；再q行d个整数查询特征。1≤k≤n≤100，1≤d≤10，1≤q≤30，坐标绝对值≤10000，标签[-100,100]整数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

q行，每行一个整数预测标签，顺序与查询一致。 输出使用十进制整数，不可带小数点。

## 样例

输入：
```text
2 1 1 3
2 0
5 10
1
9
5
```
输出：
```text
2
5
2
```

手算：训练点0标签2，点10标签5；k=1。查询1最近0得2，查询9最近10得5，查询5等距离，先下标0得2。

## 分级提示

<details><summary>提示 1</summary>

对每个查询重复P040。

</details>

<details><summary>提示 2</summary>

每次查询新建票数字典。

</details>

<details><summary>提示 3</summary>

外层遍历queries；内部计算距离排序、取k个、计票，再追加预测。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P041/exercise.py
.\.venv\Scripts\python.exe check.py P041
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P041/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P042/README.md) · [题解](../../../../solutions/P041.md)
