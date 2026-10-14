"""P024：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：按输入顺序遍历；行元组未见过才加入集合与结果列表。
def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    seen = set()
    kept = []
    for line in lines[1:n+1]:
        row = tuple(map(int, line.split()))
        if row not in seen:
            seen.add(row)
            kept.append(row)
    return '\n'.join([str(len(kept))] + [' '.join(map(str, row)) for row in kept])


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
