"""P029 SMOTE 线段插值：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行维数 d；第2行 d 个实数 x；第3行 d 个实数 z；第4行 λ。1≤d≤20，0≤λ≤1，特征绝对值≤1000000。
    # TODO 1：逐坐标处理，所有坐标使用同一个 λ。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
