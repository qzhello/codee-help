# 安装与调用

## 1. Codex

安装目录：

- `~/.codex/skills/codee/`

安装步骤：

1. 创建 `~/.codex/skills/codee`
2. 复制当前目录全部内容到该目录
3. 重启或重新加载技能环境

最小安装集：

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `examples/`
- `evals/`
- `scripts/`

调用示例：

- `use codee-init on this repo`
- `use codee-help to find where compression is implemented`
- `use codee-impact to estimate the effect of changing this function`
- `use codee-command to organize ops commands`

## 2. Claude Code

Claude Code 常见接入方式不是统一的 skill 目录，而是把能力包装成项目命令或提示模板。

推荐方式：

1. 在项目内创建 `.claude/commands/codee.md`
2. 在文件中定义 `/codee` 是统一入口
3. 在命令说明里约定分流：
   - `codee-init`
   - `codee-help`
   - `codee-impact`
   - `codee-command`
   - `codee-web`

如果宿主支持全局 prompt/skill 目录，则保留本目录结构并按宿主要求复制。

## 3. 统一入口

推荐统一从 `/codee` 开始。

示例：

- `/codee 帮我找一下 seaweedfs 的压缩实现在哪里`
- `/codee 我想要运维手册中的 volume.list 命令的参数`
- `/codee 我准备改某个方法，先帮我分析影响范围`

## 4. 调用策略

| 用户意图 | 建议命令 |
| --- | --- |
| 先建立整体认知 | `codee-init` |
| 直接问某个实现或知识点 | `codee-help` |
| 改代码前看影响范围 | `codee-impact` |
| 整理命令/接口手册 | `codee-command` |
| 生成 HTML 手册 | `codee-web` |
