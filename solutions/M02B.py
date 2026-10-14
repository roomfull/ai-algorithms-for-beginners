"""带悬挂网页的 PageRank 排名：独立参考解。"""
import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); n,m=int(next(it)),int(next(it))
    alpha,tol=Fraction(next(it)),Fraction(next(it)); limit=int(next(it))
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=int(next(it)),int(next(it)); adj[u].append(v)
    p=[Fraction(1,n)]*n; flag=0
    for step in range(1,limit+1):
        dangling=sum(p[u] for u in range(n) if not adj[u])
        q=[(1-alpha)/n+alpha*dangling/n for _ in range(n)]
        for u in range(n):
            for v in adj[u]: q[v]+=alpha*p[u]/len(adj[u])
        delta=sum(abs(q[i]-p[i]) for i in range(n))
        p=q
        if delta<=tol:
            flag=1; break
    ranking=sorted(range(n),key=lambda i:(-p[i],i))
    return f'{step} {flag}\n'+' '.join(map(str,ranking))+'\n'+' '.join(f'{float(value):.12g}' for value in p)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
