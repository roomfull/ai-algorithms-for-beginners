"""维护工具：固定手算案例，生成模拟材料。会覆盖练习，请先保存学员改动。"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location('mock_fixtures', ROOT/'tests/test_mock_algorithms.py')
fixtures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixtures)
CASES = fixtures.CASES  # 预期为独立手算固定数据，绝不运行答案生成。

MATERIALS = {}


def register(pid, title, description, inputs, outputs, manual, hints, idea, complexity, mistakes, source, code):
    MATERIALS[pid] = locals()


register('M01A', '训练集标准化后的 KNN 分类',
 '传感器两种量纲可能差异很大。仅用训练集逐列拟合均值 μ 与总体方差 v=Σ(x−μ)²/n，非恒定列作 Z-score：(x−μ)/√v。查询使用同一组统计量，不能加入训练集。恒定列以原字符串精确判断，训练与查询都置0（忽略此列）。按标准化欧氏距离平方选 k 个近邻，再以无权多数票分类。距离数学上相等时取训练下标较小者；标签票数相等时取数值较小者。',
 '首行 n d k；接着 n 行，每行 d 个十进制特征和1个整数标签；最后一行 d 个查询特征。1≤k≤n≤30，1≤d≤8；特征绝对值≤100，最多3位小数；标签绝对值≤100。输入合法。',
 '第一行 k 个近邻下标（0起）；第二行预测整数标签。两行均严格输出整数。',
 '样例均值=(2,100/3)，总体方差=(8/3,20000/9)。查询(2,0)，标准化后与三点的距离平方依次为1.5、4.5、1.5，故 k=1 取下标0，标签9。恒定列不参与距离。',
 ['统计量只从训练集取得。', '查询与样本均减同一个均值，作差后均值抵消；距离平方可写成Σ(x−q)²/v。', '从原字符串构造Fraction计算总体方差和距离，再按(distance,index)排序；Counter计票后按(-票数,标签)选标签。'],
 'Z-score 是为了消除量纲。无需计算开根号：每维标准化差平方等于(x−q)²/v。Fraction精确保存十进制值、方差、距离，避免距离平票误差。只把恒定列排除，不用查询值修正训练统计量。',
 'O(nd+nd+k log k+n log n)次有理数/比较操作，可简写为O(nd+n log n)；输入与数据O(nd)。有理数位数增长时单次运算不是恒定时间，应乘对应位运算成本。',
 '不要把查询并入训练集；方差除以n；忽略恒定列；先按距离选邻居再投票；标签最小优先不是邻居下标最小优先。',
 'https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html',
 '''import sys
from fractions import Fraction
from collections import Counter

def solve(raw):
    it=iter(raw.split())
    n,d,k=int(next(it)),int(next(it)),int(next(it))
    x=[]; labels=[]
    for _ in range(n):
        x.append([Fraction(next(it)) for _ in range(d)])
        labels.append(int(next(it)))
    q=[Fraction(next(it)) for _ in range(d)]
    means=[sum(row[j] for row in x)/n for j in range(d)]
    variances=[sum((row[j]-means[j])**2 for row in x)/n for j in range(d)]
    # Z-score差的平方无需sqrt，保留精确平票。
    distances=[sum((row[j]-q[j])**2/variances[j] for j in range(d) if variances[j]) for row in x]
    neighbors=sorted(range(n),key=lambda i:(distances[i],i))[:k]
    votes=Counter(labels[i] for i in neighbors)
    prediction=min(votes,key=lambda label:(-votes[label],label))
    return ' '.join(map(str,neighbors))+'\\n'+str(prediction)
''')

register('M01B', '机房网络布线的最小总成本',
 '多个机房需要接成一个连通网络，备选无向线路各有非负整数成本。求连接所有机房的最小总成本；无法连通时输出−1。允许自环和多条同端点线路，自环不能连接两个组件。采用Kruskal：成本相同的线路按输入下标处理。',
 '首行 n m；后续 m 行 u v w，顶点0..n−1。1≤n≤100，0≤m≤500，0≤w≤10000。输入合法。',
 '一行一个整数：最小生成树总成本，断开时−1；只有一个机房时为0。',
 '按成本选线路1(1→2,1)、2(2→3,2)、4(0→2,3)，连接4个机房，总成本1+2+3=6。线路0会形成环，线路3更贵。',
 ['连通n个点只需n−1条树边。','并查集判断两个端点是否已经连通。','按(w,输入下标)排序；根不同则合并并累加；选中数不足n−1则输出−1。'],
 '任何环中最贵边可以删除而保持连通。Kruskal依次接纳不会形成环的便宜边，用并查集维护组件。平行线路逐条考虑，单点空图也有一棵成本0的树。',
 '排序O(m log m)，路径压缩加按大小合并O((n+m)α(n))，空间O(n+m)，包括全部输入和排序边表。',
 '不能把最便宜的n−1条边直接相加；必须防环并检查连通；自环不贡献连接。',
 'https://github.com/networkx/networkx/blob/main/networkx/algorithms/tree/mst.py',
 '''import sys

def solve(raw):
    it=iter(map(int,raw.split())); n,m=next(it),next(it)
    edges=[]
    for index in range(m):
        u,v,w=next(it),next(it),next(it)
        edges.append((w,index,u,v))
    parent=list(range(n)); size=[1]*n
    def find(u):
        while parent[u]!=u:
            parent[u]=parent[parent[u]]
            u=parent[u]
        return u
    total=count=0
    for w,index,u,v in sorted(edges):
        a,b=find(u),find(v)
        if a==b: continue
        if size[a]<size[b]: a,b=b,a
        parent[b]=a; size[a]+=size[b]
        total+=w; count+=1
    return str(total if count==n-1 else -1)
''')


register('M02A', 'TF-IDF 文本余弦检索',
 '给定训练语料的词频矩阵，每列对应一个已给定词，词序不变。原始词频tf就是次数，不除文档长度、不取log。df_j为包含该词的训练文档数，idf_j=1+ln((n+1)/(df_j+1))，ln为自然对数。文档与查询都乘这组idf，查询不计入df。余弦=点积/(两个L2范数乘积)；任一零范数时定义为0，无共同词也为0。按round(score,12)降序排列，键相同时按文档下标升序；round是Python内置舍入，仅用于排名键，输出原始分数。',
 '首行 n v k；接着 n 行，每行 v 个非负整数词频；最后一行 v 个查询词频。1≤k≤n≤50，1≤v≤20，0≤词频≤100。输入合法，无需分词或下载语料。',
 '第一行前k篇文档下标（0起）；第二行对应的k个原始余弦分数。',
 '两列df都为2，idf都为1+ln(4/3)，共同系数抵消。查询(1,0)与三篇余弦分别1、0、1/√2，round(score,12)排序为0、2、1；输出原分数1、0.7071067811865476、0。',
 ['先按列统计非零文档数，不统计查询。','计算训练idf，再分别构造加权文档与加权查询；零范数直接给0。','scores存原分数；sorted(range(n),key=lambda i:(-round(scores[i],12),i))[:k]取下标，再输出对应scores。'],
 '固定词频矩阵让检索流程可手算。平滑idf保证未出现在训练集的给定词列也有有限权重。加权后用余弦消除文档向量长度影响；空文档、空查询不能直接除以0。排名键按12位小数舍入使平票规则确定，输出依然保留原分数。',
 '时间O(nv+n log n)，空间O(nv+n+v)，包含输入矩阵。使用双精度浮点，排名键按题面round(score,12)。',
 'idf需+1平滑，tf为原始次数；查询不参与df；余弦不能只算点积；空向量为0；排名按舍入键而输出未舍入分数。',
 'https://github.com/scikit-learn/scikit-learn/blob/main/doc/modules/feature_extraction.rst',
 '''import sys
import math

def solve(raw):
    it=iter(map(int,raw.split())); n,v,k=next(it),next(it),next(it)
    docs=[[next(it) for _ in range(v)] for _ in range(n)]
    query=[next(it) for _ in range(v)]
    df=[sum(row[j]>0 for row in docs) for j in range(v)]
    idf=[1+math.log((n+1)/(count+1)) for count in df]
    q=[query[j]*idf[j] for j in range(v)]
    qnorm=math.sqrt(sum(value*value for value in q))
    scores=[]
    for row in docs:
        weighted=[row[j]*idf[j] for j in range(v)]
        norm=math.sqrt(sum(value*value for value in weighted))
        score=sum(weighted[j]*q[j] for j in range(v))/(norm*qnorm) if norm and qnorm else 0.0
        scores.append(score)
    # 只有排序键舍入；输出保留未舍入分数。
    indices=sorted(range(n),key=lambda i:(-round(scores[i],12),i))[:k]
    return ' '.join(map(str,indices))+'\\n'+' '.join(f'{scores[i]:.12g}' for i in indices)
''')

register('M02B', '带悬挂网页的 PageRank 排名',
 '由均匀概率p_i=1/n开始，按给定有向链接同步迭代。悬挂网页（无出边）的全部概率均分给所有网页；每条出边分到来源概率/出度。新概率q_i=(1−alpha)/n+alpha*(悬挂质量/n+入边概率份额之和)。每轮更新后算L1=Σ|q_i−p_i|，L1≤tol即收敛，否则最多max_iter轮。始终至少迭代1轮。按最后概率精确降序排名，精确平票按网页下标升序。alpha、tol直接由原十进制字符串构造Fraction，全流程用有理数计算，不加epsilon。',
 '首行 n m alpha tol max_iter；接着 m 行 u v。1≤n≤20，0≤m≤100，0≤alpha<1，0<tol≤1，1≤max_iter≤200；小数最多6位。允许自环，无重复有向边。输入合法。小图限制用于精确边界教学，不模拟大图运行性能。',
 '第一行实际轮数及是否收敛（1/0）；第二行所有网页排名下标；第三行按原网页下标排列的最后概率（并非按排名排列）。',
 '网页1悬挂，alpha=0.8。三轮概率为(0.3,0.7)、(0.38,0.62)、(0.348,0.652)，L1为0.4、0.16、0.064。第3轮≤0.1，标记1；网页1高于0，所以排名1 0；概率仍输出原顺序0.348 0.652。',
 ['出度为0时均分，不丢掉概率。','p和q必须分开；先精确算L1，再用q替换p。','Fraction读原字符串；判断delta<=tol，按(-p[i],i)排序；只有最终打印概率才转float。'],
 '邻接表保存出边，每轮从同一旧p同步流出质量。悬挂部分与随机跳转部分先均匀填入q，再沿链接加份额。精确L1避免十进制阈值数学上相等时误判轮数；精确最后概率也决定排名平票。未收敛时仍报告末轮分布。',
 'K轮需要O(K(n+m)+n log n)次有理数/比较操作，输入与邻接表O(n+m)项、概率O(n)项。若中间整数最多B位，应乘相应大整数运算成本C(B)，概率存储O(nB)位；分母可随K增长，Fraction不能视为恒定成本。',
 '本题L1≤tol，NetworkX常用n*tol；不从float反构造Fraction；不能原地更新；输出概率按原下标；上限终止不是自动收敛。',
 'https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html',
 '''import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); n,m=int(next(it)),int(next(it))
    alpha,tol=Fraction(next(it)),Fraction(next(it)); limit=int(next(it))
    adj=[[] for _ in range(n)]
    for _ in range(m):
        u,v=int(next(it)),int(next(it)); adj[u].append(v)
    p=[Fraction(1,n)]*n; flag=0
    for step in range(1,limit+1):
        dangling=sum(p[u] for u in range(n) if not adj[u])
        q=[(1-alpha)/n+alpha*dangling/n for _ in range(n)]
        for u in range(n):
            for v in adj[u]: q[v]+=alpha*p[u]/len(adj[u])
        delta=sum(abs(q[i]-p[i]) for i in range(n))
        p=q
        if delta<=tol:
            flag=1; break
    ranking=sorted(range(n),key=lambda i:(-p[i],i))
    return f'{step} {flag}\\n'+' '.join(map(str,ranking))+'\\n'+' '.join(f'{float(value):.12g}' for value in p)
''')


register('M03A', '指定初值聚类、误差与查询分配',
 '给定k个初始中心，恰好执行T轮Lloyd更新：先按旧中心给每个训练样本分配最近中心，再同时以簇内均值替换各中心。空簇保留旧中心。距离平方数学上平票时取中心下标较小者。执行完T轮后，按最终中心重新分配全部训练样本，计算SSE=Σ样本到所属最终中心的距离平方，再把查询分配给最近的最终中心；最后重分配不再更新中心。所有十进制坐标由原字符串构造Fraction，保持精确距离平票与均值。',
 '首行 n d k T；接着n行训练坐标，每行d个十进制数；接着k行初始中心；最后一行查询坐标。1≤n≤30，1≤d≤8，1≤k≤5，1≤T≤30；坐标绝对值≤100，最多3位小数；初值可重复。输入合法。',
 '第一行n个最终训练标签（中心下标0起）；接着k行最终中心（每行d个浮点数）；然后一行SSE；最后一行查询整数标签。',
 '初始中心0、10，第一轮点0、2归0，点8、10归1，均值变为1、9；第二轮不变。最终标签0 0 1 1，SSE=1+1+1+1=4；查询5离两个中心都为4，精确平票选0。',
 ['分配与更新分成两步，各轮用全部旧中心。','空簇不改；新中心为逐维和/簇大小。','执行T次更新后再调用一次分配；SSE使用最终标签与最终中心，查询独立分配，不加入训练均值。'],
 '固定轮数与显式初值排除随机性。一个nearest函数用于训练与查询，以(距离平方,中心下标)选最小值。每轮分配后同时更新，不能处理一个样本就改中心。最后重分配保证输出标签与SSE对应已输出的中心；即使重分配改变成员，也不再计算均值。',
 '时间O(Tnkd+nkd+kd)次有理数/比较操作，即O(Tnkd)；空间O(nd+kd+n)，含输入、中心和标签。有理数运算随整数位数B而变化，应乘位运算成本C(B)，不可当作恒定时间。',
 '不能省略最后重分配；T固定不提前停止；SSE不是平均误差，也不取根号；空簇保留旧中心；查询不参与训练；平票从原字符串精确判定。',
 'https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html',
 '''import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); n,d,k,T=[int(next(it)) for _ in range(4)]
    x=[[Fraction(next(it)) for _ in range(d)] for _ in range(n)]
    centers=[[Fraction(next(it)) for _ in range(d)] for _ in range(k)]
    query=[Fraction(next(it)) for _ in range(d)]
    def distance(point, center):
        return sum((point[j]-center[j])**2 for j in range(d))
    def nearest(point):
        return min(range(k),key=lambda c:(distance(point,centers[c]),c))
    for _ in range(T):
        labels=[nearest(point) for point in x]
        updated=[]
        for c in range(k):
            members=[i for i in range(n) if labels[i]==c]
            updated.append([sum(x[i][j] for i in members)/len(members) for j in range(d)] if members else centers[c][:])
        centers=updated
    # 末轮更新后，重新分配但不再更新中心。
    labels=[nearest(point) for point in x]
    sse=sum(distance(x[i],centers[labels[i]]) for i in range(n))
    rows=[' '.join(map(str,labels))]
    rows+=[' '.join(f'{float(value):.12g}' for value in center) for center in centers]
    rows+=[f'{float(sse):.12g}',str(nearest(query))]
    return '\\n'.join(rows)
''')

register('M03B', '逐行对称权重量化与重构误差',
 '权重矩阵每行代表一个输出通道。用b位有符号对称量化，Q=2^(b−1)−1，只使用整数区间[−Q,Q]（不使用−2^(b−1)）。每行amax=max|w|，非零行scale=amax/Q，全零行scale=1。计算w/scale，四舍五入到最近整数，精确半格向远离0方向舍入，再裁剪到[−Q,Q]。反量化w_hat=q*scale；报告每行MSE=Σ(w−w_hat)²/c。原十进制字符串构造Fraction后精确计算比例与半格，不能用Python内置round的半偶规则。',
 '首行 r c b；接着r行，每行c个十进制权重。1≤r≤20，1≤c≤20，2≤b≤8；权重绝对值≤100，最多3位小数。输入合法。仅单机数值模拟，不声称量化一定加速。',
 '第一行r个scale；接着r行量化整数（每行c个）；最后一行r个反量化MSE。整数矩阵行必须严格整数。',
 'b=3，所以Q=3。第1行amax=3、scale=1，量化(−3,0,3)；第2行amax=1、scale=1/3，量化同为(−3,0,3)。两行反量化完全还原，MSE都是0。精确±0.5半格在其他案例中分别变为±1。',
 ['每行单独找amax并算scale。','对绝对比例floor(t+1/2)，再恢复符号，避免负数向零截断。','Fraction比例的分子p、分母q可用(2*p+q)//(2*q)实现非负半格向上；MSE用反量化值与原权重的平方差均值。'],
 '逐行scale适应通道量级差异。半格舍入使用精确有理数，使输入0.1/0.2数学上等于0.5的边界可重现；先处理绝对值再恢复符号。MSE报告原权重尺度下的误差，除以列数。scale只在输出时转float，不能以打印后的scale重构。',
 '时间O(rc)次有理数运算，空间O(rc+r)，包含输入、量化矩阵与输出；整数位数B变化时应计入C(B)运算成本。',
 'scale按行不是全矩阵；全零scale为1；不能用round半偶；负半格要远离零；Q不是2^(b−1)；MSE需除c。',
 'https://github.com/pytorch/pytorch/blob/main/torch/ao/quantization/observer.py',
 '''import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); r,c,b=[int(next(it)) for _ in range(3)]
    weights=[[Fraction(next(it)) for _ in range(c)] for _ in range(r)]
    Q=2**(b-1)-1; scales=[]; integers=[]; errors=[]
    for row in weights:
        maximum=max(abs(value) for value in row)
        scale=maximum/Q if maximum else Fraction(1)
        quantized=[]
        for value in row:
            ratio=abs(value)/scale
            # 精确半格远离零，不使用round的半偶舍入。
            rounded=(2*ratio.numerator+ratio.denominator)//(2*ratio.denominator)
            signed=rounded if value>=0 else -rounded
            quantized.append(max(-Q,min(Q,signed)))
        mse=sum((row[j]-quantized[j]*scale)**2 for j in range(c))/c
        scales.append(scale); integers.append(quantized); errors.append(mse)
    rows=[' '.join(f'{float(value):.12g}' for value in scales)]
    rows+=[' '.join(map(str,row)) for row in integers]
    rows+=[' '.join(f'{float(value):.12g}' for value in errors)]
    return '\\n'.join(rows)
''')


register('M04A', '卷积、ReLU 与平均池化特征',
 '单通道图像先与方形核作valid互相关（CNN惯例的“卷积”，不翻转核）：步长1，无padding，结果加给定标量偏置；逐元素ReLU=max(0,z)；再作p×p平均池化，池化步长p，无padding，只保留完整窗口，多余的下边与右边丢弃。平均池化以ReLU后的全部p²个元素为分母，零也计入。输出最终特征矩阵。',
 '首行 h w s p；接着h行图像（每行w个数）；接着s行核（每行s个数）；最后一行偏置。1≤h,w≤20，1≤s≤min(h,w)，1≤p≤min(h−s+1,w−s+1)；数值绝对值≤100，最多3位小数。输入合法。',
 '第一行最终行数 floor((h−s+1)/p) 和列数 floor((w−s+1)/p)，严格整数；随后按行输出池化浮点矩阵。',
 '核左上1、右下−1，valid四个位置都是左上值减右下值=−4。加偏置5得到四个1，ReLU仍为1；p=2，四值平均为1，最终尺寸1 1。',
 ['先算valid结果大小h−s+1、w−s+1。','每个窗口按原核顺序点乘累加，加偏置后立即ReLU。','对池化输出位置(i,j)，取激活矩阵起点(i*p,j*p)的p×p窗口，求和除p*p。'],
 '按图像空间位置两重循环，加上核位置两重循环完成互相关。池化输出尺寸用整除自然丢弃余边。实现保留激活中间矩阵使步骤清晰；ReLU在平均池化之前应用，两者不能交换。',
 '设H=h−s+1、W=w−s+1，时间O(HWs²+floor(H/p)floor(W/p)p²)，空间O(hw+s²+HW)，包含输入和激活结果。',
 'CNN互相关不翻核；偏置加在激活前；池化分母包含零；余边直接丢弃，不作小窗口平均；池化步长是p。',
 'https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html',
 '''import sys

def solve(raw):
    it=iter(raw.split()); h,w,s,p=[int(next(it)) for _ in range(4)]
    image=[[float(next(it)) for _ in range(w)] for _ in range(h)]
    kernel=[[float(next(it)) for _ in range(s)] for _ in range(s)]
    bias=float(next(it)); H,W=h-s+1,w-s+1
    activation=[]
    for i in range(H):
        row=[]
        for j in range(W):
            z=bias+sum(image[i+u][j+v]*kernel[u][v] for u in range(s) for v in range(s))
            row.append(max(0.0,z))
        activation.append(row)
    oh,ow=H//p,W//p
    rows=[f'{oh} {ow}']
    for i in range(oh):
        values=[sum(activation[i*p+u][j*p+v] for u in range(p) for v in range(p))/(p*p) for j in range(ow)]
        rows.append(' '.join(f'{value:.12g}' for value in values))
    return '\\n'.join(rows)
''')

register('M04B', '不同 worker 与 microbatch 的加权更新',
 '给定多个worker，每个worker有若干大小可能不同的microbatch（微批次）。每条微批次提供样本数s以及以样本为单位求平均后的梯度g。所有梯度已在同一初始参数w处计算。全局梯度G=Σ(s*g)/Σs（求和遍历所有worker的全部微批次），然后仅做一次SGD更新w_new=w−lr*G。不直接平均微批次平均值，也不等权平均worker平均值。此为单机数值模拟，无实际通信、多进程或性能保证。',
 '首行 worker数量 W、参数维数 d、学习率 lr；第二行d个初始参数；随后对每个worker：一行微批次数t，然后t行，每行先给样本数s，再给d个平均梯度。1≤W≤8，1≤d≤10，1≤t≤8，1≤s≤100，0≤lr≤10；参数/梯度绝对值≤100，最多3位小数。输入合法。',
 '第一行d个全局平均梯度；第二行d个更新后的参数。',
 'worker0两批：(s=1,g=(2,4))和(s=3,g=(0,0))；worker1一批：(s=2,g=(3,6))。总样本6，总梯度和(8,16)，G=(4/3,8/3)。lr=0.1，从(1,2)更新为(13/15,26/15)。',
 ['输入梯度是平均值，先乘该批样本数还原梯度和。','跨所有worker累加总样本数及每一维梯度和。','全部读完后才除总样本数，再作一次更新；不要每读一批就更新w。'],
 '样本贡献等权，微批次与worker只是划分方式。Fraction保存给定小数便于验证分批不改变结果；累加每批s*g后统一除总s，不需要保存整个梯度历史。学习率0时仍输出全局梯度，参数保持原值。',
 '设B为全部微批次数，时间O(Bd)次有理数运算，算法累加器O(d)空间；本solve先raw.split读全部输入，实际总空间O(Bd)，有理数位运算成本随整数位数变化。',
 '批大小不同不能等权平均批均值；worker总样本不同不能等权平均worker均值；只更新一次；本题没有动量和正则化；所有梯度在同一w处算。',
 'https://pytorch.org/docs/stable/notes/ddp.html',
 '''import sys
from fractions import Fraction

def solve(raw):
    it=iter(raw.split()); W,d=int(next(it)),int(next(it)); lr=Fraction(next(it))
    weights=[Fraction(next(it)) for _ in range(d)]
    totals=[Fraction(0)]*d; samples=0
    for _ in range(W):
        batches=int(next(it))
        for _ in range(batches):
            count=int(next(it)); samples+=count
            for j in range(d): totals[j]+=count*Fraction(next(it))
    # 先恢复梯度和，统一除样本总数，最后只更新一次。
    gradient=[value/samples for value in totals]
    updated=[weights[j]-lr*gradient[j] for j in range(d)]
    return ' '.join(f'{float(value):.12g}' for value in gradient)+'\\n'+' '.join(f'{float(value):.12g}' for value in updated)
''')


def build(chapter):
    number=chapter[1:]
    exam=ROOT/'exams'/f'mock{number}'
    exam.mkdir(parents=True,exist_ok=True)
    links=[]
    for pid, item in MATERIALS.items():
        if not pid.startswith(chapter): continue
        folder=exam/pid; folder.mkdir(exist_ok=True)
        c=CASES[pid][0]
        mode='int' if pid=='M01B' else 'float'
        (folder/'cases.json').write_text(json.dumps(dict(id=pid,chapter=chapter,title=item['title'],mode=mode,requires=[],cases=CASES[pid]),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (folder/'exercise.py').write_text('"""请自行完成输入解析、算法及输出格式。"""\nimport sys\n\n\ndef solve(raw):\n    raise NotImplementedError("请按题目提示完成这里")\n\n\ndef main():\n    print(solve(sys.stdin.read()))\n\n\nif __name__ == "__main__":\n    main()\n',encoding='utf-8')
        hints='\n\n'.join(f'<details><summary>提示 {i}</summary>\n\n{h}\n\n</details>' for i,h in enumerate(item['hints'],1))
        readme=f'''# {pid} {item['title']}

{item['description']}

## 输入与约束

{item['inputs']}

## 输出

{item['outputs']} 浮点行允许绝对/相对误差1e-6，建议输出12位有效数字；计算期间不要提前取整，题面明确的排名键除外。

## 样例与手算

输入：
```text
{c['input'].rstrip()}
```
输出：
```text
{c['expected'].rstrip()}
```

手算：{item['manual']}

## 分级提示

{hints}

## 运行与检查

在项目根目录运行，无需激活：
```powershell
.\\.venv\\Scripts\\python.exe exams/mock{number}/{pid}/exercise.py
.\\.venv\\Scripts\\python.exe check.py {pid}
.\\.venv\\Scripts\\python.exe check.py --chapter {chapter}
```

自行写输入解析与输出；标准输出只写结果。手动输入结束按Windows Ctrl+Z再回车，也可 `Get-Content input.txt | .\\.venv\\Scripts\\python.exe exams/mock{number}/{pid}/exercise.py`。检查器自动送入案例。

来源：[一手定义与实现参考]({item['source']})。本题为原创组合练习，未声称是正式真题；参考代码独立编写，教学约定以本题为准，离线学习无需联网。

[本卷入口](../README.md) · [课程入口](../../../README.md) · [独立题解](../../../solutions/{pid}.md)
'''
        (folder/'README.md').write_text(readme,encoding='utf-8')
        (ROOT/'solutions'/f'{pid}.py').write_text(f'"""{item["title"]}：独立参考解。"""\n'+textwrap.dedent(item['code']).lstrip()+'\n\nif __name__ == "__main__":\n    print(solve(sys.stdin.read()))\n',encoding='utf-8')
        (ROOT/'solutions'/f'{pid}.md').write_text(f'''# {pid} 题解：{item['title']}

## 思路与关键步骤

{item['idea']}

样例复核：{item['manual']}

## 复杂度

{item['complexity']}

## 易错点

{item['mistakes']}

## 代码与核验

[单文件参考代码]({pid}.py)。在根目录执行 `.\\.venv\\Scripts\\python.exe check.py {pid} --solution`。独立手算与性质测试见 [模拟算法测试](../tests/test_mock_algorithms.py)。先自己作答，再看本解。

来源：[一手定义与实现参考]({item['source']})。代码独立编写，输入输出与确定性边界由本题定义，不要求安装来源项目。
''',encoding='utf-8')
        links.append(f'- [{pid} {item["title"]}]({pid}/README.md)')
    (exam/'README.md').write_text(f'''# 模拟卷 {number}

本卷是两道原创组合题，一道公共AI基础、一道系统优化；建议完成相关章节后独立练习。它不是正式真题，题目数量、时长和评分不能推断正式考试要求。

可打开计时器，先记录自己用时，再分析读题、手算、编码、调试各阶段；本课程不规定正式考试时长或分值。模拟练习只有最小 solve/main 脚手架，输入输出需要自己写。先看输入、输出与边界，手算首样例，再实现并检查；结束后填写错题记录。

{chr(10).join(links)}

在根目录运行：
```powershell
.\\.venv\\Scripts\\python.exe check.py --chapter {chapter}
```

先修：第01—09章，[课程路线](../../README.md)。答案在独立的 [solutions](../../solutions/) 文件夹，作答完成后再对照。
''',encoding='utf-8')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chapter',choices=['M01','M02','M03','M04'],required=True)
    args=parser.parse_args()
    build(args.chapter)
