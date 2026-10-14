# 从零开始：让第一段 Python 代码跑起来

这份教程默认你使用 Windows 和 PowerShell。Python 负责逐句执行 `.py` 文件；PowerShell 是输入运行命令的窗口；编辑器用于修改代码。三者各做一件事。后面的练习只需要 CPU，不需要 GPU、Redis 或外部数据集。

## 1. 打开项目终端

在资源管理器打开本项目文件夹，在地址栏输入 `powershell` 并回车；也可以在已经打开的 PowerShell 中执行：

```powershell
Set-Location -LiteralPath 'C:\Users\98356\Documents\ChatGPT\AI科目1'
Get-Location
Get-ChildItem
```

`Get-Location` 显示当前目录，`Get-ChildItem` 列出文件。应能看到 `setup.ps1`、`check.py` 和 `requirements.txt`。以下所有命令都在这个根目录执行。命令开头的 `.\` 表示“当前目录下”；复制命令时不需要输入终端显示的 `PS C:\...>`。

## 2. 建立项目自己的 Python 环境

本机已核对的基础解释器是 Python 3.11，位置如下。本机的 `py` 启动器尚未配置可用解释器，`py --list` 实际提示 `No installed Pythons found!`，因此不使用 `py` 作为必需命令。

```powershell
& 'C:\Users\98356\AppData\Roaming\uv\python\cpython-3.11-windows-x86_64-none\python.exe' --version
.\setup.ps1
```

`setup.ps1` 会建立根目录下的 `.venv`，并只在其中安装 `requirements.txt` 固定的 NumPy 2.2.6。脚本可重复运行，不修改全局 PATH 或系统执行策略。首次下载依赖需要网络；以后运行练习不需要联网。

如果更换电脑且 Python 3.11 在其他路径，可以明确指定：

```powershell
.\setup.ps1 -PythonExe 'C:\你的Python目录\python.exe'
```

如果 PowerShell 提示禁止运行脚本，不必修改系统策略，直接逐条执行下面的等价命令。`&` 用于运行带引号的可执行文件路径；它不是 Python 语法。

```powershell
New-Item -ItemType Directory -Force .setup-tmp | Out-Null
$env:TEMP = Join-Path $PWD '.setup-tmp'
$env:TMP = $env:TEMP
& 'C:\Users\98356\AppData\Roaming\uv\python\cpython-3.11-windows-x86_64-none\python.exe' -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

这里的 TEMP/TMP 只作用于当前终端，为安装提供项目内的临时目录。关闭终端即可恢复。脚本失败后可再次运行；若提示缺少 pip，可先执行 `.\.venv\Scripts\python.exe -m ensurepip --upgrade --default-pip`，再安装依赖。

如果出现下载失败，请检查网络后重试同一安装命令。换机前如需完全离线安装，可先在兼容的 Windows/Python 3.11 电脑用 `python -m pip download -r requirements.txt -d wheels` 保存安装包，再在目标机器用 `.\.venv\Scripts\python.exe -m pip install --no-index --find-links wheels -r requirements.txt`。课程不要求下载数据集。

