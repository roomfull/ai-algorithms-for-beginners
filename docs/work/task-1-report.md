# Task 1 交付报告

状态：DONE。日期：2026-10-14。仅交付本包文件；没有创建正式题目，没有提交 Git 或修改 Git 身份。

## 文件与行为

- `check.py`：argparse 命令行；只发现 `chapters/*/problems/*/cases.json` 与 `exams/*/*/cases.json`；验证课程范围 ID、目录与 chapter 对应、mode、requires、非空标题、至少 5 案例、唯一案例名、字符串输入输出、合法数值参考输出和正有限超时。重复 ID 错误列出两个冲突路径。
- `tests/test_checker.py`：29 个 unittest 方法，所有执行类测试使用真实临时脚本和 subprocess；不 mock 执行成功。临时目录在项目内并含中文名称，结束后自动清理。
- `requirements.txt`：唯一课程必需第三方依赖锁定 `numpy==2.2.6`。
- `setup.ps1`：只在项目 `.venv` 安装，支持重复运行与 `-PythonExe`，不设置全局 PATH、不改执行策略。安装临时文件使用项目 `.setup-tmp`，脚本结束恢复 TEMP/TMP。
- `.gitignore`：忽略独立环境、缓存、安装临时目录、测试临时目录。
- `README.md` 与 `docs/START_HERE.md`：中文零基础入口，优先使用无需激活的项目解释器路径，解释终端/编辑/保存/运行/检查与常见错误；将 P001 明确标为后续工作包入口。

状态为 `pass`、`wrong_answer`、`incomplete`、`syntax_error`、`runtime_error`、`missing_module`、`timeout`、`environment_error`。CLI 保留完整 stderr traceback，语法/运行错误显示学习文件路径与行号；declared numpy 缺失时给出项目解释器安装命令。每题每案例为独立进程，使用 `sys.executable`，设置 `PYTHONUTF8=1`、`PYTHONIOENCODING=utf-8`，显式 UTF-8 编解码。CLI 的练习和参考解都在题目目录中执行。

退出码：全通过 `0`；学习代码未通过（含语法、运行、未完成、超时）`1`；参数/元数据/环境（含缺模块或缺程序文件）`2`。空库、未知 ID、无题章节均不会成功。`--chapter` 接受目录 metadata 对应的 `01`–`09` 与 `M01`–`M04`。

## 接口

- `compare_output(actual, expected, mode) -> (bool, str)`：文本允许 CRLF/LF、行尾空白及末尾空行差异；数值先验证全部行列形状，再逐元素比较；整数用严格 ASCII 十进制 token 与 Python int 比较，避免浮点精度损失；float 采用 abs_tol=rel_tol=1e-6，拒绝 NaN/inf/溢出无穷值。
- `run_case(script_path, case, mode, timeout=5.0) -> dict`：字典固定含 status/message/stdout/stderr；独立使用时 cwd 为脚本所在目录。
- `discover_problems(root) -> list[dict]`：返回按 ID 排序的 metadata，各字典增加 `directory: pathlib.Path`；无题返回空列表，非法 metadata 抛出带路径的 ValueError。
- `main(argv=None) -> int`：CLI 选择与执行；内部 `_run_case(..., cwd)` 允许参考解仍以题目目录为 cwd。
- 其余私有函数仅负责换行规范化、UTF-8 环境、超时输出解码、timeout 检查与 metadata 检查。

## TDD 证据

所有检查器实现均晚于初始测试创建与执行。初始命令：

```powershell
& 'C:\Users\98356\AppData\Roaming\uv\python\cpython-3.11-windows-x86_64-none\python.exe' -X utf8 -m unittest discover -s tests -p test_checker.py
```

初始结果：`Ran 27 tests in 0.006s`，`FAILED (failures=27)`；共同断言为 `AssertionError: False is not true : 需要先实现 check.py`，当时 check.py 不存在。随后实现，27 项通过。

补充精确契约测试后再次 RED：

