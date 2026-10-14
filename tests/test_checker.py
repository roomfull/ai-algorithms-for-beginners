"""判题器的独立测试；所有程序执行均使用临时真实脚本。"""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CheckerTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue((ROOT / "check.py").is_file(), "需要先实现 check.py")
        spec = importlib.util.spec_from_file_location("course_checker", ROOT / "check.py")
        self.checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.checker)
        self.temp = tempfile.TemporaryDirectory(prefix=".checker-test-中文_", dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def compare(self, actual, expected, mode, line_modes=None):
        try:
            if line_modes is None:
                result = self.checker.compare_output(actual, expected, mode)
            else:
                result = self.checker.compare_output(actual, expected, mode, line_modes=line_modes)
        except TypeError as error:
            self.fail(f"compare_output 应接受可选 line_modes：{error}")
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[1], str)
        return result[0]

    def script(self, code, name="中文练习.py"):
        path = self.root / name
        path.write_text(code, encoding="utf-8")
        return path

    def run_script(self, code, expected="42\n", input_text="", mode="int", timeout=5):
        result = self.checker.run_case(
            self.script(code), {"input": input_text, "expected": expected}, mode, timeout
        )
        self.assertTrue({"status", "message", "stdout", "stderr"} <= result.keys())
        return result

    def problem(self, problem_id="P001", chapter="01", folder="01_python", **updates):
        directory = self.root / "chapters" / folder / "problems" / problem_id
        directory.mkdir(parents=True, exist_ok=True)
        data = {"id": problem_id, "chapter": chapter, "title": "测试题", "mode": "int",
                "requires": [], "cases": [{"name": f"案例{i}", "input": "", "expected": "42\n"} for i in range(5)]}
        data.update(updates)
        (directory / "cases.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        (directory / "exercise.py").write_text("print(42)\n", encoding="utf-8")
        return directory

    def cli(self, *args):
        shutil.copyfile(ROOT / "check.py", self.root / "check.py")
        return subprocess.run([sys.executable, str(self.root / "check.py"), *args],
                              cwd=self.root, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=20)

    def test_text_tolerates_only_documented_whitespace(self):
        self.assertTrue(self.compare("你好  \r\n世界\t\r\n\r\n", "你好\n世界\n", "text"))
        self.assertFalse(self.compare("你 好\n", "你好\n", "text"))
        self.assertFalse(self.compare("\n你好\n", "你好\n", "text"))

    def test_debug_output_is_wrong_answer(self):
        self.assertFalse(self.compare("debug\n42\n", "42\n", "int"))

    def test_numeric_shape_is_checked_before_values(self):
        for mode in ("int", "float"):
            self.assertFalse(self.compare("1 2\n3 4\n", "1 2 3 4\n", mode))
            self.assertFalse(self.compare("1\n2 3 4\n", "1 2\n3 4\n", mode))
        ok, message = self.checker.compare_output("9 9\n3\n", "1 2\n3 4\n", "int")
        self.assertFalse(ok)
        self.assertIn("第 2 行应有", message)

    def test_integer_tokens_are_strict_decimal(self):
        self.assertTrue(self.compare("+42 -0\n", "42 0\n", "int"))
        for token in ("42.0", "4.2e1", "4_2", "四十二", "0x2a", "４２"):
            self.assertFalse(self.compare(token, "42", "int"), token)

    def test_large_integer_keeps_exact_precision(self):
        self.assertFalse(self.compare("9007199254740993", "9007199254740992", "int"))
        self.assertTrue(self.compare("9" * 100, "9" * 100, "int"))

    def test_float_tolerance_and_finite_values(self):
        self.assertTrue(self.compare("1.0000005 0.0000005", "1 0", "float"))
        self.assertFalse(self.compare("1.0001", "1", "float"))
        for token in ("nan", "NaN", "inf", "-Infinity", "1e999"):
            self.assertFalse(self.compare(token, token, "float"), token)
        self.assertFalse(self.compare("1", "nan", "float"))

    def test_mixed_rows_accept_float_tolerance_and_exact_text(self):
        self.assertTrue(self.compare("中心\t\r\n1.0000005 0.0000005\r\n+1 -0\r\n\r\n",
                                     "中心\n1 0\n1 0\n", "text", ["text", "float", "int"]))
        self.assertFalse(self.compare("中 心\n1 0\n1 0", "中心\n1 0\n1 0",
                                      "float", ["text", "float", "int"]))

    def test_mixed_integer_labels_reject_decimal_and_exponent(self):
        for token in ("0.0000001", "1e0", "1.0", "nan", "inf"):
            with self.subTest(token=token):
                self.assertFalse(self.compare("1.0\n" + token, "1\n0" if token == "0.0000001" else "1\n1",
                                              "float", ["float", "int"]))

    def test_mixed_float_rows_reject_nonfinite_actual_and_expected(self):
        for token in ("nan", "inf", "1e999"):
            with self.subTest(token=token):
                self.assertFalse(self.compare(token + "\n1", "1\n1", "int", ["float", "int"]))
                self.assertFalse(self.compare("1\n1", token + "\n1", "int", ["float", "int"]))

    def test_mixed_numeric_shape_precedes_all_value_comparison(self):
        try:
            ok, message = self.checker.compare_output("wrong\n9 9\n3", "label\n1 2\n3 4", "text",
                                                       ["text", "float", "int"])
        except TypeError as error:
            self.fail(f"compare_output 应接受可选 line_modes：{error}")
        self.assertFalse(ok)
        self.assertIn("第 3 行应有 2 个元素", message)
        self.assertFalse(self.compare("1\n0\nextra", "1\n0", "float", ["float", "int"]))

    def test_invalid_line_modes_return_clear_comparison_error(self):
        for modes in ("float", ("float", "int"), [], ["float"], ["float", "int", "int"],
                      ["float", "number"], ["float", None], ["float", []], ["float", {}]):
            with self.subTest(line_modes=modes):
                try:
                    ok, message = self.checker.compare_output("1\n0", "1\n0", "float", modes)
                except TypeError as error:
                    self.fail(f"非法 line_modes 应返回诊断：{error}")
                self.assertFalse(ok)
                self.assertIn("line_modes", message)

    def test_run_case_propagates_mixed_modes(self):
        case = {"input": "", "expected": "1\n0\n", "line_modes": ["float", "int"]}
        self.assertEqual(self.checker.run_case(self.script("print('1.0000005\\n0')"), case, "float")["status"], "pass")
        result = self.checker.run_case(self.script("print('1\\n0.0000001')"), case, "float")
        self.assertEqual(result["status"], "wrong_answer")
        self.assertIn("十进制整数", result["message"])

    def test_cli_valid_mixed_metadata_and_executor(self):
        cases = [{"name": str(i), "input": "", "expected": "1\n0\n\n", "line_modes": ["float", "int"]}
                 for i in range(5)]
        directory = self.problem(mode="text", cases=cases)
        (directory / "exercise.py").write_text("print('1.0000005\\n0')", encoding="utf-8")
        result = self.cli("--all")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (directory / "exercise.py").write_text("print('1\\n0.0000001')", encoding="utf-8")
        result = self.cli("--all")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("十进制整数", result.stdout)

    def test_invalid_line_modes_metadata_is_clean_exit_two(self):
        for modes in (None, "float", {}, [], ["float"], ["float", "int", "int"],
                      ["float", "number"], ["float", None], ["float", []], ["float", {}]):
            with self.subTest(line_modes=modes):
                cases = [{"name": str(i), "input": "", "expected": "1\n0", "line_modes": modes}
                         for i in range(5)]
                self.problem(mode="float", cases=cases)
                result = self.cli("--all")
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn("line_modes", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_mixed_invalid_integer_reference_is_metadata_error(self):
        cases = [{"name": str(i), "input": "", "expected": "1\n1e0", "line_modes": ["float", "int"]}
                 for i in range(5)]
        self.problem(mode="float", cases=cases)
        result = self.cli("--all")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("expected 不合法", result.stderr)
        self.assertIn("十进制整数", result.stderr)

    def test_utf8_stdin_stdout_and_chinese_path(self):
        result = self.run_script("print(input() + '，世界')\n", "你好，世界\n", "你好\n", "text")
        self.assertEqual(result["status"], "pass")

    def test_child_uses_script_directory_and_same_python(self):
        (self.root / "数据.txt").write_text("42", encoding="utf-8")
        result = self.run_script("from pathlib import Path\nprint(Path('数据.txt').read_text(encoding='utf-8'))\n")
        self.assertEqual(result["status"], "pass")
        result = self.run_script("import sys\nprint(sys.executable)\n", sys.executable + "\n", mode="text")
        self.assertEqual(result["status"], "pass")

    def test_correct_and_wrong_scripts(self):
        self.assertEqual(self.run_script("print(42)\n")["status"], "pass")
        self.assertEqual(self.run_script("print(41)\n")["status"], "wrong_answer")
        self.assertEqual(self.run_script("print('debug'); print(42)\n")["status"], "wrong_answer")

    def test_not_implemented(self):
        self.assertEqual(self.run_script("raise NotImplementedError('请完成')\n")["status"], "incomplete")

    def test_syntax_error(self):
        self.assertEqual(self.run_script("if True print(42)\n")["status"], "syntax_error")

    def test_missing_module(self):
        self.assertEqual(self.run_script("import nonexistent_course_module_93b7\n")["status"], "missing_module")

    def test_runtime_error(self):
        self.assertEqual(self.run_script("print(1 / 0)\n")["status"], "runtime_error")

    def test_timeout(self):
        result = self.run_script("while True: pass\n", timeout=0.15)
        self.assertEqual(result["status"], "timeout")

    def test_missing_script_is_environment_problem(self):
        result = self.checker.run_case(self.root / "missing.py", {"input": "", "expected": ""}, "text")
        self.assertEqual(result["status"], "environment_error")

    def test_discovery_only_uses_fixed_directory_patterns(self):
        self.problem()
        ignored = self.root / "notes" / "cases.json"
        ignored.parent.mkdir()
        ignored.write_text("not json", encoding="utf-8")
        problems = self.checker.discover_problems(self.root)
        self.assertEqual([p["id"] for p in problems], ["P001"])

    def test_exam_discovery_and_chapter_selection(self):
        directory = self.root / "exams" / "mock01" / "M01A"
        directory.mkdir(parents=True)
        original = self.problem()
        data = json.loads((original / "cases.json").read_text(encoding="utf-8"))
        data.update(id="M01A", chapter="M01")
        (directory / "cases.json").write_text(json.dumps(data), encoding="utf-8")
        (directory / "exercise.py").write_text("print(42)\n", encoding="utf-8")
        result = self.cli("--chapter", "M01")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("M01A", result.stdout)
        self.assertNotIn("P001", result.stdout)

    def test_invalid_metadata_is_exit_two(self):
        invalids = [
            {"id": "bad"}, {"id": "P000"}, {"id": "P081"}, {"id": "P002"}, {"chapter": "02"}, {"title": ""},
            {"mode": "json"}, {"requires": ["torch"]}, {"requires": "numpy"},
            {"cases": []}, {"timeout": 0}, {"timeout": True}, {"timeout": float("nan")},
            {"cases": [{"name": "重复", "input": "", "expected": "42"}] * 5},
            {"cases": [{"name": str(i), "input": 42, "expected": "42"} for i in range(5)]},
        ]
        for update in invalids:
            with self.subTest(update=update):
                self.problem(**update)
                result = self.cli("--all")
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def test_broken_json_reports_metadata_error(self):
        directory = self.problem()
        (directory / "cases.json").write_text("{broken", encoding="utf-8")
        self.assertEqual(self.cli("--all").returncode, 2)

    def test_duplicate_ids_report_both_paths(self):
        self.problem()
        self.problem(chapter="02", folder="02_math_numpy")
        result = self.cli("--all")
        self.assertEqual(result.returncode, 2)
        self.assertIn("重复", result.stderr)
        self.assertIn("01_python", result.stderr)
        self.assertIn("02_math_numpy", result.stderr)

    def test_cli_selects_problem_chapter_all_list_and_solution(self):
        self.problem()
        other = self.problem("P015", "02", "02_math_numpy")
        (other / "exercise.py").write_text("raise NotImplementedError()", encoding="utf-8")
        solution = self.root / "solutions" / "P015.py"
        solution.parent.mkdir()
        solution.write_text("print(42)", encoding="utf-8")
        self.assertEqual(self.cli("P001").returncode, 0)
        self.assertEqual(self.cli("--chapter", "01").returncode, 0)
        self.assertEqual(self.cli("--all").returncode, 1)
        self.assertEqual(self.cli("P015", "--solution").returncode, 0)
        listing = self.cli("--list")
        self.assertEqual(listing.returncode, 0)
        self.assertIn("P001", listing.stdout)
        self.assertIn("P015", listing.stdout)
        self.assertNotIn("solutions", listing.stdout)

    def test_cli_missing_selection_unknown_id_and_empty_chapter_are_errors(self):
        self.problem()
        for args in ((), ("P999",), ("--chapter", "09"), ("--chapter", "1"),
                     ("--all", "P001"), ("--all", "--timeout", "0"),
                     ("--all", "--timeout", "nan")):
            with self.subTest(args=args):
                self.assertEqual(self.cli(*args).returncode, 2)

    def test_empty_repository_is_not_success(self):
        self.assertEqual(self.cli("--all").returncode, 2)
        self.assertEqual(self.cli("--list").returncode, 2)

    def test_cli_timeout_override_and_missing_module_exit(self):
        directory = self.problem()
        (directory / "exercise.py").write_text("while True: pass", encoding="utf-8")
        result = self.cli("P001", "--timeout", "0.1")
        self.assertEqual(result.returncode, 1)
        self.assertIn("超时", result.stdout)
        (directory / "exercise.py").write_text("import nonexistent_course_module_93b7", encoding="utf-8")
        self.assertEqual(self.cli("P001").returncode, 2)

    def test_cli_missing_solution_is_environment_error(self):
        self.problem()
        self.assertEqual(self.cli("P001", "--solution").returncode, 2)

    def test_invalid_reference_output_is_metadata_problem(self):
        directory = self.problem(mode="float")
        data = json.loads((directory / "cases.json").read_text(encoding="utf-8"))
        data["cases"][0]["expected"] = "nan"
        (directory / "cases.json").write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(self.cli("--all").returncode, 2)

    def test_declared_dependency_is_checked_before_running(self):
        self.problem(requires=["numpy"])
        shutil.copyfile(ROOT / "check.py", self.root / "check.py")
        result = subprocess.run([sys.executable, "-S", str(self.root / "check.py"), "--all"],
                                capture_output=True, text=True, encoding="utf-8", timeout=20)
        self.assertEqual(result.returncode, 2)
        self.assertIn("numpy", result.stderr)

    def test_cli_solution_uses_problem_directory_as_cwd(self):
        directory = self.problem()
        (directory / "数据.txt").write_text("42", encoding="utf-8")
        solution = self.root / "solutions" / "P001.py"
        solution.parent.mkdir()
        solution.write_text("from pathlib import Path\nprint(Path('数据.txt').read_text(encoding='utf-8'))", encoding="utf-8")
        result = self.cli("P001", "--solution")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_out_of_course_id_cannot_be_hidden_by_matching_directory(self):
        self.problem(problem_id="P000")
        self.assertEqual(self.cli("--all").returncode, 2)


if __name__ == "__main__":
    unittest.main()
