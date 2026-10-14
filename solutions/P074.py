"""对称int8；比值精确后round ties-to-even，浮点仅用于输出。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    n=int(next(tokens))
    values=[Fraction(next(tokens)) for _ in range(n)]
    maximum=max(abs(x) for x in values)
    scale=maximum/127 if maximum else Fraction(1)
    # 对Fraction直接round返回整数，精确处理中间点并列。
    quantized=[max(-127,min(127,round(x/scale))) for x in values]
    restored=[q*scale for q in quantized]
    return (f'{float(scale):.12g}\n'+' '.join(map(str,quantized))+'\n'
            +' '.join(f'{float(x):.12g}' for x in restored))


if __name__=='__main__':
    print(solve(sys.stdin.read()))
