# `{eyou:collect}` — 文档收藏

> **用途**：提供收藏/取消收藏按钮及收藏数显示，需会员登录。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/11113.html

---

## 语法

```html
{eyou:collect id='collect' cancel='加入收藏' collect='已收藏'}
  <a {$collect.onclick}>{$collect.cancel}</a>
  收藏数：<span {$collect.numId}></span>
  {$collect.hidden}
{/eyou:collect}
```

## 参数

| 参数 | 默认 | 说明 |
|------|------|------|
| `aid` | 当前文档 | 指定文档ID |
| `cancel` | `加入收藏` | 未收藏状态文案（支持HTML） |
| `collect` | `已收藏` | 已收藏状态文案（支持HTML） |
| `class` | `off` | `on` 启用 class 控制模式 |
| `id` | `collect` | 自定义变量名 |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$collect.onclick}` | 点击事件属性，放入触发元素 |
| `{$collect.cancel}` | 当前状态文案 |
| `{$collect.numId}` | 收藏数容器 id 属性 |
| `{$collect.hidden}` | 必须输出的隐藏域 |
