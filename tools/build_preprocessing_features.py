"""Task 3 材料构建器。案例期望来自显式手算常量/定义；不运行参考答案。"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]
PRE = '03_preprocessing'
FEAT = '04_features'
DATA = {}

def add(pid, title, pairs, mode='float'):
    DATA[pid] = dict(title=title, mode=mode, pairs=pairs)

add(23, '均值填补缺失值', [
 ('3 2\n1 NA\n3 4\nNA 8\n','1 6\n3 4\n2 8\n'),
 ('2 2\nNA 2\nNA 4\n','0 2\n0 4\n'),
 ('1 1\nNA\n','0\n'),
 ('2 1\n-2\n2\n','-2\n2\n'),
 ('3 1\nNA\n-6\nNA\n','-6\n-6\n-6\n')])
add(24, '按首次出现稳定去重', [
 ('5 2\n2 1\n1 2\n2 1\n1 2\n3 3\n','3\n2 1\n1 2\n3 3\n'),
 ('1 1\n7\n','1\n7\n'),
 ('3 1\n0\n0\n0\n','1\n0\n'),
 ('3 1\n3\n2\n1\n','3\n3\n2\n1\n'),
 ('4 2\n-1 0\n0 -1\n-1 0\n-1 1\n','3\n-1 0\n0 -1\n-1 1\n')], 'int')
add(25, 'Min-Max 列缩放', [
 ('3 2\n0 7\n5 7\n10 7\n','0 0\n0.5 0\n1 0\n'),
 ('1 2\n3 -8\n','0 0\n'),
 ('3 1\n-4\n-2\n0\n','0\n0.5\n1\n'),
 ('2 2\n4 8\n2 10\n','1 0\n0 1\n'),
 ('3 1\n0.1\n0.2\n0.3\n','0\n0.5\n1\n')])
add(26, '总体 Z-score 标准化', [
 ('2 2\n2 8\n4 8\n','-1 0\n1 0\n'),
 ('1 1\n9\n','0\n'),
 ('3 1\n-1\n0\n1\n', f'{-math.sqrt(1.5)}\n0\n{math.sqrt(1.5)}\n'),
 ('2 2\n10 -4\n0 0\n','1 -1\n-1 1\n'),
 ('4 1\n1\n1\n3\n3\n','-1\n-1\n1\n1\n')])
add(27, '先划分再拟合训练统计量', [
 ('4 1 2\n0\n10\n100\n5\n0 1 2 3\n','0\n1\n10\n0.5\n'),
 ('3 1 2\n0\n10\n5\n2 1 0\n','0\n1\n-1\n'),
 ('2 2 1\n2 3\n9 8\n0 1\n','0 0\n0 0\n'),
 ('3 2 2\n0 7\n2 7\n4 8\n0 1 2\n','0 0\n1 0\n2 0\n'),
 ('3 1 2\n-3\n-1\n-5\n0 1 2\n','0\n1\n-1\n')])
add(28, '确定性类别过采样', [
 ('3 1 3 2\n0 10\n1 20\n0 30\n','5\n0 10\n1 20\n0 30\n0 10\n1 20\n'),
 ('2 1 1 1\n0 1\n1 2\n','2\n0 1\n1 2\n'),
 ('2 1 4 1\n0 7\n1 8\n','5\n0 7\n1 8\n0 7\n0 7\n0 7\n'),
 ('3 1 1 4\n1 3\n0 2\n1 5\n','5\n1 3\n0 2\n1 5\n1 3\n1 5\n'),
 ('2 2 2 2\n0 -1 2\n1 4 6\n','4\n0 -1 2\n1 4 6\n0 -1 2\n1 4 6\n')])
add(29, 'SMOTE 线段插值', [
 ('2\n1 3\n5 7\n0.25\n','2 4\n'),
 ('1\n-2\n8\n0\n','-2\n'),
 ('1\n-2\n8\n1\n','8\n'),
 ('2\n3 3\n3 3\n0.8\n','3 3\n'),
 ('3\n0 2 -4\n4 -2 0\n0.5\n','2 0 -2\n')])
add(30, '小型确定性 SMOTE', [
 ('5 1 1 2\n1 0\n0 1\n1 10\n0 2\n0 3\n0 0.5\n0 0.25\n','5\n7.5\n'),
 ('5 1 1 1\n0 50\n1 2\n0 2\n1 6\n0 3\n0 0\n','2\n'),
 ('5 1 1 1\n0 50\n1 2\n0 2\n1 6\n0 3\n0 1\n','6\n'),
 ('7 1 2 3\n1 0\n1 -2\n1 2\n0 0.1\n0 0.2\n0 0.3\n0 0.4\n0 0.5\n1 0.5\n0 0.5\n','-1\n0\n1\n'),
 ('5 2 1 3\n0 0 0\n1 1 1\n0 0 4\n1 2 2\n1 3 3\n0 0.25\n0 0.5\n0 0.75\n','0 1\n0 2\n0 3\n')])
add(31, '原始词频 TF', [
 ('3\npear apple cat\napple pear apple\n','2 0 1\n'),
 ('1\nx\nx x x\n','3\n'),
 ('2\nb a\n\n','0 0\n'),
 ('3\na b c\nc c b\n','0 1 2\n'),
 ('2\nred blue\nblue red blue red\n','2 2\n')], 'int')
idf2 = 1 + math.log(3/2)
idf3 = 1 + math.log(4/2)
add(32, '平滑 IDF', [
 ('2 3\npear apple cat\napple pear\napple\n',f'1 {1+math.log(3)} {idf2}\n'),
 ('1 1\nx\nx x x\n','1\n'),
 ('2 2\nb a\n\n\n',f'{1+math.log(3)} {1+math.log(3)}\n'),
 ('3 2\na b\na a\na\nb\n',f'{1+math.log(4/3)} {idf3}\n'),
 ('1 2\nb a\nb\n',f'{1+math.log(2)} 1\n')])
add(33, 'TF-IDF 与 L2 归一化', [
 ('2 2 0\nb a\na a b\na\n',f'2 {idf2}\n1 0\n'),
 ('1 2 1\nb a\na b\n',f'{1/math.sqrt(2)} {1/math.sqrt(2)}\n'),
 ('2 2 1\na b\n\n\n','0 0\n0 0\n'),
 ('2 1 1\nx\nx x x\nx\n','1\n1\n'),
 ('2 2 1\na b\na a\nb\n','1 0\n0 1\n')])
add(34, '等宽分箱', [
 ('5 2\n0 1 2 3 4\n','0 0 1 1 1\n'),
 ('3 4\n7 7 7\n','0 0 0\n'),
 ('4 1\n-3 0 2 9\n','0 0 0 0\n'),
 ('5 4\n4 3 2 1 0\n','3 3 2 1 0\n'),
 ('3 2\n-2 -1 0\n','0 1 1\n')], 'int')
add(35, '按秩等频分组', [
 ('5 2\n5 1 3 2 4\n','1 0 0 0 1\n'),
 ('4 2\n7 7 7 7\n','0 0 1 1\n'),
 ('3 3\n3 1 2\n','2 0 1\n'),
 ('3 1\n9 -1 4\n','0 0 0\n'),
 ('5 3\n2 1 2 1 2\n','1 0 1 0 2\n')], 'int')
add(36, '二分类列联表卡方值', [
 ('10 0\n0 10\n','20\n'),
 ('2 2\n3 3\n','0\n'),
 ('0 0\n0 0\n','0\n'),
 ('0 3\n0 7\n','0\n'),
 ('1 1\n0 2\n',f'{4/3}\n')])
add(37, '相邻卡方合并分箱', [
 ('3 2\n1 1 1\n2 2 2\n3 8 0\n','1 2 3 3\n3 3 8 0\n'),
 ('3 2\n1 1 1\n2 1 1\n3 1 1\n','1 2 2 2\n3 3 1 1\n'),
 ('3 1\n-1 0 2\n0 3 0\n5 1 1\n','-1 5 4 3\n'),
 ('2 2\n1 0 0\n4 2 3\n','1 1 0 0\n4 4 2 3\n'),
 ('4 2\n0 1 0\n1 2 0\n2 0 1\n3 0 2\n','0 1 3 0\n2 3 0 3\n')])
add(38, '中位数与 MAD 鲁棒特征', [
 ('1 2 3 100\n','2.5 1\n-1.5 -0.5 0.5 97.5\n'),
 ('7\n','7 0\n0\n'),
 ('1 1 1 9\n','1 0\n0 0 0 0\n'),
 ('-3 -1 1\n','-1 2\n-1 0 1\n'),
 ('11 12 13 110\n','12.5 1\n-1.5 -0.5 0.5 97.5\n')])

def path(pid):
    return ROOT / 'chapters' / (PRE if pid <= 30 else FEAT) / 'problems' / f'P{pid:03}'

def write_cases():
    for pid, data in DATA.items():
        folder = path(pid)
        folder.mkdir(parents=True, exist_ok=True)
        cases = [dict(name=f'独立案例{i+1}', input=stdin, expected=expected)
                 for i, (stdin, expected) in enumerate(data['pairs'])]
        (folder / 'cases.json').write_text(json.dumps(dict(id=f'P{pid:03}',
            chapter='03' if pid <= 30 else '04', title=data['title'], mode=data['mode'],
            requires=[], cases=cases), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

MATERIAL = {}
PRE_SOURCE = 'https://scikit-learn.org/stable/modules/preprocessing.html'
TEXT_SOURCE = 'https://scikit-learn.org/stable/modules/feature_extraction.html#tf-idf-term-weighting'
SMOTE_SOURCE = 'https://imbalanced-learn.org/stable/over_sampling.html#sample-generation'

def material(pid, rule, input_spec, output_spec, hand, hints, complexity, pitfalls, code, source=PRE_SOURCE):
    MATERIAL[pid] = locals()

def write_materials(ids):
    for pid in ids:
        m = MATERIAL[pid]
        data = DATA[pid]
        name = f'P{pid:03}'
        folder = path(pid)
        stdin, stdout = data['pairs'][0]
        next_link = f'../P{pid+1:03}/README.md' if pid not in (30, 38) else '../../README.md'
        hints = '\n\n'.join(f'<details><summary>提示 {i}</summary>\n\n{h}\n\n</details>' for i, h in enumerate(m['hints'], 1))
        readme = f'''# {name} {data['title']}

{m['rule']}

## 输入与约束

{m['input_spec']}

## 输出

{m['output_spec']} 浮点结果允许绝对或相对误差 1e-6。整数题须输出整数。

## 样例

输入：
```text
{stdin.rstrip()}
```
输出：
```text
{stdout.rstrip()}
```

手算：{m['hand']}

## 分级提示

{hints}

## 运行与检查

在仓库根目录，用普通文本填写输入（空文档保留空行），运行：
```powershell
.\\.venv\\Scripts\\python.exe chapters/{PRE if pid <= 30 else FEAT}/problems/{name}/exercise.py
.\\.venv\\Scripts\\python.exe check.py {name}
```

终端输入结束时，Windows 使用 Ctrl+Z 后回车；也可把输入保存为 UTF-8 文本并用 `Get-Content input.txt | .\\.venv\\Scripts\\python.exe chapters/{PRE if pid <= 30 else FEAT}/problems/{name}/exercise.py`。不要输出提示文字。

定义核对：[一手资料]({m['source']})。本题规则和确定性边界以题面为准，参考代码自行编写。

[下一题或章节入口]({next_link}) · [题解](../../../../solutions/{name}.md)
'''
        folder.joinpath('README.md').write_text(readme, encoding='utf-8')
        exercise = f'''"""{name} {data['title']}：先阅读同目录 README.md。"""
import sys


def solve(raw):
    # raw 是全部普通文本输入。用 splitlines() 保留空文档，用 split() 读取数值。
    # 输入格式：{m['input_spec']}
    # TODO 1：{m['hints'][0]}
    # TODO 2：完成题目要求的计算，遇到约定的特殊情况先处理。
    # TODO 3：把各行转成字符串，再用 "\\n" 连接；保持输出行列形状。
    raise NotImplementedError("请按题目提示完成这里")



if __name__ == '__main__':
    answer = solve(sys.stdin.read())
    print(answer)
'''
        folder.joinpath('exercise.py').write_text(exercise, encoding='utf-8')
        code = '"""'+ name + '：独立参考解。"""\nimport sys\nimport math\n\n\ndef format_row(values):\n    return " ".join(format(v, ".12g") for v in values)\n\n\n# 算法关键：' + m['hints'][2] + '\n' + m['code'].strip() + '\n\n\nif __name__ == "__main__":\n    print(solve(sys.stdin.read()))\n'
        ROOT.joinpath('solutions', name+'.py').write_text(code, encoding='utf-8')
        ROOT.joinpath('solutions', name+'.md').write_text(f'''# {name} {data['title']}题解

思路：{m['rule']}

关键步骤：{m['hints'][2]}

样例核对：{m['hand']}

复杂度（对应本参考实现）：{m['complexity']}

易错点：{m['pitfalls']}

[独立参考代码]({name}.py) · [返回题面](../chapters/{PRE if pid <= 30 else FEAT}/problems/{name}/README.md)

来源：[定义核对的一手资料]({m['source']})。本题为原创教学练习；来源用于定义与实现思路核对，参考代码独立编写。
''', encoding='utf-8')
    ROOT.joinpath('docs/work/task-3-checkpoint.md').write_text(
        '# Task 3 恢复检查点\n\nRED 已重跑并保存 task-3-red.txt（6 tests，85 failures，缺少参考解）。\n\n'
        + '已落盘材料：' + ', '.join(f'P{p:03}' for p in sorted(MATERIAL) if ROOT.joinpath('solutions', f'P{p:03}.py').exists())
        + '\n\n尚需最终 checker、独立性质、文档与结构审计。\n', encoding='utf-8')

material(23, '逐列计算非 NA 元素的算术均值，用该均值填补本列 NA；整列缺失时填 0。保持行列顺序。',
 '首行 n d；随后 n 行，每行 d 个实数或大写 NA。1≤n≤200，1≤d≤20；实数绝对值≤1000000。',
 '输出填补后的 n 行 d 列矩阵。', '第1列已知1和3，均值2；第2列已知4和8，均值6；只替换 NA。',
 ['按列收集非缺失值。', '均值是总和除以有效个数，不能把 NA 算入分母。', '先求每列均值（空列置0），再逐行用均值替换 NA。'],
 '时间 O(nd)，空间 O(nd)，保存原矩阵及输出。', '不能按行求均值；整列缺失不能除以0。', '''def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [line.split() for line in lines[1:n+1]]
    means = []
    for j in range(d):
        values = [float(row[j]) for row in rows if row[j] != 'NA']
        means.append(sum(values) / len(values) if values else 0.0)
    # 缺失位置才替换；已知值原样保留。
    return '\\n'.join(format_row(means[j] if row[j] == 'NA' else float(row[j])
                                for j in range(d)) for row in rows)''',
 'https://scikit-learn.org/stable/modules/impute.html')

material(24, '把每行当作一个整数样本，删除重复行，保留各不同样本第一次出现的位置顺序。',
 '首行 n d；随后 n 行，每行 d 个整数。1≤n≤200，1≤d≤20，整数绝对值≤1000000。',
 '首行输出不同样本数，再输出保留的样本，每行 d 个整数。', '2 1 和 1 2 第二次出现时跳过，保留第1、2、5行，共3行。',
 ['准备一个已见集合和一个结果列表。', '列表不能直接放入 set，可把每行转成 tuple。', '按输入顺序遍历；行元组未见过才加入集合与结果列表。'],
 '平均时间 O(nd)，空间 O(nd)；假定集合查找平均 O(1)，元组散列需 O(d)。', '只用 set 输出会丢失题目要求的顺序；一行不同于另一行的排列。', '''def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    seen = set()
    kept = []
    for line in lines[1:n+1]:
        row = tuple(map(int, line.split()))
        if row not in seen:
            seen.add(row)
            kept.append(row)
    return '\\n'.join([str(len(kept))] + [' '.join(map(str, row)) for row in kept])''',
 'https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset')

material(25, '逐列计算 (x-min)/(max-min)，把每列缩放到 [0,1]；常量列（max=min）所有输出均为0。',
 '首行 n d；随后 n 行，每行 d 个实数。1≤n≤200，1≤d≤20；绝对值≤1000000。',
 '输出 n 行 d 列缩放结果。', '第1列 min=0,max=10，得到0、0.5、1；第2列全是7，得到0。',
 ['列最大值与最小值分别计算。', '分母是最大值减最小值；若为0，直接输出0。', '缓存各列 min/max，再逐元素套公式，常量分支避免除0。'],
 '时间 O(nd)，空间 O(nd)，含输入及输出矩阵。', '不是除以最大值；常量列规则是本题明确的约定。', '''def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [list(map(float, line.split())) for line in lines[1:n+1]]
    low = [min(row[j] for row in rows) for j in range(d)]
    high = [max(row[j] for row in rows) for j in range(d)]
    return '\\n'.join(format_row(0.0 if high[j] == low[j] else
                      (row[j]-low[j])/(high[j]-low[j]) for j in range(d)) for row in rows)''')

material(26, '逐列求均值 μ 与总体标准差 σ=sqrt(Σ(x-μ)²/n)，输出 (x-μ)/σ。常量列输出0。',
 '首行 n d；随后 n 行，每行 d 个实数。1≤n≤200，1≤d≤20；绝对值≤1000000。',
 '输出 n 行 d 列标准化结果。', '第1列均值3，平方偏差为1和1，总体方差1，标准差1，所以-1、1。第2列常量8，输出0。',
 ['先计算每列均值。', '用偏离均值的平方求方差，分母为 n，最后开平方。', '缓存 μ 和 σ；σ=0 的列输出0，其他列用 (x-μ)/σ。'],
 '时间 O(nd)，空间 O(nd)。', '本题分母为 n 而非 n-1；标准化不会自动使分布成为正态分布。', '''def solve(raw):
    lines = raw.splitlines()
    n, d = map(int, lines[0].split())
    rows = [list(map(float, line.split())) for line in lines[1:n+1]]
    means = [sum(row[j] for row in rows)/n for j in range(d)]
    stds = [math.sqrt(sum((row[j]-means[j])**2 for row in rows)/n) for j in range(d)]
    return '\\n'.join(format_row(0.0 if stds[j] == 0 else (row[j]-means[j])/stds[j]
                                for j in range(d)) for row in rows)''')

material(27, '按给定下标排列样本：前 t 个为训练集，余下为验证集。仅用训练集逐列 min/max 做 Min-Max；训练常量列在两集合中都输出0。验证值不裁剪，可小于0或大于1。',
 '首行 n d t；随后 n 行 d 个实数；最后一行 n 个互异下标，恰好是0到n-1的排列。2≤n≤200，1≤d≤20，1≤t<n；实数绝对值≤1000000。',
 '按给定排列输出全部 n 行，先训练后验证，无标签或空行。', '排列0 1 2 3，训练值0和10给出 min=0,max=10；验证100变成10，验证5变成0.5。若先用100求最大值，就泄漏了验证集信息。',
 ['按照下标排列，取前 t 行作为训练。', '只在训练行上求统计量，但把同一组统计量应用到全部行。', '缓存训练 min/max；遍历排列逐行缩放，常量列输出0，验证结果不裁剪。'],
 '时间 O(nd)，空间 O(nd)。', '不能在整个数据上拟合；输出顺序是排列顺序；训练常量列规则是教学约定。', '''def solve(raw):
    lines = raw.splitlines()
    n, d, t = map(int, lines[0].split())
    rows = [list(map(float, line.split())) for line in lines[1:n+1]]
    order = list(map(int, lines[n+1].split()))
    training = [rows[i] for i in order[:t]]
    low = [min(row[j] for row in training) for j in range(d)]
    high = [max(row[j] for row in training) for j in range(d)]
    # 验证行参与变换，但不参与统计量估计。
    return '\\n'.join(format_row(0.0 if high[j] == low[j] else
                      (rows[i][j]-low[j])/(high[j]-low[j]) for j in range(d)) for i in order)''',
 'https://scikit-learn.org/stable/common_pitfalls.html#data-leakage')

material(28, '二分类标签为0或1。保留全部原样本，再先补标签0、后补标签1到指定目标数。每类从其原始样本列表的第一个开始循环复制，不使用新复制的样本作为循环列表。',
 '首行 n d target0 target1；随后 n 行：标签与 d 个整数特征。2≤n≤200，1≤d≤20；两类都至少1条；各 target 在该类原始数到500之间，特征绝对值≤1000000。',
 '首行输出总数 target0+target1，其后输出原样本及按规则追加的样本，每行先标签再特征。', '原0类有10和30，目标3，追加10；原1类有20，目标2，追加20。先输出原3行，再追加0 10和1 20，共5行。',
 ['分别记录两类原样本，保持各自输入顺序。', '还需增加 target-原数 条；第 r 条复制原列表 r % 原数 位置。', '先复制原输出列表，再按类0、类1循环补足；首行输出最终行数。'],
 '设 T=target0+target1，时间 O(Td)，空间 O(Td)。', '这只是复制，不能增加独立信息；目标不小于原数；不要删减或打乱原样本。', '''def solve(raw):
    lines = raw.splitlines()
    n, d, target0, target1 = map(int, lines[0].split())
    rows = [tuple(map(int, line.split())) for line in lines[1:n+1]]
    groups = [[row for row in rows if row[0] == label] for label in (0, 1)]
    output = rows.copy()
    for label, target in enumerate((target0, target1)):
        originals = groups[label]
        for r in range(target-len(originals)):
            output.append(originals[r % len(originals)])
    return '\\n'.join([str(len(output))] + [' '.join(map(str, row)) for row in output])''', SMOTE_SOURCE)

material(29, '给定同一类别的基点 x、邻点 z 和系数 λ，计算新样本 x+λ(z-x)，即线段插值。本题只做插值，不查找邻居。',
 '首行维数 d；第2行 d 个实数 x；第3行 d 个实数 z；第4行 λ。1≤d≤20，0≤λ≤1，特征绝对值≤1000000。',
 '一行 d 个新样本特征，不输出标签。', 'λ=0.25，差向量(4,4)，乘系数得(1,1)，加基点(1,3)得(2,4)。',
 ['逐坐标处理，所有坐标使用同一个 λ。', '差向量是邻点减基点，方向别反过来。', '使用 [x[j]+λ*(z[j]-x[j]) for j in range(d)]；λ=0返回x，λ=1返回z。'],
 '时间 O(d)，空间 O(d)。', '不是 x+λz；λ不是距离；不能给每个坐标随机系数。', '''def solve(raw):
    lines = raw.splitlines()
    d = int(lines[0])
    x = list(map(float, lines[1].split()))
    z = list(map(float, lines[2].split()))
    lam = float(lines[3])
    return format_row(x[j]+lam*(z[j]-x[j]) for j in range(d))''', SMOTE_SOURCE)

material(30, '实现完整小型 SMOTE 的确定性教学版。少数类是原始样本数较少的类别（本题禁止并列）。按其输入顺序列为 minority。对每个少数类基点，只在其余少数类原样本内求平方欧氏距离；按 (距离, 原始输入下标) 升序取前 k 个邻居。第 r 条新样本以 minority[r % m] 为基点，使用该条输入的邻居名次 q（0起）和 λ 做 x+λ(z-x)。新样本不加入邻居搜索。',
 '首行 n d k g；随后 n 行：0/1标签及 d 个实数特征；再有 g 行：q λ。5≤n≤200，1≤d≤20，1≤g≤200；两类均存在且样本数不等；少数类数 m≥2；1≤k≤m-1，0≤q<k，0≤λ≤1，特征绝对值≤1000000。',
 '只输出生成的 g 行特征，每行 d 个数，不输出原样本、行数或标签。', '少数类为1，其点按输入顺序是0、10；k=1时互为唯一邻居。第0条以0为基点，λ=0.5得5；第1条以10为基点，λ=0.25得7.5。多数类1、2、3不参与。',
 ['统计两类数目，取少数类，保留原始下标用于距离并列。', '针对每个少数类基点排序其他少数类点；不需要开平方，平方距离的顺序相同。', '预存每个基点前 k 个邻居；第 r 条使用 r % m 基点与输入 q 邻居，再做统一系数插值。'],
 '设少数类数 m，时间 O(nd + m²d + m² log m + gd)，空间 O(nd + mk + gd + m)；逐基点排序临时距离表，不保留全距离矩阵。', '多数类距离再近也不可用；排除自身而非排除所有同坐标点；并列按原始下标；k合法最小值1、m合法最小值2均覆盖。', '''def solve(raw):
    lines = raw.splitlines()
    n, d, k, g = map(int, lines[0].split())
    samples = []
    for i, line in enumerate(lines[1:n+1]):
        parts = line.split()
        samples.append((int(parts[0]), list(map(float, parts[1:])), i))
    counts = [sum(label == c for label, _, _ in samples) for c in (0, 1)]
    minority_label = 0 if counts[0] < counts[1] else 1
    minority = [(x, index) for label, x, index in samples if label == minority_label]
    neighbors = []
    for a, (x, original_index) in enumerate(minority):
        distances = []
        for b, (z, neighbor_index) in enumerate(minority):
            if a != b:  # 只排除同一个样本，重复坐标仍然合法。
                dist = sum((x[j]-z[j])**2 for j in range(d))
                distances.append((dist, neighbor_index, b))
        distances.sort()
        neighbors.append([b for _, _, b in distances[:k]])
    output = []
    for r, line in enumerate(lines[n+1:n+1+g]):
        q_text, lam_text = line.split()
        q, lam = int(q_text), float(lam_text)
        base = r % len(minority)
        x = minority[base][0]
        z = minority[neighbors[base][q]][0]
        output.append(format_row(x[j]+lam*(z[j]-x[j]) for j in range(d)))
    return '\\n'.join(output)''', SMOTE_SOURCE)


material(31, '给定词表和一篇文档，计算原始词频 TF：每个词在文档中出现的次数。词表按字典序输出，不按输入词表顺序。按空白分词，大小写敏感，不做分词模型或标点处理。',
 '首行 v；第2行 v 个互异小写英文字母串，长度1到20；第3行为文档（可为空行）。1≤v≤100；文档最多2000个词，所有词都在词表中。',
 '一行 v 个整数，依词表字典序排列。', '输入词表 pear apple cat 排序为 apple cat pear；文档 apple pear apple 对应词频2、0、1。',
 ['先把词表排序，文档用 split() 分成词。', '用字典累计计数，未出现词计数为0。', '遍历文档对 counts[word] 加1；最后按 sorted(vocab) 查询 counts.get(word,0)。'],
 '设词数 L、词表大小 v，时间 O(L+v log v)，空间 O(L+v)（含输入分词列表），忽略有界词长。', '本题 TF 是原始计数，未除以文档长度；空文档是0向量；词频不同于文档频率。', '''def solve(raw):
    lines = raw.splitlines()
    v = int(lines[0])
    vocab = sorted(lines[1].split())
    words = lines[2].split() if len(lines) > 2 else []
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return ' '.join(str(counts.get(word, 0)) for word in vocab)''', TEXT_SOURCE)

material(32, '给定 n 篇文档，df(w) 是含词 w 的文档篇数（同篇重复只计1）。平滑 IDF(w)=ln((1+n)/(1+df(w)))+1，ln 为自然对数。词表按字典序排列，词表中的词可完全不出现。',
 '首行 n v；第2行 v 个互异小写英文字母串，长度1到20；随后 n 行为文档，空行表示空文档。1≤n≤100，1≤v≤100；所有文档合计最多2000词，均在词表中。按空白分词。',
 '一行 v 个 IDF，按词表字典序。', '两篇 apple pear、apple：apple的df=2，IDF=1；cat的df=0，IDF=ln3+1≈2.098612；pear的df=1，IDF=ln(3/2)+1≈1.405465。',
 ['对每篇文档先去重，再增加文档频率。', 'n 是包括空文档的篇数；公式分子分母均加1，结果再加1。', 'df初始化为0，遍历 set(文档词) 对df加1；按字典序代入 math.log((1+n)/(1+df))+1。'],
 '设文档总词数 L，时间 O(L+v log v)，空间 O(L+n+v)，含输入文本与各篇分词临时集合；忽略有界词长。', '出现3次不等于df为3；不要用log10；df=0也合法，不需要除0分支。', '''def solve(raw):
    lines = raw.splitlines()
    n, v = map(int, lines[0].split())
    vocab = sorted(lines[1].split())
    df = {word: 0 for word in vocab}
    for line in lines[2:2+n]:
        for word in set(line.split()):
            df[word] += 1
    return format_row(math.log((1+n)/(1+df[word]))+1 for word in vocab)''', TEXT_SOURCE)

material(33, '对 n 篇文档计算 TF-IDF：TF为原始词次数，IDF=ln((1+n)/(1+df))+1，df为出现该词的文档篇数。按给定词表的字典序排列向量。若 norm=1，每篇向量除以自身 L2 范数 sqrt(Σa²)；若范数0则保留全0。norm=0时直接输出权重。',
 '首行 n v norm（norm为0或1）；第2行 v 个互异小写英文字母串，长度1到20；随后 n 行文档，可为空行。1≤n≤100，1≤v≤100；总词数≤2000，词均在词表中，按空白分词。',
 '输出 n 行 v 列，行顺序与文档一致。', '词表 b a 排为 a b；a出现两篇IDF=1，b只出现一篇IDF≈1.405465。norm=0，所以第1篇权重(2,1.405465)，第2篇(1,0)。若norm=1，第1篇除以sqrt(4+1.405465²)。',
 ['先处理整个语料，得出各词df与IDF。', '每篇TF独立统计，再逐词乘IDF；L2归一化是按行做的。', '存各篇计数字典；由计数字典的键累计df；逐行造TF×IDF向量，norm=1且模长>0时除以模长。'],
 '设总词数 L，时间 O(L+v log v+nv)，空间 O(L+nv+n+v)，包含分词、计数字典与格式化输出；忽略有界词长。', '先乘IDF再归一化；空文档不是NaN；没有除以词数；实际验证集应沿用训练语料拟合的词表和IDF，本题仅给一个拟合语料。', '''def solve(raw):
    lines = raw.splitlines()
    n, v, norm = map(int, lines[0].split())
    vocab = sorted(lines[1].split())
    docs = []
    df = {word: 0 for word in vocab}
    for line in lines[2:2+n]:
        counts = {}
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1
        docs.append(counts)
        for word in counts:  # 字典键只出现一次，所以是文档频率。
            df[word] += 1
    idf = [math.log((1+n)/(1+df[word]))+1 for word in vocab]
    output = []
    for counts in docs:
        vector = [counts.get(word, 0)*weight for word, weight in zip(vocab, idf)]
        length = math.sqrt(sum(x*x for x in vector))
        if norm == 1 and length > 0:
            vector = [x/length for x in vector]
        output.append(format_row(vector))
    return '\\n'.join(output)''', TEXT_SOURCE)

material(34, '把 [min,max] 分成 k 个等宽箱，编号0到k-1。非最后箱左闭右开，最后箱包含max；内部边界上的值归右箱。常量数据全部归0号箱。',
 '首行 n k；第2行 n 个整数。1≤n≤200，1≤k≤200，值绝对值≤1000000。k可以大于n，因此空箱合法。',
 '一行 n 个箱号，按原输入顺序。', 'min=0,max=4,k=2，宽度2；箱0为[0,2)，箱1为[2,4]，故0、1归0，2、3、4归1。',
 ['求最小、最大值，先处理全部相等情况。', '可用整数计算 floor((x-min)*k/(max-min))，最大值的结果k要改成k-1。', '每个整数x的箱号是 min(k-1,(x-low)*k//(high-low))；常量时全0。'],
 '时间 O(n)，空间 O(n)。', '箱的宽度相等不保证样本数相等；max必须包含；本题整数输入可避免边界浮点误差。', '''def solve(raw):
    lines = raw.splitlines()
    n, k = map(int, lines[0].split())
    values = list(map(int, lines[1].split()))
    low, high = min(values), max(values)
    if low == high:
        bins = [0]*n
    else:
        bins = [min(k-1, (x-low)*k//(high-low)) for x in values]
    return ' '.join(map(str, bins))''', PRE_SOURCE+'#discretization')

material(35, '本题采用按秩分组的等频教学规则：按 (值, 原始下标) 升序稳定排序；从0开始的秩 r 分到 floor(r*k/n) 号组；再恢复输入顺序。重复值按原始下标打破并列，同值可分到不同组，因此这不是只由数值边界决定的区间分箱。每组数量最多相差1，不保证完全相等。',
 '首行 n k；第2行 n 个整数。1≤n≤200，1≤k≤n，值绝对值≤1000000。',
 '一行 n 个组号（0到k-1），顺序与原数据相同。', '排序后的(值,下标)为(1,1),(2,3),(3,2),(4,4),(5,0)；秩0、1、2归0，秩3、4归1；恢复后得到1 0 0 0 1。',
 ['排序时保留原始位置。', '组号由秩决定，不是直接由值决定；重复值也有不同秩。', '排序 enumerate(values) 为 (value,index) 顺序；对秩r把 r*k//n 写入结果的原始index。'],
 '时间 O(n log n)，空间 O(n)。', '不能把同值全部放同一箱又声称严格等频；本规则可拆同值，与一些库的分位数边界实现不同；无法只靠箱边界给新值分组。', '''def solve(raw):
    lines = raw.splitlines()
    n, k = map(int, lines[0].split())
    values = list(map(int, lines[1].split()))
    ordered = sorted((value, index) for index, value in enumerate(values))
    groups = [0]*n
    for rank, (value, index) in enumerate(ordered):
        groups[index] = rank*k//n
    return ' '.join(map(str, groups))''', PRE_SOURCE+'#discretization')

CHI_SOURCE = 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.contingency.chi2_contingency.html'
MAD_SOURCE = 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median_abs_deviation.html'
CHI_FUNCTION = '''from fractions import Fraction


def chi_square(table):
    total = sum(sum(row) for row in table)
    if total == 0:
        return Fraction(0)
    row_sums = [sum(row) for row in table]
    col_sums = [table[0][j]+table[1][j] for j in range(2)]
    answer = Fraction(0)
    for i in range(2):
        for j in range(2):
            expected = Fraction(row_sums[i]*col_sums[j], total)
            if expected != 0:  # 题面约定：期望为0项贡献0。
                answer += (table[i][j]-expected)**2/expected
    return answer
'''

material(36, '输入2×2列联表，行是两组，列是标签0和1；各格 O 为样本数。总数 N、行和 R、列和 C；期望 E=R*C/N。计算 Pearson χ²=Σ(O-E)²/E，不做连续性（Yates）修正。N=0时输出0，E=0的项约定贡献0。本题只算统计量，不求p值或判断显著性。',
 '两行，每行两个非负整数，表示对应组的0类和1类数量；每个数≤1000000。',
 '一行一个卡方统计量。', '表[[10,0],[0,10]]：N=20，两行和、两列和都是10，各E=5；四格各贡献(10-5)²/5或(0-5)²/5=5，总和20。',
 ['先计算总数、两行和、两列和。', '每格期望由所在行和×所在列和/总数给出。', '遍历4格并累加(O-E)²/E；N=0直接0，E=0跳过；参考解用Fraction计算精确有理数，最后转浮点输出。'],
 '固定4格，时间和空间 O(1)，按题面有界整数算术计。', '不能把行和当期望；不调用默认可能含Yates修正的库函数；0期望处理为本题教学约定，不用于推断统计有效性。', CHI_FUNCTION+'''

def solve(raw):
    table = [list(map(int, line.split())) for line in raw.splitlines()]
    return format_row([float(chi_square(table))])''', CHI_SOURCE)

material(37, '给定按数值递增的初始箱，每箱有0类和1类计数。对每对相邻箱构成2×2列联表，按P036的未修正Pearson公式算χ²，期望为0项贡献0。每轮合并χ²最小的一对；精确相等时选最左一对。合并后左界取左箱左界，右界取右箱右界，两类计数相加；重新计算所有邻对，直到剩 t 箱。这是明确定义的教学变体，不宣称任何库的唯一默认算法。',
 '首行 b t；随后 b 行：value count0 count1。1≤b≤200，1≤t≤b；value为严格递增互异整数，绝对值≤1000000；两类计数为0到1000000的整数。初始左右界均为value。',
 '按从左到右输出 t 行：left right count0 count1，四个整数；不输出箱数。', '箱1计数(1,1)，箱2(2,2)，箱3(8,0)。邻对1/2的期望等于观察，χ²=0；邻对2/3行和4、8，列和10、2，总数12，四格贡献8/15、8/3、4/15、4/3，合计24/5=4.8。合并最左对后箱为边界 `[1,2]`、计数(3,3)，以及边界 `[3,3]`、计数(8,0)，已到2箱，输出这两行。',
 ['用 [left,right,count0,count1] 保存一个箱。', '每轮扫描所有相邻对，严格小于当前最优时更新位置，等于时不更新。', '借用2×2公式但在同一文件独立实现；用Fraction保持并列精确，合并列表中best与best+1，下一轮重新扫描。'],
 '时间 O(b²)，空间 O(b)，逐轮扫描及列表删除均为O(当前箱数)，按题面有界整数算术计。', '只能合并相邻箱；合并后计数和邻对χ²需重算；不能只排序初始χ²；精确有理数比较防止浮点误差打破并列。', CHI_FUNCTION+'''

def solve(raw):
    lines = raw.splitlines()
    b, target = map(int, lines[0].split())
    bins = []
    for line in lines[1:b+1]:
        value, count0, count1 = map(int, line.split())
        bins.append([value, value, count0, count1])
    while len(bins) > target:
        best = 0
        best_score = chi_square([bins[0][2:], bins[1][2:]])
        for i in range(1, len(bins)-1):
            score = chi_square([bins[i][2:], bins[i+1][2:]])
            if score < best_score:  # 相等时保留先扫描到的最左位置。
                best, best_score = i, score
        left, right = bins[best], bins[best+1]
        bins[best] = [left[0], right[1], left[2]+right[2], left[3]+right[3]]
        del bins[best+1]
    return '\\n'.join(' '.join(map(str, box)) for box in bins)''', CHI_SOURCE)

material(38, '求中位数 M：排序后奇数个取中间值，偶数个取中间两值平均。求 MAD=median(|x-M|)，即中位绝对偏差。输出鲁棒特征 (x-M)/MAD；MAD=0时本题约定所有特征输出0。使用原始MAD，不乘正态校准系数，不检测异常阈值。',
 '一行 n 个实数（无需单独输入n），1≤n≤200，绝对值≤1000000。',
 '第一行 M MAD；第二行 n 个鲁棒特征，按原始顺序。', '排序1、2、3、100，中位数(2+3)/2=2.5；绝对偏差1.5、0.5、0.5、97.5，排序0.5、0.5、1.5、97.5，中位数1。减2.5后除1，得-1.5、-0.5、0.5、97.5。',
 ['写一个排序取中间的median函数，可调用两次。', '第二次median的输入是每个元素到第一次median的绝对距离。', '先求M，再求abs(x-M)的中位数；MAD>0时逐项除MAD，否则造全0；不能用偏差的平均数代替中位数。'],
 '时间 O(n log n)，空间 O(n)，两次排序。', 'MAD不是平均绝对偏差；MAD=0不表示全部值都相等；本题0分母回退为教学约定；不对异常值做截断。', '''def median(values):
    ordered = sorted(values)
    n = len(ordered)
    if n % 2:
        return ordered[n//2]
    return (ordered[n//2-1]+ordered[n//2])/2


def solve(raw):
    values = list(map(float, raw.split()))
    center = median(values)
    mad = median([abs(x-center) for x in values])
    features = [0.0 if mad == 0 else (x-center)/mad for x in values]
    return format_row([center, mad])+'\\n'+format_row(features)''', MAD_SOURCE)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--materials', nargs='*', type=int)
    args = parser.parse_args()
    if args.materials is None:
        write_cases()
    else:
        write_materials(args.materials)
