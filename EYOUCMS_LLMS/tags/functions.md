# 模板常用函数（管道调用）

> **用途**：作用于模板变量，通过 `|` 管道调用，`###` 代表当前变量值。
> **官方文档**：https://www.eyoucms.com/doc/label/all/546.html

---

## 函数列表

| 函数 | 示例 | 说明 |
|------|------|------|
| `MyDate` | `{$field.add_time\|MyDate='Y-m-d',###}` | 日期格式化 |
| `text_msubstr` | `{$field.title\|text_msubstr=###,0,30,true}` | 纯文本截取（自带省略号） |
| `html_msubstr` | `{$field.content\|html_msubstr=###,0,250,true}` | 富文本截取（自动过滤HTML） |
| `gettoptype` | `{$field.id\|gettoptype=###,typename}` | 获取栏目最顶级名称 |
| `GetTotalArc` | `{$eyou.field.typeid\|GetTotalArc=###}` | 统计栏目文档数 |
| `htmlspecialchars_decode` | `{$eyou.field.自定义字段\|htmlspecialchars_decode=###}` | 自定义字段HTML解码 |

## 示例

```html
<!-- 日期格式化 -->
{$eyou.field.update_time|MyDate='Y-m-d H:i:s',###}
<!-- 输出：2024-05-20 13:14:00 -->

<!-- 外贸日期格式 -->
{$eyou.field.update_time|MyDate='F d, Y, H:i\\h',###}
<!-- 输出：May 07, 2024, 15:56h -->

<!-- 截取标题10个字（含省略号） -->
{$field.title|text_msubstr=###,0,10,true}

<!-- 截取内容250字（过滤HTML） -->
{$field.content|html_msubstr=###,0,250,true}

<!-- 获取栏目文档数 -->
{$eyou.field.typeid|GetTotalArc=###}
```
