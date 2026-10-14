# P011 排序与平票；独立运行，无其他答案依赖。
from operator import itemgetter

n = int(input())
records = []
for i in range(n):
    parts = input().split()
    records.append([parts[0], int(parts[1])])
# 先确定平票顺序，再用稳定排序处理主键分数。
records.sort()
records.sort(key=itemgetter(1), reverse=True)
for row in records:
    print(row[0], row[1])
