# EyouCMS 模板标签 LLM 手册

> **用途**：供 AI 辅助 EyouCMS 模板开发，涵盖所有模板标签用法与数据字典。
>
> **维护说明**：编辑标签 → 修改 `tags/xx.md`（每个标签对应一个独立文件）；更新表结构 → 修改 `dict/xx.md`。

---

## 如何使用

1. **按场景查标签组合** → 看下方「场景 → 标签组合矩阵」找到需要哪些标签
2. **查单个标签用法** → 在「标签速查表」找到标签名，点链接进 `tags/xx.md`
3. **查可用变量和字段** → 在「变量前缀速查」确认用哪个前缀，然后查对应数据字典

---

## 场景 → 标签组合矩阵

用户不会说标签名，他们说需求。这个表告诉你每个需求需要什么标签。

### 内容展示

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 首页文章列表 | `index_article.htm` | `artlist` + 可选 `artpagelist` | 首页必须指定 `typeid` |
| 首页多栏目区块 | `index_article.htm` | `models` + `modelsartlist` | 遍历栏目→取各栏目文档 |
| 列表页文档+分页 | `lists_article.htm` | `list` + `pagelist` | `list` 自动绑定当前栏目 |
| 列表页带筛选 | `lists_article.htm` | `list` + `pagelist` + `screening` | 筛选需要额外配置 |
| 列表页瀑布流 | `lists_article.htm` | `list` + `artpagelist`（配合 `tagid`） | 无限加载 |
| 内容页完整 | `view_article.htm` | `arcview` + `beafter` + `relevarticle` + `arcclick` | 详情+上下篇+相关+点击 |
| 内容页单字段 | `view_article.htm` | `{$eyou.field.xxx}` 直接输出 | 不需标签，直接用变量 |
| 栏目单页（关于我们） | `lists_single.htm` | `arcview` 或 `{$eyou.field.xxx}` | 单页模型不需要 list |

### 导航与链接

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 主导航菜单 | `header.htm` | `models` 或 `navigation` | `models` 取栏目树，`navigation` 取自定义导航 |
| 面包屑导航 | `header.htm` | `position` | 自动显示当前位置 |
| 友情链接 | `footer.htm` | `links` | `type='text'` 文字 / `type='logo'` 图片 |
| 快速导航/内链 | `header.htm` | `diyurl` | 自定义内链列表 |

### 商品与交易

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 商品列表+分页 | `lists_product.htm` | `list` + `pagelist` + `screening` | 同列表页模式 |
| 商品详情+购买 | `view_product.htm` | `arcview` + `sppurchase` + `attribute type='newattr'` | 购买组件必须完整结构 |
| 商品评价 | `view_product.htm` | `comment` | 评价列表 |
| 文章付费阅读 | `view_article.htm` | `articlepay` | 付费后才显示内容 |
| 下载付费 | `view_download.htm` | `downloadpay` | 付费下载 |

### 搜索与标签

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 搜索表单 | `header.htm` / `search.htm` | `searchform` | 需完整结构 |
| 搜索词列表 | `header.htm` / `search.htm` | `hotkeywords` | 热门搜索词 |
| 搜索结果 | `lists_search.htm` | `list`（自动切换搜索模式） | 搜索页模板 |
| TAG 标签云 | 任意页面 | `tags` | 按文档/栏目关联的标签 |
| 相关文档 | `view_article.htm` | `relevarticle` | 自动关联同栏目文档 |

### 广告与互动

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 广告位轮播 | `index_article.htm` | `adv` 或 `ad` | `adv` = 列表，`ad` = 单条 |
| 留言表单 | `lists_contact.htm` | `guestbookform` | 栏目留言 |
| 自由表单 | 任意页面 | `form` | 自定义表单 |
| 表单回复列表 | 任意页面 | `formreply` | 提交后的回复展示 |
| 问答列表 | 任意页面 | `asklist` | 问答功能 |

