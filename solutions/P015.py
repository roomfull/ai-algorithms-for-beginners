# P015 求和与均值双实现；独立运行，无其他答案依赖。
import numpy as np

values = []
for token in input().split():
    values.append(float(token))
total = 0.0
for value in values:
    total = total + value
print(total, total / len(values))
# 数组方法与上面的普通循环计算相同统计量。
array = np.array(values, dtype=float)
print(array.sum(), array.mean())
