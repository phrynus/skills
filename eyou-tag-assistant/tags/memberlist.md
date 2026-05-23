# `{eyou:memberlist}` — 会员列表

> **用途**：获取网站会员信息列表，展示会员资料。
> **官方文档**：https://www.eyoucms.com/doc/label/all/29780.html
> **关联表**：[`ey_users`](../dict/ey_users.md)

---

## 语法

```html
{eyou:memberlist row='10' orderby='logintime' id='field'}
  <div id="{$field.txtid}">
    <img src="{$field.head_pic}" />
    <span>{$field.nickname}</span>
    <span>{$field.username}</span>
    {$field.hidden}
  </div>
{/eyou:memberlist}
```

> **注意**：`{$field.hidden}` 和包含 `id="{$field.txtid}"` 的容器不可缺少。

## 参数

| 参数 | 说明 |
|------|------|
| `row` | 返回会员总数 |
| `orderby` | 排序：`logintime`登录时间 / `reg_time`注册时间 / `update_time`更新时间 / `users_id`ID / `sort_order`排序号 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.users_id}` | 会员ID |
| `{$field.head_pic}` | 头像 |
| `{$field.nickname}` | 昵称 |
| `{$field.username}` | 用户名 |
| `{$field.mobile}` | 手机号 |
| `{$field.email}` | 邮箱 |
| `{$field.level}` | 会员级别 |
| `{$field.scores}` | 积分 |
| `{$field.para_N}` | 自定义字段（N为后台字段ID） |
