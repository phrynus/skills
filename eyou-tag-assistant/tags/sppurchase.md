# `{eyou:sppurchase}` — 商品购买

> **用途**：商品详情页的完整购买组件，含规格选择、数量操作、价格显示、加购/立即购买按钮。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/31362.html

---

## 语法

```html
{eyou:sppurchase id='field' currentstyle='btn-danger'}
  <!-- 价格 -->
  <span>￥{$field.spec_price}</span>      <!-- 规格价 -->
  <span>￥{$field.users_price}</span>     <!-- 会员价 -->
  <span>￥{$field.crossed_price}</span>   <!-- 划线价 -->
  <span>￥{$field.old_price}</span>       <!-- 原价 -->
  <span>￥{$field.totol_price}</span>     <!-- 商品总价 -->

  <!-- 规格 -->
  <div class="ey-spec">
    {eyou:volist name="$field.ReturnData" id='field2'}
      <label>{$field2.spec_name}</label>
      {eyou:volist name="$field2.spec_value" id='field3'}
        <a {$field3.SpecData} class="btn {$field3.SpecClass}">
          {eyou:notempty name="$field3.spec_image"}
            <img src="{$field3.spec_image}" />
          {/eyou:notempty}
          {$field3.spec_value}
        </a>
      {/eyou:volist}
    {/eyou:volist}
  </div>

  <!-- 数量 -->
  <div class="ey-number">
    <button {$field.ReduceQuantity}>-</button>
    <input type="text" {$field.UpdateQuantity}>
    <button {$field.IncreaseQuantity}>+</button>
  </div>

  <!-- 库存 -->
  <span {$field.stock_show}>库存：{$field.stock_count} 件</span>

  <!-- 购买按钮 -->
  <a href="javascript:void(0);" {$field.ShopAddCart}>加入购物车</a>
  <a href="javascript:void(0);" {$field.BuyNow}>立即购买</a>

  {$field.hidden}
{/eyou:sppurchase}
```

## 关键变量

| 变量 | 说明 |
|------|------|
| `{$field.spec_price}` | 规格价 |
| `{$field.users_price}` | 会员价 |
| `{$field.crossed_price}` | 划线价 |
| `{$field.old_price}` | 原价 |
| `{$field.totol_price}` | 商品总价 |
| `{$field.ReturnData}` | 规格数组 |
| `{$field3.SpecData}` | 规格选择 data 属性 |
| `{$field3.SpecClass}` | 规格选中 class |
| `{$field.ReduceQuantity}` | 减少数量按钮事件 |
| `{$field.UpdateQuantity}` | 数量输入框属性 |
| `{$field.IncreaseQuantity}` | 增加数量按钮事件 |
| `{$field.stock_show}` | 库存显示控制属性 |
| `{$field.stock_count}` | 库存数量 |
| `{$field.ShopAddCart}` | 加入购物车事件 |
| `{$field.BuyNow}` | 立即购买事件 |
| `{$field.hidden}` | 必须输出的隐藏域 |
