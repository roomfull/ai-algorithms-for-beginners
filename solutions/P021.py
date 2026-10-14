# P021 索引与广播；独立运行，无其他答案依赖。
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
columns = []
for token in input().split():
    columns.append(float(token))
row_offsets = []
for token in input().split():
    row_offsets.append(float(token))
a = np.array(rows, dtype=float)
columns = np.array(columns, dtype=float)
row_offsets = np.array(row_offsets, dtype=float)
by_column = a + columns
# 显式列形状使每个行偏移沿该行的所有列重复。
by_row = a + row_offsets.reshape((r, 1))
for row in by_column:
    print(*row)
for row in by_row:
    print(*row)
