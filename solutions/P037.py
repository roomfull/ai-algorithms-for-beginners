"""P037：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：借用2×2公式但在同一文件独立实现；用Fraction保持并列精确，合并列表中best与best+1，下一轮重新扫描。
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
    lines = raw.splitlines()
    b, target = map(int, lines[0].split())
    bins = []
    for line in lines[1:b+1]:
        value, count0, count1 = map(int, line.split())
        bins.append([value, value, count0, count1])
    while len(bins) > target:
        best = 0
        best_score = chi_square([bins[0][2:], bins[1][2:]])
        for i in range(1, len(bins)-1):
            score = chi_square([bins[i][2:], bins[i+1][2:]])
            if score < best_score:  # 相等时保留先扫描到的最左位置。
                best, best_score = i, score
        left, right = bins[best], bins[best+1]
        bins[best] = [left[0], right[1], left[2]+right[2], left[3]+right[3]]
        del bins[best+1]
    return '\n'.join(' '.join(map(str, box)) for box in bins)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
