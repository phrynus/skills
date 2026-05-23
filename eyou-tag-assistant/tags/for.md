# `{eyou:for}` — 计数循环

> **用途**：按数值范围循环，等价于 PHP `for` 循环。
> **官方文档**：https://www.eyoucms.com/doc/label/all/582.html

---

## 语法

```html
{eyou:for start='1' end='10' step='1'}
  {$i}
{/eyou:for}
```

## 参数

| 参数 | 默认 | 说明 |
|------|------|------|
| `start` | — | 起始值 |
| `end` | — | 结束值 |
| `step` | `1` | 每次自增量 |
| `comparison` | `lt` | 比较符：`lt`（小于）/ `gt`（大于） |
| `name` | `i` | 循环变量名 |
