"""训练集标准化后的 KNN 分类：独立参考解。"""
import sys
from fractions import Fraction
from collections import Counter

def solve(raw):
    it=iter(raw.split())
    n,d,k=int(next(it)),int(next(it)),int(next(it))
    x=[]; labels=[]
    for _ in range(n):
        x.append([Fraction(next(it)) for _ in range(d)])
        labels.append(int(next(it)))
    q=[Fraction(next(it)) for _ in range(d)]
    means=[sum(row[j] for row in x)/n for j in range(d)]
    variances=[sum((row[j]-means[j])**2 for row in x)/n for j in range(d)]
    # Z-score差的平方无需sqrt，保留精确平票。
    distances=[sum((row[j]-q[j])**2/variances[j] for j in range(d) if variances[j]) for row in x]
    neighbors=sorted(range(n),key=lambda i:(distances[i],i))[:k]
    votes=Counter(labels[i] for i in neighbors)
    prediction=min(votes,key=lambda label:(-votes[label],label))
    return ' '.join(map(str,neighbors))+'\n'+str(prediction)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
