# codee-help

Unified codebase assistant skill for architecture init, targeted code help, impact analysis, ops command cataloging, and handbook generation.

`codee-help` is a bilingual skill package designed for technical code reading, architecture initialization, change impact analysis, ops command documentation, and handbook generation.

## English

### What It Does

- `codee-init`: initialize project-wide architecture understanding
- `codee-help`: answer focused codebase questions from a single `/codee` entry
- `codee-impact`: analyze change impact before code modification
- `codee-command`: organize ops commands, admin APIs, and scripts
- `codee-web`: generate HTML handbooks from accumulated docs

### Install

For Codex:

1. Copy this directory to `~/.codex/skills/codee/`
2. Keep at least:
   - `SKILL.md`
   - `agents/openai.yaml`
   - `references/`
   - `examples/`
   - `evals/`
   - `scripts/`

For Claude Code:

1. Create `.claude/commands/codee.md`
2. Reuse the example in `examples/claude-command.codee.md`
3. Route `/codee` requests to the appropriate mode

### Examples

- `/codee help me find where SeaweedFS compression is implemented`
- `/codee show me the parameters of volume.list in the ops manual`
- `/codee analyze the impact before I change this function`

## 中文

### 这个 skill 做什么

- `codee-init`：初始化项目整体架构认知
- `codee-help`：统一从 `/codee` 入口回答代码问题
- `codee-impact`：改代码前分析影响范围
- `codee-command`：整理运维命令、管理接口、脚本手册
- `codee-web`：把沉淀文档生成 HTML 阅读手册

### 安装方式

Codex：

1. 把当前目录复制到 `~/.codex/skills/codee/`
2. 至少保留：
   - `SKILL.md`
   - `agents/openai.yaml`
   - `references/`
   - `examples/`
   - `evals/`
   - `scripts/`

Claude Code：

1. 在项目里创建 `.claude/commands/codee.md`
2. 参考 `examples/claude-command.codee.md`
3. 统一从 `/codee` 入口分流到不同能力

### 调用示例

- `/codee 帮我找一下 seaweedfs 的压缩实现在哪里`
- `/codee 我想要运维手册中的 volume.list 命令的参数`
- `/codee 我准备改某个方法，先帮我分析影响范围`

### 目录说明

- `SKILL.md`：主说明
- `references/`：模板、安装说明、脚本设计
- `examples/`：示例输入输出与命令样板
- `evals/`：评估清单
- `scripts/`：脚本入口
