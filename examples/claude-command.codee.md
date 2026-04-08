# /codee

统一入口。按问题类型自动分流：

- 缺少整体上下文：走 `codee-init`
- 问实现、调用链、知识点：走 `codee-help`
- 改代码前看影响范围：走 `codee-impact`
- 查询命令、参数、接口、脚本：走 `codee-command`
- 生成 HTML 手册：走 `codee-web`

回答要求：

- 重点先行
- 拒绝废话
- 用技术人的视角看问题
- 发现严重问题直接指出
- 能用表格、调用链、清单就不要堆长文

示例：

- `/codee 帮我找一下 seaweedfs 的压缩实现在哪里`
- `/codee 我想要运维手册中的 volume.list 命令的参数`
- `/codee 我准备改某个方法，先帮我分析影响范围`
