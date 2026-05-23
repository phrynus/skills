# `{eyou:specialnode}` — 专题文档节点

> **用途**：获取专题页指定节点的文档列表。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/10999.html
> **关联表**：[`ey_archives`](../dict/ey_archives.md)

---

## 语法

```html
<!-- 在专题内容页使用（无需指定 aid） -->
{eyou:specialnode code='节点标识' id='field'}
  <a href='{$field.arcurl}'>{$field.title}</a>
{/eyou:specialnode}

<!-- 在非专题页使用（必须指定 aid） -->
{eyou:specialnode aid='专题文档ID' code='节点标识' id='field'}
  <a href='{$field.arcurl}'>{$field.title}</a>
{/eyou:specialnode}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `aid` | int | 专题内容页文档ID，非专题页必填 |
| `code` | string | 节点标识，每篇专题内页唯一 |
| `isauto` | int | 文档来源：`0`按文档列表 / `1`自动获取 |
| `aidlist` | string | 手动指定文档ID列表 |
| `keywords` | string | 关键字，逗号分隔 |
| `typeid` | int | 栏目ID |
| `loop` | int | 返回总数 |
| `titlelen` | int | 标题截取字数 |
| `thumb` | string | 缩略图：`on`/`off` |
| `empty` | string | 无数据文案 |
| `id` | string | 自定义变量名，默认 `field` |
