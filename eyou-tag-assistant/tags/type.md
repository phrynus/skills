# `{eyou:type}` — 指定栏目信息

> **用途**：获取指定栏目信息（名称、URL、自定义字段等）。
> **官方文档**：https://www.eyoucms.com/doc/label/all/494.html
> **关联表**：[`ey_arctype`](../dict/ey_arctype.md)

---

## 语法

```html
{eyou:type typeid='栏目ID' id='field'}
  <a href="{$field.typeurl}">{$field.typename}</a>
{/eyou:type}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `typeid` | int | 指定栏目ID，省略则取当前列表页栏目 |
| `type` | string | `self`当前栏目 / `top`最顶级栏目 |
| `addfields` | string | 附加自定义字段，如 `'content'` |
| `empty` | string | 无数据时显示文案 |
| `id` | string | 自定义变量名，默认 `field` |

## 示例

```html
<!-- 输出单页模型栏目内容（截取250字） -->
{eyou:type typeid='10' type='self' addfields='content'}
  <a href="{$field.typeurl}">{$field.typename}</a>
  <span>{$field.content|html_msubstr=###,0,250}...</span>
{/eyou:type}
```
