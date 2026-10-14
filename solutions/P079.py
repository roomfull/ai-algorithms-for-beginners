"""局部均值乘样本数还原梯度和，末尾除总样本数。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    workers,dims=int(next(tokens)),int(next(tokens))
    total=[Fraction(0) for _ in range(dims)]
    count_sum=0
    for _ in range(workers):
        count=int(next(tokens))
        count_sum+=count
        for j in range(dims):
            # 0样本行仍需读取占位梯度，乘0后自然忽略。
            total[j]+=count*Fraction(next(tokens))
    return ' '.join(f'{float(v/count_sum):.12g}' for v in total)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
