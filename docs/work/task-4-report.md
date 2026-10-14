# Task 4 交付报告

## 完成范围

已完成第05章 `chapters/05_machine_learning` 的P039–P050与第06章 `chapters/06_neural_networks` 的P051–P058，共20题、102个独立案例。每题有完整题面与边界、首例输入/输出与手算、三级提示、读取输入的未完成练习脚手架、独立可运行参考代码、题解与实际实现复杂度。

两章教学入口解释样本/特征/标签、分类/聚类、训练/预测、概率和log、梯度/学习率、矩阵形状、链式规则、CNN前向与标量GAN。全部算法只用Python标准库，`requires=[]`；无需GPU、Redis、sklearn、torch或外部数据集。练习保持NotImplementedError，不导入参考答案；参考答案互不依赖。

没有修改共享文件，没有Git提交；辅助生成器仅为 `tools/build_ml_neural.py`。定义核对使用GitHub numpy-ml、scikit-learn决策树文档、PyTorch卷积/转置卷积文档与GAN原论文，逐题已有一手链接；代码独立编写。

## 测试先行证据

测试和案例先于对应参考实现保存，并实际观察失败；按批次保存日志，避免未落盘大块工作。

| 批次 | RED结果 | 随后GREEN |
|---|---|---|
| P039–P044 | 32个缺实现断言失败（30案例+KNN/K-means测试） | 3项unittest通过 |
| P045–P047 | 16个缺实现断言失败（15案例+有限差分） | 4项unittest通过 |
| P048–P050 | 23个失败：18个缺实现断言、P045输出接口调整5个形状失败 | 6项unittest通过 |
| P051–P054 | 22个缺实现断言失败（20案例+2性质测试） | 8项unittest通过 |
| P055–P058 | 24个缺实现断言失败（21案例+完整性/卷积/GAN） | 11项unittest通过 |

RED日志为 `task-4-red-39-44.txt`、`task-4-red-45-47.txt`、`task-4-red-48-50.txt`、`task-4-red-51-54.txt`、`task-4-red-55-58.txt`；每批对应 `task-4-green-*.txt`。第一批日志在未加UTF-8开关时捕获，中文显示有编码损坏，但失败题号/数量可核对；后续使用 `-X utf8`。没有重写RED日志冒充当时输出。

最终验证：

```powershell
.\.venv\Scripts\python.exe -X utf8 -m unittest tests.test_ml_neural -v
.\.venv\Scripts\python.exe -X utf8 check.py --chapter 05 --solution
.\.venv\Scripts\python.exe -X utf8 check.py --chapter 06 --solution
```

实际结果：11项unittest全部通过；第05章61/61案例（12题）；第06章41/41案例（8题）。日志为 [最终unittest](task-4-final-unittest.txt)、[第05章checker](task-4-checker-05.txt)、[第06章checker](task-4-checker-06.txt)。另用内置compile验证20份练习和20份答案均无语法错误，检查全部20题和102案例存在，练习均保持未完成且未导入答案。

独立验证覆盖：KNN距离平局与投票平局分别检验；K-means1–5轮SSE不增（1e-10数值容差）及空簇；逻辑梯度与单层网络更新的中心有限差分；四点二分类全部16种标签的精确Fraction最佳切分枚举；CART深度2案例、深度限制、XOR无增益、常量特征停止；softmax平移不变与逐行概率和；非对称卷积核；显式9×20线性矩阵A同时核对互相关Ax与转置卷积Aᵀu，并核对内积恒等式；GAN分别对D和使用新D的G求有限差分，验证两种初值的完整交替更新。

案例预期来自手算、独立数学公式与性质，生成器不读取或执行solutions来生成预期。P050和P058各6例，其余18题各5例。最终核对时，把P044的一轮上限案例换成点0、2、3、10，中心0、2；旧标签0、1、1、1，更新中心0、5后最终标签0、0、1、1，确保确实覆盖标签重新分配。

## 确定性与真实约束

- KNN输入整数坐标，平方和精确；距离按原始下标平局，票数按最小整数标签平局。
- K-means浮点输入最多6位小数、绝对值≤100；相对于真正最小平方距离取≤min+1e-12的第一个中心，空簇保留旧值；max_iter与tol明确，最终再分配。容差下不能宣称无任何浮点误差的绝对SSE单调或全局最优。
- CART中点由相邻不同值生成，按≤阈值分左支；评分全局最小值+1e-12内按特征/阈值序决胜；根深度0，无候选或增益≤1e-12停止，叶多数平票取最小标签。实现多层递归，不是单层桩。
- P046/P047/P054使用稳定logit BCE与真实未clip梯度；P053明确输入eps且clip至[eps,1-eps]，多类不重新归一化。
- 卷积为不翻核的单通道互相关；CNN明确卷积和池化的独立stride。转置卷积dilation=1、output_padding=0、无偏置，散射越界丢弃，不宣称逆运算。
- GAN仅标量一轮模拟，D损失两项求和，G采用非饱和目标，D→G交替且G使用新D；不是完整图像GAN训练。

## 待工具接口统一事项

为满足严格整数行要求，P044/P045/P049的每个case新增 `line_modes`：P044中心行float、最终标签行int；P045每样本概率float与标签int分别两行；P049特征索引int单独一行、阈值/Gini为float行。独立unittest以十进制整数正则严格验证这些行。当前checker仍按整题mode比较，暂忽略该可选元数据，因此本包checker通过尚不代表其已会拒绝混合题的小数标签。按主线程安排，本包没有改check.py；工具包补充line_modes校验与比较后需要再跑统一验收。
