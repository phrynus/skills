# `{eyou:formreply}` — 自由表单回复列表

> **用途**：展示自由表单的用户提交记录列表，支持分页加载。
> **官方文档**：https://www.eyoucms.com/doc/label/list/31220.html
> **关联表**：[`ey_form`](../dict/ey_form.md)

---

## 前置条件

在模板目录 `pc/system/`（或 `mobile/system/`）创建分页加载文件 `formreply_block001.htm`，内容为标签体 HTML（不含 `{notempty name='$field.last_one'}` 包裹部分）。

## 语法

```html
{eyou:formreply typeid='表单ID' id='field' pagesize='5'}
  用户头像：<img src="{$field.head_pic}" />
  用户昵称：{$field.nickname}
  提交时间：{$field.add_time|MyDate='Y-m-d H:i:s',###}
  字段值：{$field.attr.字段ID.attr_value}
  字段名：{$field.attr.字段ID.attr_name}

  {eyou:notempty name='$field.last_one'}
    {$field.hidden}
    <a href="javascript:void(0);" {$field.onclick}>查看更多</a>
  {/eyou:notempty}
{/eyou:formreply}
```

## 参数

| 参数 | 说明 |
|------|------|
| `typeid` | 自由表单ID |
| `pagesize` | 每页显示条数，默认10 |
| `page` | 当前页码，默认1 |
| `ordermode` | 排序方向：`desc`/`asc` |
| `empty` | 无数据文案 |
| `id` | 自定义变量名，默认 `field` |

> `{$field.onclick}` 和 `{$field.hidden}` 在分页时不可缺少。
