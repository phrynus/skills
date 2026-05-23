# `{eyou:modelsartlist}` — 频道循环

> **用途**：获取当前栏目分类下级栏目的文档列表，常与 artlist 嵌套使用。别名：`channelartlist`。
> **官方文档**：https://www.eyoucms.com/doc/label/all/493.html
> **关联表**：[`ey_arctype`](../dict/ey_arctype.md)

---

## 语法

```html
{eyou:modelsartlist typeid='栏目ID' type='son' loop='20' id='field'}
  <a href='{eyou:field name='typeurl' /}'>{eyou:field name='typename' /}</a>
  {eyou:artlist loop='6' titlelen='30' id='art'}
    <a href='{$art.arcurl}'>{$art.title}</a>
  {/eyou:artlist}
{/eyou:modelsartlist}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `typeid` | string | 栏目ID，多个逗号分隔 |
| `type` | string | 范围：`top`/`son`/`self`/`sonself`，同 models |
| `loop` | int | 调用栏目数 |
| `titlelen` | int | 栏目名截取字数 |
| `empty` | string | 无数据时显示文案 |
| `mod` | int | 每隔N条触发 |

## 说明

> 在 modelsartlist 内部，通过 `{eyou:field name='typeurl' /}` 获取当前循环栏目的字段值（而非 `{$field.xxx}`）。
> 内嵌的 `{eyou:artlist}` 无需指定 typeid，自动绑定当前循环的栏目。
