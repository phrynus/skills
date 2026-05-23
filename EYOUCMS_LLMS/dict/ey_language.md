# 数据字典：ey_language

> **表说明**：多语言主表，存储网站配置的各语言版本信息
> **字段数量**：14
> **引用此表的标签**：[language](../tags/language.md) · [lang](../tags/lang.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(10) | 否 | — | 主键，语言ID |
| `title` | varchar(100) | 否 | — | 语言名称（如"简体中文"、"English"） |
| `mark` | varchar(50) | 否 | — | 语言标识符（唯一，如 cn、en） |
| `url` | varchar(200) | 否 | — | 语言独立域名或路径 |
| `target` | tinyint(1) | 否 | 0 | 新窗口打开：0=否，1=是 |
| `is_home_default` | tinyint(1) | 是 | 0 | 默认前台语言：0=否，1=是 |
| `is_admin_default` | tinyint(1) | 是 | 0 | 默认后台语言：0=否，1=是 |
| `syn_pack_id` | int(10) | 是 | 0 | 最后一次同步的官方语言包ID |
| `status` | tinyint(1) | 否 | 0 | 语言状态：0=关闭，1=开启 |
| `sort_order` | int(10) | 是 | 0 | 排序号 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
