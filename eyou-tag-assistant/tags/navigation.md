# `{eyou:navigation}` — 导航菜单

> **用途**：获取后台配置的导航菜单，支持多级嵌套。
> **官方文档**：https://www.eyoucms.com/doc/label/all/11849.html
> **关联表**：[`ey_nav_list`](../dict/ey_nav_list.md)

---

## 语法

```html
{eyou:navigation position_id='1' currentclass='active' id='field'}
  <li class="{$field.currentclass}">
    <a href='{$field.nav_url}' {$field.target} {$field.nofollow}>{$field.nav_name}</a>
  </li>
{/eyou:navigation}
```

## 参数

| 参数 | 说明 |
|------|------|
| `position_id` | 导航分类ID，获取该分类下全部菜单（与 nav_id 二选一） |
| `nav_id` | 菜单ID，获取该菜单的子菜单（与 position_id 二选一） |
| `currentclass` | 激活状态 class 名 |
| `name` | 子菜单数组变量名，二/三级嵌套时使用 |
| `empty` | 无数据文案 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.nav_url}` | 菜单URL |
| `{$field.nav_name}` | 菜单名称 |
| `{$field.currentclass}` | 当前菜单激活 class |
| `{$field.target}` | 新窗口属性 |
| `{$field.nofollow}` | nofollow属性 |
| `{$field.children}` | 子菜单数组 |

## 多级嵌套示例

```html
<!-- 三级导航 -->
{eyou:navigation position_id='1' id='field1' currentclass='active'}
  <li>
    <a href="{$field1.nav_url}" class="{$field1.currentclass}">{$field1.nav_name}</a>
    {eyou:notempty name='$field1.children'}
      <ul>
        {eyou:navigation name='$field1.children' id='field2'}
          <li>
            <a href="{$field2.nav_url}">{$field2.nav_name}</a>
            {eyou:notempty name='$field2.children'}
              <ul>
                {eyou:navigation name='$field2.children' id='field3'}
                  <li><a href="{$field3.nav_url}">{$field3.nav_name}</a></li>
                {/eyou:navigation}
              </ul>
            {/eyou:notempty}
          </li>
        {/eyou:navigation}
      </ul>
    {/eyou:notempty}
  </li>
{/eyou:navigation}
```
