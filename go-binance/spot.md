# 现货与杠杆交易模块 (spot)

> **模块路径**: `github.com/adshao/go-binance/v2`
> **客户端**: `Client`（通过 `binance.NewClient()` 创建）
> **相关文档**: [SKILL.md](../SKILL.md) | [websocket.md](./websocket.md) | [common.md](./common.md) | [margin.md](./margin.md)

---

## 目录

1. [客户端](#1-客户端)
2. [常量与枚举](#2-常量与枚举)
3. [行情数据](#3-行情数据)
4. [订单管理](#4-订单管理)
5. [账户操作](#5-账户操作)
6. [WebSocket](#6-websocket)
7. [类型索引](#7-类型索引)

---

## 1. 客户端

### 初始化

```go
import "github.com/adshao/go-binance/v2"

client := binance.NewClient(apiKey, secretKey)
client.HTTPClient = &http.Client{Timeout: 10 * time.Second} // 可选：自定义 HTTP 客户端
client.Debug = true // 可选：调试模式
```

### 客户端方法一览

```go
// 行情
client.NewDepthService()           // 深度
client.NewKlinesService()           // K线
client.NewAggTradesService()        // 聚合交易
client.NewRecentTradesService()     // 最近成交
client.NewHistoricalTradesService() // 历史成交
client.NewListPricesService()       // 价格列表
client.NewListBookTickersService()  // 订单簿 ticker
client.NewListPriceChangeStatsService() // 价格变动统计
client.NewExchangeInfoService()     // 交易所信息
client.NewAveragePriceService()     // 平均价格

// 账户
client.NewGetAccountService()      // 获取账户
client.NewGetBalanceService()      // 获取余额

// 订单
client.NewCreateOrderService()     // 创建订单
client.NewGetOrderService()        // 查询订单
client.NewListOrdersService()      // 订单列表
client.NewListOpenOrdersService()  // 开放订单
client.NewCancelOrderService()     // 取消订单
client.NewCancelOpenOrdersService() // 取消所有开放订单
client.NewCreateOCOService()       // 创建 OCO 订单
client.NewListOpenOcoService()     // 查询开放 OCO
client.NewCancelOCOService()       // 取消 OCO

// WebSocket
client.NewStartUserStreamService()    // 开启用户数据流
client.NewKeepaliveUserStreamService() // 续期用户数据流
client.NewCloseUserStreamService()    // 关闭用户数据流
```

---

## 2. 常量与枚举

### SideType（买卖方向）

```go
binance.SideTypeBuy  // 买入
binance.SideTypeSell // 卖出
```

### OrderType（订单类型）

```go
binance.OrderTypeLimit           // 限价单
binance.OrderTypeMarket         // 市价单
binance.OrderTypeStopLoss        // 止损单
binance.OrderTypeStopLossLimit   // 止损限价单
binance.OrderTypeTakeProfit      // 止盈单
binance.OrderTypeTakeProfitLimit  // 止盈限价单
binance.OrderTypeLimitMaker      // 只做 maker
```

### TimeInForceType（有效期）

```go
binance.TimeInForceTypeGTC // Good Till Cancel（一直有效直到取消）
binance.TimeInForceTypeIOC // Immediate Or Cancel（立即成交或取消）
binance.TimeInForceTypeFOK // Fill Or Kill（全部成交或取消）
```

### OrderStatusType（订单状态）

```go
binance.OrderStatusTypeNew            // 新订单
binance.OrderStatusTypePartiallyFilled // 部分成交
binance.OrderStatusTypeFilled          // 完全成交
binance.OrderStatusTypeCanceled        // 已取消
binance.OrderStatusTypeRejected        // 已拒绝
binance.OrderStatusTypeExpired         // 已过期
```

### NewOrderRespType（订单响应类型）

```go
binance.NewOrderRespTypeACK    // 仅返回 ACK
binance.NewOrderRespTypeRESULT // 返回完整结果
```

### SelfTradePreventionMode（自成交预防）

```go
binance.SelfTradePreventionModeNone      // 无自成交保护
binance.SelfTradePreventionModeExpireTaker  // Expire Taker
binance.SelfTradePreventionModeExpireBoth   // Expire Both
binance.SelfTradePreventionModeExpireMaker  // Expire Maker
```

### CancelReplaceMode（取消替换模式）

```go
binance.CancelReplaceModeStopOnFailure // 取消失败则停止
```

---

## 3. 行情数据

### 3.1 K线 (Klines)

**服务**: `KlinesService`

```go
klines, err := client.NewKlinesService().
    Symbol("BTCUSDT").
    Interval("1m").    // 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
    Limit(100).        // 默认 500，最大 1500
    StartTime(1700000000000).
    EndTime(1700100000000).
    Do(ctx)
```

**响应**: `[]*Kline`

```go
for _, k := range klines {
    fmt.Printf("K线: 开=%s 高=%s 低=%s 收=%s 时间=%d\n",
        k.Open, k.High, k.Low, k.Close, k.OpenTime)
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `OpenTime` | int64 | 开盘时间（毫秒） |
| `Open` | string | 开盘价 |
| `High` | string | 最高价 |
| `Low` | string | 最低价 |
| `Close` | string | 收盘价 |
| `Volume` | string | 成交量 |
| `CloseTime` | int64 | 收盘时间（毫秒） |
| `QuoteAssetVolume` | string | 成交额 |
| `TradeNum` | int64 | 成交笔数 |
| `TakerBuyBaseAssetVolume` | string | 主动买入成交量 |
| `TakerBuyQuoteAssetVolume` | string | 主动买入成交额 |

---

### 3.2 深度数据 (Depth)

**服务**: `DepthService`

```go
depth, err := client.NewDepthService().
    Symbol("BTCUSDT").
    Limit(20). // 5, 10, 20, 50, 100, 500, 1000, 5000
    Do(ctx)
```

**响应**: `*DepthResponse`

```go
fmt.Println("买一:", depth.Bids[0].Price, "×", depth.Bids[0].Quantity)
fmt.Println("卖一:", depth.Asks[0].Price, "×", depth.Asks[0].Quantity)
```

**WebSocket 深度**: 见 [websocket.md](./websocket.md#深度行情-wsdepthserve)

---

### 3.3 价格列表 (Prices)

**服务**: `ListPricesService`

```go
prices, err := client.NewListPricesService().
    // Symbol("BTCUSDT") // 可选：指定交易对
    Do(ctx)

for _, p := range prices {
    fmt.Printf("%s: %s\n", p.Symbol, p.Price)
}
```

---

### 3.4 订单簿 Ticker (BookTickers)

**服务**: `ListBookTickersService`

```go
tickers, err := client.NewListBookTickersService().
    // Symbol("BTCUSDT") // 可选
    Do(ctx)

for _, t := range tickers {
    fmt.Printf("买一: %s×%s | 卖一: %s×%s\n",
        t.BidPrice, t.BidQuantity, t.AskPrice, t.AskQuantity)
}
```

---

### 3.5 价格变动统计 (PriceChangeStats)

**服务**: `ListPriceChangeStatsService`

```go
stats, err := client.NewListPriceChangeStatsService().
    Symbol("BTCUSDT").
    Do(ctx)

fmt.Printf("24h涨跌: %s (%s%%)\n", stats[0].PriceChange, stats[0].PriceChangePercent)
fmt.Printf("最高: %s 最低: %s\n", stats[0].HighPrice, stats[0].LowPrice)
fmt.Printf("成交量: %s 成交额: %s\n", stats[0].Volume, stats[0].QuoteVolume)
```

---

### 3.6 平均价格 (AveragePrice)

**服务**: `AveragePriceService`

```go
avg, err := client.NewAveragePriceService().
    Symbol("BTCUSDT").
    Do(ctx)

fmt.Printf("5分钟平均价: %s（基于 %d 分钟数据）\n", avg.Price, avg.Mins)
```

---

### 3.7 聚合交易 (AggTrades)

**服务**: `AggTradesService`

```go
trades, err := client.NewAggTradesService().
    Symbol("BTCUSDT").
    FromID(12345).
    Limit(100).
    Do(ctx)
```

**响应**: `[]*AggTrade`

---

### 3.8 最近成交 (RecentTrades)

**服务**: `RecentTradesService`

```go
trades, err := client.NewRecentTradesService().
    Symbol("BTCUSDT").
    Limit(100).
    Do(ctx)
```

---

### 3.9 历史成交 (HistoricalTrades)

**服务**: `HistoricalTradesService`

```go
trades, err := client.NewHistoricalTradesService().
    Symbol("BTCUSDT").
    FromID(12345).
    Limit(100).
    Do(ctx)
```

---

### 3.10 交易所信息 (ExchangeInfo)

**服务**: `ExchangeInfoService`

```go
info, err := client.NewExchangeInfoService().Do(ctx)

for _, s := range info.Symbols {
    fmt.Printf("交易对: %s, 状态: %s, 订单类型: %v\n",
        s.Symbol, s.Status, s.OrderTypes)
}

// 使用过滤器
sym, _ := client.NewExchangeInfoService().Symbol("BTCUSDT").Do(ctx)
lotSize := sym.LotSizeFilter()
priceFilter := sym.PriceFilter()
fmt.Printf("数量精度: %s~%s 步长: %s\n", lotSize.MinQuantity, lotSize.MaxQuantity, lotSize.StepSize)
fmt.Printf("价格精度: %s~%s 步长: %s\n", priceFilter.MinPrice, priceFilter.MaxPrice, priceFilter.TickSize)
```

---

## 4. 订单管理

### 4.1 创建订单 (CreateOrder)

```go
// 限价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    TimeInForce(binance.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("50000.00").
    Do(ctx)

// 市价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeMarket).
    Quantity("0.001").
    Do(ctx)

// 止损限价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeStopLossLimit).
    TimeInForce(binance.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("49000.00").
    StopPrice("49500.00").
    Do(ctx)

// 设置自定义客户端订单ID
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    Quantity("0.001").
    Price("50000.00").
    NewClientOrderID("my-order-001").
    Do(ctx)

// 测试订单（不实际下单）
err = client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    Quantity("0.001").
    Price("50000.00").
    Test(ctx)
```

**响应**: `*CreateOrderResponse`

```go
fmt.Printf("订单ID: %d, 状态: %s, 成交数量: %s\n",
    order.OrderID, order.Status, order.ExecutedQuantity)
```

---

### 4.2 创建 OCO 订单 (One-Cancels-Other)

OCO = 限价单 + 止损单，其中一个成交则另一个自动取消：

```go
resp, err := client.NewCreateOCOService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeSell). // 卖出止盈
    Quantity("0.001").
    // 限价单（止盈）
    Price("55000.00").
    LimitClientOrderID("limit-oco-001").
    // 止损单
    StopPrice("54000.00").       // 触发价
    StopLimitPrice("53500.00").   // 止损限价
    StopClientOrderID("stop-oco-001").
    StopLimitTimeInForce(binance.TimeInForceTypeGTC).
    Do(ctx)

fmt.Printf("OCO订单列表ID: %d\n", resp.OrderListID)
```

---

### 4.3 查询订单

```go
// 查询单个订单
order, err := client.NewGetOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    Do(ctx)

// 按客户端订单ID查询
order, err := client.NewGetOrderService().
    Symbol("BTCUSDT").
    OrigClientOrderID("my-order-001").
    Do(ctx)

// 查询所有订单
orders, err := client.NewListOrdersService().
    Symbol("BTCUSDT").
    Limit(100).
    Do(ctx)

// 查询开放订单
orders, err := client.NewListOpenOrdersService().
    Symbol("BTCUSDT").
    Do(ctx)

// 查询开放 OCO
ocos, err := client.NewListOpenOcoService().Do(ctx)
```

**Order 响应字段**:

```go
order.OrderID       // 订单ID
order.ClientOrderID // 客户端订单ID
order.Symbol        // 交易对
order.Side          // 买卖方向
order.Type          // 订单类型
order.Price         // 订单价格
order.OrigQuantity // 原始数量
order.ExecutedQuantity // 已成交数量
order.Status        // 订单状态
order.TimeInForce   // 有效期
order.StopPrice     // 止损价
order.Time          // 创建时间
order.UpdateTime    // 更新时间
order.IsIsolated    // 是否是逐仓
```

---

### 4.4 取消订单

```go
// 取消单个订单
resp, err := client.NewCancelOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    Do(ctx)

// 按客户端订单ID取消
resp, err := client.NewCancelOrderService().
    Symbol("BTCUSDT").
    OrigClientOrderID("my-order-001").
    Do(ctx)

// 取消所有开放订单
resp, err := client.NewCancelOpenOrdersService().
    Symbol("BTCUSDT").
    Do(ctx)
```

---

### 4.5 取消并替换订单 (Cancel-Replace)

```go
resp, err := client.NewCancelReplaceOrderService().
    Symbol("BTCUSDT").
    CancelReplaceMode(binance.CancelReplaceModeStopOnFailure).
    CancelOrderID(123456).
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    TimeInForce(binance.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("51000.00").
    Do(ctx)

if resp.CancelResult == "SUCCESS" {
    fmt.Printf("新订单ID: %d\n", resp.NewOrderResponse.OrderID)
}
```

---

### 4.6 订单链式方法速查

```go
CreateOrderService 所有方法：
  .Symbol(symbol string) *CreateOrderService
  .Side(side SideType) *CreateOrderService
  .Type(orderType OrderType) *CreateOrderService
  .TimeInForce(timeInForce TimeInForceType) *CreateOrderService
  .Quantity(q string) *CreateOrderService
  .QuoteOrderQty(q string) *CreateOrderService         // 市价单按成交额
  .Price(p string) *CreateOrderService
  .NewClientOrderID(id string) *CreateOrderService
  .StopPrice(p string) *CreateOrderService
  .TrailingDelta(d string) *CreateOrderService
  .IcebergQuantity(q string) *CreateOrderService
  .NewOrderRespType(t NewOrderRespType) *CreateOrderService
  .SelfTradePreventionMode(m SelfTradePreventionMode) *CreateOrderService
  .Do(ctx, opts...) (*CreateOrderResponse, error)
  .Test(ctx, opts...) error
```

---

## 5. 账户操作

### 5.1 获取账户 (GetAccount)

```go
account, err := client.NewGetAccountService().
    Do(ctx)

fmt.Printf("手续费率 - Maker: %d, Taker: %d\n",
    account.MakerCommission, account.TakerCommission)
fmt.Printf("可交易: %v, 可充值: %v, 可提现: %v\n",
    account.CanTrade, account.CanDeposit, account.CanWithdraw)

for _, b := range account.Balances {
    if b.Free != "0" || b.Locked != "0" {
        fmt.Printf("%s: 可用=%s 锁定=%s\n", b.Asset, b.Free, b.Locked)
    }
}
```

**响应**: `*Account`

| 字段 | 类型 | 说明 |
|------|------|------|
| `MakerCommission` | int64 | Maker 手续费率 (bps) |
| `TakerCommission` | int64 | Taker 手续费率 (bps) |
| `BuyerCommission` | int64 | 买入手续费率 |
| `SellerCommission` | int64 | 卖出手续费率 |
| `CanTrade` | bool | 是否可交易 |
| `CanDeposit` | bool | 是否可充值 |
| `CanWithdraw` | bool | 可否提现 |
| `UpdateTime` | uint64 | 更新时间 |
| `AccountType` | string | 账户类型 |
| `Balances` | []Balance | 余额列表 |

---

### 5.2 获取余额 (GetBalance)

```go
balances, err := client.NewGetBalanceService().Do(ctx)

for _, b := range balances {
    fmt.Printf("%s: 可用=%s 保证金=%s\n", b.Asset, b.AvailableBalance, b.CrossWalletBalance)
}
```

**响应**: `[]*Balance`

| 字段 | 类型 | 说明 |
|------|------|------|
| `Asset` | string | 资产名称 |
| `AvailableBalance` | string | 可用余额 |
| `CrossWalletBalance` | string | 全仓保证金余额 |
| `CrossUnPnl` | string | 全仓未实现盈亏 |
| `Locked` | string | 锁定金额 |
| `UpdateTime` | int64 | 更新时间 |

---

### 5.3 账户快照 (GetAccountSnapshot)

```go
snapshot, err := client.NewGetAccountSnapshotService().
    Type("SPOT"). // SPOT, MARGIN, FUTURES
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(7).
    Do(ctx)
```

---

## 6. WebSocket

> 详细 WebSocket 文档见 [websocket.md](./websocket.md)

### 6.1 深度行情

```go
doneC, stopC, err := binance.WsDepthServe("BTCUSDT",
    func(event *binance.WsDepthEvent) {
        fmt.Println("买一:", event.Bids[0].Price)
        fmt.Println("卖一:", event.Asks[0].Price)
    },
    func(err error) { fmt.Println("错误:", err) },
)
```

### 6.2 K线行情

```go
doneC, _, err := binance.WsKlineServe("BTCUSDT", "1m",
    func(event *binance.WsKlineEvent) {
        k := event.Kline
        fmt.Printf("K线: %s~%s O=%.2f H=%.2f L=%.2f C=%.2f\n",
            k.Symbol, k.Interval, k.Open, k.High, k.Low, k.Close)
    }, errHandler,
)
```

### 6.3 成交记录

```go
doneC, _, err := binance.WsTradeServe("BTCUSDT",
    func(event *binance.WsTradeEvent) {
        fmt.Printf("成交: %s×%s 方向=%s\n",
            event.Price, event.Quantity, event.IsBuyerMaker)
    }, errHandler,
)
```

### 6.4 用户数据流

```go
listenKey, _ := client.NewStartUserStreamService().Do(ctx)

doneC, stopC, err := binance.WsUserDataServe(listenKey,
    func(event *binance.WsUserDataEvent) {
        switch e := event.Data.(type) {
        case *binance.WsOutboundAccountPosition:
            for _, b := range e.Balances {
                fmt.Printf("%s: %s\n", b.Asset, b.Free)
            }
        case *binance.WsExecutionReport:
            fmt.Printf("订单更新: %d %s %s\n", e.OrderID, e.Side, e.Status)
        case *binance.WsBalanceUpdate:
            fmt.Printf("余额变动: %s %s\n", e.Asset, e.Change)
        }
    },
    func(err error) { fmt.Println("WS错误:", err) },
)
defer func() { stopC <- struct{}{} }()

// 续期（每30分钟）
ticker := time.NewTicker(25 * time.Minute)
go func() {
    for range ticker.C {
        client.NewKeepaliveUserStreamService().ListenKey(listenKey).Do(context.Background())
    }
}()
```

---

## 7. 类型索引

### Struct 一览

| 类型名 | 文件 | 说明 |
|--------|------|------|
| `Client` | `client.go` | 主客户端 |
| `CreateOrderService` | `order_service.go` | 创建订单 |
| `GetOrderService` | `order_service.go` | 查询订单 |
| `ListOrdersService` | `order_service.go` | 订单列表 |
| `ListOpenOrdersService` | `order_service.go` | 开放订单 |
| `CancelOrderService` | `order_service.go` | 取消订单 |
| `CancelOpenOrdersService` | `order_service.go` | 取消全部开放订单 |
| `CancelReplaceOrderService` | `order_service.go` | 取消并替换 |
| `CreateOCOService` | `order_service.go` | 创建OCO |
| `CancelOCOService` | `order_service.go` | 取消OCO |
| `ListOpenOcoService` | `order_service.go` | 查询开放OCO |
| `GetAccountService` | `account_service.go` | 账户信息 |
| `GetBalanceService` | `account_service.go` | 余额 |
| `GetAccountSnapshotService` | `account_service.go` | 账户快照 |
| `GetAPIKeyPermission` | `account_service.go` | API密钥权限 |
| `KlinesService` | `kline_service.go` | K线 |
| `DepthService` | `depth_service.go` | 深度 |
| `ListPricesService` | `ticker_service.go` | 价格列表 |
| `ListBookTickersService` | `ticker_service.go` | 订单簿ticker |
| `ListPriceChangeStatsService` | `ticker_service.go` | 价格变动统计 |
| `AveragePriceService` | `ticker_service.go` | 平均价格 |
| `ListSymbolTickerService` | `ticker_service.go` | symbol ticker |
| `AggTradesService` | `trade_service.go` | 聚合交易 |
| `RecentTradesService` | `trade_service.go` | 最近成交 |
| `HistoricalTradesService` | `trade_service.go` | 历史成交 |
| `ListTradesService` | `trade_service.go` | 交易列表 |
| `ExchangeInfoService` | `exchange_info_service.go` | 交易所信息 |
| `StartUserStreamService` | `user_stream_service.go` | 开启用户流 |
| `KeepaliveUserStreamService` | `user_stream_service.go` | 续期用户流 |
| `CloseUserStreamService` | `user_stream_service.go` | 关闭用户流 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `CreateOrderResponse` | 创建订单响应 |
| `CreateOCOResponse` | 创建OCO响应 |
| `Order` | 订单详情 |
| `Oco` | OCO订单 |
| `Account` | 账户信息 |
| `Balance` | 余额 |
| `Snapshot` | 账户快照 |
| `APIKeyPermission` | API密钥权限 |
| `Kline` | K线数据 |
| `DepthResponse` | 深度响应 |
| `BookTicker` | 订单簿ticker |
| `SymbolPrice` | 交易对价格 |
| `PriceChangeStats` | 价格变动统计 |
| `AvgPrice` | 平均价格 |
| `SymbolTicker` | ticker数据 |
| `Trade` | 成交记录 |
| `TradeV3` | 成交记录V3 |
| `AggTrade` | 聚合交易 |
| `ExchangeInfo` | 交易所信息 |
| `LotSizeFilter` | 批量过滤器 |
| `PriceFilter` | 价格过滤器 |
| `PercentPriceBySideFilter` | 百分比价格过滤器 |
| `NotionalFilter` | 名义价值过滤器 |

### WebSocket Event Struct 一览

| 类型名 | 说明 |
|--------|------|
| `WsPartialDepthEvent` | 局部深度事件 |
| `WsDepthEvent` | 深度事件 |
| `WsKlineEvent` | K线事件 |
| `WsAggTradeEvent` | 聚合交易事件 |
| `WsTradeEvent` | 成交事件 |
| `WsUserDataEvent` | 用户数据事件 |
| `WsMarketStatEvent` | 市场统计事件 |
| `WsBookTickerEvent` | 订单簿ticker事件 |
| `WsAnnouncementEvent` | 公告事件 |

### Const 一览

| 类型 | 值 |
|------|-----|
| `SideType` | `Buy`, `Sell` |
| `OrderType` | `Limit`, `Market`, `StopLoss`, `StopLossLimit`, `TakeProfit`, `TakeProfitLimit`, `LimitMaker` |
| `TimeInForceType` | `GTC`, `IOC`, `FOK` |
| `NewOrderRespType` | `ACK`, `RESULT` |
| `OrderStatusType` | `New`, `PartiallyFilled`, `Filled`, `Canceled`, `Rejected`, `Expired` |
| `SelfTradePreventionMode` | `None`, `ExpireTaker`, `ExpireBoth`, `ExpireMaker` |
| `CancelReplaceMode` | `StopOnFailure` |
