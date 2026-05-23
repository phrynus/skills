# 数据字典：ey_guestbook_attr

> **表说明**：留言表单属性值表，存储每条留言的各字段实际提交值
> **字段数量**：12
> **引用此表的标签**：[guestbookform](../tags/guestbookform.md) · [form](../tags/formtag.md) · [formreply](../tags/formreply.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `guest_attr_id` 🔑 | int(11) | 否 | — | 主键，自增ID |
| `aid` | mediumint(8) | 否 | 0 | 关联留言ID（`ey_guestbook.aid`） |
| `form_type` | tinyint(1) | 是 | 0 | 数据分类：0=留言模型，1=自由表单 |
| `attr_id` | int(11) | 否 | 0 | 表单字段ID（`ey_guestbook_attribute.attr_id`） |
| `attr_value` | text | 是 | NULL | 字段提交值 |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | guest_attr_id |
| attr_id | BTREE | 否 | attr_id |
| guest_id | BTREE | 否 | aid |
