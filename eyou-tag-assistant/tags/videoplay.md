# `{eyou:videoplay}` — 视频播放

> **用途**：在视频模型内容页调用后台上传的视频文件进行播放。配合 `videolist` 可实现多选集切换。
> **官方文档**：https://www.eyoucms.com/doc/label/arc/9993.html
> **关联表**：[`ey_media_file`](../dict/ey_media_file.md)

---

## 语法

```html
{eyou:videoplay aid='$eyou.field.aid' autoplay='on' id='video'}
  <video {$video.id} width="100%" controls preload="auto">
    <source src="{$video.file_url}" type="video/mp4">
  </video>
  {$video.hidden}
{/eyou:videoplay}
```

## 参数

| 参数 | 默认 | 说明 |
|------|------|------|
| `aid` | 当前文档 | 视频文档ID，内容页用 `$eyou.field.aid` |
| `autoplay` | `off` | `on`自动播放 / `off`点击播放 |
| `empty` | — | 无数据文案 |
| `id` | `field` | 自定义变量名 |

## 内置变量

| 变量 | 说明 |
|------|------|
| `{$video.id}` | 视频容器 id 属性（JS控制播放切换必需） |
| `{$video.file_url}` | 当前播放视频的文件URL |
| `{$video.hidden}` | 必须输出的隐藏域 |
