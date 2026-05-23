# 币本位合约模块 (delivery)

> **模块路径**: `github.com/adshao/go-binance/v2/delivery`
> **客户端**: `Client`（通过 `binance.NewDeliveryClient()` 创建）
> **端点**: `https://dapi.binance.com`
> **相关文档**: [SKILL.md](../SKILL.md) | [websocket.md](./websocket.md) | [common.md](./common.md) | [futures.md](./futures.md)

币本位合约（Coin-M）与 USDT-M 永续合约的主要区别：
- 保证金为对应的币种（如 BTC），而非 USDT
- 结算货币为对应的币种
- 支持交割合约（CURRENT_QUARTER, NEXT_QUARTER）
- 支持双向持仓（Hedge Mode）

---

## 目录

1. [客户端](#1-客户端)
2. [常量与枚举](#2-常量与枚举)
3. [行情数据](#3-行情数据)
4. [订单管理](#4-订单管理)
5. [持仓与保证金](#5-持仓与保证金)
6. [账户](#6-账户)
7. [类型索引](#7-类型索引)

---

## 1. 客户端

### 初始化

```go
import "github.com/adshao/go-binance/v2/delivery"

client := binance.NewDeliveryClient(apiKey, secretKey)
delivery.UseTestnet = true // 测试网
```

### 客户端方法一览

```go
// 行情
client.NewKlinesService()                  // K线
client.NewListPricesService()             // 价格列表
client.NewListBookTickersService()        // 订单簿 ticker
client.NewListPriceChangeStatsService()   // 价格变动统计
client.NewListLiquidationOrdersService()   // 强平订单
client.NewExchangeInfoService()           // 交易所信息
client.NewGetFundingRateService()         // 资金费率
client.NewFundingRateService()            // 历史资金费率

// 账户
client.NewGetAccountService()             // 账户
client.NewGetBalanceService()             // 余额
client.NewGetPositionRiskService()        // 持仓风险
client.NewChangeLeverageService()         // 修改杠杆
client.NewChangeMarginTypeService()       // 变更保证金模式
client.NewUpdatePositionMarginService()   // 调整保证金
client.NewChangePositionModeService()     // 双向持仓模式
client.NewGetPositionModeService()        // 获取持仓模式

// 订单
client.NewCreateOrderService()            // 创建订单
client.NewGetOrderService()              // 查询订单
client.NewListOpenOrdersService()         // 开放订单
client.NewListOrdersService()            // 订单列表
client.NewCancelOrderService()           // 取消订单
client.NewCancelAllOpenOrdersService()   // 取消全部开放订单

// WebSocket
client.NewStartUserStreamService()        // 用户数据流
client.NewKeepaliveUserStreamService()
client.NewCloseUserStreamService()
```

---

## 2. 常量与枚举

### SideType

```go
delivery.SideTypeBuy  // 买入
delivery.SideTypeSell // 卖出
```

### PositionSideType

```go
delivery.PositionSideTypeBoth  // 单向持仓
delivery.PositionSideTypeLong  // 双向持仓-做多
delivery.PositionSideTypeShort // 双向持仓-做空
```

### OrderType

```go
delivery.OrderTypeLimit           // 限价单
delivery.OrderTypeMarket          // 市价单
delivery.OrderTypeStop            // 止损限价
delivery.OrderTypeStopMarket      // 止损市价
delivery.OrderTypeTakeProfit      // 止盈限价
delivery.OrderTypeTakeProfitMarket // 止盈市价
delivery.OrderTypeTrailingStopMarket // 跟踪止损
```

### TimeInForceType

```go
delivery.TimeInForceTypeGTC // Good Till Cancel
delivery.TimeInForceTypeIOC // Immediate Or Cancel
delivery.TimeInForceTypeFOK // Fill Or Kill
delivery.TimeInForceTypeGTX // Good Till Crossing
```

### MarginType

```go
delivery.MarginTypeIsolated  // 逐仓
delivery.MarginTypeCrossed   // 全仓
```

### WorkingType

```go
delivery.WorkingTypeMarkPrice     // 标记价格
delivery.WorkingTypeContractPrice // 合约价格
```

### NewOrderRespType

```go
delivery.NewOrderRespTypeACK    // 仅 ACK
delivery.NewOrderRespTypeRESULT  // 完整结果
delivery.NewOrderRespTypeFULL    // 全部信息
```

---

## 3. 行情数据

### 3.1 K线

```go
klines, err := client.NewKlinesService().
    Symbol("BTCUSD_201225"). // 币本位格式: BTCUSD_YYYYMMDD
    Interval("1m").
    Limit(100).
    Do(ctx)
```

### 3.2 价格列表

```go
prices, err := client.NewListPricesService().
    Do(ctx)
```

### 3.3 订单簿 Ticker

```go
tickers, err := client.NewListBookTickersService().
    Symbol("BTCUSD_201225").
    Do(ctx)
```

### 3.4 价格变动统计

```go
stats, err := client.NewListPriceChangeStatsService().
    Symbol("BTCUSD_201225").
    Do(ctx)
```

### 3.5 强平订单

```go
orders, err := client.NewListLiquidationOrdersService().
    Symbol("BTCUSD_201225").
    Limit(100).
    Do(ctx)
```

### 3.6 交易所信息

```go
info, err := client.NewExchangeInfoService().Do(ctx)
for _, s := range info.Symbols {
    fmt.Printf("%s: 合约类型=%s 状态=%s\n", s.Symbol, s.ContractType, s.Status)
}
```

### 3.7 资金费率

```go
// 获取资金费率信息
info, err := client.NewGetFundingRateService().
    Symbol("BTCUSD_PERP"). // 永续: _PERP
    Do(ctx)

// 获取历史资金费率
rates, err := client.NewFundingRateService().
    Symbol("BTCUSD_PERP").
    Limit(10).
    Do(ctx)
```

---

## 4. 订单管理

### 4.1 创建订单

币本位合约使用 `BTC`, `ETH` 等币种作为保证金，订单的 quantity 为合约张数。

```go
// 限价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeBuy).
    PositionSide(delivery.PositionSideTypeLong).
    Type(delivery.OrderTypeLimit).
    TimeInForce(delivery.TimeInForceTypeGTC).
    Quantity("1"). // 合约张数
    Price("20000.00").
    Do(ctx)

// 市价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeBuy).
    PositionSide(delivery.PositionSideTypeLong).
    Type(delivery.OrderTypeMarket).
    Quantity("1").
    Do(ctx)

// 双向持仓（做空）
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeSell).
    PositionSide(delivery.PositionSideTypeShort).
    Type(delivery.OrderTypeLimit).
    TimeInForce(delivery.TimeInForceTypeGTC).
    Quantity("1").
    Price("25000.00").
    Do(ctx)

// 止损市价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeSell).
    PositionSide(delivery.PositionSideTypeLong).
    Type(delivery.OrderTypeStopMarket).
    Quantity("1").
    StopPrice("19000.00").
    WorkingType(delivery.WorkingTypeMarkPrice).
    Do(ctx)

// 止盈市价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeSell).
    PositionSide(delivery.PositionSideTypeLong).
    Type(delivery.OrderTypeTakeProfitMarket).
    Quantity("1").
    StopPrice("30000.00").
    WorkingType(delivery.WorkingTypeMarkPrice).
    Do(ctx)

// 跟踪止损
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeSell).
    PositionSide(delivery.PositionSideTypeLong).
    Type(delivery.OrderTypeTrailingStopMarket).
    Quantity("1").
    CallbackRate("0.5").
    ActivationPrice("22000.00").
    Do(ctx)

// 减少-only（只平仓）
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeSell).
    PositionSide(delivery.PositionSideTypeLong).
    Type(delivery.OrderTypeLimit).
    TimeInForce(delivery.TimeInForceTypeGTC).
    Quantity("1").
    Price("25000.00").
    ReduceOnly(true).
    Do(ctx)

// 设置止损限价触发
order, err := client.NewCreateOrderService().
    Symbol("BTCUSD_201225").
    Side(delivery.SideTypeSell).
    PositionSide(delivery.PositionSideTypeLong).
    Type(delivery.OrderTypeStop).
    Quantity("1").
    Price("19500.00").         // 触发后挂出的限价
    StopPrice("19000.00").     // 触发价格
    WorkingType(delivery.WorkingTypeMarkPrice).
    Do(ctx)
```

**CreateOrderService 链式方法**:

```go
.Symbol(symbol string)
.Side(side SideType)
.PositionSide(side PositionSideType)
.Type(orderType OrderType)
.TimeInForce(t TimeInForceType)
.Quantity(q string)
.ReduceOnly(b bool)
.Price(p string)
.NewClientOrderID(id string)
.StopPrice(p string)
.WorkingType(w WorkingType)
.ActivationPrice(p string)
.CallbackRate(r string)
.PriceProtect(b bool)
.NewOrderResponseType(t NewOrderRespType)
.ClosePosition(b bool)
.Do(ctx) (*CreateOrderResponse, error)
```

---

### 4.2 查询订单

```go
// 查询单个订单
order, err := client.NewGetOrderService().
    Symbol("BTCUSD_201225").
    OrderID(123456789).
    Do(ctx)

// 查询开放订单
orders, err := client.NewListOpenOrdersService().
    Symbol("BTCUSD_201225").
    Do(ctx)

// 查询所有订单
orders, err := client.NewListOrdersService().
    Symbol("BTCUSD_201225").
    Limit(100).
    Do(ctx)
```

**Order 响应字段**:

```go
order.OrderID, order.ClientOrderID, order.Symbol, order.Pair
order.Side, order.PositionSide, order.Type, order.OrigType
order.Price, order.OrigQuantity, order.ExecutedQuantity
order.AvgPrice, order.CumBase                  // CumBase: 成交的合约张数
order.Status, order.TimeInForce, order.StopPrice
order.ClosePosition, order.WorkingType, order.PriceProtect
order.Time, order.UpdateTime
order.ReduceOnly, order.ActivatePrice, order.PriceRate
```

---

### 4.3 取消订单

```go
// 取消单个
resp, err := client.NewCancelOrderService().
    Symbol("BTCUSD_201225").
    OrderID(123456789).
    Do(ctx)

// 取消所有开放订单
err = client.NewCancelAllOpenOrdersService().
    Symbol("BTCUSD_201225").
    Do(ctx)
```

---

## 5. 持仓与保证金

### 5.1 修改杠杆

```go
result, err := client.NewChangeLeverageService().
    Symbol("BTCUSD_201225").
    Leverage(10).
    Do(ctx)
```

### 5.2 变更保证金模式

```go
// 逐仓
err = client.NewChangeMarginTypeService().
    Symbol("BTCUSD_201225").
    MarginType(delivery.MarginTypeIsolated).
    Do(ctx)

// 全仓
err = client.NewChangeMarginTypeService().
    Symbol("BTCUSD_201225").
    MarginType(delivery.MarginTypeCrossed).
    Do(ctx)
```

### 5.3 调整保证金

```go
err = client.NewUpdatePositionMarginService().
    Symbol("BTCUSD_201225").
    PositionSide(delivery.PositionSideTypeLong).
    Amount("0.001"). // 调整的 BTC 数量
    Type(1).        // 1=增加, 2=减少
    Do(ctx)
```

### 5.4 双向持仓模式

```go
// 开启双向持仓（Hedge Mode）
err = client.NewChangePositionModeService().
    DualSide(true).
    Do(ctx)

// 查询
mode, err := client.NewGetPositionModeService().
    Do(ctx)
fmt.Printf("双向持仓: %v\n", mode.DualSidePosition)
```

---

## 6. 账户

### 6.1 获取账户

```go
account, err := client.NewGetAccountService().Do(ctx)
for _, a := range account.Assets {
    fmt.Printf("%s: 余额=%s 未实现盈亏=%s 保证金=%s\n",
        a.Asset, a.WalletBalance, a.UnrealizedProfit, a.MarginBalance)
}
for _, p := range account.Positions {
    fmt.Printf("持仓: %s 数量=%s 方向=%s 盈亏=%s 强平价=%s\n",
        p.Symbol, p.PositionAmt, p.PositionSide,
        p.UnrealizedProfit, p.EntryPrice)
}
```

### 6.2 获取余额

```go
balances, err := client.NewGetBalanceService().Do(ctx)
for _, b := range balances {
    if b.Balance != "0" {
        fmt.Printf("%s: 余额=%s 可提=%s 保证金=%s\n",
            b.Asset, b.Balance, b.WithdrawAvailable, b.CrossWalletBalance)
    }
}
```

### 6.3 获取持仓风险

```go
positions, err := client.NewGetPositionRiskService().
    // Symbol("BTCUSD_201225"). // 可选，不填则返回全部
    Do(ctx)
for _, p := range positions {
    fmt.Printf("持仓: %s 数量=%s 方向=%s 盈亏=%s 强平价=%s 杠杆=%s\n",
        p.Symbol, p.PositionAmt, p.PositionSide,
        p.UnRealizedProfit, p.LiquidationPrice, p.MarginType)
}
```

---

## 7. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `Client` | 币本位合约客户端 |
| `PingService` | Ping |
| `ServerTimeService` | 服务器时间 |
| `KlinesService` | K线 |
| `ListPricesService` | 价格列表 |
| `ListBookTickersService` | 订单簿 ticker |
| `ListPriceChangeStatsService` | 价格变动统计 |
| `ListLiquidationOrdersService` | 强平订单 |
| `ExchangeInfoService` | 交易所信息 |
| `GetFundingRateService` | 资金费率信息 |
| `FundingRateService` | 历史资金费率 |
| `CreateOrderService` | 创建订单 |
| `GetOrderService` | 查询订单 |
| `ListOpenOrdersService` | 开放订单 |
| `ListOrdersService` | 订单列表 |
| `CancelOrderService` | 取消订单 |
| `CancelAllOpenOrdersService` | 取消全部 |
| `ChangeLeverageService` | 修改杠杆 |
| `ChangeMarginTypeService` | 变更保证金模式 |
| `UpdatePositionMarginService` | 调整保证金 |
| `ChangePositionModeService` | 双向持仓模式 |
| `GetPositionModeService` | 获取持仓模式 |
| `GetAccountService` | 账户 |
| `GetBalanceService` | 余额 |
| `GetPositionRiskService` | 持仓风险 |
| `StartUserStreamService` | 用户数据流 |
| `KeepaliveUserStreamService` | 续期 |
| `CloseUserStreamService` | 关闭 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `CreateOrderResponse` | 创建订单响应 |
| `Order` | 订单详情 |
| `LiquidationOrder` | 强平订单 |
| `Account` | 账户 |
| `AccountAsset` | 账户资产 |
| `AccountPosition` | 账户持仓 |
| `Balance` | 余额 |
| `SymbolLeverage` | 杠杆信息 |
| `PositionMode` | 持仓模式 |
| `FundingRate` | 资金费率 |
| `ExchangeInfo` | 交易所信息 |
| `LotSizeFilter` | 批量过滤器 |
| `PriceFilter` | 价格过滤器 |
| `PriceChangeStats` | 价格变动统计 |
| `Kline` | K线 |
| `BookTicker` | 订单簿 ticker |
| `SymbolPrice` | 交易对价格 |
| `MarkPriceIndex` | 标记价格/指数价格 |

### Const 一览

| 类型 | 值 |
|------|-----|
| `SideType` | `Buy`, `Sell` |
| `PositionSideType` | `Both`, `Long`, `Short` |
| `OrderType` | `Limit`, `Market`, `Stop`, `StopMarket`, `TakeProfit`, `TakeProfitMarket`, `TrailingStopMarket` |
| `TimeInForceType` | `GTC`, `IOC`, `FOK`, `GTX` |
| `MarginType` | `Isolated`, `Crossed` |
| `WorkingType` | `MarkPrice`, `ContractPrice` |
| `NewOrderRespType` | `ACK`, `RESULT`, `FULL` |
| `ContractType` | `Perpetual`, `CurrentQuarter`, `NextQuarter` |

### 与 USDT-M 合约对比

| 功能 | USDT-M (futures) | 币本位 (delivery) |
|------|------------------|-------------------|
| 保证金 | USDT | 对应币种（BTC、ETH）|
| 客户端 | `binance.NewFuturesClient()` | `binance.NewDeliveryClient()` |
| 交易对格式 | `BTCUSDT` | `BTCUSD_201225` |
| 端点 | `fapi.binance.com` | `dapi.binance.com` |
| 双向持仓 | 支持 | 支持 |
| 强平订单 | 支持 | 支持 |
| 算法订单 | 支持（完整） | 支持（基础）|
| 多资产模式 | 支持 | 不支持 |
