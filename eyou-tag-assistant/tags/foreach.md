# `{eyou:foreach}` — 循环输出

> **用途**：简单数组循环，常用于子栏目或表单选项遍历。
> **官方文档**：https://www.eyoucms.com/doc/label/all/506.html

---

## 语法

```html
{eyou:foreach name='$field.children' item='field1'}
  <a href='{$field1.typeurl}'>{$field1.typename}</a>
{/eyou:foreach}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 数组变量名 |
| `item` | 循环变量名 |
