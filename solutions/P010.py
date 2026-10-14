# P010 集合去重计数；独立运行，无其他答案依赖。
tokens = input().split()
seen = set()
for token in tokens:
    # 先转整数，按数值而不是文字形式判重。
    seen.add(int(token))
print(len(seen))
