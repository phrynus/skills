# 数据字典：ey_search_word

> **表说明**：搜索词统计表，记录用户搜索行为
> **字段数量**：14
> **引用此表的标签**：[hotkeywords](../tags/hotkeywords.md) · [searchform](../tags/searchform.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(10) | 否 | — | 主键 |
| `word` | varchar(255) | 是 | — | 搜索关键词 |
| `searchNum` | int(10) | 是 | 1 | 搜索次数 |
| `resultNum` | int(10) | 是 | 0 | 搜索结果数量 |
| `sort_order` | int(10) | 是 | 0 | 排序号 |
| `users_id` | int(11) | 是 | 0 | 搜索用户ID |
| `ip` | varchar(20) | 是 | — | 搜索来源IP |
| `is_hot` | tinyint(1) | 是 | 0 | 是否热搜词：0=否，1=是 |
| `lang` | varchar(30) | 是 | cn | 语言标识 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
| word | BTREE | 否 | word |
