"""P042：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math
from fractions import Fraction



def solve(raw):
    lines = raw.strip().splitlines()
    n, d, c = map(int, lines[0].split())
    points = [list(map(Fraction, line.split())) for line in lines[1:n+1]]
    centers = [list(map(Fraction, line.split())) for line in lines[n+1:n+1+c]]
    # 平票阈值使用Fraction("1e-12")，不要使用浮点1e-12。
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
