# 数据字典：ey_users

> **表说明**：会员信息表，存储注册会员的账号与个人信息
> **字段数量**：47
> **引用此表的标签**：[user](../tags/usertag.md) · [memberlist](../tags/memberlist.md) · [memberinfos](../tags/memberinfos.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `users_id` 🔑 | int(11) | 否 | — | 主键，会员ID |
| `username` | varchar(30) | 否 | — | 用户名（登录账号） |
| `password` | varchar(255) | 否 | — | 登录密码（加密存储） |
| `nickname` | varchar(50) | 否 | — | 昵称（显示名） |
| `is_mobile` | tinyint(1) | 是 | 0 | 是否绑定手机：0=否，1=是 |
| `mobile` | varchar(20) | 否 | — | 手机号码（用于登录） |
| `is_email` | tinyint(1) | 是 | 0 | 是否绑定邮箱：0=否，1=是 |
| `email` | varchar(60) | 否 | — | 电子邮件（用于登录） |
| `paypwd` | varchar(255) | 是 | — | 支付密码（预留字段） |
| `users_money` | decimal(20,2) | 是 | 0.00 | 账户余额 |
| `frozen_money` | decimal(20,2) | 是 | 0.00 | 冻结金额 |
| `scores` | int(10) | 是 | 0 | 积分 |
| `devote` | int(10) | 是 | 0 | 贡献值 |
| `reg_time` | int(11) | 是 | 0 | 注册时间（Unix时间戳） |
| `last_login` | int(11) | 是 | 0 | 最后登录时间 |
| `last_ip` | varchar(15) | 是 | — | 最后登录IP |
| `login_count` | int(11) | 是 | 0 | 登录次数 |
| `head_pic` | varchar(255) | 是 | — | 头像图片路径 |
| `province` | int(6) | 是 | 0 | 省份ID |
| `city` | int(6) | 是 | 0 | 城市ID |
| `district` | int(6) | 是 | 0 | 区县ID |
| `level` | smallint(5) | 是 | 0 | 会员等级值 |
| `open_level_time` | int(11) | 是 | 0 | 开通会员级别时间 |
| `level_maturity_days` | varchar(20) | 是 | — | 会员级别到期天数 |
| `discount` | decimal(20,2) | 是 | 1.00 | 会员折扣（1.00=无折扣） |
| `total_amount` | decimal(20,2) | 是 | 0.00 | 累计消费额度 |
| `order_total_amount` | decimal(20,2) | 是 | 0.00 | 订单累计总额（用于自动升级） |
| `is_activation` | tinyint(1) | 是 | 1 | 是否激活：0=否，1=是 |
| `register_place` | tinyint(1) | 是 | 2 | 注册来源：1=后台，2=前台 |
| `open_id` | varchar(50) | 否 | — | 第三方openid |
| `thirdparty` | tinyint(1) | 是 | 0 | 第三方注册类型：0=普通，1=微信，2=QQ，3=手机 |
| `is_lock` | tinyint(1) | 是 | 0 | 是否被锁定：0=否，1=是 |
| `admin_id` | int(10) | 是 | 0 | 关联管理员ID |
| `lang` | varchar(20) | 是 | cn | 语言标识 |
| `is_del` | tinyint(1) | 是 | 0 | 伪删除：0=否，1=是 |
| `unread_notice_num` | int(10) | 否 | 0 | 未读站内信数量 |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |
| `sex` | varchar(10) | 是 | 保密 | 性别：男/女/保密 |
| `coin` | int(11) | 是 | 0 | 金币数量 |
| `union_id` | varchar(50) | 否 | — | 微信unionId |
| `source` | tinyint(3) | 是 | 1 | 来源：1=PC，2=H5，3=微信公众号，4=微信小程序 |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | users_id |
| union_id | BTREE | 否 | union_id |
| username | BTREE | 否 | username |
| mobile | BTREE | 否 | mobile |
| open_id | BTREE | 否 | open_id |
