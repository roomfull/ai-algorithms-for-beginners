# Task 6 最终交付报告

2026-10-14，Task 6已完成。环境为Python 3.11.15、NumPy 2.2.6；唯一必需第三方依赖仍为NumPy。

## 交付范围

- exams/mock01–mock04：每卷2题，合计8题48个独立手算/闭式预期案例；题面、约束、样例手算、三级提示、最小solve/main练习、cases.json及卷入口。
- solutions/M01A–M04B.py和.md：每份参考程序可独立运行，代码解释、步骤、复杂度、易错点与一手来源齐全。
- README.md与docs/START_HERE.md：实际零基础入口、无需激活命令、九章目录/先修/标准、失败定位与模拟卷入口，清除基础阶段的临时未交付表述。
- PROGRESS.md：按章/卷分组的88个标准Markdown `- [ ]` 手动勾选条目，各含状态、理解、复习与备注；docs/MISTAKES.md：真实第一题试错例子与可复制模板。
- docs/REFERENCES.md和MAINTAINING.md：分专题一手官方/GitHub资料、教学约定与库默认行为区别、维护格式、真实验收数字及生成器覆盖练习警示。
- tools/build_mock_exams.py：维护生成器按卷执行，固定预期来自tests/test_mock_algorithms.py中的独立手算数据；不运行参考答案生成预期。
- tests/test_mock_algorithms.py与test_course_integrity.py：初版14个模拟算法方法（8题手算+6性质/枚举），修复轮1新增1个输入范围/固定数据同步回归，当前15个模拟测试方法；另有10个完整性方法。

## 实际验证

全部从项目根目录使用独立环境，无需激活。整包完成后，各执行一次：

```powershell
.\.venv\Scripts\python.exe check.py --all --solution
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

第一条实际输出“通过 461/461 个案例，共 88 题”，退出码0；第二条实际输出“Ran 104 tests in 23.885s”与“OK”，退出码0。原始完整输出分别保存在[task-6-solutions.log](task-6-solutions.log)和[task-6-unittest.log](task-6-unittest.log)。此104为unittest方法数，461为题目案例数，未混为同一指标。

实盘普通题80题413case，新增模拟题8题48case；总计88题461case。分章题数：01=14、02=8、03=8、04=8、05=12、06=8、07=12、08=6、09=4；每模拟卷2题12case。

TDD证据：[task-6-red.log](task-6-red.log)记录14项模拟算法方法因缺少答案失败；[task-6-integrity-red.log](task-6-integrity-red.log)记录导航缺失等结构失败。初版完整性中将注释中的“不要导入solutions”误作导入、用空白贪婪匹配无法正确提取空输入、05/06章期望分界错误，这些测试自身问题已按实际AST/样例/元数据修正。进度表由表格改为标准勾选前，88项勾选测试实际失败0!=88，再改成88项通过。各卷手算/性质GREEN与逐卷落盘记录见[task-6-checkpoint.md](task-6-checkpoint.md)。

模拟算法独立验证包含：MST遍历所有三边子集求最小连通树；KNN平移与正缩放不变；余弦输入正倍数不变；PageRank质量和与环对称性；量化MSE≤scale²/4且整数码在范围；worker/微批次重新分割后梯度更新不变。48case还覆盖训练恒定列、小数距离平票、投票平票、空文本/查询、训练df不含查询、悬挂网页/精确L1阈值/未收敛、空簇/最终重分配、正负十进制半格、ReLU/互相关不翻核/池化余边、不同样本权重。

完整性验收准确88ID和13组计数、全部材料和来源、每题至少5case且名称唯一、混合输出行形状合法、首样例代码块原样匹配首case、88练习保留NotImplementedError且不导入答案、答案不互相导入、九章教程与所有课程本地Markdown链接、88项勾选。人工审读模拟卷的定义、手算、输出顺序、空簇/平票/舍入与复杂度，结构关键字检查不代替数学审查。

## 跨包修复与范围限制

跨包修复经主代理授权：P001输入样例将空输入说明移到代码块外，代码块保留真正空输入；tools/build_foundations.py同步模板，不重新生成普通题，不改exercise/cases或check.py。既有第一题试错演练的输入输出和命令接口未改变，复用[beginner-walkthrough.md](beginner-walkthrough.md)，其中临时错误→提示→正确5/5已实测，正式练习不被答案替换。

生成器是维护工具，会覆盖练习脚手架，普通学习无需运行。Fraction小规模精确边界、排名键舍入和各算法规则均在题面明示；课程是原创教学及单机数值模拟，不声称正式真题、考试评分或实际系统加速。

未解决问题：无。没有Git提交；等待主代理对最终差异作独立审查。

## 独立审查修复轮1（基线41d5dc6）

根据[task-6-review.md](task-6-review.md)修复两项材料问题，参考算法不变：

- M01A“常量列忽略”案例的查询`2 999`超出特征绝对值≤100约束。独立固定数据源与exams/mock01/M01A/cases.json同步改为`2 100`，期望仍是近邻1、标签8。生成器直接读取该固定数据源，因此无需重生成或覆盖练习。训练第二列恒为5而查询为100，继续覆盖忽略训练常量列的目的。
- REFERENCES神经网络来源题号更正为P051–P054全连接/ReLU、稳定softmax、交叉熵与梯度；P055–P057卷积、最大池化与转置卷积；GAN仅P058。平均池化仍对应M04A，额外注明P056最大池化的一手来源。

新增`test_m01a_constant_fixture_within_bounds`：核对磁盘案例与独立源相同、查询绝对值≤100、查询常量列仍不同于训练值。先观察RED（[2.0,999.0]失败、退出码1），再修数据观察GREEN。

实际相关验证命令与输出：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_mock_algorithms.py -k m01a -k knn -v
.\.venv\Scripts\python.exe check.py M01A --solution
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_course_integrity.py -v
```

依次通过3个测试方法、6/6题目案例、10个完整性方法，退出码均0；RED和修后原始精简输出保存于[task-6-repair-1.log](task-6-repair-1.log)。额外只加载并统计unittest套件（未执行），当前定义105个方法。原始全库日志仍为修复前461/461、104方法OK并原样保留；此轮未重跑全套，以相关测试验证修改范围。题目和案例总数保持88题461case。
