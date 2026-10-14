"""P053：概率形式的clip BCE和多分类CE。"""
import sys
import math


def solve(raw):
    lines = raw.strip().splitlines()
    head = lines[0].split()
    n, c = map(int, head[:2])
    eps = float(head[2])
    bce = 0.0
    for line in lines[1:n+1]:
        label, probability = line.split()
        y = int(label)
        p = min(1-eps, max(eps, float(probability)))
        bce += -y*math.log(p)-(1-y)*math.log1p(-p)
    ce = 0.0
    for line in lines[n+1:2*n+1]:
        tokens = line.split()
        target = int(tokens[0])
        probabilities = list(map(float, tokens[1:]))
        p = min(1-eps, max(eps, probabilities[target]))
        ce -= math.log(p)  # 只看真实类别，不取argmax。
    return f'{bce/n:.12g} {ce/n:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
