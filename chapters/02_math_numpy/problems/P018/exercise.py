# P018 点积：请先阅读同目录 README.md。
import numpy as np

left = []
for token in input().split():
    left.append(float(token))
right = []
for token in input().split():
    right.append(float(token))
a = np.array(left, dtype=float)
b = np.array(right, dtype=float)
# TODO：对应位置相乘，再将乘积求和。
raise NotImplementedError("请按题目提示完成这里")
