# `{eyou:screening}` — 文档筛选

> **用途**：在列表页提供自定义字段的条件筛选 UI，支持文章、产品、视频、图集等模型。
> **官方文档**：https://www.eyoucms.com/doc/label/list/7881.html
> **关联表**：[`ey_channelfield`](../dict/ey_channelfield.md) · [`ey_article_content`](../dict/ey_article_content.md)

---

## 语法

```html
{eyou:screening id='field' currentclass='active' alltxt='全部'}
  <div class="filter-box">
    {eyou:volist name='$field.list' id='vo'}
      <div class="filter-group">
        <span>{$vo.title}：</span>
        {eyou:volist name='$vo.dfvalue' id='val'}
          <a {$val.onClick} class="{$val.currentclass}">{$val.name}</a>
        {/eyou:volist}
      </div>
    {/eyou:volist}
    <a href="{$field.resetUrl}">清除筛选</a>
  </div>
  {$field.hidden}
{/eyou:screening}
```

## 参数

| 参数 | 说明 |
|------|------|
| `id` | 自定义变量名，默认 `field` |
| `typeid` | 首页筛选时必须指定栏目ID |
| `currentclass` | 选中状态的 class 名 |
| `addfields` | 指定自定义字段名，逗号分隔 |
| `alltxt` | "不限"按钮文案；`off` 表示不显示 |
| `empty` | 无数据文案 |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.list}` | 筛选项数组，含 `title`（标题）和 `dfvalue`（可选值列表） |
| `{$val.onClick}` | 点击筛选的 JS 事件属性 |
| `{$val.currentclass}` | 当前选中状态 class |
| `{$val.name}` | 选项显示名称 |
| `{$field.resetUrl}` | 清除所有筛选条件的 URL |
| `{$field.hidden}` | 必须输出的隐藏域 |
