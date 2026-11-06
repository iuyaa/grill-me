# Grill

一个面向 Codex 和 Claude Code 的决策澄清 Skill：调查事实、按依赖顺序询问用户、冻结批准方案，并在实现后检查一致性。

## 安装

克隆仓库：

```bash
git clone https://github.com/iuyaa/grill-me.git
```

然后将仓库中的 `grill/` 目录复制到对应位置：

| 宿主 | 个人安装目录 | 调用方式 |
| --- | --- | --- |
| Codex | `~/.codex/skills/grill/` | `$grill <问题>` |
| Claude Code | `~/.claude/skills/grill/` | `/grill <问题>` |

也可以把 `grill/` 放入项目自己的 Skill 目录，仅对该项目生效。

### 使用前检查更新

从 `2.1.0` 起，Agent 在每个新会话首次使用 Grill 时，先检查本仓库 `main` 中的版本。有更新且本地安装未被修改时，先备份，再更新完整的 `grill/`，重新读取规则后继续；同一会话的提问轮次不重复检查。Codex／CC-Switch 等共享目录只更新实际目标一次。

更新依据内置版本号与 `manifest.json` 校验清单，避免覆盖本地开发版本。离线、检查失败、本地改动、版本固定或只读要求会保留当前安装并说明原因。这个机制由宿主 Agent 执行，不是后台更新服务，也不会自动提交、推送或改写项目决策记录。首次发布前，本机未发布的新版本不会被远端旧版本覆盖。

维护者发布前为 Skill 的每次内容变更递增 `metadata.version`，用 Python 3.10+ 运行 `python scripts/package_skill.py` 更新校验清单，再用 `python scripts/package_skill.py --check` 校验，并将 Skill 与清单一起提交。上游 `grilling` 的同步 PR 会自动递增补丁版本、更新清单；这个维护工具不要求 Skill 的使用者安装 Python。

### 已内置上游 `grilling`

Grill 已将 Matt Pocock 的 [`grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)作为受约束的 interrogation primitive 内置在 [`upstream-grilling.md`](grill/references/upstream-grilling.md) 中，用户不需要额外安装。GitHub Action 每周检查上游；发现变化时只创建 PR，审核合并后才会影响用户。

自动创建 PR 需要仓库允许 GitHub Actions 创建拉取请求；只有更新分支而没有成功创建 PR，不代表主分支已同步。Superpowers 的规则由本项目选择性整合，不在该 Action 的同步范围内。

## 使用

用户不需要先选择工作流，直接提出问题即可：

```text
$grill 我们是否应该把客户线索系统改造成 Agent？
```

Grill 会先读上下文、调查可获取的事实，只追问会影响结果且无法自行消除的关键缺口。目的尚不清楚时，先让用户自由描述；到了具体取舍，再按依赖 frontier 分轮给出选项、推荐、理由和影响。每个分支收敛后简短复述，区分用户决定、受委托的 Agent 选择和尚未确认的建议。

具体选择题优先使用宿主菜单，每项包含标题和解释，推荐项排第一；开放题不附预设答案。宿主不支持时回退为文字，不为菜单切换模式。具体推荐的问法让“是”表示接受该推荐；多题后的含糊“是”不会被当成全部同意。

已明确的小任务不会自动进入访谈。用户可以停止提问；如果同时要求执行，Agent 会说明受委托的选择并在原有授权范围内继续，但不会把退出当成设计批准。需要时用草图或一次性实验辅助讨论；小改动保留聊天设计，大设计补充实施者视角检查，不强制引入其他 Skill。

## 模式

自然语言入口会自动路由，也可以显式指定：

| 模式 | 用途 |
| --- | --- |
| `map` | 把大型目标拆成有依赖关系的决策票据 |
| `plan` | 把一个功能、设计或决策收敛为批准方案 |
| `resume` | 恢复持久化的决策会话 |
| `status` | 查看已决定、可决定、阻塞、延后和范围外事项 |
| `publish` | 将批准结果沉淀到项目文档 |
| `check` | 按批准基线检查实现并报告偏差 |

例如：

```text
$grill map 建设公司级 AI 数据平台
$grill check 检查当前实现是否符合已批准方案
```

## 核心边界

- Fact 由 Agent 调查；用户掌握决策权，可以明确委托部分选择，并保留决定来源。
- 问题按依赖 frontier 分轮提出，不使用固定问卷。
- 推荐答案不等于用户批准。
- 访谈内先批准具体设计再实现；退出访谈不批准草稿、不新增执行权限。
- `check` 默认只读，不自动修复或篡改批准基线。
- 缺少证据时明确标记 `MISSING_EVIDENCE` 或 `NOT_RUN`。

需要跨会话保存时，工作状态默认写入：

```text
.grill/<session>/
```

其中可以包含 checkpoint、决策地图、批准 Spec 和一致性检查报告。

## 来源

本 Skill 吸收了 Matt Pocock `grilling`（内置提交 `7739eae`）、`grill-with-docs`、`wayfinder` 的决策与地图思想，以及 Superpowers `brainstorming` v7.0.2 的目的澄清、阶段复述、决策委托、退出访谈和设计检查。保留原有轻量分级与批准基线。具体版本和 MIT 许可见 [第三方声明](grill/THIRD_PARTY_NOTICES.md)。
