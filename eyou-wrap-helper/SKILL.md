---
name: eyou-wrap-tags
description: |
  EyouCMS 套标签专用 — 扒站后把静态 HTML 替换为 EyouCMS 基础模板标签（不含商城/会员/多语言/视频等花哨标签）。

  核心工作方式：AI 通过阅读 HTML 理解页面结构，然后逐部分替换为标签。不是机械执行脚本，而是理解内容再动手。

  触发场景：
  - 不自动触发，只有引用才触发

  注意：eyoucms-template 那套是全流程模板建站，本 skill 专注"只替换标签不动结构"这一件事，更轻量
compatibility: python（使用 scripts/wrap.py 时需要）
---

# EyouCMS 套标签助手

## 模板结构（严格按此结构）

```
index.htm（首页，完整的 HTML 骨架）：
<!DOCTYPE html>
<html>
<head>
  {eyou:include file="header.htm" /}     ← header.htm 只含 <head> 内部内容
</head>
<body>
  {eyou:include file="nav.htm" /}        ← nav 放在 <body> 顶部

  页面主体内容...

  {eyou:include file="footer.htm" /}     ← footer 放在 <body> 底部
</body>
</html>
```

**各文件职责：**
| 文件 | 包含什么 | 不包含什么 |
|------|---------|-----------|
| `header.htm` | `<head>` 内部的 meta/title + 所有 CSS `<link>` + `<script>` | `<head>` 标签本身、`<body>`、LOGO |
| `nav.htm` | `<body>` 顶部的导航 HTML | 页面骨架标签 |
| `footer.htm` | `<body>` 底部的版权/联系方式 | 页面骨架标签 |
| `index.htm` | DOCTYPE + html + head + body 完整骨架 + include 引用 + 页面主体内容 | 不能缺少 DOCTYPE 或 html 标签 |

**规则 1：必须拆公共文件**
每个扒站项目必须从首页提取并生成 header.htm、nav.htm、footer.htm 三个公共文件。不存在"不需要拆"、"页面太简单不用拆"的情况。如果不拆公共文件，这个任务就是失败的。

**规则 2：绝对禁止修改 HTML 结构 — 只改文本内容，不改标签本身**
你只能做一件事：**把标签之间的文本内容替换为 EyouCMS 变量**。HTML 标签、属性名、标签层级、标签顺序、CSS 类名，一律不准动。

✅ 正确示范（只改内容）：

```html
<!-- 改之前 -->
<h1>产品名称</h1>
<p class="date">2024-01-15</p>
<img src="/uploads/1.jpg" alt="产品图" />

<!-- 改之后 — 标签和类名完全不变，只替换了 = 号右边的文本 -->
<h1>{$eyou.field.title}</h1>
<p class="date">{$eyou.field.add_time|MyDate='Y-m-d',###}</p>
<img src="{$eyou.field.litpic}" alt="{$eyou.field.title}" />
```

❌ 错误示范（改了结构）：

```html
<!-- 原代码 -->
<div class="news-item">
  <div class="pic">
    <a href="/news/1.html"><img src="/uploads/1.jpg" alt="标题1" /></a>
  </div>
  <div class="info">
    <h3><a href="/news/1.html">标题1</a></h3>
    <p class="desc">简介文字...</p>
  </div>
</div>

<!-- AI 错误地改了结构 — 合并了 div、改了标签、重排了顺序 -->
<div class="news-item">
  <a href="{$field.arcurl}"><img src="{$field.litpic}" alt="{$field.title}" /></a>
  <h3><a href="{$field.arcurl}">{$field.title}</a></h3>
  <p>{$field.seo_description}</p>
</div>

<!-- 正确做法 — 标签和层级完全不变，只替换内容 -->
<div class="news-item">
  <div class="pic">
    <a href="{$field.arcurl}"><img src="{$field.litpic}" alt="{$field.title}" /></a>
  </div>
  <div class="info">
    <h3><a href="{$field.arcurl}">{$field.title}</a></h3>
    <p class="desc">{$field.seo_description|html_msubstr=###,0,160,true}</p>
  </div>
</div>
```

