# M01A 训练集标准化后的 KNN 分类

传感器两种量纲可能差异很大。仅用训练集逐列拟合均值 μ 与总体方差 v=Σ(x−μ)²/n，非恒定列作 Z-score：(x−μ)/√v。查询使用同一组统计量，不能加入训练集。恒定列以原字符串精确判断，训练与查询都置0（忽略此列）。按标准化欧氏距离平方选 k 个近邻，再以无权多数票分类。距离数学上相等时取训练下标较小者；标签票数相等时取数值较小者。

## 输入与约束

首行 n d k；接着 n 行，每行 d 个十进制特征和1个整数标签；最后一行 d 个查询特征。1≤k≤n≤30，1≤d≤8；特征绝对值≤100，最多3位小数；标签绝对值≤100。输入合法。

## 输出

第一行 k 个近邻下标（0起）；第二行预测整数标签。两行均严格输出整数。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
3 2 1
0 0 9
2 100 3
4 0 7
2 0
```
输出：
```text
0
9
```

手算：样例均值=(2,100/3)，总体方差=(8/3,20000/9)。查询(2,0)，标准化后与三点的距离平方依次为1.5、4.5、1.5，故 k=1 取下标0，标签9。恒定列不参与距离。

## 分级提示

<details><summary>提示 1</summary>

统计量只从训练集取得。

</details>

<details><summary>提示 2</summary>

查询与样本均减同一个均值，作差后均值抵消；距离平方可写成Σ(x−q)²/v。

</details>

<details><summary>提示 3</summary>

从原字符串构造Fraction计算总体方差和距离，再按(distance,index)排序；Counter计票后按(-票数,标签)选标签。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock01/M01A/exercise.py
.\.venv\Scripts\python.exe check.py M01A
.\.venv\Scripts\python.exe check.py --chapter M01
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock01/M01A/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M01A.md)
