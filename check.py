"""课程的标准输入输出检查器，仅运行本地学习代码。"""
import argparse
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys


STATUS_NAMES = {
    "pass": "通过", "wrong_answer": "答案错误", "incomplete": "未完成",
    "syntax_error": "语法错误", "runtime_error": "运行错误",
    "missing_module": "缺少模块", "timeout": "超时", "environment_error": "环境问题",
}
INTEGER = re.compile(r"[+-]?[0-9]+")
FLOAT = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?")


def _lines(value):
    lines = [line.rstrip() for line in value.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def compare_output(actual, expected, mode):
    """返回 (是否通过, 中文诊断)。数值比较保留行、列形状。"""
    if mode not in ("text", "int", "float"):
        return False, f"不支持的比较模式：{mode}"
    actual_lines, expected_lines = _lines(actual), _lines(expected)
    if len(actual_lines) != len(expected_lines):
        return False, f"输出行数应为 {len(expected_lines)}，实际为 {len(actual_lines)}"
    if mode != "text":
        for row, (got_line, want_line) in enumerate(zip(actual_lines, expected_lines), 1):
            got_count, want_count = len(got_line.split()), len(want_line.split())
            if got_count != want_count:
                return False, f"第 {row} 行应有 {want_count} 个元素，实际为 {got_count}"
    for row, (got_line, want_line) in enumerate(zip(actual_lines, expected_lines), 1):
        if mode == "text":
            if got_line != want_line:
                return False, f"第 {row} 行应为 {want_line!r}，实际为 {got_line!r}"
            continue
        got_tokens, want_tokens = got_line.split(), want_line.split()
        for column, (got, want) in enumerate(zip(got_tokens, want_tokens), 1):
            label = f"第 {row} 行第 {column} 个元素"
            if mode == "int":
                if not INTEGER.fullmatch(got) or not INTEGER.fullmatch(want):
                    return False, f"{label}必须是十进制整数：实际 {got!r}，期望 {want!r}"
                # 直接用整数比较，避免先转 float 丢失大整数精度。
                try:
                    equal = int(got) == int(want)
                except ValueError:
                    return False, f"{label}整数超出当前 Python 可解析的位数"
            else:
                if not FLOAT.fullmatch(got) or not FLOAT.fullmatch(want):
                    return False, f"{label}必须是有限数值：实际 {got!r}，期望 {want!r}"
                got_number, want_number = float(got), float(want)
                if not math.isfinite(got_number) or not math.isfinite(want_number):
                    return False, f"{label}不能是 NaN 或无穷大"
                equal = math.isclose(got_number, want_number, rel_tol=1e-6, abs_tol=1e-6)
            if not equal:
                return False, f"{label}应为 {want}，实际为 {got}"
    return True, "输出符合要求"


def _utf8_env():
    env = os.environ.copy()
    env.update(PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    return env


def _decoded(value):
    # TimeoutExpired 即使 text=True 也可能携带 bytes。
    return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else (value or "")


def run_case(script_path, case, mode, timeout=5.0):
    """在独立进程运行一例；不向检查器进程导入学习代码。"""
    return _run_case(script_path, case, mode, timeout, Path(script_path).resolve().parent)


def _run_case(script_path, case, mode, timeout, cwd):
    script_path = Path(script_path).resolve()
    result = {"status": "environment_error", "message": "", "stdout": "", "stderr": ""}
    if not script_path.is_file():
        result["message"] = f"找不到程序：{script_path}"
        return result
    try:
        process = subprocess.run(
            [sys.executable, str(script_path)], input=case["input"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            cwd=cwd, env=_utf8_env(), timeout=timeout,
        )
    except subprocess.TimeoutExpired as error:
        result.update(status="timeout", message=f"运行超过 {timeout:g} 秒，请检查循环和算法",
                      stdout=_decoded(error.stdout), stderr=_decoded(error.stderr))
        return result
    except OSError as error:
        result["message"] = f"无法启动 Python：{error}"
        return result
    result.update(stdout=process.stdout, stderr=process.stderr)
    if process.returncode:
        status = "runtime_error"
        for pattern, candidate in (
            (r"^ModuleNotFoundError:", "missing_module"),
            (r"^NotImplementedError(?::|$)", "incomplete"),
            (r"^(?:SyntaxError|IndentationError|TabError):", "syntax_error"),
        ):
            if re.search(pattern, process.stderr, re.MULTILINE):
                status = candidate
                break
        lines = process.stderr.strip().splitlines()
        result.update(status=status, message=lines[-1] if lines else f"程序退出码：{process.returncode}")
        return result
    ok, message = compare_output(process.stdout, case["expected"], mode)
    result.update(status="pass" if ok else "wrong_answer", message=message)
    return result


def _positive_seconds(value):
    number = float(value)
    if isinstance(value, bool) or not math.isfinite(number) or number <= 0:
        raise ValueError("超时秒数必须是有限的正数")
    return number


def _validate_metadata(data, path):
    def fail(message):
        raise ValueError(f"{path}：{message}")

    if not isinstance(data, dict):
        fail("顶层必须是 JSON 对象")
    for key in ("id", "chapter", "title", "mode", "requires", "cases"):
        if key not in data:
            fail(f"缺少字段 {key}")
    problem_id = data["id"]
    if not isinstance(problem_id, str) or not re.fullmatch(r"P(?:00[1-9]|0[1-7][0-9]|080)|M0[1-4][AB]", problem_id):
        fail("id 必须在 P001–P080 或 M01A–M04B 的课程范围内")
    if problem_id != path.parent.name:
        fail("id 必须与题目目录名一致")
    if path.parent.parent.name == "problems":
        chapter_dir = path.parent.parent.parent.name
        if not re.fullmatch(r"0[1-9]_[a-z0-9_]+", chapter_dir) or not problem_id.startswith("P"):
            fail("普通题目录应为 chapters/01_name/problems/P001")
        expected_chapter = chapter_dir[:2]
    else:
        exam_dir = path.parent.parent.name
        if not re.fullmatch(r"mock0[1-4]", exam_dir) or not problem_id.startswith("M"):
            fail("模拟题目录应为 exams/mock01/M01A")
        expected_chapter = "M" + exam_dir[-2:]
        if problem_id[:3] != expected_chapter:
            fail("模拟题 id 必须与试卷目录一致")
    if data["chapter"] != expected_chapter:
        fail(f"chapter 必须与目录一致，应为 {expected_chapter}")
    if not isinstance(data["title"], str) or not data["title"].strip():
        fail("title 必须是非空字符串")
    if data["mode"] not in ("text", "int", "float"):
        fail("mode 仅支持 text、int、float")
    if data["requires"] not in ([], ["numpy"]):
        fail('requires 仅支持 [] 或 ["numpy"]')
    if not isinstance(data["cases"], list) or len(data["cases"]) < 5:
        fail("每题至少需要 5 个案例")
    names = set()
    for index, case in enumerate(data["cases"], 1):
        if not isinstance(case, dict):
            fail(f"案例 {index} 必须是对象")
        if not isinstance(case.get("name"), str) or not case["name"].strip():
            fail(f"案例 {index} 缺少非空 name")
        if case["name"] in names:
            fail(f"案例名重复：{case['name']}")
        names.add(case["name"])
        for key in ("input", "expected"):
            if not isinstance(case.get(key), str):
                fail(f"案例 {case['name']} 的 {key} 必须是字符串")
        ok, message = compare_output(case["expected"], case["expected"], data["mode"])
        if not ok:
            fail(f"案例 {case['name']} 的 expected 不合法：{message}")
    if "timeout" in data:
        try:
            if not isinstance(data["timeout"], (int, float)):
                raise ValueError("必须是数值")
            _positive_seconds(data["timeout"])
        except (ValueError, TypeError) as error:
            fail(f"timeout 不合法：{error}")


def discover_problems(root):
    """仅扫描两个约定目录，返回含 directory(Path) 的元数据字典列表。"""
    root = Path(root).resolve()
    paths = sorted(root.glob("chapters/*/problems/*/cases.json"))
    paths += sorted(root.glob("exams/*/*/cases.json"))
    problems, seen = [], {}
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as error:
            raise ValueError(f"{path}：无法读取 cases.json：{error}") from error
        _validate_metadata(data, path)
        if data["id"] in seen:
            raise ValueError(f"题号重复 {data['id']}：{seen[data['id']]} 与 {path}")
        seen[data["id"]] = path
        problems.append({**data, "directory": path.parent})
    return sorted(problems, key=lambda problem: problem["id"])


def main(argv=None):
    parser = argparse.ArgumentParser(description="检查 Python 课程练习（默认运行 exercise.py）")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("problem", nargs="?", help="题号，如 P001 或 M01A")
    selection.add_argument("--chapter", help="章节 01–09 或模拟卷 M01–M04")
    selection.add_argument("--all", action="store_true", help="检查所有题目")
    selection.add_argument("--list", action="store_true", help="只列出题号、章节、标题")
    parser.add_argument("--solution", action="store_true", help="维护/对照：检查独立参考解")
    parser.add_argument("--timeout", type=_positive_seconds, help="覆盖每案例超时秒数（默认 5）")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent
    try:
        problems = discover_problems(root)
        if not problems:
            raise ValueError("未发现题目；请确认课程文件完整且位于约定目录")
        if args.problem:
            problems = [problem for problem in problems if problem["id"] == args.problem]
            if not problems:
                raise ValueError(f"未知题号：{args.problem}，可运行 --list 查看")
        if args.chapter:
            problems = [problem for problem in problems if problem["chapter"] == args.chapter]
            if not problems:
                raise ValueError(f"章节 {args.chapter} 没有题目；章节格式为 01 或 M01")
        if args.list:
            for problem in problems:
                print(f"{problem['id']}  {problem['chapter']}  {problem['title']}")
            return 0
        needed = {module for problem in problems for module in problem["requires"]}
        for module in sorted(needed):
            if importlib.util.find_spec(module) is None:
                raise ValueError(f"缺少模块 {module}：请使用 .\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt")
    except (ValueError, OSError) as error:
        print(f"参数/元数据/环境问题：{error}", file=sys.stderr)
        return 2
    total, passed, exit_code = 0, 0, 0
    for problem in problems:
        script = root / "solutions" / f"{problem['id']}.py" if args.solution else problem["directory"] / "exercise.py"
        timeout = args.timeout if args.timeout is not None else problem.get("timeout", 5.0)
        print(f"\n{problem['id']} {problem['title']}")
        for case in problem["cases"]:
            result = _run_case(script, case, problem["mode"], timeout, problem["directory"])
            total += 1
            passed += result["status"] == "pass"
            print(f"  [{STATUS_NAMES[result['status']]}] {case['name']}：{result['message']}")
            if result["status"] != "pass":
                exit_code = max(exit_code, 2 if result["status"] in ("missing_module", "environment_error") else 1)
                if result["stderr"]:
                    print(result["stderr"].rstrip())
    print(f"\n通过 {passed}/{total} 个案例，共 {len(problems)} 题")
    return exit_code


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
