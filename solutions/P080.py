"""数值模拟microbatch累积与全局同步SGD，只更新一次。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    workers,dims=int(next(tokens)),int(next(tokens))
    lr=Fraction(next(tokens))
    theta=[Fraction(next(tokens)) for _ in range(dims)]
    total=[Fraction(0) for _ in range(dims)]
    count_sum=0
    for _ in range(workers):
        batches=int(next(tokens))
        for _ in range(batches):
            count=int(next(tokens))
            count_sum+=count
            for j in range(dims):
                total[j]+=count*Fraction(next(tokens))
    # 所有局部梯度都在旧theta上计算；全局归一化一次、参数更新一次。
    gradient=[v/count_sum for v in total]
    updated=[theta[j]-lr*gradient[j] for j in range(dims)]
    return (' '.join(f'{float(v):.12g}' for v in gradient)+'\n'
            +' '.join(f'{float(v):.12g}' for v in updated))


if __name__=='__main__':
    print(solve(sys.stdin.read()))
