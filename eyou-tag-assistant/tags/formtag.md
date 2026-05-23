# `{eyou:form}` — 自由表单

> **用途**：不依赖栏目的独立表单，在后台「功能地图→留言管理→表单管理」中创建。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/29138.html
> **关联表**：[`ey_form`](../dict/ey_form.md) · [`ey_guestbook`](../dict/ey_guestbook.md) · [`ey_guestbook_attribute`](../dict/ey_guestbook_attribute.md) · [`ey_guestbook_attr`](../dict/ey_guestbook_attr.md)

---

## 语法

```html
{eyou:form type='default' formid='表单ID' id='field'}
  <form method="POST" action="{$field.action}" {$field.formhidden} onsubmit="{$field.submit}">
    <input id="attr_1" type="text" name="{$field.attr_1}" placeholder="{$field.itemname_1}">
    <textarea id="attr_2" name="{$field.attr_2}" placeholder="{$field.itemname_2}"></textarea>
    <input type="submit" value="提交">
    {$field.hidden}
  </form>
{/eyou:form}
```

## 参数

| 参数 | 说明 |
|------|------|
| `formid` | 后台表单管理中的表单ID，必填 |
| `type` | `default`手动添加字段标签 / `auto`自动循环显示所有字段 |
| `empty` | 表单字段被删完时显示的文案 |
| `id` | 自定义变量名，默认 `field` |

## 自动循环字段（type='auto'）

```html
{eyou:form type='auto' formid='表单ID' id='field'}
  <form method="POST" {$field.formhidden} action="{$field.action}" onsubmit="{$field.submit}">
    {eyou:volist name="$field.attrlist" id="attr"}
      {$attr.attr_name}：{$attr.attr_html}
    {/eyou:volist}
    <input type="submit" value="提交">
    {$field.hidden}
  </form>
{/eyou:form}
```

> **变量说明**同 `guestbookform`，`{$field.hidden}` 不可缺少。
