"""P029：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：使用 [x[j]+λ*(z[j]-x[j]) for j in range(d)]；λ=0返回x，λ=1返回z。
def solve(raw):
    lines = raw.splitlines()
    d = int(lines[0])
    x = list(map(float, lines[1].split()))
    z = list(map(float, lines[2].split()))
    lam = float(lines[3])
    return format_row(x[j]+lam*(z[j]-x[j]) for j in range(d))


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
