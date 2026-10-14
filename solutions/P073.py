"""行L1范数精确比较；选择顺序与输出顺序不同。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    rows,cols,keep=int(next(tokens)),int(next(tokens)),int(next(tokens))
    matrix=[[Fraction(next(tokens)) for _ in range(cols)] for _ in range(rows)]
    norm=[sum(abs(x) for x in row) for row in matrix]
    order=sorted(range(rows),key=lambda i:(-norm[i],i))
    selected=set(order[:keep])
    mask=[int(i in selected) for i in range(rows)]
    output=[' '.join(map(str,mask))]
    # 最终结果按原始行索引，不按范数排序。
    for i in range(rows):
        if mask[i]:
            output.append(' '.join(f'{float(x):.12g}' for x in matrix[i]))
    return '\n'.join(output)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