### 会员与用户

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 登录/注册/退出 | `header.htm` | `user type='userinfo'` | 未登录显示登录链接 |
| 会员列表 | 会员中心 | `memberlist` | 会员展示 |
| 站内信未读数 | 会员中心 | `notice` | 消息提示 |
| 文档关联会员信息 | `view_article.htm` | `memberinfos` | 发布者信息 |
| 会员注销 | 会员中心 | 会员注销功能 | 账号注销按钮 |

### 多媒体

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 视频播放器 | `view_video.htm` | `videoplay` | 视频播放 |
| 视频选集列表 | `view_video.htm` | `videolist` | 选集切换 |

### 高级功能

| 用户需求 | 模板文件 | 标签组合 | 说明 |
|----------|----------|----------|------|
| 多语言切换 | 任意 | `language` + `lang` | 需要开启多语言 |
| 城市分站 | 任意 | `citysite` + `{$eyou.site.name}` | 城市站点列表 |
| 自定义 SQL | 任意 | `sql` | 直接 SQL 查询输出 |
| PHP 逻辑 | 任意 | `php` | 原生 PHP 代码 |
| 应用插件加载 | 任意 | `weapp` | 插件入口 |
| 专题列表 | `lists_special.htm` | `specialnode` | 专题文档节点 |

### 通用逻辑

| 用户需求 | 模板 | 说明 |
|----------|------|------|
| 条件判断 | `if` / `empty` / `notempty` / `switch` / `range` / `eq/neq/gt/lt` 等 | 多种条件标签可选 |
| 赋值/循环 | `assign` / `foreach` / `volist` / `for` | 变量赋值和数组循环 |
| 引入公共文件 | `include` | `{eyou:include file='header.htm' /}` |
| 全局配置 | `global` | 网站名称/版权/联系方式等 |
| 静态资源 | `static` | 引入 CSS/JS |
| 追加点击 | `arcclick` | 内容页点击量+1 |
| 收藏/取消 | `collect` / `collectnum` | 文档收藏功能 |
| 下载次数 | `downcount` | 文档下载统计 |
| 分页 | `pagelist` / `artpagelist` | 列表页分页 / 瀑布流分页 |
| 字段输出(field) | `field` | channelartlist 嵌套时输出字段值 |

---

## 变量前缀速查

变量前缀用错是 EyouCMS 模板最常见的错误。记住这个原则：

| 场景 | 格式 | 出现位置 | 示例 |
|------|------|----------|------|
| **循环体内** | `{$field.xxx}` | artlist / list / foreach / models / adv 等标签内部 | `{$field.title}` |
| **内容页（arcview 外部）** | `{$eyou.field.xxx}` | view_*.htm 模板，arcview 标签之外 | `{$eyou.field.title}` |
| **全局配置** | `{$eyou.global.xxx}` | 任何页面 | `{$eyou.global.web_title}` |
| **自定义嵌套** | `{$自定义ID.xxx}` | 内层循环指定了 `id='myid'` | 外层 `{$field.title}` + 内层 `{$myid.tag}` |
| **当前页面** | `{$eyou.xxx}` | 当前栏目名/当前文档信息 | `{$eyou.typename}` |
| **城市站点** | `{$eyou.site.xxx}` | 已开启城市分站时 | `{$eyou.site.name}` |

### 快速判断口诀

```
循环体里 $field
内容页加 eyou.
全局配置 eyou.global
内层嵌套换 ID
```

---

## 标签索引（按分类）

### 内容与文档

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/artlist.md](tags/artlist.md) | `{eyou:artlist}` | 文章/文档列表（通用） |
| [tags/list.md](tags/list.md) | `{eyou:list}` | 列表页文档列表 |
| [tags/arcview.md](tags/arcview.md) | `{eyou:arcview}` | 单条文档数据 |
| [tags/type.md](tags/type.md) | `{eyou:type}` | 指定栏目信息 |
| [tags/models.md](tags/models.md) | `{eyou:models}` | 栏目列表（导航） |
| [tags/modelsartlist.md](tags/modelsartlist.md) | `{eyou:modelsartlist}` | 频道循环 |
| [tags/beafter.md](tags/beafter.md) | `{eyou:beafter}` | 上一篇/下一篇 |
| [tags/relevarticle.md](tags/relevarticle.md) | `{eyou:relevarticle}` | 相关文档 |
| [tags/specialnode.md](tags/specialnode.md) | `{eyou:specialnode}` | 专题文档节点 |
| [tags/diyurl.md](tags/diyurl.md) | `{eyou:diyurl}` | 内链URL / 列表排序 |

