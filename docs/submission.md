# 最终提交索引

小组仓库地址：https://github.com/Autumn-XY/iot-repair-group24

选定语言：Python

| 成员 | GitHub用户名 | 任务Issue链接 | 主要PR链接 | 评审记录链接 |
| --- | --- | --- | --- | --- |
| A | Autumn-XY | https://github.com/Autumn-XY/iot-repair-group24/issues/1 | https://github.com/Autumn-XY/iot-repair-group24/pull/8 | https://github.com/Autumn-XY/iot-repair-group24/pull/8#pullrequestreview-5796526103 |
| B | LHWY-322 | https://github.com/Autumn-XY/iot-repair-group24/issues/2 | https://github.com/Autumn-XY/iot-repair-group24/pull/6 | https://github.com/Autumn-XY/iot-repair-group24/pull/6#issuecomment-6678894442 |
| C | yep316 | https://github.com/Autumn-XY/iot-repair-group24/issues/7 | https://github.com/Autumn-XY/iot-repair-group24/pull/9 | https://github.com/Autumn-XY/iot-repair-group24/pull/9#pullrequestreview-5796483633 |
| D | Xlb222333 | https://github.com/Autumn-XY/iot-repair-group24/issues/3 | https://github.com/Autumn-XY/iot-repair-group24/pull/4 | https://github.com/Autumn-XY/iot-repair-group24/pull/4#discussion_r4489604984 |

## 最终复核
main下载ZIP后运行的实际结果：
PS F:\1软件工程\实验 \iot-repair-starter\src\python> python test_status_rule.py
T01 PASS: PENDING -> PROCESSING, expected=True, actual=True
T02 PASS: PROCESSING -> COMPLETED, expected=True, actual=True
T03 PASS: PENDING -> COMPLETED, expected=False, actual=False
T04 PASS: COMPLETED -> PROCESSING, expected=False, actual=False
Summary: 4/4 passed

## 个人简短总结
A：负责仓库初始化与成员邀请，完成FR-01～FR-03三条需求（docs/requirements.md）及用例图（含可编辑源文件，docs/assets相对路径引用）。主要成果见本人Issue与主要PR。评审B的PR时核对：状态图只有"开始维修""完成维修"两条允许转换，COMPLETED为终态；类图中一台设备对应0..*工单、每张工单对应1台设备，多重性标注清楚，与需求一致，提交Approve。

B：完成工单状态图与简单类图（docs/models.md，含图源材料），状态名称与PENDING/PROCESSING/COMPLETED对应，未增加重新打开、撤销等状态。主要成果见本人Issue与主要PR。评审C的PR时核对：can_transition/canTransition除两条允许规则外均返回false，拒绝PENDING直接到COMPLETED的跳级和COMPLETED退回PROCESSING；docs/test-results.md含真实执行命令与终端输出，与状态图一致，提交Approve。

C：完成一种语言的状态判断函数（Python的can_transition），保留原文件名与参数，未修改测试预期值；先运行起始测试观察到2/4 passed、退出码1，补齐两条允许规则后4/4 passed、退出码0，并将真实输出写入docs/test-results.md。主要成果见本人Issue与主要PR。评审A的PR时核对：三个功能齐全、报修人与维修人员角色对应正确、提交工单初始状态为PENDING、异常与验收条件明确，提交Approve。

D：完成docs/acceptance.md验收清单，并从main下载ZIP独立复测，记录具体检查对象、操作及真实结果；未改写C的测试结果文件。主要成果见本人Issue与主要PR（分支docs/acceptance-d）。评审A的PR时核对需求与用例图三角色/三功能一致，指出/确认可检查项，提交Approve。

## 验收清单
- [ ] 3条功能需求完整
- [ ] 3种图齐全且源材料可编辑
- [ ] 一种语言的状态函数与4项测试
- [ ] 三人均有实际提交和同伴评审
- [ ] 三个主要PR均已合并
- [ ] 教师能够访问仓库
