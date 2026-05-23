# `{eyou:tags}` — Tag标签调用

> **用途**：输出文档关联的TAG标签，或全站/指定栏目的TAG列表。
> **官方文档**：https://www.eyoucms.com/doc/label/all/520.html
> **关联表**：[`ey_tagindex`](../dict/ey_tagindex.md)

---

## 语法

```html
{eyou:tags sort='now' getall='0' loop='100' id='field'}
  <a href='{$field.link}'>{$field.tag}</a>（{$field.total}篇）
{/eyou:tags}
```

## 参数

| 参数 | 说明 |
|------|------|
| `aid` | 文档ID，内容页可省略 |
| `typeid` | 栏目ID，调取某栏目下全部TAG |
| `getall` | `0`当前内容页TAG / `1`全部TAG |
| `loop` | 返回总数 |
| `type` | 栏目范围：`son`/`self`/`top`/`sonself`/`first` |
| `sort` | 排序：`new`最新 / `rand`随机 / `week`周统计 / `month`月统计 / `hot`点击数 / `total`文档数 |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.link}` | TAG页面URL |
| `{$field.tag}` | TAG名称 |
| `{$field.total}` | 该TAG关联的文档数 |

## 示例

```html
<!-- 当前文档的TAG -->
{eyou:tags getall='0' id='field'}
  <a href='{$field.link}'>{$field.tag}</a>
{/eyou:tags}

<!-- 指定栏目下按热度排序的TAG云 -->
{eyou:tags getall='1' typeid='2' loop='50' sort='hot' id='field'}
  <a href='{$field.link}'>{$field.tag}</a>
{/eyou:tags}

<!-- 指定文档ID的TAG（任意页面可用） -->
{eyou:tags getall='0' aid='3' id='field'}
  <a href='{$field.link}'>{$field.tag}</a>
{/eyou:tags}
```
