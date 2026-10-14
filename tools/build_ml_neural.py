"""Task 4 材料生成器；案例用手算/独立数学公式，不能读取参考代码生成预期。"""
from pathlib import Path
import json
import math
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[1]
TOPICS = {}
ML = 'https://github.com/ddbourgin/numpy-ml'
TREE = 'https://scikit-learn.org/stable/modules/tree.html'
CONV = 'https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html'
TRANSPOSE = 'https://docs.pytorch.org/docs/stable/generated/torch.nn.ConvTranspose2d.html'
GAN = 'https://arxiv.org/abs/1406.2661'


def add(pid, title, task, inputs, outputs, hand, hints, complexity, pitfalls, cases,
        source=ML, mode='float', scaffold=''):
    TOPICS[pid] = dict(title=title, task=task, inputs=inputs, outputs=outputs,
                       hand=hand, hints=hints, complexity=complexity, pitfalls=pitfalls,
                       cases=cases, source=source, mode=mode, scaffold=scaffold)


def case(name, raw, expected):
    return dict(name=name, input=raw.strip()+'\n', expected=expected.strip()+'\n')


def row(values):
    return ' '.join(format(v, '.12g') for v in values)


add(39, 'KNN 近邻排序',
    '每一行是一个样本，每一列是一个特征。对查询向量计算欧氏距离的平方 Σ(x_j-q_j)²；不必开根号，因为非负数开根号不改变大小顺序。按(距离平方, 原始下标)升序取前k个。下标从0开始。',
    '第一行 n d k；接着n行，每行d个整数特征；最后一行d个整数查询特征。1≤k≤n≤100，1≤d≤10，特征绝对值≤10000。',
    '一行k个整数近邻下标，按距离从小到大排列。',
    '查询(0,0)到三点(1,0)、(-1,0)、(0,2)的距离平方是1、1、4。前两点平局按下标0、1；k=2，输出0 1。',
    ['先逐维作差并平方。', '给每个距离配上原始下标。', '排序键是(distance,index)，取排序列表[:k]，输出其中的index。'],
    '时间 O(nd+n log n)，空间 O(n+d)。',
    '不要先排序输入点后丢掉原下标；不要用曼哈顿距离；题目限定整数，Python整数平方和精确。',
    [case('等距离按下标', '3 2 2\n1 0\n-1 0\n0 2\n0 0', '0 1'),
     case('单点', '1 1 1\n7\n2', '0'),
     case('重复点', '3 1 3\n2\n2\n0\n2', '0 1 2'),
     case('负坐标', '3 1 2\n-4\n-1\n3\n-2', '1 0'),
     case('多维距离', '3 3 1\n1 2 3\n0 0 0\n1 1 1\n1 1 2', '2')], mode='int',
    scaffold='n, d, k = map(int, lines[0].split())\npoints = [list(map(int, line.split())) for line in lines[1:1+n]]\nquery = list(map(int, lines[1+n].split()))')

add(40, '单样本 KNN 多数投票',
    '分类是根据带标签的训练样本预测类别。先按P039规则选择k个邻居，再统计整数标签的票数。票数相等时取数值最小的标签，不按最近邻标签决胜。',
    '第一行 n d k；接着n行，每行先整数标签，再d个整数特征；最后d个查询特征。1≤k≤n≤100，1≤d≤10，特征绝对值≤10000，标签为[-100,100]整数。',
    '一行一个整数预测标签。',
    '到0的三个点是1、-1、3，距离平方1、1、9，标签分别9、2、9。k=2选下标0和1，各一票，较小标签2胜出。',
    ['选择邻居与投票是两个步骤。', '字典counts[label]保存票数。', '在出现的标签中最小化(-counts[label],label)。'],
    '时间 O(nd+n log n+k)，空间 O(n+d+k)。',
    '标签无需连续；距离平局按样本下标，票数平局按标签，两种平局不能混淆。',
    [case('票数平局取小标签', '3 1 2\n9 1\n2 -1\n9 3\n0', '2'),
     case('多数获胜', '3 1 3\n9 1\n2 -1\n9 3\n0', '9'),
     case('负标签', '2 1 2\n-3 2\n1 4\n3', '-3'),
     case('只取最近', '3 1 1\n3 5\n8 2\n1 8\n0', '8'),
     case('距离平局先下标', '2 1 1\n8 1\n2 -1\n0', '8')], mode='int')

add(41, '多查询 KNN 分类',
    '对q个查询分别做近邻排序与多数投票，训练数据保持不变；查询没有已知标签，也不能加入训练集。距离平局按下标，投票平局取最小整数标签。',
    '第一行 n d k q；随后n行标签+d个整数特征；再q行d个整数查询特征。1≤k≤n≤100，1≤d≤10，1≤q≤30，坐标绝对值≤10000，标签[-100,100]整数。',
    'q行，每行一个整数预测标签，顺序与查询一致。',
    '训练点0标签2，点10标签5；k=1。查询1最近0得2，查询9最近10得5，查询5等距离，先下标0得2。',
    ['对每个查询重复P040。', '每次查询新建票数字典。', '外层遍历queries；内部计算距离排序、取k个、计票，再追加预测。'],
    '时间 O(q(nd+n log n+k))，空间 O(nd+qd+n+k)。',
    '勿把前一个查询的票数留到下一个查询；不需要重新拟合训练数据。',
    [case('三个查询含距离平局', '2 1 1 3\n2 0\n5 10\n1\n9\n5', '2\n5\n2'),
     case('所有点投票', '2 1 2 2\n9 0\n2 10\n0\n10', '2\n2'),
     case('单训练点', '1 2 1 2\n-1 0 0\n3 4\n-3 -4', '-1\n-1'),
     case('重复坐标先下标', '2 1 1 2\n3 7\n1 7\n7\n8', '3\n3'),
     case('多维', '3 2 1 2\n0 0 0\n1 10 0\n2 0 10\n9 1\n1 9', '1\n2')], mode='int')

