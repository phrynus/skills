# `{eyou:arcview}` — 单条文档

> **用途**：获取单条文档的详细数据，适用于内容页或在列表中嵌套获取指定文档。
> **官方文档**：https://www.eyoucms.com/doc/label/all/498.html
> **关联表**：[`ey_archives`](../dict/ey_archives.md)

---

## 语法

```html
{eyou:arcview aid='文档ID' id='field'}
  <a href="{$field.arcurl}">{$field.title}</a>
{/eyou:arcview}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `aid` | int/var | 文档ID，省略则取当前内容页文档ID |
| `addfields` | string | 附加自定义字段，逗号分隔 |
| `joinaid` | int | 关联文档ID |
| `id` | string | 自定义变量名，默认 `field` |

## 示例

```html
<!-- 内容页调用自定义字段 -->
{eyou:arcview aid='$eyou.field.aid' addfields='test1,test2' id='view'}
  {$view.test1} - {$view.test2}
{/eyou:arcview}

<!-- 在 artlist 中嵌套调用自定义字段 -->
{eyou:artlist typeid='2' loop='5' id='field'}
  {eyou:arcview aid='$field.aid' addfields='price,spec' id='view'}
    {$view.price}
  {/eyou:arcview}
{/eyou:artlist}
```
