"""P048：标签熵与Gini。"""
import sys
import math


def solve(raw):
    labels = list(map(int, raw.split()))
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0)+1
    probabilities = [count/len(labels) for count in counts.values()]
    entropy = -sum(p*math.log2(p) for p in probabilities)
    gini = 1-sum(p*p for p in probabilities)
    return f'{entropy:.12g} {gini:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
