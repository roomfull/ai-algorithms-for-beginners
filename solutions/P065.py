"""在每个分量中做双色BFS，检查所有边。"""
import sys
from collections import deque


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=next(tokens),next(tokens)
        adj[u].append(v)
        adj[v].append(u)
    color=[-1]*n
    for root in range(n):
        if color[root]!=-1:
            continue
        color[root]=0
        queue=deque([root])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if color[v]==-1:
                    color[v]=1-color[u]
                    queue.append(v)
                elif color[v]==color[u]:
                    return '0'
    return '1'


if __name__=='__main__':
    print(solve(sys.stdin.read()))
