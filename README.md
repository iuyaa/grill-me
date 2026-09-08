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

### 已内置上游 `grilling`

Grill 已将 Matt Pocock 的 [`grilling`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)作为受约束的 interrogation primitive 内置在 [`upstream-grilling.md`](grill/references/upstream-grilling.md) 中，用户不需要额外安装。GitHub Action 每周检查上游；发现变化时只创建 PR，审核合并后才会影响用户。

## 使用

用户不需要先选择工作流，直接提出问题即可：

```text
$grill 我们是否应该把客户线索系统改造成 Agent？
```

Grill 会自动判断范围、调查可获取的事实、构造决策依赖图，并只询问当前可以决定的 frontier。存在真实选项时，每个问题会给出推荐答案、理由、可逆性和影响。

宿主当前支持结构化选择菜单时，Grill 优先使用菜单；否则回退为可移植的 A/B/C 文字选项。它不会仅为了显示菜单而切换宿主模式。

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

- Fact 由 Agent 调查，Decision 由用户决定。
- 问题按依赖 frontier 分轮提出，不使用固定问卷。
- 推荐答案不等于用户批准。
- 未批准设计前不进入实现。
- `check` 默认只读，不自动修复或篡改批准基线。
- 缺少证据时明确标记 `MISSING_EVIDENCE` 或 `NOT_RUN`。

需要跨会话保存时，工作状态默认写入：

```text
.grill/<session>/
```

其中可以包含 checkpoint、决策地图、批准 Spec 和一致性检查报告。

## 来源

本 Skill 吸收了 Matt Pocock `grilling`、`grill-with-docs`、`wayfinder` 的决策与地图思想，以及 Superpowers `brainstorming` 的流程分级、批准闸门和 Spec 自检设计。具体版本和 MIT 许可见 [第三方声明](grill/THIRD_PARTY_NOTICES.md)。