**变通规则**：只有 href、src、alt 这三个属性可以替换值，其他属性（class、id、style、data-\* 等）一律保持原样。

**规则 2 补充：所有 CSS/JS 引用必须保留，无论出现在哪里**

- `<head>` 中的 `<link>` 和 `<script>` 不能删
- 页面底部的 `<script>` 不能删（很多 JS 在 body 末尾加载）
- 页面中间的 `<style>` 或 `<script>` 不能删
- 不能把 CSS/JS 从一处搬到另一处，保持原位置不变
- 唯一例外：统计代码（百度统计、cnzz 等）可以清理，但先问用户要不要保留

**规则 3：所有页面必须按标准骨架引入公共文件**
每个页面的骨架必须是：

```html
<!DOCTYPE html>
<html>
  <head>
    {eyou:include file="header.htm" /}
  </head>
  <body>
    {eyou:include file="nav.htm" /}

    <!-- 页面主体内容 -->

    {eyou:include file="footer.htm" /}
  </body>
</html>
```

- DOCTYPE 和 `<html>` 标签不能丢
- header.htm 放在 `<head>` 内部（不是外面）
- nav.htm 放在 `<body>` 顶部
- footer.htm 放在 `<body>` 底部
- 缺失任何一项、位置放错、或丢了 DOCTYPE/html 骨架，都是失败

**规则 4：禁止使用花哨标签**
你不能使用以下标签：`{eyou:sppurchase}`、`{eyou:attribute}`、`{eyou:comment}`、`{eyou:videoplay}`、`{eyou:language}`、`{eyou:citysite}`、`{eyou:form}`、`{eyou:weapp}`、`{eyou:sql}`。如果用户要求这些，告诉用户去查 `eyou-tag-assistant` 技能。

**规则 5：内容页用 `{$eyou.field.*}`，循环体内用 `{$field.*}`**
这两个不能混用。内容页（文章详情/产品详情页等）里所有变量必须加 `eyou.` 前缀。混淆了这个就是失败。

**规则 6：每页只能有一个 `{eyou:list}` 标签**
一个列表页只能有一个 `{eyou:list}`（配套一个 `{eyou:pagelist}`）。首页不能用 `{eyou:list}`，只能用 `{eyou:artlist}` 且必须指定 `typeid`。

**规则 7：禁止改变文件结构和文件名**

- 不能重命名任何已有文件（`about.html` 保持 `about.html`，不能改成 `lists_single.htm`）
- 不能移动文件到其他目录
- 不能创建新的目录结构
- 所有修改在原文件上直接进行
- 唯一可以新建的文件：header.htm、nav.htm、footer.htm（这三个是公共文件，必须新建）
- 如果用户明确要求重命名，可以用 `python scripts/wrap.py rename`，否则不动

---

## 本 skill 范围（只做这些）

| 类别     | 包含                                                                                                                                                                                        | 不包含                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 全局变量 | `web_title`, `web_keywords`, `web_description`, `web_logo`, `web_copyright`, `web_recordnum`, `web_name`                                                                                    | 自定义全局变量                                                          |
| 公共文件 | header.htm, nav.htm, footer.htm                                                                                                                                                             | 其他片段                                                                |
| 导航     | `{eyou:models}` 一级导航和两级导航                                                                                                                                                          | 特殊结构的导航                                                          |
| 列表     | `{eyou:artlist}`（首页）, `{eyou:list}`（列表页）                                                                                                                                           | 筛选、排序、属性过滤等高级功能                                          |
| 内容页   | `{$eyou.field.title}`, `{$eyou.field.content}`, `{$eyou.field.add_time}`, `{$eyou.field.litpic}`                                                                                            | 自定义字段、多模型字段                                                  |
| 功能组件 | 分页 `{eyou:pagelist}`, 面包屑 `{eyou:position}`, 上下篇 `{eyou:beafter}`, 搜索 `{eyou:searchform}`, 友链 `{eyou:links}`, 广告 `{eyou:adv}`, 点击 `{eyou:arcclick}`, 条件 `{eyou:notempty}` | sppurchase/attribute/comment/videoplay/language/citysite/form/weapp/sql |

