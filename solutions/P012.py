# P012 函数与 return；独立运行，无其他答案依赖。
def square(x):
    # 返回计算值，交由调用者决定怎样输出。
    return x * x


a = int(input())
b = int(input())
print(square(a))
print(square(b))
