# `{eyou:if}` — 条件判断

> **用途**：基于原生 PHP 语法的条件判断，比 switch 更灵活。
> **官方文档**：https://www.eyoucms.com/doc/label/all/508.html

---

## 语法

```html
{eyou:if condition='($eyou.field.has_children > 0)'}
  有下级栏目
  {eyou:elseif condition='($eyou.field.has_children == 0)' /}
  没有下级栏目
  {eyou:else /}
  其他情况
{/eyou:if}
```

## 参数

| 参数 | 说明 |
|------|------|
| `condition` | 原生 PHP 条件表达式 |
