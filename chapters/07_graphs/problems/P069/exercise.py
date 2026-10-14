"""P069 PageRank迭代至收敛：完成后只向标准输出写题目要求的结果。"""
import sys
from fractions import Fraction


def solve(raw):
    # 1. 按题面解析输入；注意整数、浮点和精确小数字符串的区别。
    tokens = raw.split()
    # 2. 从原字符串构造Fraction(alpha)、Fraction(tol)，均匀初值用Fraction(1,n)。
    # 3. 所有概率流与delta保持Fraction，先求delta再用q替换p；输出时才转float。
    # 4. 返回按题目行格式构造的字符串。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
