"""模拟卷独立手算案例；不运行参考答案生成期望。"""
import importlib.util
import itertools
import math
from pathlib import Path
import unittest

from check import compare_output

ROOT = Path(__file__).resolve().parents[1]


def case(name, raw, expected, modes=None):
    item = dict(name=name, input=raw, expected=expected)
    if modes:
        item['line_modes'] = modes
    return item


# 每个数字来自手算或闭式表达式。表达式也不调用待测算法。
a = 1 + math.log(1.5)
unequal = 1 / math.sqrt(1 + a*a)
CASES = {
 'M01A': [
  case('两维缩放改变近邻', '3 2 1\n0 0 9\n2 100 3\n4 0 7\n2 0\n', '0\n9\n', ['int','int']),
  case('常量列忽略', '2 2 1\n0 5 4\n2 5 8\n2 999\n', '1\n8\n', ['int','int']),
  case('距离及投票平票', '4 1 4\n-3 8\n-1 5\n1 8\n3 5\n0\n', '1 2 0 3\n5\n', ['int','int']),
  case('单样本全常量', '1 2 1\n4 6 -2\n100 -100\n', '0\n-2\n', ['int','int']),
  case('多数票', '3 1 3\n0 9\n1 9\n2 2\n2\n', '2 1 0\n9\n', ['int','int']),
  case('十进制对称边界', '2 1 1\n0.1 10\n0.3 20\n0.2\n', '0\n10\n', ['int','int'])],
 'M01B': [
  case('机房四节点', '4 5\n0 1 4\n1 2 1\n2 3 2\n0 3 9\n0 2 3\n', '6\n'),
  case('单节点', '1 0\n', '0\n'),
  case('断开的机房', '4 2\n0 1 2\n2 3 2\n', '-1\n'),
  case('零价与自环', '3 4\n0 0 0\n0 1 0\n1 2 5\n0 2 8\n', '5\n'),
  case('平行备选线路', '2 3\n0 1 9\n1 0 2\n0 1 3\n', '2\n'),
  case('等价三角形', '3 3\n0 1 7\n1 2 7\n0 2 7\n', '14\n')],
 'M02A': [
  case('余弦方向排序', '3 2 3\n1 0\n0 1\n1 1\n1 0\n', '0 2 1\n1 0.7071067811865476 0\n', ['int','float']),
  case('空查询', '2 2 2\n1 0\n0 1\n0 0\n', '0 1\n0 0\n', ['int','float']),
  case('空文档与未知词列', '2 2 2\n0 0\n0 0\n0 1\n', '0 1\n0 0\n', ['int','float']),
  case('词频倍数平票', '2 1 2\n1\n5\n3\n', '0 1\n1 1\n', ['int','float']),
  case('训练文档频率不含查询', '2 2 2\n1 1\n1 0\n1 0\n', f'1 0\n1 {unequal:.16g}\n', ['int','float']),
  case('只取一篇', '3 2 1\n1 0\n0 1\n1 1\n0 2\n', '1\n1\n', ['int','float'])],
 'M02B': [
  case('悬挂流三轮', '2 1 0.8 0.1 10\n0 1\n', '3 1\n1 0\n0.348 0.652\n', ['int','int','float']),
  case('全部悬挂', '3 0 0.85 0.000001 10\n', '1 1\n0 1 2\n0.3333333333333333 0.3333333333333333 0.3333333333333333\n', ['int','int','float']),
  case('上限未收敛', '2 1 0.8 0.1 1\n0 1\n', '1 0\n1 0\n0.3 0.7\n', ['int','int','float']),
  case('L1正好阈值', '2 1 0.8 0.4 8\n0 1\n', '1 1\n1 0\n0.3 0.7\n', ['int','int','float']),
  case('无阻尼', '2 1 0 0.000001 5\n0 1\n', '1 1\n0 1\n0.5 0.5\n', ['int','int','float']),
  case('单页自环', '1 1 0.9 0.000001 5\n0 0\n', '1 1\n0\n1\n', ['int','int','float'])],
 'M03A': [
  case('中心更新后查询', '4 1 2 2\n0\n2\n8\n10\n0\n10\n5\n', '0 0 1 1\n1\n9\n4\n0\n', ['int','float','float','float','int']),
  case('保留空簇', '2 1 2 1\n0\n2\n0\n100\n99\n', '0 0\n1\n100\n2\n1\n', ['int','float','float','float','int']),
  case('单簇二维', '2 2 1 1\n0 0\n2 4\n99 99\n2 4\n', '0 0\n1 2\n10\n0\n', ['int','float','float','int']),
  case('最终重新分配', '4 1 2 1\n0\n3\n4\n5\n0\n8\n4\n', '0 0 1 1\n2.3333333333333333\n5\n6.8888888888888889\n1\n', ['int','float','float','float','int']),
  case('小数精确平票', '2 1 2 1\n0.1\n0.3\n0.1\n0.3\n0.2\n', '0 1\n0.1\n0.3\n0\n0\n', ['int','float','float','float','int']),
  case('重复初值', '2 1 2 2\n0\n4\n0\n0\n0\n', '1 0\n4\n0\n0\n1\n', ['int','float','float','float','int'])],
 'M03B': [
  case('逐行不同scale', '2 3 3\n-3 0 3\n-1 0 1\n', '1 0.3333333333333333\n-3 0 3\n-3 0 3\n0 0\n', ['float','int','int','float']),
  case('全零权重', '1 3 4\n0 0 0\n', '1\n0 0 0\n0\n', ['float','int','float']),
  case('正负半格远离零', '1 3 2\n-0.5 0.5 1\n', '1\n-1 1 1\n0.1666666666666667\n', ['float','int','float']),
  case('十进制半格', '1 3 2\n0.1 -0.1 0.2\n', '0.2\n1 -1 1\n0.006666666666666667\n', ['float','int','float']),
  case('两位整数精确值', '2 2 2\n2 -2\n0 4\n', '2 4\n1 -1\n0 1\n0 0\n', ['float','int','int','float']),
  case('四位小误差', '1 3 4\n-7 2.2 7\n', '1\n-7 2 7\n0.01333333333333333\n', ['float','int','float'])],
 'M04A': [
  case('卷积激活池化', '3 3 2 2\n1 2 3\n4 5 6\n7 8 9\n1 0\n0 -1\n5\n', '1 1\n1\n', ['int','float']),
  case('ReLU截断', '2 2 1 2\n-1 2\n3 -4\n1\n0\n', '1 1\n1.25\n', ['int','float']),
  case('丢弃池化余边', '3 3 1 2\n1 2 100\n3 4 100\n100 100 100\n1\n0\n', '1 1\n2.5\n', ['int','float']),
  case('池化尺寸一', '2 2 1 1\n-1 2\n3 4\n2\n-1\n', '2 2\n0 3\n5 7\n', ['int','float','float']),
  case('互相关不翻核', '2 2 2 1\n1 2\n3 4\n1 2\n0 -1\n0\n', '1 1\n1\n', ['int','float']),
  case('矩形图像', '2 4 1 2\n1 2 3 4\n5 6 7 8\n1\n0\n', '1 2\n3.5 5.5\n', ['int','float'])],
 'M04B': [
  case('各worker样本数不同', '2 2 0.1\n1 2\n2\n1 2 4\n3 0 0\n1\n2 3 6\n', '1.3333333333333333 2.6666666666666667\n0.8666666666666667 1.7333333333333333\n', ['float','float']),
  case('单worker多批', '1 1 0.5\n10\n2\n1 2\n3 6\n', '5\n7.5\n', ['float','float']),
  case('零学习率', '1 2 0\n1 -2\n1\n4 9 -3\n', '9 -3\n1 -2\n', ['float','float']),
  case('互相抵消', '2 1 1\n4\n1\n2 -3\n1\n2 3\n', '0\n4\n', ['float','float']),
  case('负梯度', '1 1 0.2\n1\n1\n5 -2.5\n', '-2.5\n1.5\n', ['float','float']),
  case('不能平均批平均值', '2 1 1\n0\n2\n1 0\n1 0\n1\n8 10\n', '8\n-8\n', ['float','float'])]
}


