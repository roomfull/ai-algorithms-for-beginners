"""P023：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：先求每列均值（空列置0），再逐行用均值替换 NA。
def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [line.split() for line in lines[1:n+1]]
    means = []
    for j in range(d):
        values = [float(row[j]) for row in rows if row[j] != 'NA']
        means.append(sum(values) / len(values) if values else 0.0)
    # 缺失位置才替换；已知值原样保留。
    return '\n'.join(format_row(means[j] if row[j] == 'NA' else float(row[j])
                                for j in range(d)) for row in rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