```text
Ran 28 tests in 8.348s
FAILED (failures=2)
test_cli_solution_uses_problem_directory_as_cwd: FileNotFoundError: 数据.txt
test_numeric_shape_is_checked_before_values: 期望第2行形状诊断，实际先报告第1行数值
```

修复 CLI cwd 与全形状优先检查后，`Ran 28 tests in 10.372s`、`OK`。

补充课程范围 P000 拒绝测试后 RED：`Ran 29 tests in 11.248s`，`FAILED (failures=1)`，实际退出 `0`、期望 `2`。收紧合法 ID 范围后最终 GREEN：

```powershell
.\.venv\Scripts\python.exe -X utf8 -m unittest discover -s tests -p test_checker.py -v
```

最终结果：`Ran 29 tests in 9.075s`、`OK`、退出 `0`。覆盖多余 debug、浮点形状、整数小数/指数/下划线/非 ASCII token、大整数精度、NaN/inf、中文路径、stdin、解释器一致、工作目录、正确/错误解、未实现、语法/运行/缺模块/超时、metadata、CLI 选择/错误码/空库/未知题号/空章节/参考解/模拟卷。

## 独立环境实际验证

基础解释器：`C:\Users\98356\AppData\Roaming\uv\python\cpython-3.11-windows-x86_64-none\python.exe`，Python **3.11.15**。用该解释器 `-m venv .venv` 创建环境；首次 ensurepip 因沙箱系统 TEMP 写权限失败，随后将进程 TEMP/TMP 指向项目 `.setup-tmp`，项目解释器 `-m ensurepip --upgrade --default-pip` 成功安装 pip 24.0 / setuptools 79.0.1。没有安装到应用环境。

普通沙箱网络首次安装因 DNS 限制失败；随后通过允许的依赖安装提权运行 `setup.ps1`，下载 `numpy-2.2.6-cp311-cp311-win_amd64.whl`，成功安装。没有自动审批拒绝或未解决阻塞。

安装后再用普通权限重复执行：

```powershell
.\setup.ps1
```

退出 `0`，提示 `Requirement already satisfied: numpy==2.2.6`、`Python: 3.11.15`、`NumPy: 2.2.6`，Interpreter 指向本项目 `.venv\Scripts\python.exe`。重复运行不重建环境、不改系统策略。

```powershell
.\.venv\Scripts\python.exe -X utf8 -c "import sys, numpy; print('version:', sys.version.split()[0]); print('isolated:', sys.prefix != sys.base_prefix); print('numpy:', numpy.__version__); print('matrix:', (numpy.array([[1,2]]) @ numpy.array([[3],[4]])).tolist())"
.\.venv\Scripts\python.exe -m pip check
```

实际输出：`version: 3.11.15`、`isolated: True`、`numpy: 2.2.6`、`matrix: [[11]]`；pip check 输出 `No broken requirements found.`。

`check.py --help` 实际显示 ID、chapter、all、list、solution、timeout 选项。当前尚无正式题目，`check.py --list` 和 `check.py --all` 给出“未发现题目”；在 PowerShell 显式打印 `$LASTEXITCODE` 验证为 **2**。

`Get-Command py` 发现启动器文件，但 `py --list` 实际输出 `No installed Pythons found!`。教程据此说明本机启动器未配置可用解释器，避免把 py 当唯一方案。执行策略检查为 RemoteSigned，脚本未修改该值。

## 依据与剩余工作

已查阅 [Python subprocess 官方文档](https://docs.python.org/3.11/library/subprocess.html)、[GitHub CPython 3.11 subprocess 实现](https://github.com/python/cpython/blob/3.11/Lib/subprocess.py) 核对进程、encoding、cwd 和 timeout 约定；[NumPy 2.2.6 PyPI 官方发布](https://pypi.org/project/numpy/2.2.6/) 标注 Python >=3.10、支持 Python3.11，并且本机已经实际安装运行。

本包没有未解决问题。正式题目/章节教程/总进度与全库验收属于后续工作包，本报告不将临时 fixture 误称为正式题目。README 与 START_HERE 后续应由 Task 6 更新为已实际生成的课程入口。
