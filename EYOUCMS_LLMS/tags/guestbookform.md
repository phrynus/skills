# `{eyou:guestbookform}` — 栏目留言表单

> **用途**：调用留言模型栏目的留言表单，通过后台留言模型建立栏目并配置字段。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/502.html
> **关联表**：[`ey_guestbook`](../dict/ey_guestbook.md) · [`ey_guestbook_attribute`](../dict/ey_guestbook_attribute.md) · [`ey_guestbook_attr`](../dict/ey_guestbook_attr.md)

---

## 语法

```html
{eyou:guestbookform type='default' id='field'}
  <form method="POST" action="{$field.action}" {$field.formhidden} onsubmit="{$field.submit}">
    <input id="attr_1" type="text" name="{$field.attr_1}" placeholder="{$field.itemname_1}">
    <input id="attr_2" type="text" name="{$field.attr_2}" placeholder="{$field.itemname_2}">
    <textarea id="attr_3" name="{$field.attr_3}" placeholder="{$field.itemname_3}"></textarea>
    <input type="submit" value="提交">
    {$field.hidden}
  </form>
{/eyou:guestbookform}
```

## 参数

| 参数 | 说明 |
|------|------|
| `typeid` | 留言栏目ID，省略则取当前留言栏目（在非留言栏目页需指定） |
| `type` | 固定填 `default`，不可省略 |
| `empty` | 表单字段被删完时显示的文案 |
| `id` | 自定义变量名，默认 `field` |

## 关键变量说明

| 变量 | 说明 |
|------|------|
| `{$field.action}` | 表单提交URL |
| `{$field.formhidden}` | 支持图片上传的 enctype 属性，放入 `<form>` 标签 |
| `{$field.submit}` | 内置JS验证，放入 `onsubmit` 属性 |
| `{$field.attr_N}` | 第N个字段的 name 属性值（N从后台字段ID获取） |
| `{$field.itemname_N}` | 第N个字段的提示文字 |
| `{$field.options}` | 下拉/多选字段的选项数组，配合 volist 循环 |
| `{$field.hidden}` | 必须输出的令牌验证隐藏域 |

## 含下拉框的完整示例

```html
{eyou:guestbookform typeid='6' type='default' id='field'}
  <form method="POST" enctype="multipart/form-data" action="{$field.action}" onsubmit="{$field.submit}">
    <input id="attr_5" type="text" name="{$field.attr_5}" placeholder="{$field.itemname_5}">
    <textarea id="attr_6" name="{$field.attr_6}" placeholder="{$field.itemname_6}"></textarea>
    <select name="{$field.attr_7}" id="attr_7">
      <option value="无">无</option>
      {eyou:volist name='$field.options' id='vo'}
        <option value="{$vo.value}">{$vo.value}</option>
      {/eyou:volist}
    </select>
    <input type="submit" value="提交">
    {$field.hidden}
  </form>
{/eyou:guestbookform}
```
