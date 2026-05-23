# 快速转换模块 (convert)

> **模块路径**: `github.com/adshao/go-binance/v2`（通过 `client.NewConvertGetQuoteService()` 等使用）
> **相关文档**: [SKILL.md](../SKILL.md) | [common.md](./common.md)

快速转换（Convert）是一种简化版的币币交易，用户获得实时报价后在有效期内确认即可完成转换。

---

## 目录

1. [汇率查询](#1-汇率查询)
2. [获取报价](#2-获取报价)
3. [接受报价](#3-接受报价)
4. [交易历史](#4-交易历史)
5. [订单状态](#5-订单状态)
6. [类型索引](#6-类型索引)

---

## 1. 汇率查询 (ExchangeInfo)

```go
infos, err := client.NewConvertExchangeInfoService().
    FromAsset("BTC").
    ToAsset("USDT").
    Do(ctx)

for _, info := range infos {
    fmt.Printf("BTC→USDT: 最小=%s 最大=%s\n",
        info.FromAssetMinAmount, info.ToAssetMaxAmount)
}
```

---

## 2. 获取报价 (GetQuote)

获取实时报价，需要在有效期内接受才能成交。

```go
quote, err := client.NewConvertGetQuoteService().
    FromAsset("BTC").
    ToAsset("USDT").
    FromAmount("0.001").     // 二选一：按源资产数量
    // ToAmount("50").       // 或：按目标资产数量
    ValidTime("5").          // 有效时间（秒），可选，默认30
    Do(ctx)

fmt.Printf("报价ID: %s\n", quote.QuoteId)
fmt.Printf("转换比例: %s (1:%s)\n", quote.Ratio, quote.InverseRatio)
fmt.Printf("有效期至: %d\n", quote.ValidTime)
fmt.Printf("目标数量: %s %s\n", quote.ToAmount, "USDT")
fmt.Printf("源资产数量: %s %s\n", quote.FromAmount, "BTC")
```

---

## 3. 接受报价 (AcceptQuote)

接受报价后，在有效期内完成转换。

```go
accepted, err := client.NewConvertAcceptQuoteService().
    QuoteId(quote.QuoteId).
    Do(ctx)

fmt.Printf("转换成功: 订单ID=%s 状态=%s 创建时间=%d\n",
    accepted.OrderId, accepted.OrderStatus, accepted.CreateTime)
```

---

## 4. 交易历史 (TradeHistory)

```go
history, err := client.NewConvertTradeHistoryService().
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)

for _, h := range history.List {
    fmt.Printf("转换: ID=%d 状态=%s %s→%s 源=%s 目标=%s 比例=%s 时间=%d\n",
        h.OrderId, h.OrderStatus,
        h.FromAsset, h.ToAsset,
        h.FromAmount, h.ToAmount,
        h.Ratio, h.CreateTime)
}
```

---

## 5. 订单状态 (OrderStatus)

```go
status, err := client.NewConvertOrderStatusService().
    OrderId(123456).
    // QuoteId("xxx"). // 也可通过 QuoteId 查询
    Do(ctx)

fmt.Printf("订单ID: %d\n", status.OrderId)
fmt.Printf("状态: %s\n", status.OrderStatus)
fmt.Printf("%s→%s: %s→%s\n",
    status.FromAsset, status.ToAsset, status.FromAmount, status.ToAmount)
fmt.Printf("比例: %s 创建时间: %d\n", status.Ratio, status.CreateTime)
```

---

## 6. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `ConvertExchangeInfoService` | 汇率查询 |
| `ConvertAssetInfoService` | 资产精度信息 |
| `ConvertGetQuoteService` | 获取报价 |
| `ConvertAcceptQuoteService` | 接受报价 |
| `ConvertTradeHistoryService` | 交易历史 |
| `ConvertOrderStatusService` | 订单状态 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `ConvertExchangeInfo` | 汇率信息 |
| `ConvertAssetInfo` | 资产精度 |
| `ConvertQuote` | 报价 |
| `ConvertAcceptQuote` | 接受报价响应 |
| `ConvertTradeHistory` | 交易历史 |
| `ConvertTradeHistoryItem` | 历史记录项 |
| `ConvertOrderStatus` | 订单状态 |

### ConvertExchangeInfo 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `FromAsset` | string | 源资产 |
| `ToAsset` | string | 目标资产 |
| `FromAssetMinAmount` | string | 最小源资产数量 |
| `FromAssetMaxAmount` | string | 最大源资产数量 |
| `ToAssetMinAmount` | string | 最小目标资产数量 |
| `ToAssetMaxAmount` | string | 最大目标资产数量 |

### ConvertQuote 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `QuoteId` | string | 报价ID |
| `Ratio` | string | 转换比例 |
| `InverseRatio` | string | 反向比例 |
| `ValidTime` | int64 | 有效期（Unix时间戳）|
| `ToAmount` | string | 目标资产数量 |
| `FromAmount` | string | 源资产数量 |

### ConvertAcceptQuote 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `OrderId` | string | 转换订单ID |
| `CreateTime` | int64 | 创建时间 |
| `OrderStatus` | string | 订单状态 |

### ConvertTradeHistory 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `List` | []ConvertTradeHistoryItem | 历史列表 |
| `StartTime` | int64 | 开始时间 |
| `EndTime` | int64 | 结束时间 |
| `Limit` | int32 | 限制数 |
| `MoreData` | bool | 是否有更多数据 |

### ConvertTradeHistoryItem 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `QuoteId` | string | 报价ID |
| `OrderId` | int64 | 转换订单ID |
| `OrderStatus` | string | 订单状态 |
| `FromAsset` | string | 源资产 |
| `FromAmount` | string | 源资产数量 |
| `ToAsset` | string | 目标资产 |
| `ToAmount` | string | 目标资产数量 |
| `Ratio` | string | 转换比例 |
| `InverseRatio` | string | 反向比例 |
| `CreateTime` | int64 | 创建时间 |

### ConvertOrderStatus 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `OrderId` | int64 | 订单ID |
| `OrderStatus` | string | 状态 |
| `FromAsset` | string | 源资产 |
| `FromAmount` | string | 源资产数量 |
| `ToAsset` | string | 目标资产 |
| `ToAmount` | string | 目标资产数量 |
| `Ratio` | string | 转换比例 |
| `InverseRatio` | string | 反向比例 |
| `CreateTime` | int64 | 创建时间 |
