# `{eyou:downloadpay}` — 下载付费

> **用途**：下载模型实现付费下载，支持免费/付费/会员专享/会员付费等类型。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/28561.html

---

## 前置条件

- 后台在频道模型→下载模型→编辑→开启下载付费
- 将 `/template/pc/system/download_pay.htm` 放入对应模板目录

## 语法

```html
{eyou:downloadpay id='res'}
  <!-- 未购买：显示购买区域 -->
  <div {$res.buyId}>
    <a {$res.onclick} class="btn">立即购买</a>
  </div>

  <!-- 已购买：显示下载区域 -->
  <div {$res.downloadId}>
    {eyou:volist name="$eyou.field.file_list" id="vo"}
      <a href="{$vo.downurl}">{$vo.server_name}</a>
      {eyou:if condition="$vo.extract_code !=''"}
        提取码：{$vo.extract_code}
      {/eyou:if}
    {/eyou:volist}
  </div>

  {$res.hidden}
{/eyou:downloadpay}
```

## 关键变量

| 变量 | 说明 |
|------|------|
| `{$res.buyId}` | 未购买区域容器 id 属性 |
| `{$res.downloadId}` | 已购买下载区域容器 id 属性 |
| `{$res.onclick}` | 购买点击事件 |
| `{$res.hidden}` | 必须输出的隐藏域 |
