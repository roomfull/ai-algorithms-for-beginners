"""P033：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：存各篇计数字典；由计数字典的键累计df；逐行造TF×IDF向量，norm=1且模长>0时除以模长。
def solve(raw):
    lines = raw.splitlines()
    n, v, norm = map(int, lines[0].split())
    vocab = sorted(lines[1].split())
    docs = []
    df = {word: 0 for word in vocab}
    for line in lines[2:2+n]:
        counts = {}
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1
        docs.append(counts)
        for word in counts:  # 字典键只出现一次，所以是文档频率。
            df[word] += 1
    idf = [math.log((1+n)/(1+df[word]))+1 for word in vocab]
    output = []
    for counts in docs:
        vector = [counts.get(word, 0)*weight for word, weight in zip(vocab, idf)]
        length = math.sqrt(sum(x*x for x in vector))
        if norm == 1 and length > 0:
            vector = [x/length for x in vector]
        output.append(format_row(vector))
    return '\n'.join(output)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
