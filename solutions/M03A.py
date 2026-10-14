"""指定初值聚类、误差与查询分配：独立参考解。"""
import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); n,d,k,T=[int(next(it)) for _ in range(4)]
    x=[[Fraction(next(it)) for _ in range(d)] for _ in range(n)]
    centers=[[Fraction(next(it)) for _ in range(d)] for _ in range(k)]
    query=[Fraction(next(it)) for _ in range(d)]
    def distance(point, center):
        return sum((point[j]-center[j])**2 for j in range(d))
    def nearest(point):
        return min(range(k),key=lambda c:(distance(point,centers[c]),c))
    for _ in range(T):
        labels=[nearest(point) for point in x]
        updated=[]
        for c in range(k):
            members=[i for i in range(n) if labels[i]==c]
            updated.append([sum(x[i][j] for i in members)/len(members) for j in range(d)] if members else centers[c][:])
        centers=updated
    # 末轮更新后，重新分配但不再更新中心。
    labels=[nearest(point) for point in x]
    sse=sum(distance(x[i],centers[labels[i]]) for i in range(n))
    rows=[' '.join(map(str,labels))]
    rows+=[' '.join(f'{float(value):.12g}' for value in center) for center in centers]
    rows+=[f'{float(sse):.12g}',str(nearest(query))]
    return '\n'.join(rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
