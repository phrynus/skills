# `{eyou:memberinfos}` — 文档关联的会员信息

> **用途**：显示文档关联的会员信息（投稿者），与当前登录会员无关。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/10050.html
> **关联表**：[`ey_users`](../dict/ey_users.md)

---

## 语法

```html
<!-- 内容页：显示投稿会员信息 -->
{eyou:memberinfos mid='$eyou.field.users_id' id='users'}
  昵称：{$users.nickname}
  <img src="{$users.head_pic}" width='50' height='50' />
  {$users.hidden}
{/eyou:memberinfos}

<!-- 列表页（artlist/list 内嵌套） -->
{eyou:memberinfos mid='$field.users_id' id='users'}
  昵称：{$users.nickname}
  {$users.hidden}
{/eyou:memberinfos}
```

## 参数

| 参数 | 说明 |
|------|------|
| `mid` | 会员ID，默认取当前文档的 users_id |
| `addfields` | 附加字段：`level_name`等级名 / `para_*`自定义属性 |
| `empty` | 无数据文案 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$users.nickname}` | 昵称 |
| `{$users.head_pic}` | 头像 |
| `{$users.level_name}` | 等级名（需 addfields='level_name'） |
| `{$users.para_N}` | 自定义属性（需 addfields='para_*'） |
| `{$users.hidden}` | 必须输出的隐藏域 |
