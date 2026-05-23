# `{eyou:empty}` — 为空判断

> **用途**：判断变量为空时输出内容，可嵌套在任何标签内。
> **官方文档**：https://www.eyoucms.com/doc/label/all/504.html

---

## 语法

```html
{eyou:empty name='$eyou.field.seo_title'}
  {$eyou.field.title}        <!-- 为空时显示普通标题 -->
  {eyou:else /}
  {$eyou.field.seo_title}    <!-- 不为空时显示SEO标题 -->
{/eyou:empty}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 要判断的变量名（含 `$` 前缀） |
