"""P057：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math


def solve(raw):
    lines = raw.strip().splitlines()
    h, w, kh, kw, stride, pad = map(int, lines[0].split())
    x = [list(map(float, line.split())) for line in lines[1:h+1]]
    kernel = [list(map(float, line.split())) for line in lines[h+1:h+1+kh]]
    # 初始化输出为全0，散射累加，不能覆盖。
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
