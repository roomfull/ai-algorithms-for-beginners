"""P053：概率形式的clip BCE和多分类CE。"""
import sys
import math


def negative_log_clipped(probability, eps):
    # 直接裁剪真实类别概率，避免1-(1-eps)丢失eps有效位。
    if probability <= eps:
        return -math.log(eps)
    if probability >= 1-eps:
        return -math.log1p(-eps)  # 不先构造舍入后的1-eps再取log。
    return -math.log(probability)


def solve(raw):
    lines = raw.strip().splitlines()
    head = lines[0].split()
    n, c = map(int, head[:2])
    eps = float(head[2])
    bce = 0.0
    for line in lines[1:n+1]:
        label, probability = line.split()
        y = int(label)
        p = float(probability)
        true_probability = p if y == 1 else 1-p
        bce += negative_log_clipped(true_probability, eps)
    ce = 0.0
    for line in lines[n+1:2*n+1]:
        tokens = line.split()
        target = int(tokens[0])
        probabilities = list(map(float, tokens[1:]))
        ce += negative_log_clipped(probabilities[target], eps)  # 只看真实类别，不取argmax。
    return f'{bce/n:.12g} {ce/n:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
