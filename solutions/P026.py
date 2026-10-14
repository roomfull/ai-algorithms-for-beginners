"""P026：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：先逐列检查所有输入值是否等于首行值，常量列直接设σ=0，避免十进制0.1求均值的舍入误差；其他列缓存μ和σ后用 (x-μ)/σ。
def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [list(map(float, line.split())) for line in lines[1:n+1]]
    constant = [all(row[j] == rows[0][j] for row in rows) for j in range(d)]
    means = [sum(row[j] for row in rows)/n for j in range(d)]
    # 相同输入构成常量列；浮点均值的微小舍入不能制造出非零方差。
    stds = [0.0 if constant[j] else
            math.sqrt(sum((row[j]-means[j])**2 for row in rows)/n) for j in range(d)]
    return '\n'.join(format_row(0.0 if stds[j] == 0 else (row[j]-means[j])/stds[j]
                                for j in range(d)) for row in rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
