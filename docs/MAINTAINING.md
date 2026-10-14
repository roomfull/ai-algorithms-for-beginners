# 课程维护与验收

学习者只需要阅读题面、修改exercise.py并运行check.py。下面是维护课程材料的方法；不要用参考解覆盖学员作答。

## 环境与文件布局

固定Python 3.11与NumPy 2.2.6；本机验证为Python 3.11.15。唯一必需第三方库为NumPy，见根目录requirements.txt。标准库Fraction用于小规模精确十进制边界。课程离线运行，无GPU、Redis或外部数据。

- 普通题：`chapters/章目录/problems/P001/{README.md,exercise.py,cases.json}`。
- 模拟题：`exams/mock01/M01A/{README.md,exercise.py,cases.json}`；卷入口在`exams/mock01/README.md`。
- 参考程序/题解：`solutions/题号.py`和`solutions/题号.md`，每份程序可独立提交，不导入其他答案。
- 独立算法测试和检查器测试：`tests/test_*.py`。

题目发现按上述目录扫描，不要添加中心注册表。普通题88题目标中的80题为P001–P080，模拟卷8题为M01A–M04B。

## 元数据格式

cases.json为UTF-8对象，字段如下；新增题前先写手算或独立推导的预期值，不能运行参考解生成预期。

```json
{
  "id": "P001",
  "chapter": "01",
  "title": "第一行固定输出",
  "mode": "text",
  "requires": [],
  "cases": [
    {"name": "样例", "input": "", "expected": "Hello, Python!\n"}
  ]
}
```

此处仅示范结构，正式每题至少5个案例，name题内唯一。chapter为`01`–`09`或`M01`–`M04`；mode为text/int/float；requires为[]或["numpy"]。可选timeout为正秒数。输入保证符合该题约束，不要求提交程序自行验证所有无效输入。

混合输出每个case可以增加`line_modes`，例如`["int","float"]`，长度等于expected去末尾空行后的行数。整数标签行严格以十进制整数解析；浮点行允许abs_tol=rel_tol=1e-6，拒绝NaN/inf，先查行数/每行列数。文本允许CRLF/LF、行尾空白与末尾空行差异，保留行内内容。

## 新增与修改材料

先写独立手算案例和必要数学性质测试，观察缺实现/错误行为失败，再实现参考解并验证。题面必须写清输入、输出、约束、首案例原样样例、手算、三级提示、运行命令和一手来源；空输入的说明放在代码块外。题解应说明思路、关键步骤、实际复杂度与易错点，来源不代表照搬代码。练习保留NotImplementedError，不导入答案；模拟卷仅给最小solve/main，输入输出由学员写。

新增后同步章节/模拟卷入口、根目录路线、PROGRESS的题目链接和真实统计；完整性测试的88个ID和分章计数是本期交付契约，扩展课程时需有意更新该契约。

**tools/build_*.py均为课程维护生成工具，可能重新写题面、cases、参考解以及exercise脚手架，覆盖学员的改动。只在干净副本或已经另存学员作答后运行；普通学习不需要运行这些生成器。** build_mock_exams.py的每卷数据来自tests/test_mock_algorithms.py中的独立手算固定案例，不读取参考答案产生预期。其他生成器的参数请先看各文件，不将其当作判题或恢复作业工具。

## 验证命令与真实统计

全部在项目根目录，无需激活环境：

```powershell
.\.venv\Scripts\python.exe check.py --list
.\.venv\Scripts\python.exe check.py --all --solution
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

改一题后可用`check.py 题号 --solution`以及对应测试文件定位；全库核验在整包完成时做，修复后只跑相关检查，避免重复无意义运行。默认check.py运行exercise，因此全新课程出现“未完成”是预期起点。

2026-10-14实际验收：88题参考解通过461/461案例；unittest discover通过104个测试方法；两个命令退出码均为0。每章题数为14、8、8、8、12、8、12、6、4；每模拟卷2题12案例。命令和证据记录在[最终交付报告](work/task-6-report.md)，原始输出见[全解日志](work/task-6-solutions.log)和[单元测试日志](work/task-6-unittest.log)。修改后以新日志重新统计，不凭计划估计通过数。

随后独立审查修复轮1只调整M01A一个越界查询案例及来源题号，新增1个范围回归。修后相关算法3方法、M01A6/6案例、完整性10方法均通过，见[修复日志](work/task-6-repair-1.log)；仅加载统计当前定义105个方法，未重跑全套，原104方法全库日志保留为修复前证据。

完整性检查验证准确ID与分章数量、文件、样例代码块和首case相符、题内case名称唯一与数值形状合法、未完成练习AST、答案互相独立、章节教程及本地Markdown链接、88项学习进度。它验证结构与连接；数学正确性还需独立手算/枚举/性质测试及人工阅读，不能只搜索关键字当作内容审查。

[第一题试错演练](work/beginner-walkthrough.md)在临时副本走过未完成→错误→读提示→正确5/5，正式练习保持原状；若输入输出或起步流程改变，需要重新走该流程。单纯把空输入说明移出代码块不改变运行接口，本次保留原演练证据。

[来源与约定](REFERENCES.md) · [返回课程](../README.md)
