# P072 按比例剪掉最小绝对值

计算k=floor(n*ratio)，按(abs(weight),index)升序选择恰好k个位置置0。并列时较小索引先剪。掩码1表示保留，0表示被选中剪掉；原值本来是0但未选中仍可有掩码1。

## 输入与约束

首行 n ratio；第二行n个权重。1≤n≤1000，0≤ratio≤1；ratio为十进制字符串，应按其精确值计算floor。 保证输入合法。 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

第一行n个0/1保留掩码；第二行n个剪枝后权重。 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
5 0.4
3 1 0 -1 2
```
输出：
```text
1 0 0 1 1
3 0 0 -1 2
```

n=5，ratio=0.4，k=2。绝对值最小的索引2（0）先剪，其次索引1（1）；索引3（-1）并列但更靠后保留。

## 分级提示

<details><summary>提示 1</summary>

先算要剪几个，再排序位置。

</details>

<details><summary>提示 2</summary>

用Fraction(ratio_token)保留比例的精确十进制值。

</details>

<details><summary>提示 3</summary>

k=int(n*Fraction(token))；idx=sorted(range(n),key=lambda i:(abs(x[i]),i))[:k]；更新mask。

</details>

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\.venv\Scripts\python.exe chapters/08_compression/problems/P072/exercise.py
.\.venv\Scripts\python.exe check.py P072
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/08_compression/problems/P072/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html)。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/P072.md) · [下一题](../P073/README.md)
