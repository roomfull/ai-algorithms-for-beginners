# P018 点积；独立运行，无其他答案依赖。
import numpy as np

left = []
for token in input().split():
    left.append(float(token))
right = []
for token in input().split():
    right.append(float(token))
a = np.array(left, dtype=float)
b = np.array(right, dtype=float)
products = a * b  # 逐元素相乘，之后才求和。
print(products.sum())
