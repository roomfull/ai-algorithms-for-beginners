"""P045：稳定sigmoid与分类。"""
import sys
import math
from fractions import Fraction


def sigmoid(z):
    if z >= 0:
        return 1/(1+math.exp(-z))
    e = math.exp(z)
    return e/(1+e)


def solve(raw):
    lines = raw.strip().splitlines()
    n, d = map(int, lines[0].split())
    # 直接从输入字符串构造分数，保留十进制数的精确值。
    points = [list(map(Fraction, s.split())) for s in lines[1:n+1]]
    w = list(map(Fraction, lines[n+1].split()))
    b = Fraction(lines[n+2])
    result = []
    for x in points:
        score = sum(a*t for a, t in zip(w, x))+b
        p = sigmoid(float(score))
        # sigmoid严格递增；依据精确分数的符号判类，不能依据舍入后的概率。
        result.extend([f'{p:.12g}', str(int(score >= 0))])
    return '\n'.join(result)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
