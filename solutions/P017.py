# P017 欧氏距离；独立运行，无其他答案依赖。
import numpy as np

left = []
for token in input().split():
    left.append(float(token))
right = []
for token in input().split():
    right.append(float(token))
a = np.array(left, dtype=float)
b = np.array(right, dtype=float)
difference = a - b
# 先合并平方，再开平方；不是各坐标距离之和。
print(np.sqrt((difference ** 2).sum()))
