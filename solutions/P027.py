"""P027：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(float(v), ".12g") for v in values)


# 算法关键：减法、统计量及除法均保留Fraction，只在最终输出时转float。缓存训练 min/max；遍历排列逐行缩放，常量列输出0，验证结果不裁剪。
from fractions import Fraction


def solve(raw):
    lines = raw.splitlines()
    n, d, t = map(int, lines[0].split())
    rows = [list(map(Fraction, line.split())) for line in lines[1:n+1]]
    order = list(map(int, lines[n+1].split()))
    training = [rows[i] for i in order[:t]]
    low = [min(row[j] for row in training) for j in range(d)]
    high = [max(row[j] for row in training) for j in range(d)]
    # 验证行参与变换，但不参与统计量估计。
    return '\n'.join(format_row(0.0 if high[j] == low[j] else
                      (rows[i][j]-low[j])/(high[j]-low[j]) for j in range(d)) for i in order)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
