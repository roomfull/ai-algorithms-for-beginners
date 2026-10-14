"""P036：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：遍历4格并累加(O-E)²/E；N=0直接0，E=0跳过；参考解用Fraction计算精确有理数，最后转浮点输出。
from fractions import Fraction


def chi_square(table):
    total = sum(sum(row) for row in table)
    if total == 0:
        return Fraction(0)
    row_sums = [sum(row) for row in table]
    col_sums = [table[0][j]+table[1][j] for j in range(2)]
    answer = Fraction(0)
    for i in range(2):
        for j in range(2):
            expected = Fraction(row_sums[i]*col_sums[j], total)
            if expected != 0:  # 题面约定：期望为0项贡献0。
                answer += (table[i][j]-expected)**2/expected
    return answer


def solve(raw):
    table = [list(map(int, line.split())) for line in raw.splitlines()]
    return format_row([float(chi_square(table))])


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
