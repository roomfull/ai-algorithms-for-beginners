"""PageRank一轮同步更新，悬挂概率均分。"""
import sys
import math


def solve(raw):
    tokens=iter(raw.split())
    n,m,alpha=int(next(tokens)),int(next(tokens)),float(next(tokens))
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=int(next(tokens)),int(next(tokens))
        adj[u].append(v)
    p=[float(next(tokens)) for _ in range(n)]
    dangling=math.fsum(p[u] for u in range(n) if not adj[u])
    q=[(1-alpha)/n+alpha*dangling/n for _ in range(n)]
    for u in range(n):
        if adj[u]:
            share=alpha*p[u]/len(adj[u])
            for v in adj[u]:
                q[v]+=share
    return ' '.join(f'{v:.12g}' for v in q)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
