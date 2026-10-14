# P032 平滑 IDF

给定 n 篇文档，df(w) 是含词 w 的文档篇数（同篇重复只计1）。平滑 IDF(w)=ln((1+n)/(1+df(w)))+1，ln 为自然对数。词表按字典序排列，词表中的词可完全不出现。

## 输入与约束

首行 n v；第2行 v 个互异小写英文字母串，长度1到20；随后 n 行为文档，空行表示空文档。1≤n≤100，1≤v≤100；所有文档合计最多2000词，均在词表中。按空白分词。

## 输出

一行 v 个 IDF，按词表字典序。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
2 3
pear apple cat
apple pear
apple
```
输出：
```text
1 2.09861228866811 1.4054651081081644
```

手算：两篇 apple pear、apple：apple的df=2，IDF=1；cat的df=0，IDF=ln3+1≈2.098612；pear的df=1，IDF=ln(3/2)+1≈1.405465。

## 分级提示

<details><summary>提示 1</summary>

对每篇文档先去重，再增加文档频率。

</details>

<details><summary>提示 2</summary>

n 是包括空文档的篇数；公式分子分母均加1，结果再加1。

</details>

<details><summary>提示 3</summary>

df初始化为0，遍历 set(文档词) 对df加1；按字典序代入 math.log((1+n)/(1+df))+1。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P032/exercise.py
.\.venv\Scripts\python.exe check.py P032
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P032/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/feature_extraction.html#tf-idf-term-weighting)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P033/README.md) · [题解](../../../../solutions/P032.md)
