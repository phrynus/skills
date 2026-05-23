# `{eyou:videolist}` — 视频列表（选集）

> **用途**：输出当前视频文档的选集列表，点击可切换 `videoplay` 中正在播放的视频。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/9994.html
> **关联表**：[`ey_media_file`](../dict/ey_media_file.md)

---

## 语法

```html
{eyou:videolist aid='$eyou.field.aid' id='video'}
  <a href="javascript:void(0);" {$video.onclick}>
    {$video.file_title} - {$video.file_time}
  </a>
  {$video.hidden}
{/eyou:videolist}
```

## 参数

| 参数 | 说明 |
|------|------|
| `aid` | 视频文档ID，内容页用 `$eyou.field.aid` |
| `autoplay` | `on`自动播放 / `off`点击播放 |
| `empty` | 无数据文案 |
| `mod` | 每隔N条触发 |
| `id` | 自定义变量名，默认 `field` |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$video.onclick}` | 点击切换视频的事件属性，放入 `<a>` 标签 |
| `{$video.file_title}` | 选集标题 |
| `{$video.file_time}` | 视频时长 |
| `{$video.hidden}` | 必须输出的隐藏域 |

## 完整用法示例（播放器 + 选集列表）

```html
<!-- 视频播放器 -->
{eyou:videoplay aid='$eyou.field.aid' autoplay='on' id='video'}
  <video {$video.id} width="100%" controls preload="auto">
    <source src="{$video.file_url}" type="video/mp4">
  </video>
  {$video.hidden}
{/eyou:videoplay}

<!-- 选集列表 -->
{eyou:videolist aid='$eyou.field.aid' id='video'}
  <a href="javascript:void(0);" {$video.onclick}>
    {$video.file_title} - {$video.file_time}
  </a>
  {$video.hidden}
{/eyou:videolist}
```
