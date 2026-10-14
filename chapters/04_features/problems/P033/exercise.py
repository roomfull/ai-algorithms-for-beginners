"""P033 TF-IDF 与 L2 归一化：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 n v norm（norm为0或1）；第2行 v 个互异小写英文字母串，长度1到20；随后 n 行文档，可为空行。1≤n≤100，1≤v≤100；总词数≤2000，词均在词表中，按空白分词。
    # TODO 1：先处理整个语料，得出各词df与IDF。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