add(42, 'K-means 分配样本',
    '聚类没有已知类别标签；这里只给定c个中心，把每个点分配给距离平方最小的中心。先求最小距离m，再从小索引到大选第一个distance≤m+1e-12的中心。这个绝对容差明确处理浮点并列。',
    '第一行 n d c；随后n行d个实数样本，再c行d个实数中心。1≤n≤100，1≤d≤10，1≤c≤10；有限实数绝对值≤100，输入最多6位小数。',
    '一行n个整数中心编号，从0开始。',
    '点0、2、5；中心0、4。距离平方依次(0,16)、(4,4)、(25,1)，点2平局取中心0，得到0 0 1。',
    ['每个点分别到所有中心算距离。', '先拿到最小距离，不能在逐个扫描时累积容差误差。', 'min_dist=min(distances)，用next找第一个dist≤min_dist+1e-12的索引。'],
    '时间 O(ncd)，空间 O(nd+cd+c)。',
    '距离平方并列用题面容差；不要计算质心，这是下一题。',
    [case('中点平局', '3 1 2\n0\n2\n5\n0\n4', '0 0 1'),
     case('十进制等距离', '1 1 2\n0.3\n0.4\n0.2', '0'),
     case('同中心', '2 1 2\n1\n9\n3\n3', '0 0'),
     case('一个中心', '2 2 1\n-1 2\n8 -3\n0 0', '0 0'),
     case('二维分配', '3 2 2\n0 1\n9 1\n5 0\n0 0\n10 0', '0 1 0')], mode='int')

add(43, 'K-means 更新中心与空簇',
    '给定分配标签，非空簇中心改成该簇各维的算术平均；空簇保留旧中心，不产生NaN。这里不重新分配样本。',
    '第一行 n d c；随后n行d个实数样本、c行d个旧中心；最后一行n个整数分配标签[0,c-1]。1≤n≤100，1≤d≤10，1≤c≤10，有限实数绝对值≤100，最多6位小数。',
    'c行新中心，每行d个浮点数，按簇编号顺序。',
    '点0、2归簇0，点9归簇1，簇2为空。旧中心0、10、20；新中心(0+2)/2=1、9、20。',
    ['每簇保存计数与逐维总和。', '计数为0时拷贝旧中心。', '非空中心sum/count；遍历0到c-1，不能只遍历出现的标签。'],
    '时间 O(nd+cd)，空间 O(nd+cd+n)。',
    '空簇不能除0或被删掉；中心编号必须固定；平均按样本数除，不按维数除。',
    [case('空簇保留', '3 1 3\n0\n2\n9\n0\n10\n20\n0 0 1', '1\n9\n20'),
     case('二维平均', '2 2 1\n1 3\n3 7\n0 0\n0 0', '2 5'),
     case('常量小数', '3 1 1\n0.1\n0.1\n0.1\n8\n0 0 0', '0.1'),
     case('簇编号非顺序', '3 1 2\n3\n5\n9\n0\n0\n1 0 1', '5\n6'),
     case('单点另簇空', '1 1 2\n-2\n7\n8\n1', '7\n-2')])

add(44, '完整 Lloyd 迭代',
    '从给定中心开始，每轮先按P042规则分配，再按P043规则更新。若所有中心的坐标最大绝对变化≤tol，提前停止；否则至多执行max_iter轮。最终必须再按最终中心分配一次，输出标签配合这些中心；即使达到轮数上限也要重分配。',
    '第一行 n d c max_iter tol；随后n行样本、c行初始中心。n,d,c和数值范围同P042，1≤max_iter≤100，0≤tol≤1；tol有限实数。',
    '先c行最终中心，每行d个数；最后一行n个整数最终标签。',
    '点0、2、8、10，初始中心0、10。分配0 0 1 1；更新得1、9。再分配仍相同，更新无变化停止；最终中心1、9，标签0 0 1 1。',
    ['组合分配函数与更新函数。', '保留旧中心，计算更新前后的最大坐标变化。', '每轮assign→update→判停，循环后再assign最终中心；不要输出上一轮旧中心对应的标签。'],
    '时间 O(Tncd+Tnd+Tcd+ncd)，空间 O(nd+cd+n+c)，T≤max_iter。',
    '固定初始中心，不随机；空簇保留；轮数上限不保证收敛；最后重新分配保证标签一致。',
    [case('两簇收敛', '4 1 2 10 0\n0\n2\n8\n10\n0\n10', '1\n9\n0 0 1 1'),
     case('一轮后必须重分配', '4 1 2 1 0\n0\n2\n3\n10\n0\n2', '0\n5\n0 0 1 1'),
     case('空簇', '2 1 2 10 0\n0\n2\n0\n100', '1\n100\n0 0'),
     case('同初始中心', '2 1 2 10 0\n-1\n1\n0\n0', '0\n0\n0 0'),
     case('小数中点', '3 1 2 1 0\n0.2\n0.3\n0.4\n0.4\n0.2', '0.35\n0.2\n1 0 0')])


def probability(z):
    return 1/(1+math.exp(-z))


def sp(z):
    return max(z,0)+math.log1p(math.exp(-abs(z)))


add(45, '逻辑回归 sigmoid 预测',
    '权重w与偏置b已经给定；先算分数z=Σw_j x_j+b，再算p=1/(1+exp(-z))，表示类别1概率；p≥0.5预测1，否则0。此题只预测，不训练。为防exp溢出，z≥0用常见式，z<0用exp(z)/(1+exp(z))。',
    '第一行 n d；随后n行d个实数特征，一行d个权重，最后一行偏置。1≤n≤100，1≤d≤10；特征、权重、偏置均有限且绝对值≤10，最多6位小数。',
    '共2n行；每个样本先单独一行概率p，再单独一行整数预测标签，按样本顺序。',
    'w=1，b=0。x=0、1、-1给z=0、1、-1，p分别0.5、约0.73105857863、约0.26894142137。0.5也归标签1。',
    ['先算内积并加偏置。', 'sigmoid要分正负分支，尤其z=-1100。', 'z≥0返回1/(1+exp(-z))；否则e=exp(z)后返回e/(1+e)，用p≥0.5判断标签。'],
    '时间 O(nd)，空间 O(nd+d+n)，保存输出行。',
    '预测时不得改权重；偏置只加一次；负大分数的exp(-z)会溢出。',
    [case('零正负分数','3 1\n0\n1\n-1\n1\n0','0.5 1\n0.73105857863 1\n0.26894142137 0'),
     case('纯偏置','2 1\n5\n-5\n0\n-1',f'{probability(-1):.12g} 0\n{probability(-1):.12g} 0'),
     case('二维内积','1 2\n2 3\n1 -1\n1','0.5 1'),
     case('大负分数稳定','1 10\n'+row([-10]*10)+'\n'+row([10]*10)+'\n-10','0 0'),
     case('大正分数稳定','1 10\n'+row([10]*10)+'\n'+row([10]*10)+'\n10','1 1')])

