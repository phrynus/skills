# `{eyou:artpagelist}` — 瀑布流分页

> **用途**：实现无刷新 Ajax 瀑布流加载，配合 `artlist` 标签使用。
> **官方文档**：https://www.eyoucms.com/doc/label/list/6279.html

---

## 前置条件

在模板目录 `pc/system/` 中创建瀑布流加载模板文件，命名格式：`arclist_{tagid}.htm`，内容为 `artlist` 标签包裹的 HTML 片段（不含标签本身）。

## 语法

```html
<!-- 步骤1：artlist 指定 tagid -->
<div id='tagid名称'>
  {eyou:artlist typeid='栏目ID' loop='10' tagid='唯一标识' id='field'}
    <a href='{$field.arcurl}'>{$field.title}</a>
  {/eyou:artlist}
</div>

<!-- 步骤2：紧跟 artpagelist -->
{eyou:artpagelist tagid='唯一标识' pagesize='10' tips='没有更多了' id='field'}
  <a href="javascript:void(0);" {$field.onclick}>加载更多</a>
{/eyou:artpagelist}

<!-- 步骤3：创建 pc/system/arclist_唯一标识.htm，内容为：-->
<!-- <a href='{$field.arcurl}'>{$field.title}</a> -->
```

## 参数

| 参数 | 说明 |
|------|------|
| `tagid` | 与对应 artlist 的 tagid 一致 |
| `pagesize` | 每次加载条数 |
| `tips` | 加载完毕后显示的文案 |
| `loading` | 加载中的提示文案（默认转圈图片） |
| `id` | 自定义变量名，默认 `field` |
