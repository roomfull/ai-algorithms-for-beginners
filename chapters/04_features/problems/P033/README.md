# P033 TF-IDF 与 L2 归一化

对 n 篇文档计算 TF-IDF：TF为原始词次数，IDF=ln((1+n)/(1+df))+1，df为出现该词的文档篇数。按给定词表的字典序排列向量。若 norm=1，每篇向量除以自身 L2 范数 sqrt(Σa²)；若范数0则保留全0。norm=0时直接输出权重。

## 输入与约束

首行 n v norm（norm为0或1）；第2行 v 个互异小写英文字母串，长度1到20；随后 n 行文档，可为空行。1≤n≤100，1≤v≤100；总词数≤2000，词均在词表中，按空白分词。

## 输出

输出 n 行 v 列，行顺序与文档一致。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
2 2 0
b a
a a b
a
```
输出：
```text
2 1.4054651081081644
1 0
```

手算：词表 b a 排为 a b；a出现两篇IDF=1，b只出现一篇IDF≈1.405465。norm=0，所以第1篇权重(2,1.405465)，第2篇(1,0)。若norm=1，第1篇除以sqrt(4+1.405465²)。

## 分级提示

<details><summary>提示 1</summary>

先处理整个语料，得出各词df与IDF。

</details>

<details><summary>提示 2</summary>

每篇TF独立统计，再逐词乘IDF；L2归一化是按行做的。

</details>

<details><summary>提示 3</summary>

存各篇计数字典；由计数字典的键累计df；逐行造TF×IDF向量，norm=1且模长>0时除以模长。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P033/exercise.py
.\.venv\Scripts\python.exe check.py P033
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P033/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/feature_extraction.html#tf-idf-term-weighting)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P034/README.md) · [题解](../../../../solutions/P033.md)
