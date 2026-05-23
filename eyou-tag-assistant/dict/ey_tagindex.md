# 数据字典：ey_tagindex

> **表说明**：TAG标签索引表，存储文档标签的统计信息
> **字段数量**：24
> **引用此表的标签**：[tags](../tags/tags.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(10) | 否 | — | 主键，tagID |
| `tag` | varchar(50) | 否 | — | TAG内容（关键词） |
| `typeid` | int(10) | 否 | 0 | 所属栏目ID |
| `litpic` | varchar(250) | 是 | — | TAG封面图 |
| `seo_title` | varchar(200) | 是 | — | SEO标题 |
| `seo_keywords` | varchar(200) | 是 | — | SEO关键词 |
| `seo_description` | text | 是 | NULL | SEO描述 |
| `count` | int(10) | 是 | 0 | 点击数 |
| `total` | int(10) | 是 | 0 | 关联文档总数 |
| `weekcc` | int(10) | 是 | 0 | 本周点击数 |
| `monthcc` | int(10) | 是 | 0 | 本月点击数 |
| `weekup` | int(10) | 是 | 0 | 本周新增文档数 |
| `monthup` | int(10) | 是 | 0 | 本月新增文档数 |
| `is_common` | tinyint(1) | 是 | 0 | 是否常用标签：0=否，1=是 |
| `sort_order` | int(10) | 是 | 100 | 排序号 |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `add_time` | int(10) | 是 | 0 | 添加时间（Unix时间戳） |
| `update_time` | int(10) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
| typeid | BTREE | 否 | typeid |
| count | BTREE | 否 | count |
| tag | BTREE | 否 | tag |
| lang | BTREE | 否 | lang |
