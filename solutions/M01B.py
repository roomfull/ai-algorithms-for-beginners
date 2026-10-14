"""机房网络布线的最小总成本：独立参考解。"""
import sys

def solve(raw):
    it=iter(map(int,raw.split())); n,m=next(it),next(it)
    edges=[]
    for index in range(m):
        u,v,w=next(it),next(it),next(it)
        edges.append((w,index,u,v))
    parent=list(range(n)); size=[1]*n
    def find(u):
        while parent[u]!=u:
            parent[u]=parent[parent[u]]
            u=parent[u]
        return u
    total=count=0
    for w,index,u,v in sorted(edges):
        a,b=find(u),find(v)
        if a==b: continue
        if size[a]<size[b]: a,b=b,a
        parent[b]=a; size[a]+=size[b]
        total+=w; count+=1
    return str(total if count==n-1 else -1)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
