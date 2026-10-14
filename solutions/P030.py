"""P030：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：用Fraction(原始坐标文本)求精确平方距离，不能先转float；排序后预存前 k 个邻居，第 r 条按 r % m 与 q 选点，转float后插值输出。
from fractions import Fraction


def solve(raw):
    lines = raw.splitlines()
    n, d, k, g = map(int, lines[0].split())
    samples = []
    for i, line in enumerate(lines[1:n+1]):
        parts = line.split()
        # 从原文本解析有理数，保留输入十进制坐标的精确距离关系。
        samples.append((int(parts[0]), list(map(Fraction, parts[1:])), i))
    counts = [sum(label == c for label, _, _ in samples) for c in (0, 1)]
    minority_label = 0 if counts[0] < counts[1] else 1
    minority = [(x, index) for label, x, index in samples if label == minority_label]
    neighbors = []
    for a, (x, original_index) in enumerate(minority):
        distances = []
        for b, (z, neighbor_index) in enumerate(minority):
            if a != b:  # 只排除同一个样本，重复坐标仍然合法。
                dist = sum((x[j]-z[j])**2 for j in range(d))
                distances.append((dist, neighbor_index, b))
        distances.sort()
        neighbors.append([b for _, _, b in distances[:k]])
    output = []
    for r, line in enumerate(lines[n+1:n+1+g]):
        q_text, lam_text = line.split()
        q, lam = int(q_text), float(lam_text)
        base = r % len(minority)
        # 邻居已经用精确距离确定；输出插值允许题面规定的浮点误差。
        x = list(map(float, minority[base][0]))
        z = list(map(float, minority[neighbors[base][q]][0]))
        output.append(format_row(x[j]+lam*(z[j]-x[j]) for j in range(d)))
    return '\n'.join(output)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
