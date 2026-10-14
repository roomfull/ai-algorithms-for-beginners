"""P052：先减每行最大值，再归一化指数。"""
import sys
import math


def solve(raw):
    lines = raw.strip().splitlines()
    n, c = map(int, lines[0].split())
    outputs = []
    for line in lines[1:n+1]:
        logits = list(map(float, line.split()))
        maximum = max(logits)
        e = [math.exp(v-maximum) for v in logits]
        total = math.fsum(e)
        outputs.append(' '.join(format(v/total, '.12g') for v in e))
    return '\n'.join(outputs)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
