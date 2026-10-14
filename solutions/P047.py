"""P047：固定轮数的全批量逻辑回归训练。"""
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
    n, d, steps = map(int, head[:3])
    lr = float(head[3])
    samples = [list(map(float, s.split())) for s in lines[1:n+1]]
    w = list(map(float, lines[n+1].split()))
    b = float(lines[n+2])
    for _ in range(steps):
        gw = [0.0]*d
        gb = 0.0
        for sample in samples:
            y, x = sample[0], sample[1:]
            residual = sigmoid(sum(a*t for a, t in zip(w, x))+b)-y
            gb += residual
            for j in range(d):
                gw[j] += residual*x[j]
        # 整批梯度算完才更新，所有坐标使用同一旧参数。
        w = [a-lr*g/n for a, g in zip(w, gw)]
        b -= lr*gb/n
    loss = 0.0
    for sample in samples:
        y, x = sample[0], sample[1:]
        z = sum(a*t for a, t in zip(w, x))+b
        loss += max(z, 0)+math.log1p(math.exp(-abs(z)))-y*z
    return ' '.join(format(v, '.12g') for v in w)+f'\n{b:.12g}\n{loss/n:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
