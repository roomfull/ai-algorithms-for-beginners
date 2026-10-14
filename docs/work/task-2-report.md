# Task 2 交付与验收报告

日期：2026-10-14。范围：第01章、第02章，P001–P022。使用已准备的项目解释器 `.\.venv\Scripts\python.exe`（Python3.11.15、NumPy2.2.6）。

## 完成内容

- `chapters/01_python/README.md`：从文件、终端、解释器、保存运行开始，逐步讲解变量、类型、读入、条件、循环、容器、稳定排序、函数、二维列表和多组输入。
- `chapters/02_math_numpy/README.md`：列表到数组、均值、总体方差、距离、点积、矩阵乘法、shape/reshape、广播和axis；各概念有手算与形状推导。
- 22题，每题五件材料：题面README、保留未完成状态的exercise.py、cases.json、独立solutions/Pxxx.py、题解solutions/Pxxx.md。共110份逐题材料，另有两份章节教程。
- 111个案例：P005六个，其余各五个。所有题均有至少五种不同stdin；P001专门说明忽略stdin，非算法变例，其余均为真实不同输入。
- `tests/test_foundations.py`：4个额外独立数学测试。
- `tools/build_foundations.py`：维护生成器，题目特有描述、提示、手算、代码、复杂度与误区均显式保存在LESSONS中；不是从答案运行结果生成expected。

未修改共享检查器、环境和根README；未创建Git提交；未启动其他代理。

## TDD：先案例，再实现

首先只创建生成器的DATA与`--cases`分支和独立测试，未写参考解。先运行：

```powershell
.\.venv\Scripts\python.exe tools/build_foundations.py --cases
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_foundations.py
```

实际结果：4个测试全部FAIL，失败断言为缺少独立参考解P022、P021、P016、P019；`Ran 4 tests ... FAILED (failures=4)`。这不是导入错误或错误的期望值。

同样在参考解缺失时运行：

```powershell
.\.venv\Scripts\python.exe check.py --chapter 01 --solution
.\.venv\Scripts\python.exe check.py --chapter 02 --solution
```

结果：第01章0/71，第02章0/40；原因逐案为“环境问题：找不到程序 solutions/Pxxx.py”。22题的案例均已先存在并接受检查。

之后才添加LESSONS中的实现、练习和教程，运行`tools/build_foundations.py --content`生成正式文件。

