"""逐行对称权重量化与重构误差：独立参考解。"""
import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); r,c,b=[int(next(it)) for _ in range(3)]
    weights=[[Fraction(next(it)) for _ in range(c)] for _ in range(r)]
    Q=2**(b-1)-1; scales=[]; integers=[]; errors=[]
    for row in weights:
        maximum=max(abs(value) for value in row)
        scale=maximum/Q if maximum else Fraction(1)
        quantized=[]
        for value in row:
            ratio=abs(value)/scale
            # 精确半格远离零，不使用round的半偶舍入。
            rounded=(2*ratio.numerator+ratio.denominator)//(2*ratio.denominator)
            signed=rounded if value>=0 else -rounded
            quantized.append(max(-Q,min(Q,signed)))
        mse=sum((row[j]-quantized[j]*scale)**2 for j in range(c))/c
        scales.append(scale); integers.append(quantized); errors.append(mse)
    rows=[' '.join(f'{float(value):.12g}' for value in scales)]
    rows+=[' '.join(map(str,row)) for row in integers]
    rows+=[' '.join(f'{float(value):.12g}' for value in errors)]
    return '\n'.join(rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
