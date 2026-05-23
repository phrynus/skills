# `{eyou:notice}` — 站内信

> **用途**：统计未读站内通知数量，展示消息入口。
> **官方文档**：https://www.eyoucms.com/doc/label/all/11112.html

---

## 语法

```html
{eyou:notice id='field'}
  <a href="{$field.url}">站内消息<span id="{$field.id}"></span></a>
  {$field.hidden}
{/eyou:notice}
```

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.url}` | 消息中心URL |
| `{$field.id}` | 未读数量容器的 id 属性（JS动态注入数量） |
| `{$field.hidden}` | 必须输出的隐藏域 |
