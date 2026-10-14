"""P028：独立参考解。"""
import sys
import math


def format_row(values):
    return " ".join(format(v, ".12g") for v in values)


# 算法关键：先复制原输出列表，再按类0、类1循环补足；首行输出最终行数。
def solve(raw):
    lines = raw.splitlines()
    n, d, target0, target1 = map(int, lines[0].split())
    rows = [tuple(map(int, line.split())) for line in lines[1:n+1]]
    groups = [[row for row in rows if row[0] == label] for label in (0, 1)]
    output = rows.copy()
    for label, target in enumerate((target0, target1)):
        originals = groups[label]
        for r in range(target-len(originals)):
            output.append(originals[r % len(originals)])
    return '\n'.join([str(len(output))] + [' '.join(map(str, row)) for row in output])


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
