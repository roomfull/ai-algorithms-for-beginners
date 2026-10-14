"""P058：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math



def solve(raw):
    lines = raw.strip().splitlines()
    real, z, a, g, w, b, lr_d, lr_g = map(float, raw.split())
    # 先保存fake，再计算D梯度和新w,b，最后计算G梯度。
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
