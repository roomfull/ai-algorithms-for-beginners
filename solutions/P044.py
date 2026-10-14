"""P044：完整Lloyd迭代，无随机初始化。"""
import sys
from fractions import Fraction


def assign(points, centers):
    # 原字符串、中心及容差都保持Fraction，等距和近距离平票均精确。
    labels = []
    for point in points:
        distances = [sum((x-z)**2 for x, z in zip(point, center)) for center in centers]
        minimum = min(distances)
        labels.append(next(i for i, v in enumerate(distances) if v <= minimum+Fraction("1e-12")))
    return labels


def solve(raw):
    lines = raw.strip().splitlines()
    head = lines[0].split()
    n, d, c, max_iter = map(int, head[:4])
    tol = Fraction(head[4])
    points = [list(map(Fraction, s.split())) for s in lines[1:n+1]]
    centers = [list(map(Fraction, s.split())) for s in lines[n+1:n+1+c]]
    for _ in range(max_iter):
        labels = assign(points, centers)
        groups = [[] for _ in range(c)]
        for point, label in zip(points, labels):
            groups[label].append(point)
        updated = [[sum(p[j] for p in group)/len(group) for j in range(d)]
                   if group else centers[i][:] for i, group in enumerate(groups)]
        change = max(abs(old-new) for a, b in zip(centers, updated) for old, new in zip(a, b))
        centers = updated  # 判停前也必须保留这次更新。
        if change <= tol:
            break
    labels = assign(points, centers)  # 对最终中心再分配，包含达到上限的情况。
    output = [' '.join(format(float(v), '.12g') for v in center) for center in centers]
    output.append(' '.join(map(str, labels)))
    return '\n'.join(output)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
