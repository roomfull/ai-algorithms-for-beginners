"""有向边起点增加出度，终点增加入度。"""
import sys


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,m=next(tokens),next(tokens)
    indegree=[0]*n
    outdegree=[0]*n
    for _ in range(m):
        u,v=next(tokens),next(tokens)
        outdegree[u]+=1
        indegree[v]+=1
    return '\n'.join(f'{indegree[i]} {outdegree[i]}' for i in range(n))


if __name__=='__main__':
    print(solve(sys.stdin.read()))
