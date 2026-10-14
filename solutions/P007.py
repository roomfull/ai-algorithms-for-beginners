# P007 while 计数；独立运行，无其他答案依赖。
n = int(input())
current = 2
count = 0
# 每轮消费一个正偶数；更新 current 保证循环终止。
while current <= n:
    count = count + 1
    current = current + 2
print(count)
