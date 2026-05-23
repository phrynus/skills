# 数据字典：ey_article_content

> **表说明**：文章附加表，与 `ey_archives` 一对一关联，存储正文内容（避免主表过大）
> **字段数量**：9
> **引用此表的标签**：[arcview](../tags/arcview.md) · [artlist](../tags/artlist.md) · [screening](../tags/screening.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(10) | 否 | — | 主键（自增） |
| `aid` | int(10) | 是 | 0 | 文档ID，关联 `ey_archives.aid` |
| `content` | longtext | 是 | NULL | PC端内容详情（富文本HTML） |
| `content_ey_m` | longtext | 是 | NULL | 手机端内容详情（富文本HTML） |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
| news_id | BTREE | 否 | aid |