add(46, '二分类交叉熵与一轮梯度',
    '损失衡量预测与标签差距。二分类交叉熵L=平均[-y ln p-(1-y)ln(1-p)]；ln为自然对数。为避免p舍入成0/1，直接用等价的logit公式：每样本softplus(z)-y z，其中softplus(z)=max(z,0)+ln(1+exp(-|z|))。梯度g_w=平均[(p-y)x]，g_b=平均[p-y]。只求当前损失和梯度，不更新。',
    '第一行 n d；随后n行，每行整数标签y(0/1)+d个实数特征；一行d个权重，最后一行偏置。尺寸及实数范围同P045。',
    '第一行平均损失L，第二行d个权重梯度，第三行偏置梯度。',
    '两条样本(y,x)=(0,0)、(1,2)，w=b=0，所以p均0.5，L=ln2。残差p-y为0.5、-0.5；g_w=(0.5×0-0.5×2)/2=-0.5；g_b=0。',
    ['对每行算z、p和残差p-y。', '所有样本的损失和梯度都要除n。', '用稳定softplus计算损失；g_w[j]=Σ(residual*x[j])/n，g_b=Σresidual/n。'],
    '时间 O(nd)，空间 O(nd+d)，不保存逐样本梯度。',
    '不要用log10；损失对标签求平均；梯度不是预测概率本身；稳定logit损失无需clip。',
    [case('手算零权重','2 1\n0 0\n1 2\n0\n0',f'{math.log(2):.12g}\n-0.5\n0'),
     case('单正例','1 1\n1 1\n0\n0',f'{math.log(2):.12g}\n-0.5\n-0.5'),
     case('非零logit','1 1\n0 2\n0.5\n0',f'{sp(1):.12g}\n{2*probability(1):.12g}\n{probability(1):.12g}'),
     case('二维梯度','1 2\n1 2 -4\n0 0\n0',f'{math.log(2):.12g}\n-1 2\n-0.5'),
     case('极端错误预测','1 1\n1 -10\n10\n-10','110\n10\n-1')])

b2=0.5+(1-probability(0.5))
add(47, '完整逻辑回归梯度下降',
    '从输入初值开始执行steps轮全批量梯度下降。每轮用所有样本在旧参数处计算P046的平均梯度，然后同时更新w←w-lr*g_w、b←b-lr*g_b。学习率lr控制每次沿降低损失方向走多远。执行固定轮数，无正则、无随机、无提前停止。最后输出更新后参数和重新计算的最终损失。',
    '第一行 n d steps lr；随后n行 标签(0/1)+d个特征；一行d个初始权重，一行初始偏置。1≤n≤100，1≤d≤10，0≤steps≤200，0<lr≤1；特征与初始参数有限且绝对值≤10，最多6位小数。',
    '第一行d个最终权重，第二行最终偏置，第三行最终平均损失（稳定logit形式）。',
    '沿P046两条样本，初始w=b=0、lr=1、steps=1：g_w=-0.5、g_b=0，更新w=0.5、b=0。最终z=0、1，损失(ln2+ln(1+exp(-1)))/2≈0.503204434。',
    ['每轮先积累整批梯度，再改参数。', '复用同一套稳定sigmoid与softplus公式。', '循环steps次，旧w、b产生整批residual；所有g除n；同时减lr*g。最后再前向算损失。'],
    '时间 O((steps+1)nd)，空间 O(nd+d)。',
    'steps=0也要输出初值处损失；不能逐样本更新替代全批量；最终损失不能用更新前的值。',
    [case('一轮完整更新','2 1 1 1\n0 0\n1 2\n0\n0',f'0.5\n0\n{(math.log(2)+sp(-1))/2:.12g}'),
     case('零轮','1 1 0 0.5\n1 2\n1\n0',f'1\n0\n{sp(-2):.12g}'),
     case('两轮偏置训练','1 1 2 1\n1 0\n3\n0',f'3\n{b2:.12g}\n{sp(-b2):.12g}'),
     case('平衡零梯度','2 1 20 1\n0 0\n1 0\n2\n0',f'2\n0\n{math.log(2):.12g}'),
     case('二维一轮','1 2 1 0.1\n1 2 -4\n0 0\n0',f'0.1 -0.2\n0.05\n{sp(-1.05):.12g}')])


add(48, '熵与 Gini 不纯度',
    '标签比例p_c=count_c/n。熵H=-Σp_c log2(p_c)，Gini=1-Σp_c²。熵这里用以2为底的对数，而交叉熵题用自然对数。纯标签集合两者都是0；越混杂通常数值越大，但两者数值不能直接混用。只遍历实际出现的标签，0 log0按0处理。',
    '一行n个整数标签，无单独n。1≤n≤200，标签[-100,100]。',
    '一行 熵H Gini。',
    '0 0 1 1中两类各一半。H=-2×(1/2)log2(1/2)=1；Gini=1-2×(1/2)²=0.5。',
    ['先计每类数量。', '用n把计数转为比例，math.log2求熵。', '只枚举counts.values()中的正计数，累加-p*log2(p)，再算1-Σp²。'],
    '时间 O(n+C)，空间 O(n+C)，C为出现的类别数。',
    'Gini不是分类错误率；熵的对数底数是2；一个样本也是纯集合。',
    [case('二类均衡','0 0 1 1','1 0.5'),
     case('纯类','7 7 7','0 0'),
     case('单样本','-3','0 0'),
     case('三类均衡','0 1 2',f'{math.log2(3):.12g} {2/3:.12g}'),
     case('不均衡','0 0 0 1',f'{-(.75*math.log2(.75)+.25*math.log2(.25)):.12g} 0.375')])

