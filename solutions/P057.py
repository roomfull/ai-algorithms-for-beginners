"""P057：转置卷积散射累加，不是逆运算。"""
import sys


def solve(raw):
    lines = raw.strip().splitlines()
    h, w, kh, kw, stride, pad = map(int, lines[0].split())
    x = [list(map(float, s.split())) for s in lines[1:h+1]]
    kernel = [list(map(float, s.split())) for s in lines[h+1:h+1+kh]]
    oh, ow = (h-1)*stride-2*pad+kh, (w-1)*stride-2*pad+kw
    output = [[0.0]*ow for _ in range(oh)]
    for i in range(h):
        for j in range(w):
            for a in range(kh):
                for b in range(kw):
                    r, c = i*stride-pad+a, j*stride-pad+b
                    if 0 <= r < oh and 0 <= c < ow:
                        output[r][c] += x[i][j]*kernel[a][b]  # 重叠必须累加。
    return '\n'.join(' '.join(format(v, '.12g') for v in r) for r in output)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
