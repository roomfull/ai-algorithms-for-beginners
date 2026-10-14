# P022 axis 行列聚合：请先阅读同目录 README.md。
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
# TODO：第一行输出行和，第二行输出列和，注意轴和结果长度。
raise NotImplementedError("请按题目提示完成这里")
