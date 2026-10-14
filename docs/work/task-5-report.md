# Task 5 完成报告

交付范围：P059–P080，共22道原创教学题；07图分析12题、08压缩6题、09分布式数值模拟4题。每题均有README、保留未实现状态的exercise.py、cases.json、独立可提交的参考答案和题解。初次交付110案例；修复轮1后P069有7案例，其余每题5案例，当前总计112个。无需新增第三方库、GPU、Redis或外部数据。

## 文件

- `chapters/07_graphs/README.md` 与 `problems/P059`–`P070`：点边方向、邻接表、队列栈、BFS/DFS、并查集、贪心MST、三角/双色、PageRank概率流和收敛。
- `chapters/08_compression/README.md` 与 `problems/P071`–`P076`：权重、位数、掩码、行L1、scale、精确舍入、反量化、误差界和理论字节。
- `chapters/09_distributed/README.md` 与 `problems/P077`–`P080`：半开分片、全局batch、简单/加权平均、不等microbatch累积和单次SGD；明确为单机教学模拟。
- `solutions/P059.py`–`P080.py` 和同编号 `.md`：22份独立答案，无互相导入；代码有中文关键注释，题解复杂度对应实际实现。
- `tests/test_system_algorithms.py`：当前15个测试方法，其中112案例执行1个、完整性1个、独立算法性质13个（修复轮1新增十进制精确停止回归）。
- `tools/build_system_algorithms.py`：持久化原始题面及独立预期，可重建学习材料；不调用答案生成预期，不生成/改写参考代码。
- `docs/work/task-5-checkpoint.md`：分批落盘检查点。

首次交付新增117个文件（22×5题目材料=110，3教程、1测试、1生成器、1检查点、1报告），修复轮1另加1份精简日志。未修改共享检查器或其他章节，未执行Git命令或提交。

## RED → GREEN 证据

