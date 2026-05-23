# 数据字典：ey_archives

> **表说明**：文档主表，存储所有模型文档的公共字段
> **字段数量**：71
> **引用此表的标签**：[artlist](../tags/artlist.md) · [list](../tags/list.md) · [arcview](../tags/arcview.md) · [relevarticle](../tags/relevarticle.md) · [beafter](../tags/beafter.md) · [specialnode](../tags/specialnode.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `aid` 🔑 | int(10) | 否 | — | 主键，文档ID |
| `typeid` | int(10) | 否 | 0 | 当前所属栏目ID |
| `stypeid` | varchar(90) | 是 | — | 副栏目ID集合（逗号分隔） |
| `channel` | int(10) | 否 | 0 | 模型ID |
| `is_b` | tinyint(1) | 是 | 0 | 加粗标记 |
| `title` | varchar(500) | 是 | — | 文档标题 |
| `subtitle` | varchar(500) | 是 | — | 副标题 |
| `litpic` | varchar(250) | 是 | — | 封面图片路径 |
| `is_head` | tinyint(1) | 是 | 0 | 头条：0=否，1=是 |
| `is_special` | tinyint(1) | 是 | 0 | 特荐：0=否，1=是 |
| `is_top` | tinyint(1) | 是 | 0 | 置顶：0=否，1=是 |
| `is_recom` | tinyint(1) | 是 | 0 | 推荐：0=否，1=是 |
| `is_jump` | tinyint(1) | 是 | 0 | 跳转链接：0=否，1=是 |
| `is_litpic` | tinyint(1) | 是 | 0 | 有图标记：0=否，1=是 |
| `is_roll` | tinyint(1) | 否 | 0 | 滚动：0=否，1=是 |
| `is_slide` | tinyint(1) | 否 | 0 | 幻灯：0=否，1=是 |
| `is_diyattr` | tinyint(1) | 否 | 0 | 自定义属性：0=否，1=是 |
| `origin` | varchar(200) | 是 | — | 来源 |
| `author` | varchar(200) | 是 | — | 作者 |
| `click` | int(10) | 是 | 0 | 点击数 |
| `arcrank` | int(10) | 是 | 0 | 阅读权限：0=开放，-1=待审核 |
| `jumplinks` | varchar(255) | 是 | — | 跳转网址 |
| `ismake` | tinyint(1) | 是 | 0 | 是否静态页面：0=动态，1=静态 |
| `seo_title` | varchar(500) | 是 | — | SEO标题 |
| `seo_keywords` | varchar(500) | 是 | — | SEO关键词 |
| `seo_description` | text | 是 | NULL | SEO描述 |
| `attrlist_id` | int(10) | 否 | 0 | 商品参数列表ID |
| `merchant_id` | int(11) | 否 | 0 | 多商家ID |
| `free_shipping` | tinyint(1) | 否 | 0 | 是否包邮：1=是，0=跟随系统 |
| `users_price` | decimal(20,2) | 否 | 0.00 | 会员价 |
| `crossed_price` | decimal(10,2) | 否 | 0.00 | 商品划线价（原价） |
| `users_discount_type` | tinyint(1) | 否 | 0 | 会员折扣类型：0=系统默认，1=指定级别，2=自定义 |
| `users_free` | tinyint(1) | 否 | 0 | 会员免费：0=否，1=是 |
| `old_price` | decimal(20,2) | 否 | 0.00 | 商品旧价 |
| `sales_num` | int(10) | 否 | 0 | 实际总销量 |
| `virtual_sales` | int(10) | 是 | 0 | 虚拟销量（虚假显示用） |
| `sales_all` | int(10) | 是 | 0 | 实际+虚拟总销量 |
| `stock_count` | int(10) | 否 | 0 | 库存量 |
| `stock_show` | tinyint(1) | 否 | 1 | 库存是否在详情页显示：1=是，0=否 |
| `prom_type` | tinyint(1) | 是 | 0 | 产品类型：0=普通，1=虚拟手动发货，2=虚拟自动发货 |
| `logistics_type` | varchar(100) | 是 | 1 | 物流支持：1=物流配送，2=到店核销 |
| `tempview` | varchar(200) | 是 | — | 文档自定义模板文件名 |
| `status` | tinyint(1) | 是 | 1 | 状态：0=屏蔽，1=正常 |
| `sort_order` | int(10) | 是 | 0 | 排序号 |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `admin_id` | int(10) | 是 | 0 | 发布管理员ID |
| `users_id` | int(10) | 是 | 0 | 发布会员ID |
| `arc_level_id` | int(10) | 是 | 0 | 文档会员权限ID |
| `restric_type` | tinyint(1) | 是 | 0 | 访问限制：0=免费，1=付费，2=会员专享，3=会员付费，4=积分 |
| `users_score` | varchar(20) | 是 | — | 积分访问时所需积分数（restric_type=4时有效） |
| `is_del` | tinyint(1) | 是 | 0 | 伪删除：0=否，1=是 |
| `del_method` | tinyint(1) | 是 | 0 | 删除方式：1=主动删除，2=跟随栏目删除 |
| `joinaid` | int(10) | 是 | 0 | 关联文档ID |
| `downcount` | int(10) | 是 | 0 | 下载次数 |
| `appraise` | int(10) | 是 | 0 | 评价数 |
| `collection` | int(10) | 是 | 0 | 收藏数 |
| `htmlfilename` | varchar(500) | 是 | — | 自定义静态文件名 |
| `province_id` | int(10) | 是 | 0 | 所在省份ID |
| `city_id` | int(10) | 是 | 0 | 所在城市ID |
| `area_id` | int(10) | 是 | 0 | 所在区县ID |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |
| `removal_time` | int(11) | 是 | 0 | 下架时间（自动下架用） |
| `no_vip_pay` | tinyint(3) | 是 | 0 | restric_type=2时，非会员可付费访问 |
| `editor_remote_img_local` | tinyint(1) | 是 | 1 | 远程图片本地化：1=开启 |
| `editor_img_clear_link` | tinyint(1) | 是 | 1 | 清除非本站链接：1=开启 |
| `reason` | text | 是 | NULL | 审核退回原因 |
| `stock_code` | varchar(100) | 是 | NULL | 商品编码（SKU） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | aid |
| add_time | BTREE | 否 | add_time |
