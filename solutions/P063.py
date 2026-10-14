"""并查集：路径折半与按大小合并。"""
import sys


def solve(raw):
    tokens=iter(map(int,raw.split()))
    n,q=next(tokens),next(tokens)
    parent=list(range(n))
    size=[1]*n

    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]  # 路径折半，缩短以后查询的路径。
            x=parent[x]
        return x

    output=[]
    for _ in range(q):
        kind,a,b=next(tokens),next(tokens),next(tokens)
        ra,rb=find(a),find(b)
        if kind==1:
            output.append(str(int(ra==rb)))
        elif ra!=rb:
            if size[ra]<size[rb]:
                ra,rb=rb,ra
            parent[rb]=ra
            size[ra]+=size[rb]
    return '\n'.join(output)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
