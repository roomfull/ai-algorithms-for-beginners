"""递增枚举三点，避免重复统计同一个三角形。"""
import sys


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    adj=[set() for _ in range(n)]
    for _ in range(m):
        u,v=next(tokens),next(tokens)
        adj[u].add(v)
        adj[v].add(u)
    total=0
    for a in range(n):
        for b in range(a+1,n):
            if b not in adj[a]:
                continue
            for c in range(b+1,n):
                if c in adj[a] and c in adj[b]:
                    total+=1
    return str(total)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
