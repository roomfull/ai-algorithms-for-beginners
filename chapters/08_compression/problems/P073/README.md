# P073 按行L1范数结构化剪枝

矩阵的每一行看作一个整体，L1范数为该行所有元素绝对值之和。保留范数最大的keep行；范数相同则较小索引优先保留。结果保留行按原行顺序输出。

## 输入与约束

首行 rows cols keep；随后rows行，每行cols个权重。1≤rows,cols≤100，0≤keep≤rows。 保证输入合法。 行索引从0开始。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行rows个0/1掩码，1表示保留。后续恰好keep行输出保留的原始行，按索引升序；keep=0时仅输出掩码一行。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
3 2 2
1 -2
3 0
2 2
```
输出：
```text
1 0 1
1 -2
2 2
```

三行范数是3、3、4，keep=2先留索引2，再在并列3中留索引0。掩码1 0 1，按原顺序输出行0、行2。

## 分级提示

<details><summary>提示 1</summary>

行L1是绝对值之和，不是普通和。

</details>

<details><summary>提示 2</summary>

用(-norm,index)排序，选前keep个。

</details>

<details><summary>提示 3</summary>

selected=set(order[:keep])；先打印掩码，再按原索引扫描只打印selected中的行。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/08_compression/problems/P073/exercise.py
.\.venv\Scripts\python.exe check.py P073
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/08_compression/problems/P073/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P073.md) · [下一题](../P074/README.md)
