# P019 矩阵乘法：请先阅读同目录 README.md。
import numpy as np

dimensions = input().split()
r = int(dimensions[0])
k = int(dimensions[1])
c = int(dimensions[2])
rows_a = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows_a.append(row)
rows_b = []
for i in range(k):
    row = []
    for token in input().split():
        row.append(float(token))
    rows_b.append(row)
a = np.array(rows_a, dtype=float)
b = np.array(rows_b, dtype=float)
result = np.zeros((r, c), dtype=float)
# TODO：三层循环，按 A 的行与 B 的列做点积；然后逐行输出。
raise NotImplementedError("请按题目提示完成这里")
