# 混合输出行类型检查器交付报告

2026-10-14，按 `task-checker-mixed.md` 补充检查器；未改课程题面、练习或参考答案，未提交 Git。

## API 与行为

`compare_output(actual, expected, mode, line_modes=None)` 返回 `(bool, 中文诊断)`。原三参数调用及显式 `None` 仍按整体 `mode` 比较。传入列表后，每项覆盖对应行的比较模式。

每个 case 可以增加 `line_modes` 列表，只接受字符串 `text`、`int`、`float`，长度必须等于经过现有换行、行末空白和末尾空行规范化后的 expected 行数。元数据显式 `null`、非列表、错误长度和非法元素均清晰报错，CLI 退出码为 2，无 traceback。expected 也按逐行模式验证，整数参考行中的 `1e0` 被判为非法元数据。

比较顺序为先检查总行数，再检查所有数值行的元素数，最后比较各行内容。因此后面数值行形状错误会先于前面文本或数值内容错误报告。text 保留原空白规则；float 保留绝对/相对 `1e-6` 容差及非有限值拒绝规则；int 保留严格十进制词法和大整数精确比较。

`run_case` 保留原签名，经 `_run_case` 读取 case 的可选 `line_modes` 并传给比较函数；CLI 同样使用这一执行路径。START_HERE 增补混合浮点输出中的整数标签仍严格判断。implementation-plan 的合同由主线程同步更新。

## 测试先行证据

先保存 9 个新测试，再实现生产代码。为保留原 29 个测试的三参数调用，测试辅助函数仅在提供逐行模式时传第四参数。

RED 命令：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_checker.py
```

实现前结果：退出码 1，`Ran 38 tests in 11.822s`，`FAILED (failures=32)`。32 是含 subTest 的失败断言数量；原 29 个测试通过，新 9 个测试失败。失败证据包括 API 尚不接受第四参数、无效元数据未拒绝、真实脚本输出 `0.0000001` 标签被原整体 float 模式错误接受、CLI 忽略混合规则。

GREEN 命令：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_checker.py -v
```

实现后结果：退出码 0，`Ran 38 tests in 10.021s`，`OK`。覆盖合法混合输出、浮点容差、text 规则、严格 int 标签、实际及期望非有限值、规范化后的列表长度、总行数、数值形状优先、run_case 传播、CLI 传播、错误元数据和错误整数参考输出；包含原 29 项回归测试。

## 课程集成验证

```powershell
.\.venv\Scripts\python.exe check.py P044 --solution
.\.venv\Scripts\python.exe check.py P045 --solution
.\.venv\Scripts\python.exe check.py P049 --solution
```

三个命令分别退出码 0，每题均 `通过 5/5 个案例，共 1 题`，合计 15/15 案例通过。使用现有题目元数据中的逐行模式验证，未修改这三题。

本机实测解释器为 `.venv` Python 3.11.15，NumPy 2.2.6。`git diff --check -- check.py tests/test_checker.py docs/START_HERE.md docs/work/task-checker-mixed-report.md` 退出码 0，仅有 Git 的 LF/CRLF 转换提示。
