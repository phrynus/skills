# `{eyou:ad}` — 单条广告

> **用途**：获取指定ID的单条广告数据。
> **官方文档**：https://www.eyoucms.com/doc/label/all/836.html
> **关联表**：[`ey_ad`](../dict/ey_ad.md)

---

## 语法

```html
{eyou:ad aid='广告ID' id='field'}
  <a href='{$field.links}' {$field.target}>
    <img src='{$field.litpic}' alt='{$field.title}' />
  </a>
{/eyou:ad}
```

## 参数

| 参数 | 说明 |
|------|------|
| `aid` | 广告ID |
| `id` | 自定义变量名，默认 `field` |
