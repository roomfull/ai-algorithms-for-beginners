"""P073 按行L1范数结构化剪枝：完成后只向标准输出写题目要求的结果。"""
import sys


def solve(raw):
    # 1. 按题面解析输入；注意整数、浮点和精确小数字符串的区别。
    tokens = raw.split()
    # 2. 行L1是绝对值之和，不是普通和。
    # 3. 用(-norm,index)排序，选前keep个。
    # 4. 返回按题目行格式构造的字符串。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
