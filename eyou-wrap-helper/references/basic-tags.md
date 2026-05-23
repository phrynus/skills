# EyouCMS 基础标签速查

> 只收录扒站套模板最常用的基础标签，花哨的不用。
> 每个标签都配**原站代码 → EyouCMS 标签**对照，直接照着改。

---

## 目录

- [全局变量](#全局变量)
- [引用公共文件](#引用公共文件)
- [导航菜单](#导航菜单)
- [首页文章列表](#首页文章列表)
- [列表页](#列表页)
- [内容页](#内容页)
- [分页](#分页)
- [面包屑](#面包屑)
- [上下篇](#上下篇)
- [搜索表单](#搜索表单)
- [友情链接](#友情链接)
- [广告](#广告)
- [条件判断](#条件判断)
- [点击数](#点击数)
- [常用管道函数](#常用管道函数)

---

## 全局变量

| 原站代码 | 替换为 |
|---------|--------|
| `<title>某公司官网</title>` | `<title>{eyou:global name='web_title' /}</title>` |
| `<meta name="keywords" content="关键词">` | `<meta name="keywords" content="{eyou:global name='web_keywords' /}">` |
| `<meta name="description" content="描述">` | `<meta name="description" content="{eyou:global name='web_description' /}">` |
| `© 2024 某公司 版权所有` | `{eyou:global name='web_copyright' /}` |
| `<img src="/logo.png" alt="某公司">` | `<img src="{eyou:global name='web_logo' /}" alt="{eyou:global name='web_name' /}">` |
| `ICP备XXXXXXXX号` | `{eyou:global name='web_recordnum' /}` |

常用全局变量名：

| 变量名 | 说明 |
|--------|------|
| `web_title` | 网站标题（浏览器标签栏） |
| `web_name` | 网站名称 |
| `web_keywords` | 网站关键词 |
| `web_description` | 网站描述 |
| `web_logo` | 网站 LOGO 图片路径 |
| `web_copyright` | 版权信息 |
| `web_recordnum` | ICP 备案号 |
| `web_templeturl` | 当前模板目录路径 |
| `web_cmsurl` | 网站根目录路径 |
| `web_basehost` | 网站域名 |

---

## 引用公共文件

把拆出来的公共文件引用到模板中：

```html
<!-- 放在每个页面顶部 -->
{eyou:include file="header.htm" /}

<!-- 放在导航位置 -->
{eyou:include file="nav.htm" /}

<!-- 放在页面底部 -->
{eyou:include file="footer.htm" /}
```

---

## 导航菜单

**原站：**
```html
<ul class="nav">
  <li><a href="/">首页</a></li>
  <li><a href="/about/">关于我们</a></li>
  <li><a href="/product/">产品中心</a></li>
  <li><a href="/news/">新闻资讯</a></li>
  <li><a href="/contact/">联系我们</a></li>
</ul>
```

**替换后（结构、类名完全不变）：**
```html
<ul class="nav">
  {eyou:models type='top' loop='10' currentclass='active' id='field'}
  <li><a href="{$field.typeurl}" class="{$field.currentclass}">{$field.typename}</a></li>
  {/eyou:models}
</ul>
```

**两级导航（带子菜单）：**

原站导航带下拉的，套两层：
```html
<ul class="nav">
  {eyou:models type='top' loop='10' id='field1' currentclass='active'}
  <li class="{$field1.currentclass}">
    <a href="{$field1.typeurl}">{$field1.typename}</a>
    {eyou:notempty name='$field1.children'}
    <ul class="sub-menu">
      {eyou:models name='$field1.children' id='field2' loop='10'}
      <li><a href="{$field2.typeurl}">{$field2.typename}</a></li>
      {/eyou:models}
    </ul>
    {/eyou:notempty}
  </li>
  {/eyou:models}
</ul>
```

---

## 首页文章列表

**原站：**
```html
<div class="news-list">
  <div class="item">
    <a href="/news/1.html"><img src="/uploads/thumb1.jpg" alt="新闻标题1"></a>
    <h3><a href="/news/1.html">新闻标题1</a></h3>
    <p class="date">2024-01-15</p>
    <p class="desc">新闻简介文字...</p>
  </div>
  <div class="item">
    <a href="/news/2.html"><img src="/uploads/thumb2.jpg" alt="新闻标题2"></a>
    <h3><a href="/news/2.html">新闻标题2</a></h3>
    <p class="date">2024-01-10</p>
    <p class="desc">新闻简介文字...</p>
  </div>
</div>
```

**替换后（只保留第一个 .item 作为循环模板）：**
```html
<div class="news-list">
  {eyou:artlist typeid='1' loop='6' titlelen='30' infolen='160' id='field'}
  <div class="item">
    <a href="{$field.arcurl}"><img src="{$field.litpic}" alt="{$field.title}"></a>
    <h3><a href="{$field.arcurl}">{$field.title}</a></h3>
    <p class="date">{$field.add_time|MyDate='Y-m-d',###}</p>
    <p class="desc">{$field.seo_description|html_msubstr=###,0,100,true}</p>
  </div>
  {/eyou:artlist}
</div>
```

**artlist 常用参数：**

| 参数 | 说明 | 示例 |
|------|------|------|
| `typeid` | 栏目ID（首页必填） | `typeid='1'` 或 `typeid='1,2,3'` |
| `loop` | 取多少条 | `loop='6'` |
| `titlelen` | 标题截取字数 | `titlelen='30'` |
| `infolen` | 简介截取字数 | `infolen='160'` |
| `orderby` | 排序方式 | `orderby='add_time'`（默认）`sort_order`（排序）`rand`（随机）`click`（点击）`hot`（热度） |
| `flag` | 属性筛选 | `flag='c'`（推荐） |

**artlist 内置变量：**

| 变量 | 说明 |
|------|------|
| `{$field.arcurl}` | 文章链接 |
| `{$field.title}` | 文章标题 |
| `{$field.litpic}` | 缩略图 |
| `{$field.add_time}` | 发布时间（时间戳，需配合 MyDate） |
| `{$field.seo_description}` | 文章简介/描述 |
| `{$field.seo_keywords}` | 文章关键词 |
| `{$key}` | 序号（从0开始） |
| `{$i}` | 序号（从1开始） |

---

## 列表页

> 用在 `lists_article.htm`、`lists_product.htm` 等列表页模板，自动绑定当前栏目。

**原站：**
```html
<div class="product-grid">
  <div class="product-item">
    <a href="/product/1.html"><img src="/uploads/p1.jpg" alt="产品1"></a>
    <h4><a href="/product/1.html">产品1</a></h4>
    <p class="price">¥199</p>
  </div>
  <!-- 多个重复项... -->
</div>
```

**替换后：**
```html
<div class="product-grid">
  {eyou:list loop='12' titlelen='30' id='field'}
  <div class="product-item">
    <a href="{$field.arcurl}"><img src="{$field.litpic}" alt="{$field.title}"></a>
    <h4><a href="{$field.arcurl}">{$field.title}</a></h4>
    <p class="price">{$field.自定义价格字段}</p>
  </div>
  {/eyou:list}
</div>
<!-- 分页 -->
<div class="pagination">
  {eyou:pagelist listitem='index,pre,pageno,next,end,info' listsize='2' /}
</div>
```

> **注意**：`{eyou:list}` 和 `{eyou:pagelist}` 配套使用，一个列表页只能用**一个** list 标签。

---

## 内容页

> 用在 `view_article.htm`、`view_product.htm` 等内容页模板。

**原站：**
```html
<div class="detail">
  <h1>产品名称</h1>
  <div class="meta">
    <span>发布时间：2024-01-15</span>
    <span>点击：1234 次</span>
  </div>
  <div class="content">
    产品详细介绍内容...
  </div>
</div>
```

**替换后：**
```html
<div class="detail">
  <h1>{$eyou.field.title}</h1>
  <div class="meta">
    <span>发布时间：{$eyou.field.add_time|MyDate='Y-m-d',###}</span>
    <span>点击：{eyou:arcclick /} 次</span>
  </div>
  <div class="content">
    {$eyou.field.content}
  </div>
</div>
```

**内容页常用变量：**

| 变量 | 说明 |
|------|------|
| `{$eyou.field.title}` | 文档标题 |
| `{$eyou.field.content}` | 文档正文 |
| `{$eyou.field.add_time}` | 发布时间 |
| `{$eyou.field.update_time}` | 更新时间 |
| `{$eyou.field.seo_description}` | 文档描述 |
| `{$eyou.field.seo_keywords}` | 文档关键词 |
| `{$eyou.field.litpic}` | 缩略图 |
| `{$eyou.field.typeid}` | 当前栏目ID |
| `{$eyou.field.aid}` | 当前文档ID |
| `{$eyou.field.click}` | 点击数 |
| `{$eyou.field.typename}` | 当前栏目名称 |

---

## 分页

用在列表页，搭配 `{eyou:list}` 使用。

```html
<!-- 完整分页 -->
{eyou:pagelist listitem='index,pre,pageno,next,end,info' listsize='2' /}

<!-- 简洁分页（仅上下页+页码） -->
{eyou:pagelist listitem='pre,pageno,next' listsize='3' /}
```

listitem 取值：`index`首页 `pre`上一页 `pageno`数字页码 `next`下一页 `end`末页 `info`共N页N条

---

## 面包屑

```html
<!-- 原站 -->
<div class="breadcrumb">首页 > 产品中心 > 产品详情</div>

<!-- 替换后 -->
<div class="breadcrumb">
  你的位置：{eyou:position style='crumb' /}
</div>
```

> 直接输出，无需循环。系统自动生成面包屑 HTML 和链接。

---

## 上下篇

**原站：**
```html
<div class="prevnext">
  <span class="prev">上一篇：<a href="/news/1.html">上一篇新闻</a></span>
  <span class="next">下一篇：<a href="/news/3.html">下一篇新闻</a></span>
</div>
```

**替换后：**
```html
<div class="prevnext">
  <span class="prev">
    {eyou:beafter get='pre' id='field'}
      <a href="{$field.arcurl}">上一篇：{$field.title}</a>
    {eyou:else /}上一篇：暂无
    {/eyou:beafter}
  </span>
  <span class="next">
    {eyou:beafter get='next' id='field'}
      <a href="{$field.arcurl}">下一篇：{$field.title}</a>
    {eyou:else /}下一篇：暂无
    {/eyou:beafter}
  </span>
</div>
```

---

## 搜索表单

**原站：**
```html
<div class="search-box">
  <form action="/search.php" method="get">
    <input type="text" name="keyword" placeholder="搜索">
    <button type="submit">搜索</button>
  </form>
</div>
```

**替换后：**
```html
<div class="search-box">
  {eyou:searchform type='default' id='field'}
  <form method="get" action="{$field.action}">
    <input type="text" name="keywords" placeholder="搜索">
    <button type="submit">搜索</button>
    {$field.hidden}
  </form>
  {/eyou:searchform}
</div>
```

---

## 友情链接

**原站：**
```html
<div class="links">
  <a href="http://example.com" target="_blank">友情链接1</a>
  <a href="http://example2.com" target="_blank">友情链接2</a>
</div>
```

**替换后：**
```html
<div class="links">
  {eyou:links type='text' loop='20' id='field'}
  <a href="{$field.url}" {$field.target} {$field.nofollow}>{$field.title}</a>
  {/eyou:links}
</div>
```

图片链接（logo 友链）：
```html
{eyou:links type='image' loop='20' id='field'}
<a href="{$field.url}" {$field.target}>
  <img src="{$field.logo}" alt="{$field.title}">
</a>
{/eyou:links}
```

---

## 广告

**原站：**
```html
<div class="banner">
  <a href="/link1"><img src="/uploads/banner1.jpg" alt="广告1"></a>
  <a href="/link2"><img src="/uploads/banner2.jpg" alt="广告2"></a>
</div>
```

**替换后：**
```html
<div class="banner">
  {eyou:adv pid='1' loop='5' id='field'}
  <a href="{$field.links}" {$field.target}>
    <img src="{$field.litpic}" alt="{$field.title}">
  </a>
  {/eyou:adv}
</div>
```

> `pid` 是后台广告位置的ID，不记得先写 `pid='1'` 回头改。

---

## 条件判断

判断变量不为空时才输出：
```html
{eyou:notempty name='$eyou.field.seo_title'}
  {$eyou.field.seo_title}
{eyou:else /}
  {$eyou.field.title}
{/eyou:notempty}
```

判断是否有子栏目（配合二级导航）：
```html
{eyou:notempty name='$field1.children'}
  <ul class="sub-menu">...</ul>
{/eyou:notempty}
```

---

## 点击数

```html
<!-- 内容页显示/累计点击 -->
<span>浏览：{eyou:arcclick /} 次</span>
```

---

## 常用管道函数

| 函数 | 用途 | 示例 |
|------|------|------|
| `MyDate` | 时间戳转日期 | `{$field.add_time\|MyDate='Y-m-d',###}` |
| `html_msubstr` | 富文本截取（过滤HTML） | `{$field.content\|html_msubstr=###,0,250,true}` |
| `text_msubstr` | 纯文本截取（含省略号） | `{$field.title\|text_msubstr=###,0,30,true}` |

---

## 常见错误

| 错误写法 | 正确写法 |
|---------|---------|
| `{eyou:artlist typeid=2}` | `{eyou:artlist typeid='2'}`（参数值要引号） |
| `{$field.arcurl}` 用在内容页 | 内容页用 `{$eyou.field.title}`（加 `eyou.` 前缀） |
| 内外层都用 `id='field'` | 内层改 `id='field2'` 避免变量覆盖 |
| `{eyou:sppurchase /}` 自闭合 | 花哨标签不用管，基本标签用不上 |

> 更详细的标签文档见 `../eyou-tag-assistant/tags/` 目录。
