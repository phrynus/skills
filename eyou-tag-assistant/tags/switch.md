# `{eyou:switch}` — 简单条件判断

> **用途**：简单的值匹配判断，适合固定值枚举。
> **官方文档**：https://www.eyoucms.com/doc/label/all/509.html

---

## 语法

```html
{eyou:switch name='$eyou.field.has_children'}
  {eyou:case value='1'}有1个子栏目{/eyou:case}
  {eyou:case value='2|3'}有2或3个子栏目{/eyou:case}
  {eyou:default /}其他情况
{/eyou:switch}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 要匹配的变量 |
| `value`（case） | 匹配值，多值用 `\|` 分隔 |
