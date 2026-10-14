"""P034 等宽分箱：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 n k；第2行 n 个整数。1≤n≤200，1≤k≤200，值绝对值≤1000000。k可以大于n，因此空箱合法。
    # TODO 1：求最小、最大值，先处理全部相等情况。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
