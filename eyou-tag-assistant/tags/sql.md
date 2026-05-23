# `{eyou:sql}` — 自定义数据查询

> **用途**：直接执行 SQL 语句获取数据，数据表前缀用 `__PREFIX__` 替代。
> **官方文档**：https://www.eyoucms.com/doc/label/all/579.html

---

## 语法

```html
{eyou:sql sql='SELECT id,typename FROM __PREFIX__arctype WHERE id=2' cachetime='3600' id='field'}
  {$field.typename}
{/eyou:sql}
```

## 参数

| 参数 | 默认 | 说明 |
|------|------|------|
| `sql` | — | SQL查询语句，表前缀用 `__PREFIX__` |
| `cachetime` | `86400` | 缓存秒数，`-1` 表示不缓存 |
| `empty` | — | 无数据文案 |
| `mod` | — | 每隔N条触发 |
| `id` | `field` | 自定义循环变量名 |
