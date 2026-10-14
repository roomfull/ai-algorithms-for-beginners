# P009 字典词频；独立运行，无其他答案依赖。
words = input().split()
query = input()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] = counts[word] + 1
# 不直接读取不存在的键，避免 KeyError。
if query in counts:
    print(counts[query])
else:
    print(0)
