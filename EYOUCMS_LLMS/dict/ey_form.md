# 数据字典：ey_form

> **表说明**：表单管理表，存储后台创建的自由表单基础信息
> **字段数量**：12
> **引用此表的标签**：[form](../tags/formtag.md) · [formreply](../tags/formreply.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `form_id` 🔑 | int(11) | 否 | — | 主键，表单ID（模板中 `formid` 参数填此值） |
| `form_name` | varchar(255) | 否 | — | 表单名称 |
| `intro` | text | 否 | — | 表单描述（预留字段） |
| `status` | tinyint(1) | 否 | 1 | 表单状态：0=关闭，1=开启 |
| `attr_auto` | tinyint(1) | 是 | 0 | 自动标签模式：0=否，1=是（type='auto'时） |
| `lang` | varchar(10) | 否 | cn | 语言标识 |
| `add_time` | int(11) | 否 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 否 | 0 | 更新时间（Unix时间戳） |
| `open_reply` | tinyint(1) | 是 | 0 | 是否开启回复：0=否，1=是 |
| `open_examine` | tinyint(1) | 是 | 0 | 是否开启审核：0=否，1=是 |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | form_id |
