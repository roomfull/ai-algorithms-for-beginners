"""精确比例floor，按绝对值与索引稳定选择剪枝位置。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    n,ratio=int(next(tokens)),Fraction(next(tokens))
    values=[Fraction(next(tokens)) for _ in range(n)]
    # ratio非负，因此int(Fraction)等于数学floor；100*0.29精确得到29。
    count=int(n*ratio)
    order=sorted(range(n),key=lambda i:(abs(values[i]),i))
    mask=[1]*n
    for i in order[:count]:
        mask[i]=0
    pruned=[values[i] if mask[i] else 0 for i in range(n)]
    return ' '.join(map(str,mask))+'\n'+' '.join(f'{float(x):.12g}' for x in pruned)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
