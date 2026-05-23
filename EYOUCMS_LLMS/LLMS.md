# EyouCMS 模板标签 LLM 手册

> **用途**：供 AI 辅助 EyouCMS 模板开发，涵盖所有模板标签用法与数据字典。
>
> **维护说明**：编辑标签 → 修改 `tags/xx.md`（每个标签对应一个独立文件）；更新表结构 → 修改 `dict/xx.md`。
>
> ⚠️ **常见问题**：[问题记录.md](问题记录.md)

---

## 如何使用本手册

1. **查找标签** → 查看下方「标签速查表」定位标签名，点击链接跳转到对应文档
2. **查找字段** → 查看「数据字典索引」找到对应数据表，字段详情在 `dict/` 目录
3. **跨文件关联** → 每个 `tags/xx.md` 文件顶部列出了涉及的数据表链接

---

## 标签文档索引

> 每个标签均有独立文件。

### 内容与文档标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/artlist.md](tags/artlist.md) | `{eyou:artlist}` | 文章/文档列表（通用） |
| [tags/models.md](tags/models.md) | `{eyou:models}` | 栏目列表（导航） |
| [tags/modelsartlist.md](tags/modelsartlist.md) | `{eyou:modelsartlist}` | 频道循环 |
| [tags/type.md](tags/type.md) | `{eyou:type}` | 指定栏目信息 |
| [tags/arcview.md](tags/arcview.md) | `{eyou:arcview}` | 单条文档数据 |
| [tags/list.md](tags/list.md) | `{eyou:list}` | 列表页文档列表 |
| [tags/attribute.md](tags/attribute.md) | `{eyou:attribute}` | 栏目属性 / 商品参数 |
| [tags/beafter.md](tags/beafter.md) | `{eyou:beafter}` | 上一篇/下一篇 |
| [tags/relevarticle.md](tags/relevarticle.md) | `{eyou:relevarticle}` | 相关文档 |
| [tags/specialnode.md](tags/specialnode.md) | `{eyou:specialnode}` | 专题文档节点 |
| [tags/diyurl.md](tags/diyurl.md) | `{eyou:diyurl}` | 内链URL / 列表排序 |

### 模板基础标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/include.md](tags/include.md) | `{eyou:include}` | 引用模板文件 |
| [tags/assign.md](tags/assign.md) | `{eyou:assign}` | 模板变量赋值 |
| [tags/empty.md](tags/empty.md) | `{eyou:empty}` | 变量为空判断 |
| [tags/notempty.md](tags/notempty.md) | `{eyou:notempty}` | 变量不为空判断 |
| [tags/if.md](tags/if.md) | `{eyou:if}` | 条件判断 |
| [tags/switch.md](tags/switch.md) | `{eyou:switch}` | 简单条件判断 |
| [tags/compare.md](tags/compare.md) | `{eyou:eq}` / `{eyou:neq}` / `{eyou:gt}` 等 | 变量比较 |
| [tags/range.md](tags/range.md) | `{eyou:range}` | 范围判断 |
| [tags/foreach.md](tags/foreach.md) | `{eyou:foreach}` | 数组循环输出 |
| [tags/volist.md](tags/volist.md) | `{eyou:volist}` | 数组循环输出（增强版） |
| [tags/for.md](tags/for.md) | `{eyou:for}` | 计数循环 |
| [tags/global.md](tags/global.md) | `{eyou:global}` | 全局配置变量 |
| [tags/field.md](tags/field.md) | `{eyou:field}` | channelartlist 内字段值 |
| [tags/sql.md](tags/sql.md) | `{eyou:sql}` | 自定义SQL查询 |
| [tags/static.md](tags/static.md) | `{eyou:static}` | 静态资源引入 |
| [tags/php.md](tags/php.md) | `{eyou:php}` | 执行PHP代码 |
| [tags/functions.md](tags/functions.md) | 常用函数 | 管道函数：MyDate/text_msubstr/html_msubstr等 |