先写并落盘P059–P073的75案例和全22题的性质测试，再创建参考实现。首次命令：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_system_algorithms.py
```

RED：运行14个方法，88个失败（包括案例subTest），均为缺少对应参考实现的明确断言；没有把语法/导入错误充作算法RED。随后以2–4题一批写参考实现并执行案例检查。量化材料追加后，`-k quant`另观察3个缺少P074/P075/P076的RED；分布式材料追加后，`-k microbatch`、`-k shards`、`-k average`各观察1个缺少实现的RED。之后逐批实现并GREEN。

首次交付完整运行14/14方法通过（当次0.146秒）；修复轮1最终15/15通过（0.151秒）。耗时只记录各次运行，不作性能结论。未完成exercise仍保留NotImplementedError，不用参考答案覆盖学习文件。

## 检查器验收

```powershell
.\.venv\Scripts\python.exe check.py --chapter 07 --solution
.\.venv\Scripts\python.exe check.py --chapter 08 --solution
.\.venv\Scripts\python.exe check.py --chapter 09 --solution
```

首次结果分别为60/60（12题）、30/30（6题）、20/20（4题），合计110/110。修复轮1图章复验62/62，其他两章未变，当前112案例在完整unittest案例方法中全部通过。答案经检查器作为单文件独立进程运行。整数输出全部使用int比较；P066/P067断连案例单独标text；混合浮点与掩码/量化码/轮数/字节的输出按case配置line_modes，严格核验整数行而不让float模式吞掉整数错误。

## 独立性质与边界

- 三角计数：5顶点全部1024种简单图，用三点组合及全边条件独立枚举。
- 搜索/双色/综合：4顶点全部64种简单图，Floyd距离作BFS/连通oracle，枚举2^4种着色作二分oracle，核验P061/P062/P065/P070；每图检查4个BFS起点。
- MST：4顶点全部64种边子集，独立枚举n-1条边的所有候选生成树，连通候选的最小权重同时核验Kruskal与Prim，包含负权、0权与孤立点。
- PageRank：4组图显式有理数转移矩阵检查单轮与概率和；迭代核验L1等于阈值、略低阈值、上限未收敛与固定点，输出末轮分布。
- 剪枝：精确100×0.29=29、比例0/1、并列索引与数学上相等的0.1+0.2/0.3行范数；量化码和mask都是整数。
- 对称量化：±0.5/±1.5/±2.5半格、全零scale=1、0.15/(0.3/127)=63.5精确ties-to-even、码范围与半格误差界。
- 仿射量化：奇数zero_point证明先round再加zp的区别，6个正负小数半格与两端截断；只对未截断项验证半格误差界。
- 存储误差：独立MSE与最大误差公式，FP32=4n与INT8=n仅计数据部分。
- 分片：n=0..8、workers=1..6共54种组合，核验恰好覆盖一次、连续边界、前部余数、长度差≤1及空片。
- 聚合：等样本简单均值与不等样本加权结果明确不同；零样本忽略；用6个显式样本梯度先分不同大小microbatch，聚合和参数更新与同一旧参数的大batch均值独立比较；空worker和0样本批不改变结果。

精确边界用原字符串构造Fraction，不把float转换回Fraction。P068采用浮点单轮同步更新；修复轮1后P069采用Fraction全程精确同步迭代及精确L1<=tol，仅输出转float。复杂度注明Prim懒删除堆可占O(m)、输入split持有全部tokens、P069有理数位数随轮数增长及其成本。

## 材料审计

22题当前112案例；案例名字每题唯一；首次44份答案/练习Python经ast.parse语法检查；22份练习均含NotImplementedError且不含solutions导入；本包全部题面、题解与章教程的本地Markdown链接首次审计不存在失效目标（0处）。题面模板仅图题提顶点编号，P073提行索引，量化/分布式题无无关图术语。生成器与当前题面规则保持同步。

一手资料与task-5.md约定一致：[Kruskal实现](https://github.com/TheAlgorithms/Python/blob/master/graphs/minimum_spanning_tree_kruskal.py)、[NetworkX PageRank源码](https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html)、[PyTorch剪枝教程](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html)、[PyTorch DDP教程](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)，并链接官方MST与量化文档。资料用于核对定义与思想，题目和代码独立编写；不称原创练习为真题，不宣称剪枝置零自动压缩文件或获得实测加速。

## 修复轮1附录（9ec25a2审查）

P2已修：P069的合法输入 `2 1 0.02 0.010 1\n0 1\n` 首轮为(0.495,0.505)，精确L1为0.010。先加入独立Fraction回归，观察实际输出第一行1 0与期望1 1不符的RED；修复后全程Fraction计算，精确比较L1<=tol，不添加epsilon、不把float转回Fraction。新增该等阈值案例与tol=0.009999不收敛反例，P069从5增至7案例。题面、三级提示、练习Fraction导入、题解、章教程与生成器均同步。

精确算术适用规模已明确为n≤20、m≤100、max_iter≤200，经主代理确认后实施。探索性强制迭代（不提前按tol停止）实测：原n=200/m=2000在139轮已耗4.0438秒，分母4074bit，不适合保留10000轮教学上限；n=20/m=100执行200轮0.4308秒，分母4955bit。均为本机探索，不作为性能保证或加速结论。题解明确有理数操作次数O(K(n+m))、B位整数运算成本C(B)、概率整数位存储O(nB)，并给出分母增长上界；不掩盖精确算术与真实大图浮点实现的差别。

P3已修：P060题解与生成器复杂度均改为总辅助空间O(n+m)，其中raw.split持有O(m)输入tokens、计数数组本身O(n)；代码无需改动。

实际验证：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_system_algorithms.py -k exact_decimal_stop_boundary
# 修复前：Ran 1 test in 0.001s; FAILED (failures=1)
# 修复后：Ran 1 test in 0.002s; OK
.\.venv\Scripts\python.exe check.py P069 --solution
# 通过 7/7 个案例，共 1 题
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_system_algorithms.py
# Ran 15 tests in 0.151s; OK
.\.venv\Scripts\python.exe check.py --chapter 07 --solution
# 通过 62/62 个案例，共 12 题
```

精简实际日志：[task-5-repair-1.log](task-5-repair-1.log)。修复相关3份Python经AST语法检查；P060/P069再生成后逐文件字节不变，确认生成器、7案例、精确约束与Fraction脚手架一致。本轮仅修P060说明、P069算法与材料、07教程、对应测试/生成器/本包工作文档；未修改其他题实现或共享文件，未执行Git操作。等待主代理范围复核。
