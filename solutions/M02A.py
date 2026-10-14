"""TF-IDF 文本余弦检索：独立参考解。"""
import sys
import math

def solve(raw):
    it=iter(map(int,raw.split())); n,v,k=next(it),next(it),next(it)
    docs=[[next(it) for _ in range(v)] for _ in range(n)]
    query=[next(it) for _ in range(v)]
    df=[sum(row[j]>0 for row in docs) for j in range(v)]
    idf=[1+math.log((n+1)/(count+1)) for count in df]
    q=[query[j]*idf[j] for j in range(v)]
    qnorm=math.sqrt(sum(value*value for value in q))
    scores=[]
    for row in docs:
        weighted=[row[j]*idf[j] for j in range(v)]
        norm=math.sqrt(sum(value*value for value in weighted))
        score=sum(weighted[j]*q[j] for j in range(v))/(norm*qnorm) if norm and qnorm else 0.0
        scores.append(score)
    # 只有排序键舍入；输出保留未舍入分数。
    indices=sorted(range(n),key=lambda i:(-round(scores[i],12),i))[:k]
    return ' '.join(map(str,indices))+'\n'+' '.join(f'{scores[i]:.12g}' for i in indices)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
