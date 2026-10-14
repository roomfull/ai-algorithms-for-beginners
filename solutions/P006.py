# P006 for 累加；独立运行，无其他答案依赖。
n = int(input())
total = 0
# range 不包含右端点，因此右端写 n + 1。
for i in range(1, n + 1):
    total = total + i
print(total)
