"""P027 先划分再拟合训练统计量：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 n d t；随后 n 行 d 个实数；最后一行 n 个互异下标，恰好是0到n-1的排列。2≤n≤200，1≤d≤20，1≤t<n；实数绝对值≤1000000。
    # TODO 1：按照下标排列，取前 t 行作为训练。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
