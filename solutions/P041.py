"""P041：每个查询独立投票，不修改训练集。"""
import sys


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, k, q = map(int, lines[0].split())
    samples = [list(map(int, s.split())) for s in lines[1:n+1]]
    outputs = []
    for line in lines[n+1:n+1+q]:
        query = list(map(int, line.split()))
        order = sorted((sum((x-z)**2 for x, z in zip(sample[1:], query)), i)
                       for i, sample in enumerate(samples))
        counts = {}  # 查询之间不能累计票数。
        for _, i in order[:k]:
            label = samples[i][0]
            counts[label] = counts.get(label, 0)+1
        outputs.append(str(min(counts, key=lambda v: (-counts[v], v))))
    return '\n'.join(outputs)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
