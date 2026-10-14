# P031 原始词频 TF

给定词表和一篇文档，计算原始词频 TF：每个词在文档中出现的次数。词表按字典序输出，不按输入词表顺序。按空白分词，大小写敏感，不做分词模型或标点处理。

## 输入与约束

首行 v；第2行 v 个互异小写英文字母串，长度1到20；第3行为文档（可为空行）。1≤v≤100；文档最多2000个词，所有词都在词表中。

## 输出

一行 v 个整数，依词表字典序排列。 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
3
pear apple cat
apple pear apple
```
输出：
```text
2 0 1
```

手算：输入词表 pear apple cat 排序为 apple cat pear；文档 apple pear apple 对应词频2、0、1。

## 分级提示

<details><summary>提示 1</summary>

先把词表排序，文档用 split() 分成词。

</details>

<details><summary>提示 2</summary>

用字典累计计数，未出现词计数为0。

</details>

<details><summary>提示 3</summary>

遍历文档对 counts[word] 加1；最后按 sorted(vocab) 查询 counts.get(word,0)。

</details>

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\.venv\Scripts\python.exe chapters/04_features/problems/P031/exercise.py
.\.venv\Scripts\python.exe check.py P031
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\.venv\Scripts\python.exe chapters/04_features/problems/P031/exercise.py`。不要输出提示文字。

定义核对：[一手资料](https://scikit-learn.org/stable/modules/feature_extraction.html#tf-idf-term-weighting)。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口](../P032/README.md) · [题解](../../../../solutions/P031.md)
