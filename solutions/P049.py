"""P049：连续特征最佳Gini二叉切分。"""
import sys


def gini(labels):
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0)+1
    return 1-sum((count/len(labels))**2 for count in counts.values())


def solve(raw):
    lines = raw.strip().splitlines()
    n, d = map(int, lines[0].split())
    rows = []
    for line in lines[1:n+1]:
        tokens = line.split()
        rows.append((int(tokens[0]), list(map(float, tokens[1:]))))
    candidates = []
    for j in range(d):
        values = sorted(set(x[j] for y, x in rows))
        for a, b in zip(values, values[1:]):
            threshold = (a+b)/2
            left = [y for y, x in rows if x[j] <= threshold]
            right = [y for y, x in rows if x[j] > threshold]
            score = (len(left)*gini(left)+len(right)*gini(right))/n
            candidates.append((score, j, threshold))
    if not candidates:
        return f'-1\n0 {gini([y for y, x in rows]):.12g}'
    minimum = min(score for score, _, _ in candidates)
    # 候选已按feature、threshold升序生成；按全局最小评分筛选。
    score, j, threshold = next(item for item in candidates if item[0] <= minimum+1e-12)
    return f'{j}\n{threshold:.12g} {score:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
