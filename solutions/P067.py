"""Prim最小堆懒删除：每次加入一个未访问顶点。"""
import sys
import heapq


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v,w=next(tokens),next(tokens),next(tokens)
        adj[u].append((v,w))
        adj[v].append((u,w))
    seen=[False]*n
    heap=[(0,0)]
    count=total=0
    while heap:
        w,u=heapq.heappop(heap)
        if seen[u]:
            continue
        seen[u]=True
        count+=1
        total+=w
        for v,edge_weight in adj[u]:
            if not seen[v]:
                heapq.heappush(heap,(edge_weight,v))
    return str(total) if count==n else 'DISCONNECTED'


if __name__=='__main__':
    print(solve(sys.stdin.read()))
