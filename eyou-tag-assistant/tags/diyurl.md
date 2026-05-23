# `{eyou:diyurl}` — 内链URL / 列表排序

> **用途**：① 输出系统内置页面URL（登录、注册、搜索等）；② 在列表页输出排序链接。
> **官方文档（内链）**：https://www.eyoucms.com/doc/label/all/8391.html
> **官方文档（排序）**：https://www.eyoucms.com/doc/label/list/11823.html

---

## 用法一：系统内链URL

```html
<a href="{eyou:diyurl type='tags' /}">TAG标签</a>
<a href="{eyou:diyurl type='login' /}">登录</a>
<a href="{eyou:diyurl type='reg' /}">注册</a>
<a href="{eyou:diyurl type='sindex' /}">搜索</a>
<a href="{eyou:diyurl type='citysite' /}">城市站点</a>
```

### 内链 type 取值

| type 值 | 说明 |
|---------|------|
| `tags` | TAG标签主页 |
| `login` | 登录页 |
| `reg` | 注册页 |
| `sindex` | 搜索主页 |
| `citysite` | 多城市分站主页 |

---

## 用法二：列表页排序链接

```html
<!-- 自动附加 href 和激活 class -->
<a {eyou:diyurl type='DefaultUrl' class='ey_active' /}>默认</a>
<a {eyou:diyurl type='SalesUrl' class='ey_active' /}>销量</a>
<a {eyou:diyurl type='PriceUrl' class='ey_active' /}>价格</a>
<a {eyou:diyurl type='NewUrl' class='ey_active' /}>新品</a>
<a {eyou:diyurl type='AppraiseUrl' class='ey_active' /}>评价</a>
<a {eyou:diyurl type='CollectionUrl' class='ey_active' /}>收藏</a>
<a {eyou:diyurl type='ClickUrl' class='ey_active' /}>点击量</a>
<a {eyou:diyurl type='DownloadUrl' class='ey_active' /}>下载量</a>
```

## 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `type` | string | URL类型，见上方各取值表 |
| `class` | string | 激活状态 class 名（排序链接时使用） |
