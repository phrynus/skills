# `{eyou:range}` — 范围判断

> **用途**：判断变量是否在某个范围内（in/notin/between/notbetween）。
> **官方文档**：https://www.eyoucms.com/doc/label/all/581.html

---

## 语法

```html
{eyou:range name='$eyou.field.typeid' value='1,2,3' type='in'}
  栏目ID在1,2,3中
{/eyou:range}

{eyou:range name='$eyou.field.aid' value='1,10' type='between'}
  aid在1~10区间内
  {eyou:else /}
  aid不在1~10区间内
{/eyou:range}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 变量名 |
| `value` | 范围值（in/notin 用逗号分隔多值；between/notbetween 用逗号分隔两个边界） |
| `type` | `in` / `notin` / `between` / `notbetween` |
