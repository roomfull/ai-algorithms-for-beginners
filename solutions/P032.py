"""P032：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：df初始化为0，遍历 set(文档词) 对df加1；按字典序代入 math.log((1+n)/(1+df))+1。
def solve(raw):
    lines = raw.splitlines()
    n, v = map(int, lines[0].split())
    vocab = sorted(lines[1].split())
    df = {word: 0 for word in vocab}
    for line in lines[2:2+n]:
        for word in set(line.split()):
            df[word] += 1
    return format_row(math.log((1+n)/(1+df[word]))+1 for word in vocab)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
