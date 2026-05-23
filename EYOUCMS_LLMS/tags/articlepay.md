# `{eyou:articlepay}` — 文章付费

> **用途**：文章模型实现付费阅读，支持按价格付费、积分付费、会员免费等多种限制类型。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/11810.html

---

## 前置条件

- 后台开启文章模型付费阅读
- 将 `/template/pc/system/article_pay.htm` 放入对应模板目录

## 语法

将内容页原有的 `{$eyou.field.content}` 替换为：

```html
{eyou:articlepay id='field'}
  <!-- 内容区域 -->
  <div {$field.contentId}>{$field.content}</div>

  <!-- 付费提示区域（restric_type=1 金额付费；=4 积分付费；=2/3 会员专享） -->
  {eyou:if condition='$eyou.field.restric_type == 1'}
    <div {$field.displayId}>
      <p>需支付 ￥{$eyou.field.users_price}</p>
      <a {$field.onclick}>立即支付</a>
    </div>
  {eyou:else /}
    <div {$field.vipDisplayId}>
      <a {$field.onBuyVipClick}>购买会员</a>
    </div>
  {/eyou:if}

  {$field.hidden}
{/eyou:articlepay}
```

## 关键变量

| 变量 | 说明 |
|------|------|
| `{$field.contentId}` | 内容容器 id 属性 |
| `{$field.displayId}` | 付费提示容器 id 属性 |
| `{$field.vipDisplayId}` | 会员限制容器 id 属性 |
| `{$field.onclick}` | 付费点击事件 |
| `{$field.onBuyVipClick}` | 购买会员点击事件 |
| `{$field.hidden}` | 必须输出的隐藏域 |
| `{eyou:freebuynum /}` | 已支付人数 |
