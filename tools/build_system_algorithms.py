"""Task 5 materials generator. Cases are hand-derived, never run answers to make oracles."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SPECS = {}

def add(pid, title, statement, inputs, outputs, hand, hints, idea, complexity, pitfalls, cases, mode='int', source=None):
    chapter = '07_graphs' if pid <= 70 else '08_compression' if pid <= 76 else '09_distributed'
    SPECS[pid] = dict(id=f'P{pid:03}', chapter=chapter, title=title, statement=statement,
                      inputs=inputs, outputs=outputs, hand=hand, hints=hints, idea=idea,
                      complexity=complexity, pitfalls=pitfalls, cases=cases, mode=mode,
                      source=source or ('https://networkx.org/documentation/stable/reference/algorithms/index.html' if pid<=70 else 'https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html' if pid<=73 else 'https://docs.pytorch.org/docs/stable/quantization.html' if pid<=76 else 'https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html'))

def case(name, raw, expected, modes=None):
    d=dict(name=name,input=raw,expected=expected)
    if modes is not None:
        d['line_modes']=modes
    return d

def materialize(ids=None):
    for pid,s in SPECS.items():
        if ids is not None and pid not in ids:
            continue
        folder=ROOT/'chapters'/s['chapter']/'problems'/s['id']
        folder.mkdir(parents=True,exist_ok=True)
        metadata={k:s[k] for k in ('id','title','mode')}
        metadata.update(chapter=s['chapter'][:2],requires=[],cases=s['cases'])
        (folder/'cases.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        hints='\n\n'.join(f'<details><summary>提示 {i}</summary>\n\n{h}\n\n</details>' for i,h in enumerate(s['hints'],1))
        first=s['cases'][0]
        index_note=' 顶点编号为0..n-1。' if pid<=70 else ' 行索引从0开始。' if pid==73 else ''
        text=f'''# {s['id']} {s['title']}

{s['statement']}

## 输入与约束

{s['inputs']} 保证输入合法。{index_note} 所有小数最多6位，有限且绝对值≤10000，除非本题另有说明。

## 输出

{s['outputs']} 整数行必须输出整数；浮点行允许绝对或相对误差1e-6，建议保留12位有效数字，计算期间不要提前取整。

## 样例与手算

输入：
```text
{first['input'].rstrip()}
```
输出：
```text
{first['expected'].rstrip()}
```

{s['hand']}

## 分级提示

{hints}

## 运行与检查

在仓库根目录，无需激活环境：
```powershell
.\\.venv\\Scripts\\python.exe chapters/{s['chapter']}/problems/{s['id']}/exercise.py
.\\.venv\\Scripts\\python.exe check.py {s['id']}
```

输入结束按 Windows Ctrl+Z 后回车；也可 `Get-Content input.txt | .\\.venv\\Scripts\\python.exe chapters/{s['chapter']}/problems/{s['id']}/exercise.py`。标准输出只写结果。

来源：[一手定义与实现参考]({s['source']})。本题为原创教学练习，参考代码独立编写，具体输出与确定性约定以题面为准，离线学习不用联网。

[章节入口](../../README.md) · [题解](../../../../solutions/{s['id']}.md) · [下一题](../P{pid+1:03}/README.md)
'''
        if pid in (70,76,80):
            nextchapter={'07_graphs':'08_compression','08_compression':'09_distributed','09_distributed':None}[s['chapter']]
            replacement=f'[下一章](../../../{nextchapter}/README.md)' if nextchapter else '[模拟卷与学习路线](../../../../README.md)'
            text=text.replace(f'[下一题](../P{pid+1:03}/README.md)',replacement)
        (folder/'README.md').write_text(text,encoding='utf-8')
        scaffold=f'''"""{s['id']} {s['title']}：完成后只向标准输出写题目要求的结果。"""
import sys


def solve(raw):
    # 1. 按题面解析输入；注意整数、浮点和精确小数字符串的区别。
    tokens = raw.split()
    # 2. {s['hints'][0]}
    # 3. {s['hints'][1]}
    # 4. 返回按题目行格式构造的字符串。
    raise NotImplementedError("请按题目提示完成这里")


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
'''
        (folder/'exercise.py').write_text(scaffold,encoding='utf-8')
        sol=f'''# {s['id']} 题解：{s['title']}

## 思路与关键步骤

{s['idea']}

{s['hand']}

## 复杂度

{s['complexity']}

## 易错点

{s['pitfalls']}

## 代码与核验

[独立参考代码]({s['id']}.py)。在根目录运行 `.\\.venv\\Scripts\\python.exe check.py {s['id']} --solution`；学习时先做练习和提示，再对照代码。案例覆盖样例和不同边界；独立性质测试见 `tests/test_system_algorithms.py`。

来源：[一手定义与实现参考]({s['source']})。代码独立编写；本题的规模、输入输出和边界约定是教学设计。
'''
        (ROOT/'solutions'/f'{s["id"]}.md').write_text(sol,encoding='utf-8')

add(59,'无向图邻接表','把无向简单图的每条边分别登记到两端的邻居表；同一个顶点的邻居按编号升序输出。无向边(u,v)意味着u能到v且v能到u。',
    '首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；无自环、无重边。',
    '共n行，第i行依次输出 i、邻居个数、所有邻居；孤立点只输出 i 0。',
    '边0—2给0增加邻居2，给2增加邻居0；边0—1同理。因此0的邻居升序为1,2，3没有邻居。',
    ['先为每个点建立一个空列表。','每条边执行两次append，再排序各行。','遍历i=0..n-1，输出 [i,len(adj[i])]+sorted(adj[i])。'],
    '初始化n个空列表。读边时对两个端点各登记一次，按点编号依次排序并输出；列表长度即无向度数。不要把点数当作边数。',
    '构建O(n+m)，排序O(Σ d_i log(d_i+1))，存储O(n+m)；每条边在邻接表中占两项。',
    '只登记一端会得到错误的有向图；不能漏掉孤立点的输出；邻居必须排序。',[
case('星形与孤立点','4 2\n0 2\n0 1\n','0 2 1 2\n1 1 0\n2 1 0\n3 0\n'),
case('单点','1 0\n','0 0\n'),case('无边','3 0\n','0 0\n1 0\n2 0\n'),
case('反向输入边','3 2\n2 1\n1 0\n','0 1 1\n1 2 0 2\n2 1 1\n'),
case('三角形','3 3\n0 1\n1 2\n0 2\n','0 2 1 2\n1 2 0 2\n2 2 0 1\n')])

add(60,'有向图入度与出度','有向边u→v只给u增加出度，给v增加入度；统计每个顶点的两个计数。自环给同一点同时增加入度和出度。',
    '首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；允许自环，不允许重复同向边；两个反向边可以共存。',
    '共n行，第i行输出 indegree[i] outdegree[i]，无需输出顶点编号。',
    '0→1与0→2让0出度为2；2→1让1入度为2、2入出度各1。',
    ['区分“指向我”与“从我出发”。','准备长度n的两个计数数组。','每次只执行 outdegree[u]+=1 与 indegree[v]+=1。'],
    '用两个独立整数数组分别计数。输入一次有向边，只在其起点的出度和终点的入度上加一。所有入度之和和出度之和都等于m。',
    '时间O(n+m)，辅助空间O(n)。无需存储边。','不要把两个方向都加；反向边不是重复；自环必须计入两种度数。',[
case('多对一','3 3\n0 1\n0 2\n2 1\n','0 2\n2 0\n1 1\n'),case('单自环','1 1\n0 0\n','1 1\n'),
case('孤立点','2 0\n','0 0\n0 0\n'),case('反向共存','2 2\n0 1\n1 0\n','1 1\n1 1\n'),
case('链','4 3\n3 2\n2 1\n1 0\n','1 0\n1 1\n1 1\n0 1\n')])

add(61,'BFS最短层次','在无向简单图中，从起点s开始用队列执行广度优先搜索。每条边的代价都是1，输出最少经过几条边到每个点；不可达为-1。',
    '首行 n m s；随后m行 u v。1≤n≤1000，0≤m≤5000，0≤s<n；无自环、无重边。',
    '一行n个距离，按顶点编号排列。',
    '起点0距离0；1和2一条边可达，距离1；3经过0→1→3距离2；4不可达为-1。',
    ['BFS需要先进先出的队列。','首次发现邻居时就标记距离，避免重复入队。','dist[s]=0；弹出u，若dist[v]==-1，则赋dist[v]=dist[u]+1并入队。'],
    '所有距离初始化为-1。先给s距离0并入队；用collections.deque的popleft取最早入队的点。第一次到达v时路径一定最短，因为队列按层扩展。',
    '时间O(n+m)，空间O(n+m)包含邻接表；队列和距离数组O(n)。','不要用栈代替队列；不能在出队时才标记；这只适用于等权边。',[
case('两层与不可达','5 4 0\n0 1\n0 2\n1 3\n2 3\n','0 1 1 2 -1\n'),
case('单点','1 0 0\n','0\n'),case('起点孤立','3 1 2\n0 1\n','-1 -1 0\n'),
case('链端起点','4 3 3\n0 1\n1 2\n2 3\n','3 2 1 0\n'),case('环捷径','4 4 0\n0 1\n1 2\n2 3\n3 0\n','0 1 2 1\n')])

add(62,'DFS与连通分量','对整个无向简单图做深度优先搜索。连通分量是互相存在路径的一组点；按最小顶点升序给分量编号0,1,...。使用显式栈避免递归深度限制。',
    '首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；无自环、无重边。',
    '第一行分量总数；第二行n个分量编号。',
    '0,2,3通过路径相连，分量编号0；1,4相连，编号1；5孤立，编号2。外层按0到5扫描保证编号确定。',
    ['从尚未标记的点启动一次DFS，就发现一个新分量。','栈后进先出；发现时立即给邻居标记当前编号。','扫描root；若label[root]==-1，标记并入栈，反复弹出扩展，结束后count+=1。'],
    '使用邻接表与整数label数组。外层按顶点升序检查未访问点，内部用栈走完整个分量。因此输出与输入边顺序无关，而不是输出不稳定的访问次序。',
    '时间O(n+m)，空间O(n+m)，显式栈最多O(n)。','只从0开始会漏掉其他分量；分量编号不是最短距离；孤立点也是分量。',[
case('非连续编号分量','6 3\n0 2\n2 3\n1 4\n','3\n0 1 0 0 1 2\n'),case('单点','1 0\n','1\n0\n'),
case('全孤立','3 0\n','3\n0 1 2\n'),case('连通链','4 3\n2 3\n1 2\n0 1\n','1\n0 0 0 0\n'),
case('两个环块','5 4\n0 1\n1 2\n2 0\n3 4\n','2\n0 0 0 1 1\n')])

add(63,'并查集连接查询','维护一组点的连接关系。操作0 a b表示把a与b所属的两个集合合并；操作1 a b询问两点是否属于同一集合。使用路径压缩与按集合大小合并。',
    '首行 n q；随后q行 type a b；type为0或1。1≤n≤1000，1≤q≤5000，保证至少一个查询；允许重复合并及a=b。',
    '每个查询一行：相连为1，否则0；合并不输出。',
    '最初0与1分开，查询得0；合并0,1后查询得1；合并1,2让0,2间接相连；3,4仍分开。',
    ['每个点最初是自己的父节点。','find沿父指针到根，同时缩短路径。','若两根不同，把较小集合的根挂到较大根下；查询比较find(a)==find(b)。'],
    'parent代表集合树，size只在根上有效。find用循环路径折半，不依赖递归。union先找根并按大小连接，重复合并直接略过；查询只比较根，不比较直接父节点。',
    '初始化O(n)，q次操作摊还O(q α(n))；parent与size空间O(n)，另存查询输出O(q)。α为增长极慢的反Ackermann函数。','父节点相同不是集合相同的必要条件；重复合并不能再次增加size；自身始终相连。',[
case('连接传递','5 7\n1 0 1\n0 0 1\n1 0 1\n0 1 2\n1 0 2\n1 3 4\n1 4 4\n','0\n1\n1\n0\n1\n'),
case('单点自查','1 1\n1 0 0\n','1\n'),case('没有合并','3 2\n1 0 2\n1 1 1\n','0\n1\n'),
case('重复合并','2 4\n0 0 1\n0 1 0\n0 0 0\n1 0 1\n','1\n'),
case('连接两个已有组','4 5\n0 0 1\n0 2 3\n1 0 3\n0 1 2\n1 0 3\n','0\n1\n')])

add(64,'无向简单图三角形计数','三角形是三个不同顶点，两两之间都有边。每组三点只统计一次；同一三角形的六种排列不重复计数。',
    '首行 n m；随后m行 u v。1≤n≤120，0≤m≤n(n-1)/2；无自环、无重边。',
    '一行一个整数：三角形数。',
    '三点0,1,2的三条边齐全，构成1个三角形；额外边2—3不能构成另一组三角形。',
    ['只枚举a<b<c。','用邻接集合快速判断一条边是否存在。','若b在adj[a]、c在adj[a]且c在adj[b]，计数加一。'],
    '为每个顶点建立邻居集合，三重循环只选择递增顶点；集合成员测试核对三条边。该实现便于手算和独立穷举验证，不追求大图优化。',
    '时间O(n³+m)，集合平均成员查询O(1)；空间O(n+m)。','不要把长度3的有向回路概念混进来；不能用度数直接断言三角形；若枚举所有排列须去重，本题直接按编号去重。',[
case('三角加尾巴','4 4\n0 1\n1 2\n2 0\n2 3\n','1\n'),case('单点','1 0\n','0\n'),
case('四边形','4 4\n0 1\n1 2\n2 3\n3 0\n','0\n'),case('完全四点','4 6\n0 1\n0 2\n0 3\n1 2\n1 3\n2 3\n','4\n'),
case('共边两三角','4 5\n0 1\n0 2\n1 2\n0 3\n1 3\n','2\n')])

add(65,'所有连通分量二分图判断','二分图可以把所有点分成两组，让每条边的两端处于不同组。用BFS双色标记检查整个无向简单图；每个孤立点也能合法染色。',
    '首行 n m；随后m行 u v。1≤n≤1000，0≤m≤5000；无自环、无重边。',
    '一行一个整数：整个图可二分输出1，否则0。',
    '四边形交替染色0,1,0,1，回边3—0也连接异色点，因此输出1。',
    ['每条边要求两端颜色不同。','从每个未染色点启动一次搜索。','color初始-1；根设0，邻居设1-color[u]；若已染色且相同就失败。'],
    '按顶点扫描全部分量，BFS传播相反颜色。碰到任意同色边立即返回0。遍历结束无冲突才返回1。奇数环无法交替染色，偶数环可以。',
    '时间O(n+m)，空间O(n+m)含邻接表；颜色与队列O(n)。','只检查起点0所在分量会漏掉另一分量的奇环；没有边应输出1；不要求两组都非空。',[
case('偶数环','4 4\n0 1\n1 2\n2 3\n3 0\n','1\n'),case('三角奇环','3 3\n0 1\n1 2\n2 0\n','0\n'),
case('空边集','3 0\n','1\n'),case('后方分量有奇环','5 4\n0 1\n2 3\n3 4\n4 2\n','0\n'),
case('五点链','5 4\n0 1\n1 2\n2 3\n3 4\n','1\n')])

mstcases=[case('便宜两边','3 3\n0 1 4\n1 2 2\n0 2 5\n','6\n'),case('单点树','1 0\n','0\n'),
case('孤立点','3 1\n0 1 2\n','DISCONNECTED\n',['text']),
case('负权','3 3\n0 1 -3\n1 2 1\n0 2 4\n','-2\n'),
case('并列与零权','4 5\n0 1 0\n1 2 2\n2 3 2\n0 3 2\n0 2 5\n','4\n')]
add(66,'Kruskal最小生成树','无向加权图的生成树包含全部顶点，恰好n-1条边且无环。Kruskal按权重升序考虑边，用并查集跳过成环边，求最小总权重；若图不连通则不存在生成树。',
    '首行 n m；随后m行 u v weight。1≤n≤200，0≤m≤2000；无自环、无重边，weight为[-10000,10000]整数。',
    '连通时一行最小总权重整数；不连通时一行 DISCONNECTED。单点的空生成树权重为0。',
    '先选权重2的1—2，再选权重4的0—1，已得到n-1=2条边，总权重6；权重5的边会成环。',
    ['最便宜边只有在不成环时才能选。','并查集判断两端是否已经相连。','边按(weight,u,v)排序；两端根不同则合并、total+=weight、used+=1；最后检查used==n-1。'],
    '对边排序后用路径压缩、按大小合并的并查集维护当前森林。跨两个集合的边安全连接分量；同集合边成环跳过。最终接受边数不足n-1时输出断连标记。',
    '时间O(m log(m+1)+(n+m) α(n))，空间O(n+m)，排序持有全部边。','负权完全合法，不要用Dijkstra的非负约束；不能把森林总和伪装成MST；并列权重可有多种树但最小总和相同。',mstcases,
    source='https://github.com/TheAlgorithms/Python/blob/master/graphs/minimum_spanning_tree_kruskal.py')
add(67,'Prim最小生成树','从顶点0开始，维护已加入的点集；每次选跨越该点集与外部的最便宜边。用最小堆实现Prim，与Kruskal应得到相同最小总权重。',
    '首行 n m；随后m行 u v weight。1≤n≤200，0≤m≤2000；无自环、无重边，weight为[-10000,10000]整数。',
    '连通时一行最小总权重整数；不连通时一行 DISCONNECTED。单点权重0。',
    '从0选0—1的权重4；可选边中1—2权重2比0—2权重5便宜，再选它；总权重6。',
    ['堆里保存可以把新点加入树的候选边。','同一个点可能有多个候选，出堆时跳过已经加入的点。','堆初始(0,0)，弹出(w,u)；若未访问则加入、加权并推入邻边；最后检查访问点数为n。'],
    '邻接表保存双向权重。最小堆从(0,0)开始，弹出未访问点时把对应边权加入total；起点虚拟边权0。把该点通向未访问邻居的边加入堆，旧候选稍后跳过。',
    '时间O(n+m log(m+1))，空间O(n+m)；懒删除堆可能有O(m)项，不应宣称堆最多n项。','起点的虚拟边不是图中的真实边；负权可加入；堆耗尽仍未访问全部点就是断连。',mstcases,
    source='https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html')

add(68,'PageRank单轮概率流','在有向图中，一轮PageRank由旧概率p同时计算新概率：q[v]=(1-alpha)/n+alpha*(Σ_{u→v}p[u]/outdegree[u]+dangling_mass/n)。无出边点的概率均匀分给全部点。不得边计算边覆盖旧p。',
    '首行 n m alpha；随后m行 u v；最后一行n个初始概率p。1≤n≤200，0≤m≤2000，0≤alpha<1；无重复有向边，允许自环；p≥0且总和为1（输入舍入误差≤1e-6）。',
    '一行n个新概率，按顶点顺序。',
    'alpha=0.8，旧p=(0.6,0.4)，只有0→1。传送基础每点0.1；悬挂点1贡献0.8×0.4/2=0.16；0再把0.48传给1，因此新p=(0.26,0.74)。',
    ['先算没有出边的概率总质量。','把传送项和悬挂均分项加入每个新概率。','q=[(1-alpha)/n+alpha*dangling/n]*n；每条u→v再给q[v]加alpha*p[u]/outdegree[u]。'],
    '从全部旧概率建立独立q数组。无出边点质量先汇总后均分；有出边点沿每条出边平均传递。若漏悬挂处理，总概率会减少。',
    '时间O(n+m)，空间O(n+m)包含邻接表与新旧概率。','有向边方向不可颠倒；不要忽略dangling质量；不用原地更新；alpha=0结果必为均匀分布。',[
case('一悬挂点','2 1 0.8\n0 1\n0.6 0.4\n','0.26 0.74\n'),
case('无边均分','3 0 0.9\n0.2 0.3 0.5\n','0.333333333333 0.333333333333 0.333333333333\n'),
case('均匀环','3 3 0.85\n0 1\n1 2\n2 0\n0.333333 0.333334 0.333333\n','0.33333305 0.33333305 0.3333339\n'),
case('零阻尼','2 1 0\n1 0\n1 0\n','0.5 0.5\n'),
case('自环单点','1 1 0.9\n0 0\n1\n','1\n')],mode='float',source='https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html')

add(69,'PageRank迭代至收敛','从均匀概率p[i]=1/n开始，重复P068的同步更新（包括悬挂点均分）。每轮更新后计算L1变化量Σ|q[i]-p[i]|；≤tol即停止并标记收敛，最多max_iter轮。输出最后已完成的q。此处直接使用tol，不采用某些库的n*tol阈值。',
    '首行 n m alpha tol max_iter；随后m行 u v。1≤n≤200，0≤m≤2000，0≤alpha<1，0<tol≤1，1≤max_iter≤10000；允许自环，无重复有向边。',
    '第一行 实际轮数 是否收敛（1/0）；第二行n个最后概率。即使初始分布已经是固定点，也先做一轮再判断。',
    '均匀初值(0.5,0.5)，alpha=0.8，0→1。前3轮分别为(0.3,0.7)、(0.38,0.62)、(0.348,0.652)。L1依次0.4,0.16,0.064；第3轮≤0.1，输出3 1。',
    ['每轮调用与单轮相同的概率流过程。','先计算delta，再用q替换p；收敛输出的是q。','for step in 1..max_iter：构造q；delta=sum(abs(q[i]-p[i]))；p=q；若delta<=tol则标记并break。'],
    '用两数组同步更新；每轮对无出边质量均分，再沿边传递，最后计算L1差。轮数从1计。达到上限但差仍大于tol时明确输出0，不把强制终止称作收敛。',
    'K实际轮时，时间O(K(n+m))，空间O(n+m)；不存历史迭代。','不能拿每元素差替代L1；阈值不是n*tol；未收敛仍返回末轮概率；不检查均匀初值并输出0轮。',[
case('三轮收敛','2 1 0.8 0.1 10\n0 1\n','3 1\n0.348 0.652\n',['int','float']),
case('达到上限','2 1 0.8 0.01 1\n0 1\n','1 0\n0.3 0.7\n',['int','float']),
case('无边固定点','3 0 0.9 0.001 5\n','1 1\n0.333333333333 0.333333333333 0.333333333333\n',['int','float']),
case('均匀环固定点','3 3 0.85 0.000001 5\n0 1\n1 2\n2 0\n','1 1\n0.333333333333 0.333333333333 0.333333333333\n',['int','float']),
case('恰好阈值','2 1 0.5 0.25 5\n0 1\n','1 1\n0.375 0.625\n',['int','float'])],mode='float',source='https://networkx.org/documentation/stable/_modules/networkx/algorithms/link_analysis/pagerank_alg.html')

add(70,'图综合验收','对同一个无向简单图输出三个统计量：连通分量总数、整个图是否二分、三角形总数。必须独立判断二分图；没有三角形仍可能存在五边奇环。',
    '首行 n m；随后m行 u v。1≤n≤120，0≤m≤n(n-1)/2；无自环、无重边。',
    '一行三个整数：components bipartite triangles。二分标记为1或0。',
    '0,1,2形成三角，3—4形成另一分量。共有2分量；三角是奇环所以二分为0；三角总数1。',
    ['分量搜索、染色与三角统计共享邻接结构。','染色冲突不要提前终止全部搜索，否则分量数会不完整。','每个未访问根增加分量并完成双色搜索，冲突只设flag=0；另枚举a<b<c统计三角。'],
    '邻接集合用于三角检查，同时可用于BFS。每个未染色根启动一个新分量，遇到同色边把标记置0但继续遍历所有点。三角统计独立按递增三点计数。',
    '时间O(n³+n+m)，空间O(n+m)。','三角为0不能推出二分；发现奇环仍须统计剩余分量；输出顺序固定。',[
case('三角和边','5 4\n0 1\n1 2\n2 0\n3 4\n','2 0 1\n'),case('无边','4 0\n','4 1 0\n'),
case('五边奇环无三角','5 5\n0 1\n1 2\n2 3\n3 4\n4 0\n','1 0 0\n'),
case('完全四点','4 6\n0 1\n0 2\n0 3\n1 2\n1 3\n2 3\n','1 0 4\n'),
case('偶数环与孤点','5 4\n0 1\n1 2\n2 3\n3 0\n','2 1 0\n')])

add(71,'绝对值阈值剪枝','把权重向量中绝对值严格小于阈值t的项置0；等于阈值的项保留。剪枝只是改变数值，普通稠密存储的元素数量仍是n。',
    '首行 n t；第二行n个权重。1≤n≤1000，0≤t≤10000。',
    '一行n个剪枝后的浮点权重，位置不变。',
    '阈值1：|0.5|和|-0.2|小于1置0；-1和1恰等阈值保留；2也保留。',
    ['先取绝对值再比较。','判断是严格小于，不能写成小于等于。','依次输出0 if abs(x)<t else x；用Fraction从原始字符串读入可让小数边界精确。'],
    '解析十进制权重和阈值为Fraction，逐项执行严格比较。输出时转float格式化；算法判断本身不使用人为epsilon。',
    '在输入小数长度有界的约定下时间O(n)，空间O(n)含输入和输出；精确有理数运算的位数成本在此有界。','小于与小于等于不同；阈值0保留所有值；不能称置零为已压缩文件或实测加速。',[
case('等于阈值保留','5 1\n0.5 -1 1 2 -0.2\n','0 -1 1 2 0\n'),case('零阈值','3 0\n0 -0.1 2\n','0 -0.1 2\n'),
case('全部剪掉','3 5\n-4 0 4\n','0 0 0\n'),case('精确小数边界','3 0.3\n0.299999 -0.3 0.300001\n','0 -0.3 0.300001\n'),
case('单个大权重','1 2\n-3\n','-3\n')],mode='float')

add(72,'按比例剪掉最小绝对值','计算k=floor(n*ratio)，按(abs(weight),index)升序选择恰好k个位置置0。并列时较小索引先剪。掩码1表示保留，0表示被选中剪掉；原值本来是0但未选中仍可有掩码1。',
    '首行 n ratio；第二行n个权重。1≤n≤1000，0≤ratio≤1；ratio为十进制字符串，应按其精确值计算floor。',
    '第一行n个0/1保留掩码；第二行n个剪枝后权重。',
    'n=5，ratio=0.4，k=2。绝对值最小的索引2（0）先剪，其次索引1（1）；索引3（-1）并列但更靠后保留。',
    ['先算要剪几个，再排序位置。','用Fraction(ratio_token)保留比例的精确十进制值。','k=int(n*Fraction(token))；idx=sorted(range(n),key=lambda i:(abs(x[i]),i))[:k]；更新mask。'],
    '有理数精确求n*ratio后向下取整；非负时int等于floor。按绝对值及原索引排序全部位置，选前k个，用掩码构造结果。100×0.29的数学结果是29，不能让浮点表示误差变成28。',
    '时间O(n log n)，空间O(n)；有界小数字符串的Fraction成本有界。','ratio不是阈值；并列要稳定按索引；计数指被选的位置而非最终零元素个数。',[
case('零值与并列','5 0.4\n3 1 0 -1 2\n','1 0 0 1 1\n3 0 0 -1 2\n',['int','float']),
case('零比例','2 0\n0 2\n','1 1\n0 2\n',['int','float']),case('全部剪枝','3 1\n2 -1 0\n','0 0 0\n0 0 0\n',['int','float']),
case('向下取整','3 0.5\n1 -1 1\n','0 1 1\n0 -1 1\n',['int','float']),
case('精确百分比','100 0.29\n'+' '.join(map(str,range(100)))+'\n',' '.join(['0']*29+['1']*71)+'\n'+' '.join(['0']*29+list(map(str,range(29,100))))+'\n',['int','float'])],mode='float')

add(73,'按行L1范数结构化剪枝','矩阵的每一行看作一个整体，L1范数为该行所有元素绝对值之和。保留范数最大的keep行；范数相同则较小索引优先保留。结果保留行按原行顺序输出。',
    '首行 rows cols keep；随后rows行，每行cols个权重。1≤rows,cols≤100，0≤keep≤rows。',
    '第一行rows个0/1掩码，1表示保留。后续恰好keep行输出保留的原始行，按索引升序；keep=0时仅输出掩码一行。',
    '三行范数是3、3、4，keep=2先留索引2，再在并列3中留索引0。掩码1 0 1，按原顺序输出行0、行2。',
    ['行L1是绝对值之和，不是普通和。','用(-norm,index)排序，选前keep个。','selected=set(order[:keep])；先打印掩码，再按原索引扫描只打印selected中的行。'],
    'Fraction精确累加行范数，避免数学上相等的十进制范数被误分出大小。按负范数及索引排序选择行，输出排序依据和最终输出顺序各有用途。',
    '时间O(rows*cols+rows log rows)，空间O(rows*cols+rows)；保留原矩阵以输出。','不能按普通行和排序；不能把排序后的行顺序直接作为结果；保留数0时不要输出空白数据行。',[
case('范数并列','3 2 2\n1 -2\n3 0\n2 2\n','1 0 1\n1 -2\n2 2\n',['int','float','float']),
case('不保留行','2 2 0\n1 2\n3 4\n','0 0\n',['int']),
case('全部保留','2 1 2\n-2\n0\n','1 1\n-2\n0\n',['int','float','float']),
case('全零并列','3 1 1\n0\n0\n0\n','1 0 0\n0\n',['int','float']),
case('小数范数精确并列','2 2 1\n0.1 0.2\n0.3 0\n','1 0\n0.1 0.2\n',['int','float'])],mode='float')

add(74,'对称int8量化与反量化','把浮点权重映射到整数[-127,127]。scale=max(abs(x))/127；全零向量规定scale=1。q=clip(round(x/scale),-127,127)，反量化x_hat=q*scale。round使用ties-to-even：恰处两整数中间时选偶数。',
    '首行 n；第二行n个权重。1≤n≤1000。用原始小数字符串构造Fraction，精确计算scale和x/scale后round；输出scale与反量化值可转float。',
    '第一行scale浮点；第二行n个整数q；第三行n个反量化浮点值。',
    '最大绝对值127，scale=1；±127映射原值，0.5→0，1.5→2，2.5→2，-0.5→0，-1.5→-2。ties-to-even不是一律四舍五入远离0。',
    ['先找maxabs，零向量需单独规定scale。','round(Fraction)可以精确实现ties-to-even；不要先把比值转float。','scale=maxabs/Fraction(127)或Fraction(1)；q=max(-127,min(127,round(x/scale)))；dequant=q*scale。'],
    'Fraction保存原十进制权重，scale与整数判定保持精确。Python对Fraction的round无ndigits时返回ties-to-even整数。显式截断满足范围契约，再用q*scale得到反量化值。输出整数行用str(q)，其余格式化float。',
    '有界小数字符串下时间O(n)，空间O(n)；Fraction位数运算成本由输入长度决定，不宣称无限精度操作常数。','对称范围使用-127而非-128；全零不能除0；0.3/127的scale应在整数判定前保持精确；实际量化还需保存scale元数据。',[
case('正负半格','8\n127 -127 0.5 1.5 2.5 -0.5 -1.5 0\n','1\n127 -127 0 2 2 0 -2 0\n127 -127 0 2 2 0 -2 0\n',['float','int','float']),
case('全部为零','3\n0 0 0\n','1\n0 0 0\n0 0 0\n',['float','int','float']),
case('精确小数半格','3\n0.3 0.15 -0.15\n','0.00236220472441\n127 64 -64\n0.3 0.151181102362 -0.151181102362\n',['float','int','float']),
case('单负值','1\n-2\n','0.0157480314961\n-127\n-2\n',['float','int','float']),
case('粗量化','3\n254 1 -3\n','2\n127 0 -2\n254 0 -4\n',['float','int','float'])],mode='float')

add(75,'仿射uint8量化与截断','给定正scale和整数zero_point，把权重量化到[0,255]：先求round(x/scale)（ties-to-even），再加zero_point，最后截断。反量化为(q-zero_point)*scale。顺序是本题契约，不能改成round(x/scale+zero_point)，奇数zero_point时半格结果可能不同。',
    '首行 n scale zero_point；第二行n个权重。1≤n≤1000，0<scale≤10000，0≤zero_point≤255。从原小数字符串用Fraction计算x/scale和round。',
    '第一行n个整数q；第二行n个反量化浮点值。',
    'scale=0.5，zero_point=128；比值[-2,-1,0,1,2]加128变成[126,127,128,129,130]，均未截断，反量化还原输入。',
    ['反量化先减zero_point。','小于0设0，大于255设255。','q=max(0,min(255,round(Fraction(x)/Fraction(scale))+zp))，再算(q-zp)*scale。'],
    '精确有理数计算比值并round，再加整数零点和截断。零点表示输入0对应的整数码。由于截断，极大或极小输入无法还原，不能对截断数据承诺半格误差界。',
    '有界输入长度下时间O(n)，空间O(n)。','ties-to-even与向远离0取整不同；先round再加零点；输出整数q而非浮点1.0；只有未截断值有scale/2误差界。',[
case('无误差整数格','5 0.5 128\n-1 -0.5 0 0.5 1\n','126 127 128 129 130\n-1 -0.5 0 0.5 1\n',['int','float']),
case('奇零点半格','6 0.1 1\n0.05 0.15 0.25 -0.05 -0.15 -0.25\n','1 3 3 1 0 0\n0 0.2 0.2 0 -0.1 -0.1\n',['int','float']),
case('双端截断','3 1 128\n-200 200 0\n','0 255 128\n-128 127 0\n',['int','float']),
case('零点为零','3 2 0\n-2 1 3\n','0 0 2\n0 0 4\n',['int','float']),
case('零点为255','3 2 255\n-3 -1 2\n','253 255 255\n-4 0 0\n',['int','float'])],mode='float')

add(76,'量化误差与理论存储字节','给定原值x与反量化值x_hat，计算MSE=Σ(x-x_hat)²/n与最大绝对误差max|x-x_hat|。再按FP32每项4字节、INT8每项1字节计算纯数组理论字节数；不计scale、零点、文件头、Python对象等元数据。',
    '首行 n；第二行n个原值；第三行n个反量化值。1≤n≤1000；输入最大绝对值10000。',
    '第一行 MSE max_abs_error 两个浮点；第二行 FP32_bytes INT8_bytes 两个整数。',
    '误差[-0.5,-1,1]的平方[0.25,1,1]，MSE=2.25/3=0.75，最大绝对误差1。n=3所以理论数据字节12与3。',
    ['误差绝对值与误差平方是两种统计。','MSE除以元素数n，不是除以worker数。','用Fraction计算每项差、平方和/n与最大abs；字节直接4*n和n。'],
    '原输入转Fraction，逐元素作差并归约。精确归约后再转float输出误差。存储模型是题目明确给出的理论数据体积，不能把Python列表sys.getsizeof当作此值。',
    '时间O(n)，空间O(n)存原值和误差；若流式读取可进一步减少，但当前实现未采用。','MSE不是平均绝对误差；不能漏除n；不计元数据必须注明；置零通常不改变稠密数组字节数，实际速度须另测。',[
case('混合误差','3\n1 -2 3\n1.5 -1 2\n','0.75 1\n12 3\n',['float','int']),
case('完全还原','2\n1 -1\n1 -1\n','0 0\n8 2\n',['float','int']),
case('单点误差','1\n0.3\n0.2\n','0.01 0.1\n4 1\n',['float','int']),
case('正负对称','2\n-0.5 0.5\n0 0\n','0.25 0.5\n8 2\n',['float','int']),
case('不等幅误差','4\n1 2 3 4\n1 1 3 2\n','1.25 2\n16 4\n',['float','int'])],mode='float')

add(77,'连续均衡数据分片','把编号0..n-1的样本依次分给workers个worker，形成连续区间。每个worker先得n//workers个，余数n%workers个依次给前面的worker，每个多1；允许空片。这里只模拟分片，不启动进程。',
    '一行 n workers。0≤n≤1000000，1≤workers≤1000。',
    '共workers行，每行 start end，表示半开区间[start,end)。空片start=end；不输出样本本身。',
    '10//3=3，余数1，所以长度4,3,3，区间[0,4)、[4,7)、[7,10)。end不属于该片。',
    ['除法的商给每人，余数给前面的人。','每个区间从上一片end开始。','base,extra=divmod(n,workers)；第i片length=base+(i<extra)，输出start,start+length，再移动start。'],
    '用divmod得到基础长度及额外名额，维护游标start。循环每个worker只输出两个边界，所以n很大也不必创建样本列表。',
    '时间O(workers)，输出缓存空间O(workers)；不创建长度n的数组。','最后一个样本编号n-1，而最后end为n；worker多于样本数时有空片；余数必须给前面的worker。',[
case('十样本三片','10 3\n','0 4\n4 7\n7 10\n'),case('整除','6 3\n','0 2\n2 4\n4 6\n'),
case('多worker空片','2 4\n','0 1\n1 2\n2 2\n2 2\n'),case('没有样本','0 2\n','0 0\n0 0\n'),
case('单worker','5 1\n','0 5\n')])

add(78,'等样本worker梯度平均','每个worker给出相同参数位置的局部平均梯度向量，且题面保证各worker样本数相等。逐参数求worker梯度的简单平均，这时也等于全体样本平均梯度。',
    '首行 workers dims；随后workers行，每行dims个局部平均梯度。1≤workers,dims≤100；各worker处理的样本数相等且正数。',
    '一行dims个全局平均梯度。',
    '两个worker梯度(1,3)和(5,-1)，逐坐标平均得到((1+5)/2,(3-1)/2)=(3,1)。',
    ['每个参数坐标分别聚合，不能先把向量变成标量。','所有worker相同样本数时，每个worker权重相同。','sum_grad[j]=sum(g[w][j] for w in workers)，最后除以workers一次。'],
    '逐行读梯度并给对应参数累加，用Fraction避免小数求和误差，再在最后除以worker数。参数维度不参与平均分母。',
    '时间O(workers*dims)，解析tokens空间O(workers*dims)，聚合数组O(dims)；当前raw.split会持有所有输入。','局部梯度已平均，不再除局部样本数；只有样本数相等才能简单平均；这是数值模拟，不实际调用DDP或测通信速度。',[
case('两维双worker','2 2\n1 3\n5 -1\n','3 1\n'),case('单worker','1 3\n2 -1 0\n','2 -1 0\n'),
case('正负抵消','3 1\n-3\n0\n3\n','0\n'),case('小数平均','2 1\n0.1\n0.2\n','0.15\n'),
case('三worker两维','3 2\n1 2\n4 5\n7 8\n','4 5\n')],mode='float')

add(79,'不同样本数的加权梯度','各worker输入一个样本数count和局部平均梯度向量。全局平均=Σ(count_w*g_w)/Σcount_w；count=0的worker忽略，即使其占位梯度非零也不贡献。总样本数保证大于0。',
    '首行 workers dims；随后workers行 count g1 ... gd。1≤workers,dims≤100，0≤count≤1000000，count为整数且总和>0。',
    '一行dims个样本加权全局平均梯度。',
    'worker0有1样本梯度(1,3)，worker1有3样本梯度(5,-1)。全局=(1*(1,3)+3*(5,-1))/4=(4,0)，不是简单平均(3,1)。',
    ['局部平均乘count才能还原局部梯度和。','先累加梯度和与样本数，最后统一除总样本数。','numerator[j]+=count*g[j]；total+=count；global[j]=numerator[j]/total。'],
    '每行样本数作为该梯度向量的权重。Fraction精确累加count*g，最后按总count归一化。零count自然贡献0，但仍按格式读完其占位向量。',
    '时间O(workers*dims)，tokens空间O(workers*dims)，聚合数组O(dims)。','权重是样本数不是worker编号；不要除worker数；不能忽略0样本行导致解析错位；输入已是局部平均。',[
case('样本不均衡','2 2\n1 1 3\n3 5 -1\n','4 0\n'),case('零权重忽略','2 1\n0 999\n4 -2\n','-2\n'),
case('相等样本','2 1\n2 1\n2 5\n','3\n'),case('单worker','1 2\n7 2 -3\n','2 -3\n'),
case('三方加权','3 1\n1 0\n2 3\n3 6\n','4\n')],mode='float')

add(80,'Microbatch累积与同步SGD','各worker把局部数据分成microbatch。每个microbatch提供样本数c与局部平均梯度g；把全部worker的全部microbatch累加Σc*g，再除全局样本总数一次，得到global_grad。所有梯度都在同一个旧参数theta上计算，最后只执行一次同步SGD：theta_new=theta-lr*global_grad。',
    '首行 workers dims lr；第二行dims个旧参数theta。随后按worker顺序：先一行该worker的microbatch数b，再b行 count g1 ... gd。1≤workers,dims≤100，0≤b≤100，0≤count≤1000000，0<lr≤1；全局count总和>0；允许b=0与count=0。',
    '第一行dims个全局平均梯度；第二行dims个更新后的参数。',
    'worker0的两批为1样本梯度2与3样本梯度4，worker1的一批2样本梯度8。加权和=2+12+16=30，总样本6，全局梯度5；theta=10，lr=0.1，只更新一次得到9.5。',
    ['不能按microbatch个数简单平均，因为每批大小可能不同。','跨worker仍用样本总数作分母，不能再次除worker数。','对所有批积累count*grad和total_count，末尾global=sum/total，new=theta-lr*global。'],
    'Fraction保存十进制参数与梯度，逐worker读取microbatch。数值上直接归约全局梯度和与总样本数，等价于每个worker先形成局部和再求和同步。最后统一更新参数，不在各microbatch后改变参数。',
    '令B为全部microbatch数，时间O(workers+B*dims)，tokens空间O(workers+B*dims)，聚合和参数数组O(dims)。','局部梯度已平均，要乘样本数还原和；不能除两次；worker空片合法；若梯度在不同参数处计算，不能再宣称等价于同一个全局大batch。教学模拟不启动分布式进程。',[
case('不等微批','2 1 0.1\n10\n2\n1 2\n3 4\n1\n2 8\n','5\n9.5\n'),
case('单worker单批','1 2 0.5\n1 -1\n1\n2 2 -4\n','2 -4\n0 1\n'),
case('空worker与零批权重','2 1 0.5\n4\n0\n2\n0 999\n2 6\n','6\n1\n'),
case('正负抵消','1 1 1\n3\n2\n2 4\n2 -4\n','0\n3\n'),
case('二维样本加权','2 2 0.25\n2 4\n1\n1 0 4\n1\n3 4 0\n','3 1\n1.25 3.75\n')],mode='float')

if __name__ == '__main__':
    materialize()
