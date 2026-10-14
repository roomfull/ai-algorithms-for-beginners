"""P032 平滑 IDF：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：首行 n v；第2行 v 个互异小写英文字母串，长度1到20；随后 n 行为文档，空行表示空文档。1≤n≤100，1≤v≤100；所有文档合计最多2000词，均在词表中。按空白分词。
    # TODO 1：对每篇文档先去重，再增加文档频率。
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
