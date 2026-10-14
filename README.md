# Python 零基础到 AI 科目一练习

从普通 Python 开始，再学 NumPy、公共 AI 基础和 AI 系统优化算法。练习为原创训练材料；正式考试的版本、环境和规则请以你的考试说明为准。

**第一次学习请先读 [零基础起步](docs/START_HERE.md)。** 它从打开终端、运行第一段代码讲起。

在项目根目录的 PowerShell 中执行：

```powershell
.\setup.ps1
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import numpy; print(numpy.__version__)"
```

项目使用 Python 3.11、NumPy 2.2.6。`.venv` 是独立环境；无需激活即可运行，也不需要全局 pip。首次安装依赖需要网络，安装完成后课程运行与判题无需网络。

题目入口将在后续课程工作包生成：`chapters/01_python/problems/P001/README.md`。本基础工具阶段尚未提供正式题目。题目加入后，在根目录运行：

```powershell
.\.venv\Scripts\python.exe check.py --list
.\.venv\Scripts\python.exe check.py P001
.\.venv\Scripts\python.exe check.py --chapter 01
```

学习顺序是读题、手算、编辑题目目录下的 `exercise.py`、保存、检查、根据失败案例修改。`未完成` 提示表示脚手架中的 `NotImplementedError` 还没有替换。

检查器维护测试可直接执行：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p test_checker.py -v
```

检查器运行真实子进程，判定通过、答案错误、未完成、语法错误、运行错误、缺少模块和超时。退出码 `0` 表示全通过，`1` 表示学习代码未通过，`2` 表示参数、题目元数据或环境存在问题。当前目录没有题目时，`--list` 和 `--all` 返回 `2`，避免把空检查误报为成功。

<details>
<summary>维护与对照用参考答案入口</summary>

后续独立参考解位于 `solutions/<题号>.py`，讲解位于 `solutions/<题号>.md`。使用 `--solution` 才会检查答案，普通检查默认运行练习。

```powershell
.\.venv\Scripts\python.exe check.py --all --solution
```

</details>
