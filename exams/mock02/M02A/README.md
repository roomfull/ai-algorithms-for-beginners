# M02A TF-IDF 文本余弦检索

给定训练语料的词频矩阵，每列对应一个已给定词，词序不变。原始词频tf就是次数，不除文档长度、不取log。df_j为包含该词的训练文档数，idf_j=1+ln((n+1)/(df_j+1))，ln为自然对数。文档与查询都乘这组idf，查询不计入df。余弦=点积/(两个L2范数乘积)；任一零范数时定义为0，无共同词也为0。按round(score,12)降序排列，键相同时按文档下标升序；round是Python内置舍入，仅用于排名键，输出原始分数。

## 输入与约束

首行 n v k；接着 n 行，每行 v 个非负整数词频；最后一行 v 个查询词频。1≤k≤n≤50，1≤v≤20，0≤词频≤100。输入合法，无需分词或下载语料。

## 输出

第一行前k篇文档下标（0起）；第二行对应的k个原始余弦分数。 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
3 2 3
1 0
0 1
1 1
1 0
```
输出：
```text
0 2 1
1 0.7071067811865476 0
```

手算：两列df都为2，idf都为1+ln(4/3)，共同系数抵消。查询(1,0)与三篇余弦分别1、0、1/√2，round(score,12)排序为0、2、1；输出原分数1、0.7071067811865476、0。

## 分级提示

<details><summary>提示 1</summary>

先按列统计非零文档数，不统计查询。

</details>

<details><summary>提示 2</summary>

计算训练idf，再分别构造加权文档与加权查询；零范数直接给0。

</details>

<details><summary>提示 3</summary>

scores存原分数；sorted(range(n),key=lambda i:(-round(scores[i],12),i))[:k]取下标，再输出对应scores。

</details>

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\.venv\Scripts\python.exe exams/mock02/M02A/exercise.py
.\.venv\Scripts\python.exe check.py M02A
.\.venv\Scripts\python.exe check.py --chapter M02
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\.venv\Scripts\python.exe exams/mock02/M02A/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考](https://github.com/scikit-learn/scikit-learn/blob/main/doc/modules/feature_extraction.rst)。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/M02A.md)
