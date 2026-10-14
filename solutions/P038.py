"""P038：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(float(v), ".12g") for v in values)


# 算法关键：减法、统计量及除法均保留Fraction，只在最终输出时转float。先求M，再求abs(x-M)的中位数；MAD>0时逐项除MAD，否则造全0；不能用偏差的平均数代替中位数。
from fractions import Fraction


def median(values):
    ordered = sorted(values)
    n = len(ordered)
    if n % 2:
        return ordered[n//2]
    return (ordered[n//2-1]+ordered[n//2])/2


def solve(raw):
    values = list(map(Fraction, raw.split()))
    center = median(values)
    mad = median([abs(x-center) for x in values])
    features = [0.0 if mad == 0 else (x-center)/mad for x in values]
    return format_row([center, mad])+'\n'+format_row(features)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
