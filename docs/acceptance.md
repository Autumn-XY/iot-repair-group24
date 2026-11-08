# 验收清单与复测记录（任务D）

负责人：Xlb222333　状态规则依据：仅允许 PENDING→PROCESSING、PROCESSING→COMPLETED，其余一律拒绝。

## 一、验收清单

### 1. A：需求说明与用例图
- [ ] FR-01 查看设备、FR-02 提交报修、FR-03 更新状态三条齐全，编号固定
- [ ] 每条需求包含角色、前置条件、输入、正常结果、异常结果、可检查的验收条件
- [ ] FR-02 中工单创建后的初始状态为 PENDING
- [ ] FR-03 明确写出其余转换一律拒绝（含跳级、回退、相同状态）
- [ ] 用例图含系统边界、报修人与维修人员两个参与者、查看设备/提交报修/更新工单状态三个用例，连线与角色权限一致
- [ ] 未把数据库或设备本身画成操作者
- [ ] 用例图 PNG 可打开，可编辑源文件已提交至 docs/assets，usecase.md 使用相对路径 assets/xxx 引用

### 2. B：状态图与简单类图
- [ ] 状态图初始进入待处理 PENDING
- [ ] 仅"开始维修"（PENDING→PROCESSING）与"完成维修"（PROCESSING→COMPLETED）两条转换
- [ ] 已完成为终态，无重新打开、撤销等额外状态或转换
- [ ] 类图 Device 含 deviceId、name、location；WorkOrder 含 orderId、deviceId、description、status
- [ ] 多重性标注：一台设备对应 0..* 张工单，每张工单对应 1 台设备
- [ ] 图与需求说明、状态名称前后一致；若用 Mermaid，代码块完整可渲染

### 3. C：状态判断函数与测试记录
- [ ] 仅两条允许转换返回 true，其余（含相同状态）一律返回 false
- [ ] 未修改测试文件中的预期值，文件名、参数名保持原样
- [ ] test-results.md 写明选用语言、环境版本、执行命令、测试者用户名、四项实际结果及真实终端输出代码块
- [ ] 说明"本次覆盖规定的4项场景，其他状态组合尚未全部执行"
- [ ] 未提交 .class、`__pycache__` 或整个 IDE 工程目录

### 4. 仓库与协作完整性
- [ ] README 登记组号、各成员 GitHub 用户名、选定语言（只完成一种）
- [ ] 三个模型均可在线查看，可编辑源材料可下载
- [ ] main 为最终验收版本，docs/submission.md 链接可打开且内容齐全
- [ ] 关联 Issue 均已关闭；各成员有本人 Issue、主要 PR 和一次真实评审记录

## 二、main 复测记录（实验二）

- 复测版本来源：main 分支 Download ZIP
- 下载日期：2026-11-06
- 选用语言：Python 3 (Windows)
- 运行环境：Windows + Python 3
- 执行命令：python test_status_rule.py
- 四项实际结果：

| 编号 | 当前状态 | 目标状态 | 预期 | 实际 | 结论 |
| --- | --- | --- | --- | --- | --- |
| T01 | PENDING | PROCESSING | true | true | PASS |
| T02 | PROCESSING | COMPLETED | true | true | PASS |
| T03 | PENDING | COMPLETED | false | false | PASS |
| T04 | COMPLETED | PROCESSING | false | false | PASS |

真实终端输出：

```text
PS F:\1软件工程\实验 \iot-repair-starter\src\python> python test_status_rule.py
T01 PASS: PENDING -> PROCESSING, expected=True, actual=True
T02 PASS: PROCESSING -> COMPLETED, expected=True, actual=True
T03 PASS: PENDING -> COMPLETED, expected=False, actual=False
T04 PASS: COMPLETED -> PROCESSING, expected=False, actual=False
Summary: 4/4 passed

结论：main 中代码与测试记录一致，规定 4 项全部通过；本次复测覆盖规定的 4 项场景，其他状态组合尚未全部执行。
