# `{eyou:hotkeywords}` — 热门搜索词

> **用途**：获取网站的热门搜索关键字列表。
> **官方文档**：https://www.eyoucms.com/doc/label/all/10195.html
> **关联表**：[`ey_search_word`](../dict/ey_search_word.md)

---

## 语法

```html
{eyou:hotkeywords num='6' subday='365' maxlength='20' orderby='hot' id='field'}
  <a href='{$field.url}' target="_blank">{$field.word}</a>
{/eyou:hotkeywords}
```

## 参数

| 参数 | 说明 |
|------|------|
| `num` | 关键词数量 |
| `subday` | 显示N天内的关键词 |
| `maxlength` | 关键词最大字符长度 |
| `orderby` | 排序：`hot`最热 / `new`最新 / `sort_order`排序号 / `rand`随机 |
| `screen` | 筛选：`is_hot` 只显示后台设为热搜的关键词（v1.6.6+） |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.word}` | 搜索词文本 |
| `{$field.url}` | 该词的搜索结果页URL |
