"""Kruskal按权重选边，并查集阻止形成环。"""
import sys


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    edges=[]
    for _ in range(m):
        u,v,w=next(tokens),next(tokens),next(tokens)
        edges.append((w,u,v))
    parent=list(range(n))
    size=[1]*n

    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x

    total=used=0
    for w,u,v in sorted(edges):
        a,b=find(u),find(v)
        if a==b:
            continue
        if size[a]<size[b]:
            a,b=b,a
        parent[b]=a
        size[a]+=size[b]
        total+=w
        used+=1
    # 一个森林不足n-1条边时，不能声称是生成树。
    return str(total) if used==n-1 else 'DISCONNECTED'


if __name__=='__main__':
    print(solve(sys.stdin.read()))
