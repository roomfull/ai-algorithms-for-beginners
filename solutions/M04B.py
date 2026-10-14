"""不同 worker 与 microbatch 的加权更新：独立参考解。"""
import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); W,d=int(next(it)),int(next(it)); lr=Fraction(next(it))
    weights=[Fraction(next(it)) for _ in range(d)]
    totals=[Fraction(0)]*d; samples=0
    for _ in range(W):
        batches=int(next(it))
        for _ in range(batches):
            count=int(next(it)); samples+=count
            for j in range(d): totals[j]+=count*Fraction(next(it))
    # 先恢复梯度和，统一除样本总数，最后只更新一次。
    gradient=[value/samples for value in totals]
    updated=[weights[j]-lr*gradient[j] for j in range(d)]
    return ' '.join(f'{float(value):.12g}' for value in gradient)+'\n'+' '.join(f'{float(value):.12g}' for value in updated)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
