"""P026：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(float(v), ".12g") for v in values)


# 算法关键：以Fraction求均值μ和总体方差v；v=0直接输出0；否则令delta=x-μ，先精确算delta²/v，再取平方根并恢复delta的正负号。仅在开平方与输出时转float。
from fractions import Fraction


def zscore(delta, variance):
    if variance == 0:
        return 0.0
    # 先精确相除，再开平方：0 <= delta²/variance <= n。
    # 不把很小的原始方差先转float，避免尺度导致的下溢。
    magnitude = math.sqrt(float(delta * delta / variance))
    return -magnitude if delta < 0 else magnitude


def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [list(map(Fraction, line.split())) for line in lines[1:n+1]]
    means = [sum(row[j] for row in rows)/n for j in range(d)]
    variances = [sum((row[j]-means[j])**2 for row in rows)/n for j in range(d)]
    return '\n'.join(format_row(zscore(row[j]-means[j], variances[j])
                                for j in range(d)) for row in rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
