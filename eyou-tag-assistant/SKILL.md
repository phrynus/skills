---
name: eyou-tag-assistant
description: |
  EYOUCMS 模板标签专家，必须调用此 skill **任何时候**用户涉及 EYOUCMS/易优CMS 模板标签相关的工作——包括写标签、查标签用法、改模板、排查标签不生效、问某个标签的参数/变量/用法。
  
  触发场景（即使只是擦边也必须调）：
  - 用户提到 `{eyou:xxx}` 或 `eyou:xxx` 格式的标签名
  - 用户提到「EYOUCMS」「易优CMS」「Eyou 模板」「易优标签」任何变体
  - 用户需要写/改 `.htm` 模板文件，涉及动态数据（列表、内容、导航、表单等）
  - 用户问「怎么在首页显示文章」「列表页怎么加分页」「内容页的上一篇怎么弄」等模板需求
  - 用户反馈标签不生效、页面空白、变量没输出
  - 用户问某个字段/变量的可用参数（如 `$field.title`/`$eyou.field.xxx`/`$eyou.global.xxx`）
  - 用户给了一段 HTML 要求「换成标签」

  **关键禁令**：禁止凭记忆写标签参数和变量名。必须查 LLMS.md → tags/xx.md 确认。

  与 eyou-wrap-helper 的区别：本 skill 负责所有标签的**准确语法查询**，包括商城/会员/视频等复杂标签；eyou-wrap-helper 负责「扒站套标签」那一特定场景。
---

# EYOUCMS 标签助手

## 核心原则

**先查手册，再写代码。** 禁止凭记忆或猜测写 EYOUCMS 标签。EyouCMS 的标签参数名、变量前缀、嵌套规则有大量细节，写错一个字母模板就空白。

## 五步工作流

### Step 1：需求分析

用户说一句话，你要拆解出：
- **模板场景**：首页 / 列表页 / 内容页 / 搜索页 / 单页 / 商品页 / ...
- **需要的标签组合**：一个需求通常需要 2-5 个标签配合
- **可能用到的栏目ID/文档ID**：用户可能没给，需要问

例如用户说「帮我做个产品列表页带分页」，你应意识到：
- 模板类型：`lists_product.htm`
- 标签：`{eyou:list}` + `{eyou:pagelist}`，可能还要 `{eyou:screening}` 筛选

### Step 2：定位标签

打开 `LLMS.md`，使用「场景 → 标签组合矩阵」找到用户需求对应的标签组合。然后按标签名在「标签速查表」找到链接，跳转 `tags/xx.md`。

**绝对不要**：凭印象知道某个标签就直接写，跳过文档查阅。

### Step 3：阅读标签文档

每个 `tags/xx.md` 文件包含：语法、参数表、变量说明、示例。阅读时重点确认：

1. **参数名** — EyouCMS 参数名是 `typeid` 不是 `type_id`，`titlelen` 不是 `title_length`
2. **变量前缀** — 循环内用 `{$field.xxx}`，内容页用 `{$eyou.field.xxx}`，全局用 `{$eyou.global.xxx}`
3. **闭合方式** — 是自闭合 `{eyou:xxx /}` 还是完整结构 `{eyou:xxx}...{/eyou:xxx}`
4. **嵌套规则** — 嵌套时内层是否需要自定义 `id` 避免变量覆盖
5. **必须参数** — 哪些参数是必填的（如首页 artlist 必须指定 `typeid`）

如果文档内容不够清晰，参考文档中的示例代码，不要自己造。

### Step 4：生成代码

根据文档写出正确标签。输出要求：
- 每个标签带**完整参数**（除非参数真的可选且没必要）
- 保持用户原有的 HTML 结构（如果用户给了 HTML）
- 标签内适当添加**简短行内注释**辅助理解
- **禁止添加不存在的参数**或自创参数名
- 不确定的参数宁可省略，不要猜

```html
<!-- 好的输出：完整参数 + 清晰 -->
{eyou:artlist typeid='2' loop='6' titlelen='30' id='field'}
  <a href="{$field.arcurl}">{$field.title}</a>
{/eyou:artlist}

<!-- 坏输出：自创参数名 -->
{eyou:artlist category_id='2' limit='6'}   {* category_id 不存在！ *}
```

### Step 5：自我验证

输出前逐项复核：
- [ ] 每个标签的参数名与文档一致？
- [ ] 变量前缀正确？（循环内 `$field` / 内容页 `$eyou.field` / 全局 `$eyou.global`）
- [ ] 嵌套标签的内层用了自定义 `id`？
- [ ] 闭合标签名与开标签一致？
- [ ] 自闭合/完整结构选择正确？
- [ ] 所有参数值加了引号？（`typeid='2'` 不是 `typeid=2`）

