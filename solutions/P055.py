"""P055：单通道二维互相关，无核翻转。"""
import sys


def solve(raw):
    lines = raw.strip().splitlines()
    h, w, kh, kw, stride, pad = map(int, lines[0].split())
    x = [list(map(float, s.split())) for s in lines[1:h+1]]
    kernel = [list(map(float, s.split())) for s in lines[h+1:h+1+kh]]
    padded = [[0.0]*(w+2*pad) for _ in range(h+2*pad)]
    for i in range(h):
        for j in range(w):
            padded[i+pad][j+pad] = x[i][j]
    oh = (h+2*pad-kh)//stride+1
    ow = (w+2*pad-kw)//stride+1
    output = [[0.0]*ow for _ in range(oh)]
    for i in range(oh):
        for j in range(ow):
            for a in range(kh):
                for b in range(kw):
                    output[i][j] += padded[i*stride+a][j*stride+b]*kernel[a][b]
    return '\n'.join(' '.join(format(v, '.12g') for v in r) for r in output)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