add(49, '连续特征的最佳二叉切分',
    '对每个特征，将不同值升序排列，相邻不同值的中点作为阈值t。左支x_j≤t，右支x_j>t；评分为(|L|Gini(L)+|R|Gini(R))/n。先找所有候选评分最小值m，再在评分≤m+1e-12的候选中按特征索引、阈值升序取第一项。此题返回最佳候选，即使增益为0；没有候选才输出哨兵。',
    '第一行 n d；接着n行，每行整数标签+d个实数特征。1≤n≤50，1≤d≤5，标签[-100,100]，有限特征绝对值≤100且最多6位小数。不同值比较不加容差，中点用(a+b)/2。',
    '第一行整数特征索引(从0开始)，第二行 阈值 加权Gini。所有特征恒定而无法分裂时输出-1，第二行0和父节点Gini。',
    '一维x=0、1、2、3，标签0、0、1、1。候选t=0.5、1.5、2.5；t=1.5得到两边纯标签，加权Gini=0，为最佳；特征编号0。',
    ['先用sorted(set(...))取得每个特征的不同值。', '每个中点都分别构造左右标签，计算加权Gini。', '存候选(score,feature,threshold)，找全局最小score；筛score≤min+1e-12，再按(feature,threshold)选第一项。'],
    '时间 O(dn²+dn log n)，空间 O(nd+dn)，本实现每个阈值重新遍历n个样本并保存候选。',
    '中点来自相邻不同值；阈值等于的点去左支；同分先特征再阈值；无候选与无增益不相同。',
    [case('纯分裂','4 1\n0 0\n0 1\n1 2\n1 3','0\n1.5 0'),
     case('特征并列','4 2\n0 0 0\n0 1 1\n1 2 2\n1 3 3','0\n1.5 0'),
     case('阈值并列','3 1\n0 0\n1 1\n0 2',f'0\n0.5 {1/3:.12g}'),
     case('无不同特征值','2 1\n0 7\n1 7','-1\n0 0.5'),
     case('十进制中点','2 1\n4 0.2\n8 0.3','0\n0.25 0')],source=TREE)

add(50, '小型 CART 分类树训练与预测',
    '在当前节点递归用P049规则挑最佳切分。根深度0；达到max_depth、标签纯、无候选、或Gini降低≤1e-12时，成为叶节点。叶节点预测当前训练标签的多数类，票数平局取最小整数标签。否则按≤阈值和>阈值分出两支并递归。查询从根逐层走到叶，不只训练一层。无剪枝、无随机特征。',
    '第一行 n d q max_depth；随后n行整数标签+d个实数特征，再q行d个查询特征。1≤n≤50，1≤d≤5，1≤q≤30，0≤max_depth≤8，标签[-100,100]，有限特征绝对值≤100，最多6位小数。候选评分并列容差、特征/阈值次序同P049。',
    'q行，每行一个整数预测标签。',
    '训练x=0..5、标签0 0 1 1 0 0。根最佳阈值1.5与3.5同分，取1.5；左支纯0，右支再以3.5分成纯1和纯0。max_depth=2时查询-1、2.5、5输出0、1、0。',
    ['写train(rows,depth)，返回叶标签或分裂节点。', '先判断停止条件，再选分裂，左右递归深度加1。', '最佳评分与父Gini差≤1e-12就返回多数叶；否则保存(feature,threshold,left,right)，predict按x[feature]≤threshold走左支。'],
    '训练时间 O(dn²(H+1)+dn(H+1)log n)的保守上界，H≤max_depth；预测 O(q(H+1))。额外空间 O(nd(H+1)+dn+q)的保守上界，包含递归暂存样本子集及候选。',
    'XOR在根处无增益时按本题规则停止，不能声称该贪心树必能拟合所有数据；根深度为0；无增益不要无限递归。',
    [case('深度二层','6 1 3 2\n0 0\n0 1\n1 2\n1 3\n0 4\n0 5\n-1\n2.5\n5','0\n1\n0'),
     case('零深度多数','3 1 2 0\n4 0\n2 1\n2 2\n0\n2','2\n2'),
     case('深度一层限制','6 1 3 1\n0 0\n0 1\n1 2\n1 3\n0 4\n0 5\n-1\n2.5\n5','0\n0\n0'),
     case('XOR无增益停止','4 2 2 8\n0 0 0\n1 0 1\n1 1 0\n0 1 1\n0 1\n1 0','0\n0'),
     case('纯标签','2 1 2 8\n7 -1\n7 3\n-10\n10','7\n7'),
     case('常量特征多数平局','2 1 1 8\n9 0.1\n-2 0.1\n0.1','-2')],source=TREE,mode='int')


add(51, '全连接层与 ReLU',
    '矩阵X形状n×d，n是样本数，d是输入维数；W形状d×o，o是输出神经元数；b有o项。先做Z=XW+b，每行都加同一b；再做ReLU(z)=max(0,z)。本题只有前向计算，负数变0，正数保留。',
    '第一行 n d o；随后n行X，每行d项；随后d行W，每行o项；最后一行o个偏置。1≤n,d,o≤20，全部有限实数绝对值≤10，最多6位小数。',
    'n行ReLU输出，每行o项。',
    'X两行(1,2)、(-1,3)，W两行(1,-1)、(2,0)，b=(0,1)。第一行Z=(1×1+2×2,1×(-1)+2×0+1)=(5,0)；第二行为(5,2)。ReLU后不变。',
    ['先检查n×d乘d×o会得到n×o。', '每个输出z[i][j]遍历输入维t累加X[i][t]*W[t][j]。', '三层循环算内积，加b[j]一次，再max(0,z)。无需实现矩阵库。'],
    '时间 O(ndo)，空间 O(nd+do+no+o)。',
    'W第一维对应输入特征；不要逐元素相乘替代矩阵乘法；偏置按输出列广播。',
    [case('二维全连接','2 2 2\n1 2\n-1 3\n1 -1\n2 0\n0 1','5 0\n5 2'),
     case('负值截零','1 1 2\n2\n-1 -3\n0 1','0 0'),
     case('偏置逐样本','2 1 2\n0\n2\n1 -2\n1 3','1 3\n3 0'),
     case('单位矩阵','1 3 3\n1 -2 3\n1 0 0\n0 1 0\n0 0 1\n0 0 0','1 0 3'),
     case('零输入','1 1 1\n0\n0\n0','0')])

