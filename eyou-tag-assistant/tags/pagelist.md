# `{eyou:pagelist}` — 列表分页

> **用途**：在列表页输出分页页码，必须配合 `list` 标签使用。
> **官方文档**：https://www.eyoucms.com/doc/label/list/497.html

---

## 语法

```html
{eyou:list loop='10' titlelen='30' id='field'}
  <a href='{$field.arcurl}'>{$field.title}</a>
{/eyou:list}
{eyou:pagelist listitem='index,pre,pageno,next,end,info' listsize='2' /}
```

## 参数

| 参数 | 默认 | 说明 |
|------|------|------|
| `listitem` | — | 页码组件，逗号组合：`index`首页 / `pre`上一页 / `pageno`数字页码 / `next`下一页 / `end`末页 / `info`共N页N条 / `dots`省略号 |
| `listsize` | `2` | 数字页码显示数量，公式：`listsize * 2 + 1` 个页码 |

## 示例

```html
<!-- 完整分页 -->
<div class="pglist">
  {eyou:pagelist listitem='index,pre,pageno,next,end,info' listsize='3' /}
</div>

<!-- 仅上下页 -->
{eyou:pagelist listitem='index,pre,next,end' listsize='2' /}

<!-- 通常使用 -->
{eyou:pagelist listitem="pre,next,pageno"  listsize="2" /}
```
