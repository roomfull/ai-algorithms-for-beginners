"""全部分量双色搜索，加递增三点统计。"""
import sys
from collections import deque


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    adj=[set() for _ in range(n)]
    for _ in range(m):
        u,v=next(tokens),next(tokens)
        adj[u].add(v)
        adj[v].add(u)
    color=[-1]*n
    components=0
    bipartite=1
    for root in range(n):
        if color[root]!=-1:
            continue
        components+=1
        color[root]=0
        queue=deque([root])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if color[v]==-1:
                    color[v]=1-color[u]
                    queue.append(v)
                elif color[v]==color[u]:
                    # 只记冲突，仍需搜索剩余点以统计全部分量。
                    bipartite=0
    triangles=0
    for a in range(n):
        for b in range(a+1,n):
            if b in adj[a]:
                for c in range(b+1,n):
                    if c in adj[a] and c in adj[b]:
                        triangles+=1
    return f'{components} {bipartite} {triangles}'


if __name__=='__main__':
    print(solve(sys.stdin.read()))