def load_solution(pid):
    path = ROOT / 'solutions' / f'{pid}.py'
    assert path.exists(), f'缺少模拟卷参考解 {pid}'
    spec = importlib.util.spec_from_file_location(pid, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solve


class MockAlgorithms(unittest.TestCase):
    def check_cases(self, pid):
        solve = load_solution(pid)
        for c in CASES[pid]:
            with self.subTest(pid=pid, case=c['name']):
                ok, reason = compare_output(solve(c['input']), c['expected'], 'int' if pid == 'M01B' else 'float', c.get('line_modes'))
                self.assertTrue(ok, reason)

    def test_m01a_manual(self): self.check_cases('M01A')
    def test_m01b_manual(self): self.check_cases('M01B')
    def test_m02a_manual(self): self.check_cases('M02A')
    def test_m02b_manual(self): self.check_cases('M02B')
    def test_m03a_manual(self): self.check_cases('M03A')
    def test_m03b_manual(self): self.check_cases('M03B')
    def test_m04a_manual(self): self.check_cases('M04A')
    def test_m04b_manual(self): self.check_cases('M04B')

    def test_mst_matches_tree_enumeration(self):
        solve = load_solution('M01B')
        edges = [(0,1,6),(0,2,2),(0,3,8),(1,2,4),(1,3,1),(2,3,3)]
        totals = []
        for subset in itertools.combinations(edges, 3):
            reached = {0}
            for _ in range(4):
                for u,v,w in subset:
                    if u in reached or v in reached: reached.update([u,v])
            if len(reached) == 4: totals.append(sum(w for u,v,w in subset))
        raw = '4 6\n' + ''.join(f'{u} {v} {w}\n' for u,v,w in edges)
        self.assertEqual(int(solve(raw)), min(totals))

    def test_pagerank_probability_and_symmetry(self):
        solve = load_solution('M02B')
        rows = solve('3 3 0.8 0.000001 5\n0 1\n1 2\n2 0\n').splitlines()
        self.assertEqual(rows[:2], ['1 1', '0 1 2'])
        self.assertAlmostEqual(sum(map(float, rows[2].split())), 1)

    def test_knn_translation_and_positive_scaling(self):
        solve = load_solution('M01A')
        original = '3 2 2\n0 0 8\n2 10 3\n4 0 3\n3 1\n'
        changed = '3 2 2\n5 -3 8\n9 97 3\n13 -3 3\n11 7\n'
        self.assertEqual(solve(original), solve(changed))

    def test_gradient_microbatch_split_invariant(self):
        solve = load_solution('M04B')
        self.assertEqual(solve('1 1 0.1\n1\n1\n8 3\n'), solve('2 1 0.1\n1\n2\n1 3\n2 3\n1\n5 3\n'))

    def test_quantization_error_bound(self):
        rows = load_solution('M03B')('1 5 3\n-2.5 -1.1 0 0.7 3\n').splitlines()
        scale = float(rows[0]); mse = float(rows[2])
        self.assertLessEqual(mse, scale**2/4 + 1e-12)
        self.assertTrue(all(-3 <= int(x) <= 3 for x in rows[1].split()))

    def test_cosine_scale_invariant(self):
        solve = load_solution('M02A')
        self.assertEqual(solve('2 2 2\n1 2\n2 1\n1 0\n'), solve('2 2 2\n3 6\n4 2\n7 0\n'))


if __name__ == '__main__': unittest.main()
