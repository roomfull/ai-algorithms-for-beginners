"""P030 小型确定性 SMOTE：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 n d k g；随后 n 行：0/1标签及 d 个实数特征；再有 g 行：q λ。5≤n≤200，1≤d≤20，1≤g≤200；两类均存在且样本数不等；少数类数 m≥2；1≤k≤m-1，0≤q<k，0≤λ≤1，特征绝对值≤1000000。
    # TODO 1：统计两类数目，取少数类，保留原始下标用于距离并列。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
