"""P035：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：排序 enumerate(values) 为 (value,index) 顺序；对秩r把 r*k//n 写入结果的原始index。
def solve(raw):
    lines = raw.splitlines()
    n, k = map(int, lines[0].split())
    values = list(map(int, lines[1].split()))
    ordered = sorted((value, index) for index, value in enumerate(values))
    groups = [0]*n
    for rank, (value, index) in enumerate(ordered):
        groups[index] = rank*k//n
    return ' '.join(map(str, groups))


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
