# P013 二维列表行和；独立运行，无其他答案依赖。
r = int(input())
matrix = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(int(token))
    matrix.append(row)
for row in matrix:
    total = 0  # 每一行使用独立的累加器。
    for value in row:
        total = total + value
    print(total)
