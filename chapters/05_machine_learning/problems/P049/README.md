# P049 连续特征的最佳二叉切分

对每个特征，将不同值升序排列，相邻不同值的中点作为阈值t。左支x_j≤t，右支x_j>t；评分为(|L|Gini(L)+|R|Gini(R))/n。先找所有候选评分最小值m，再在评分≤m+1e-12的候选中按特征索引、阈值升序取第一项。此题返回最佳候选，即使增益为0；没有候选才输出哨兵。

## 输入与约束

第一行 n d；接着n行，每行整数标签+d个实数特征。1≤n≤50，1≤d≤5，标签[-100,100]，有限特征绝对值≤100且最多6位小数。不同值比较不加容差，中点用(a+b)/2。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

第一行整数特征索引(从0开始)，第二行 阈值 加权Gini。所有特征恒定而无法分裂时输出-1，第二行0和父节点Gini。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。 整数标签/索引单独一行，严格输出十进制整数。

## 样例

输入：
```text
4 1
0 0
0 1
1 2
1 3
```
输出：
```text
0
1.5 0
```

手算：一维x=0、1、2、3，标签0、0、1、1。候选t=0.5、1.5、2.5；t=1.5得到两边纯标签，加权Gini=0，为最佳；特征编号0。

## 分级提示

<details><summary>提示 1</summary>

先用sorted(set(...))取得每个特征的不同值。

</details>

<details><summary>提示 2</summary>

每个中点都分别构造左右标签，计算加权Gini。

</details>

<details><summary>提示 3</summary>

存候选(score,feature,threshold)，找全局最小score；筛score≤min+1e-12，再按(feature,threshold)选第一项。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P049/exercise.py
.\.venv\Scripts\python.exe check.py P049
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P049/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://scikit-learn.org/stable/modules/tree.html)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P050/README.md) · [题解](../../../../solutions/P049.md)
