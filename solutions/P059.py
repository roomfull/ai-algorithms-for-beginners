"""无向边登记两端，邻居升序。"""
import sys


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=next(tokens),next(tokens)
        adj[u].append(v)
        adj[v].append(u)
    # 孤立点也有一行，只是邻居列表为空。
    return '\n'.join(' '.join(map(str,[i,len(adj[i])]+sorted(adj[i]))) for i in range(n))


if __name__=='__main__':
    print(solve(sys.stdin.read()))
