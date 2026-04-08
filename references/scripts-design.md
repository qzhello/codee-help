# scripts 设计建议

这个文件用于说明 `codee` 后续脚本层的职责划分。

## 建议目录

```text
scripts/
├── codee_init.py
├── codee_help.py
├── codee_web.py
├── codee_impact.py
├── codee_command.py
├── codee_command_web.py
└── scanners/
    ├── repo_fingerprint.py
    ├── keyword_index.py
    ├── tree_sitter_index.py
    ├── git_hotspots.py
    ├── go_pkg_graph.py
    └── go_call_graph.py
```

## 各脚本职责

### codee_init.py

负责：

- 识别语言、版本、构建工具、依赖
- 扫描顶层目录与模块边界
- 提取项目入口、测试入口、部署入口
- 产出初始化总览文档

### codee_help.py

负责：

- 根据用户问题缩小扫描范围
- 抽取相关调用链、关键文件、关键方法
- 更新专题文档和关键词映射表
- 必要时把问题分发到 init / impact / command / web 的处理路径

### codee_web.py

负责：

- 读取既有 Markdown 文档
- 生成 HTML 导航页和专题页
- 展示版本、修改时间和产出日志

### codee_impact.py

负责：

- 从目标文件、方法或关键词定位修改点
- 分析调用链与依赖关系
- 汇总影响范围、测试建议和风险分级

### codee_command.py

负责：

- 扫描 CLI、HTTP 管理接口、shell 脚本与内部工具
- 提取命令名、参数、示例、风险与代码入口
- 生成命令目录的结构化中间数据

### codee_command_web.py

负责：

- 读取命令目录 JSON
- 生成命令手册 HTML 页面
- 让读者按命令名快速跳转查看参数、示例和风险

## 推荐工具组合

### 通用层

- `rg`：文本初筛
- `tree-sitter`：结构化语法扫描
- `ast-grep`：快速结构化检索
- `git`：热点和近期演进分析

### Go 项目

- `godepgraph`：包依赖图
- `golang.org/x/tools/cmd/callgraph`：函数级调用图

## 输出原则

脚本输出应尽量是结构化中间结果，再由模板层渲染成 Markdown/HTML。

输出风格目标：

- 高信息密度
- 默认可扫描
- 重点前置
- 表格优先于长段说明
- 便于后续继续机器处理

推荐中间格式：

- JSON：适合存放符号、依赖、调用边
- Markdown：适合最终阅读
