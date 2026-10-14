"""P031：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：遍历文档对 counts[word] 加1；最后按 sorted(vocab) 查询 counts.get(word,0)。
def solve(raw):
    lines = raw.splitlines()
    v = int(lines[0])
    vocab = sorted(lines[1].split())
    words = lines[2].split() if len(lines) > 2 else []
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return ' '.join(str(counts.get(word, 0)) for word in vocab)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
