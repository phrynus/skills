# `{eyou:language}` — 语言列表

> **用途**：输出多语言切换列表，配合全局变量 `web_language_switch` 控制显示/隐藏。
> **官方文档**：https://www.eyoucms.com/doc/label/language/6058.html
> **关联表**：[`ey_language`](../dict/ey_language.md)

---

## 语法

```html
{eyou:language type='default' id='field'}
  <a href="{$field.url}">
    <img src="{$field.logo}" alt="{$field.title}">
    {$field.title}
  </a>
{/eyou:language}
```

## 参数

| 参数 | 说明 |
|------|------|
| `type` | `default`不含当前语言 / `list`含当前语言 |
| `limit` | 范围，如 `'0,5'` |
| `titlelen` | 标题截取字数 |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.url}` | 语言切换URL |
| `{$field.title}` | 语言名称 |
| `{$field.logo}` | 语言国旗图标 |

## 示例

```html
<!-- 根据后台开关控制显示 -->
{eyou:notempty name='$eyou.global.web_language_switch'}
  {eyou:language type='default' id='field'}
    <a href="{$field.url}">
      <img src="{$field.logo}" alt="{$field.title}">{$field.title}
    </a>
  {/eyou:language}
{/eyou:notempty}
```