### 模板基础

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/include.md](tags/include.md) | `{eyou:include}` | 引用模板文件 |
| [tags/assign.md](tags/assign.md) | `{eyou:assign}` | 模板变量赋值 |
| [tags/if.md](tags/if.md) | `{eyou:if}` | 条件判断 |
| [tags/empty.md](tags/empty.md) | `{eyou:empty}` | 变量为空判断 |
| [tags/notempty.md](tags/notempty.md) | `{eyou:notempty}` | 变量不为空判断 |
| [tags/switch.md](tags/switch.md) | `{eyou:switch}` | 简单条件判断 |
| [tags/compare.md](tags/compare.md) | `{eyou:eq}`/`{eyou:neq}`/`{eyou:gt}` 等 | 变量比较 |
| [tags/range.md](tags/range.md) | `{eyou:range}` | 范围判断 |
| [tags/foreach.md](tags/foreach.md) | `{eyou:foreach}` | 数组循环输出 |
| [tags/volist.md](tags/volist.md) | `{eyou:volist}` | 数组循环输出（增强版） |
| [tags/for.md](tags/for.md) | `{eyou:for}` | 计数循环 |
| [tags/global.md](tags/global.md) | `{eyou:global}` | 全局配置变量 |
| [tags/field.md](tags/field.md) | `{eyou:field}` | channelartlist 内字段值 |
| [tags/sql.md](tags/sql.md) | `{eyou:sql}` | 自定义SQL查询 |
| [tags/static.md](tags/static.md) | `{eyou:static}` | 静态资源引入 |
| [tags/php.md](tags/php.md) | `{eyou:php}` | 执行PHP代码 |
| [tags/functions.md](tags/functions.md) | 常用管道函数 | MyDate/text_msubstr/html_msubstr等 |

### 分页与统计

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/pagelist.md](tags/pagelist.md) | `{eyou:pagelist}` | 列表分页页码 |
| [tags/artpagelist.md](tags/artpagelist.md) | `{eyou:artpagelist}` | 瀑布流分页 |
| [tags/screening.md](tags/screening.md) | `{eyou:screening}` | 列表页文档筛选 |
| [tags/arcclick.md](tags/arcclick.md) | `{eyou:arcclick}` | 追加点击数 |
| [tags/downcount.md](tags/downcount.md) | `{eyou:downcount}` | 文档下载次数 |
| [tags/collect.md](tags/collect.md) | `{eyou:collect}` | 文档收藏/取消 |
| [tags/collectnum.md](tags/collectnum.md) | `{eyou:collectnum}` | 文档收藏数 |

### 广告与导航

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/adv.md](tags/adv.md) | `{eyou:adv}` | 广告列表 |
| [tags/ad.md](tags/ad.md) | `{eyou:ad}` | 单条广告 |
| [tags/navigation.md](tags/navigation.md) | `{eyou:navigation}` | 自定义导航菜单 |
| [tags/links.md](tags/links.md) | `{eyou:links}` | 友情链接 |
| [tags/position.md](tags/position.md) | `{eyou:position}` | 面包屑导航 |

### 搜索与Tag

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/tags.md](tags/tags.md) | `{eyou:tags}` | TAG标签调用 |
| [tags/searchform.md](tags/searchform.md) | `{eyou:searchform}` | 搜索表单 |
| [tags/hotkeywords.md](tags/hotkeywords.md) | `{eyou:hotkeywords}` | 热门搜索词 |

