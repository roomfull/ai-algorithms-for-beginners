"""P056：互相关加偏置→ReLU→最大池化。"""
import sys


def solve(raw):
    lines = raw.strip().splitlines()
    h, w, kh, kw, stride, pad, ph, pw, ps = map(int, lines[0].split())
    x = [list(map(float, s.split())) for s in lines[1:h+1]]
    kernel = [list(map(float, s.split())) for s in lines[h+1:h+1+kh]]
    bias = float(lines[h+1+kh])
    padded = [[0.0]*(w+2*pad) for _ in range(h+2*pad)]
    for i in range(h):
        for j in range(w):
            padded[i+pad][j+pad] = x[i][j]
    oh, ow = (h+2*pad-kh)//stride+1, (w+2*pad-kw)//stride+1
    relu = [[0.0]*ow for _ in range(oh)]
    for i in range(oh):
        for j in range(ow):
            value = bias
            for a in range(kh):
                for b in range(kw):
                    value += padded[i*stride+a][j*stride+b]*kernel[a][b]
            relu[i][j] = max(0.0, value)
    pool_h, pool_w = (oh-ph)//ps+1, (ow-pw)//ps+1
    pooled = [[0.0]*pool_w for _ in range(pool_h)]
    for i in range(pool_h):
        for j in range(pool_w):
            # 池化stride与卷积stride分开使用。
            pooled[i][j] = max(relu[i*ps+a][j*ps+b] for a in range(ph) for b in range(pw))
    return '\n'.join(' '.join(format(v, '.12g') for v in r) for r in pooled)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
