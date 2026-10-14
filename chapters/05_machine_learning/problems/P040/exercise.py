"""P040：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math



def solve(raw):
    lines = raw.strip().splitlines()
    n, d, k = map(int, lines[0].split())
    samples = [list(map(int, line.split())) for line in lines[1:n+1]]
    query = list(map(int, lines[n+1].split()))
    # samples[i][0]是标签，samples[i][1:]是特征。
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
