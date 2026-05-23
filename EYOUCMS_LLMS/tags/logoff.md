# 会员注销标签

> **用途**：提供账号注销功能按钮。
> **官方文档**：https://www.eyoucms.com/doc/label/all/30629.html

---

## 语法

```html
{eyou:volist name=":users_log_off();" id='field'}
  <a href="JavaScript:void(0);" {$field.func}>{$field.text}</a>
  {$field.hidden}
{/eyou:volist}
```

> **注意**：`{$field.func}`、`{$field.hidden}` 不可缺少。
