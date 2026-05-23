# `{eyou:notempty}` — 不为空判断

> **用途**：判断变量不为空时输出内容，与 empty 相反。
> **官方文档**：https://www.eyoucms.com/doc/label/all/505.html

---

## 语法

```html
{eyou:notempty name='$eyou.field.seo_title'}
  {$eyou.field.seo_title}
  {eyou:else /}
  {$eyou.field.title}
{/eyou:notempty}

<!-- 判断是否有子栏目 -->
{eyou:notempty name='$field1.children'}
  <ul>...</ul>
{/eyou:notempty}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 要判断的变量名 |
