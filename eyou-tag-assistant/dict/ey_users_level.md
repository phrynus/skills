# 数据字典：ey_users_level

> **表说明**：会员级别表，定义会员等级及其权限与升级条件
> **字段数量**：19
> **引用此表的标签**：[user](../tags/usertag.md) · [memberlist](../tags/memberlist.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `level_id` 🔑 | int(10) | 否 | — | 主键，级别ID |
| `level_name` | varchar(30) | 是 | — | 级别名称 |
| `level_value` | int(10) | 是 | 0 | 会员等级值（与 ey_users.level 对应） |
| `is_system` | tinyint(1) | 是 | 0 | 类型：0=用户自建，1=系统内置 |
| `amount` | decimal(10,2) | 是 | 0.00 | 开通该级别所需消费额度 |
| `down_count` | int(10) | 是 | 0 | 每天下载次数限制（0=不限） |
| `discount_type` | tinyint(1) | 否 | 1 | 折扣类型：0=不设置折扣，1=自定义折扣 |
| `discount` | float(10,2) | 是 | 100.00 | 折扣率（100=无折扣，90=9折） |
| `posts_count` | int(10) | 是 | 5 | 会员投稿次数限制 |
| `ask_is_release` | tinyint(1) | 是 | 1 | 允许在问答中发布问题：0=否，1=是 |
| `ask_is_review` | tinyint(1) | 是 | 0 | 问答内容是否需审核：0=否，1=是 |
| `upgrade_type` | tinyint(1) | 否 | 0 | 自动升级条件：0=不自动升级，1=按订单金额 |
| `upgrade_order_money` | decimal(10,2) | 否 | 0.00 | 累计订单满多少自动升级到此级别 |
| `status` | tinyint(1) | 否 | 1 | 状态：0=禁用，1=启用 |
| `lang` | varchar(20) | 是 | cn | 语言标识 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | level_id |
