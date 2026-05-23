# `{eyou:models}` — 栏目列表

> **用途**：获取栏目信息，常用于导航、侧边栏，支持多层嵌套。别名：`channel`。
> **官方文档**：https://www.eyoucms.com/doc/label/all/492.html
> **关联表**：[`ey_arctype`](../dict/ey_arctype.md)

---

## 语法

```html
{eyou:models type='top' loop='8' currentclass='active' id='field'}
  <li class="{$field.currentclass}">
    <a href="{$field.typeurl}" {$field.extends}>{$field.typename}</a>
  </li>
{/eyou:models}
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `typeid` | int | 指定栏目ID |
| `type` | string | 范围：`top`顶级 / `son`下级 / `self`同级 / `sonself`下级+同级 / `first`最顶级的一级 |
| `loop` | int | 返回总数 |
| `limit` | string | 范围，如 `'0,10'` |
| `offset` | int | 跳过前N条 |
| `titlelen` | int | 栏目名截取字数 |
| `currentclass` | string | 当前栏目激活的 class 名 |
| `name` | string | 子栏目数组变量名，三级嵌套时使用 |
| `empty` | string | 无数据时显示文案 |
| `mod` | int | 每隔N条触发 |
| `id` | string | 自定义循环变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.typeurl}` | 栏目URL |
| `{$field.typename}` | 栏目名称 |
| `{$field.currentclass}` | 当前栏目时输出 currentclass 值，否则空 |
| `{$field.extends}` | 新窗口/nofollow等属性，直接放入 `<a>` 标签 |
| `{$field.children}` | 子栏目数组，配合 `{eyou:notempty}` 判断是否有子栏目 |

## 示例

```html
<!-- 顶级栏目导航 -->
{eyou:models type='top' loop='10' currentclass='active' id='field'}
  <a href="{$field.typeurl}" class="{$field.currentclass}">{$field.typename}</a>
{/eyou:models}

<!-- 两级嵌套导航 -->
{eyou:models type='top' loop='10' id='field1' currentclass='active'}
  <li>
    <a href="{$field1.typeurl}" class="{$field1.currentclass}">{$field1.typename}</a>
    {eyou:notempty name='$field1.children'}
      <ul>
        {eyou:models name='$field1.children' id='field2' loop='10'}
          <a href="{$field2.typeurl}">{$field2.typename}</a>
        {/eyou:models}
      </ul>
    {/eyou:notempty}
  </li>
{/eyou:models}
```
