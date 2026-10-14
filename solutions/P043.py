"""P043：非空簇取平均，空簇保留。"""
import sys
import math


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, c = map(int, lines[0].split())
    points = [list(map(float, s.split())) for s in lines[1:n+1]]
    old = [list(map(float, s.split())) for s in lines[n+1:n+1+c]]
    labels = list(map(int, lines[n+1+c].split()))
    groups = [[] for _ in range(c)]
    for point, label in zip(points, labels):
        groups[label].append(point)
    centers = []
    for i, group in enumerate(groups):
        # fsum改善小数累加精度；相同小数不会引入累积漂移。
        centers.append([math.fsum(point[j] for point in group)/len(group)
                        for j in range(d)] if group else old[i][:])
    return '\n'.join(' '.join(format(v, '.12g') for v in center) for center in centers)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