### 会员

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/usertag.md](tags/usertag.md) | `{eyou:user}` | 会员登录/注册/退出入口 |
| [tags/memberlist.md](tags/memberlist.md) | `{eyou:memberlist}` | 会员列表 |
| [tags/notice.md](tags/notice.md) | `{eyou:notice}` | 站内信未读数 |
| [tags/memberinfos.md](tags/memberinfos.md) | `{eyou:memberinfos}` | 文档关联的会员信息 |
| [tags/logoff.md](tags/logoff.md) | 会员注销 | 账号注销功能按钮 |

### 商城

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/sppurchase.md](tags/sppurchase.md) | `{eyou:sppurchase}` | 商品购买组件 |
| [tags/attribute.md](tags/attribute.md) | `{eyou:attribute}` | 栏目属性 / 商品参数 |
| [tags/comment.md](tags/comment.md) | `{eyou:comment}` | 商品评价列表 |
| [tags/goodslabel.md](tags/goodslabel.md) | 商品服务标签 | goodsLabel 变量循环 |
| [tags/articlepay.md](tags/articlepay.md) | `{eyou:articlepay}` | 文章付费阅读 |
| [tags/downloadpay.md](tags/downloadpay.md) | `{eyou:downloadpay}` | 下载付费 |

### 表单与留言

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/guestbookform.md](tags/guestbookform.md) | `{eyou:guestbookform}` | 栏目留言表单 |
| [tags/formtag.md](tags/formtag.md) | `{eyou:form}` | 自由表单 |
| [tags/formreply.md](tags/formreply.md) | `{eyou:formreply}` | 自由表单回复列表 |
| [tags/asklist.md](tags/asklist.md) | `{eyou:asklist}` | 问答列表 |

### 多媒体

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/videoplay.md](tags/videoplay.md) | `{eyou:videoplay}` | 视频播放器 |
| [tags/videolist.md](tags/videolist.md) | `{eyou:videolist}` | 视频选集列表 |

### 多语言与城市

| 文件 | 标签 | 说明 |
|------|------|------|
| [tags/language.md](tags/language.md) | `{eyou:language}` | 语言列表 |
| [tags/lang.md](tags/lang.md) | `{eyou:lang}` | 语言包变量 |
| [tags/lang_title.md](tags/lang_title.md) | `{$eyou.global.lang_title}` | 当前语言标识变量 |
| [tags/citysite.md](tags/citysite.md) | `{eyou:citysite}` | 城市站点列表 |
| [tags/weapp.md](tags/weapp.md) | `{eyou:weapp}` | 应用插件加载 |

---

## 标签速查表（按字母）

> 新增「常用搭配」列，列出该标签常见的协作标签。