遇到"不包含"中的内容 → 停，告诉用户去查 `eyou-tag-assistant`。

---

## 工作流程（严格执行，跳过任何一步即为失败）

### 第 1 步：通读 HTML，识别页面结构

拿到 HTML 后，先通读每个文件，识别以下内容：

| 识别项          | 要干什么                                                        |
| --------------- | --------------------------------------------------------------- |
| **header 区域** | 找到 `<head>` 内的 title/meta，以及顶部品牌区域（LOGO、公司名） |
| **nav 区域**    | 找到导航栏，通常有 `.nav` `.menu` 类或 `<nav>` 标签             |
| **footer 区域** | 找到底部版权、备案号、联系方式区域                              |
| **重复结构**    | 找到多个结构相同的 HTML 块（列表项、产品卡片、新闻条目）        |
| **页面的类型**  | 判断是首页、列表页、内容页还是单页                              |

### 第 2 步：生成公共文件（必须执行）

从首页提取以下三个公共文件：

**header.htm** — 只包含 `<head>` 内部的 meta/title/CSS/JS，不包含 `<head>` 标签本身。

- 保留全部 CSS `<link>` 和 `<script>` 标签（必须保留，否则页面无样式）
- 替换 title/keywords/description 为全局变量
- LOGO 放在 nav.htm 中（因为它在 `<body>` 中），不放在 header.htm

```html
<meta charset="utf-8" />
<title>{eyou:global name='web_title' /}</title>
<meta name="keywords" content="{eyou:global name='web_keywords' /}" />
<meta name="description" content="{eyou:global name='web_description' /}" />
<!-- 原站的全部 CSS 和 JS 链接保留不动 -->
<link rel="stylesheet" href="css/style.css" />
<script src="js/main.js"></script>
```

**nav.htm** — 原样保留导航 HTML 结构和类名，只替换链接。如果页面顶部有 LOGO（通常和导航在一起），保留 LOGO 的 HTML 结构，只替换 src/alt 为全局变量：

```html
<!-- 一级导航 -->
{eyou:models type='top' loop='10' currentclass='active' id='field'}
<li><a href="{$field.typeurl}" class="{$field.currentclass}">{$field.typename}</a></li>
{/eyou:models}

<!-- 两级导航（原站有下拉才用） -->
{eyou:models type='top' loop='10' id='field1' currentclass='active'}
<li>
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
```

**footer.htm**：

```html
<p>{eyou:global name='web_copyright' /} - {eyou:global name='web_recordnum' /}</p>
```

如果 footer 中有联系方式、地址，保留 HTML 结构，标签替换为对应的全局变量。

> **LOGO 处理**：原站 `<img src="/logo.png" alt="公司名">` 保留 HTML 结构不变，只替换值为全局变量：`<img src="{eyou:global name='web_logo' /}" alt="{eyou:global name='web_name' /}">`。LOGO 放在 nav.htm 中（若原站 LOGO 和导航在同一区域）。

### 第 3 步：替换主体内容（逐页处理）

**首页（通常是 index.html / index.htm）**：

- 找到重复结构（多个结构相同的列表项），外套 `{eyou:artlist typeid='栏目ID' loop='N'}`
- 只保留第一个列表项作为模板，删除后续重复项（这是唯一允许的结构精简）
- 替换第一个列表项内的硬编码：`{$field.arcurl}`、`{$field.litpic}`、`{$field.title}` 等
- 除了删除多余的重复项之外，**不动任何其他 HTML 结构**
- 不要忘记 Banner 轮播替换为 `{eyou:adv}`、友链替换为 `{eyou:links}`

