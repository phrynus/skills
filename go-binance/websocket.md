# WebSocket 模块总览 (websocket)

> **现货 WebSocket**: `github.com/adshao/go-binance/v2`
> **合约 WebSocket**: `github.com/adshao/go-binance/v2/futures`
> **期权 WebSocket**: `github.com/adshao/go-binance/v2/options`
> **相关文档**: [SKILL.md](../SKILL.md) | [spot.md](./spot.md) | [futures.md](./futures.md) | [options.md](./options.md)

WebSocket 提供实时数据推送，支持行情数据、用户数据流、多路复用等多种模式。

---

## 目录

1. [现货 WebSocket](#1-现货-websocket)
2. [合约 WebSocket](#2-合约-websocket)
3. [期权 WebSocket](#3-期权-websocket)
4. [用户数据流](#4-用户数据流)
5. [多路复用 Combined Streams](#5-多路复用-combined-streams)
6. [优雅关闭](#6-优雅关闭)
7. [类型索引](#7-类型索引)

---

## 1. 现货 WebSocket

### 1.1 全局配置

```go
// 现货 WebSocket 端点
binance.BaseWsMainURL    // "wss://stream.binance.com:9443/ws"
binance.BaseWsTestnetURL // "wss://stream.testnet.binance.vision/ws"
binance.BaseWsDemoURL   // "wss://demo-stream.binance.com/ws"

// WebSocket API 端点
binance.BaseWsApiMainURL    // "wss://ws-api.binance.com:443/ws-api/v3"
binance.BaseWsApiTestnetURL // "wss://ws-api.testnet.binance.vision/ws-api/v3"
binance.BaseWsApiDemoURL   // "wss://demo-ws-api.binance.com/ws-api/v3"

// 连接配置
binance.WebsocketTimeout = time.Second * 600
binance.WebsocketPongTimeout = time.Second * 10
binance.WebsocketPingTimeout = time.Second * 10
binance.WebsocketKeepalive = true
binance.WebsocketTimeoutReadWriteConnection = time.Second * 10
binance.ProxyUrl = ""

// 设置代理
binance.SetWsProxyUrl("http://proxy:port")
```

### 1.2 深度行情 (WsDepthServe)

```go
// 逐档深度（更新推送）
doneC, stopC, err := binance.WsDepthServe("BTCUSDT",
    func(event *binance.WsDepthEvent) {
        fmt.Println("买一:", event.Bids[0].Price, "×", event.Bids[0].Quantity)
        fmt.Println("卖一:", event.Asks[0].Price, "×", event.Asks[0].Quantity)
    },
    func(err error) { fmt.Println("错误:", err) },
)

// 100ms 推送深度
doneC, stopC, err := binance.WsDepthServe100Ms("BTCUSDT",
    func(event *binance.WsDepthEvent) {
        fmt.Println("深度更新:", event.LastUpdateID)
    }, errHandler,
)

// 局部深度
doneC, stopC, err := binance.WsPartialDepthServe("BTCUSDT", "20",
    func(event *binance.WsPartialDepthEvent) {
        fmt.Println("局部深度:", event.Bids[:5])
    }, errHandler,
)
```

### 1.3 K线行情 (WsKlineServe)

```go
// 间隔: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
doneC, _, err := binance.WsKlineServe("BTCUSDT", "1m",
    func(event *binance.WsKlineEvent) {
        k := event.Kline
        fmt.Printf("K线[%s-%s]: O=%.2f H=%.2f L=%.2f C=%.2f V=%.2f 成交额=%.2f\n",
            event.Symbol, k.Interval,
            k.Open, k.High, k.Low, k.Close, k.Volume, k.QuoteVolume)
    }, errHandler,
)

// 是否最后K线
fmt.Printf("是否收盘: %v\n", k.IsFinal)
```

### 1.4 成交记录 (WsTradeServe / WsAggTradeServe)

```go
// 单交易对成交
doneC, _, err := binance.WsTradeServe("BTCUSDT",
    func(event *binance.WsTradeEvent) {
        fmt.Printf("成交: 价格=%s 数量=%s 方向=%s 买方为maker=%v\n",
            event.Price, event.Quantity, event.Side, event.IsBuyerMaker)
    }, errHandler,
)

// 聚合交易
doneC, _, err := binance.WsAggTradeServe("BTCUSDT",
    func(event *binance.WsAggTradeEvent) {
        fmt.Printf("聚合成交: ID=%d 价格=%s 数量=%s Maker=%v\n",
            event.AggTradeID, event.Price, event.Quantity, event.Maker)
    }, errHandler,
)
```

### 1.5 市场 Ticker (WsMarketStatServe)

```go
// 单交易对 ticker
doneC, _, err := binance.WsMarketStatServe("BTCUSDT",
    func(event *binance.WsMarketStatEvent) {
        fmt.Printf("24h涨跌: %s (%s%%) 高=%.2f 低=%.2f 成交量=%s\n",
            event.PriceChange, event.PriceChangePercent,
            event.HighPrice, event.LowPrice, event.Volume)
    }, errHandler,
)

// 所有交易对 ticker
doneC, _, err := binance.WsAllMarketsStatServe(
    func(event binance.WsAllMarketsStatEvent) {
        fmt.Printf("%s: %s (%s%%)\n",
            event.Symbol, event.LastPrice, event.PriceChangePercent)
    }, errHandler,
)
```

### 1.6 订单簿 Ticker (WsBookTickerServe)

```go
// 单交易对
doneC, _, err := binance.WsBookTickerServe("BTCUSDT",
    func(event *binance.WsBookTickerEvent) {
        fmt.Printf("最优买卖: 买=%s×%s 卖=%s×%s\n",
            event.BestBidPrice, event.BestBidQty,
            event.BestAskPrice, event.BestAskQty)
    }, errHandler,
)

// 所有交易对
doneC, _, err := binance.WsAllBookTickerServe(
    func(event *binance.WsBookTickerEvent) {
        fmt.Printf("%s: 买=%s 卖=%s\n",
            event.Symbol, event.BestBidPrice, event.BestAskPrice)
    }, errHandler,
)
```

### 1.7 公告 (WsAnnouncementServe)

```go
doneC, _, err := binance.WsAnnouncementServe(
    binance.WsAnnouncementParam{
        Random:   "optional_random_string",
        Topic:    "all",
        RecvWindow: 60000,
        Timestamp: time.Now().UnixMilli(),
        Signature: "signature_string",
        ApiKey:   "your_api_key",
    },
    func(event *binance.WsAnnouncementEvent) {
        fmt.Printf("公告: [%s] %s\n", event.CatalogName, event.Title)
    }, errHandler,
)
```

---

## 2. 合约 WebSocket

### 2.1 全局配置

```go
futures.BaseWsMainUrl    // "wss://fstream.binance.com/ws"
futures.BaseWsTestnetUrl // "wss://stream.binancefuture.com/ws"
futures.BaseWsDemoURL    // "wss://fstream.binancefuture.com/ws"

futures.UseTestnet = true
futures.WebsocketTimeout = time.Second * 600
futures.WebsocketPongTimeout = time.Second * 10
futures.WebsocketKeepalive = true
```

### 2.2 合约深度 (WsDepthServe)

```go
// 深度（默认 100ms）
doneC, stopC, err := futures.WsDepthServe("btcusdt",
    func(event *futures.WsDepthEvent) {
        fmt.Printf("深度: 买一=%s 卖一=%s\n", event.Bids[0].Price, event.Asks[0].Price)
    }, errHandler,
)

// 差异深度
doneC, stopC, err := futures.WsDiffDepthServe("btcusdt",
    func(event *futures.WsDepthEvent) {
        fmt.Printf("差异深度 LastUpdateID=%d\n", event.LastUpdateID)
    }, errHandler,
)
```

### 2.3 合约 K线 (WsKlineServe)

```go
doneC, _, err := futures.WsKlineServe("btcusdt", "1m",
    func(event *futures.WsKlineEvent) {
        k := event.Kline
        fmt.Printf("合约K线: C=%.2f V=%.2f\n", k.Close, k.Volume)
    }, errHandler,
)

// 连续合约 K线
doneC, _, err := futures.WsContinuousKlineServe(
    futures.WsContinuousKlineSubscribeArgs{
        Pair: "BTCUSDT", ContractType: "PERPETUAL", Interval: "1m",
    },
    func(event *futures.WsContinuousKlineEvent) {
        k := event.Kline
        fmt.Printf("连续K线[%s]: C=%.2f\n", event.PairSymbol, k.Close)
    }, errHandler,
)
```

### 2.4 标记价格 (WsMarkPriceServe)

```go
// 所有 symbol 100ms 更新
doneC, _, err := futures.WsAllMarkPriceServeWithRate("100ms",
    func(event futures.WsAllMarkPriceEvent) {
        for _, m := range event {
            fmt.Printf("标记价格 %s: %s 资金费率: %s\n",
                m.Symbol, m.MarkPrice, m.FundingRate)
        }
    }, errHandler,
)

// 单 symbol
doneC, _, err := futures.WsMarkPriceServe("btcusdt",
    func(event *futures.WsMarkPriceEvent) {
        fmt.Printf("标记价格: %s 资金费率: %s 下次资金时间: %d\n",
            event.MarkPrice, event.FundingRate, event.NextFundingTime)
    }, errHandler,
)
```

### 2.5 合约 Ticker

```go
// 迷你 ticker（单 symbol）
doneC, _, err := futures.WsMiniMarketTickerServe("btcusdt",
    func(event *futures.WsMiniMarketTickerEvent) {
        fmt.Printf("迷你Ticker %s: 收=%.2f 开=%.2f 高=%.2f 低=%.2f\n",
            event.Symbol, event.ClosePrice, event.OpenPrice, event.HighPrice, event.LowPrice)
    }, errHandler,
)

// 全部迷你 ticker
doneC, _, err := futures.WsAllMiniMarketTickerServe(
    func(event futures.WsAllMiniMarketTickerEvent) {
        for _, t := range event {
            fmt.Printf("%s: 收=%.2f\n", t.Symbol, t.ClosePrice)
        }
    }, errHandler,
)
```

### 2.6 强平事件 (WsLiquidationOrderServe)

```go
// 单交易对
doneC, _, err := futures.WsLiquidationOrderServe("btcusdt",
    func(event *futures.WsLiquidationOrderEvent) {
        o := event.LiquidationOrder
        fmt.Printf("强平: %s %s 价格=%s 数量=%s 状态=%s\n",
            o.Symbol, o.Side, o.AvgPrice, o.OrigQuantity, o.OrderStatus)
    }, errHandler,
)

// 所有交易对
doneC, _, err := futures.WsAllLiquidationOrderServe(
    func(event *futures.WsLiquidationOrderEvent) {
        fmt.Printf("全市场强平: %s %s\n",
            event.LiquidationOrder.Symbol, event.LiquidationOrder.Side)
    }, errHandler,
)
```

### 2.7 综合指数 (WsCompositiveIndexServe)

```go
doneC, _, err := futures.WsCompositiveIndexServe("BTCUSD",
    func(event *futures.WsCompositiveIndexEvent) {
        fmt.Printf("综合指数 %s: %s\n", event.Symbol, event.Price)
        for _, c := range event.Composition {
            fmt.Printf("  成分: %s 权重=%s\n", c.BaseAsset, c.WeighPercent)
        }
    }, errHandler,
)
```

### 2.8 合约成交 (WsAggTradeServe)

```go
doneC, _, err := futures.WsAggTradeServe("btcusdt",
    func(event *futures.WsAggTradeEvent) {
        fmt.Printf("合约成交: 价格=%s 数量=%s Maker=%v\n",
            event.Price, event.Quantity, event.Maker)
    }, errHandler,
)
```

---

## 3. 期权 WebSocket

期权 WebSocket 接口位于 `github.com/adshao/go-binance/v2/options`。

---

## 4. 用户数据流

### 4.1 现货用户数据流

```go
// 获取 listenKey
listenKey, _ := client.NewStartUserStreamService().Do(ctx)

// 建立 WebSocket 连接
doneC, stopC, err := binance.WsUserDataServe(listenKey,
    func(event *binance.WsUserDataEvent) {
        switch e := event.Data.(type) {
        case *binance.WsOutboundAccountPosition:
            // 账户余额变动
            for _, b := range e.Balances {
                fmt.Printf("%s: 可用=%s 锁定=%s\n", b.Asset, b.Free, b.Locked)
            }

        case *binance.WsExecutionReport:
            // 订单更新
            fmt.Printf("订单更新: ID=%d 状态=%s 成交量=%s\n",
                e.OrderID, e.Status, e.CumulativeFilledQty)

        case *binance.WsBalanceUpdate:
            // 余额更新
            fmt.Printf("余额变动: %s %s\n", e.Asset, e.Change)

        case *binance.WsListStatus:
            // OCO 列表状态更新
            fmt.Printf("OCO更新: 状态=%s 订单数=%d\n",
                e.ListStatusType, len(e.Orders))
        }
    },
    func(err error) { fmt.Println("WS错误:", err) },
)
defer func() { stopC <- struct{}{} }()

// 自动续期（每30分钟）
ticker := time.NewTicker(25 * time.Minute)
go func() {
    for range ticker.C {
        client.NewKeepaliveUserStreamService().
            ListenKey(listenKey).
            Do(context.Background())
    }
}()
```

### 4.2 合约用户数据流

```go
listenKey, _ := futuresClient.NewStartUserStreamService().Do(ctx)

doneC, stopC, err := futures.WsUserDataServe(listenKey,
    func(event *futures.WsUserDataEvent) {
        switch e := event.Data.(type) {
        case *futures.WsUserDataMarginCall:
            // 强平预警
            for _, p := range e.MarginCallPositions {
                fmt.Printf("强平预警: %s 数量=%s 类型=%s 保证金类型=%s\n",
                    p.Symbol, p.Amount, p.Side, p.MarginType)
            }

        case *futures.WsUserDataAccountUpdate:
            // 账户更新
            for _, b := range e.AccountUpdate.Balances {
                fmt.Printf("余额: %s=%s 变动=%s\n",
                    b.Asset, b.Balance, b.ChangeBalance)
            }
            for _, p := range e.AccountUpdate.Positions {
                fmt.Printf("持仓: %s=%s %s\n",
                    p.Symbol, p.Amount, p.EntryPrice)
            }

        case *futures.WsUserDataOrderTradeUpdate:
            o := e.OrderTradeUpdate
            fmt.Printf("订单更新: ID=%d %s %s %s 成交=%s\n",
                o.OrderID, o.Side, o.Type, o.Status, o.AccumulatedFilledQty)

        case *futures.WsUserDataAccountConfigUpdate:
            c := e.AccountConfigUpdate
            fmt.Printf("账户配置更新: symbol=%s leverage=%d\n",
                c.Symbol, c.Leverage)

        case *futures.WsUserDataAlgoUpdate:
            a := e.AlgoUpdate
            fmt.Printf("算法订单: AlgoID=%d 状态=%s\n",
                a.AlgoID, a.AlgoStatus)

        case *futures.WsUserDataConditionalOrderTriggerReject:
            r := e.ConditionalOrderTriggerReject
            fmt.Printf("条件订单触发拒绝: ID=%d 原因=%s\n",
                r.OrderId, r.RejectReason)
        }
    },
    func(err error) { fmt.Println("WS错误:", err) },
)
```

### 4.3 逐仓用户数据流

```go
// 获取逐仓 listenKey（每个 symbol 独立）
listenKey, _ := client.NewStartIsolatedMarginUserStreamService().
    Symbol("BTCUSDT").
    Do(ctx)

doneC, stopC, err := binance.WsUserDataServe(listenKey,
    func(event *binance.WsUserDataEvent) {
        // 同现货用户数据流处理
    }, errHandler,
)

// 续期
client.NewKeepaliveIsolatedMarginUserStreamService().
    Symbol("BTCUSDT").
    ListenKey(listenKey).
    Do(ctx)

// 关闭
client.NewCloseIsolatedMarginUserStreamService().
    Symbol("BTCUSDT").
    ListenKey(listenKey).
    Do(ctx)
```

---

## 5. 多路复用 Combined Streams

同时订阅多个数据流，减少连接数。

### 5.1 现货 Combined Streams

```go
streams := []string{
    "btcusdt@depth@100ms",
    "btcusdt@kline_1m",
    "ethusdt@trade",
    "btcusdt@bookTicker",
}

doneC, _, err := binance.WsCombinedServe(streams,
    func(event any) {
        switch e := event.(type) {
        case *binance.WsDepthEvent:
            fmt.Printf("[深度] %s 买一=%s\n", e.Symbol, e.Bids[0].Price)
        case *binance.WsKlineEvent:
            fmt.Printf("[K线] %s %s 收=%.2f\n", e.Symbol, e.Kline.Interval, e.Kline.Close)
        case *binance.WsTradeEvent:
            fmt.Printf("[成交] %s 价格=%s\n", e.Symbol, e.Price)
        case *binance.WsBookTickerEvent:
            fmt.Printf("[Ticker] %s 买=%s 卖=%s\n", e.Symbol, e.BestBidPrice, e.BestAskPrice)
        }
    }, errHandler,
)
```

### 5.2 合约 Combined Streams

```go
streams := []string{
    "btcusdt@depth@100ms",
    "btcusdt@kline_1m",
    "btcusdt@markPrice@100ms",
}

doneC, _, err := futures.WsCombinedServe(streams,
    func(event any) {
        switch e := event.(type) {
        case *futures.WsDepthEvent:
            fmt.Printf("[深度] %s 买一=%s\n", e.Symbol, e.Bids[0].Price)
        case *futures.WsKlineEvent:
            fmt.Printf("[K线] %s 收=%.2f\n", e.Symbol, e.Kline.Close)
        case *futures.WsMarkPriceEvent:
            fmt.Printf("[标记价格] %s=%s\n", e.Symbol, e.MarkPrice)
        }
    }, errHandler,
)

// K线多间隔订阅
doneC, _, err := futures.WsCombinedKlineServeMultiInterval(
    map[string][]string{
        "BTCUSDT": {"1m", "5m", "15m"},
        "ETHUSDT": {"1m", "1h"},
    },
    func(event *futures.WsKlineEvent) {
        fmt.Printf("[%s] %s %s 收=%.2f\n",
            event.Symbol, event.Kline.Interval, event.Symbol, event.Kline.Close)
    }, errHandler,
)
```

### 5.3 深度多交易对

```go
// 多个 symbol 的深度
streams := []string{
    "btcusdt@depth@100ms",
    "ethusdt@depth@100ms",
}
doneC, _, err := futures.WsCombinedDepthServe(streams,
    func(event *futures.WsDepthEvent) {
        fmt.Printf("[%s] 买一=%s 卖一=%s\n",
            event.Symbol, event.Bids[0].Price, event.Asks[0].Price)
    }, errHandler,
)
```

---

## 6. 优雅关闭

所有 WebSocket 连接都需要正确关闭以释放资源：

```go
// 创建连接
doneC, stopC, err := binance.WsDepthServe("BTCUSDT", handler, errHandler)

// 关闭时：
func shutdown() {
    // 1. 发送停止信号
    stopC <- struct{}{}

    // 2. 等待 WebSocket 优雅关闭
    <-doneC

    // 3. 资源清理
}

// 使用 defer 确保关闭
func main() {
    doneC, stopC, err := binance.WsDepthServe("BTCUSDT", handler, errHandler)
    defer func() {
        stopC <- struct{}{}
        <-doneC
    }()

    // 业务逻辑...
}
```

---

## 7. 类型索引

### 现货 WebSocket Handler 类型

| 类型名 | 事件类型 |
|--------|----------|
| `WsPartialDepthHandler` | `*WsPartialDepthEvent` |
| `WsDepthHandler` | `*WsDepthEvent` |
| `WsKlineHandler` | `*WsKlineEvent` |
| `WsAggTradeHandler` | `*WsAggTradeEvent` |
| `WsTradeHandler` | `*WsTradeEvent` |
| `WsCombinedTradeHandler` | `*WsCombinedTradeEvent` |
| `WsUserDataHandler` | `*WsUserDataEvent` |
| `WsMarketStatHandler` | `*WsMarketStatEvent` |
| `WsAllMarketsStatHandler` | `WsAllMarketsStatEvent` |
| `WsAllMiniMarketsStatServeHandler` | `WsAllMiniMarketsStatEvent` |
| `WsBookTickerHandler` | `*WsBookTickerEvent` |
| `WsAnnouncementHandler` | `*WsAnnouncementEvent` |
| `ErrHandler` | `error` |

### 合约 WebSocket Handler 类型

| 类型名 | 事件类型 |
|--------|----------|
| `WsAggTradeHandler` | `*WsAggTradeEvent` |
| `WsMarkPriceHandler` | `*WsMarkPriceEvent` |
| `WsAllMarkPriceHandler` | `WsAllMarkPriceEvent` |
| `WsKlineHandler` | `*WsKlineEvent` |
| `WsContinuousKlineHandler` | `*WsContinuousKlineEvent` |
| `WsMiniMarketTickerHandler` | `*WsMiniMarketTickerEvent` |
| `WsAllMiniMarketTickerHandler` | `WsAllMiniMarketTickerEvent` |
| `WsMarketTickerHandler` | `*WsMarketTickerEvent` |
| `WsAllMarketTickerHandler` | `WsAllMarketTickerEvent` |
| `WsBookTickerHandler` | `*WsBookTickerEvent` |
| `WsLiquidationOrderHandler` | `*WsLiquidationOrderEvent` |
| `WsDepthHandler` | `*WsDepthEvent` |
| `WsUserDataHandler` | `*WsUserDataEvent` |
| `ErrHandler` | `error` |

### 现货 WebSocket Event Struct

| 类型名 | 说明 |
|--------|------|
| `WsPartialDepthEvent` | 局部深度（top N档）|
| `WsDepthEvent` | 全量深度更新 |
| `WsKlineEvent` | K线 |
| `WsKline` | K线数据 |
| `WsAggTradeEvent` | 聚合交易 |
| `WsTradeEvent` | 成交 |
| `WsCombinedTradeEvent` | 组合交易 |
| `WsUserDataEvent` | 用户数据（多态）|
| `WsOutboundAccountPosition` | 账户余额 |
| `WsExecutionReport` | 订单执行报告 |
| `WsBalanceUpdate` | 余额更新 |
| `WsListStatus` | OCO 列表状态 |
| `WsMarketStatEvent` | 市场统计 |
| `WsAllMarketsStatEvent` | 所有市场统计 |
| `WsMiniMarketsStatEvent` | 迷你市场统计 |
| `WsAllMiniMarketsStatEvent` | 所有迷你市场统计 |
| `WsBookTickerEvent` | 订单簿 ticker |
| `WsCombinedBookTickerEvent` | 组合 ticker |
| `WsAnnouncementEvent` | 公告 |
| `WsAnnouncementParam` | 公告参数 |

### 合约 WebSocket Event Struct

| 类型名 | 说明 |
|--------|------|
| `WsAggTradeEvent` | 聚合交易 |
| `WsMarkPriceEvent` | 标记价格 |
| `WsAllMarkPriceEvent` | 所有标记价格 |
| `WsKlineEvent` | K线 |
| `WsKline` | K线数据 |
| `WsContinuousKlineEvent` | 连续合约K线 |
| `WsContinuousKline` | 连续合约K线数据 |
| `WsMiniMarketTickerEvent` | 迷你 ticker |
| `WsAllMiniMarketTickerEvent` | 所有迷你 ticker |
| `WsMarketTickerEvent` | ticker |
| `WsAllMarketTickerEvent` | 所有 ticker |
| `WsBookTickerEvent` | 订单簿 ticker |
| `WsCombinedBookTickerEvent` | 组合 ticker |
| `WsLiquidationOrderEvent` | 强平事件 |
| `WsDepthEvent` | 深度事件 |
| `WsUserDataEvent` | 用户数据（多态）|
| `WsUserDataMarginCall` | 强平预警 |
| `WsUserDataAccountUpdate` | 账户更新 |
| `WsUserDataOrderTradeUpdate` | 订单/成交更新 |
| `WsUserDataAccountConfigUpdate` | 账户配置更新 |
| `WsUserDataAlgoUpdate` | 算法订单更新 |
| `WsUserDataTradeLite` | 简化成交 |
| `WsUserDataConditionalOrderTriggerReject` | 条件订单触发拒绝 |
| `WsAlgoUpdate` | 算法更新详情 |
| `WsBalance` | 余额 |
| `WsPosition` | 持仓 |
| `WsOrderTradeUpdate` | 订单/成交更新 |
| `WsComposition` | 指数成分 |
| `WsCompositiveIndexEvent` | 综合指数 |
