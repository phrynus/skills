# `{eyou:citysite}` — 城市站点

> **用途**：多城市站群标签，输出城市站点列表，用法与 `models`（channel）标签相似。需专业版授权并开启多城市功能。
> **官方文档**：https://www.eyoucms.com/doc/label/all/11842.html

---

## 语法

```html
{eyou:citysite type='top' loop='8' currentclass='active' id='field'}
  <li class="{$field.currentclass}">
    <a href='{$field.siteurl}'>{$field.name}</a>
  </li>
{/eyou:citysite}
```

## 参数

| 参数 | 说明 |
|------|------|
| `type` | 范围：`top`顶级 / `son`下级 / `self`同级 / `sonself`下级+同级 / `first`最顶级的一级 |
| `siteid` | 指定城市站点ID |
| `notypeid` | 排除的城市站点ID，不可与 siteid 同时使用 |
| `loop` | 返回总数 |
| `limit` | 范围，如 `'0,10'` |
| `offset` | 跳过前N条 |
| `titlelen` | 城市名截取字数 |
| `currentclass` | 当前站点激活 class 名 |
| `name` | 子站点数组变量名，二/三级嵌套时使用 |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.siteurl}` | 城市站点URL |
| `{$field.name}` | 城市站点名称 |
| `{$field.currentclass}` | 当前站点激活 class |
| `{$field.children}` | 子站点数组 |
| `{$field.province_name}` | 文章归属省份名 |
| `{$field.city_name}` | 文章归属城市名 |
| `{$field.area_name}` | 文章归属区县名 |

## 当前城市信息（全局可用）

| 变量 | 说明 |
|------|------|
| `{$eyou.site.name}` | 当前城市名称 |
| `{$eyou.site.seo_title}` | 当前城市SEO标题 |
| `{$eyou.site.seo_keywords}` | 当前城市SEO关键词 |
| `{$eyou.site.seo_description}` | 当前城市SEO描述 |
| `{$eyou.site.name\|default='全国'}` | 未选城市时显示默认值 |

## 示例

```html
<!-- 顶级城市导航 -->
{eyou:citysite type='top' loop='10' currentclass='active' id='field'}
  <a href="{$field.siteurl}" class="{$field.currentclass}">{$field.name}</a>
{/eyou:citysite}

<!-- 两级城市嵌套 -->
{eyou:citysite type='top' loop='10' id='field1' currentclass='active'}
  <li>
    <a href="{$field1.siteurl}" class="{$field1.currentclass}">{$field1.name}</a>
    {eyou:notempty name='$field1.children'}
      <ul>
        {eyou:citysite name='$field1.children' id='field2' loop='10'}
          <a href="{$field2.siteurl}">{$field2.name}</a>
        {/eyou:citysite}
      </ul>
    {/eyou:notempty}
  </li>
{/eyou:citysite}
```
