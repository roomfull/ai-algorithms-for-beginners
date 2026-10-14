"""P044：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math


def solve(raw):
    lines = raw.strip().splitlines()
    head = lines[0].split()
    n, d, c, max_iter = map(int, head[:4])
    tol = float(head[4])
    points = [list(map(float, line.split())) for line in lines[1:n+1]]
    centers = [list(map(float, line.split())) for line in lines[n+1:n+1+c]]
    # 建议写assign函数，循环后也调用它。
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
