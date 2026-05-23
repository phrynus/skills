# `{eyou:beafter}` — 上一篇/下一篇

> **用途**：获取当前文档的上一篇或下一篇，用于内容页。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/518.html
> **关联表**：[`ey_archives`](../dict/ey_archives.md)

---

## 语法

```html
{eyou:beafter get='pre' id='field'}
  <a href="{$field.arcurl}">上一篇：{$field.title}</a>
  {eyou:else /}上一篇：暂无
{/eyou:beafter}

{eyou:beafter get='next' id='field'}
  <a href="{$field.arcurl}">下一篇：{$field.title}</a>
  {eyou:else /}下一篇：暂无
{/eyou:beafter}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `get` | string | `pre`上一篇 / `next`下一篇 |
| `titlelen` | int | 标题截取字数，默认100 |
| `id` | string | 自定义变量名，默认 `field` |
