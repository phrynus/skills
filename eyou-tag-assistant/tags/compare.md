# `{eyou:eq}` / `{eyou:neq}` / `{eyou:gt}` 等 — 变量比较

> **用途**：一组比较标签，用于简单的变量比对输出（eq/neq/gt/egt/lt/elt/heq/nheq）。
> **官方文档**：https://www.eyoucms.com/doc/label/all/510.html

---

## 标签对照表

| 标签 | 含义 |
|------|------|
| `{eyou:eq}` / `{eyou:equal}` | 等于 |
| `{eyou:neq}` / `{eyou:notequal}` | 不等于 |
| `{eyou:gt}` | 大于 |
| `{eyou:egt}` | 大于等于 |
| `{eyou:lt}` | 小于 |
| `{eyou:elt}` | 小于等于 |
| `{eyou:heq}` | 恒等于（`===`） |
| `{eyou:nheq}` | 不恒等于（`!==`） |

## 语法

```html
{eyou:eq name='$eyou.field.typeid' value='3'}
  当前栏目ID等于3
{/eyou:eq}

<!-- 配合 else -->
{eyou:eq name='$i' value='1'}
  第一条
  {eyou:else /}
  其他条
{/eyou:eq}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 变量名 |
| `value` | 比较值 |
