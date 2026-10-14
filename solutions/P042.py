"""P042：给定中心的K-means分配。"""
import sys
from fractions import Fraction


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, c = map(int, lines[0].split())
    points = [list(map(Fraction, s.split())) for s in lines[1:n+1]]
    centers = [list(map(Fraction, s.split())) for s in lines[n+1:n+1+c]]
    # 原字符串、中心及容差都保持Fraction，等距和近距离平票均精确。
    labels = []
    for point in points:
        distances = [sum((x-z)**2 for x, z in zip(point, center)) for center in centers]
        minimum = min(distances)
        # 相对于真正最小值判断容差，然后取首个中心。
        labels.append(next(i for i, distance in enumerate(distances) if distance <= minimum+Fraction("1e-12")))
    return ' '.join(map(str, labels))


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
