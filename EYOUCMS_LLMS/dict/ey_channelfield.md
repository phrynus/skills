# 数据字典：ey_channelfield

> **表说明**：自定义字段表，存储各模型的自定义字段定义
> **字段数量**：24
> **引用此表的标签**：[artlist](../tags/artlist.md) · [arcview](../tags/arcview.md) · [screening](../tags/screening.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `id` 🔑 | int(10) | 否 | — | 主键，自增ID |
| `name` | varchar(32) | 否 | — | 字段名称（英文，用于模板调用） |
| `channel_id` | int(10) | 否 | 0 | 所属文档模型ID |
| `title` | varchar(250) | 否 | — | 字段标题（后台显示名称） |
| `dtype` | varchar(32) | 否 | — | 字段类型（text/textarea/select/radio/checkbox/img/imgs/file/date/number/editor等） |
| `define` | text | 否 | — | 字段定义（下拉/单选/多选时存储选项） |
| `maxlength` | int(10) | 否 | 0 | 最大长度（>255时为text类型） |
| `dfvalue` | text | 否 | — | 默认值 |
| `dfvalue_unit` | varchar(50) | 否 | — | 数值单位 |
| `remark` | varchar(256) | 否 | — | 后台提示说明 |
| `is_screening` | tinyint(1) | 否 | 0 | 是否用于条件筛选：0=否，1=是 |
| `is_release` | tinyint(1) | 否 | 0 | 是否用于会员投稿：0=否，1=是 |
| `ifeditable` | tinyint(1) | 否 | 1 | 编辑页是否显示：1=是，0=否 |
| `ifrequire` | tinyint(1) | 否 | 0 | 是否必填：0=否，1=是 |
| `ifsystem` | tinyint(1) | 否 | 0 | 字段分类：0=自定义，1=系统（不可修改） |
| `ifmain` | tinyint(1) | 否 | 0 | 是否为主表字段（存在 ey_archives） |
| `ifcontrol` | tinyint(1) | 否 | 1 | 是否允许被控制：0=允许，1=不允许 |
| `sort_order` | int(5) | 否 | 100 | 排序号 |
| `status` | tinyint(1) | 否 | 1 | 状态：0=禁用，1=启用 |
| `add_time` | int(11) | 否 | 0 | 创建时间（Unix时间戳） |
| `update_time` | int(11) | 否 | 0 | 更新时间（Unix时间戳） |
| `set_type` | tinyint(3) | 是 | 0 | 区域选择联动：0=否，1=三级联动 |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | id |