### 分页与统计标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/pagelist.md](tags/pagelist.md) | `{eyou:pagelist}` | 列表分页页码 |
| [tags/artpagelist.md](tags/artpagelist.md) | `{eyou:artpagelist}` | 瀑布流分页 |
| [tags/screening.md](tags/screening.md) | `{eyou:screening}` | 列表页文档筛选 |
| [tags/arcclick.md](tags/arcclick.md) | `{eyou:arcclick}` | 追加点击数 |
| [tags/downcount.md](tags/downcount.md) | `{eyou:downcount}` | 文档下载次数 |
| [tags/collect.md](tags/collect.md) | `{eyou:collect}` | 文档收藏/取消 |
| [tags/collectnum.md](tags/collectnum.md) | `{eyou:collectnum}` | 文档收藏数 |

### 广告与导航标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/adv.md](tags/adv.md) | `{eyou:adv}` | 广告列表 |
| [tags/ad.md](tags/ad.md) | `{eyou:ad}` | 单条广告 |
| [tags/navigation.md](tags/navigation.md) | `{eyou:navigation}` | 导航菜单 |
| [tags/links.md](tags/links.md) | `{eyou:links}` | 友情链接 |
| [tags/position.md](tags/position.md) | `{eyou:position}` | 面包屑导航 |

### 搜索与Tag标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/tags.md](tags/tags.md) | `{eyou:tags}` | TAG标签调用 |
| [tags/searchform.md](tags/searchform.md) | `{eyou:searchform}` | 搜索表单 |
| [tags/hotkeywords.md](tags/hotkeywords.md) | `{eyou:hotkeywords}` | 热门搜索词 |

### 会员标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/usertag.md](tags/usertag.md) | `{eyou:user}` | 会员登录/注册/退出入口 |
| [tags/memberlist.md](tags/memberlist.md) | `{eyou:memberlist}` | 会员列表 |
| [tags/notice.md](tags/notice.md) | `{eyou:notice}` | 站内信未读数 |
| [tags/memberinfos.md](tags/memberinfos.md) | `{eyou:memberinfos}` | 文档关联的会员信息 |
| [tags/logoff.md](tags/logoff.md) | 会员注销 | 账号注销功能按钮 |

### 商城标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/attribute.md](tags/attribute.md) | `{eyou:attribute type='newattr'}` | 商品参数（与内容标签共用） |
| [tags/comment.md](tags/comment.md) | `{eyou:comment}` | 商品评价列表 |
| [tags/articlepay.md](tags/articlepay.md) | `{eyou:articlepay}` | 文章付费阅读 |
| [tags/downloadpay.md](tags/downloadpay.md) | `{eyou:downloadpay}` | 下载付费 |
| [tags/sppurchase.md](tags/sppurchase.md) | `{eyou:sppurchase}` | 商品购买组件 |
| [tags/goodslabel.md](tags/goodslabel.md) | 商品服务标签 | goodsLabel 变量循环 |

### 表单与留言标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/guestbookform.md](tags/guestbookform.md) | `{eyou:guestbookform}` | 栏目留言表单 |
| [tags/formtag.md](tags/formtag.md) | `{eyou:form}` | 自由表单 |
| [tags/formreply.md](tags/formreply.md) | `{eyou:formreply}` | 自由表单回复列表 |
| [tags/asklist.md](tags/asklist.md) | `{eyou:asklist}` | 问答列表 |

### 多媒体标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/videoplay.md](tags/videoplay.md) | `{eyou:videoplay}` | 视频播放器 |
| [tags/videolist.md](tags/videolist.md) | `{eyou:videolist}` | 视频选集列表 |

### 多语言标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/language.md](tags/language.md) | `{eyou:language}` | 语言列表 |
| [tags/lang.md](tags/lang.md) | `{eyou:lang}` | 语言包变量 |
| [tags/lang_title.md](tags/lang_title.md) | `{$eyou.global.lang_title}` 等 | 当前语言标识变量 |

### 城市站点与应用标签

