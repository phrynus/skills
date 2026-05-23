# 数据字典：ey_guestbook_attribute

> **表说明**：留言表单属性定义表，定义留言/自由表单的字段结构
> **字段数量**：18
> **引用此表的标签**：[guestbookform](../tags/guestbookform.md) · [form](../tags/formtag.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `attr_id` 🔑 | int(11) | 否 | — | 主键，表单字段ID（模板中 `{$field.attr_N}` 的N即此值） |
| `attr_name` | varchar(60) | 是 | — | 字段名称（提示标签） |
| `typeid` | int(11) | 是 | 0 | 所属栏目ID（留言模型）或表单ID（自由表单） |
| `form_type` | tinyint(1) | 是 | 0 | 数据分类：0=留言模型，1=自由表单 |
| `attr_input_type` | tinyint(1) | 是 | 0 | 输入类型：0=文本框，1=下拉框，2=多行文本框 |
| `attr_values` | text | 是 | NULL | 下拉框/多选框的选项列表（换行分隔） |
| `is_showlist` | tinyint(1) | 是 | 0 | 在列表中显示：0=隐藏，1=显示 |
| `required` | tinyint(1) | 是 | 0 | 是否必填：0=否，1=是 |
| `validate_type` | smallint(5) | 是 | 0 | 验证格式：0=不验证，1=手机号，2=Email |
| `real_validate` | tinyint(1) | 是 | 0 | 是否真实验证：0=否，1=是 |
| `sort_order` | int(11) | 是 | 0 | 字段排序号 |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `is_del` | tinyint(1) | 是 | 0 | 是否已删除：0=否，1=是 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | attr_id |
| guest_id | BTREE | 否 | typeid |