## Green验收

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_foundations.py
```

实际结果：`Ran 4 tests in 0.744s`，`OK`。

```powershell
.\.venv\Scripts\python.exe check.py --chapter 01 --solution
```

实际结果：`通过 71/71 个案例，共 14 题`，退出码0。

```powershell
.\.venv\Scripts\python.exe check.py --chapter 02 --solution
```

实际结果：`通过 40/40 个案例，共 8 题`，退出码0。上述两章验证分别约4.8秒、7.6秒。

```powershell
.\.venv\Scripts\python.exe -m py_compile tools/build_foundations.py tests/test_foundations.py
```

实际结果：退出码0。另用ast.parse检查全部22份练习与22份参考解，无语法错误。结构自查得到：`AUDIT: 22 problems, 111 cases; AST, exercise markers, sample outputs, solution paths OK`。

```powershell
.\.venv\Scripts\python.exe check.py P001
```

实际结果：`[未完成] ... NotImplementedError: 请按题目提示完成这里`，0/5，退出码1。这是有意保留的学习起点，证明未用答案覆盖练习。正式练习P001的错误→提示→正确全流程演练由总体任务进行，本包只验证起点未完成状态。

## 独立期望值的依据

cases.json的expected均手工录入常量，未导入、未执行参考解生成。案例覆盖零、负数、单元素、空筛选、未出现的查询词、分数边界、平票、单行/单列、矩形矩阵等。NumPy统计与线性代数的关键手算如下：

- P015：[1,2,3,4]总和10、均值10/4=2.5；[-3,-1]总和-4、均值-2。
- P016：[1,2,3]的均值2，平方偏差和2，总体方差2/3；[0,2,4,6]均值3，平方偏差和20，20/4=5。
- P017：(0,0)到(3,4)的平方差和25，距离5；三维(1,2,2)到零距离3。
- P018：(1,2,3)·(4,5,6)=4+10+18=32；(-2,3)·(4,-1)=-8-3=-11。
- P019：2×3与3×2矩阵乘法，四个值分别为7+18+33=58、8+20+36=64、28+45+66=139、32+50+72=154。
- P020：1到6按行填2×3，第一行1,2,3、第二行4,5,6；单列按原顺序逐行输出。
- P021：原A=[[1,2,3],[4,5,6]]，列偏移[10,20,30]得到[[11,22,33],[14,25,36]]；行偏移[100,200]独立从原A计算得到[[101,102,103],[204,205,206]]。
- P022：[[1,2],[3,4],[5,6]]行和[3,7,11]、列和[9,12]，长度分别3和2，总和都21。

独立测试不复用solutions中的函数，也不调用NumPy生成期望。P019验证完整矩形乘积；P016刻意区分分母n与n-1；P021使用2×3矩阵暴露广播方向错误；P022使用3×2矩阵验证axis与输出长度。所有期望由上述公式展开录入。

## 人工教学检查

1. **首次语法先解释**：逐题检查“开始前先读”及先修章节。P001介绍print、字符串和注释；P002先解释input/int最小用途并保留输入脚手架，明确不必一开始背下来，P004再专练int/float。P003介绍字符串拼接；P005分支与四空格缩进；P006循环、range与累加赋值；P007while终止；P008列表、split、索引和join；P009字典及键存在判断；P010集合；P011稳定排序与标准库itemgetter，未提前使用自定义函数、lambda、推导式或复杂解包；P012才定义函数与return；P013二维列表；P014无新语法。NumPy章先解释导入、dtype和方法，P019再解释元组形状、二维索引及仅用于输出的星号解包，后续题建立在此前语法上。
2. **raise替换/删除**：每题动手部分明确指出raise是故意的未完成标记，必须替换或删除；章节开头也解释为何只在它前面补代码仍会报错。P012的标记位于待实现函数中，其余在顶层。全部正式练习均保留NotImplementedError，未导入答案。
3. **题解与实际代码一致**：每份题解只链接同题独立.py，不另复制可能漂移的代码块；给出`solutions/Pxxx.py`直接运行及`check.py Pxxx --solution`命令。检查器实际运行的就是该文件。
4. 逐题样例输出与cases第一个案例逐字一致；P001空输入特别说明，其他题样例完整。三级提示依次给方向、数据/公式、具体操作，均为题目特有内容。复杂度与实际实现对应，例如P019为显式O(rkc)，P011为两次稳定排序，不宣称哈希操作无条件最坏常数。

## 资料核对

本次阅读了 [Python 3.11官方教程](https://docs.python.org/3.11/tutorial/)、[NumPy官方初学者指南](https://numpy.org/doc/stable/user/absolute_beginners.html)、[NumPy官方教程GitHub仓库](https://github.com/numpy/numpy-tutorials)，结合稳定排序、广播、var/dot/matmul定义的官方链接组织内容。各题面和题解单独标注一手来源；教程内容、题目和答案独立编写。课程无需联网即可学习运行。

注意官方stable在线文档在本次浏览时指向较新NumPy文档；课程只使用本地NumPy2.2.6已实测的基础接口，不要求升级。

## 后续集成事项

- 本包内部链接均有效。仅两条指向后续`chapters/03_preprocessing/README.md`的前进链接暂时不存在：第02章末尾、P022末尾；待Task3创建该章后自然有效，最终审计须复查。
- 本包不把所有参考解通过等同于用户已掌握，也不将原创训练题称为真题或高频题。
- 无其他已知阻塞或未实现需求。
