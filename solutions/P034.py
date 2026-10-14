"""P034：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：每个整数x的箱号是 min(k-1,(x-low)*k//(high-low))；常量时全0。
def solve(raw):
    lines = raw.splitlines()
    n, k = map(int, lines[0].split())
    values = list(map(int, lines[1].split()))
    low, high = min(values), max(values)
    if low == high:
        bins = [0]*n
    else:
        bins = [min(k-1, (x-low)*k//(high-low)) for x in values]
    return ' '.join(map(str, bins))


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
