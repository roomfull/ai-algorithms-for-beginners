"""卷积、ReLU 与平均池化特征：独立参考解。"""
import sys

def solve(raw):
    it=iter(raw.split()); h,w,s,p=[int(next(it)) for _ in range(4)]
    image=[[float(next(it)) for _ in range(w)] for _ in range(h)]
    kernel=[[float(next(it)) for _ in range(s)] for _ in range(s)]
    bias=float(next(it)); H,W=h-s+1,w-s+1
    activation=[]
    for i in range(H):
        row=[]
        for j in range(W):
            z=bias+sum(image[i+u][j+v]*kernel[u][v] for u in range(s) for v in range(s))
            row.append(max(0.0,z))
        activation.append(row)
    oh,ow=H//p,W//p
    rows=[f'{oh} {ow}']
    for i in range(oh):
        values=[sum(activation[i*p+u][j*p+v] for u in range(p) for v in range(p))/(p*p) for j in range(ow)]
        rows.append(' '.join(f'{value:.12g}' for value in values))
    return '\n'.join(rows)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
