"""P050：多层递归CART分类树。"""
import sys
from fractions import Fraction


def counts_of(rows):
    counts = {}
    for y, x in rows:
        counts[y] = counts.get(y, 0)+1
    return counts


def gini(rows):
    return 1-sum((count/len(rows))**2 for count in counts_of(rows).values())


def train(rows, d, max_depth, depth=0):
    counts = counts_of(rows)
    majority = min(counts, key=lambda y: (-counts[y], y))
    # 叶子用单元素元组；分裂节点用(feature,threshold,left,right)。
    if depth >= max_depth or len(counts) == 1:
        return (majority,)
    candidates = []
    for j in range(d):
        values = sorted(set(x[j] for y, x in rows))
        for a, b in zip(values, values[1:]):
            threshold = (a+b)/2  # Fraction中点与查询严格比较，不为边界加epsilon。
            left = [(y, x) for y, x in rows if x[j] <= threshold]
            right = [(y, x) for y, x in rows if x[j] > threshold]
            score = (len(left)*gini(left)+len(right)*gini(right))/len(rows)
            candidates.append((score, j, threshold))
    if not candidates:
        return (majority,)
    minimum = min(item[0] for item in candidates)
    score, j, threshold = next(item for item in candidates if item[0] <= minimum+1e-12)
    if gini(rows)-score <= 1e-12:
        return (majority,)  # 无足够增益终止，防止无意义递归。
    left = [(y, x) for y, x in rows if x[j] <= threshold]
    right = [(y, x) for y, x in rows if x[j] > threshold]
    return (j, threshold, train(left, d, max_depth, depth+1),
            train(right, d, max_depth, depth+1))


def predict(tree, x):
    while len(tree) != 1:
        j, threshold, left, right = tree
        tree = left if x[j] <= threshold else right
    return tree[0]


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, q, max_depth = map(int, lines[0].split())
    rows = []
    for line in lines[1:n+1]:
        tokens = line.split()
        rows.append((int(tokens[0]), list(map(Fraction, tokens[1:]))))
    queries = [list(map(Fraction, line.split())) for line in lines[n+1:n+1+q]]
    tree = train(rows, d, max_depth)
    return '\n'.join(str(predict(tree, x)) for x in queries)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
