"""P047：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math



def solve(raw):
    lines = raw.strip().splitlines()
    head = lines[0].split()
    n, d, steps = map(int, head[:3])
    lr = float(head[3])
    samples = [list(map(float, line.split())) for line in lines[1:n+1]]
    weights = list(map(float, lines[n+1].split()))
    bias = float(lines[n+2])
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
