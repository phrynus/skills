# 期权交易模块 (options)

> **模块路径**: `github.com/adshao/go-binance/v2/options`
> **客户端**: `Client`（通过 `binance.NewOptionsClient()` 创建）
> **端点**: `https://eapi.binance.com`
> **相关文档**: [SKILL.md](../SKILL.md) | [websocket.md](./websocket.md) | [common.md](./common.md)

期权是一种在未来某一特定时间以特定价格买入或卖出标的资产的合约。

---

## 目录

1. [客户端](#1-客户端)
2. [常量与枚举](#2-常量与枚举)
3. [行情数据](#3-行情数据)
4. [订单管理](#4-订单管理)
5. [持仓与行权](#5-持仓与行权)
6. [账户与资金](#6-账户与资金)
7. [类型索引](#7-类型索引)

---

## 1. 客户端

### 初始化

```go
import "github.com/adshao/go-binance/v2/options"

client := binance.NewOptionsClient(apiKey, secretKey)
```

### 客户端方法一览

```go
// 行情
client.NewExchangeInfoService()          // 交易所信息
client.NewDepthService()               // 期权合约深度
client.NewTradesService()              // 最新成交
client.NewHistoricalTradesService()    // 历史成交
client.NewKlinesService()              // K线
client.NewMarkService()                // 标记价格
client.NewTickerService()             // Ticker
client.NewIndexService()              // 指数价格
client.NewExerciseHistoryService()     // 行权历史
client.NewOpenInterestService()        // 持仓量

// 账户
client.NewAccountService()             // 账户（希腊字母等）
client.NewPositionService()            // 持仓
client.NewUserTradesService()          // 用户成交
client.NewExercistRecordService()      // 行权记录
client.NewBillService()               // 资金账单
client.NewIncomeDownloadIdService()   // 收益下载ID
client.NewIncomeDownloadLinkService()  // 收益下载链接

// 订单
client.NewCreateOrderService()          // 创建订单
client.NewCreateBatchOrdersService()   // 批量下单
client.NewGetOrderService()            // 查询订单
client.NewCancelOrderService()         // 取消订单
client.NewCancelBatchOrdersService()   // 批量取消
client.NewCancelAllOpenOrdersService() // 取消全部开放订单
client.NewCancelAllOpenOrdersByUnderlyingService() // 按标的取消
client.NewListOpenOrdersService()     // 开放订单
client.NewHistoryOrdersService()      // 历史订单

// WebSocket
client.NewStartUserStreamService()
client.NewKeepaliveUserStreamService()
client.NewCloseUserStreamService()
```

---

## 2. 常量与枚举

### SideType

```go
options.SideTypeBuy  // 买入期权（开多仓）
options.SideTypeSell // 卖出期权（开空仓）
```

### OptionSideType

```go
options.OptionSideTypeCall // 看涨期权
options.OptionSideTypePut  // 看跌期权
```

### PositionSideType

```go
options.PositionSideTypeBoth  // 双向
options.PositionSideTypeLong  // 多头
options.PositionSideTypeShort // 空头
```

### OrderType

```go
options.OrderTypeLimit           // 限价单
options.OrderTypeMarket          // 市价单
options.OrderTypeStop           // 止损限价
options.OrderTypeStopMarket     // 止损市价
options.OrderTypeTakeProfit     // 止盈限价
options.OrderTypeTakeProfitMarket // 止盈市价
options.OrderTypeTrailingStopMarket // 跟踪止损
```

### TimeInForceType

```go
options.TimeInForceTypeGTC // Good Till Cancel
options.TimeInForceTypeIOC // Immediate Or Cancel
options.TimeInForceTypeFOK // Fill Or Kill
options.TimeInForceTypeGTX // Good Till Crossing
```

### NewOrderRespType

```go
options.NewOrderRespTypeACK    // ACK
options.NewOrderRespTypeRESULT // RESULT
```

---

## 3. 行情数据

### 3.1 期权合约信息 (ExchangeInfo)

```go
info, err := client.NewExchangeInfoService().Do(ctx)
for _, s := range info {
    fmt.Printf("合约: %s 标的: %s 行权价: %s 到期: %d\n",
        s.Symbol, s.Underlying, s.StrikePrice, s.ExpiryDate)
}
```

### 3.2 深度 (Depth)

```go
depth, err := client.NewDepthService().
    Symbol("BTC-220624-40000-C"). // 格式: BTC-YYYYMMDD-行权价-C/P
    Limit(20).
    Do(ctx)
```

### 3.3 最新成交 (Trades)

```go
trades, err := client.NewTradesService().
    Symbol("BTC-220624-40000-C").
    Limit(100).
    Do(ctx)
```

### 3.4 K线

```go
klines, err := client.NewKlinesService().
    Symbol("BTC-220624-40000-C").
    Interval("1m").
    Limit(100).
    Do(ctx)
```

### 3.5 标记价格 (Mark)

```go
mark, err := client.NewMarkService().
    Symbol("BTC-220624-40000-C").
    Do(ctx)
fmt.Printf("标记价格: %s, 波动率: %s\n", mark.Price, mark.MarkPrice)
```

### 3.6 Ticker

```go
ticker, err := client.NewTickerService().
    Symbol("BTC-220624-40000-C").
    Do(ctx)
fmt.Printf("最新价: %s, 24h涨跌: %s%%\n", ticker.LastPrice, ticker.PriceChangePercent)
```

### 3.7 指数价格 (Index)

```go
index, err := client.NewIndexService().
    Symbol("BTCUSDT").
    Do(ctx)
fmt.Printf("指数价格: %s\n", index.Price)
```

### 3.8 行权历史 (ExerciseHistory)

```go
history, err := client.NewExerciseHistoryService().
    Symbol("BTC-220624-40000-C").
    Limit(100).
    Do(ctx)
```

### 3.9 持仓量 (OpenInterest)

```go
oi, err := client.NewOpenInterestService().
    Symbol("BTC-220624-40000-C").
    Do(ctx)
fmt.Printf("持仓量: %s\n", oi.OpenInterest)
```

---

## 4. 订单管理

### 4.1 创建订单

期权订单的数量为合约张数，价格为期权费（以标的资产计价）。

```go
// 限价单（买入看涨期权）
order, err := client.NewCreateOrderService().
    Symbol("BTC-220624-40000-C").
    Side(options.SideTypeBuy).
    Type(options.OrderTypeLimit).
    Quantity("1"). // 张数
    Price("0.05"). // 期权费（BTC计价）
    Do(ctx)

// 市价单（卖出看跌期权）
order, err := client.NewCreateOrderService().
    Symbol("BTC-220624-40000-C").
    Side(options.SideTypeSell).
    Type(options.OrderTypeMarket).
    Quantity("1").
    Do(ctx)

// 止损限价单
order, err := client.NewCreateOrderService().
    Symbol("BTC-220624-40000-C").
    Side(options.SideTypeBuy).
    Type(options.OrderTypeStop).
    Quantity("1").
    Price("0.08").
    StopPrice("0.10").
    Do(ctx)

// 设置自定义客户端订单ID
order, err := client.NewCreateOrderService().
    Symbol("BTC-220624-40000-C").
    Side(options.SideTypeBuy).
    Type(options.OrderTypeLimit).
    Quantity("1").
    Price("0.05").
    ClientOrderId("my-option-order-001").
    Do(ctx)
```

**CreateOrderService 链式方法**:

```go
.Symbol(symbol string)
.Side(side SideType)
.Type(orderType OrderType)
.TimeInForce(t TimeInForceType)
.Quantity(q string)
.ReduceOnly(b bool)
.PostOnly(b bool)               // 仅Maker
.Price(p string)
.ClientOrderId(id string)
.NewOrderResponseType(t NewOrderRespType)
.IsMmp(b bool)                  // Market Maker Protection
.Do(ctx) (*Order, error)
```

---

### 4.2 批量下单 (CreateBatchOrders)

```go
orders := []*options.CreateOrderService{
    client.NewCreateOrderService().
        Symbol("BTC-220624-40000-C").
        Side(options.SideTypeBuy).
        Type(options.OrderTypeLimit).
        Quantity("1").
        Price("0.05"),
    client.NewCreateOrderService().
        Symbol("BTC-220624-41000-C").
        Side(options.SideTypeBuy).
        Type(options.OrderTypeLimit).
        Quantity("1").
        Price("0.03"),
}
resp, err := client.NewCreateBatchOrdersService(orders).Do(ctx)
```

---

### 4.3 查询订单

```go
// 查询单个订单
order, err := client.NewGetOrderService().
    Symbol("BTC-220624-40000-C").
    OrderID(123456789).
    Do(ctx)

// 按客户端订单ID查询
order, err := client.NewGetOrderService().
    Symbol("BTC-220624-40000-C").
    ClientOrderId("my-option-order-001").
    Do(ctx)

// 查询开放订单
orders, err := client.NewListOpenOrdersService().
    Symbol("BTC-220624-40000-C").
    Do(ctx)

// 查询历史订单
orders, err := client.NewHistoryOrdersService().
    Symbol("BTC-220624-40000-C").
    Limit(100).
    Do(ctx)
```

**Order 响应字段**:

```go
order.OrderId
order.Symbol
order.Price      // 期权费
order.Quantity   // 张数
order.ExecutedQty
order.Fee
order.Side
order.Type
order.TimeInForce
order.ReduceOnly
order.PostOnly
order.Status
order.AvgPrice
order.ClientOrderId
order.CreateTime
order.UpdateTime
order.RateLimitOrder10s // 10秒内订单限制
order.RateLimitOrder1m  // 1分钟内订单限制
order.Source
order.PriceScale       // 价格精度
order.QuantityScale     // 数量精度
order.OptionSide       // Call/Put
```

---

### 4.4 取消订单

```go
// 取消单个
order, err := client.NewCancelOrderService().
    Symbol("BTC-220624-40000-C").
    OrderID(123456789).
    Do(ctx)

// 批量取消
resp, err := client.NewCancelBatchOrdersService().
    Symbol("BTC-220624-40000-C").
    OrderIds([]int64{123, 456}).
    Do(ctx)

// 取消全部开放订单
resp, err := client.NewCancelAllOpenOrdersService().
    Symbol("BTC-220624-40000-C").
    Do(ctx)

// 按标的取消（取消该标的下的所有期权合约订单）
resp, err := client.NewCancelAllOpenOrdersByUnderlyingService().
    Underlying("BTCUSDT").
    Do(ctx)
```

---

## 5. 持仓与行权

### 5.1 持仓 (Position)

```go
// 获取所有持仓
positions, err := client.NewPositionService().Do(ctx)

// 获取指定合约持仓
positions, err := client.NewPositionService().
    Symbol("BTC-220624-40000-C").
    Do(ctx)

for _, p := range positions {
    fmt.Printf("合约: %s 方向: %s 数量: %s 可平数量: %s 标记价值: %s 盈亏: %s 行权价: %s 到期: %d\n",
        p.Symbol, p.Side, p.Quantity, p.ReducibleQty,
        p.MarkValue, p.UnrealizedPNL, p.StrikePrice, p.ExpiryDate)
}
```

### 5.2 行权记录 (ExerciseRecord)

```go
records, err := client.NewExercistRecordService().
    Symbol("BTC-220624-40000-C").
    Limit(100).
    Do(ctx)

for _, r := range records {
    fmt.Printf("行权: %s 数量: %s 行权价: %s 标记价: %s 手续费: %s 时间: %d\n",
        r.Symbol, r.Quantity, r.ExercisePrice, r.MarkPrice,
        r.Fee, r.CreateDate)
}
```

---

## 6. 账户与资金

### 6.1 账户 (Account)

期权账户包含希腊字母（Delta, Gamma, Theta, Vega）等风险指标：

```go
account, err := client.NewAccountService().Do(ctx)
for _, a := range account.Asset {
    fmt.Printf("%s: 余额=%s 保证金余额=%s 可用=%s 未实现盈亏=%s\n",
        a.Asset, a.Equity, a.MarginBalance, a.Available, a.UnrealizedPNL)
}
for _, g := range account.Greek {
    fmt.Printf("标的: %s Delta=%s Gamma=%s Theta=%s Vega=%s\n",
        g.Underlying, g.Delta, g.Gamma, g.Theta, g.Vega)
}
fmt.Printf("风险等级: %s\n", account.RiskLevel)
```

### 6.2 用户成交 (UserTrades)

```go
trades, err := client.NewUserTradesService().
    Symbol("BTC-220624-40000-C").
    Limit(100).
    Do(ctx)

for _, t := range trades {
    fmt.Printf("成交: ID=%d 价格=%s 数量=%s 手续费=%s 方向=%s 时间=%d\n",
        t.TradeId, t.Price, t.Quantity, t.Fee, t.Side, t.Time)
}
```

### 6.3 资金账单 (Bill)

```go
bills, err := client.NewBillService().
    Currency("BTC").
    Limit(100).
    Do(ctx)

for _, b := range bills {
    fmt.Printf("账单: %s 类型=%s 金额=%s 时间=%d\n",
        b.Asset, b.Type, b.Amount, b.CreateDate)
}
```

### 6.4 收益下载 (Income Download)

```go
// 获取下载ID
downloadId, err := client.NewIncomeDownloadIdService().
    StartTime(1700000000000).
    EndTime(1700100000000).
    Do(ctx)

// 获取下载链接
link, err := client.NewIncomeDownloadLinkService().
    DownloadId(downloadId.DownloadId).
    Do(ctx)
fmt.Printf("下载链接: %s 过期时间: %d\n", link.Url, link.ExpirationTimestamp)
```

---

## 7. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `Client` | 期权客户端 |
| `ExchangeInfoService` | 交易所信息 |
| `DepthService` | 深度 |
| `TradesService` | 最新成交 |
| `HistoricalTradesService` | 历史成交 |
| `KlinesService` | K线 |
| `MarkService` | 标记价格 |
| `TickerService` | Ticker |
| `IndexService` | 指数价格 |
| `ExerciseHistoryService` | 行权历史 |
| `OpenInterestService` | 持仓量 |
| `AccountService` | 账户 |
| `PositionService` | 持仓 |
| `UserTradesService` | 用户成交 |
| `ExercistRecordService` | 行权记录 |
| `BillService` | 资金账单 |
| `IncomeDownloadIdService` | 收益下载ID |
| `IncomeDownloadLinkService` | 收益下载链接 |
| `CreateOrderService` | 创建订单 |
| `CreateBatchOrdersService` | 批量下单 |
| `GetOrderService` | 查询订单 |
| `CancelOrderService` | 取消订单 |
| `CancelBatchOrdersService` | 批量取消 |
| `CancelAllOpenOrdersService` | 取消全部 |
| `CancelAllOpenOrdersByUnderlyingService` | 按标的取消 |
| `ListOpenOrdersService` | 开放订单 |
| `HistoryOrdersService` | 历史订单 |
| `StartUserStreamService` | 用户数据流 |
| `KeepaliveUserStreamService` | 续期 |
| `CloseUserStreamService` | 关闭 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `Account` | 账户（含希腊字母）|
| `Asset` | 账户资产 |
| `Greek` | 希腊字母（Delta/Gamma/Theta/Vega）|
| `Position` | 持仓 |
| `Order` | 订单 |
| `LastTrade` | 最近成交 |
| `UserTrade` | 用户成交 |
| `ExerciseRecord` | 行权记录 |
| `Bill` | 资金账单 |
| `IncomeDownloadId` | 下载ID |
| `IncomeDownloadLink` | 下载链接 |
| `DepthResponse` | 深度响应 |
| `MarkPrice` | 标记价格 |
| `SymbolTicker` | Ticker |
| `IndexPrice` | 指数价格 |
| `ExerciseHistory` | 行权历史 |
| `OpenInterest` | 持仓量 |

### Const 一览

| 类型 | 值 |
|------|-----|
| `SideType` | `Buy`, `Sell` |
| `OptionSideType` | `Call`, `Put` |
| `PositionSideType` | `Both`, `Long`, `Short` |
| `OrderType` | `Limit`, `Market`, `Stop`, `StopMarket`, `TakeProfit`, `TakeProfitMarket`, `TrailingStopMarket` |
| `TimeInForceType` | `GTC`, `IOC`, `FOK`, `GTX` |
| `NewOrderRespType` | `ACK`, `RESULT` |

### 期权合约命名规则

```
BTC-220624-40000-C
 │       │      │  └── C=Call (看涨), P=Put (看跌)
 │       │         └── 行权价格
 │       └── 到期日 (YYYYMMDD)
 └── 标的资产 (BTCUSDT)
```

### 希腊字母说明

| 字母 | 名称 | 说明 |
|------|------|------|
| `Delta` | 德尔塔 | 期权价格对标的资产价格的敏感度 |
| `Gamma` | 伽马 | Delta 对标的资产价格的敏感度 |
| `Theta` | 西塔 | 期权价格对时间的衰减 |
| `Vega` | 维加 | 期权价格对波动率的敏感度 |
