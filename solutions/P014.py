# P014 多组数据输入输出验收；独立运行，无其他答案依赖。
t = int(input())
for group in range(t):
    total = 0  # 各组互不影响。
    for token in input().split():
        total = total + int(token)
    print(total)
