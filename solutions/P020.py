# P020 shape 与 reshape；独立运行，无其他答案依赖。
import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
values = []
for token in input().split():
    values.append(float(token))
array = np.array(values, dtype=float)
matrix = array.reshape((r, c))  # 默认先填完整的一行。
print(*matrix.shape)
for row in matrix:
    print(*row)