## 3. 验证用的是项目环境

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
.\.venv\Scripts\python.exe -c "import numpy; print(numpy.__version__)"
```

第一条应显示 `Python 3.11.x`，第二条路径应以本项目的 `.venv\Scripts\python.exe` 结尾，第三条应显示 `2.2.6`。第三条中 `import numpy` 是导入数值计算库，初学普通 Python 时暂时无需学习它。

后面的教程统一使用 `.\.venv\Scripts\python.exe`，所以不需要激活环境。可选执行 `.\.venv\Scripts\Activate.ps1` 后用 `python` 简写；如果激活被策略阻止，继续使用完整路径即可。退出已激活环境用 `deactivate`。

## 4. 理解“运行代码”和“检查答案”

先在终端尝试：

```powershell
.\.venv\Scripts\python.exe -c "print('你好，Python！')"
```

应看到 `你好，Python！`。`print(...)` 输出括号内的内容，引号表示文字，`-c` 表示把后面的文字作为一小段 Python 代码运行。

通常我们把多行 Python 放进 `.py` 文件。用编辑器新建根目录下的 `hello.py`，保存为 UTF-8，写入：

```python
print("Hello, Python!")
```

然后执行：

```powershell
.\.venv\Scripts\python.exe hello.py
```

如果看到 `Hello, Python!`，说明保存与运行都正常。修改文件后需要先保存，再重新运行；终端不会自动读取尚未保存的编辑内容。`hello.py` 是你自己的试验文件，不是课程题目。

## 5. 开始第一题

课程题目由后续工作包生成；基础工具阶段计划入口是 `chapters/01_python/problems/P001/README.md`，此阶段不宣称该题已存在或已经验收。内容完成后，先读第 01 章教程与 P001 题面，再编辑相邻的 `exercise.py`。

在根目录运行以下命令即可列题与检查：

```powershell
.\.venv\Scripts\python.exe check.py --list
.\.venv\Scripts\python.exe check.py P001
.\.venv\Scripts\python.exe check.py --chapter 01
```

`--list` 列出题号、章节和标题。`P001` 只检查这题；`--chapter 01` 检查这一章。模拟卷内容完成后使用 `--chapter M01`。未发现题目、未知题号、空章节都会清楚报错。

要单独运行题目，可在根目录使用 `.\.venv\Scripts\python.exe chapters\01_python\problems\P001\exercise.py`。如果程序需要输入，按题面逐行输入并回车；程序等待输入时没有新提示不等于卡住。检查器会自动把案例输入送给程序。

## 6. 看懂检查结果

| 结果 | 含义与处理 |
| --- | --- |
| 通过 | 该案例输出符合题面 |
| 答案错误 | 对照案例、行数、每行元素数、数值与空格；删除临时 debug 输出 |
| 未完成 | 仍有 `raise NotImplementedError(...)`；按提示填写该位置 |
| 语法错误 | 先看报错指向的行，检查冒号、括号、引号与缩进 |
| 运行错误 | 语法有效，但运行时出错；如除以零、列表下标越界、输入读取错误 |
| 缺少模块 | 确认运行的是 `.venv` 的 Python，再安装 requirements |
| 超时 | 单案例默认 5 秒；检查循环是否结束、算法是否重复过多 |
| 环境问题 | 文件缺失或解释器无法启动，检查目录与完整课程文件 |

文本模式允许 Windows/Unix 换行差异、行末空白与末尾空行差异；行内文字仍须一致。整数模式要求十进制整数；`42.0` 不能代替 `42`。数值输出先检查行数和每行元素数；浮点允许绝对/相对误差 `1e-6`，不接受 NaN 或无穷大。不要输出“请输入数字”之类提示性文字。

同一题同时输出浮点数和整数标签时，检查器按题目案例指定的逐行规则判断；浮点行允许上述误差，整数标签行仍要求十进制整数，`0.0000001` 或 `1e0` 不能代替整数标签。

退出码用于脚本自动判断：`0` 是全部通过，`1` 是学习代码未通过，`2` 是参数、元数据或环境问题。PowerShell 可在命令结束后查看 `$LASTEXITCODE`。参考答案对照命令见根 README 的折叠入口；学习时先完成自己的练习。

## 资料依据

- [Python 3.11 虚拟环境教程](https://docs.python.org/3.11/tutorial/venv.html)：独立环境和 `python -m pip`。
- [Python subprocess 官方文档](https://docs.python.org/3.11/library/subprocess.html) 与 [CPython 3.11 实现](https://github.com/python/cpython/blob/3.11/Lib/subprocess.py)：独立进程、输入输出和超时。
- [NumPy 2.2.6 官方包信息](https://pypi.org/project/numpy/2.2.6/)：该固定版本要求 Python 3.10 及以上，并提供 Python 3.11 的 Windows 安装包。
