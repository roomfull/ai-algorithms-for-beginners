"""维护第 01–02 章；--cases 只写先验手算案例，--content 写教学与实现。"""
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]
PYTHON = "https://docs.python.org/3.11/tutorial/"
NUMPY = "https://numpy.org/doc/stable/user/absolute_beginners.html"

# 所有 expected 均直接录入手算结果；不执行或导入 solutions 计算答案。
DATA = [
    ("第一行固定输出", "text", [("", "Hello, Python!\n"), ("abc\n", "Hello, Python!\n"), ("123\n", "Hello, Python!\n"), ("你好\n", "Hello, Python!\n"), ("1\n2\n", "Hello, Python!\n")]),
    ("变量与四则运算", "float", [("8\n2\n", "10\n6\n16\n4\n"), ("3\n4\n", "7\n-1\n12\n0.75\n"), ("0\n5\n", "5\n-5\n0\n0\n"), ("-6\n3\n", "-3\n-9\n-18\n-2\n"), ("-4\n-2\n", "-6\n-2\n8\n2\n")]),
    ("字符串拼接", "text", [("小明\nPython\n", "小明正在学习Python\n"), ("A\nAI\n", "A正在学习AI\n"), ("\n数学\n", "正在学习数学\n"), ("李 华\n数据 科学\n", "李 华正在学习数据 科学\n"), ("Alice\n\n", "Alice正在学习\n")]),
    ("input 与数值转换", "float", [("3\n2.5\n", "7.5\n"), ("0\n8.1\n", "0\n"), ("2\n0.25\n", "0.5\n"), ("10\n1.2\n", "12\n"), ("1\n0\n", "0\n")]),
    ("if 分数分类", "text", [("60\n", "PASS\n"), ("59\n", "FAIL\n"), ("90\n", "EXCELLENT\n"), ("89\n", "PASS\n"), ("0\n", "FAIL\n"), ("100\n", "EXCELLENT\n")]),
    ("for 累加", "int", [("4\n", "10\n"), ("0\n", "0\n"), ("1\n", "1\n"), ("5\n", "15\n"), ("10\n", "55\n")]),
    ("while 计数", "int", [("7\n", "3\n"), ("0\n", "0\n"), ("1\n", "0\n"), ("2\n", "1\n"), ("10\n", "5\n")]),
    ("列表筛选", "text", [("1 -2 3 0 -4\n", "1 3\n"), ("0 -1 -2\n", "EMPTY\n"), ("5\n", "5\n"), ("2 2 -3 1\n", "2 2 1\n"), ("-8\n", "EMPTY\n")]),
    ("字典词频", "int", [("cat dog cat\ncat\n", "2\n"), ("a b c\nx\n", "0\n"), ("hi hi hi\nhi\n", "3\n"), ("A a A\na\n", "1\n"), ("one\none\n", "1\n")]),
    ("集合去重计数", "int", [("1 2 1 3 2\n", "3\n"), ("7\n", "1\n"), ("0 0 0\n", "1\n"), ("-1 1 -1 0\n", "3\n"), ("1 2 3 4\n", "4\n")]),
    ("排序与平票", "text", [("3\nBob 80\nAmy 90\nZoe 90\n", "Amy 90\nZoe 90\nBob 80\n"), ("1\nSolo 0\n", "Solo 0\n"), ("2\nz 100\na 100\n", "a 100\nz 100\n"), ("3\nb 1\na 2\nc 3\n", "c 3\na 2\nb 1\n"), ("2\na 59\nb 60\n", "b 60\na 59\n")]),
    ("函数与 return", "int", [("3\n4\n", "9\n16\n"), ("0\n-2\n", "0\n4\n"), ("1\n1\n", "1\n1\n"), ("-3\n5\n", "9\n25\n"), ("10\n-10\n", "100\n100\n")]),
    ("二维列表行和", "int", [("2\n1 2 3\n4 5 6\n", "6\n15\n"), ("1\n-1 0 1\n", "0\n"), ("3\n2\n3\n4\n", "2\n3\n4\n"), ("2\n0 0\n-2 -3\n", "0\n-5\n"), ("1\n7\n", "7\n")]),
    ("多组数据输入输出验收", "int", [("2\n1 2 3\n-1 5\n", "6\n4\n"), ("1\n0\n", "0\n"), ("3\n1\n2\n3\n", "1\n2\n3\n"), ("2\n-2 -3\n0 0\n", "-5\n0\n"), ("1\n10 -10 4 6\n", "10\n")]),
    ("求和与均值双实现", "float", [("1 2 3 4\n", "10 2.5\n10 2.5\n"), ("5\n", "5 5\n5 5\n"), ("-2 0 2\n", "0 0\n0 0\n"), ("0.5 1.5\n", "2 1\n2 1\n"), ("-3 -1\n", "-4 -2\n-4 -2\n")]),
    ("总体方差", "float", [("1 2 3\n", "0.6666666666666666\n"), ("7\n", "0\n"), ("2 2 2\n", "0\n"), ("-2 2\n", "4\n"), ("0 2 4 6\n", "5\n")]),
    ("欧氏距离", "float", [("0 0\n3 4\n", "5\n"), ("1 2\n1 2\n", "0\n"), ("-1\n2\n", "3\n"), ("0 0 0\n1 2 2\n", "3\n"), ("1 1\n2 2\n", "1.4142135623730951\n")]),
    ("点积", "float", [("1 2 3\n4 5 6\n", "32\n"), ("1 0\n0 1\n", "0\n"), ("-2 3\n4 -1\n", "-11\n"), ("0\n9\n", "0\n"), ("0.5 2\n2 0.5\n", "2\n")]),
    ("矩阵乘法", "float", [("2 3 2\n1 2 3\n4 5 6\n7 8\n9 10\n11 12\n", "58 64\n139 154\n"), ("1 1 1\n3\n-2\n", "-6\n"), ("2 2 2\n1 0\n0 1\n2 3\n4 5\n", "2 3\n4 5\n"), ("1 2 3\n0 0\n1 2 3\n4 5 6\n", "0 0 0\n"), ("2 1 2\n2\n-1\n3 4\n", "6 8\n-3 -4\n")]),
    ("shape 与 reshape", "float", [("2 3\n1 2 3 4 5 6\n", "2 3\n1 2 3\n4 5 6\n"), ("1 3\n7 8 9\n", "1 3\n7 8 9\n"), ("3 1\n7 8 9\n", "3 1\n7\n8\n9\n"), ("2 2\n-1 0 1 2\n", "2 2\n-1 0\n1 2\n"), ("1 1\n0.5\n", "1 1\n0.5\n")]),
    ("索引与广播", "float", [("2 2\n1 2\n3 4\n10 20\n100 200\n", "11 22\n13 24\n101 102\n203 204\n"), ("1 3\n1 2 3\n0 10 20\n5\n", "1 12 23\n6 7 8\n"), ("3 1\n1\n2\n3\n10\n0 100 200\n", "11\n12\n13\n1\n102\n203\n"), ("2 3\n0 0 0\n1 1 1\n1 2 3\n4 5\n", "1 2 3\n2 3 4\n4 4 4\n6 6 6\n"), ("1 1\n-1\n2\n3\n", "1\n2\n")]),
    ("axis 行列聚合", "float", [("2 3\n1 2 3\n4 5 6\n", "6 15\n5 7 9\n"), ("1 2\n2 4\n", "6\n2 4\n"), ("3 1\n1\n2\n3\n", "1 2 3\n6\n"), ("2 2\n-1 1\n2 -2\n", "0 0\n1 -1\n"), ("1 1\n0\n", "0\n0\n")]),
]


def write(path, content):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_cases():
    for number, (title, mode, pairs) in enumerate(DATA, 1):
        chapter = "01_python" if number <= 14 else "02_math_numpy"
        pid = f"P{number:03}"
        data = dict(id=pid, chapter=chapter[:2], title=title, mode=mode,
                    requires=[] if number <= 14 else ["numpy"],
                    cases=[dict(name=f"手算案例{i}", input=stdin, expected=stdout)
                           for i, (stdin, stdout) in enumerate(pairs, 1)])
        write(f"chapters/{chapter}/problems/{pid}/cases.json",
              json.dumps(data, ensure_ascii=False, indent=2) + "\n")