**列表页（新闻列表、产品列表等，通常是 news.html / product.html 等原文件名）**：

- 用 `{eyou:list}` 替换循环，**不要加 typeid**（自动绑定当前栏目）
- 必须加分页 `{eyou:pagelist listitem='index,pre,pageno,next,end,info' listsize='2' /}`
- 面包屑 `{eyou:position style='crumb' /}`

**内容页（文章详情、产品详情等，通常是 detail.html / view.html 等原文件名）**：

- 标题、正文、时间、缩略图全部用 `{$eyou.field.*}` 变量
- 用 `{eyou:arcclick /}` 替换点击数
- 上下篇用 `{eyou:beafter get='pre'}` / `{eyou:beafter get='next'}`
- 面包屑 `{eyou:position style='crumb' /}`

**单页（关于我们/联系我们等，保持原文件名如 about.html）**：

- 用 `{$eyou.field.title}` 和 `{$eyou.field.content}` 替换

### 第 4 步：按标准骨架引入公共文件

每个页面必须套上完整的 HTML5 骨架，不能只贴 include 标签：

```html
<!DOCTYPE html>
<html>
  <head>
    {eyou:include file="header.htm" /}
  </head>
  <body>
    {eyou:include file="nav.htm" /}

    <!-- 页面主体内容 -->

    {eyou:include file="footer.htm" /}
  </body>
</html>
```

注意：header.htm 放在 `<head>` 内部，nav/footer 放在 `<body>` 内部。

### 第 5 步：检查清单（必须逐项确认）

**公共文件检查：**

- [ ] header.htm 生成了？包含 title/keywords/description 标签？
- [ ] nav.htm 生成了？链接替换为 `{eyou:models}` 了？
- [ ] footer.htm 生成了？版权替换为全局变量了？

**每页检查：**

- [ ] 页面有完整的 HTML5 骨架（DOCTYPE + html + head + body）？
- [ ] header.htm 在 `<head>` 内部引入？nav.htm 在 `<body>` 顶部？footer.htm 在 `<body>` 底部？
- [ ] HTML 标签、类名、嵌套层级、标签顺序全部和原站一致？（diff 检查，只看标签不看内容）
- [ ] 只修改了 href/src/alt 的值？class/id/style 没有被改过？
- [ ] 没有残留的硬编码标题/链接/图片路径？
- [ ] 列表页有分页 `{eyou:pagelist}`？
- [ ] 内容页用 `{$eyou.field.*}` 而不是 `{$field.*}`？
- [ ] 首页用 `{eyou:artlist}`（有 typeid）而不是 `{eyou:list}`？
- [ ] 没有使用花哨标签？
- [ ] 嵌套标签内层用了自定义 id（如 `id='field2'`）？

---

## 文件中各部分的替换规则

### header 部分

| 原站代码                                  | 替换为                                                                              |
| ----------------------------------------- | ----------------------------------------------------------------------------------- |
| `<title>某公司</title>`                   | `<title>{eyou:global name='web_title' /}</title>`                                   |
| `<meta name="keywords" content="...">`    | `<meta name="keywords" content="{eyou:global name='web_keywords' /}">`              |
| `<meta name="description" content="...">` | `<meta name="description" content="{eyou:global name='web_description' /}">`        |
| `<img src="/logo.png" alt="...">`         | `<img src="{eyou:global name='web_logo' /}" alt="{eyou:global name='web_name' /}">` |

### 循环体内变量映射

