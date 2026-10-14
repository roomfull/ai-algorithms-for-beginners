# P005 if 分数分类；独立运行，无其他答案依赖。
score = int(input())
# 从高到低判断，避免优秀先被及格条件截住。
if score >= 90:
    print("EXCELLENT")
elif score >= 60:
    print("PASS")
else:
    print("FAIL")