| 标签 | 说明 | 文档 | 常用搭配 |
|------|------|------|----------|
| `{eyou:ad}` | 单条广告 | [ad.md](tags/ad.md) | — |
| `{eyou:adv}` | 广告列表 | [adv.md](tags/adv.md) | — |
| `{eyou:arcclick}` | 追加点击数 | [arcclick.md](tags/arcclick.md) | arcview |
| `{eyou:arcview}` | 单条文档数据 | [arcview.md](tags/arcview.md) | beafter, relevarticle, arcclick |
| `{eyou:articlepay}` | 文章付费阅读 | [articlepay.md](tags/articlepay.md) | arcview |
| `{eyou:artlist}` | 文章/文档列表 | [artlist.md](tags/artlist.md) | pagelist, artpagelist |
| `{eyou:artpagelist}` | 瀑布流分页 | [artpagelist.md](tags/artpagelist.md) | artlist（需 tagid） |
| `{eyou:asklist}` | 问答列表 | [asklist.md](tags/asklist.md) | — |
| `{eyou:assign}` | 模板变量赋值 | [assign.md](tags/assign.md) | foreach, volist |
| `{eyou:attribute}` | 栏目属性/商品参数 | [attribute.md](tags/attribute.md) | sppurchase（商品页） |
| `{eyou:beafter}` | 上一篇/下一篇 | [beafter.md](tags/beafter.md) | arcview |
| `{eyou:citysite}` | 城市站点列表 | [citysite.md](tags/citysite.md) | `{$eyou.site.name}` |
| `{eyou:collect}` | 文档收藏/取消 | [collect.md](tags/collect.md) | arcview, collectnum |
| `{eyou:collectnum}` | 文档收藏数 | [collectnum.md](tags/collectnum.md) | arcview, collect |
| `{eyou:comment}` | 商品评价列表 | [comment.md](tags/comment.md) | sppurchase, attribute |
| `{eyou:eq/neq}` 等 | 变量比较 | [compare.md](tags/compare.md) | if |
| `{eyou:diyurl}` | 内链URL / 排序 | [diyurl.md](tags/diyurl.md) | — |
| `{eyou:downcount}` | 下载次数 | [downcount.md](tags/downcount.md) | arcview |
| `{eyou:downloadpay}` | 下载付费 | [downloadpay.md](tags/downloadpay.md) | arcview |
| `{eyou:empty}` | 变量为空判断 | [empty.md](tags/empty.md) | if, notempty |
| `{eyou:field}` | channelartlist 内字段值 | [field.md](tags/field.md) | modelsartlist |
| `{eyou:for}` | 计数循环 | [for.md](tags/for.md) | — |
| `{eyou:foreach}` | 数组循环 | [foreach.md](tags/foreach.md) | assign |
| `{eyou:form}` | 自由表单 | [formtag.md](tags/formtag.md) | formreply |
| `{eyou:formreply}` | 表单回复列表 | [formreply.md](tags/formreply.md) | form |
| `{eyou:global}` | 全局配置变量 | [global.md](tags/global.md) | 任何模板 |
| `{eyou:guestbookform}` | 栏目留言表单 | [guestbookform.md](tags/guestbookform.md) | — |
| `{eyou:hotkeywords}` | 热门搜索词 | [hotkeywords.md](tags/hotkeywords.md) | searchform |
| `{eyou:if}` | 条件判断 | [if.md](tags/if.md) | empty, notempty, switch, compare |
| `{eyou:include}` | 引用模板文件 | [include.md](tags/include.md) | 公共模板拆分 |
| `{eyou:lang}` | 语言包变量 | [lang.md](tags/lang.md) | language |
| `{eyou:language}` | 语言列表 | [language.md](tags/language.md) | lang |
| `{eyou:links}` | 友情链接 | [links.md](tags/links.md) | — |
| `{eyou:list}` | 列表页文档列表 | [list.md](tags/list.md) | pagelist, screening |
| `{eyou:memberinfos}` | 文档关联会员信息 | [memberinfos.md](tags/memberinfos.md) | arcview |
| `{eyou:memberlist}` | 会员列表 | [memberlist.md](tags/memberlist.md) | — |
| `{eyou:models}` | 栏目列表（导航） | [models.md](tags/models.md) | modelsartlist |
| `{eyou:modelsartlist}` | 频道循环 | [modelsartlist.md](tags/modelsartlist.md) | models |
| `{eyou:navigation}` | 自定义导航菜单 | [navigation.md](tags/navigation.md) | — |
| `{eyou:notempty}` | 变量不为空判断 | [notempty.md](tags/notempty.md) | if, empty |
| `{eyou:notice}` | 站内信未读数 | [notice.md](tags/notice.md) | user |
| `{eyou:pagelist}` | 列表分页页码 | [pagelist.md](tags/pagelist.md) | list |
| `{eyou:php}` | 执行PHP代码 | [php.md](tags/php.md) | — |
| `{eyou:position}` | 面包屑导航 | [position.md](tags/position.md) | — |
| `{eyou:range}` | 范围判断 | [range.md](tags/range.md) | if |
| `{eyou:relevarticle}` | 相关文档 | [relevarticle.md](tags/relevarticle.md) | arcview |
| `{eyou:screening}` | 列表页文档筛选 | [screening.md](tags/screening.md) | list, pagelist |
| `{eyou:searchform}` | 搜索表单 | [searchform.md](tags/searchform.md) | hotkeywords |
| `{eyou:specialnode}` | 专题文档节点 | [specialnode.md](tags/specialnode.md) | — |
| `{eyou:sppurchase}` | 商品购买组件 | [sppurchase.md](tags/sppurchase.md) | attribute, comment |
| `{eyou:sql}` | 自定义SQL查询 | [sql.md](tags/sql.md) | — |
| `{eyou:static}` | 静态资源引入 | [static.md](tags/static.md) | — |
| `{eyou:switch}` | 简单条件判断 | [switch.md](tags/switch.md) | if |
| `{eyou:tags}` | TAG标签调用 | [tags.md](tags/tags.md) | artlist |
| `{eyou:type}` | 指定栏目信息 | [type.md](tags/type.md) | — |
| `{eyou:user}` | 会员入口 | [usertag.md](tags/usertag.md) | notice |
| `{eyou:videolist}` | 视频选集列表 | [videolist.md](tags/videolist.md) | videoplay |
| `{eyou:videoplay}` | 视频播放器 | [videoplay.md](tags/videoplay.md) | videolist |
| `{eyou:volist}` | 数组循环（增强） | [volist.md](tags/volist.md) | assign |
| `{eyou:weapp}` | 应用插件加载 | [weapp.md](tags/weapp.md) | — |
| 会员注销 | 账号注销功能 | [logoff.md](tags/logoff.md) | user |
| 商品服务标签 | goodsLabel 变量循环 | [goodslabel.md](tags/goodslabel.md) | sppurchase |
| 常用函数 | 管道函数 | [functions.md](tags/functions.md) | MyDate, text_msubstr 等 |

