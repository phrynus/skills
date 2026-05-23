# `{eyou:comment}` — 商品评价

> **用途**：在商品详情页输出评价列表，需配合系统评价模板文件。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/11191.html

---

## 前置条件

- PC端：将 `/template/pc/system/product_comment.htm` 放入对应模板目录
- 移动端：将 `product_comment.htm`、`comment_list.htm` 放入 `mobile/system/`

## 语法

```html
{eyou:comment aid='$eyou.field.aid' id='c_field'}
  <div class="evalute" {$c_field.CommentID}></div>
  {$c_field.hidden}
{/eyou:comment}
```

## 参数

| 参数 | 说明 |
|------|------|
| `aid` | 文档ID，内容页用 `$eyou.field.aid` |
| `id` | 自定义变量名，默认 `c_field` |

> `{$c_field.CommentID}` 和 `{$c_field.hidden}` 不可缺少。
