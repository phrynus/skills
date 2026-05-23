# `{eyou:links}` — 友情链接

> **用途**：获取友情链接列表（文字链接或图片链接）。
> **官方文档**：https://www.eyoucms.com/doc/label/all/578.html
> **关联表**：[`ey_links`](../dict/ey_links.md)

---

## 语法

```html
{eyou:links type='text' loop='30' titlelen='15' id='field'}
  <a href='{$field.url}' {$field.target} {$field.nofollow}>{$field.title}</a>
{/eyou:links}
```

## 参数

| 参数 | 说明 |
|------|------|
| `type` | `text`文字 / `image`图片 / `all`全部 |
| `groupid` | 链接分组ID；`all` 为全部分组（默认输出默认分组） |
| `loop` | 链接数量 |
| `titlelen` | 标题截取字数 |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.url}` | 链接URL |
| `{$field.title}` | 链接标题 |
| `{$field.logo}` | 图片链接的图片地址（type='image' 时使用） |
| `{$field.target}` | 新窗口属性 |
| `{$field.nofollow}` | nofollow属性 |
