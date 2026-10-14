"""P039：KNN距离排序，单文件可运行。"""
import sys


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, k = map(int, lines[0].split())
    points = [list(map(int, s.split())) for s in lines[1:1+n]]
    query = list(map(int, lines[n+1].split()))
    # 输入是整数，平方距离与下标的二元组可以精确比较。
    order = sorted((sum((x-q)**2 for x, q in zip(point, query)), i)
                   for i, point in enumerate(points))
    return ' '.join(str(i) for distance, i in order[:k])


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
