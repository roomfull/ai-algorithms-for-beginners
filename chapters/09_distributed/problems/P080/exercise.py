"""P080 Microbatch累积与同步SGD：完成后只向标准输出写题目要求的结果。"""
import sys


def solve(raw):
    # 1. 按题面解析输入；注意整数、浮点和精确小数字符串的区别。
    tokens = raw.split()
    # 2. 不能按microbatch个数简单平均，因为每批大小可能不同。
    # 3. 跨worker仍用样本总数作分母，不能再次除worker数。
    # 4. 返回按题目行格式构造的字符串。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
