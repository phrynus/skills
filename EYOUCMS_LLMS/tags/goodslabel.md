# 商品服务标签（goodsLabel）

> **用途**：在商品详情页输出商品服务标签列表（运费险、七天无理由等）。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/31557.html

---

## 语法

```html
<!-- 商品服务标签（运费险、七天无理由等） -->
{eyou:volist name="$eyou.field.goodsLabel" id="field"}
  {$field.label_title}   <!-- 标签标题 -->
  {$field.label_pic}     <!-- 标签图片路径 -->
  {$field.label_intro}   <!-- 标签描述 -->
{/eyou:volist}
```

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$field.label_title}` | 标签标题 |
| `{$field.label_pic}` | 标签图片路径 |
| `{$field.label_intro}` | 标签描述 |