add(52, '稳定 softmax',
    '把每行c个分数变成类别概率：p_j=exp(z_j-m)/Σexp(z_t-m)，m=max(z)。减同一个常数不改变概率，但避免直接exp(1000)溢出。每行各自归一化，概率和为1。',
    '第一行 n c；随后n行，每行c个logit分数。1≤n≤50，1≤c≤20；有限实数绝对值≤1000，最多6位小数。',
    'n行概率矩阵，每行c项。',
    '第一行z=(0,1)，减最大值得(-1,0)，exp值(e^-1,1)，概率约(0.26894142137,0.73105857863)。第二行(999,1000)减最大值后完全相同。',
    ['每行先取最大值。', '对减最大值后的分数取指数，再求指数总和。', '每行e=[exp(v-max(row))]，输出各e/sum(e)，不要把整矩阵一起归一化。'],
    '时间 O(nc)，空间 O(nc+c)。',
    '减最大值不是裁剪；sigmoid和softmax不同；softmax每行只有一个类别时输出1。',
    [case('平移不变','2 2\n0 1\n999 1000',f'{probability(-1):.12g} {probability(1):.12g}\n{probability(-1):.12g} {probability(1):.12g}'),
     case('均匀三类','1 3\n0 0 0',row([1/3]*3)),
     case('单类','2 1\n-1000\n1000','1\n1'),
     case('相差极大','1 2\n1000 -1000','1 0'),
     case('全负相同','1 3\n-5 -5 -5',row([1/3]*3))])

add(53, 'BCE 与多分类交叉熵',
    '输入的是概率。二分类先p←min(1-eps,max(eps,p))，算平均[-y ln p-(1-y)ln(1-p)]。多分类每行真实类别为t，只取它的概率p_t做同样clip，算平均[-ln p_t]；不重新归一化clip后的概率。本题clip上界也用于多分类，真实类概率1会产生很小正损失。',
    '第一行 n c eps；随后n行，每行二分类整数标签(0/1)与p；再n行，每行真实整数类别[0,c-1]与c个概率。1≤n≤50，1≤c≤10，1e-12≤eps≤0.01；概率有限且在[0,1]，多分类每行概率和与1误差≤1e-9。概率最多6位小数，eps可用科学记数法。',
    '一行 平均BCE 平均多分类交叉熵。',
    '二分类(1,0.8)、(0,0.6)：正确类别概率分别0.8、0.4，BCE=-(ln0.8+ln0.4)/2≈0.569717142。多分类真实类概率0.8、0.75，CE=-(ln0.8+ln0.75)/2≈0.255412812。eps=1e-6未触发clip。',
    ['先clip，再log，别对0取log。', '多分类只取真实类别索引对应概率。', '对n行二分类分别求-y*log(p)-(1-y)*log1p(-p)，平均；多分类累加-log(clip(probs[target]))后除n。'],
    '时间 O(nc)，空间 O(nc+n)，解析全部概率行。',
    '不能用argmax代替真实类概率；clip不重新归一化；eps改变边界损失，不能固定写死另一eps。',
    [case('两种损失','2 2 0.000001\n1 0.8\n0 0.6\n0 0.8 0.2\n1 0.25 0.75',row([-(math.log(.8)+math.log(.4))/2,-(math.log(.8)+math.log(.75))/2])),
     case('错误边界clip','1 2 0.01\n1 0\n1 1 0',row([-math.log(.01)]*2)),
     case('正确边界clip','1 2 0.01\n0 0\n0 1 0',row([-math.log(.99)]*2)),
     case('均匀概率','1 2 0.000001\n1 0.5\n1 0.5 0.5',row([math.log(2)]*2)),
     case('三类选择正确列','1 3 0.000001\n0 0.25\n2 0.2 0.3 0.5',row([-math.log(.75),math.log(2)]))])

add(54, '单层 sigmoid 网络梯度更新',
    '一个输出神经元z=w·x+b，激活p=sigmoid(z)，损失用未clip的稳定logit BCE。链式规则把损失对p的导数乘p对z的导数，得到∂L/∂z=p-y；再乘z对w_j的导数x_j得到权重梯度。用整批平均梯度执行一次w←w-lr*g_w、b←b-lr*g_b，所有参数同时更新。',
    '第一行 n d lr；随后n行，每行整数标签y(0/1)+d个实数特征；再一行d个初始权重、一行初始偏置。1≤n≤100，1≤d≤10，0<lr≤1，特征和初始参数有限且绝对值≤10，最多6位小数。',
    '第一行更新前的平均损失，第二行d个更新后权重，第三行更新后偏置。',
    '一条正样本x=(2,-4)，旧w=(0,0)、b=0，p=0.5，损失ln2。残差-0.5，权重梯度(-1,2)，偏置梯度-0.5；lr=0.1更新w=(0.1,-0.2)、b=0.05。',
    ['这个单层网络与逻辑回归数学相同。', '先用旧参数计算所有梯度，全部平均。', 'dw[j]=Σ((p-y)*x[j])/n，db=Σ(p-y)/n；返回旧损失和w-lr*dw、b-lr*db。'],
    '时间 O(nd)，空间 O(nd+d)。',
    '本题输出旧损失，与P047的最终损失不同；若用clip损失却配原BCE梯度，会破坏有限差分一致性。',
    [case('链式规则二维','1 2 0.1\n1 2 -4\n0 0\n0',f'{math.log(2):.12g}\n0.1 -0.2\n0.05'),
     case('单负样本','1 1 1\n0 2\n0\n0',f'{math.log(2):.12g}\n-1\n-0.5'),
     case('整批平均','2 1 1\n0 0\n1 2\n0\n0',f'{math.log(2):.12g}\n0.5\n0'),
     case('零梯度平衡','2 1 0.5\n0 0\n1 0\n3\n0',f'{math.log(2):.12g}\n3\n0'),
     case('非零初值','1 1 0.5\n1 1\n1\n0',f'{sp(-1):.12g}\n{1+.5*(1-probability(1)):.12g}\n{.5*(1-probability(1)):.12g}')])


