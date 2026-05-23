# 数据字典：ey_nav_list

> **表说明**：导航列表，存储后台配置的导航菜单数据
> **字段数量**：22
> **引用此表的标签**：[navigation](../tags/navigation.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `nav_id` 🔑 | int(10) | 否 | — | 主键，导航ID |
| `nav_name` | varchar(200) | 否 | — | 导航名称 |
| `parent_id` | int(10) | 否 | 0 | 上级菜单ID（0=顶级） |
| `topid` | int(10) | 否 | 0 | 顶级菜单ID |
| `en_name` | varchar(200) | 否 | — | 英文名称 |
| `nav_url` | varchar(200) | 否 | — | 导航链接URL |
| `position_id` | int(10) | 否 | 0 | 导航位置ID |
| `arctype_sync` | tinyint(1) | 否 | 0 | 是否与栏目同步：0=否，1=是 |
| `type_id` | int(10) | 否 | 0 | 同步栏目的ID |
| `nav_pic` | varchar(255) | 否 | — | 导航图标/图片 |
| `is_remote` | tinyint(1) | 否 | 0 | 图片是否为远程：0=否，1=是 |
| `target` | tinyint(1) | 否 | 0 | 新窗口打开：0=否，1=是 |
| `nofollow` | tinyint(1) | 否 | 0 | nofollow：0=否，1=是 |
| `status` | tinyint(1) | 否 | 1 | 状态：0=停用，1=正常 |
| `is_del` | tinyint(1) | 否 | 0 | 伪删除：0=否，1=是 |
| `sort_order` | int(10) | 否 | 100 | 排序号 |
| `add_time` | int(11) | 否 | 0 | 新增时间（Unix时间戳） |
| `update_time` | int(11) | 否 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | nav_id |
| position_id | BTREE | 否 | position_id |
| type_id | BTREE | 否 | type_id |
