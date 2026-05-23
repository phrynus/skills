# `{eyou:global}` — 全局变量

> **用途**：获取网站后台基本设置中的全局配置变量。
> **官方文档**：https://www.eyoucms.com/doc/label/all/513.html

---

## 语法

```html
{eyou:global name='web_title' /}
<!-- 或直接使用变量 -->
{$eyou.global.web_title}

<!-- 截取描述50字 -->
{$eyou.global.web_description|html_msubstr=###,0,50}
```

## 常用变量名

| 变量名 | 说明 |
|--------|------|
| `web_name` | 网站名称 |
| `web_title` | 网站标题 |
| `web_keywords` | 网站关键词 |
| `web_description` | 网站描述 |
| `web_logo` | 网站LOGO |
| `web_basehost` | 网站网址 |
| `web_copyright` | 版权信息 |
| `web_templeturl` | 模板根目录网址 |
| `web_cmsurl` | 程序安装根目录网址 |
| `web_attr_*` | 自定义变量（后台设置） |
