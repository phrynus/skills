# `{eyou:field}` — 字段值（channelartlist 专用）

> **用途**：在 `channelartlist`/`modelsartlist` 标签内获取当前循环栏目的字段值。
> **官方文档**：https://www.eyoucms.com/doc/label/all/519.html
> **关联表**：[`ey_arctype`](../dict/ey_arctype.md)

---

## 语法

```html
{eyou:channelartlist typeid='栏目ID' type='son' row='20'}
  <a href='{eyou:field name='typeurl' /}'>{eyou:field name='typename' /}</a>
  <!-- 截取栏目描述 -->
  {eyou:field name='seo_description|html_msubstr=###,0,100' /}
{/eyou:channelartlist}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 字段名，支持函数管道，如 `'seo_description\|html_msubstr=###,0,100'` |
