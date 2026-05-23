# `{eyou:attribute}` — 栏目属性 / 商品参数

> **用途**：获取栏目自定义属性列表，或新版商城商品参数（`type='newattr'`）。
> **官方文档（栏目属性）**：https://www.eyoucms.com/doc/label/all/6394.html
> **官方文档（商品参数）**：https://www.eyoucms.com/doc/label/arc/10108.html

---

## 语法

```html
<!-- 栏目自定义属性：自动循环所有属性 -->
{eyou:attribute type='auto' id='attr'}
  {$attr.name}：{$attr.value}
{/eyou:attribute}

<!-- 商城商品参数（详情页） -->
{eyou:attribute type='newattr' attrid='$eyou.field.attrlist_id' id='attr'}
  {$attr.name}：{$attr.value}
{/eyou:attribute}

<!-- 商城商品参数（列表页，嵌套在 artlist/list 内） -->
{eyou:artlist typeid='产品栏目ID' loop='10' id='field'}
  {eyou:attribute type='newattr' attrid='$field.attrlist_id' id='attr'}
    {$attr.name}：{$attr.value}
  {/eyou:attribute}
{/eyou:artlist}
```

## 参数

| 参数 | 说明 |
|------|------|
| `aid` | 文档ID，列表/内容页可省略 |
| `type` | `default`手动 / `auto`自动循环（栏目属性） / `newattr`新版商品参数 |
| `attrid` | 参数列表ID（newattr时）：详情页用 `$eyou.field.attrlist_id`，列表页用 `$field.attrlist_id` |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `attr` |
