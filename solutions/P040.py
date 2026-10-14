"""P040：先选邻居，再按标签多数投票。"""
import sys


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, k = map(int, lines[0].split())
    samples = [list(map(int, s.split())) for s in lines[1:1+n]]
    query = list(map(int, lines[n+1].split()))
    order = sorted((sum((x-q)**2 for x, q in zip(sample[1:], query)), i)
                   for i, sample in enumerate(samples))
    counts = {}
    for _, i in order[:k]:
        label = samples[i][0]
        counts[label] = counts.get(label, 0)+1
    # 负票数使票多者排前；同票时小整数标签排前。
    return str(min(counts, key=lambda label: (-counts[label], label)))


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