add(55, '二维卷积：不翻转核的互相关',
    '本题采用深度学习常用的互相关：核不翻转。输入四周补p层0，核每次移动s格。输出位置(i,j)为ΣX_padded[i*s+a,j*s+b]K[a,b]。只有一个输入通道与一个核，无偏置，无dilation。输出高H=(h+2p-kh)//s+1，宽W=(w+2p-kw)//s+1。',
    '第一行 h w kh kw s p（全为整数）；接着h行输入，每行w项；接着kh行核，每行kw项。1≤h,w≤20，1≤kh,kw≤7，1≤s≤4，0≤p≤3，保证h+2p≥kh且w+2p≥kw；数据有限，绝对值≤10，最多6位小数。',
    'H行输出矩阵，每行W个数；不另写尺寸。',
    '输入1..9排成3×3，核[[1,2],[3,4]]。左上=1×1+2×2+4×3+5×4=37；右上=47，左下=67，右下=77。核翻转会给另一个答案，因此必须保留核方向。',
    ['先算输出尺寸并创建零填充输入。', '输出位置(i,j)对应填充输入起点(i*s,j*s)。', '四重循环i,j,a,b累加padded[i*s+a][j*s+b]*kernel[a][b]，不要把kernel倒序。'],
    '时间 O(HWkhkw+(h+2p)(w+2p))，空间 O((h+2p)(w+2p)+HW+khkw+hw)。',
    'stride影响起点，不影响核内部步长；padding必须四边都补0；整除舍弃不足一个窗口的尾部。',
    [case('非对称核','3 3 2 2 1 0\n1 2 3\n4 5 6\n7 8 9\n1 2\n3 4','37 47\n67 77'),
     case('单点padding','1 1 2 2 1 1\n3\n1 2\n3 4','12 9\n6 3'),
     case('stride二','3 3 2 2 2 0\n1 2 3\n4 5 6\n7 8 9\n1 2\n3 4','37'),
     case('矩形核差分','2 3 1 2 1 0\n1 2 3\n4 5 6\n1 -1','-1 -1\n-1 -1'),
     case('标量核','1 2 1 1 1 0\n1 -2\n2','2 -4')],source=CONV)

add(56, 'CNN 前向：卷积、ReLU、最大池化',
    '先按P055做互相关并加标量偏置b，逐元素做ReLU，然后最大池化。池化窗口ph×pw，移动ps格，只取窗口最大数，不乘权重，不padding。卷积尺寸H,W同P055；池化输出高(H-ph)//ps+1、宽(W-pw)//ps+1。只计算前向，不训练。',
    '第一行 h w kh kw s p ph pw ps（整数）；随后h行输入、kh行核，最后一行偏置b。卷积范围同P055，1≤ph,pw,ps≤4；保证H≥ph,W≥pw；b有限且绝对值≤10，其他数值范围同P055。',
    '只输出最终池化矩阵，不输出中间矩阵或尺寸。',
    '输入[[-1,2],[3,-4]]，1×1核为1，偏置0，卷积原样；ReLU得到[[0,2],[3,0]]；2×2池化取max(0,2,3,0)=3。',
    ['先做完整卷积矩阵，再做激活和池化。', 'ReLU在池化之前，偏置在ReLU之前。', 'pool[i][j]=max(relu[i*ps+a][j*ps+b])，a范围ph、b范围pw；卷积stride s与池化stride ps分别使用。'],
    '时间 O(HWkhkw+(h+2p)(w+2p)+HW+H_pW_p ph pw)，空间 O(hw+khkw+(h+2p)(w+2p)+HW+H_pW_p)。',
    '最大池化不是平均；卷积偏置不能在ReLU后加；池化尾部不足窗口则舍弃。',
    [case('含负数ReLU池化','2 2 1 1 1 0 2 2 2\n-1 2\n3 -4\n1\n0','3'),
     case('非对称核后池化','3 3 2 2 1 0 2 2 1\n1 2 3\n4 5 6\n7 8 9\n1 2\n3 4\n-10','67'),
     case('padding加偏置','1 1 1 1 1 1 2 2 1\n2\n1\n-1','1 1\n1 1'),
     case('矩形池化stride','2 4 1 1 1 0 2 2 2\n1 2 3 4\n5 6 7 8\n1\n0','6 8'),
     case('卷积stride与一格池化','3 3 1 1 2 0 1 1 1\n1 2 3\n4 5 6\n7 8 9\n1\n0','1 3\n7 9')],source=CONV)

add(57, '二维转置卷积：散射累加',
    '输出先全0；每个输入X[i,j]把X[i,j]K[a,b]加到输出(i*s-p+a,j*s-p+b)，越界项丢弃。重叠位置必须累加。输出高H=(h-1)s-2p+kh，宽W=(w-1)s-2p+kw；本题dilation=1、output_padding=0、无偏置。它是同核互相关线性算子的转置，在尺寸匹配时满足内积恒等式；一般不是卷积逆运算。',
    '第一行 h w kh kw s p（整数）；接着h行输入、kh行核。1≤h,w≤20，1≤kh,kw≤7，1≤s≤4，0≤p≤3；保证H,W≥1；输入与核有限且绝对值≤10，最多6位小数。',
    'H行输出，每行W个数，不另写尺寸。',
    '输入[[1,2],[3,4]]、核[[1,2],[3,4]]、s=1,p=0，输出3×3。中心收到1×4+2×3+3×2+4×1=20。四角分别1、4、9、16；其余累加得到[[1,4,4],[6,20,16],[9,24,16]]。',
    ['先按公式建输出，不能照抄普通卷积输出尺寸。', '遍历输入，把一个缩放的核散射到输出。', 'r=i*s-p+a，c=j*s-p+b；若0≤r<H且0≤c<W，out[r][c]+=x[i][j]*kernel[a][b]。'],
    '时间 O(hwkhkw+HW)，空间 O(hw+khkw+HW)。',
    '重叠要+=；padding对应散射的偏移和裁掉边缘；尺寸扩大不代表恢复了原始信息；不要翻核。',
    [case('重叠累加非对称核','2 2 2 2 1 0\n1 2\n3 4\n1 2\n3 4','1 4 4\n6 20 16\n9 24 16'),
     case('stride二无重叠','2 2 2 2 2 0\n1 2\n3 4\n1 2\n3 4','1 2 2 4\n3 4 6 8\n3 6 4 8\n9 12 12 16'),
     case('padding裁边','2 2 2 2 1 1\n1 2\n3 4\n1 2\n3 4','20'),
     case('矩形一维嵌入','1 2 1 2 1 0\n2 3\n1 -1','2 1 -3'),
     case('零输入','1 1 2 2 1 0\n0\n1 2\n3 4','0 0\n0 0')],source=TRANSPOSE)

