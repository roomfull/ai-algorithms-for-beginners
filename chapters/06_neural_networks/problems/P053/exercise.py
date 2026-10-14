"""P053：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math



def solve(raw):
    lines = raw.strip().splitlines()
    head = lines[0].split()
    n, c = map(int, head[:2])
    eps = float(head[2])
    binary_rows = [line.split() for line in lines[1:n+1]]
    multiclass_rows = [line.split() for line in lines[n+1:2*n+1]]
    # 两种行格式不同，标签用int，概率用float。
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
