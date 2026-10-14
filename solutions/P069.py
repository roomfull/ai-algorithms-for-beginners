"""小图精确PageRank：Fraction保持十进制L1<=tol契约。"""
import sys
from fractions import Fraction


def solve(raw):
    tokens=iter(raw.split())
    n,m=int(next(tokens)),int(next(tokens))
    alpha,tol=Fraction(next(tokens)),Fraction(next(tokens))
    max_iter=int(next(tokens))
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=int(next(tokens)),int(next(tokens))
        adj[u].append(v)
    p=[Fraction(1,n)]*n
    converged=0
    for step in range(1,max_iter+1):
        dangling=sum(p[u] for u in range(n) if not adj[u])
        q=[(1-alpha)/n+alpha*dangling/n for _ in range(n)]
        for u in range(n):
            if adj[u]:
                share=alpha*p[u]/len(adj[u])
                for v in adj[u]:
                    q[v]+=share
        # 每轮概率和L1都精确计算，不能用epsilon扩大收敛阈值。
        delta=sum(abs(q[i]-p[i]) for i in range(n))
        p=q  # 输出和下轮输入都使用本轮的新分布。
        if delta<=tol:
            converged=1
            break
    return f'{step} {converged}\n'+' '.join(f'{float(v):.12g}' for v in p)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
