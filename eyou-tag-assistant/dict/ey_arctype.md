# 数据字典：ey_arctype

> **表说明**：文档栏目表，存储所有栏目/分类的配置信息
> **字段数量**：42
> **引用此表的标签**：[models](../tags/models.md) · [type](../tags/type.md) · [list](../tags/list.md) · [field](../tags/field.md) · [navigation](../tags/navigation.md) · [position](../tags/position.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(10) | 否 | — | 主键，栏目ID |
| `channeltype` | int(10) | 是 | 0 | 栏目顶级模型ID |
| `current_channel` | int(10) | 是 | 0 | 栏目当前模型ID |
| `parent_id` | int(10) | 是 | 0 | 上级栏目ID（0=顶级） |
| `topid` | int(10) | 是 | 0 | 顶级栏目ID |
| `typename` | varchar(200) | 是 | — | 栏目名称 |
| `dirname` | varchar(200) | 是 | — | 目录英文名（URL路径） |
| `dirpath` | varchar(200) | 是 | — | 目录存放HTML路径 |
| `diy_dirpath` | varchar(200) | 是 | — | 自定义目录路径 |
| `rulelist` | varchar(200) | 是 | — | 列表静态文件存放规则 |
| `ruleview` | varchar(200) | 是 | — | 文档静态文件存放规则 |
| `englist_name` | varchar(200) | 是 | — | 栏目英文名 |
| `grade` | tinyint(1) | 是 | 0 | 栏目等级（1=一级，2=二级…） |
| `typelink` | varchar(200) | 是 | — | 栏目链接（外部链接时使用） |
| `litpic` | varchar(250) | 是 | — | 栏目封面图片 |
| `templist` | varchar(200) | 是 | — | 列表页模板文件名 |
| `tempview` | varchar(200) | 是 | — | 文档页模板文件名 |
| `seo_title` | varchar(200) | 是 | — | SEO标题 |
| `seo_keywords` | varchar(200) | 是 | — | SEO关键词 |
| `seo_description` | text | 是 | NULL | SEO描述 |
| `sort_order` | int(10) | 是 | 0 | 排序号 |
| `is_hidden` | tinyint(1) | 是 | 0 | 是否隐藏：0=显示，1=隐藏 |
| `is_part` | tinyint(1) | 是 | 0 | 栏目属性：0=内容栏目，1=外部链接 |
| `admin_id` | int(10) | 是 | 0 | 管理员ID |
| `is_del` | tinyint(1) | 是 | 0 | 伪删除：0=否，1=是 |
| `del_method` | tinyint(1) | 是 | 0 | 删除方式：1=主动，2=跟随上级 |
| `status` | tinyint(1) | 是 | 1 | 状态：0=屏蔽，1=正常 |
| `is_release` | tinyint(1) | 是 | 0 | 是否允许会员投稿：0=否，1=是 |
| `weapp_code` | varchar(50) | 是 | — | 插件栏目唯一标识 |
| `lang` | varchar(50) | 是 | cn | 语言标识 |
| `add_time` | int(11) | 是 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 是 | 0 | 更新时间（Unix时间戳） |
| `target` | tinyint(1) | 是 | 0 | 新窗口打开：0=否，1=是 |
| `nofollow` | tinyint(1) | 是 | 0 | 防抓取nofollow：0=否，1=是 |
| `typearcrank` | int(10) | 是 | 0 | 栏目默认阅读权限：0=开放，-1=待审核 |
| `empty_logic` | tinyint(1) | 是 | 0 | 空内容逻辑处理 |
| `page_limit` | varchar(10) | 是 | 0 | 限制页面：0=文档页，1=栏目页 |
| `total_arc` | int(10) | 是 | 0 | 栏目下文档总数量 |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
| dirname | BTREE | 是 | dirname |
| parent_id | BTREE | 否 | channeltype |
