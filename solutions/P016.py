# P016 总体方差；独立运行，无其他答案依赖。
import numpy as np

values = []
for token in input().split():
    values.append(float(token))
array = np.array(values, dtype=float)
mean = array.mean()
difference = array - mean
# 平方偏差的均值就是总体方差，即 ddof=0。
squared = difference ** 2
print(squared.mean())
