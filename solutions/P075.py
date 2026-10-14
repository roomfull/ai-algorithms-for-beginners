"""仿射uint8：先round，再加整数零点，最后截断。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    n,scale,zp=int(next(tokens)),Fraction(next(tokens)),int(next(tokens))
    values=[Fraction(next(tokens)) for _ in range(n)]
    quantized=[]
    for x in values:
        shifted=round(x/scale)+zp
        quantized.append(max(0,min(255,shifted)))
    restored=[(q-zp)*scale for q in quantized]
    return ' '.join(map(str,quantized))+'\n'+' '.join(f'{float(x):.12g}' for x in restored)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