---

## 数据字典索引

| 文件 | 表名 | 说明 | 字段数 |
|------|------|------|:------:|
| [dict/ey_archives.md](dict/ey_archives.md) | `ey_archives` | 文档主表 | 71 |
| [dict/ey_arctype.md](dict/ey_arctype.md) | `ey_arctype` | 文档栏目表 | 42 |
| [dict/ey_article_content.md](dict/ey_article_content.md) | `ey_article_content` | 文章附加表 | 9 |
| [dict/ey_channelfield.md](dict/ey_channelfield.md) | `ey_channelfield` | 自定义字段表 | 24 |
| [dict/ey_ad.md](dict/ey_ad.md) | `ey_ad` | 广告表 | 26 |
| [dict/ey_nav_list.md](dict/ey_nav_list.md) | `ey_nav_list` | 导航列表 | 22 |
| [dict/ey_links.md](dict/ey_links.md) | `ey_links` | 友情链接表 | 21 |
| [dict/ey_search_word.md](dict/ey_search_word.md) | `ey_search_word` | 搜索词统计表 | 14 |
| [dict/ey_tagindex.md](dict/ey_tagindex.md) | `ey_tagindex` | 标签索引表 | 24 |
| [dict/ey_users.md](dict/ey_users.md) | `ey_users` | 会员信息表 | 47 |
| [dict/ey_users_level.md](dict/ey_users_level.md) | `ey_users_level` | 会员级别表 | 19 |
| [dict/ey_form.md](dict/ey_form.md) | `ey_form` | 表单管理表 | 12 |
| [dict/ey_guestbook.md](dict/ey_guestbook.md) | `ey_guestbook` | 留言主表 | 19 |
| [dict/ey_guestbook_attr.md](dict/ey_guestbook_attr.md) | `ey_guestbook_attr` | 留言表单属性值 | 12 |
| [dict/ey_guestbook_attribute.md](dict/ey_guestbook_attribute.md) | `ey_guestbook_attribute` | 留言表单属性 | 18 |
| [dict/ey_media_file.md](dict/ey_media_file.md) | `ey_media_file` | 视频附件表 | 21 |
| [dict/ey_language.md](dict/ey_language.md) | `ey_language` | 多语言主表 | 14 |
| [dict/ey_language_pack.md](dict/ey_language_pack.md) | `ey_language_pack` | 模板语言包变量 | 10 |
