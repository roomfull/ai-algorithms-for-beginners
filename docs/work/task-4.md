# Task 4：机器学习与神经网络（20 题）

先读 docs/implementation-plan.md；只拥有 chapters/05_machine_learning、chapters/06_neural_networks、solutions/P039–P058.{py,md}、tests/test_ml_neural.py。

具体题序：P039 KNN 近邻排序（欧氏距离平方，平局按索引）；P040 单样本多数投票（票数平局取最小整数标签）；P041 多查询 KNN 分类；P042 K-means 分配（并列取最小中心索引）；P043 更新中心（空簇保留旧中心）；P044 给定初始中心的完整 Lloyd 迭代（明确 max_iter、收敛规则与最终标签配合最终中心）；P045 逻辑回归 sigmoid 预测；P046 二分类交叉熵与一轮梯度；P047 完整二分类逻辑回归梯度下降；P048 熵与 Gini；P049 连续特征决策树最佳二叉切分（Gini，阈值取相邻不同值中点，平局特征序/阈值序）；P050 小型 CART 分类树训练和预测（明确 max_depth、纯叶/无增益/多数平票终止，完整算法非只一层桩）。
P051 全连接加 ReLU；P052 稳定 softmax；P053 BCE 与交叉熵计算（明确 clipping eps）；P054 单层网络梯度更新；P055 二维卷积（实际为深度学习互相关，不翻转核，明确 stride/padding）；P056 卷积-ReLU-最大池化的 CNN 前向链；P057 二维转置卷积（散射累加，不宣称卷积逆运算）；P058 标量生成器与判别器 GAN 损失及一次交替更新（先 D，后用更新后 D 算 G，明确标准/非饱和损失及公式）。

章节讲解零基础所需概念：样本/特征/标签、训练/预测、分类/聚类、概率/log、梯度作为变化方向、学习率。先手算再代码。神经网络先解释矩阵形状、损失和链式规则，不把 GAN 全训练作为要求。每题符合统一5件材料、5+独立案例、手算样例、3级提示；题解复杂度要对应实际实现。

独立测试：KNN平票；K-means SSE 不增与空簇；逻辑梯度 finite difference；决策树需有深度>1案例与无分裂终止；卷积非对称核验证不翻转；转置卷积用线性算子内积恒等式交叉检验；GAN一轮手算/数值梯度验证且 G 使用新 D。先测试后实现，使用 checker 本包验证。

一手来源：numpy-ml https://github.com/ddbourgin/numpy-ml （只参考，独立写代码）；https://scikit-learn.org/stable/modules/tree.html ；https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html ；https://docs.pytorch.org/docs/stable/generated/torch.nn.ConvTranspose2d.html ；GAN 原论文 https://arxiv.org/abs/1406.2661 。不依赖 sklearn/torch。

不修改共享文件，不 Git commit；需要生成器仅 tools/build_ml_neural.py。报告 docs/work/task-4-report.md。
