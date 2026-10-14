# P020 shape 与 reshape：请先阅读同目录 README.md。
import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
values = []
for token in input().split():
    values.append(float(token))
array = np.array(values, dtype=float)
# TODO：重排、输出形状，再输出各行。
raise NotImplementedError("请按题目提示完成这里")
