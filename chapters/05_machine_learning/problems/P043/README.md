# P043 K-means 更新中心与空簇

给定分配标签，非空簇中心改成该簇各维的算术平均；空簇保留旧中心，不产生NaN。这里不重新分配样本。

## 输入与约束

第一行 n d c；随后n行d个实数样本、c行d个旧中心；最后一行n个整数分配标签[0,c-1]。1≤n≤100，1≤d≤10，1≤c≤10，有限实数绝对值≤100，最多6位小数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

c行新中心，每行d个浮点数，按簇编号顺序。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。

## 样例

输入：
```text
3 1 3
0
2
9
0
10
20
0 0 1
```
输出：
```text
1
9
20
```

手算：点0、2归簇0，点9归簇1，簇2为空。旧中心0、10、20；新中心(0+2)/2=1、9、20。

## 分级提示

<details><summary>提示 1</summary>

每簇保存计数与逐维总和。

</details>

<details><summary>提示 2</summary>

计数为0时拷贝旧中心。

</details>

<details><summary>提示 3</summary>

非空中心sum/count；遍历0到c-1，不能只遍历出现的标签。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P043/exercise.py
.\.venv\Scripts\python.exe check.py P043
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P043/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P044/README.md) · [题解](../../../../solutions/P043.md)
