# `{eyou:list}` — 列表页文档列表

> **用途**：在列表模板中获取当前栏目的文档列表，**一个列表模板中只能使用一个 list 标签**。
> **官方文档**：https://www.eyoucms.com/doc/label/list/496.html
> **关联表**：[`ey_archives`](../dict/ey_archives.md)
> **配套标签**：[pagelist](pagelist.md)（分页）

---

## 语法

```html
{eyou:list loop='10' titlelen='30' orderby='add_time' id='field'}
  <a href='{$field.arcurl}'>{$field.title}</a>
{/eyou:list}
```

## 参数

> 参数与 [artlist](artlist.md) 基本一致，主要差异：list 用于列表页模板，自动绑定当前栏目，无需指定 typeid。

| 参数 | 类型 | 说明 |
|------|------|------|
| `loop` | int | 分页每页条数 |
| `titlelen` | int | 标题截取字数 |
| `infolen` | int | 简介截取字数 |
| `addfields` | string | 附加自定义字段 |
| `orderby` | string | 排序字段，同 artlist |
| `ordermode` | string | `desc`/`asc` |
| `flag` | string | 属性过滤 |
| `empty` | string | 无数据文案 |
| `mod` | int | 每隔N条触发 |
| `id` | string | 自定义变量名，默认 `field` |
