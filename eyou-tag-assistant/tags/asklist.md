# `{eyou:asklist}` — 问答列表

> **用途**：调用内置问答模型的提问列表，可用于首页、列表页、内容页。
> **官方文档**：https://www.eyoucms.com/doc/label/all/11336.html

---

## 语法

```html
{eyou:asklist id='field' loop='20' orderby='add_time'}
  <li>
    <a href="{$field.ask_url}">{$field.ask_title|html_msubstr=###,0,30,true}</a>
    <span>回复：{$field.replies} | 查看：{$field.click}</span>
    <span>{$field.add_time|MyDate='Y-m-d',###}</span>
    <span><a href="{$field.type_url}">{$field.type_name}</a></span>
  </li>
{/eyou:asklist}
```

## 参数

| 参数 | 说明 |
|------|------|
| `loop` | 返回总数 |
| `limit` | 范围，如 `'0,20'` |
| `titlelen` | 标题截取字数 |
| `orderby` | 排序：`ask_id`/`click`/`add_time`/`sort_order`/`recom`/`replies`/`solve_time`/`money`/自定义多字段 |
| `ordermode` | `desc`/`asc` |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.ask_title}` | 提问标题 |
| `{$field.ask_url}` | 提问页面URL |
| `{$field.content}` | 提问内容 |
| `{$field.money}` | 悬赏金额 |
| `{$field.click}` | 查看人数 |
| `{$field.replies}` | 回复人数 |
| `{$field.add_time}` | 提问时间（时间戳） |
| `{$field.type_name}` | 所属分类名 |
| `{$field.type_url}` | 所属分类URL |
| `{$field.users.username}` | 提问者用户名 |
| `{$field.users.nickname}` | 提问者昵称 |
| `{$field.users.head_pic}` | 提问者头像 |
| `{$field.is_recom}` | 是否推荐（1=是） |
