#!/usr/bin/env python3
"""
EyouCMS 套标签助手 — 扒站后快速转为 EyouCMS 模板

用法:
  python wrap.py init  <html文件>      从 HTML 提取 header/nav/footer 模板
  python wrap.py scan <html文件或目录>  扫描硬编码内容，推荐替换的标签
  python wrap.py rename <目录>         批量重命名文件为 EyouCMS 规范命名
  python wrap.py clean <html文件>      清理广告弹窗等干扰代码

示例:
  python wrap.py init index.html
  python wrap.py scan ./templates/
  python wrap.py rename ./templates/
  python wrap.py clean list.html
"""

import argparse
import re
from pathlib import Path


# ── 1. 初始化模板结构 ─────────────────────────────────────────────

def cmd_init(html_path: str):
    """从 HTML 文件提取 header/nav/footer 模板结构"""
    filepath = Path(html_path)
    if not filepath.exists():
        print(f"[ERROR] 文件不存在: {html_path}")
        return

    html = filepath.read_text(encoding='utf-8')

    out_dir = filepath.parent / 'eyou_templates'
    out_dir.mkdir(exist_ok=True)

    print(f"\n[处理] {filepath.name}")
    print(f"[输出] {out_dir}/\n")

    # 提取 header
    header = _extract_header(html)
    if header:
        (out_dir / 'header.htm').write_text(header, encoding='utf-8')
        print(f"  [OK] 已生成 header.htm ({len(header)} 字符)")
    else:
        print(f"  [WARN] 未找到 <head> 区域，header.htm 跳过")

    # 提取导航
    nav = _extract_nav(html)
    if nav:
        (out_dir / 'nav.htm').write_text(nav, encoding='utf-8')
        print(f"  [OK] 已生成 nav.htm ({len(nav)} 字符)")
    else:
        print(f"  [WARN] 未找到导航区域，nav.htm 跳过")
        print(f"    提示：wrap.py 只匹配 <nav> / .nav / #nav / .menu 元素")
        print(f"    你也可以手动从 HTML 复制导航部分到 nav.htm")

    # 提取 footer
    footer = _extract_footer(html)
    if footer:
        (out_dir / 'footer.htm').write_text(footer, encoding='utf-8')
        print(f"  [OK] 已生成 footer.htm ({len(footer)} 字符)")
    else:
        print(f"  [WARN] 未找到页脚区域，footer.htm 跳过")

    # 生成 nav.htm 的标签替换提示
    nav_path = out_dir / 'nav.htm'
    if nav_path.exists():
        print(f"\n[提示] nav.htm 标签替换：")
        print(f"   将导航链接替换为 EyouCMS 标签:")
        print(f"   <ul class=\"nav\">")
        print(f"     {{eyou:models type='top' loop='10' currentclass='active' id='field'}}")
        print(f"     <li><a href=\"{{$field.typeurl}}\" class=\"{{$field.currentclass}}\">{{$field.typename}}</a></li>")
        print(f"     {{/eyou:models}}")
        print(f"   </ul>")

    print(f"\n[下一步]")
    print(f"  1. 编辑 header.htm，把 title/keywords/description 替换为 EyouCMS 全局标签")
    print(f"  2. 编辑 nav.htm，按上面的提示替换导航标签")
    print(f"  3. 编辑 footer.htm，替换版权为 EyouCMS 标签")
    print(f"  4. 在其他页面顶部加上 include 引用 header / nav / footer")


def _extract_header(html: str) -> str:
    """提取 <head> 中的 meta/title"""
    match = re.search(r'<head[^>]*>(.*?)</head>', html, re.DOTALL | re.IGNORECASE)
    if not match:
        return ''

    head_content = match.group(1)

    parts = []
    for tag in ['title', 'meta']:
        pattern = rf'<{tag}[^>]*>.*?</{tag}>' if tag == 'title' else rf'<{tag}[^>]*/?>'
        for m in re.finditer(pattern, head_content, re.DOTALL | re.IGNORECASE):
            parts.append(m.group(0))

    if not parts:
        return ''

    result = '<meta charset="utf-8">\n'
    for p in parts:
        result += p + '\n'
    result += '<!-- CSS/JS 放在各自页面，不提取到 header -->\n'
    return result.strip()


