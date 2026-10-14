"""P026：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：缓存 μ 和 σ；σ=0 的列输出0，其他列用 (x-μ)/σ。
def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [list(map(float, line.split())) for line in lines[1:n+1]]
    means = [sum(row[j] for row in rows)/n for j in range(d)]
    stds = [math.sqrt(sum((row[j]-means[j])**2 for row in rows)/n) for j in range(d)]
    return '\n'.join(format_row(0.0 if stds[j] == 0 else (row[j]-means[j])/stds[j]
                                for j in range(d)) for row in rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
