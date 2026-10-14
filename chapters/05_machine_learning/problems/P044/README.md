# P044 完整 Lloyd 迭代

从给定中心开始，每轮先按P042规则分配，再按P043规则更新。若所有中心的坐标最大绝对变化≤tol，提前停止；否则至多执行max_iter轮。最终必须再按最终中心分配一次，输出标签配合这些中心；即使达到轮数上限也要重分配。

## 输入与约束

第一行 n d c max_iter tol；随后n行样本、c行初始中心。n,d,c和数值范围同P042，1≤max_iter≤100，0≤tol≤1；tol有限实数。 所有尺寸和标签均严格输入整数；不要求处理无效输入。

## 输出

先c行最终中心，每行d个数；最后一行n个整数最终标签。 浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。 整数标签/索引单独一行，严格输出十进制整数。

## 样例

输入：
```text
4 1 2 10 0
0
2
8
10
0
10
```
输出：
```text
1
9
0 0 1 1
```

手算：点0、2、8、10，初始中心0、10。分配0 0 1 1；更新得1、9。再分配仍相同，更新无变化停止；最终中心1、9，标签0 0 1 1。

## 分级提示

<details><summary>提示 1</summary>

组合分配函数与更新函数。

</details>

<details><summary>提示 2</summary>

保留旧中心，计算更新前后的最大坐标变化。

</details>

<details><summary>提示 3</summary>

每轮assign→update→判停，循环后再assign最终中心；不要输出上一轮旧中心对应的标签。

</details>

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P044/exercise.py
.\.venv\Scripts\python.exe check.py P044
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/05_machine_learning/problems/P044/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考](https://github.com/ddbourgin/numpy-ml)。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P045/README.md) · [题解](../../../../solutions/P044.md)
