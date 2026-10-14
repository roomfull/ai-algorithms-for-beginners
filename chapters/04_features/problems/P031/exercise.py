"""P031 原始词频 TF：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 v；第2行 v 个互异小写英文字母串，长度1到20；第3行为文档（可为空行）。1≤v≤100；文档最多2000个词，所有词都在词表中。
    # TODO 1：先把词表排序，文档用 split() 分成词。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
