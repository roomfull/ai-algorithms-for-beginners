"""独立验收：常量答案由公式展开手算，不导入参考解。"""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FoundationsTests(unittest.TestCase):
    def numbers(self, pid, stdin):
        solution = ROOT / "solutions" / f"{pid}.py"
        self.assertTrue(solution.is_file(), f"缺少独立参考解 {pid}")
        result = subprocess.run([sys.executable, str(solution)], input=stdin,
                                text=True, capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        return [[float(x) for x in line.split()] for line in result.stdout.splitlines()]

    def test_rectangular_matrix_multiplication_by_hand(self):
        # 行乘列：1*7+2*9+3*11=58；4*8+5*10+6*12=154。
        actual = self.numbers("P019", "2 3 2\n1 2 3\n4 5 6\n7 8\n9 10\n11 12\n")
        self.assertEqual(actual, [[58, 64], [139, 154]])

    def test_population_variance_divides_by_n(self):
        # 均值3，平方偏差9+1+1+9=20；总体方差20/4=5，而非20/3。
        self.assertEqual(self.numbers("P016", "0 2 4 6\n"), [[5]])

    def test_broadcast_axes_are_different(self):
        # 矩形矩阵刻意避开行列长度相同导致错误广播也可执行的情况。
        actual = self.numbers("P021", "2 3\n1 2 3\n4 5 6\n10 20 30\n100 200\n")
        self.assertEqual(actual, [[11, 22, 33], [14, 25, 36],
                                  [101, 102, 103], [204, 205, 206]])

    def test_axis_aggregation_shapes(self):
        self.assertEqual(self.numbers("P022", "3 2\n1 2\n3 4\n5 6\n"),
                         [[3, 7, 11], [9, 12]])


if __name__ == "__main__":
    unittest.main()
