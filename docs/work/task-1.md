# Task 1：判题工具与运行环境

先读 docs/implementation-plan.md 的全局约束和统一接口，只实现本工作包。

交付 check.py、tests/test_checker.py、requirements.txt、setup.ps1、.gitignore、README.md 初始入口、docs/START_HERE.md 零基础环境教程。不创建课程正式题目，测试用临时题目 fixture。

使用 argparse、pathlib、subprocess、unittest。检查器从固定目录发现 cases.json，校验 ID/目录/metadata/至少五案例，重复 ID 清晰报错。子进程用 sys.executable，显式 UTF-8 输入输出环境，cwd 为题目目录。要能正确报告通过、答案错误、未完成、语法错误、运行错误、缺少模块、超时。返回值：全通过 0、学习代码未通过 1、参数/元数据/环境问题 2。未知题号和空章节不能当成功。执行器不导入学习代码到主进程。

暴露便于测试的 compare_output(actual, expected, mode)->(bool, str)，run_case(script_path, case, mode, timeout=5.0)->字典（status/message/stdout/stderr）。其他内部接口自行合理设计并在报告记录。测试用实际临时脚本 subprocess，不用 mock 假装执行成功。覆盖多余 debug 输出、数值接近但形状不符、整数非整数字符串、大整数精度、NaN/inf、中文路径、stdin、正确解、未实现、语法错误、缺少依赖、运行错误、超时、CLI 选择与退出码。

先写测试并记录预期失败，再实现工具。用现有 Python 的 base executable 创建本项目 .venv（现有 python 可 -m venv，ensurepip 可用）。安装并锁定一个实际可安装且兼容 Python 3.11 的 NumPy 版本；不要修改应用环境。setup.ps1 不改系统策略、不改全局 PATH，无须全局 pip；支持重复运行。README/START_HERE 以 `.\.venv\Scripts\python.exe` 为可靠主命令，说明激活只是可选。教程明确 py 启动器本机未配置，不把 py 作为唯一方案。P001 入口等可写指向后续计划的路径，但不宣称它已存在/验证。

不提交 Git，不改变 Git 身份；只改本包文件。报告写 docs/work/task-1-report.md，包含创建内容、测试先失败后通过证据、最终验证命令/结果、依赖版本、任何未解问题。完成只回简短状态与报告路径。