dg=2*probability(1)-1
new_w=1-.1*dg
new_b=-.1*dg
new_u=new_w+new_b
gg=(probability(new_u)-1)*new_w
add(58, '标量 GAN 损失与交替更新',
    '生成器G(z)=a*z+g，判别器D(x)=sigmoid(w*x+b)。一条真实样本xr与一条噪声z。先固定G，用L_D=-ln D(xr)-ln(1-D(G(z)))=softplus(-u_r)+softplus(u_f)训练D（两项求和，不除2）。g_w=(p_r-1)*xr+p_f*G(z)，g_b=p_r-1+p_f；w,b同时减lrD乘梯度。然后固定新D，采用非饱和生成器损失L_G=-ln D_new(G(z))=softplus(-u_f_new)，g_a=(p_f_new-1)*w_new*z，g_g=(p_f_new-1)*w_new，再同时更新a,g。标准minimax生成器目标ln(1-D(G(z)))仅作概念比较，本题不采用它。',
    '一行 xr z a g w b lrD lrG 共8个有限实数；前6项绝对值≤2，0<lrD,lrG≤1，最多6位小数。所有概率用稳定sigmoid，损失用softplus(t)=max(t,0)+ln(1+exp(-|t|))；不clip。',
    '第一行 L_D（D更新前） L_G（D更新后、G更新前）；第二行 a_new g_new w_new b_new。只执行一轮D→G。',
    'xr=z=1，a=g=w=b=0，学习率均1。fake=0，p_r=p_f=0.5，L_D=2ln2。D梯度g_w=-0.5,g_b=0，新w=0.5,b=0。新D在fake0的概率仍0.5，L_G=ln2；G梯度g_a=g_g=-0.25，所以新a=g=0.25。用旧w=0会错误地让G不更新。',
    ['D步中fake当作固定输入，不能顺便更新G。', 'D同时更新后重新算fake的判别概率，再算G梯度。', '先保存old_fake=a*z+g；求D梯度并更新w,b；p_new=sigmoid(w_new*old_fake+b_new)，再算G梯度与更新。两个损失输出的计算时点不同。'],
    '时间 O(1)，空间 O(1)。',
    'D使用梯度下降的负对数损失；G用非饱和损失；不能用旧D更新G；G步不再次改变D；这是标量教学模拟，不是完整图像GAN训练。',
    [case('必须使用新判别器','1 1 0 0 0 0 1 1',f'{2*math.log(2):.12g} {math.log(2):.12g}\n0.25 0.25 0.5 0'),
     case('噪声二与不同学习率','1 2 0 0 0 0 1 0.5',f'{2*math.log(2):.12g} {math.log(2):.12g}\n0.25 0.125 0.5 0'),
     case('全零样本不动','0 0 0 0 0 0 1 1',f'{2*math.log(2):.12g} {math.log(2):.12g}\n0 0 0 0'),
     case('真假相同零判别器','1 1 1 0 0 0 1 1',f'{2*math.log(2):.12g} {math.log(2):.12g}\n1 0 0 0'),
     case('非零初值','1 1 1 0 1 0 0.1 0.1',f'{sp(-1)+sp(1):.12g} {sp(-new_u):.12g}\n{1-.1*gg:.12g} {-.1*gg:.12g} {new_w:.12g} {new_b:.12g}'),
     case('噪声零权重不动','1 0 0.7 0 0 0 1 1',f'{2*math.log(2):.12g} {math.log(2):.12g}\n0.7 0.25 0.5 0')],source=GAN)


def chapter(pid):
    return '05_machine_learning' if pid <= 50 else '06_neural_networks'


SCAFFOLDS = {
    40: 'n, d, k = map(int, lines[0].split())\nsamples = [list(map(int, line.split())) for line in lines[1:n+1]]\nquery = list(map(int, lines[n+1].split()))\n# samples[i][0]是标签，samples[i][1:]是特征。',
    41: 'n, d, k, q = map(int, lines[0].split())\nsamples = [list(map(int, line.split())) for line in lines[1:n+1]]\nqueries = [list(map(int, line.split())) for line in lines[n+1:n+1+q]]',
    42: 'n, d, c = map(int, lines[0].split())\npoints = [list(map(float, line.split())) for line in lines[1:n+1]]\ncenters = [list(map(float, line.split())) for line in lines[n+1:n+1+c]]',
    43: 'n, d, c = map(int, lines[0].split())\npoints = [list(map(float, line.split())) for line in lines[1:n+1]]\nold_centers = [list(map(float, line.split())) for line in lines[n+1:n+1+c]]\nlabels = list(map(int, lines[n+1+c].split()))',
    44: 'head = lines[0].split()\nn, d, c, max_iter = map(int, head[:4])\ntol = float(head[4])\npoints = [list(map(float, line.split())) for line in lines[1:n+1]]\ncenters = [list(map(float, line.split())) for line in lines[n+1:n+1+c]]\n# 建议写assign函数，循环后也调用它。',
    45: 'n, d = map(int, lines[0].split())\npoints = [list(map(float, line.split())) for line in lines[1:n+1]]\nweights = list(map(float, lines[n+1].split()))\nbias = float(lines[n+2])',
    46: 'n, d = map(int, lines[0].split())\nsamples = [list(map(float, line.split())) for line in lines[1:n+1]]\nweights = list(map(float, lines[n+1].split()))\nbias = float(lines[n+2])\n# sample[0]是0/1标签，sample[1:]是特征。',
    47: 'head = lines[0].split()\nn, d, steps = map(int, head[:3])\nlr = float(head[3])\nsamples = [list(map(float, line.split())) for line in lines[1:n+1]]\nweights = list(map(float, lines[n+1].split()))\nbias = float(lines[n+2])',
    48: 'labels = list(map(int, raw.split()))\n# 可以先用字典统计每类出现的次数。',
    49: 'n, d = map(int, lines[0].split())\nrows = []\nfor line in lines[1:n+1]:\n    tokens = line.split()\n    rows.append((int(tokens[0]), list(map(float, tokens[1:]))))\n# rows中的元素是(label, features)。',
    50: 'n, d, q, max_depth = map(int, lines[0].split())\nrows = []\nfor line in lines[1:n+1]:\n    tokens = line.split()\n    rows.append((int(tokens[0]), list(map(float, tokens[1:]))))\nqueries = [list(map(float, line.split())) for line in lines[n+1:n+1+q]]\n# 建议分别写gini、train、predict函数；根节点深度为0。',
    51: 'n, d, o = map(int, lines[0].split())\nx = [list(map(float, line.split())) for line in lines[1:n+1]]\nw = [list(map(float, line.split())) for line in lines[n+1:n+1+d]]\nb = list(map(float, lines[n+1+d].split()))\n# 输出的行数是n，列数是o。',
    52: 'n, c = map(int, lines[0].split())\nlogits = [list(map(float, line.split())) for line in lines[1:n+1]]\n# 每行独立求概率，先减本行最大值。',
    53: 'head = lines[0].split()\nn, c = map(int, head[:2])\neps = float(head[2])\nbinary_rows = [line.split() for line in lines[1:n+1]]\nmulticlass_rows = [line.split() for line in lines[n+1:2*n+1]]\n# 两种行格式不同，标签用int，概率用float。',
    54: 'head = lines[0].split()\nn, d = map(int, head[:2])\nlr = float(head[2])\nsamples = [list(map(float, line.split())) for line in lines[1:n+1]]\nweights = list(map(float, lines[n+1].split()))\nbias = float(lines[n+2])',
    55: 'h, w, kh, kw, stride, pad = map(int, lines[0].split())\nx = [list(map(float, line.split())) for line in lines[1:h+1]]\nkernel = [list(map(float, line.split())) for line in lines[h+1:h+1+kh]]\n# 输出高度/宽度由README公式计算。',
    56: 'h, w, kh, kw, stride, pad, ph, pw, ps = map(int, lines[0].split())\nx = [list(map(float, line.split())) for line in lines[1:h+1]]\nkernel = [list(map(float, line.split())) for line in lines[h+1:h+1+kh]]\nbias = float(lines[h+1+kh])\n# 先构造卷积-ReLU矩阵，再单独遍历池化窗口。',
    57: 'h, w, kh, kw, stride, pad = map(int, lines[0].split())\nx = [list(map(float, line.split())) for line in lines[1:h+1]]\nkernel = [list(map(float, line.split())) for line in lines[h+1:h+1+kh]]\n# 初始化输出为全0，散射累加，不能覆盖。',
    58: 'real, z, a, g, w, b, lr_d, lr_g = map(float, raw.split())\n# 先保存fake，再计算D梯度和新w,b，最后计算G梯度。',
}


