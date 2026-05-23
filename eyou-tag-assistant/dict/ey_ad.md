# 数据字典：ey_ad

> **表说明**：广告表，存储广告位的广告内容
> **字段数量**：26
> **引用此表的标签**：[adv](../tags/adv.md) · [ad](../tags/ad.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(11) | 否 | — | 主键，广告ID |
| `pid` | int(11) | 否 | 0 | 广告位置ID（关联广告位） |
| `media_type` | tinyint(1) | 是 | 0 | 广告类型（0=图片，1=Flash，2=代码） |
| `title` | varchar(60) | 是 | — | 广告名称 |
| `links` | varchar(255) | 是 | — | 广告点击链接URL |
| `litpic` | varchar(255) | 是 | — | 广告图片路径 |
| `start_time` | int(11) | 是 | 0 | 投放开始时间（Unix时间戳） |
| `end_time` | int(11) | 是 | 0 | 投放结束时间（Unix时间戳） |
| `intro` | text | 是 | NULL | 广告描述 |
| `link_man` | varchar(60) | 是 | — | 广告主联系人 |
| `link_email` | varchar(60) | 是 | — | 广告主邮箱 |
| `link_phone` | varchar(60) | 是 | — | 广告主电话 |
| `click` | int(11) | 是 | 0 | 点击量 |
| `bgcolor` | varchar(30) | 是 | — | 背景颜色 |
| `status` | tinyint(1) | 是 | 1 | 状态：0=屏蔽，1=显示 |
| `sort_order` | int(11) | 是 | 0 | 排序号 |
| `target` | varchar(50) | 是 | — | 是否新窗口打开 |
| `admin_id` | int(10) | 是 | 0 | 管理员ID |
| `is_del` | tinyint(1) | 是 | 0 | 伪删除：0=否，1=是 |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
| position_id | BTREE | 否 | pid |
| status | BTREE | 否 | status |
