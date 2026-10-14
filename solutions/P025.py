"""P025：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(float(v), ".12g") for v in values)


# 算法关键：减法、统计量及除法均保留Fraction，只在最终输出时转float。缓存各列 min/max，再逐元素套公式，常量分支避免除0。
from fractions import Fraction


def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [list(map(Fraction, line.split())) for line in lines[1:n+1]]
    low = [min(row[j] for row in rows) for j in range(d)]
    high = [max(row[j] for row in rows) for j in range(d)]
    return '\n'.join(format_row(0.0 if high[j] == low[j] else
                      (row[j]-low[j])/(high[j]-low[j]) for j in range(d)) for row in rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
