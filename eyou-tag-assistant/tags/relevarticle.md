# `{eyou:relevarticle}` — 相关文档

> **用途**：通过TAG或关键词检索相关文档，用于内容页。需安装相关文档标签插件。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/8785.html
> **关联表**：[`ey_archives`](../dict/ey_archives.md)

---

## 语法

```html
{eyou:relevarticle limit='0,5' titlelen='30' id='field'}
  <li><a href="{$field.arcurl}">{$field.title}</a></li>
{/eyou:relevarticle}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `modelid` | string | 指定模型ID，逗号分隔多个 |
| `typeid` | string | 指定栏目ID |
| `limit` | string | 范围，如 `'0,12'` |
| `titlelen` | int | 标题截取字数 |
| `infolen` | int | 简介截取字数 |
| `thumb` | string | 缩略图：`on`/`off` |
| `empty` | string | 无数据文案 |
| `id` | string | 自定义变量名，默认 `field` |
