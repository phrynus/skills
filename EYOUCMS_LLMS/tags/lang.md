# `{eyou:lang}` — 语言包变量

> **用途**：输出后台配置的语言包变量值，实现模板多语言化（将模板中的中文替换为变量调用）。
> **官方文档**：https://www.eyoucms.com/doc/label/language/6059.html
> **关联表**：[`ey_language_pack`](../dict/ey_language_pack.md)

---

## 语法

```html
{eyou:lang name='变量名' /}
```

## 参数

| 参数 | 说明 |
|------|------|
| `name` | 语言包变量名（来自后台→语言设置→模板语言变量/官方语言包变量） |

## 示例

```html
<!-- 将"网站首页"替换为多语言变量 -->
{eyou:lang name='sys9' /}
```
