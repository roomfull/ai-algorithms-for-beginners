# Task 6：模拟卷与完整学习交付

先读 docs/implementation-plan.md；此时课程 P001–P080 已存在。拥有 exams/、solutions/M01A–M04B.{py,md}、README.md、PROGRESS.md、docs/MISTAKES.md、docs/REFERENCES.md、docs/MAINTAINING.md、tests/test_course_integrity.py、tests/test_mock_algorithms.py。可更新 docs/START_HERE.md 的实际命令/路径，不改基础检查器。

四卷8题：M01A 训练集逐列 Z-score 后 KNN 查询，统计量仅训练集；M01B 网络布线 MST（新故事/数据）；M02A 给定语料的 TF-IDF 文本余弦相似度排名；M02B 带悬挂节点的网页 PageRank 排序；M03A 给定初值 K-means 后报告聚类误差与查询分配；M03B 按行权重对称量化及反量化误差；M04A 卷积+ReLU+平均池化特征；M04B 不同worker、不同microbatch大小的加权梯度更新。都是一道公共基础配一道系统优化，新的组合题不能只复制普通题。

每题同样完整材料与>=5独立案例、显式边界规则。模拟题 exercise 仅最小 solve/main 脚手架，自行输入输出。卷README讲清建议使用计时器但不杜撰正式考试时长/评分。提供按卷检查命令 --chapter M01 等。

根README为真正零基础导航：快速开始(无需激活的命令)、从 docs/START_HERE.md 到 P001 的链接、九章目录/题数/先修、答题流程、遇到失败怎么看、题解入口单独收起、每章掌握标准、模拟卷入口、考试环境默认假设。PROGRESS 88项链接和手动复习状态，MISTAKES 有一份具体填好的例子和可复制模板。

REFERENCES 逐专题权威来源、采用的约定和区别；MAINTAINING 描述格式/新增题目/运行全解与单元测试/NumPy版本/全库统计，最终验证数要真实。

完整性测试：准确88个ID/分章计数；全部 required files、题面有输入输出/提示/样例/复杂度题解与来源；>=440案例且题内name唯一；首样例与文档实际相符（可机器提取 fenced blocks）；无练习导入solutions；所有练习仍未完成；每章教程和链接存在。不要只断言字符串存在替代内容审查。模拟题关键期望值要独立推导，有手算/性质测试。

用现有 checker 全部答案验证，用 unittest discover 全套验证。完整走第一题：临时复制试错版得到错误、读题面提示、正确版通过，不改正式练习；记录命令与结果。修复本包问题，别改其他工作包而不向主代理报告。

不 Git commit；生成器仅 tools/build_mock_exams.py。报告 docs/work/task-6-report.md。

## 集成补充（此前工作包已验证的接口）

- 混合输出可给每个case设置 `line_modes`，逐行指定int/float/text；整数标签不能靠全局float容差判定。
- 前五包已完成80题与411个案例（111+82+108+110）；测试方法数合计79（检查器38、基础4、预处理9、ML14、系统14）。最终数字需按磁盘实际统计。
- 十进制边界要明确且可复现：训练集常量列显式判定；分类平票/聚类距离/排名平票说明精确或容差规则；量化半格与floor比例可从原字符串构造Fraction。不要从float反构造Fraction。
- P069审查发现float在数学L1恰等于tol时会误判标记。修复采用Fraction精确迭代并将本教学题约束为n≤20、m≤100、max_iter≤200。M02B若输出精确轮数/排序平票，也须考虑此边界，可用相同小规模精确计算；不要无说明添加epsilon改变题面规则。
- P001完整试错演练已记录于 docs/work/beginner-walkthrough.md，正式练习没有改变。读该证据；除非入口/题目改变了流程，不必重复同一测试。
- docs/START_HERE.md 仍含基础阶段“题目后续生成”的临时文字，本包须替换成真实可点击入口；根README同样更新。
- 每完成一卷或一组文档立即落盘并更新 docs/work/task-6-checkpoint.md，防止应用闪退丢失进度。
