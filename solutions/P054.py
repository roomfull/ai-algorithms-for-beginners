"""P054：单层sigmoid网络的整批梯度更新。"""
import sys
import math


def sigmoid(z):
    if z >= 0:
        return 1/(1+math.exp(-z))
    e = math.exp(z)
    return e/(1+e)


def solve(raw):
    lines = raw.strip().splitlines()
    head = lines[0].split()
    n, d = map(int, head[:2])
    lr = float(head[2])
    samples = [list(map(float, s.split())) for s in lines[1:n+1]]
    w = list(map(float, lines[n+1].split()))
    b = float(lines[n+2])
    gw, gb, loss = [0.0]*d, 0.0, 0.0
    for sample in samples:
        y, x = sample[0], sample[1:]
        z = sum(a*t for a, t in zip(w, x))+b
        # 链式规则把sigmoid+BCE简化为残差p-y。
        residual = sigmoid(z)-y
        gb += residual
        for j in range(d):
            gw[j] += residual*x[j]
        loss += max(z, 0)+math.log1p(math.exp(-abs(z)))-y*z
    updated = [a-lr*g/n for a, g in zip(w, gw)]
    new_b = b-lr*gb/n
    return f'{loss/n:.12g}\n'+' '.join(format(v, '.12g') for v in updated)+f'\n{new_b:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
