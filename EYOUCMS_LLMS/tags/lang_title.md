# 当前语言标识（lang_title / lang_url / lang_logo）

> **用途**：获取当前正在使用的语言信息（名称、URL、国旗图标），通过全局变量直接调用。
> **官方文档**：https://www.eyoucms.com/doc/label/language/11886.html

---

## 语法

```html
<!-- 当前语言名称 -->
{$eyou.global.lang_title}

<!-- 当前语言切换URL -->
{$eyou.global.lang_url}

<!-- 当前语言国旗图标 -->
{$eyou.global.lang_logo}

<!-- 组合使用：带链接的语言切换按钮 -->
<a href="{$eyou.global.lang_url}">
  <img src="{$eyou.global.lang_logo}" />
  {$eyou.global.lang_title}
</a>
```

## 变量说明

| 变量 | 说明 |
|------|------|
| `{$eyou.global.lang_title}` | 当前语言名称 |
| `{$eyou.global.lang_url}` | 当前语言切换URL |
| `{$eyou.global.lang_logo}` | 当前语言国旗图标 |
