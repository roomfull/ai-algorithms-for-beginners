"""P051：全连接矩阵形状与ReLU。"""
import sys


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, o = map(int, lines[0].split())
    x = [list(map(float, s.split())) for s in lines[1:n+1]]
    w = [list(map(float, s.split())) for s in lines[n+1:n+1+d]]
    b = list(map(float, lines[n+1+d].split()))
    outputs = []
    for point in x:
        result = []
        for j in range(o):
            z = sum(point[t]*w[t][j] for t in range(d))+b[j]
            result.append(max(0.0, z))
        outputs.append(' '.join(format(v, '.12g') for v in result))
    return '\n'.join(outputs)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
