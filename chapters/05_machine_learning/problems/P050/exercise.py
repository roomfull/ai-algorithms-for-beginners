"""P050：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math


def solve(raw):
    lines = raw.strip().splitlines()
    n, d, q, max_depth = map(int, lines[0].split())
    rows = []
    for line in lines[1:n+1]:
        tokens = line.split()
        rows.append((int(tokens[0]), list(map(float, tokens[1:]))))
    queries = [list(map(float, line.split())) for line in lines[n+1:n+1+q]]
    # 建议分别写gini、train、predict函数；根节点深度为0。
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