def _extract_nav(html: str) -> str:
    """尝试提取导航区域"""
    patterns = [
        r'<nav[^>]*>.*?</nav>',
        r'<div[^>]*class=["\'][^"\']*\bnav\b[^"\']*["\'][^>]*>.*?</div>',
        r'<div[^>]*class=["\'][^"\']*\bmenu\b[^"\']*["\'][^>]*>.*?</div>',
        r'<ul[^>]*class=["\'][^"\']*\bnav\b[^"\']*["\'][^>]*>.*?</ul>',
        r'<div[^>]*id=["\'][^"\']*\bnav\b[^"\']*["\'][^>]*>.*?</div>',
    ]
    for pat in patterns:
        match = re.search(pat, html, re.DOTALL | re.IGNORECASE)
        if match:
            nav_html = match.group(0)
            nav_html = re.sub(
                r'href=["\']/[^"\']*["\']',
                'href="{$field.typeurl}"',
                nav_html
            )
            return nav_html
    return ''


def _extract_footer(html: str) -> str:
    """尝试提取页脚区域"""
    patterns = [
        r'<footer[^>]*>.*?</footer>',
        r'<div[^>]*class=["\'][^"\']*\bfooter\b[^"\']*["\'][^>]*>.*?</div>',
        r'<div[^>]*id=["\'][^"\']*\bfooter\b[^"\']*["\'][^>]*>.*?</div>',
    ]
    for pat in patterns:
        match = re.search(pat, html, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(0)
    return ''


# ── 2. 扫描硬编码内容 ─────────────────────────────────────────────

SCAN_RULES = [
    (r'<title>(.*?)</title>',
     '{eyou:global name=\'web_title\' /}', '网站标题'),
    (r'web_keywords', None, '已有 keywords 标签'),
    (r'web_description', None, '已有 description 标签'),
    (r'[©®]\s*\d{4}\s+[^<]+',
     '{eyou:global name=\'web_copyright\' /}', '版权信息'),
    (r'ICP备[^<]+号',
     '{eyou:global name=\'web_recordnum\' /}', '备案号'),
    (r'href=["\']/[a-zA-Z][^"\']*["\']',
     '{eyou:models} / {$field.typeurl}', '导航/内部链接'),
    (r'class=["\'][^"\']*pag[ei][^"\']*["\']',
     '{eyou:pagelist}', '分页区域'),
    (r'class=["\'][^"\']*crumb[^"\']*["\']',
     '{eyou:position style=\'crumb\' /}', '面包屑'),
    (r'上一篇|下一篇',
     '{eyou:beafter}', '上下篇'),
    (r'class=["\'][^"\']*search[^"\']*["\']',
     '{eyou:searchform}', '搜索表单'),
    (r'class=["\'][^"\']*link[s]?["\'][^>]*>',
     '{eyou:links}', '友链区域'),
    (r'class=["\'][^"\']*banner[^"\']*["\']',
     '{eyou:adv}', '广告轮播'),
    (r'<img[^>]*src=["\']/uploads/',
     '{$field.litpic}', '上传目录图片'),
]


def cmd_scan(path: str):
    """扫描 HTML 文件中的硬编码内容"""
    p = Path(path)
    if p.is_dir():
        files = list(p.glob('**/*.htm')) + list(p.glob('**/*.html'))
    elif p.is_file():
        files = [p]
    else:
        print(f"[ERROR] 路径不存在: {path}")
        return

    if not files:
        print("[WARN] 未找到任何 .htm/.html 文件")
        return

    for f in files:
        print(f"\n{'='*60}")
        print(f"[文件] {f.name}")
        print(f"{'='*60}")
        html = f.read_text(encoding='utf-8')
        found = False

        for pattern, suggestion, desc in SCAN_RULES:
            matches = re.findall(pattern, html, re.IGNORECASE | re.DOTALL)
            if matches:
                found = True
                if suggestion:
                    match_text = matches[0]
                    if isinstance(match_text, str):
                        excerpt = match_text[:80]
                    else:
                        excerpt = match_text[0][:80]
                    print(f"\n  [发现] {desc}")
                    print(f"    原文: {excerpt}")
                    print(f"    替换: {suggestion}")
                else:
                    print(f"  [OK] {desc} -- 已替换")

        if not found:
            print(f"  [OK] 未检测到明显的硬编码内容")


# ── 3. 文件重命名 ─────────────────────────────────────────────

FILE_RULES = [
    (r'.*index.*\.html?$',      'index.htm'),
    (r'.*about.*\.html?$',      'lists_single.htm'),
    (r'.*contact.*\.html?$',    'lists_single.htm'),
    (r'.*single.*\.html?$',     'lists_single.htm'),
    (r'.*news.*\.html?$',       'lists_article.htm'),
    (r'.*article.*\.html?$',    'lists_article.htm'),
    (r'.*product.*\.html?$',    'lists_product.htm'),
    (r'.*pro.*\.html?$',        'lists_product.htm'),
    (r'.*image.*\.html?$',      'lists_image.htm'),
    (r'.*photo.*\.html?$',      'lists_image.htm'),
    (r'.*download.*\.html?$',   'lists_download.htm'),
    (r'.*video.*\.html?$',      'lists_video.htm'),
    (r'.*search.*\.html?$',     'lists_search.htm'),
    (r'.*view.*article.*\.html?$', 'view_article.htm'),
    (r'.*view.*product.*\.html?$', 'view_product.htm'),
    (r'.*detail.*\.html?$',     'view_product.htm'),
    (r'.*view.*image.*\.html?$', 'view_image.htm'),
    (r'.*view.*download.*\.html?$', 'view_download.htm'),
    (r'.*view.*video.*\.html?$', 'view_video.htm'),
]


def cmd_rename(dir_path: str):
    """批量重命名 HTML 文件为 EyouCMS 模板命名规范"""
    p = Path(dir_path)
    if not p.is_dir():
        print(f"[ERROR] 目录不存在: {dir_path}")
        return

    html_files = list(p.glob('*.html')) + list(p.glob('*.htm'))
    if not html_files:
        print(f"[WARN] 目录中没有 .html/.htm 文件: {dir_path}")
        return

    renamed = []
    skipped = []

    for f in html_files:
        name_lower = f.name.lower()
        target = None
        for pattern, replacement in FILE_RULES:
            if re.match(pattern, name_lower):
                target = replacement
                break

        if target:
            if f.name == target:
                skipped.append((f.name, '命名已规范'))
                continue
            new_path = f.parent / target
            if new_path.exists():
                skipped.append((f.name, f'{target} 已存在'))
                continue
            f.rename(new_path)
            renamed.append((f.name, target))
        else:
            skipped.append((f.name, '无法匹配已知页面类型'))

    if renamed:
        print(f"\n[OK] 已重命名 {len(renamed)} 个文件：")
        for old, new in renamed:
            print(f"   {old} -> {new}")

    if skipped:
        print(f"\n[跳过] {len(skipped)} 个：")
        for name, reason in skipped:
            print(f"   {name} ({reason})")

    if not renamed and not skipped:
        print("[WARN] 未找到任何 HTML 文件")


# ── 4. 清理干扰代码 ─────────────────────────────────────────────

CLEAN_PATTERNS = [
    (r'<div[^>]*class=["\'][^"\']*popup[^"\']*["\'][^>]*>.*?</div>',
     '<!-- popup cleaned -->'),
    (r'<div[^>]*class=["\'][^"\']*modal[^"\']*["\'][^>]*>.*?</div>',
     '<!-- modal cleaned -->'),
    (r'<div[^>]*class=["\'][^"\']*overlay[^"\']*["\'][^>]*>.*?</div>',
     '<!-- overlay cleaned -->'),
    (r'<div[^>]*class=["\'][^"\']*float[^"\']*["\'][^>]*>.*?</div>',
     '<!-- float cleaned -->'),
    (r'<div[^>]*class=["\'][^"\']*fixed[^"\']*["\'][^>]*>.*?</div>',
     '<!-- fixed cleaned -->'),
    (r'<script[^>]*>.*?(?:var\s+_hmt|var\s+_ga|gtag\(|baidu|cnzz|tongji).*?</script>', ''),
    (r'<a[^>]*href=["\']http://www\.cnzz\.com[^>]*>.*?</a>', ''),
    (r'<script[^>]*>.*?(?:kf|KF|livechat|chatbot).*?</script>', ''),
    (r'<div\s+class=["\'][^"\']*clear[^"\']*["\']\s*></div>', ''),
    (r'<div\s+class=["\']clearfix["\']\s*></div>', ''),
    (r'<div\s+style=["\']clear:\s*both["\']\s*></div>', ''),
    (r'<script[^>]*>.*?(?:alert\(|confirm\(|prompt\().*?</script>', ''),
    (r'onclick=["\'](?:alert|confirm|prompt)\([^)]*\)["\']', ''),
]


def cmd_clean(html_path: str):
    """清理广告、弹窗、统计代码等"""
    filepath = Path(html_path)
    if not filepath.exists():
        print(f"[ERROR] 文件不存在: {html_path}")
        return

    html = filepath.read_text(encoding='utf-8')
    original_len = len(html)
    clean_count = 0

    for pattern, replacement in CLEAN_PATTERNS:
        new_html = re.sub(pattern, replacement, html, flags=re.DOTALL | re.IGNORECASE)
        if new_html != html:
            clean_count += 1
            html = new_html

    # 清理硬编码电话
    html = re.sub(
        r'[电话|手机|热线|tel|phone|mobile][：:]\s*[\d-]{7,15}',
        '<!-- phone cleaned -->',
        html,
        flags=re.IGNORECASE
    )
    # 清理多余空行
    html = re.sub(r'\n\s*\n\s*\n', '\n\n', html)

    if clean_count > 0 or original_len != len(html):
        report_path = filepath.parent / (filepath.stem + '_cleaned.htm')
        report_path.write_text(html, encoding='utf-8')
        print(f"[OK] 清理完成！")
        print(f"   原大小: {original_len} 字符")
        print(f"   现大小: {len(html)} 字符")
        print(f"   清理了 {clean_count} 个代码块")
        print(f"   输出: {report_path.name}")
    else:
        print("[INFO] 未发现需要清理的内容")


# ── 主入口 ─────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='EyouCMS 套标签助手',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python wrap.py init index.html              从首页提取 header/nav/footer
  python wrap.py scan ./templates/            扫描目录下所有硬编码内容
  python wrap.py rename ./templates/          按易优规范重命名文件
  python wrap.py clean list.html              清理广告弹窗

基础标签速查见 basic-tags.md
详细标签文档见 ../eyou-tag-assistant/tags/
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    p_init = subparsers.add_parser('init', help='从 HTML 提取 header/nav/footer 模板')
    p_init.add_argument('html_file', help='原始 HTML 文件路径')

    p_scan = subparsers.add_parser('scan', help='扫描硬编码内容，推荐替换标签')
    p_scan.add_argument('path', help='HTML 文件或目录')

    p_rename = subparsers.add_parser('rename', help='按 EyouCMS 规范重命名文件')
    p_rename.add_argument('dir_path', help='模板目录')

    p_clean = subparsers.add_parser('clean', help='清理广告弹窗等干扰代码')
    p_clean.add_argument('html_file', help='HTML 文件路径')

    args = parser.parse_args()

    if args.command == 'init':
        cmd_init(args.html_file)
    elif args.command == 'scan':
        cmd_scan(args.path)
    elif args.command == 'rename':
        cmd_rename(args.dir_path)
    elif args.command == 'clean':
        cmd_clean(args.html_file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
