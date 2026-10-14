"""P028 确定性类别过采样：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 n d target0 target1；随后 n 行：标签与 d 个整数特征。2≤n≤200，1≤d≤20；两类都至少1条；各 target 在该类原始数到500之间，特征绝对值≤1000000。
    # TODO 1：分别记录两类原样本，保持各自输入顺序。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
