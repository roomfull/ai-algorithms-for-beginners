# Task 2：Python 与 NumPy 入门（22 题）

先读 docs/implementation-plan.md 的全局约束和统一接口，再阅读 check.py --help 或源码确认已实现接口。只拥有 chapters/01_python、chapters/02_math_numpy、solutions/P001–P022.{py,md} 和对应 tests/test_foundations.py。

逐题顺序锁定：P001 第一行固定输出；P002 变量与四则运算；P003 字符串拼接；P004 input 与 int/float；P005 if 分类；P006 for 累加；P007 while 计数；P008 列表筛选；P009 字典词频；P010 集合去重；P011 排序与平票；P012 函数与 return；P013 二维列表行和；P014 多组数据考试输入输出验收。
P015 求和均值（NumPy 与纯 Python 对照）；P016 总体方差 ddof=0；P017 欧氏距离；P018 点积；P019 矩阵乘法；P020 数组 shape/reshape；P021 索引与广播；P022 axis 行列聚合验收。

每章 README.md 充分教学，不只是目录：从终端、文件、逐句代码过渡到抽象。变量赋值、类型、索引从零开始；P001–P014 在对应新语法首次出现前讲明白，不提前使用推导式/函数/递归/复杂解包。P001 的固定输出 5 案例可用不同被忽略的 stdin，须说明程序不读输入且这只是输出格式练习。其余题的至少 5 案例必须有真实不同输入，预期来自独立手算。

每题 5 件材料按统一格式生成。每题必须有具体手算例，不能仅写“遍历计算”；三级提示有实质差异。讲解可以将函数/循环代码块放题解中。标准输出使用行式数值/文本，不把 JSON 输入当学生主流程。每章 README 包含逐题链接、先修、示例演算、常见报错/数学误区、验收清单。引用 Python 3.11 官方教程 https://docs.python.org/3.11/tutorial/ 与 NumPy https://numpy.org/doc/stable/user/absolute_beginners.html。

先写案例观察缺失参考解失败，再实现；检查本包全部参考解。额外独立测试至少验证矩阵乘法的手算、广播轴差异、总体方差（不从 solutions 生成期望）。若写生成器用于批量输出文件，生成器只作维护工具放 tools/build_foundations.py 并保留可维护的题目特有内容，不用重复空泛段落凑数。

不修改共享检查器/环境/根 README；不提交 Git。报告 docs/work/task-2-report.md，写详细验证与任何问题，最终简短回复。
