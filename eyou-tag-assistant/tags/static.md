# `{eyou:static}` — 静态资源引入

> **用途**：加载 CSS/JS/图片，自动追加版本号防止浏览器缓存。
> **官方文档**：https://www.eyoucms.com/doc/label/all/11919.html

---

## 语法

```html
<!-- 绝对路径（从网站根目录） -->
{eyou:static file='/static/css/style.css' /}

<!-- 相对路径（相对模板目录） -->
{eyou:static file='skin/css/style.css' /}

<!-- 同时加载多个文件 -->
{eyou:static file='skin/js/common.js,skin/css/style.css' /}
```

## 参数

| 参数 | 说明 |
|------|------|
| `file` | 资源文件路径，多个用逗号分隔 |
