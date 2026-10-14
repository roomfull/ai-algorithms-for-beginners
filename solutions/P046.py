"""P046：稳定BCE与整批平均梯度。"""
import sys
import math


def sigmoid(z):
    if z >= 0:
        return 1/(1+math.exp(-z))
    e = math.exp(z)
    return e/(1+e)


def solve(raw):
    lines = raw.strip().splitlines()
    n, d = map(int, lines[0].split())
    samples = [list(map(float, s.split())) for s in lines[1:n+1]]
    w = list(map(float, lines[n+1].split()))
    b = float(lines[n+2])
    loss, gb = 0.0, 0.0
    gw = [0.0]*d
    for sample in samples:
        y, x = sample[0], sample[1:]
        z = sum(a*t for a, t in zip(w, x))+b
        residual = sigmoid(z)-y
        # 从logit求BCE，概率舍入为0或1也不取log(0)。
        loss += max(z, 0)+math.log1p(math.exp(-abs(z)))-y*z
        gb += residual
        for j in range(d):
            gw[j] += residual*x[j]
    return f'{loss/n:.12g}\n'+ ' '.join(format(v/n, '.12g') for v in gw)+f'\n{gb/n:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