LESSONS = [
    dict(
        task="让程序只输出一行 `Hello, Python!`。大小写、逗号、空格和感叹号必须一致。这只是输出格式练习，程序不读取任何输入；五个案例用不同的被忽略 stdin 验证这一点。",
        io="输入：无须读取；即使存在输入也忽略。输出：一行固定文本 `Hello, Python!`。",
        bounds="不对 stdin 作任何假设；标准输出只有指定的一行。",
        learn="先把文件理解为按顺序写下的指令。`print(...)` 是 Python 自带的输出操作；括号内是要显示的内容。英文双引号圈住的是字符串，即原样保存的文字；引号本身不会打印。`#` 到行尾是注释，只给人看。请用英文标点，中文引号不是代码中的引号。",
        hand="这题没有数字计算。`print` 取出引号内的 14 个字符：Hello（5）+逗号（1）+空格（1）+Python（6）+感叹号（1），然后自动换行。输入为空或为 abc 时，输出完全一样。",
        hints=["把目标文字看作一个完整字符串，不需要拆开。", "输出的操作名是 print，内容要放在英文引号内。", "写一条 print 语句，括号内放题面给定的完整文本；不要额外写提示语。"],
        code='''# print 自动在文字末尾补一个换行。
print("Hello, Python!")
''',
        scaffold='''# 第一步：在英文引号内写出目标文字。
# 第二步：用 print 把它输出；不要读 input。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="程序只有一条输出语句，没有读取 stdin 的语句。因此改变输入不会影响结果。这个练习用于建立保存文件、执行文件、核对标准输出的完整流程。",
        complexity="时间 O(1)，额外空间 O(1)，因为目标文本长度固定。",
        pitfall="把中文逗号写成英文逗号的替代品会判错；`Hello,Python!` 缺少一个空格。不要把 Python 交互提示符 `>>>` 一起复制进文件。",
        source=PYTHON + "introduction.html#text"),
    dict(
        task="读取两个整数 a、b，依次输出 a+b、a-b、a*b、a/b，每个结果占一行。先把读入行当作已经提供的工具，重点体会变量保存值以及表达式计算；不必一开始背下输入写法。",
        io="输入两行，第一行整数 a，第二行非零整数 b。输出四行，分别是和、差、积、真除法的商。",
        bounds="-1000 ≤ a,b ≤ 1000，b ≠ 0。允许负数和零；除法输出可为小数。",
        learn="变量名是给值贴的名字。`a = 8` 的 `=` 表示把右边的值交给左边的名字，不是数学等式。`input()` 每次读一行文字；`int(...)` 把表示整数的文字转成整数；所以 `a = int(input())` 是从内向外先读、再转换、再命名。这两行已写在练习里，P004 再集中练转换。`+ - * /` 分别表示加、减、乘、真除法。`print(a + b)` 先算括号内再输出。",
        hand="a=8、b=2 时，8+2=10，8-2=6，8×2=16，8÷2=4。Python 的 `/` 会得到浮点数，显示为 4.0 也正确；换成 a=3、b=4 时商为 0.75。",
        hints=["每一行只做一种运算；两个输入值都要保留。", "乘法写 *，除法写 /；不要用 ×、÷。", "读入行之后依次写四次 print，括号分别是 a+b、a-b、a*b、a/b。"],
        code='''# 输入行把文字变成整数，再保存为 a、b。
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
''',
        scaffold='''# 下面两行已提供，不必现在背下来；P004 会专门练习转换。
a = int(input())
b = int(input())
# TODO：分别输出和、差、积、商，每个占一行。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="两次读取不可互相覆盖，因此分别命名为 a、b。四个输出表达式都使用这两个原始值；无需先把 a 改成和，否则后面的减法、乘法会丢失原值。",
        complexity="在题目限定整数范围内，时间 O(1)，额外空间 O(1)。",
        pitfall="`a = a + b` 会修改 a；`//` 是向下取整除法，并非本题要求。未转换时 '8'+'2' 得到文字 '82'。",
        source=PYTHON + "introduction.html#numbers"),
    dict(
        task="读取姓名和学习内容，拼成一行“姓名正在学习内容”。两侧输入中的空格应保留，空姓名或空学习内容也是合法输入。",
        io="输入恰好两行字符串，第一行姓名，第二行内容。输出一行：第一行文字 + 正在学习 + 第二行文字。",
        bounds="每行长度 0–100 个字符，可含中文、英文和空格；不含换行符本身。",
        learn="`str` 是字符串类型，`input()` 的结果本来就是 str，因此本题不调用 int。`name = input()` 读取一整行且去掉末尾换行，行内空格仍然保留。两个字符串之间的 `+` 表示拼接：`\"A\" + \"B\"` 得到 `\"AB\"`。`\"\"` 是长度为零的字符串，也能参与拼接。",
        hand="第一行“小明”、第二行“Python”，先把“小明”和“正在学习”连成“小明正在学习”，再接上“Python”，得到“小明正在学习Python”。若姓名是“李 华”，中间那个空格不能删掉。",
        hints=["把输出分成输入文字、固定文字、输入文字三段。", "三段都是字符串，所以可以使用两次 + 连接。", "先读取 name 与 subject，再输出 name + 固定字符串 + subject。不要对输入做 split。"],
        code='''# input 保留行内空格；这里没有数值转换。
name = input()
subject = input()
print(name + "正在学习" + subject)
''',
        scaffold='''name = input()
subject = input()
# TODO：把姓名、固定文字、内容连接成一个字符串并输出。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="输入本身就是文字。构造一个完整结果再 print，可以避免 print 多参数默认插入空格。既不切词，也不删除两端空白，因而空输入和含空格姓名都自然适用。",
        complexity="设两行字符数之和为 L，时间 O(L)，保存输入和拼接结果需 O(L) 空间。",
        pitfall="`print(name, '正在学习', subject)` 默认在参数之间额外加空格。`strip()` 会删掉本题允许保留的输入空白。",
        source=PYTHON + "introduction.html#text"),
    dict(
        task="商店有 n 件同价商品，每件价格 p 元。读取整数件数和小数单价，计算总价 n×p，只输出数值。",
        io="输入两行：非负整数 n、非负实数 p。输出一行总价，不附加元字或其他文字。",
        bounds="0 ≤ n ≤ 10000，0 ≤ p ≤ 10000。无需财务舍入；浮点比较容差为 1e-6。",
        learn="类型决定运算含义。`int` 表示整数，`float` 表示浮点数，`str` 表示文字。`int('3')` 为 3，`float('2.5')` 为 2.5；`int('2.5')` 会报 ValueError，因为它不是整数字面文字。`input()` 不会根据你输入的样子自动选择类型，也不要在括号里放‘请输入’，那会污染标准输出。",
        hand="件数文字 '3' 转成整数 3，单价文字 '2.5' 转成浮点数 2.5；3×2.5=7.5。若件数为 0，即使单价是 8.1，总价也为 0。",
        hints=["件数没有小数，单价可能有小数；选择不同转换。", "先用 int(input()) 读件数，用 float(input()) 读单价。", "将两个已经转换的变量相乘后 print；不需要把结果再转回整数。"],
        code='''# int 用于件数，float 保留单价的小数部分。
count = int(input())
price = float(input())
total = count * price
print(total)
''',
        scaffold='''# TODO：读取整数 count 和浮点数 price。
# 再计算总价并只输出数值；不要输出“请输入”。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="使用合适类型保存各输入。乘法由整数和浮点数共同参与，结果为浮点数。将它交给 print；无需为了输出 12 而强行转换，12.0 也是合法数值。",
        complexity="在输入数值范围内，时间 O(1)，额外空间 O(1)。",
        pitfall="字符串乘整数会重复文字，如 '2.5'*3 得到 '2.52.52.5'。二进制浮点不能精确表示所有十进制小数，检查器允许小误差。",
        source=PYTHON + "introduction.html#numbers"),
    dict(
        task="按成绩分类：90 分及以上输出 EXCELLENT；60–89 分输出 PASS；低于 60 分输出 FAIL。",
        io="输入一行整数 score。输出一行大写分类文本。",
        bounds="0 ≤ score ≤ 100；边界 60 和 90 包含在较高等级。",
        learn="比较表达式 `score >= 90` 的值是布尔值 True 或 False。`if 条件:` 在条件为真时执行缩进的语句；`elif` 表示前面的条件没满足时再判断；`else` 接住剩余情况。冒号不可漏。统一用四个空格缩进，同一层对齐。`=` 赋值，`==` 才是相等比较。",
        hand="score=60，先比较 60≥90 为假，再比较 60≥60 为真，输出 PASS。score=90 第一项立即成立，输出 EXCELLENT，不会再执行后面的分支。",
        hints=["先判断最高的等级，再判断及格，否则处理不及格。", "最高分支使用 >=90，第二个分支使用 >=60，剩余写 else。", "三个分支分别只 print 一次；用 if/elif/else 保证只有一条结果。"],
        code='''score = int(input())
# 从高到低判断，避免优秀先被及格条件截住。
if score >= 90:
    print("EXCELLENT")
elif score >= 60:
    print("PASS")
else:
    print("FAIL")
''',
        scaffold='''score = int(input())
# TODO：用 if / elif / else 分类，注意冒号和四个空格缩进。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="从最严格的条件开始形成互斥分支。elif 已隐含没有达到 90，因此不必再写小于 90。最后的 else 包含所有小于 60 的成绩。",
        complexity="最多两次比较，时间 O(1)，额外空间 O(1)。",
        pitfall="三个独立 if 可能让优秀成绩打印两行。`>60` 会漏掉恰好及格；先写 >=60 会挡住优秀分支。",
        source=PYTHON + "controlflow.html#if-statements"),
    dict(
        task="用 for 循环计算从 1 到 n（包含 n）的整数和。本题要求练习逐步累加，不用等差数列公式替代循环。",
        io="输入一行非负整数 n。输出一行整数总和。",
        bounds="0 ≤ n ≤ 100000，n=0 时没有待累加的数，总和定义为 0。",
        learn="`for i in range(1, n + 1):` 表示依次让 i 取 1、2、…、n。range 的右边界不包含在内，所以写 n+1。循环体缩进，循环结束后的 print 恢复到左边。累加器先设为 0；`total = total + i` 是先取旧 total 加上 i，再存回名字 total。",
        hand="n=4，初始 total=0；i=1 后为1，i=2 后为3，i=3 后为6，i=4 后为10。循环完只输出10。n=0 时 range(1,1) 没有数，total 仍是0。",
        hints=["需要一个起点为 0 的总和变量。", "range 的结束值不包含在内，目标循环到 n 应写 n+1。", "循环内更新 total = total + i；循环外输出 total，避免输出每一步。"],
        code='''n = int(input())
total = 0
# range 不包含右端点，因此右端写 n + 1。
for i in range(1, n + 1):
    total = total + i
print(total)
''',
        scaffold='''n = int(input())
total = 0
# TODO：用 for 遍历 1 到 n，更新 total。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="累加器维持‘已经遍历过的整数之和’。每加入下一个 i，这个含义继续成立；结束时恰好包含 1 到 n。0 是加法的中性起点，能自然处理空循环。",
        complexity="循环 n 次，时间 O(n)，题目范围内额外空间 O(1)。",
        pitfall="把 total=0 放在循环内会每轮清零。把 print 放进循环会输出 n 行而非一行。",
        source=PYTHON + "controlflow.html#for-statements"),
    dict(
        task="用 while 循环统计 1 到 n 中偶数的个数。每轮访问下一个正偶数，训练循环条件和更新。",
        io="输入一行非负整数 n。输出一行偶数数量。",
        bounds="0 ≤ n ≤ 100000；0 不在本题区间 1 到 n 内。",
        learn="`while 条件:` 在每轮开始前检查条件，条件为真就执行缩进的语句。与 for 不同，下一步如何前进由你安排。设 `current=2`，每访问一次便把 count 加1，再令 current 增加2。`<=` 表示小于或等于。只要更新能让 current 最终超过 n，循环就会结束。",
        hand="n=7：current 依次是2、4、6，count 依次变1、2、3；current 更新成8后条件8≤7为假，退出并输出3。n=1 时第一轮条件就为假，输出0。",
        hints=["从最小正偶数 2 开始，不必逐个检查奇数。", "循环条件是 current <= n，每轮计数加 1，current 加 2。", "初始 count=0、current=2；while 内同时更新两个变量，循环后打印 count。"],
        code='''n = int(input())
current = 2
count = 0
# 每轮消费一个正偶数；更新 current 保证循环终止。
while current <= n:
    count = count + 1
    current = current + 2
print(count)
''',
        scaffold='''n = int(input())
current = 2
count = 0
# TODO：用 while 逐个访问不超过 n 的正偶数。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="current 始终是尚未统计的最小正偶数。循环每次恰好计入它，再移动两个整数位置；没有漏掉或重复统计偶数。",
        complexity="执行 floor(n/2) 轮，时间 O(n)，额外空间 O(1)。",
        pitfall="忘记更新 current 会无限循环；条件写成 <n 会在 n 为偶数时漏掉 n。不要把 0 算进去。",
        source=PYTHON + "introduction.html#first-steps-towards-programming"),
    dict(
        task="筛选一行整数中严格大于 0 的数，保持原顺序和重复次数。输出它们，彼此用一个空格隔开；没有正数则输出 EMPTY。",
        io="输入一行空格分隔的整数。输出一行筛选结果或 EMPTY。",
        bounds="1–1000 个整数，每个数在 [-10000,10000]；0 不属于正数。",
        learn="列表是有顺序的容器，`[]` 是空列表，`append(x)` 把 x 放到末尾。`input().split()` 将一行按空白拆成字符串列表，for 能逐个访问这些字符串。`len(items)` 返回元素个数。索引从0开始，`items[0]` 是第一个元素。`' '.join(parts)` 把字符串列表按空格接成一行；所以筛选后可保存原来的文字 token。这里只用普通循环，不用列表推导式。",
        hand="输入1 -2 3 0 -4：先保留1，-2跳过，再保留3，0和-4跳过，结果列表为['1','3']，连接成1 3。输入2 2 -3 1时两个2都要保留。",
        hints=["用空列表保存通过条件的元素，遍历时保持顺序。", "比较时将 token 转成 int；保存时仍可保存字符串 token，方便 join。", "每遇到 int(token)>0 就 append(token)，最后按列表长度决定 join 或 EMPTY。"],
        code='''tokens = input().split()
selected = []
for token in tokens:
    if int(token) > 0:
        selected.append(token)
# join 要求列表中的元素都是字符串。
if len(selected) == 0:
    print("EMPTY")
else:
    print(" ".join(selected))
''',
        scaffold='''tokens = input().split()
selected = []
# TODO：普通 for 循环筛选正数，保留 token 的原顺序。
# TODO：空列表输出 EMPTY，否则用空格连接。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="每个 token 只判断一次，满足条件就追加到列表末尾，因此不改变原顺序，重复正数不会被消去。最后单独处理空结果，确保不是空白行。",
        complexity="设 n 为整数个数、L 为输入字符数，时间 O(L+n)，输入与结果列表及输出占 O(L+n) 空间。",
        pitfall="用 >=0 会错误保留0；用 set 会丢失重复值。join 不能直接连接整数列表，会报 TypeError。",
        source=PYTHON + "datastructures.html#more-on-lists"),
    dict(
        task="统计一行单词的出现次数，并输出指定查询单词的次数。区分大小写；单词按空白分开。必须先建立词频字典，再查询。",
        io="第一行一个或多个单词，第二行一个查询单词。输出一行非负整数。",
        bounds="第一行 1–1000 个单词；每词1–30个英文字母；查询词可能未出现。",
        learn="字典把键映射到值，例如 `{'cat': 2}` 表示 cat 出现2次。`{}` 是空字典。`word in counts` 判断键是否存在。`counts[word]` 读取或写入该键的值；不存在时直接读取会报 KeyError。因此第一次见单词先设0，再加1。字典与列表的区别是键可以是单词，不必是从0开始的整数位置。",
        hand="cat dog cat：初始{}；读cat变{'cat':1}；读dog新增dog:1；再次读cat将其增为2。查询cat得到2，若查询bird则没这个键，输出0。",
        hints=["每个不同单词作为一个键，次数作为对应的值。", "加1前先检查键是否存在，未出现时初始化为0。", "遍历单词建立 counts；查询时用 if 判断存在，否则打印0。"],
        code='''words = input().split()
query = input()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] = counts[word] + 1
# 不直接读取不存在的键，避免 KeyError。
if query in counts:
    print(counts[query])
else:
    print(0)
''',
        scaffold='''words = input().split()
query = input()
counts = {}
# TODO：先建词频字典，再安全查询；不存在输出0。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="counts[word] 表示已读前缀中该词的出现次数。新词从0开始，每次出现加1；整个输入读完就得到最终词频。查询阶段只输出指定键，不输出整个字典。",
        complexity="设输入共L个字符、n个词、k个不同词。哈希平均假设下建表时间 O(L+n)，存储输入和词频为 O(L+n+k)。极端哈希冲突会降低字典性能。",
        pitfall="不要自动转小写：A和a在本题不同。{} 创建的是字典而非集合；未初始化直接 counts[word]+1 会失败。",
        source=PYTHON + "datastructures.html#dictionaries"),
    dict(
        task="读取一行整数，求不同数值的个数。集合只用于消除重复，本题不要求输出集合元素或它们的顺序。",
        io="输入一行整数，空格分隔。输出一行不同整数数量。",
        bounds="1–1000 个整数，数值在 [-10000,10000]；1 与 01 表示相同整数。",
        learn="集合 set 保存不重复的元素，`set()` 创建空集合。注意 `{}` 已用于空字典。`seen.add(x)` 将元素放入集合；重复加入不增加元素数。先把输入文字转成整数，再去重，才能按数值比较。`len(seen)` 得到集合的元素数。集合不是按输入位置取值的列表，不用 seen[0]。",
        hand="输入1 2 1 3 2：依次加入后集合大小为1、2、2、3、3，所以输出3。输入-1 1 -1 0：不同值为-1、1、0，共3个。",
        hints=["你只关心某个数是否已经出现过，不关心出现几次。", "建立空集合，每次 add 转换后的整数。", "遍历 input().split()，seen.add(int(token))，最后输出 len(seen)。"],
        code='''tokens = input().split()
seen = set()
for token in tokens:
    # 先转整数，按数值而不是文字形式判重。
    seen.add(int(token))
print(len(seen))
''',
        scaffold='''tokens = input().split()
seen = set()
# TODO：将每个整数加入集合，最后输出集合大小。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="集合中每个数最多保存一份，因此最终集合元素与输入中的不同整数一一对应。整数转换发生在 add 之前，避免把01和1误当作两个值。",
        complexity="设L为输入长度、n为数量，哈希平均假设下时间 O(L+n)，输入及集合占 O(L+n) 空间；极端冲突下性能会下降。",
        pitfall="输出 set(...) 的外观不符合只要数量的要求。不要依赖集合遍历顺序，也不要把空集合写成{}。",
        source=PYTHON + "datastructures.html#sets"),
    dict(
        task="将学生成绩按分数从高到低排列；分数相同时按姓名的字典序从小到大排列。输出全部记录。使用两次稳定排序即可，无需 lambda 或尚未学过的自定义函数。",
        io="第一行人数 n，后面 n 行各为姓名和整数分数，空格分隔。每条输出为姓名、一个空格、分数。",
        bounds="1 ≤ n ≤ 1000；姓名为1–20个小写/大写英文字母且互异，分数0–100。字典序按 Python 字符串顺序，大小写不同；示例平票使用同一大小写。",
        learn="`sorted(items)` 返回升序的新列表；`list.sort()` 原地修改列表。Python 排序是稳定的：排序键相等时保留原先相对顺序。先把记录写成 `[name, score]`，默认排序依次比较姓名再比较分数。`row[0]`、`row[1]` 取两个位置。`key` 参数指定比较依据，`operator.itemgetter(1)` 表示按位置1取分数；`reverse=True` 表示降序。`from operator import itemgetter` 导入标准库提供的工具，学完函数后再考虑自己写 key。",
        hand="Bob80、Amy90、Zoe90；先按姓名得到Amy90、Bob80、Zoe90，再按分数降序；两个90保持Amy在Zoe前，最终Amy90、Zoe90、Bob80。",
        hints=["平票规则可以先确定，再进行稳定的主键排序。", "先对 [姓名,分数] 的列表默认排序，建立姓名升序。", "第二次按 itemgetter(1) 排分数并 reverse=True；稳定性会保留同分姓名顺序。"],
        code='''from operator import itemgetter

n = int(input())
records = []
for i in range(n):
    parts = input().split()
    records.append([parts[0], int(parts[1])])
# 先确定平票顺序，再用稳定排序处理主键分数。
records.sort()
records.sort(key=itemgetter(1), reverse=True)
for row in records:
    print(row[0], row[1])
''',
        scaffold='''from operator import itemgetter

n = int(input())
records = []
for i in range(n):
    parts = input().split()
    records.append([parts[0], int(parts[1])])
# TODO：先排姓名，再稳定地按分数降序；逐行输出。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="先以姓名为第一比较位置进行默认升序排序。第二次只看整数分数，按降序排序；稳定排序使相同分数的记录保持第一次排好的姓名顺序。输入分数字段必须转整数，否则100会按文字排在90之前。",
        complexity="设n为人数、s为最大姓名长度，两次排序最坏时间 O(n log n·s)，记录和排序辅助空间 O(n·s+n)。输入分数固定范围但这里使用一般排序。",
        pitfall="对整条记录 reverse=True 会让同分姓名也降序。list.sort() 返回 None，不能写 records=records.sort()。",
        source="https://docs.python.org/3.11/howto/sorting.html#sort-stability-and-complex-sorts"),
    dict(
        task="定义函数 square(x)，用 return 返回 x 的平方。读取两行整数，分别调用函数并逐行输出结果；函数内部不负责输出。",
        io="输入两行整数 a、b。输出两行，分别为 a² 和 b²。",
        bounds="-10000 ≤ a,b ≤ 10000。必须定义 square 并在两次计算中调用。",
        learn="函数是给一段可重复执行的代码取名字。`def square(x):` 定义名称 square，x 是形参，调用 `square(3)` 时 x 收到3。缩进的函数体在调用时才运行。`return` 把值交还调用处并结束本次调用；`print` 只往屏幕写文字，不能代替返回值。函数定义后空一行，再写顶层输入代码。",
        hand="square(3) 内部计算3×3=9，并把9返回给 print；square(4) 返回16，最终两行9和16。square(-2) 计算(-2)×(-2)=4，平方不会保留负号。",
        hints=["平方就是一个数与自身相乘；把这个规则写进函数。", "函数体写 return x*x，在函数外读取和输出。", "先定义 square，后面两个 print 分别调用 square(a) 和 square(b)。"],
        code='''def square(x):
    # 返回计算值，交由调用者决定怎样输出。
    return x * x


a = int(input())
b = int(input())
print(square(a))
print(square(b))
''',
        scaffold='''def square(x):
    # TODO：返回平方；不要在函数内部 print。
    raise NotImplementedError("请按题目提示完成这里")


a = int(input())
b = int(input())
print(square(a))
print(square(b))
''',
        steps="函数定义保存规则，并不立即计算。两次调用各有独立的参数值，返回后由外层 print 输出。把逻辑与输出分开，使同一平方规则也能用于后续数学表达式。",
        complexity="限定数值范围内，两次乘法时间 O(1)，每次调用固定大小，额外空间 O(1)。",
        pitfall="Python 的乘方运算是 **，^ 是按位异或。忘写 return 时函数默认返回 None；内部 print 之后外部再 print 会多出 None。",
        source=PYTHON + "controlflow.html#defining-functions"),
    dict(
        task="把 r 行整数存成二维列表，再计算并逐行输出每一行的和。所有行长度相同，目标是理解一张表由行列表组成。",
        io="第一行整数 r；随后 r 行，每行 c 个整数。输出 r 行，各为对应行的整数和。c 由数据行长度确定，不另输入。",
        bounds="1 ≤ r,c ≤ 100；元素在 [-10000,10000]；所有行长度相同。",
        learn="二维列表就是列表里面放列表。`matrix[0]` 取得第一行；`matrix[0][1]` 再从该行取第二个元素。不要写成 matrix[0,1]，那是之后 NumPy 的写法。构建每行时重新写 `row=[]`，转换每个 token 再 append；把完成的 row 放入 matrix。嵌套循环中，内层负责一行，外层负责各行。",
        hand="表为[[1,2,3],[4,5,6]]。外层先拿到[1,2,3]，内层从0累加成1、3、6，输出6；新的一行重新从0累加成4、9、15，输出15。",
        hints=["先完成一个 row，再把它 append 到 matrix。", "输出阶段的 total 应在每次开始新行时重置。", "外层 for row in matrix，内层 for value in row 累加，内层结束后打印一行总和。"],
        code='''r = int(input())
matrix = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(int(token))
    matrix.append(row)
for row in matrix:
    total = 0  # 每一行使用独立的累加器。
    for value in row:
        total = total + value
    print(total)
''',
        scaffold='''r = int(input())
matrix = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(int(token))
    matrix.append(row)
# TODO：逐行计算行和，记得每一行重新设置 total=0。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="读入阶段创建独立的行对象，形成表格。输出阶段每行从0开始累加，避免把上一行的总和带入下一行。每个元素恰好参与一次加法。",
        complexity="r行c列，数值位数限定，时间 O(rc)，保存矩阵空间 O(rc)，计算阶段额外空间 O(1)。",
        pitfall="若只在外层循环之前设 total=0，会输出跨行累计和。不要用 `[[]]*r` 后反复修改子列表，因为它们会共享同一对象。",
        source=PYTHON + "introduction.html#lists"),
    dict(
        task="进行一次考试式输入输出验收：输入 T 组数据，每组是一行整数；对每组独立求和并输出。不要输出组号、提示语或中间步骤。",
        io="第一行正整数 T；接下来恰好 T 行，每行是一组非空整数序列。输出恰好 T 行，对应各组总和。",
        bounds="1 ≤ T ≤ 100；每组1–1000个整数，每数在 [-10000,10000]。无需处理输入不合法或缺行。",
        learn="本题不增加新语法，练习把‘读取组数→重复读一组→重置状态→计算→输出’连起来。`range(T)` 依次给出0到T-1，共T次；循环变量只用于控制次数，不要输出它。输入文件的换行是分组边界，因此每轮恰好调用一次 input 读这一组，而不是把整个文件混成一行。",
        hand="T=2，第一组1 2 3求和为6；第二组-1 5必须重新从0开始，得到4。因此输出6、4两行，而不是6、10，也不把最前面的2当作数据参与求和。",
        hints=["第一行只是说明接下来有几组，不属于第一组数。", "在 for 的每一轮内先 total=0，再读当前行并累加。", "用 for group in range(T)，循环体读取一行、转换、求和、打印；不要额外输出空行。"],
        code='''t = int(input())
for group in range(t):
    total = 0  # 各组互不影响。
    for token in input().split():
        total = total + int(token)
    print(total)
''',
        scaffold='''t = int(input())
# TODO：精确处理 t 组；每一组独立累加，只输出结果。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="外层执行T次，每次只消费一行。内层把这行各token转为整数并累加。状态total在外层循环内部初始化，天然隔离不同组。",
        complexity="设各组元素总数为N、最长输入行为L字符，时间 O(N+输入总字符数)，当前行拆分占 O(L)，不保存全部组。",
        pitfall="把 total 放到外层循环前会混合组结果。不要输出‘第1组：6’，检查器要求纯结果；空白分隔的负数由 int 正常处理。",
        source=PYTHON + "controlflow.html#the-range-function"),
]

LESSONS.extend([
    dict(
        task="对同一组数，先用普通 Python 循环计算总和及均值，再用 NumPy 数组计算同样两个量，输出两行结果用于对照。",
        io="输入一行实数。输出两行，每行两个数：总和、均值。第一行来自普通循环，第二行来自 NumPy。",
        bounds="1–1000 个有限实数，绝对值不超过10000。均值分母为元素个数，不是元素总和。",
        learn="`import numpy as np` 导入 NumPy 并用简称 np。`np.array(values, dtype=float)` 把列表转成所有元素同为浮点数的数组。数组提供 `.sum()` 求和、`.mean()` 求平均；小括号表示调用计算。`len(values)` 是元素数。均值是总和除以个数；它能概括中心位置，但不表示数据一定接近中心。",
        hand="输入1 2 3 4，总和1+2+3+4=10，共4个数，所以均值10/4=2.5。普通循环与NumPy应各输出一行10 2.5。输入只有5时，和为5、均值也为5。",
        hints=["先保存数字列表，普通循环累加时仍使用0作为起点。", "第一行的第二个数是 total/len(values)，不是除以最后一个值。", "将列表转换为 NumPy 数组；第二行输出 array.sum() 和 array.mean()。"],
        code='''import numpy as np

values = []
for token in input().split():
    values.append(float(token))
total = 0.0
for value in values:
    total = total + value
print(total, total / len(values))
# 数组方法与上面的普通循环计算相同统计量。
array = np.array(values, dtype=float)
print(array.sum(), array.mean())
''',
        scaffold='''import numpy as np

values = []
for token in input().split():
    values.append(float(token))
# TODO：先循环输出总和与均值，再转数组输出 NumPy 结果。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="输入只读取一次以确保两个方法面对同一组数据。纯Python逐项累加后除以长度；NumPy将列表转换为浮点数组，分别调用两个聚合方法。保持两行同样的‘和、均值’顺序。",
        complexity="n个数，两个求和及数组转换均为 O(n) 时间；列表与数组占 O(n) 空间。这里不据此承诺小数组一定更快。",
        pitfall="空数组的均值无定义，本题保证非空；不要把 mean 这个方法对象直接打印，必须写 mean()。",
        source=NUMPY + "#basic-array-operations"),
    dict(
        task="计算输入数据的总体方差：先求均值，再把每个数与均值之差平方，最后对这些平方求平均。明确使用分母 n（ddof=0）。",
        io="输入一行实数。输出一行总体方差。",
        bounds="1–1000个有限实数，绝对值≤10000。把输入当作整个总体，不计算样本方差。",
        learn="方差衡量数据偏离均值的程度。公式为 var=(Σ(xᵢ−μ)²)/n；Σ表示把所有对应项相加，μ是均值，n是个数。`array - mean` 对每个元素减同一个数；`** 2` 对每个差平方；新数组的 mean() 取平均。NumPy 的 `np.var(array, ddof=0)` 与这个定义一致，ddof=1 会改变分母，本题不用。",
        hand="数据1、2、3均值是2，偏差为-1、0、1，平方是1、0、1，相加为2，再除以3得到2/3。不能除以2，那是另一种定义。单个7的偏差为0，总体方差为0。",
        hints=["先求中心，再求偏差；直接对原始数据平方取平均不是方差。", "差值数组写 array-array.mean()，平方后再求 mean。", "三步分别保存 mean、difference、squared，然后输出 squared.mean()，分母自然是 n。"],
        code='''import numpy as np

values = []
for token in input().split():
    values.append(float(token))
array = np.array(values, dtype=float)
mean = array.mean()
difference = array - mean
# 平方偏差的均值就是总体方差，即 ddof=0。
squared = difference ** 2
print(squared.mean())
''',
        scaffold='''import numpy as np

values = []
for token in input().split():
    values.append(float(token))
array = np.array(values, dtype=float)
# TODO：依次计算均值、偏差、平方偏差，最后取平均。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="使用两遍中心化定义：先算均值，再算平方偏差均值。避免采用 E[x²]−E[x]² 形式时两个大数相减可能放大的消减误差；这仍使用浮点数，不保证任意数值精确。",
        complexity="n个数，时间 O(n)，列表、数组及临时差值数组占 O(n) 空间。",
        pitfall="平方之前就对偏差求平均，理论上总是0；忘平方会丢失离散程度。单元素总体方差应为0，不能用 n-1 作分母。",
        source="https://numpy.org/doc/stable/reference/generated/numpy.var.html"),
    dict(
        task="计算两个同维向量之间的欧氏距离：对应坐标相减、平方求和，再开平方。",
        io="输入两行，各是相同个数的实数坐标。输出一行非负距离。",
        bounds="向量维数1–1000，坐标绝对值≤10000；两行长度相等。",
        learn="向量可以先理解为一排按位置对应的数。二维点(0,0)到(3,4)的距离来自勾股定理；n维时同样计算 sqrt(Σ(aᵢ-bᵢ)²)。`np.sqrt(value)` 求非负平方根。数组减法要求坐标按同一顺序对应，不能先各自排序；求和后的结果是单个数。",
        hand="a=(0,0)、b=(3,4)，差为(-3,-4)，平方为(9,16)，和为25，平方根为5。a=(0,0,0)、b=(1,2,2)时平方和为1+4+4=9，距离3。",
        hints=["先逐坐标做差，距离与各自坐标总和之差不同。", "用差数组 **2 后 sum，再对结果开平方。", "difference=a-b；输出 np.sqrt((difference**2).sum())，保持括号包住平方与求和。"],
        code='''import numpy as np

left = []
for token in input().split():
    left.append(float(token))
right = []
for token in input().split():
    right.append(float(token))
a = np.array(left, dtype=float)
b = np.array(right, dtype=float)
difference = a - b
# 先合并平方，再开平方；不是各坐标距离之和。
print(np.sqrt((difference ** 2).sum()))
''',
        scaffold='''import numpy as np

left = []
for token in input().split():
    left.append(float(token))
right = []
for token in input().split():
    right.append(float(token))
a = np.array(left, dtype=float)
b = np.array(right, dtype=float)
# TODO：做差、平方、求和、开平方。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="对应坐标的差构成差向量。平方去掉符号，求和合并各坐标贡献，最后开平方把量纲恢复为坐标的单位。交换两个输入只使差变号，因此距离应不变。",
        complexity="n维向量，时间 O(n)，输入及差向量等数组占 O(n) 空间。",
        pitfall="Σ|aᵢ-bᵢ| 是曼哈顿距离，本题要求平方和再开方；`sqrt(sum)` 与 `sum(sqrt(...))` 不可交换。",
        source="https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html"),
    dict(
        task="计算两个同维向量的点积：每个位置相乘，再将所有乘积相加。理解线性模型中‘特征乘权重再汇总’的基本操作。",
        io="输入两行等长实数序列。输出一行点积，允许为负数。",
        bounds="维数1–1000，元素绝对值≤10000，两行长度相同。",
        learn="点积符号 a·b 代表 Σaᵢbᵢ。NumPy 对同形状数组的 `a * b` 是逐元素乘法，结果仍是一排数；再 `.sum()` 才得到单个点积。点积不等于两个向量各自先求和再相乘，也不等于距离。它可能为正、负或零。",
        hand="a=(1,2,3)，b=(4,5,6)，逐项乘积4、10、18，相加32。a=(-2,3)，b=(4,-1)时结果为-8-3=-11。两个非零向量(1,0)、(0,1)点积为0。",
        hints=["每个位置只和另一向量相同位置相乘。", "先得到 a*b 的乘积数组，不要对它开平方。", "输出 (a*b).sum()；可以用手算32验证没有误写为 (a.sum()*b.sum())。"],
        code='''import numpy as np

left = []
for token in input().split():
    left.append(float(token))
right = []
for token in input().split():
    right.append(float(token))
a = np.array(left, dtype=float)
b = np.array(right, dtype=float)
products = a * b  # 逐元素相乘，之后才求和。
print(products.sum())
''',
        scaffold='''import numpy as np

left = []
for token in input().split():
    left.append(float(token))
right = []
for token in input().split():
    right.append(float(token))
a = np.array(left, dtype=float)
b = np.array(right, dtype=float)
# TODO：对应位置相乘，再将乘积求和。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="乘积数组中的第i项保存aᵢbᵢ，sum把它们合并成定义中的求和。本题显式展开这两步，之后可以将 np.dot(a,b) 用作对照。",
        complexity="n维向量，时间 O(n)，输入及乘积数组占 O(n) 空间。",
        pitfall="逐元素乘法本身并未完成点积；只打印 products 会输出数组。不要把点积为0误认作某个向量必为零。",
        source="https://numpy.org/doc/stable/reference/generated/numpy.dot.html"),
    dict(
        task="手写三层循环计算矩阵乘法 A×B。A 为 r×k，B 为 k×c，输出 r×c 的乘积。允许 NumPy 存储数据，但不能直接用 @、dot 或 matmul 替代求和循环。",
        io="第一行三个整数 r k c；后 r 行是 A，每行 k 个数；再后 k 行是 B，每行 c 个数。输出 r 行，每行 c 个数，空格分隔。",
        bounds="1 ≤ r,k,c ≤ 30，元素为绝对值≤100的实数。维度总是匹配。",
        learn="矩阵是按行列排列的数表。二维 NumPy 数组用 `a[i,j]` 取第i行第j列，位置从0开始。乘积 C 的形状是(r,c)，`np.zeros((r,c), dtype=float)` 创建全0数组。Cᵢⱼ=ΣₜAᵢₜBₜⱼ：选A的一行、B的一列，沿共同长度k做点积。`print(*row)` 中星号将一行数拆成多个参数，print默认用空格分隔；这只用于输出。",
        hand="A第一行(1,2,3)，B第一列(7,9,11)：C₀₀=1×7+2×9+3×11=58。B第二列(8,10,12)给64。第二行得到4×7+5×9+6×11=139，以及4×8+5×10+6×12=154。",
        hints=["先写出输出形状(r,c)，共同维度k会被求和消掉。", "外两层选择输出位置i,j，第三层t从0到k-1累加 a[i,t]*b[t,j]。", "每个i,j先 total=0.0；内部t循环完才把 total 存入 result[i,j]，最后按行 print(*row)。"],
        code='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
k = int(dimensions[1])
c = int(dimensions[2])
rows_a = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows_a.append(row)
rows_b = []
for i in range(k):
    row = []
    for token in input().split():
        row.append(float(token))
    rows_b.append(row)
a = np.array(rows_a, dtype=float)
b = np.array(rows_b, dtype=float)
result = np.zeros((r, c), dtype=float)
for i in range(r):
    for j in range(c):
        total = 0.0
        for t in range(k):
            total = total + a[i, t] * b[t, j]
        result[i, j] = total
for row in result:
    print(*row)
''',
        scaffold='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
k = int(dimensions[1])
c = int(dimensions[2])
rows_a = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows_a.append(row)
rows_b = []
for i in range(k):
    row = []
    for token in input().split():
        row.append(float(token))
    rows_b.append(row)
a = np.array(rows_a, dtype=float)
b = np.array(rows_b, dtype=float)
result = np.zeros((r, c), dtype=float)
# TODO：三层循环，按 A 的行与 B 的列做点积；然后逐行输出。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="输入维度决定两个读取循环的行数。输出共有rc个位置，每个位置独立从0开始，沿t轴累加k项。i固定选择A的行、j固定选择B的列，只有t在乘积求和中变化。",
        complexity="实际使用三层循环，时间 O(rkc)，输入与输出存储 O(rk+kc+rc)，除这些数组外的累加空间 O(1)。",
        pitfall="A*B是逐元素乘法，并不等于矩阵乘法，矩形样例甚至形状不匹配。把B写为b[j,t]会把行列颠倒；total必须每个输出位置重置。",
        source="https://numpy.org/doc/stable/reference/generated/numpy.matmul.html"),
    dict(
        task="将一行数据按行优先顺序重排成 r×c 数组；先输出形状，再逐行输出新数组。重排只改变摆放方式，不改变数值或先后顺序。",
        io="第一行整数 r c；第二行恰好 r×c 个实数。第一行输出 r c，其后输出 r 行数组内容。",
        bounds="1 ≤ r,c ≤ 100；输入元素绝对值≤10000；保证元素数量匹配。",
        learn="`array.shape` 是形状属性，不加括号；二维数组得到(r,c)，一维数组得到(n,)，尾逗号表明只有一个维度。`array.reshape((r,c))` 按默认C顺序先填满一行再填下一行。形状中的尺寸相乘必须等于元素总数。reshape与转置含义不同，不会自动把数值进行排序。",
        hand="1 2 3 4 5 6改为(2,3)：先填第一行1 2 3，再填第二行4 5 6。总数2×3=6不变；改成(3,2)会得到1 2、3 4、5 6，绝不是同一个输出。",
        hints=["先核对 r*c 是否等于一行元素数。", "把列表变成一维浮点数组，然后调用 reshape((r,c))。", "用 print(*matrix.shape) 输出两个维度，再 for row in matrix 逐行 print(*row)。"],
        code='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
values = []
for token in input().split():
    values.append(float(token))
array = np.array(values, dtype=float)
matrix = array.reshape((r, c))  # 默认先填完整的一行。
print(*matrix.shape)
for row in matrix:
    print(*row)
''',
        scaffold='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
values = []
for token in input().split():
    values.append(float(token))
array = np.array(values, dtype=float)
# TODO：重排、输出形状，再输出各行。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="输入values先建立一维数组，再指定二维目标形状；默认行优先填入，与手算逐行放置一致。读取shape属性得到实际维度，而非打印带括号逗号的元组外观。",
        complexity="本程序读入转换和输出共rc个元素，时间 O(rc)，列表及数组占 O(rc) 空间。此处连续一维数组reshape通常可以创建视图，但不把reshape推广为总是零复制。",
        pitfall="shape不是方法，shape()会失败。打印matrix本体会带方括号；输出规范要求每行数值。元素总数不匹配会报ValueError。",
        source=NUMPY + "#can-you-reshape-an-array"),
    dict(
        task="对同一个 r×c 矩阵做两种独立加法：第一块将长度c的向量按列加到每一行；第二块将长度r的向量按行加到每一列。两块都从原矩阵计算，展示广播方向差异。",
        io="第一行 r c；接着 r 行矩阵；再一行c个列偏移量；最后一行r个行偏移量。先输出第一块r行，再输出第二块r行，中间没有空行。",
        bounds="1 ≤ r,c ≤ 30，所有输入绝对值≤10000。输出每行c个数，总计2r行。",
        learn="`a[i,:]` 中冒号表示取该行全部列；`a[:,j]` 表示取该列全部行。广播从最右边维度对齐，两个尺寸必须相等或其中一个为1。矩阵(r,c)加向量(c,)时，向量沿各行重复。行偏移(r,)不能直接当成(r,1)：先reshape((r,1))，右端的1才能扩展到c列。广播是运算规则，不要求手工复制数组。",
        hand="A=[[1,2],[3,4]]。列偏移[10,20]：第一列各加10、第二列各加20，得到[[11,22],[13,24]]。行偏移[100,200]变为[[100],[200]]：第一行各加100，第二行各加200，得到[[101,102],[203,204]]。第二块不接着第一块相加。",
        hints=["先画出(r,c)、(c,)与(r,1)，确认最后一维怎样对齐。", "列偏移可直接 a+column_offsets；行偏移要先 reshape((r,1))。", "分别保存 by_column=a+列向量、by_row=a+行向量.reshape((r,1))；依次输出，别修改a。"],
        code='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
rows = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows.append(row)
columns = []
for token in input().split():
    columns.append(float(token))
row_offsets = []
for token in input().split():
    row_offsets.append(float(token))
a = np.array(rows, dtype=float)
columns = np.array(columns, dtype=float)
row_offsets = np.array(row_offsets, dtype=float)
by_column = a + columns
# 显式列形状使每个行偏移沿该行的所有列重复。
by_row = a + row_offsets.reshape((r, 1))
for row in by_column:
    print(*row)
for row in by_row:
    print(*row)
''',
        scaffold='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
rows = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows.append(row)
columns = []
for token in input().split():
    columns.append(float(token))
row_offsets = []
for token in input().split():
    row_offsets.append(float(token))
a = np.array(rows, dtype=float)
columns = np.array(columns, dtype=float)
row_offsets = np.array(row_offsets, dtype=float)
# TODO：独立计算两块；行偏移先改为(r,1)，再按顺序输出。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="第一块将(c,)从右与(r,c)对齐，视为(1,c)，扩展行数。第二块显式转成(r,1)，只扩展列数。两个表达式都以a为左操作数，从原数据独立建立新数组。",
        complexity="读取、两次加法和输出均为 O(rc+r+c) 时间，数组与两个结果占 O(rc+r+c) 空间。广播避免手写重复偏移数组，但结果仍占空间。",
        pitfall="方阵上错误的(r,)行偏移也能相加，却会按列加而非按行加；必须用矩形样例检验。`a += columns` 会改变原矩阵，导致第二块错误叠加。",
        source="https://numpy.org/doc/stable/user/basics.broadcasting.html"),
    dict(
        task="对矩阵分别求行和与列和，验收你对 axis 的理解。第一行输出每一行的和，第二行输出每一列的和。",
        io="第一行 r c；随后 r 行，每行c个实数。输出恰好两行：r个行和、c个列和。",
        bounds="1 ≤ r,c ≤ 100，元素绝对值≤10000。单行、单列、全零均合法。",
        learn="二维形状(r,c)的axis=0对应行位置，axis=1对应列位置。沿某个axis求和，消掉的就是那个维度：sum(axis=0)把多行合并，留下c个列和；sum(axis=1)把每行的列合并，留下r个行和。不要只背‘axis0竖着’，请从输出剩下哪个维度推导。",
        hand="A=[[1,2,3],[4,5,6]]。行和：1+2+3=6，4+5+6=15，长度2。列和：1+4=5、2+5=7、3+6=9，长度3。先输出6 15，再输出5 7 9。",
        hints=["先根据题目推断输出长度：第一行r个，第二行c个。", "行和要合并列维度，所以axis=1；列和合并行维度，所以axis=0。", "分别调用 a.sum(axis=1)、a.sum(axis=0)，用print(*结果)避免数组方括号。"],
        code='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
rows = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows.append(row)
a = np.array(rows, dtype=float)
row_sums = a.sum(axis=1)  # 消掉列维度，留下各行。
column_sums = a.sum(axis=0)  # 消掉行维度，留下各列。
print(*row_sums)
print(*column_sums)
''',
        scaffold='''import numpy as np

dimensions = input().split()
r = int(dimensions[0])
c = int(dimensions[1])
rows = []
for i in range(r):
    row = []
    for token in input().split():
        row.append(float(token))
    rows.append(row)
a = np.array(rows, dtype=float)
# TODO：第一行输出行和，第二行输出列和，注意轴和结果长度。
raise NotImplementedError("请按题目提示完成这里")
''',
        steps="先确认原矩阵有r行c列。沿axis=1加总每行中的c个数，结果长度r；沿axis=0合并r行的同列数，结果长度c。整体和应同时等于行和总和与列和总和，可作自查。",
        complexity="两次遍历矩阵，时间 O(rc)，输入矩阵及读入列表占 O(rc)，两条聚合结果另占 O(r+c)。",
        pitfall="sum()不传axis会得到一个整体总和，丢掉行列结构；axis=0不代表输出‘行和’。矩形矩阵可暴露互换错误。",
        source=NUMPY + "#basic-array-operations"),
])


def build_chapters():
    python_chapter = r'''# 第 01 章：从第一行 Python 到考试式输入输出

先修：不要求编程经验。目标是读懂每行代码如何把输入变成输出，能够独立完成 P001–P014。不要按天赶进度；一次只引入一种主要能力，能解释上一题再前进。以下代码是概念示范，不是必须拷进每道题的公共模板。

## 先分清文件、终端和解释器

代码文件是保存指令的文本，例如 `exercise.py`；终端是输入命令并查看文字输出的窗口；Python解释器是执行这些指令的程序。终端里运行Python命令，不代表已经在写Python代码。在编辑器打开 `.py` 文件写代码并保存，回到仓库根目录的PowerShell运行文件。

本课程已准备独立环境，不必激活。先运行：

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe check.py --list
.\.venv\Scripts\python.exe chapters/01_python/problems/P001/exercise.py
```

`--version` 应显示Python 3.11系列；本次验收使用3.11.15。相对路径从仓库根目录开始算。若报找不到文件，先确认终端当前目录，而不是随意重装Python。代码中的 `>>>` 是官方教程的交互提示符，复制示例时不要复制它。编辑器里的“保存”很重要：解释器执行的是磁盘上的文件。

每题有 `README.md`（题目与提示）、`exercise.py`（你修改的练习）和 `cases.json`（自动检查数据，不要求你学习JSON）；独立答案另存于根目录 `solutions/`。练习中的 `raise NotImplementedError(...)` 表示这里故意尚未完成。将这一行替换成自己的代码，或完成该部分后删除它；不要只在它前面写答案而保留这行。开始遇到它报错是正常现象，阅读最后一行异常能看到原因。

## P001：字符串、括号与输出

```python
print("你好")
```

程序从上往下执行。print 是内置的输出操作，英文括号里面写输出内容；英文引号把文字圈成字符串，字符串是保存文字的值。屏幕显示“你好”，不显示引号，并自动换行。`#` 后是注释，不会执行。这一步只需练习保存、运行和核对输出，不需要理解输入。P001 的输入都忽略，五个测试不是五种算法情况，而是检查固定输出保持不变。

## P002–P004：变量、类型和输入

变量是值的名字。`count = 3` 表示先得到右边的3，再让count指向它。以后使用count，就是使用这个值；重新赋值可改变名字对应的值。`=` 不是数学证明中的相等符号。变量名不能含空格，大小写有区别。

数值和文字是不同类型：整数 `3` 是int；小数 `2.5` 是float；带引号的 `"3"` 是str。整数的 `+ - * /` 分别算加减乘除；`3/4` 得0.75，`8/2` 得4.0。字符串的 `+` 是拼接，`"3"+"4"` 得到 `"34"`。同一符号必须结合值的类型理解。

为了让P002能用不同数字练习，下面两行先作为已提供的输入工具，不必一开始背下来：

```python
a = int(input())
b = int(input())
```

执行顺序从内向外：input()读一整行，结果是字符串；int把表示整数的文字转成整数；赋值保存它。两行表示读取两行，不是读一行中的两个数。P003直接用input()读取姓名和内容，因为文字无需转整数。P004再自行填写整数件数、浮点单价的读入：单价要用float(input())，否则 `int("2.5")` 会失败。

手算 `3 × 2.5 = 7.5` 后再运行程序，确认类型与运算是否对应。不在input括号内写提示语：`input("请输入：")` 会把提示混入标准输出，自动判题不接受。float是近似数值，0.1等十进制数通常不能被二进制浮点精确表示；本课程数值检查使用1e-6的绝对/相对容差，并仍检查行数和每行元素数。

## P005：条件和缩进

比较 `score >= 60` 得到True（真）或False（假）。比较相等用 `==`，不要与赋值 `=` 混淆。`if` 在条件为真时执行其下面缩进的代码；`elif` 表示前面不成立再检查；`else` 表示都不成立。条件行末尾用冒号，代码块缩进四个空格。

```python
score = 60
if score >= 60:
    print("及格")
else:
    print("未及格")
```

这段只打印一行。等级多于两个时按最高门槛向下判断，例如90分先检查优秀，再检查及格。先手算59、60、89、90四个边界，尤其留意 `>=` 中的等号。

## P006–P007：反复执行和状态

for适合知道要访问哪些值的情况。`range(1,5)` 给出1、2、3、4，右端5不包含；`range(n)` 是0到n-1，共n次。循环体缩进，循环结束后恢复原缩进。

```python
total = 0
for i in range(1, 5):
    total = total + i
print(total)
```

右边先取旧total和当前i相加，再存回total；这不是数学里左右抵消的等式。手算状态表是：初始0，第一轮1，第二轮3，第三轮6，第四轮10。把初始化放进循环会每轮清零；把print放进循环会输出中间过程。

while适合“条件仍成立就继续”的情况。P007令current从2起，每次增加2；条件是current不超过n。一次循环必须向终止方向推进，忘更新current就会无限循环。先想“循环之前状态是什么、每轮改变什么、什么时候退出”，再写代码。n=0要能零轮执行并输出0。

## P008–P010：一排数、查次数与去重复

列表保留顺序和重复值，例如 `[3,1,3]` 有三个元素。`[]` 是空列表，`items.append(x)` 在末尾添加，`len(items)` 取个数。位置叫索引，从0开始：`items[0]` 是3，`items[1]` 是1；索引等于长度就越界。不要把“第一个”写成位置1。

一行输入多个数时，`input().split()` 先按空白拆成字符串列表，普通for逐项取出token，再调用int或float转换。P008保留正数时，把通过条件的token追加到列表；`" ".join(parts)` 用空格连接字符串元素。join要求里面是字符串，不能直接放整数。空结果按题面输出EMPTY。

字典将键对应到值：`counts["cat"] = 2` 表示cat对应2次；`{}` 是空字典。`word in counts` 判断键存在，`word not in counts` 判断不存在。P009初次遇词先设0，再加1；查询未出现的词输出0，避免直接索引不存在的键。大小写是否相同由题面决定，本题区分A与a。

集合只保留不同元素，`set()` 创建空集合，`seen.add(x)` 加入元素。P010将整数加入集合后输出len，不输出顺序。不要把空集合写成{}，也不要靠集合保存原输入顺序。列表适合保留明细，字典适合查词频，集合适合问“有哪些不同值”。

## P011：稳定排序与平票

记录可保存为 `[姓名, 分数]`，多条记录再放进一个列表。`row[0]`是姓名，`row[1]`是分数。`records.sort()` 原地升序排序，默认按记录的第一个元素比较，必要时再看下一个元素；它返回None，不要将返回值赋给records。

`from operator import itemgetter` 从Python标准库导入现成工具。`itemgetter(1)`提供“按位置1取值”的排序依据。`records.sort(key=itemgetter(1), reverse=True)` 中 `key=...`、`reverse=True` 是传给排序操作的具名设置，意思分别为按分数比较、降序排列。P011已提供导入和读入，不要求现在自己定义函数或lambda。

排序稳定性表示键相同的记录保留原先相对顺序。因此先按姓名升序，再按分数降序，就能让同分时仍按姓名升序。手算Amy90、Zoe90、Bob80：第二次排序只移动分数组，两个90的先后不改变。`reverse=True` 用在整条记录上会连平票规则一起反转。

## P012：把规则写成函数

```python
def square(x):
    return x * x

print(square(3))
```

`def` 定义函数，square是名字，x是接收调用值的参数。定义时不计算，调用square(3)时才让x收到3，执行乘法，return把9交回调用位置；外面的print再输出9。return与print不同，函数只打印而不返回，调用结果会是None。掌握这一点后才需要考虑lambda等简写，本章不使用它们。

## P013–P014：二维结构与多组验收

二维列表是行列表的列表，如 `[[1,2],[3,4]]`。`matrix[0]` 是第一行，`matrix[0][1]` 是第一行第二个数2；嵌套for先遍历行，再遍历行中元素。P013每次建行都创建新的空列表，每次求行和都重新设置total=0。

P014没有新语法，要求你独立连接整个流程。输入第一行T只控制组数；每轮读一行、重置total、转换、累加、输出。T=2，数据行1 2 3与-1 5，正确输出6与4；若得到6与10，说明跨组状态没重置。

## 逐题入口

{links01}

## 报错时按证据排查

`SyntaxError`：先看报错行的英文引号、括号和冒号；错误有时来自上一行未闭合的括号。`IndentationError`：检查同级是否对齐，不混用Tab与空格。`NameError`：变量拼错或在赋值前使用。`ValueError`：例如把2.5传给int文字转换。`TypeError`：例如文字加整数、join整数。`IndexError`：索引越界。`KeyError`：字典键不存在。`EOFError`：程序想读更多行而输入已结束，核对题面行数。`NotImplementedError`：尚有未替换的练习标记。不要见错就整份重写；先定位读取、计算、输出三个阶段。

## 验收清单

- 能说明input读取结果是文字，知道何时用int、float。
- 能手动追踪循环每轮变量，处理0轮循环和分数边界。
- 能选择列表、字典、集合，解释索引为什么从0开始。
- 能解释return如何把结果交回调用处，以及多组数据何时重置状态。
- P001–P014都用自己的代码通过，stdout中没有调试文字。

```powershell
.\.venv\Scripts\python.exe check.py --chapter 01
```

遇到卡点先展开三级提示；完成后再查看独立题解。下一站：[第02章 数学与NumPy](../02_math_numpy/README.md)。

核对依据：[Python 3.11官方教程](https://docs.python.org/3.11/tutorial/)、[官方排序指南](https://docs.python.org/3.11/howto/sorting.html)。这些是语法和行为的一手资料；本章示例与题目为独立编写，学习无需联网。
'''
    numpy_chapter = r'''# 第 02 章：必要数学与 NumPy

先修：已能完成第01章的输入、类型转换、循环、列表、函数和二维列表。目标不是背API，而是把公式中的每一项对应到数组形状与计算步骤。只需要CPU和NumPy，无需GPU、Redis或外部数据。本章验收环境为Python3.11.15、NumPy2.2.6；下面使用的基础接口以本地验证为准。

## 先从列表走到数组

列表可保留任意Python对象；数值数组适合在一致类型的多维数据上计算。NumPy是第三方库，导入后常用np作为简称。下面每个符号先理解，再去P015实践：

```python
import numpy as np

values = [1.0, 2.0, 3.0]
array = np.array(values, dtype=float)
print(array.sum())
print(array.mean())
```

`import numpy as np` 让后续代码用np访问该库。`np.array(...)`将列表转为数组；`dtype=float`这个具名参数要求保存浮点数。`array.sum()`、`array.mean()`是数组的方法，分别计算和、平均值。小括号表示执行；不加括号就只是引用方法。输入仍是普通文本：split后逐个float转换再建数组；不把JSON当作学生必会格式。

数组与列表的运算含义不同。`[1,2]+[3,4]`将列表连接为四个元素；两个同形状的数组相加，会逐位置得到[4,6]。初学时遇到结果不符合预期，先问自己拿到的是列表还是数组。

## P015：和与平均数

设n个数x₁到xₙ，总和为Σxᵢ；Σ只是“把指定项都加起来”的数学简记。均值μ=(Σxᵢ)/n。对1、2、3、4，总和10，个数4，均值2.5。μ不一定等于输入中的某个数；均值反映中心，不能反映所有分布细节。

P015要求先用普通循环实现，再用NumPy计算。输入只读一次，保证对比对象相同。不要只调用NumPy然后把同一结果打印两遍，这样没有练到从循环过渡到数组。两种方法实现同一定义，浮点求和的顺序可能影响最末几位，因此按容差比较。

## P016：总体方差与平方偏差

方差描述偏离均值的程度。先算μ，再算每个(xᵢ−μ)，平方消去正负抵消，最后取平均：var=Σ(xᵢ−μ)²/n。数据1、2、3的μ=2，偏差-1、0、1，平方1、0、1，总体方差2/3。

NumPy中数组减标量会给每个元素减去同一个值，`difference ** 2`会对每项平方；`**`是乘方，`^`不是。总体方差分母为n，记为ddof=0。样本方差常用n-1，对应ddof=1；本题把输入当作整个总体，所以不作这种修正。单个数总体方差为0。

用0、2、4、6手算：μ=3，平方偏差9、1、1、9，总和20，20/4=5。若程序得到20/3，说明混用了分母；若得到0，可能只对未平方的偏差求了平均。两遍中心化定义更容易核查，也比直接做两个大数相减的公式更适合本练习，但仍受浮点精度限制。

## P017–P018：向量、距离与点积

向量就是按顺序对应的一排数，不必先想复杂几何。二维向量可视为平面坐标，高维则可视为更多特征。两行输入必须同维，第一项与第一项对应，不可各自排序。

欧氏距离是sqrt(Σ(aᵢ−bᵢ)²)。从(0,0)到(3,4)，差(-3,-4)，平方和9+16=25，开方5。`np.sqrt(...)`计算非负平方根。计算顺序是做差、平方、求和、开方；绝对值之和对应另一种距离，不能替代。

点积是Σaᵢbᵢ。向量(1,2,3)与(4,5,6)，逐项乘积4、10、18，总和32。NumPy的`a*b`只得到逐元素乘积数组，再sum才得到点积。点积可能为负：(-2,3)·(4,-1)=-11；两个非零向量点积也可能为0。距离与点积算的是不同量，不要把开方机械加到每题。

## P019：矩阵乘法先看共同维度

矩阵A形状(r,k)，B形状(k,c)，共同的k必须匹配，输出形状(r,c)。圆括号(r,c)是有顺序的两个尺寸，可理解为一个元组；`np.zeros((r,c),dtype=float)`据此建立全零结果。二维数组的位置用`a[i,j]`，从0开始；它与二维列表的`matrix[i][j]`写法不同。

每个输出位置由A的一行和B的一列做点积：Cᵢⱼ=ΣₜAᵢₜBₜⱼ。外层选i，再选j，最内层沿t累加。这是P018的一维点积在多个输出位置重复执行。不要一开始用现成的矩阵乘法掩盖行列对应关系。

例：A=[[1,2,3],[4,5,6]]，B=[[7,8],[9,10],[11,12]]。输出(0,0)是1×7+2×9+3×11=58；(0,1)为64；第二行为139、154。A是(2,3)，B是(3,2)，输出(2,2)。若写成逐元素乘法A*B，连形状都对不上。学会手写之后，可用`a @ b`或NumPy matmul核对定义，本题参考实现仍为三层循环。

矩阵要按文本行输出，直接print整个数组会带方括号。`print(*row)`中的星号把一行元素依次作为多个参数，输出时默认用一个空格相隔；这是输出语法，并不改变算法。

## P020：shape是尺寸，reshape是重新摆放

`array.shape`是属性，不用括号；一维六元素形状是(6,)，二维两行三列是(2,3)。`reshape((2,3))`将六个值按默认行优先顺序放成两行。1到6得到第一行1 2 3、第二行4 5 6；改成(3,2)则得到三行1 2、3 4、5 6。

总元素数必须守恒，2×3=6，不能reshape成(2,4)。reshape不会排序，不等同于转置。它有时共享原数组存储、有时需要复制，不把所有reshape都当作独立拷贝；本题不会修改重排后的数据来考共享细节。

## P021：索引和广播从右对齐

`a[i,:]`是第i行全部列，`a[:,j]`是第j列全部行，冒号表示这一维全部位置。广播允许形状不同的数组运算，规则是从最右维度向左比较：每一对尺寸相等，或至少有一个是1，才兼容；缺失的左侧维度视为1。

矩阵(2,3)加向量(3,)时视为(2,3)+(1,3)：给每行加相同三个列偏移。若想给两行分别加100和200，必须让偏移为(2,1)，例如`offset.reshape((2,1))`，让每行的一个数扩展到三列。写成(2,)会从右对齐到3，尺寸2与3冲突；方阵中甚至可能悄悄按错误方向计算，因此测试要用矩形。

手算A=[[1,2],[3,4]]：加[10,20]得到[[11,22],[13,24]]；独立从原A加[[100],[200]]得到[[101,102],[203,204]]。第一块按列分配偏移，第二块按行分配偏移。不要先原地改变A再算第二块，否则改变了任务。

## P022：axis指被合并的维度

形状(r,c)的axis=0是行位置，axis=1是列位置。沿axis求和意味着合并该维度并把它从结果中消掉。`a.sum(axis=1)`合并每行里的c列，留下r个行和；`a.sum(axis=0)`合并r行，留下c个列和。不要从axis数字直接猜“输出的是行还是列”，应看哪个维度被消掉。

对[[1,2,3],[4,5,6]]，行和[6,15]，列和[5,7,9]。两条输出长度分别2和3，总和都为21。用单行、单列再检查一次：一行时列和还是原来的各个值；一列时行和还是原来的各个值。sum()不传axis则把所有元素合成一个整体和，不能满足两条向量输出。

## 逐题入口

{links02}

## 常见错误和自查方法

`ModuleNotFoundError: numpy`通常表示用了环境之外的解释器，先用本仓库的 `.\.venv\Scripts\python.exe`。`ValueError`若提到reshape，核对尺寸乘积；若提到broadcast，画出从右对齐的形状。二维数据出现object或不规则行，先检查每行是否读足列数。输出多出方括号，检查是否应该逐行print(*row)。计算得到NaN或inf，本课程检查器拒绝非有限结果，应检查除零、空数据或错误公式；本章合法输入已避免这些情况。

不要只盯最后数字。先写输入形状，再写每一步形状，再手算一个位置。方差看分母，距离看平方根，点积看是否求和，矩阵乘法看行列方向，reshape看元素顺序，广播看右对齐，axis看哪一维消失。小例子比背一长串API更能定位错误。

## 验收清单

- 能分别手算均值、总体方差、距离和点积，并说出公式分母或最后一步。
- 能从(r,k)与(k,c)推断矩阵乘积形状，计算一个输出位置。
- 能区分(r,c)、(c,)、(r,1)，解释广播方向。
- 能在不运行代码前写出两个axis聚合结果长度。
- P015–P022自己实现通过，理解纯Python与NumPy的对应关系。

```powershell
.\.venv\Scripts\python.exe check.py --chapter 02
```

完成后进入 [第03章 预处理](../03_preprocessing/README.md)。

核对依据：[Python 3.11官方教程](https://docs.python.org/3.11/tutorial/)、[NumPy绝对初学者指南](https://numpy.org/doc/stable/user/absolute_beginners.html)、[NumPy广播文档](https://numpy.org/doc/stable/user/basics.broadcasting.html)、[NumPy官方教程仓库](https://github.com/numpy/numpy-tutorials)。曾参考官方教程仓库的教学组织方式；本课程采用可离线运行的单文件练习，不依赖notebook。官方stable网页可能更新到较新版本，本课程接口均以本地NumPy2.2.6实测。链接用于进一步阅读，学习和验收无需网络。
'''
    for chapter, text, start, end, placeholder in [
        ("01_python", python_chapter, 1, 14, "{links01}"),
        ("02_math_numpy", numpy_chapter, 15, 22, "{links02}"),
    ]:
        links = "\n".join(f"- [P{n:03} {DATA[n-1][0]}](problems/P{n:03}/README.md)" for n in range(start, end+1))
        write(f"chapters/{chapter}/README.md", text.replace(placeholder, links))


def build_content():
    assert len(LESSONS) == len(DATA) == 22
    for number, (lesson, item) in enumerate(zip(LESSONS, DATA), 1):
        title, mode, pairs = item
        chapter = "01_python" if number <= 14 else "02_math_numpy"
        pid = f"P{number:03}"
        directory = f"chapters/{chapter}/problems/{pid}"
        first_input, first_output = pairs[0]
        sample_input = first_input if first_input else "（空输入；不要输入这一行说明）\n"
        hints = "\n\n".join(
            f"<details><summary>提示{i}</summary>\n\n{text}\n\n</details>"
            for i, text in enumerate(lesson["hints"], 1))
        if number == 14:
            next_link = "[下一章：必要数学与 NumPy](../../../02_math_numpy/README.md)"
        elif number == 22:
            next_link = "[下一章：预处理与特征工程](../../../03_preprocessing/README.md)（完成后再前往）"
        else:
            next_link = f"[下一题 P{number + 1:03}](../P{number + 1:03}/README.md)"
        prerequisite = "无；从本章开头的终端与文件说明开始。" if number == 1 else f"先完成 P{number - 1:03}；本题新概念见下方‘开始前先读’。"
        readme = f'''# {pid} {title}

本题为原创训练题。先修：{prerequisite}

## 任务

{lesson['task']}

## 开始前先读

{lesson['learn']}

## 输入输出与约束

{lesson['io']}

{lesson['bounds']}

标准输出只包含要求的结果。数值题允许等值的常见数值写法；行数与每行个数仍必须符合要求。本题比较模式为 `{mode}`。

## 完整样例

输入（与 cases.json 第一个案例一致）：

```text
{sample_input}```

输出：

```text
{first_output}```

手算：{lesson['hand']}

## 三级提示

{hints}

## 动手与验收

在仓库根目录操作，编辑本目录 `exercise.py`。`raise NotImplementedError(...)` 是故意放入的未完成标记：将它替换为自己的实现，或在完成相应部分后删除它；否则程序会在这一行主动报错。保留已经给出的输入脚手架，不要把题解导入练习。

```powershell
.\\.venv\\Scripts\\python.exe {directory}/exercise.py
.\\.venv\\Scripts\\python.exe check.py {pid}
```

第一条命令进入等待输入状态时，依次输入样例的各行，每行回车；P001 不等待输入。第二条自动运行本题至少5个案例。先手算样例，再看失败案例，必要时展开下一条提示。

完成后再阅读 [独立参考解与讲解](../../../../solutions/{pid}.md)。{next_link}；[本章教程](../../README.md)。

来源用于核对语法或数学定义，题目及答案独立编写：[一手资料]({lesson['source']})。
'''
        write(f"{directory}/README.md", readme)
        write(f"{directory}/exercise.py", "# " + pid + " " + title + "：请先阅读同目录 README.md。\n" + lesson["scaffold"])
        write(f"solutions/{pid}.py", "# " + pid + " " + title + "；独立运行，无其他答案依赖。\n" + lesson["code"])
        solution = f'''# {pid} {title}：题解

先尝试 [题目](../{directory}/README.md)，再对照本页。

## 思路和关键步骤

{lesson['steps']}

## 再做一次手算

{lesson['hand']}

## 可运行代码

实际参考代码为 [{pid}.py]({pid}.py)，本页不另行复制代码，以免出现不同版本。它只读标准输入、只写要求的标准输出，可以作为单文件运行；不依赖其他参考解。

在仓库根目录执行：

```powershell
.\\.venv\\Scripts\\python.exe solutions/{pid}.py
.\\.venv\\Scripts\\python.exe check.py {pid} --solution
```

第一条需手动输入题面给出的样例；第二条用同一份 .py 自动验证本题所有案例。正式学习通常运行不带 --solution 的命令检查自己的练习。

## 复杂度

{lesson['complexity']}

## 易错点与自查

{lesson['pitfall']}

比较样例中间值，定位是读取、计算还是输出的错误。不要在最终stdout保留调试文字。

## 来源

[一手资料]({lesson['source']})，用于定义或API核对。Python章另可查阅 [Python 3.11 官方教程]({PYTHON})；数组章另可查阅 [NumPy 官方入门]({NUMPY})。题目、手算数据和参考代码均为本课程独立编写。
'''
        write(f"solutions/{pid}.md", solution)
    build_chapters()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", action="store_true")
    parser.add_argument("--content", action="store_true")
    args = parser.parse_args()
    if args.cases:
        build_cases()
    if args.content:
        build_content()