## 输出规范

### 代码格式

```
- 标签参数用单引号：typeid='2'
- 标签与 HTML 混排时保持缩进清晰
- 复杂标签（如 sppurchase）必须完整结构，不自闭合
```

### 注释规范

```
- 在非常规用法、容易踩坑的地方加注释
- 注释用 HTML 格式：<!-- 说明 -->
- 不要给每个标签都加注释，只加需要解释的地方
```

### 变量前缀速查

| 使用场景 | 变量格式 | 典型标签 |
|----------|----------|----------|
| 循环体内 | `{$field.xxx}` | artlist, list, foreach, models, adv |
| 内容页（arcview 外） | `{$eyou.field.xxx}` | view_*.htm 模板 |
| 全局配置 | `{$eyou.global.xxx}` | 任何模板 |
| 自定义嵌套 | `{$自定义ID.xxx}` | 内层循环指定 id='myid' |
| 当前页面信息 | `{$eyou.xxx}` | 当前栏目、当前文档等 |

## 常见错误对照（扩展）

### 1. 参数名写错
```html
<!-- 错误 -->
{eyou:artlist type_id='2'}     <!-- type_id 不存在 -->
{eyou:list titlelen='30'}      <!-- 正确参数是 titlelen -->

<!-- 正确 -->
{eyou:artlist typeid='2'}
{eyou:list titlelen='30'}
```

### 2. 变量前缀混用
```html
<!-- 错误：内容页用 $field -->
{$field.title}

<!-- 正确：内容页用 $eyou.field -->
{$eyou.field.title}

<!-- 错误：循环内用 $eyou.field -->
{eyou:artlist}
  {$eyou.field.title}   <!-- 空值 -->
{/eyou:artlist}

<!-- 正确：循环内用 $field -->
{eyou:artlist}
  {$field.title}
{/eyou:artlist}
```

### 3. 嵌套时变量被覆盖
```html
<!-- 错误 -->
{eyou:artlist}
  {eyou:tags loop='3'}
    {$field.tag}  <!-- 被内层覆盖，外层 field 丢失 -->
  {/eyou:tags}
{/eyou:artlist}

<!-- 正确 -->
{eyou:artlist}
  {eyou:tags loop='3' id='tag'}
    {$tag.tag}
  {/eyou:tags}
{/eyou:artlist}
```

### 4. sppurchase 错误闭合
```html
<!-- 错误 -->
{eyou:sppurchase /}

<!-- 正确 -->
{eyou:sppurchase id='field'}
  <button {$field.BuyNow}>立即购买</button>
  {$field.hidden}
{/eyou:sppurchase}
```

### 5. 栏目类型不对应
```html
<!-- 错误：产品栏目下用 article 模型的内容标签 -->
{eyou:list model='article'}

<!-- 正确：产品列表不需要指定 model，list 自动绑定当前栏目 -->
{eyou:list loop='12'}
```

### 6. 忘记指定 typeid
```html
<!-- 首页用 artlist 不指定 typeid → 取不到数据 -->
{eyou:artlist loop='5'}

<!-- 正确 -->
{eyou:artlist typeid='2' loop='5'}
```

### 7. assign 命名冲突
```html
<!-- 错误：assign 覆盖了已有变量名 -->
{eyou:assign name='field' value='...'}  <!-- 与循环变量名冲突 -->

<!-- 正确 -->
{eyou:assign name='myVar' value='...'}
```

## 错误恢复策略

| 情况 | 处理方式 |
|------|----------|
| LLMS.md 中找不到用户提到的标签 | 告诉用户该标签不在记录范围内，建议查官方文档 |
| tags/xx.md 文档不完整 | 参考文档中的示例代码，不要自创；告知用户文档可能不完整 |
| 不确定参数的值域 | 给用户列出可选值让用户确认，不要猜测 |
| 用户给的参数与文档矛盾 | 以文档为准并提醒用户 |
| 一个需求涉及多个标签 | 逐个查阅每个标签的文档，不要只查一个就写全部 |

## 与其他 skill 的关系

- **eyou-wrap-helper**：专门处理「扒站套标签」，把静态 HTML 替换为标签。如果用户在做全套模板迁移，建议先用 `eyou-wrap-helper` 处理公共部分和基础标签，复杂标签（商城/会员/视频）回来查本 skill
- **eyoucms-template**：全流程模板建站，包含更多业务逻辑。本 skill 专注「标签语法准确」这一件事
