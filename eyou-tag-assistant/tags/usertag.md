# `{eyou:user}` — 会员入口标签

> **用途**：动态显示登录、注册、退出、购物车、会员中心入口，登录状态自动切换显示内容。
> **官方文档**：https://www.eyoucms.com/doc/label/all/7171.html
> **关联表**：[`ey_users`](../dict/ey_users.md) · [`ey_users_level`](../dict/ey_users_level.md)

---

## type 类型速查

| type 值 | 说明 |
|---------|------|
| `userinfo` | 【推荐】登录前后状态切换，需配置 `system/users_info.htm` |
| `open` | 会员中心开启/关闭判断包裹标签 |
| `login` | 登录入口，已登录显示会员名 |
| `reg` | 注册入口 |
| `logout` | 退出入口 |
| `cart` | 购物车数量与入口 |
| `info` | 登录后显示用户信息（未登录自动隐藏） |

## 语法（推荐用法 userinfo）

```html
{eyou:user type='userinfo' id='field'}
  <!-- 登录前显示（HTML写在标签内） -->
  <div id="{$field.htmlid}">
    <a href="{eyou:diyurl type='login' /}">登录</a>
    <a href="{eyou:diyurl type='reg' /}">注册</a>
  </div>
  {$field.hidden}
{/eyou:user}
```

> 登录后的显示效果由模板文件 `pc/system/users_info.htm`（或 `mobile/system/users_info.htm`）控制。

## users_info.htm 可用变量

| 变量 | 说明 |
|------|------|
| `{$users.username}` | 会员用户名 |
| `{$users.nickname}` | 会员昵称 |
| `{$users.head_pic}` | 会员头像 |
| `{$users.mobile}` | 手机号 |
| `{$users.email}` | 邮箱 |
| `{$users.users_money}` | 账户余额 |
| `{$users.scores}` | 积分 |
| `{$users.level_name}` | 会员等级名称 |
| `{$users.level_value}` | 会员等级值 |
| `{$users.cart_num}` | 购物车数量 |

## 参数

| 参数 | 说明 |
|------|------|
| `type` | 标签类型，见上方速查表 |
| `id` | 自定义变量名，默认 `field` |

## 完整示例

```html
<!-- 推荐写法：登录前后状态切换 -->
{eyou:user type='open'}
  {eyou:user type='userinfo' id='field'}
    <li id="{$field.htmlid}">
      <a href="{eyou:diyurl type='login' /}">登录</a>
      <a href="{eyou:diyurl type='reg' /}">注册</a>
    </li>
    {$field.hidden}
  {/eyou:user}
{/eyou:user}
```
