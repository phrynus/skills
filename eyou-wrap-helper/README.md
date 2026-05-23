# EyouCMS 套标签助手

扒站后把静态 HTML 套上 EyouCMS 标签的工具和速查。

## 包含什么

| 文件 | 用途 |
|------|------|
| `basic-tags.md` | 基础标签速查（只含常用标签，不花哨） |
| `wrap.py` | 命令行辅助脚本 |

## 快速上手

```
python wrap.py init index.html              # 从首页提取 header/nav/footer
python wrap.py scan about.html              # 扫描硬编码内容
python wrap.py rename ./templates           # 批量重命名文件
```

## 工作流程

```
原始 HTML  →  python wrap.py init  →  header.htm / nav.htm / footer.htm
                  wrap.py rename   →  index.htm / lists_article.htm / view_product.htm
                  手动套标签        →  用 basic-tags.md 替换硬编码内容
```

## 基础标签一览

| 替换什么 | 用什么标签 |
|---------|-----------|
| 网站标题/关键词/描述 | `{eyou:global name='web_title' /}` |
| 导航链接 | `{eyou:models type='top'}` + `{$field.typeurl}` |
| 文章/产品列表 | `{eyou:artlist}` / `{eyou:list}` |
| 内容页标题/正文 | `{$eyou.field.title}` / `{$eyou.field.content}` |
| 缩略图 | `{$field.litpic}` |
| 分页 | `{eyou:pagelist}` |
| 面包屑 | `{eyou:position style='crumb' /}` |
| 上下篇 | `{eyou:beafter}` |
| 版权 | `{eyou:global name='web_copyright' /}` |
| 搜索表单 | `{eyou:searchform}` |

> 完整标签参考见 [basic-tags.md](basic-tags.md)，详细标签文档见 `../eyou-tag-assistant/`。
