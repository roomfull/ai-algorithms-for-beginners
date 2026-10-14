"""绝对值严格小于阈值才剪掉，十进制比较精确。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    n,threshold=int(next(tokens)),Fraction(next(tokens))
    values=[Fraction(next(tokens)) for _ in range(n)]
    result=[0 if abs(x)<threshold else x for x in values]
    return ' '.join(f'{float(x):.12g}' for x in result)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
