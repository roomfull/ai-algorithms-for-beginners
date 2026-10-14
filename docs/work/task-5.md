# Task 5：图分析、压缩、分布式（22 题）

先读 docs/implementation-plan.md；只拥有 chapters/07_graphs、chapters/08_compression、chapters/09_distributed、solutions/P059–P080.{py,md}、tests/test_system_algorithms.py。

P059 无向图邻接表；P060 有向图入出度；P061 BFS 最短层次；P062 DFS/连通分量；P063 并查集连接查询；P064 无向简单图三角形计数（每三点一次）；P065 所有连通分量二分图；P066 Kruskal MST（不连通输出 DISCONNECTED）；P067 Prim MST（相同约定）；P068 PageRank 单轮（给定初始概率和 alpha，无出边均匀分配）；P069 PageRank 收敛（均匀初值，L1阈值/max_iter/未收敛输出明确）；P070 图综合验收：连通分量、二分图、三角形统计。
P071 绝对值阈值剪枝（小于阈值置0，等于保留）；P072 按 floor(n*ratio) 最小绝对值剪枝，并列按索引；P073 行 L1 范数结构化剪枝（明确返回保留行/掩码格式，行范数并列按索引）；P074 对称 int8 量化（[-127,127]，scale=maxabs/127，全零 scale=1，round ties-to-even）；P075 给定 scale>0、zero_point 与 [0,255] 仿射量化/反量化（先 round(x/scale)+zp 再截断，ties-to-even）；P076 量化误差 MSE/maxabs 与理论存储字节（FP32=4n，INT8=n，标明未计元数据；不得剪枝置零就宣称压缩文件或实际加速）。
P077 连续均衡数据分片（余数给前面的 worker，允许空片）；P078 各 worker 梯度简单平均（题面保证等样本数）；P079 不同样本数的加权梯度聚合（权重0可忽略，总数>0）；P080 microbatch 梯度累积、跨worker同步 SGD（样本加权、更新一次、明确每输入梯度已是局部平均，不重复除以worker数）。

章节需解释图的点边、方向、邻居、队列、栈、BFS/DFS区别、并查集/贪心、PageRank概率流；压缩先解释权重/位数/scale，展示量化与误差手算；分布式解释 worker 只是模拟分片、全局batch、平均和加权差别。每题统一5件材料、5+手算独立case、三级提示和实际复杂度。模型压缩/分布式使用纯Python或NumPy，没GPU也可运行。

先测试后实现；独立测试：小图枚举三角形与MST、两个MST算法相互交叉及负权/孤立点、PageRank和=1/均匀环、剪枝确定数量与并列、量化半格误差界/截断、样本不等聚合与整体大batch等价。比较器若混合文本数字按 text，样例固定输出精度并明确；避免浮点测试混合文本无法容差。

参考 https://github.com/TheAlgorithms/Python/blob/master/graphs/minimum_spanning_tree_kruskal.py 、https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html 、https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html 、https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html 。注明教学模拟不等于运行PyTorch DDP，不宣称实测加速。

不修改共享文件，不 Git commit；生成器仅 tools/build_system_algorithms.py。报告 docs/work/task-5-report.md。
