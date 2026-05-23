# `{eyou:adv}` — 广告列表

> **用途**：获取指定广告位的广告列表。
> **官方文档**：https://www.eyoucms.com/doc/label/all/511.html
> **关联表**：[`ey_ad`](../dict/ey_ad.md)

---

## 语法

```html
{eyou:adv pid='1' loop='3' id='field'}
  <a href='{$field.links}' {$field.target}>
    <img src='{$field.litpic}' alt='{$field.title}' />
  </a>
{/eyou:adv}
```

## 参数

| 参数 | 说明 |
|------|------|
| `pid` | 广告位置ID（后台广告管理中查看） |
| `loop` | 返回广告总数 |
| `orderby` | 排序：`now`最新 / `hot`/`click`点击数 / `sort_order`排序号 / `rand`随机 / 自定义多字段 |
| `currentclass` | 激活状态 class 名 |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.links}` | 广告链接URL |
| `{$field.title}` | 广告标题 |
| `{$field.litpic}` | 广告图片 |
| `{$field.intro}` | 广告描述 |
| `{$field.target}` | 新窗口属性（后台配置） |
| `{$key}` | 索引（从0） |
| `{$i}` | 顺序（从1） |

## 示例

```html
<!-- 每3条后加分割线 -->
{eyou:adv pid='1' loop='9' mod='3' id='field'}
  <a href='{$field.links}'><img src='{$field.litpic}' alt='{$field.title}' /></a>
  {eyou:eq name='mod' value='0'}<hr />{/eyou:eq}
{/eyou:adv}
```
