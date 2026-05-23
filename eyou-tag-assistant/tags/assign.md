# `{eyou:assign}` — 定义变量

> **用途**：在模板中定义变量，供后续标签引用。
> **官方文档**：https://www.eyoucms.com/doc/label/all/503.html

---

## 语法

```html
{eyou:assign name='typeid' value='5' /}

<!-- 后续标签中引用 -->
{eyou:type typeid='$typeid'}
  <a href="{$field.typeurl}">{$field.typename}</a>
{/eyou:type}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 变量名 |
| `value` | 变量值 |