def write_materials():
    for pid, t in TOPICS.items():
        ident = f'P{pid:03}'
        folder = ROOT / 'chapters' / chapter(pid) / 'problems' / ident
        folder.mkdir(parents=True, exist_ok=True)
        cases = [c.copy() for c in t['cases']]
        if pid == 44:
            for c in cases:
                c['line_modes']=['float']*(len(c['expected'].splitlines())-1)+['int']
        if pid == 45:
            for c in cases:
                c['expected']='\n'.join(token for line in c['expected'].splitlines() for token in line.split())+'\n'
                c['line_modes']=['float','int']*(len(c['expected'].splitlines())//2)
        if pid == 49:
            for c in cases:
                c['line_modes']=['int','float']
        data = dict(id=ident, chapter='05' if pid<=50 else '06', title=t['title'],
                    mode=t['mode'], requires=[], cases=cases)
        (folder/'cases.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        sample=cases[0]
        hints='\n\n'.join(f'<details><summary>提示 {i}</summary>\n\n{h}\n\n</details>' for i,h in enumerate(t['hints'],1))
        integer_input = '' if pid == 58 else ' 所有尺寸和标签均严格输入整数；'
        output_precision = ('输出使用十进制整数，不可带小数点。' if t['mode']=='int' else
                            '浮点允许绝对或相对误差1e-6。计算中保留精度，只在输出格式化。')
        if pid in (44,45,49):
            output_precision += ' 整数标签/索引单独一行，严格输出十进制整数。'
        readme=f'''# {ident} {t['title']}

{t['task']}

## 输入与约束

{t['inputs']}{integer_input}不要求处理无效输入。

## 输出

{t['outputs']} {output_precision}

## 样例

输入：
```text
{sample['input'].rstrip()}
```
输出：
```text
{sample['expected'].rstrip()}
```

手算：{t['hand']}

## 分级提示

{hints}

## 运行与检查

在仓库根目录运行（无需激活环境）：
```powershell
.\\.venv\\Scripts\\python.exe chapters/{chapter(pid)}/problems/{ident}/exercise.py
.\\.venv\\Scripts\\python.exe check.py {ident}
```

输入结束用Windows Ctrl+Z后回车；也可 `Get-Content input.txt | .\\.venv\\Scripts\\python.exe chapters/{chapter(pid)}/problems/{ident}/exercise.py`。标准输出只写结果，不写提示文字。

来源：[一手定义/实现参考]({t['source']})。本题为原创教学练习；数值和确定性约定以题面为准，参考代码独立编写，离线练习不用联网。

[章节入口](../../README.md) · [下一题](../P{pid+1:03}/README.md) · [题解](../../../../solutions/{ident}.md)
'''
        if pid in (50,58):
            readme=readme.replace(f'[下一题](../P{pid+1:03}/README.md)', '[后续学习路线](../../../../README.md)')
        (folder/'README.md').write_text(readme, encoding='utf-8')
        scaffold=t['scaffold'] or SCAFFOLDS[pid]
        exercise=f'''"""{ident}：练习脚手架，保持独立；不要导入solutions。"""
import sys
import math


def solve(raw):
    lines = raw.strip().splitlines()
{textwrap.indent(scaffold, '    ')}
    # TODO：完成计算并返回结果字符串（可用空格连接一行，换行连接多行）。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
'''
        (folder/'exercise.py').write_text(exercise, encoding='utf-8')
        solution_md=f'''# {ident} {t['title']}题解

思路：{t['task']}

关键步骤：{t['hints'][2]}

样例核对：{t['hand']}

复杂度（对应参考实现）：{t['complexity']}

易错点：{t['pitfalls']}

[独立参考代码]({ident}.py) · [返回题面](../chapters/{chapter(pid)}/problems/{ident}/README.md)

来源：[一手资料]({t['source']})。只核对定义和思路，答案自行编写，无需安装来源项目。
'''
        (ROOT/'solutions'/f'{ident}.md').write_text(solution_md,encoding='utf-8')


if __name__ == '__main__':
    write_materials()
