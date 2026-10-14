# Task 3：预处理与特征工程（16 题）

先读 docs/implementation-plan.md；只拥有 chapters/03_preprocessing、chapters/04_features、solutions/P023–P038.{py,md}、tests/test_preprocessing_features.py。

顺序：P023 均值填补缺失值（输入用 NA，整列缺失明确回退 0）；P024 稳定去重（保留首次）；P025 Min-Max 常量列输出 0；P026 Z-score 总体标准差，常量列输出 0；P027 给定顺序的训练/验证集划分，训练集统计量用于验证集；P028 按指定目标数确定性类别过采样（循环选原样本）；P029 显式给邻居和 lambda 的 SMOTE 插值；P030 完整小型 SMOTE（少数类内 KNN，不包含自身，距离并列按输入索引，明确生成顺序/邻居选择/lambda 输入；少数类过少按题面合法约束，测试合法最小值）。
P031 TF；P032 IDF；P033 TF-IDF（默认原始词频 tf，ln((1+n)/(1+df))+1，按词典序词表，按题目明确是否 L2，P033 要包含 L2 与零向量处理）；P034 等宽分箱；P035 等频分箱（明确重复值边界与确定性规则，不伪称分组一定等频）；P036 二分类列联表卡方统计量，期望为0项贡献0；P037 按相邻最小卡方合并至指定箱数（并列最左）；P038 MAD=median(abs(x-median(x))) 鲁棒特征，非均值绝对偏差（不需假设阈值公式）。

章节教程要补足均值、中位数、标准差、训练泄漏、类别不平衡、词频/文档频率差异、卡方是哪些数的计算。SMOTE 要从插值线段到近邻查找，分箱要演示完整相邻合并一轮。题面具体输入范围/规则/输出精度，样例手算，三级不同提示，复杂度对应实现；5+ 独立案例每题。普通文本行输入，避免把 JSON 作为学生必会。

先写案例再实现。独立验证性质：标准化均值/方差与常量列；SMOTE 不用多数类、插值端点；TF-IDF 手算和平滑；卡方独立表=0；MAD 对平移不变。交叉验证期望不是由参考答案自身产生。来源标注官方文档 https://scikit-learn.org/stable/modules/feature_extraction.html#tf-idf-term-weighting 、https://imbalanced-learn.org/stable/over_sampling.html#sample-generation 、https://scikit-learn.org/stable/modules/preprocessing.html 。卡方合并是明确定义的教学变体，不能宣称某库唯一默认算法。

使用现有 checker 验证本包，不修改共享文件，不 Git commit。若需要生成器只能 tools/build_preprocessing_features.py。报告 docs/work/task-3-report.md。
