# P050 小型 CART 分类树训练与预测

在当前节点递归用P049规则挑最佳切分。根深度0；达到max_depth、标签纯、无候选、或Gini降低≤1e-12时，成为叶节点。叶节点预测当前训练标签的多数类，票数平局取最小整数标签。否则按≤阈值和>阈值分出两支并递归。查询从根逐层走到叶，不只训练一层。无剪枝、无随机特征。 特征、阈值与查询的大小关系按输入十进制数精确比较；用Fraction从原字符串读取，中点仍保持Fraction，不对x≤阈值的边界加容差。1e-12只用于Gini评分并列/增益判断。

## 输入与约束

第一行 n d q max_depth；随后n行整数标签+d个实数特征，再q行d个查询特征。1≤n≤50，1≤d≤5，1≤q≤30，0≤max_depth≤8，标签[-100,100]，有限特征绝对值≤100，最多6位小数。候选评分并列容差、特征/阈值次序同P049。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

q行，每行一个整数预测标签。 输出使用十进制整数，不可带小数点。

## 样例

输入：
```text
6 1 3 2
0 0
0 1
1 2
1 3
0 4
0 5
-1
2.5
5
```
输出：
```text
0
1
0
```

手算：训练x=0..5、标签0 0 1 1 0 0。根最佳阈值1.5与3.5同分，取1.5；左支纯0，右支再以3.5分成纯1和纯0。max_depth=2时查询-1、2.5、5输出0、1、0。

## 分级提示

<details><summary>提示 1</summary>

写train(rows,depth)，返回叶标签或分裂节点。

</details>

<details><summary>提示 2</summary>

先判断停止条件，再选分裂，左右递归深度加1。

</details>

<details><summary>提示 3</summary>

最佳评分与父Gini差≤1e-12就返回多数叶；否则保存(feature,threshold,left,right)，predict按x[feature]≤threshold走左支。 特征、查询、中点都用Fraction，边界判断保持精确。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P050/exercise.py
.\.venv\Scripts\python.exe check.py P050
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P050/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://scikit-learn.org/stable/modules/tree.html)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [后续学习路线](../../../../README.md) · [题解](../../../../solutions/P050.md)
