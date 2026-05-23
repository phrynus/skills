# `{eyou:volist}` — 数据循环

> **用途**：数组循环输出，比 foreach 多支持 `id`/`offset`/`mod` 等参数。
> **官方文档**：https://www.eyoucms.com/doc/label/all/507.html

---

## 语法

```html
{eyou:volist name='$field.children' id='field1'}
  <a href='{$field1.typeurl}'>{$field1.typename}</a>
{/eyou:volist}

<!-- 遍历下拉选项 -->
{eyou:volist name='$field.options' id='vo'}
  <option value="{$vo.value}">{$vo.value}</option>
{/eyou:volist}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 数组变量名 |
| `id` | 循环变量名 |
