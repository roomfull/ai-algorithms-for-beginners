"""独立数学性质和手算案例；不导入参考答案。"""
from pathlib import Path
import importlib.util
import json
import math
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PreprocessingFeatureTests(unittest.TestCase):
    def run_solution(self, pid, stdin):
        solution = ROOT / 'solutions' / f'P{pid:03}.py'
        self.assertTrue(solution.is_file(), f'缺少参考解 P{pid:03}')
        result = subprocess.run([sys.executable, str(solution)], input=stdin,
                                text=True, capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        return [[float(t) for t in line.split()] for line in result.stdout.splitlines()]

    def test_all_hand_calculated_cases(self):
        for folder in ('03_preprocessing', '04_features'):
            for case_file in sorted((ROOT / 'chapters' / folder / 'problems').glob('*/cases.json')):
                data = json.loads(case_file.read_text(encoding='utf-8'))
                self.assertGreaterEqual(len(data['cases']), 5)
                for case in data['cases']:
                    with self.subTest(pid=data['id'], case=case['name']):
                        actual = self.run_solution(int(data['id'][1:]), case['input'])
                        expected = [[float(t) for t in line.split()] for line in case['expected'].splitlines()]
                        self.assertEqual([len(r) for r in actual], [len(r) for r in expected])
                        for row, wanted in zip(actual, expected):
                            for x, y in zip(row, wanted):
                                self.assertTrue(math.isclose(x, y, abs_tol=1e-6, rel_tol=1e-6), (x, y))

    def test_zscore_population_invariants_and_constant_column(self):
        rows = self.run_solution(26, '4 2\n2 9\n4 9\n8 9\n10 9\n')
        self.assertAlmostEqual(sum(r[0] for r in rows)/4, 0)
        self.assertAlmostEqual(sum(r[0]**2 for r in rows)/4, 1)
        self.assertEqual([r[1] for r in rows], [0]*4)

    def test_zscore_decimal_constant_column_is_exactly_zero(self):
        self.assertEqual(self.run_solution(26, '3 1\n0.1\n0.1\n0.1\n'), [[0], [0], [0]])

    def test_scaling_preserves_decimal_gaps_at_large_offset(self):
        for pid, raw in ((25, '3 1\n999999.999992\n999999.999993\n999999.999994\n'),
                         (27, '3 1 2\n999999.999992\n999999.999994\n999999.999993\n0 1 2\n')):
            with self.subTest(pid=pid):
                expected = [[0], [0.5], [1]] if pid == 25 else [[0], [1], [0.5]]
                self.assertEqual(self.run_solution(pid, raw), expected)

    def test_zscore_large_offset_and_small_scale(self):
        # 三个等间距数的总体方差是2h²/3，标准化与偏移和h无关。
        for values in ('999999.999998\n999999.999999\n1000000',
                       '0\n0.000000000001\n0.000000000002'):
            with self.subTest(values=values):
                rows = self.run_solution(26, '3 1\n'+values+'\n')
                for row, expected in zip(rows, (-math.sqrt(1.5), 0, math.sqrt(1.5))):
                    self.assertAlmostEqual(row[0], expected, places=10)
        self.assertEqual(self.run_solution(26, '3 1\n999999.999999\n999999.999999\n999999.999999\n'), [[0], [0], [0]])

    def test_mad_preserves_decimal_gaps(self):
        for raw in ('999999.999992 999999.999993 999999.999994\n',
                    '0 0.000000000001 0.000000000002\n'):
            with self.subTest(raw=raw):
                self.assertEqual(self.run_solution(38, raw)[1], [-1, 0, 1])

    def test_small_scale_training_range_and_constant_columns(self):
        self.assertEqual(self.run_solution(25, '3 2\n0 999999.999999\n0.000000000001 999999.999999\n0.000000000002 999999.999999\n'), [[0, 0], [0.5, 0], [1, 0]])
        # 训练宽度10^-12，验证值1得到10^12；不能裁剪或提前转float。
        self.assertEqual(self.run_solution(27, '3 1 2\n0\n0.000000000001\n1\n0 1 2\n'), [[0], [1], [1e12]])

    def test_smote_decimal_distance_tie_uses_original_index(self):
        # 两邻点离0.3的十进制距离都是0.1，输入下标1的0.4先于下标2的0.2。
        rows = self.run_solution(30, '7 1 1 1\n1 0.3\n1 0.4\n1 0.2\n0 1\n0 2\n0 3\n0 4\n0 1\n')
        self.assertEqual(rows, [[0.4]])

    def test_integer_metadata_rejects_fractional_output(self):
        spec = importlib.util.spec_from_file_location('course_checker', ROOT / 'check.py')
        checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(checker)
        for pid, chapter in ((28, '03_preprocessing'), (37, '04_features')):
            with self.subTest(pid=pid):
                data = json.loads((ROOT / 'chapters' / chapter / 'problems' /
                                   f'P{pid:03}' / 'cases.json').read_text(encoding='utf-8'))
                expected = data['cases'][0]['expected']
                rows = [line.split() for line in expected.splitlines()]
                rows[0][0] += '.0000001'  # 浮点模式容差会误接受这个非整数。
                actual = '\n'.join(' '.join(row) for row in rows)
                self.assertFalse(checker.compare_output(actual, expected, data['mode'])[0])
                self.assertEqual(data['mode'], 'int')

    def test_smote_excludes_closer_majority_and_endpoints(self):
        rows = self.run_solution(30, '5 1 1 2\n1 0\n0 0.01\n1 10\n0 0.02\n0 0.03\n0 0\n0 1\n')
        self.assertEqual(rows, [[0], [0]])  # 基点0的lambda=0；基点10的邻居是0。

    def test_tfidf_smoothed_manual_weights_and_unit_norm(self):
        rows = self.run_solution(33, '2 2 1\nb a\na a b\na\n')
        weight = 1 + math.log(3/2)  # b只在一篇文档出现；a在两篇出现。
        norm = math.sqrt(4 + weight*weight)
        self.assertAlmostEqual(rows[0][0], 2/norm)
        self.assertAlmostEqual(rows[0][1], weight/norm)
        self.assertAlmostEqual(sum(v*v for v in rows[0]), 1)

    def test_independent_contingency_is_zero(self):
        self.assertEqual(self.run_solution(36, '4 6\n10 15\n'), [[0]])

    def test_mad_translation_invariant(self):
        first = self.run_solution(38, '-4 0 2 8 10\n')
        shifted = self.run_solution(38, '96 100 102 108 110\n')
        self.assertEqual(shifted[0][0] - first[0][0], 100)
        self.assertEqual(first[0][1], shifted[0][1])
        self.assertEqual(first[1], shifted[1])


if __name__ == '__main__':
    unittest.main()
