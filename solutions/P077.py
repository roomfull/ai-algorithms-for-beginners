"""连续半开区间分片；余数给最前面的worker。"""
import sys


def solve(raw):
    n,workers=map(int,raw.split())
    base,extra=divmod(n,workers)
    start=0
    output=[]
    for i in range(workers):
        length=base+int(i<extra)
        end=start+length
        output.append(f'{start} {end}')
        start=end
    return '\n'.join(output)


if __name__=='__main__':
    print(solve(sys.stdin.read()))
