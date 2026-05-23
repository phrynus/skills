# 数据字典：ey_links

> **表说明**：友情链接表
> **字段数量**：21
> **引用此表的标签**：[links](../tags/links.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(11) | 否 | — | 主键 |
| `typeid` | tinyint(1) | 是 | 1 | 链接类型：1=文字链接，2=图片链接 |
| `groupid` | int(11) | 否 | 1 | 分组ID（默认分组值为1） |
| `title` | varchar(50) | 是 | — | 网站标题 |
| `url` | varchar(100) | 是 | — | 网站地址 |
| `logo` | varchar(255) | 是 | — | 网站LOGO图片路径 |
| `sort_order` | int(11) | 是 | 0 | 排序号 |
| `target` | tinyint(1) | 是 | 0 | 新窗口打开：0=否，1=是 |
| `nofollow` | tinyint(1) | 是 | 0 | nofollow：0=否，1=是 |
| `email` | varchar(50) | 是 | NULL | 联系邮箱 |
| `intro` | text | 是 | NULL | 网站简介 |
| `status` | tinyint(1) | 是 | 1 | 状态：0=屏蔽，1=显示 |
| `province_id` | int(10) | 是 | 0 | 省份ID |
| `city_id` | int(10) | 是 | 0 | 城市ID |
| `area_id` | int(10) | 是 | 0 | 区县ID |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `delete_time` | int(11) | 是 | 0 | 软删除时间戳 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
