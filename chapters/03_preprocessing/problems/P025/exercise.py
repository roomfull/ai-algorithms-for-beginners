"""P025 Min-Max 列缩放：先阅读同目录 README.md。"""
import sys
from fractions import Fraction


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 n d；随后 n 行，每行 d 个实数。1≤n≤200，1≤d≤20；绝对值≤1000000。 数值使用普通十进制写法（不使用指数），小数点后最多12位。
    # TODO 1：先用Fraction(原始数值字符串)保存十进制精度，不能先转float。列最大值与最小值分别计算。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
