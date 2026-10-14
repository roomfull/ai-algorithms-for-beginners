# P021 索引与广播：请先阅读同目录 README.md。
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
# TODO：独立计算两块；行偏移先改为(r,1)，再按顺序输出。
raise NotImplementedError("请按题目提示完成这里")
