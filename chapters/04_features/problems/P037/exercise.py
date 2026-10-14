"""P037 相邻卡方合并分箱：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 b t；随后 b 行：value count0 count1。1≤b≤200，1≤t≤b；value为严格递增互异整数，绝对值≤1000000；两类计数为0到1000000的整数。初始左右界均为value。
    # TODO 1：用 [left,right,count0,count1] 保存一个箱。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
