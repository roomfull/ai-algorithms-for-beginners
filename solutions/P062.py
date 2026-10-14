"""显式栈DFS；按最小顶点的顺序标记连通分量。"""
import sys


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=next(tokens),next(tokens)
        adj[u].append(v)
        adj[v].append(u)
    label=[-1]*n
    count=0
    for root in range(n):
        if label[root]!=-1:
            continue
        label[root]=count
        stack=[root]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if label[v]==-1:
                    label[v]=count
                    stack.append(v)
        count+=1
    return str(count)+'\n'+' '.join(map(str,label))


if __name__=='__main__':
    print(solve(sys.stdin.read()))
