# `{eyou:searchform}` — 搜索表单

> **用途**：输出文档标题搜索表单，默认搜索整站。
> **官方文档**：https://www.eyoucms.com/doc/label/all/521.html

---

## 语法

```html
{eyou:searchform type='sonself' id='field'}
  <form method="get" action="{$field.action}">
    <input type="text" name="keywords" placeholder="请输入关键词" />
    <input type="submit" value="搜索" />
    {$field.hidden}
  </form>
{/eyou:searchform}
```

## 参数

| 参数 | 说明 |
|------|------|
| `type` | `default`默认 / `sonself`含子分类搜索 |
| `typeid` | 限定搜索栏目ID，如 `typeid='$eyou.field.typeid'` 表示当前栏目 |
| `modelid` | 限定搜索模型ID，如 `modelid='$eyou.field.current_channel'` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.action}` | 表单提交URL |
| `{$field.hidden}` | 必须输出的隐藏域 |

## 搜索结果模板

搜索列表默认模板：`lists_search.htm`。按模型区分模板格式：`lists_search_{模型ID}.htm`

| 模型 | 模板文件名 |
|------|-----------|
| 文章 | `lists_search_1.htm` |
| 产品 | `lists_search_2.htm` |
| 图集 | `lists_search_3.htm` |
| 下载 | `lists_search_4.htm` |
| 视频 | `lists_search_5.htm` |
