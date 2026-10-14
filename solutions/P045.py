"""P045：稳定sigmoid与分类。"""
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
    points = [list(map(float, s.split())) for s in lines[1:n+1]]
    w = list(map(float, lines[n+1].split()))
    b = float(lines[n+2])
    result = []
    for x in points:
        p = sigmoid(sum(a*t for a, t in zip(w, x))+b)
        result.extend([f'{p:.12g}', str(int(p >= 0.5))])
    return '\n'.join(result)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
