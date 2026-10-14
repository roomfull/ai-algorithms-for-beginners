# P019 矩阵乘法；独立运行，无其他答案依赖。
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
for i in range(r):
    for j in range(c):
        total = 0.0
        for t in range(k):
            total = total + a[i, t] * b[t, j]
        result[i, j] = total
for row in result:
    print(*row)
