# 实际测试记录

语言与版本：Python 3 (Windows)

测试人员GitHub用户名：yep316

运行命令：python test_status_rule.py

| 编号 | 当前状态 | 目标状态 | 预期 | 实际 | 结论 |
| --- | --- | --- | --- | --- | --- |
| T01 | PENDING | PROCESSING | true | true | PASS |
| T02 | PROCESSING | COMPLETED | true | true | PASS |
| T03 | PENDING | COMPLETED | false | false | PASS |
| T04 | COMPLETED | PROCESSING | false | false | PASS |

## 原始输出

```text
T01 PASS: PENDING -> PROCESSING, expected=True, actual=True
T02 PASS: PROCESSING -> COMPLETED, expected=True, actual=True
T03 PASS: PENDING -> COMPLETED, expected=False, actual=False
T04 PASS: COMPLETED -> PROCESSING, expected=False, actual=False
Summary: 4/4 passed
