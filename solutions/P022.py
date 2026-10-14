# P022 axis 行列聚合；独立运行，无其他答案依赖。
import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
rows = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows.append(row)
a = np.array(rows, dtype=float)
row_sums = a.sum(axis=1)  # 消掉列维度，留下各行。
column_sums = a.sum(axis=0)  # 消掉行维度，留下各列。
print(*row_sums)
print(*column_sums)
