"""等样本数worker局部均值，只除worker数一次。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    workers,dims=int(next(tokens)),int(next(tokens))
    total=[Fraction(0) for _ in range(dims)]
    for _ in range(workers):
        for j in range(dims):
            total[j]+=Fraction(next(tokens))
    return ' '.join(f'{float(v/workers):.12g}' for v in total)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
