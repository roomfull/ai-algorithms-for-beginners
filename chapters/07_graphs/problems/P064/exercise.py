"""P064 无向简单图三角形计数：完成后只向标准输出写题目要求的结果。"""
import sys


def solve(raw):
    # 1. 按题面解析输入；注意整数、浮点和精确小数字符串的区别。
    tokens = raw.split()
    # 2. 只枚举a<b<c。
    # 3. 用邻接集合快速判断一条边是否存在。
    # 4. 返回按题目行格式构造的字符串。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
