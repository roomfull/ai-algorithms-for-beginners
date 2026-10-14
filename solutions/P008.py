# P008 列表筛选；独立运行，无其他答案依赖。
tokens = input().split()
selected = []
for token in tokens:
    if int(token) > 0:
        selected.append(token)
# join 要求列表中的元素都是字符串。
if len(selected) == 0:
    print("EMPTY")
else:
    print(" ".join(selected))
