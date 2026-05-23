# `{eyou:artlist}` — 文章列表

> **用途**：获取网站栏目（文章、产品、图集、软件等）的文档列表，可用于首页、列表页、内容页。
> **官方文档**：https://www.eyoucms.com/doc/label/all/491.html
> **关联表**：[`ey_archives`](../dict/ey_archives.md)

---

## 语法

```html
{eyou:artlist typeid='栏目ID' loop='10' titlelen='30' infolen='160' orderby='add_time' id='field'}
  <a href="{$field.arcurl}">{$field.title}</a>
{/eyou:artlist}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `typeid` | string | 栏目ID，首页可用逗号分隔多个（同模型），列表/内容页可省略 |
| `notypeid` | string | 排除的栏目ID，不可与 typeid 同时使用 |
| `tagid` | string | 唯一标识，配合 artpagelist 实现瀑布流分页 |
| `loop` | int | 返回总数（与 limit 不可同时使用） |
| `limit` | string | 范围，如 `'0,10'`（取10条）/ `'2,8'`（跳过前2条取8条） |
| `aid` | int | 指定单个文档ID |
| `aidlist` | string | 指定多个文档ID，逗号分隔 |
| `idrange` | string | aid范围，如 `'1-3'` |
| `titlelen` | int | 标题截取字数 |
| `infolen` | int | 简介截取字数 |
| `addfields` | string | 自定义字段名，逗号分隔，如 `'price,spec'` |
| `orderby` | string | 排序字段：`new`/`hot`/`click`/`add_time`/`update_time`/`aid`/`sort_order`/`rand` |
| `ordermode` | string | 排序方向：`desc`（默认）或 `asc` |
| `modelid` | int | 频道ID，优先级高于 typeid |
| `keyword` | string | 含指定关键字的文档，逗号分隔多个 |
| `flag` | string | 属性过滤：推荐`c`、跳转`j` |
| `noflag` | string | 排除属性，不可与 flag 同时使用 |
| `empty` | string | 无数据时显示的文案 |
| `mod` | int | 每隔N条触发，配合 `{eyou:eq name='mod' value='0'}` 使用 |
| `thumb` | string | 缩略图：`on`（默认）/ `off` |
| `arcrank` | string | 阅读权限：`on` 开启 / `off`（默认）关闭 |
| `id` | string | 自定义循环变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.arcurl}` | 文档URL |
| `{$field.title}` | 文档标题 |
| `{$field.litpic}` | 缩略图 |
| `{$field.add_time}` | 发布时间（时间戳） |
| `{$field.level_name}` | 阅读权限会员等级名 |
| `{$field.level_value}` | 阅读权限会员等级值 |
| `{$key}` | 索引（从0开始） |
| `{$i}` | 顺序（从1开始） |

## 示例

```html
<!-- 调用指定栏目最新5篇文章 -->
{eyou:artlist typeid='2' loop='5' titlelen='30' id='field'}
  <li><a href="{$field.arcurl}">{$field.title}</a></li>
{/eyou:artlist}

<!-- 每隔3条换行 -->
{eyou:artlist typeid='2' loop='9' mod='3' id='field'}
  <a href="{$field.arcurl}">{$field.title}</a>
  {eyou:eq name='mod' value='0'}<br/>{/eyou:eq}
{/eyou:artlist}

<!-- 嵌套标签，内层重定义变量名避免冲突 -->
{eyou:artlist typeid='2' loop='5' id='field'}
  <li>
    <a href="{$field.arcurl}">{$field.title}</a>
    {eyou:tags sort='now' getall='0' loop='100' id='field1'}
      <a href='{$field1.link}'>{$field1.tag}</a>
    {/eyou:tags}
  </li>
{/eyou:artlist}
```
