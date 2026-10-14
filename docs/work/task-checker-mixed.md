# 检查器补充：混合输出行类型

Task4发现P044等题同时输出浮点中心和整数标签。统一float会误接受小数标签，必须支持逐行模式。保持现有全部CLI、旧metadata、函数调用兼容。

- 每个case可选 `line_modes: ["float", "float", "int"]`，长度等于规范化expected输出行数。只接受list和三个合法字符串；非法metadata清晰错误退出2。
- `compare_output(actual, expected, mode, line_modes=None)` 保留原3参数调用。先校验所有行数和数值行元素数，再按对应行模式比较。text行规则不变。所有数字拒绝非有限值。
- run_case/_run_case 和metadata校验接入case可选字段；旧题保持原行为。
- 测试先行：混合输出合法通过；float行容差通过；int标签0.0000001拒绝、1e0拒绝；非法模式或长度拒绝；mixed行形状不匹配先于值比较；旧29测试回归通过。
- 文档 START_HERE 可简要说明整数标签仍严格判断。更新 docs/implementation-plan.md 已有合同并为后续维护文档提供说明。
- 只改 check.py/tests/test_checker.py/必要工具文档，不改课程练习或答案；本任务将在Task4内容交付后执行，避免同包多个实现者并行。
- 报告 docs/work/task-checker-mixed-report.md，不提交Git。
