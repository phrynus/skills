# 数据字典：ey_media_file

> **表说明**：视频附件表，存储视频模型文档的选集文件信息
> **字段数量**：21
> **引用此表的标签**：[videoplay](../tags/videoplay.md) · [videolist](../tags/videolist.md)

---

## 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| `file_id` 🔑 | int(10) | 否 | — | 主键，文件ID |
| `aid` | int(10) | 否 | 0 | 关联文档ID（`ey_archives.aid`） |
| `title` | varchar(200) | 否 | — | 文档标题 |
| `file_name` | varchar(200) | 否 | — | 文件名称 |
| `file_title` | varchar(200) | 否 | — | 选集标题（模板中 `{$video.file_title}`） |
| `file_url` | text | 否 | — | 文件存储路径/URL（模板中 `{$video.file_url}`） |
| `file_time` | int(8) | 否 | 0 | 视频时长（秒，模板中 `{$video.file_time}`） |
| `file_ext` | varchar(50) | 否 | — | 文件后缀名（如 mp4） |
| `file_size` | varchar(255) | 否 | — | 文件大小 |
| `file_mime` | varchar(200) | 否 | — | 文件MIME类型 |
| `uhash` | varchar(200) | 否 | — | 自定义加密值（视频播放权限验证） |
| `md5file` | varchar(200) | 否 | — | 文件MD5（用于检测文件完整性） |
| `is_remote` | tinyint(1) | 否 | 0 | 是否远程文件：0=本地，1=远程 |
| `playcount` | int(10) | 否 | 0 | 播放次数 |
| `gratis` | tinyint(1) | 否 | 0 | 是否可试看：0=否，1=是 |
| `sort_order` | smallint(5) | 否 | 0 | 排序号 |
| `add_time` | int(10) | 否 | 0 | 上传时间（Unix时间戳） |
| `update_time` | int(11) | 否 | 0 | 更新时间（Unix时间戳） |

## 索引

| 键名 | 类型 | 唯一 | 字段 |
|------|------|:----:|------|
| PRIMARY | BTREE | 是 | file_id |
| aid | BTREE | 否 | aid |