| 独立文件 | 标签名 | 说明 |
|---------|--------|------|
| [tags/citysite.md](tags/citysite.md) | `{eyou:citysite}` | 城市站点列表 |
| [tags/weapp.md](tags/weapp.md) | `{eyou:weapp}` | 应用插件加载 |

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

---

## 标签速查表

> 按字母排序，每个标签直接链接到独立文档文件。

| 标签名 | 说明 | 独立文档 |
|--------|------|---------|
| `{eyou:ad}` | 单条广告 | [ad.md](tags/ad.md) |
| `{eyou:adv}` | 广告列表 | [adv.md](tags/adv.md) |
| `{eyou:arcclick}` | 追加点击数（内容页） | [arcclick.md](tags/arcclick.md) |
| `{eyou:arcview}` | 单条文档数据 | [arcview.md](tags/arcview.md) |
| `{eyou:articlepay}` | 文章付费阅读 | [articlepay.md](tags/articlepay.md) |
| `{eyou:artlist}` | 文章/文档列表（通用） | [artlist.md](tags/artlist.md) |
| `{eyou:artpagelist}` | 瀑布流分页 | [artpagelist.md](tags/artpagelist.md) |
| `{eyou:asklist}` | 问答列表 | [asklist.md](tags/asklist.md) |
| `{eyou:assign}` | 模板变量赋值 | [assign.md](tags/assign.md) |
| `{eyou:attribute}` | 栏目属性 / 商品参数 | [attribute.md](tags/attribute.md) |
| `{eyou:beafter}` | 上一篇/下一篇 | [beafter.md](tags/beafter.md) |
| `{eyou:citysite}` | 城市站点列表 | [citysite.md](tags/citysite.md) |
| `{eyou:collect}` | 文档收藏/取消 | [collect.md](tags/collect.md) |
| `{eyou:collectnum}` | 文档收藏数 | [collectnum.md](tags/collectnum.md) |
| `{eyou:comment}` | 商品评价列表 | [comment.md](tags/comment.md) |
| `{eyou:eq}` / `{eyou:neq}` 等 | 变量比较（eq/neq/gt/egt/lt/elt/heq/nheq） | [compare.md](tags/compare.md) |
| `{eyou:diyurl}` | 内链URL / 列表排序 | [diyurl.md](tags/diyurl.md) |
| `{eyou:downcount}` | 文档下载次数 | [downcount.md](tags/downcount.md) |
| `{eyou:downloadpay}` | 下载付费 | [downloadpay.md](tags/downloadpay.md) |
| `{eyou:empty}` | 变量为空判断 | [empty.md](tags/empty.md) |
| `{eyou:field}` | channelartlist 内字段值 | [field.md](tags/field.md) |
| `{eyou:for}` | 计数循环 | [for.md](tags/for.md) |
| `{eyou:foreach}` | 数组循环输出 | [foreach.md](tags/foreach.md) |
| `{eyou:form}` | 自由表单 | [formtag.md](tags/formtag.md) |
| `{eyou:formreply}` | 自由表单回复列表 | [formreply.md](tags/formreply.md) |
| `{eyou:global}` | 全局配置变量 | [global.md](tags/global.md) |
| `{eyou:guestbookform}` | 栏目留言表单 | [guestbookform.md](tags/guestbookform.md) |
| `{eyou:hotkeywords}` | 热门搜索词 | [hotkeywords.md](tags/hotkeywords.md) |
| `{eyou:if}` | 条件判断 | [if.md](tags/if.md) |
| `{eyou:include}` | 引用模板文件 | [include.md](tags/include.md) |
| `{eyou:lang}` | 语言包变量 | [lang.md](tags/lang.md) |
| `{$eyou.global.lang_title}` 等 | 当前语言标识变量 | [lang_title.md](tags/lang_title.md) |
| `{eyou:language}` | 语言列表 | [language.md](tags/language.md) |
| `{eyou:links}` | 友情链接 | [links.md](tags/links.md) |
| `{eyou:list}` | 列表页文档列表 | [list.md](tags/list.md) |
| `{eyou:memberinfos}` | 文档关联的会员信息 | [memberinfos.md](tags/memberinfos.md) |
| `{eyou:memberlist}` | 会员列表 | [memberlist.md](tags/memberlist.md) |
| `{eyou:models}` | 栏目列表（导航） | [models.md](tags/models.md) |
| `{eyou:modelsartlist}` | 频道循环 | [modelsartlist.md](tags/modelsartlist.md) |
| `{eyou:navigation}` | 导航菜单 | [navigation.md](tags/navigation.md) |
| `{eyou:notempty}` | 变量不为空判断 | [notempty.md](tags/notempty.md) |
| `{eyou:notice}` | 站内信未读数 | [notice.md](tags/notice.md) |
| `{eyou:pagelist}` | 列表分页页码 | [pagelist.md](tags/pagelist.md) |
| `{eyou:php}` | 执行PHP代码 | [php.md](tags/php.md) |
| `{eyou:position}` | 面包屑导航 | [position.md](tags/position.md) |
| `{eyou:range}` | 范围判断（in/between等） | [range.md](tags/range.md) |
| `{eyou:relevarticle}` | 相关文档 | [relevarticle.md](tags/relevarticle.md) |
| `{eyou:screening}` | 列表页文档筛选 | [screening.md](tags/screening.md) |
| `{eyou:searchform}` | 搜索表单 | [searchform.md](tags/searchform.md) |
| `{eyou:specialnode}` | 专题文档节点 | [specialnode.md](tags/specialnode.md) |
| `{eyou:sppurchase}` | 商品购买组件 | [sppurchase.md](tags/sppurchase.md) |
| `{eyou:sql}` | 自定义SQL查询 | [sql.md](tags/sql.md) |
| `{eyou:static}` | 静态资源引入 | [static.md](tags/static.md) |
| `{eyou:switch}` | 简单条件判断 | [switch.md](tags/switch.md) |
| `{eyou:tags}` | TAG标签调用 | [tags.md](tags/tags.md) |
| `{eyou:type}` | 指定栏目信息 | [type.md](tags/type.md) |
| `{eyou:user}` | 会员登录/注册/退出入口 | [usertag.md](tags/usertag.md) |
| `{eyou:videolist}` | 视频选集列表 | [videolist.md](tags/videolist.md) |
| `{eyou:videoplay}` | 视频播放器 | [videoplay.md](tags/videoplay.md) |
| `{eyou:volist}` | 数组循环输出（增强版） | [volist.md](tags/volist.md) |
| `{eyou:weapp}` | 应用插件加载 | [weapp.md](tags/weapp.md) |
| 会员注销 | 账号注销功能 | [logoff.md](tags/logoff.md) |
| 商品服务标签 | goodsLabel 变量循环 | [goodslabel.md](tags/goodslabel.md) |
| 常用函数 | MyDate/text_msubstr/html_msubstr等管道函数 | [functions.md](tags/functions.md) |

---

## 常用场景速查

| 场景 | 需要的标签 |
|------|-----------|
| 首页文章列表 | `artlist` |
| 列表页文档列表 + 分页 | `list` + `pagelist` |
| 首页导航 | `models` 或 `navigation` |
| 内容页上下篇 | `beafter` |
| 内容页相关文档 | `relevarticle` |
| 搜索功能 | `searchform` + `hotkeywords` |
| 广告位 | `adv`（列表）/ `ad`（单条） |
| 面包屑 | `position` |
| 会员登录注册区域 | `user type='userinfo'` |
| 商品详情页 | `sppurchase` + `attribute type='newattr'` + `comment` |
| 文章付费 | `articlepay` |
| 多语言切换 | `language` + `lang` |
| 城市分站 | `citysite` + `{$eyou.site.name}` |
| 留言表单 | `guestbookform` 或 `form` |
| 视频播放+选集 | `videoplay` + `videolist` |
| 全局网站配置 | `global` |
| 自定义SQL | `SQL` |
