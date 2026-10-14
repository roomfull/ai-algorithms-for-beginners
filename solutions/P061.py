"""BFS第一次发现时确定最短边数。"""
import sys
from collections import deque


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m,start=next(tokens),next(tokens),next(tokens)
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=next(tokens),next(tokens)
        adj[u].append(v)
        adj[v].append(u)
    distance=[-1]*n
    distance[start]=0
    queue=deque([start])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if distance[v]==-1:
                # 入队时标记，保证每个顶点最多入队一次。
                distance[v]=distance[u]+1
                queue.append(v)
    return ' '.join(map(str,distance))


if __name__=='__main__':
    print(solve(sys.stdin.read()))
