# Skills

Claude Code / AI Coding Assistant 的 Skills 存放仓库，提供领域专业知识以增强 AI 编程助手的准确性和效率。

---

## 📦 仓库结构

```
skills/
├── eyou-tag-assistant/     # EyouCMS 模板标签专家
├── eyou-wrap-helper/       # EyouCMS 套标签助手
├── EYOUCMS_LLMS/           # EyouCMS 模板标签 LLM 手册
├── go-binance/             # go-binance 币安 API 开发助手
└── README.md
```

---

## 🏷️ Skills 列表

### 1. eyou-tag-assistant — EyouCMS 模板标签专家

**用途**：为 AI 助手提供 EyouCMS（易优CMS）模板标签的准确语法查询能力，覆盖所有内置标签的参数、变量、嵌套规则。

**触发场景**：
- 编写或修改 EyouCMS 模板标签（`{eyou:xxx}` 格式）
- 查询标签用法、参数、可用变量
- 排查标签不生效、页面空白等问题
- 将静态 HTML 转换为 EyouCMS 动态模板

**核心原则**：先查手册，再写代码——禁止凭记忆写标签。

**包含内容**：
- 60+ 标签文档（`tags/`）
- 15+ 数据字典（`dict/`）
- 完整 LLM 使用手册（`LLMS.md`）

---

### 2. eyou-wrap-helper — EyouCMS 套标签助手

**用途**：扒站后将静态 HTML 快速替换为 EyouCMS 基础模板标签，保持原有结构不变。

**触发场景**：
- 有静态 HTML 页面需要套上 EyouCMS 标签
- 需要提取 header/nav/footer 公共部分
- 批量重命名模板文件

**包含内容**：
- 基础标签速查表（`references/basic-tags.md`）
- 命令行辅助脚本（`scripts/wrap.py`）

**快速上手**：
```bash
python wrap.py init index.html       # 从首页提取公共部分
python wrap.py scan about.html       # 扫描硬编码内容
python wrap.py rename ./templates    # 批量重命名文件
```

---

### 3. EYOUCMS_LLMS — EyouCMS 模板标签 LLM 手册

**用途**：EyouCMS 模板开发的完整参考手册，涵盖所有标签文档、数据字典、编码规范。

**包含内容**：
- `LLMS.md` — 标签文档索引与速查表
- `tags/` — 每个标签的独立文档（60+ 标签）
- `dict/` — 数据表字段字典（15+ 张表）
- `编写规范.md` — 前端模板编码规范
- `标签规划.md` — 标签规划说明
- `风格决策.md` — UI 风格决策指南
- `提示词.md` — 模板生成提示词模板
- `问题记录.md` — 常见问题与解决方案
- `html/` — HTML 模板示例

**适用场景**：
- AI 辅助生成整站模板
- 查询特定标签的完整用法
- 了解数据表结构，正确使用字段变量

---

### 4. go-binance — 币安 API Golang 开发助手

**用途**：为 AI 助手提供 go-binance（`github.com/adshao/go-binance/v2`）SDK 的完整使用指南，覆盖币安全产品线 API。

**触发场景**：
- 使用 go-binance SDK 进行现货/合约/杠杆/期权交易
- 获取行情数据、K线、深度
- 实现量化策略、交易机器人
- 调用 Binance API 的任何场景

**包含内容**：

| 模块 | 文件 | 说明 |
|------|------|------|
| 通用 | `common.md` | 客户端初始化、基础类型 |
| 现货 | `spot.md` | 下单、K线、账户 |
| USDT-M 合约 | `futures.md` | 合约下单、持仓、杠杆 |
| 币本位合约 | `delivery.md` | 币本位合约交易 |
| 杠杆 | `margin.md` | 借贷、利率、OCO |
| 期权 | `options.md` | 期权下单、行权 |
| 钱包 | `wallet.md` | 充值、提现、转账 |
| 子账户 | `subaccount.md` | 子账户管理 |
| 理财 | `savings.md` | 灵活/定期储蓄 |
| 组合保证金 | `portfolio.md` | 组合保证金账户 |
| 参考 | `reference.md` | 项目结构、限频、错误码 |

---

## 🚀 使用方式

将这些 Skills 目录放置到 AI 编程助手（如 Claude Code、GitHub Copilot 等）的 Skills 目录中，助手将在相关场景下自动加载对应 Skill，提供更准确、更专业的回答。

---

## 📄 许可证

仅供个人学习和参考使用。
