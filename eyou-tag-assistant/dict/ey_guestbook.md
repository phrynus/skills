# 数据字典：ey_guestbook

> **表说明**：留言主表，存储用户提交的留言/表单记录
> **字段数量**：19
> **引用此表的标签**：[guestbookform](../tags/guestbookform.md) · [form](../tags/formtag.md) · [formreply](../tags/formreply.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `aid` 🔑 | int(11) | 否 | — | 主键，留言ID |
| `form_type` | tinyint(1) | 是 | 0 | 数据分类：0=留言模型，1=自由表单 |
| `typeid` | int(11) | 是 | 0 | 栏目ID（留言模型）或表单ID（自由表单） |
| `channel` | smallint(5) | 是 | 0 | 模型ID |
| `users_id` | int(11) | 是 | 0 | 提交用户ID（0=游客） |
| `md5data` | varchar(50) | 是 | — | 提交内容的MD5（用于防重复提交） |
| `ip` | varchar(255) | 是 | — | 提交来源IP |
| `is_read` | tinyint(1) | 是 | 0 | 是否已读：0=未读，1=已读 |
| `is_star` | tinyint(1) | 是 | 0 | 星标标记：0=否，1=是 |
| `source` | tinyint(1) | 是 | 0 | 提交来源：1=电脑端，2=手机端 |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `add_time` | int(11) | 是 | 0 | 提交时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |
| `reply` | varchar(1000) | 是 | — | 管理员回复内容 |
| `admin_id` | int(11) | 是 | 0 | 回复管理员ID |
| `reply_time` | int(11) | 是 | 0 | 回复时间（Unix时间戳） |
| `examine` | tinyint(1) | 是 | 1 | 审核状态：0=未审核，1=通过，2=不通过 |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | aid |
