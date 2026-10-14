"""P074 对称int8量化与反量化：完成后只向标准输出写题目要求的结果。"""
import sys


def solve(raw):
    # 1. 按题面解析输入；注意整数、浮点和精确小数字符串的区别。
    tokens = raw.split()
    # 2. 先找maxabs，零向量需单独规定scale。
    # 3. round(Fraction)可以精确实现ties-to-even；不要先把比值转float。
    # 4. 返回按题目行格式构造的字符串。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
