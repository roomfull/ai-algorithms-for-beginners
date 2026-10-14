"""误差统计与纯数组理论数据字节；未计元数据。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    n=int(next(tokens))
    original=[Fraction(next(tokens)) for _ in range(n)]
    error=[original[i]-Fraction(next(tokens)) for i in range(n)]
    mse=sum(e*e for e in error)/n
    maximum=max(abs(e) for e in error)
    return f'{float(mse):.12g} {float(maximum):.12g}\n{4*n} {n}'


if __name__=='__main__':
    print(solve(sys.stdin.read()))