| 硬编码 | 替换为（artlist/list 循环内）                           | 替换为（内容页）                             |
| ------ | ------------------------------------------------------- | -------------------------------------------- |
| 标题   | `{$field.title}`                                        | `{$eyou.field.title}`                        |
| 链接   | `{$field.arcurl}`                                       | 不需要                                       |
| 缩略图 | `{$field.litpic}`                                       | `{$eyou.field.litpic}`                       |
| 日期   | `{$field.add_time\|MyDate='Y-m-d',###}`                 | `{$eyou.field.add_time\|MyDate='Y-m-d',###}` |
| 正文   | 不适用                                                  | `{$eyou.field.content}`                      |
| 简介   | `{$field.seo_description\|html_msubstr=###,0,160,true}` | `{$eyou.field.seo_description}`              |
| 点击数 | 不适用                                                  | `{eyou:arcclick /}`                          |

### 功能组件替换

| 原站有什么 | 替换为                                                                     |
| ---------- | -------------------------------------------------------------------------- |
| 面包屑导航 | `{eyou:position style='crumb' /}`                                          |
| 分页       | `{eyou:pagelist listitem='index,pre,pageno,next,end,info' listsize='2' /}` |
| 上一篇     | `{eyou:beafter get='pre' id='field'}...{/eyou:beafter}`                    |
| 下一篇     | `{eyou:beafter get='next' id='field'}...{/eyou:beafter}`                   |
| 搜索表单   | `{eyou:searchform type='default'}...{$field.hidden}{/eyou:searchform}`     |
| 友情链接   | `{eyou:links type='text' loop='20'}`                                       |
| 广告轮播   | `{eyou:adv pid='1' loop='5'}`                                              |
| © 版权     | `{eyou:global name='web_copyright' /}`                                     |
| 备案号     | `{eyou:global name='web_recordnum' /}`                                     |

---

## 关于文件类型（AI 自己理解即可，不改文件名）

读 HTML 时理解出这是首页、列表页还是内容页，在替换标签时用对应的标签语法。

| 实际内容          | 替换标签                                           |
| ----------------- | -------------------------------------------------- |
| 首页              | 用 `{eyou:artlist}` 必须加 typeid                  |
| 列表页            | 用 `{eyou:list}` 不加 typeid，加 `{eyou:pagelist}` |
| 内容页            | 用 `{$eyou.field.*}` 变量                          |
| 单页（关于/联系） | 用 `{$eyou.field.title}` `{$eyou.field.content}`   |

---

## 输出要求

- **不改变任何已有文件的位置和名称**
- 只新建三个公共文件：header.htm、nav.htm、footer.htm（放在原文件同级目录）
- 修改原文件时，只替换硬编码内容为标签，不动其他任何东西
- 每个页面必须套上完整的骨架：DOCTYPE + html + head（含 header.htm include）+ body（含 nav + footer include）

---

## 脚本辅助

`scripts/wrap.py` 提供以下辅助功能。**脚本输出只是初稿，AI 必须逐项复核修正**：

```bash
python scripts/wrap.py init index.html        # 从首页粗提取 header/nav/footer 初稿
python scripts/wrap.py scan ./templates/      # 扫描可能遗漏的硬编码内容
python scripts/wrap.py rename ./templates/    # 批量重命名（仅在用户明确要求时使用）
python scripts/wrap.py clean page.html        # 清理弹窗/统计代码初稿
```

**脚本的限制**（AI 必须手动修正）：

- `init` 命令提取的 header/nav/footer 只是原始 HTML，没有替换标签。AI 必须手动替换为 EyouCMS 标签。
- `scan` 命令可能漏掉复杂结构中的硬编码，AI 必须逐页肉眼检查。
- `rename` 命令默认**不使用**，必须用户明确要求才运行。且运行后 AI 要确认没有破坏文件结构。

---

## 参考资源

- `references/basic-tags.md` — 基础标签速查

## 关联 skill

- **eyou-tag-assistant** — 标签大全，含所有花哨标签的详细语法；本 skill 只含基础部分，遇到复杂标签去那边查
