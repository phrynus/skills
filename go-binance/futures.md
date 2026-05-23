# USDT-M 永续合约模块 (futures)

> **模块路径**: `github.com/adshao/go-binance/v2/futures`
> **客户端**: `Client`（通过 `binance.NewFuturesClient()` 创建）
> **相关文档**: [SKILL.md](../SKILL.md) | [websocket.md](./websocket.md) | [common.md](./common.md) | [spot.md](./spot.md)

---

## 目录

1. [客户端](#1-客户端)
2. [常量与枚举](#2-常量与枚举)
3. [行情数据](#3-行情数据)
4. [订单管理](#4-订单管理)
5. [持仓与保证金](#5-持仓与保证金)
6. [账户与收益](#6-账户与收益)
7. [算法订单](#7-算法订单)
8. [WebSocket](#8-websocket)
9. [类型索引](#9-类型索引)

---

## 1. 客户端

### 初始化

```go
import "github.com/adshao/go-binance/v2/futures"

client := binance.NewFuturesClient(apiKey, secretKey)
client.Debug = true
futures.UseTestnet = true // 测试网
```

### 客户端方法一览

```go
// 行情
client.NewPingService()                    // Ping
client.NewServerTimeService()             // 服务器时间
client.NewKlinesService()                 // K线
client.NewContinuousKlinesService()       // 连续合约K线
client.NewIndexPriceKlinesService()       // 指数价格K线
client.NewMarkPriceKlinesService()        // 标记价格K线
client.NewDepthService()                  // 深度
client.NewAggTradesService()              // 聚合交易
client.NewRecentTradesService()           // 最近成交
client.NewHistoricalTradesService()       // 历史成交
client.NewListPricesService()            // 价格列表
client.NewListBookTickersService()       // 订单簿ticker
client.NewListPriceChangeStatsService()  // 价格变动统计
client.NewPremiumIndexService()          // 资金费率基础指数
client.NewPremiumIndexKlinesService()    // 资金费率K线
client.NewFundingRateService()           // 历史资金费率
client.NewFundingRateInfoService()       // 资金费率信息
client.NewGetOpenInterestService()       // 持仓量
client.NewOpenInterestStatisticsService() // 持仓量统计
client.NewLongShortRatioService()        // 多空人数比
client.NewTopLongShortAccountRatioService() // 大户多空比
client.NewTopLongShortPositionRatioService() // 大户持仓比
client.NewTakerLongShortRatioService()    // Taker多空比
client.NewExchangeInfoService()          // 交易所信息
client.NewDeliveryPriceService()         // 交割价格

// 账户与持仓
client.NewGetAccountService()              // 账户
client.NewGetBalanceService()             // 余额
client.NewGetPositionRiskService()         // 持仓风险
client.NewGetPositionRiskV3Service()      // 持仓风险V3
client.NewGetAccountV3Service()           // 账户V3
client.NewGetIncomeHistoryService()        // 收益历史
client.NewGetPositionMarginHistoryService() // 调整保证金历史
client.NewCommissionRateService()         // 手续费率
client.NewRebateNewUserService()          // 返佣（新用户）
client.NewGetFeeBurnService()             // 手续费率抵扣
client.NewFeeBurnService()                 // 设置手续费率抵扣
client.NewAccountConfigService()          // 账户配置
client.NewSymbolConfigService()           // 交易对配置

// 持仓管理
client.NewChangeLeverageService()          // 修改杠杆
client.NewGetLeverageBracketService()     // 杠杆档位
client.NewChangeMarginTypeService()        // 变更保证金模式
client.NewUpdatePositionMarginService()   // 调整逐仓保证金
client.NewChangePositionModeService()     // 双向持仓模式
client.NewGetPositionModeService()        // 获取持仓模式
client.NewChangeMultiAssetModeService()   // 多资产模式
client.NewGetMultiAssetModeService()      // 获取多资产模式

// 订单
client.NewCreateOrderService()             // 创建订单
client.NewModifyOrderService()             // 修改订单
client.NewCreateBatchOrdersService()      // 批量下单
client.NewModifyBatchOrdersService()       // 批量修改订单
client.NewGetOrderService()               // 查询订单
client.NewListOpenOrdersService()          // 开放订单
client.NewListOrdersService()             // 订单列表
client.NewCancelOrderService()            // 取消订单
client.NewCancelAllOpenOrdersService()    // 取消全部开放订单
client.NewCancelMultipleOrdersService()    // 批量取消订单
client.NewGetOpenOrderService()           // 查询单个开放订单
client.NewListLiquidationOrdersService()   // 强平订单
client.NewListUserLiquidationOrdersService() // 用户强平订单
client.NewRebateNewUserService()          // 返佣

// 算法订单
client.NewCreateAlgoOrderService()         // 创建算法订单
client.NewCancelAlgoOrderService()        // 取消算法订单
client.NewCancelAllAlgoOpenOrdersService() // 取消全部算法订单
client.NewGetAlgoOrderService()           // 查询算法订单
client.NewListOpenAlgoOrdersService()     // 开放算法订单
client.NewListAllAlgoOrdersService()      // 全部算法订单

// WebSocket
client.NewStartUserStreamService()    // 开启用户数据流
client.NewKeepaliveUserStreamService() // 续期
client.NewCloseUserStreamService()    // 关闭
```

---

## 2. 常量与枚举

### SideType

```go
futures.SideTypeBuy  // 买入/做多
futures.SideTypeSell // 卖出/做空
```

### PositionSideType

```go
futures.PositionSideTypeBoth  // 单向持仓（默认）
futures.PositionSideTypeLong  // 双向持仓-做多
futures.PositionSideTypeShort // 双向持仓-做空
```

### OrderType

```go
futures.OrderTypeLimit           // 限价单
futures.OrderTypeMarket          // 市价单
futures.OrderTypeStop            // 止损单
futures.OrderTypeStopMarket      // 止损市价单
futures.OrderTypeTakeProfit      // 止盈单
futures.OrderTypeTakeProfitMarket // 止盈市价单
futures.OrderTypeTrailingStopMarket // 跟踪止损市价单
futures.OrderTypeLiquidation     // 强平单
```

### TimeInForceType

```go
futures.TimeInForceTypeGTC    // Good Till Cancel
futures.TimeInForceTypeGTD    // Good Till Date
futures.TimeInForceTypeGTEGTC // Good Till Crossing（仅 Maker）
futures.TimeInForceTypeIOC    // Immediate Or Cancel
futures.TimeInForceTypeFOK    // Fill Or Kill
futures.TimeInForceTypeGTX    // Good Till Crossing
```

### OrderStatusType

```go
futures.OrderStatusTypeNew            // 新订单
futures.OrderStatusTypePartiallyFilled // 部分成交
futures.OrderStatusTypeFilled          // 完全成交
futures.OrderStatusTypeCanceled        // 已取消
futures.OrderStatusTypeRejected        // 已拒绝
futures.OrderStatusTypeExpired         // 已过期
futures.OrderStatusTypeNewInsurance    // 保险基金
futures.OrderStatusTypeNewADL          // ADL自动减仓
```

### MarginType

```go
futures.MarginTypeIsolated  // 逐仓
futures.MarginTypeCrossed   // 全仓
```

### PriceMatchType（对手价相关）

```go
futures.PriceMatchTypeOpponent   // 对手价
futures.PriceMatchTypeOpponent5  // 对手价5档
futures.PriceMatchTypeOpponent10 // 对手价10档
futures.PriceMatchTypeOpponent20 // 对手价20档
futures.PriceMatchTypeQueue      // 队列价
futures.PriceMatchTypeQueue5     // 队列价5档
futures.PriceMatchTypeQueue10    // 队列价10档
futures.PriceMatchTypeQueue20    // 队列价20档
futures.PriceMatchTypeNone      // 无
```

### WorkingType

```go
futures.WorkingTypeMarkPrice     // 标记价格触发
futures.WorkingTypeContractPrice // 合约价格触发
```

### SelfTradePreventionMode

```go
futures.SelfTradePreventionModeNone
futures.SelfTradePreventionModeExpireTaker
futures.SelfTradePreventionModeExpireBoth
futures.SelfTradePreventionModeExpireMaker
```

### UserDataEventType

```go
futures.UserDataEventTypeListenKeyExpired        // 会话过期
futures.UserDataEventTypeMarginCall             // 强平通知
futures.UserDataEventTypeAccountUpdate           // 账户更新
futures.UserDataEventTypeOrderTradeUpdate        // 订单/交易更新
futures.UserDataEventTypeAccountConfigUpdate     // 账户配置更新
futures.UserDataEventTypeTradeLite              // 简化成交
futures.UserDataEventTypeConditionalOrderTriggerReject // 条件订单触发拒绝
futures.UserDataEventTypeAlgoUpdate             // 算法订单更新
```

### ForceOrderCloseType

```go
futures.ForceOrderCloseTypeLiquidation // 强平
futures.ForceOrderCloseTypeADL         // ADL
```

---

## 3. 行情数据

### 3.1 K线 (Klines)

```go
klines, err := client.NewKlinesService().
    Symbol("BTCUSDT").
    Interval("1m").
    Limit(100).
    Do(ctx)
```

### 3.2 深度 (Depth)

```go
depth, err := client.NewDepthService().
    Symbol("BTCUSDT").
    Limit(20).
    Do(ctx)
```

### 3.3 聚合交易 (AggTrades)

```go
trades, err := client.NewAggTradesService().
    Symbol("BTCUSDT").
    FromID(12345).
    Limit(100).
    Do(ctx)
```

### 3.4 订单簿 Ticker

```go
tickers, err := client.NewListBookTickersService().
    Symbol("BTCUSDT").
    Do(ctx)
```

### 3.5 价格变动统计

```go
stats, err := client.NewListPriceChangeStatsService().
    Symbol("BTCUSDT").
    Do(ctx)
```

### 3.6 持仓量 (OpenInterest)

```go
oi, err := client.NewGetOpenInterestService().
    Symbol("BTCUSDT").
    Do(ctx)
fmt.Printf("持仓量: %s\n", oi.OpenInterest)
```

### 3.7 资金费率 (FundingRate)

```go
fr, err := client.NewFundingRateService().
    Symbol("BTCUSDT").
    Limit(10).
    Do(ctx)
for _, f := range fr {
    fmt.Printf("资金费率: %s 时间: %d\n", f.FundingRate, f.FundingTime)
}
```

### 3.8 标记价格 (MarkPrice Klines)

```go
klines, err := client.NewMarkPriceKlinesService().
    Symbol("BTCUSDT").
    Interval("1m").
    Limit(100).
    Do(ctx)
```

### 3.9 连续合约 K线

```go
klines, err := client.NewContinuousKlinesService().
    Pair("BTCUSDT").       // 如 "BTCUSDT"
    ContractType("PERPETUAL"). // PERPETUAL, CURRENT_QUARTER, NEXT_QUARTER
    Interval("1h").
    Limit(100).
    Do(ctx)
```

### 3.10 多空比 (LongShortRatio)

```go
ratio, err := client.NewLongShortRatioService().
    Symbol("BTCUSDT").
    Period("1h").  // 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d
    Limit(10).
    Do(ctx)
for _, r := range ratio {
    fmt.Printf("多空比: %s (多:%s 空:%s)\n", r.LongShortRatio, r.LongAccount, r.ShortAccount)
}
```

### 3.11 交易所信息 (ExchangeInfo)

```go
info, err := client.NewExchangeInfoService().Do(ctx)
for _, s := range info.Symbols {
    fmt.Printf("%s: 状态=%s 合约类型=%s\n", s.Symbol, s.Status, s.ContractType)
}
```

---

## 4. 订单管理

### 4.1 创建订单 (CreateOrder)

```go
// 限价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeBuy).
    PositionSide(futures.PositionSideTypeLong).  // 双向持仓模式必填
    Type(futures.OrderTypeLimit).
    TimeInForce(futures.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("50000.00").
    Do(ctx)

// 市价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeBuy).
    PositionSide(futures.PositionSideTypeLong).
    Type(futures.OrderTypeMarket).
    Quantity("0.001").
    Do(ctx)

// 双向持仓下单（做空）
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeShort).
    Type(futures.OrderTypeLimit).
    TimeInForce(futures.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("55000.00").
    Do(ctx)

// 止损市价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeLong).
    Type(futures.OrderTypeStopMarket).
    Quantity("0.001").
    StopPrice("49000.00").
    WorkingType(futures.WorkingTypeMarkPrice).
    Do(ctx)

// 止盈市价单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeLong).
    Type(futures.OrderTypeTakeProfitMarket).
    Quantity("0.001").
    StopPrice("60000.00").
    WorkingType(futures.WorkingTypeMarkPrice).
    Do(ctx)

// 跟踪止损
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeLong).
    Type(futures.OrderTypeTrailingStopMarket).
    Quantity("0.001").
    CallbackRate("0.5").   // 回调率 0.1%~5%
    ActivationPrice("52000.00").
    Do(ctx)

// 减少-only（只平仓不开新仓）
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeLong).
    Type(futures.OrderTypeLimit).
    TimeInForce(futures.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("55000.00").
    ReduceOnly(true).
    Do(ctx)

// 止盈止损联动
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(futures.SideTypeBuy).
    Type(futures.OrderTypeStop).
    Quantity("0.001").
    Price("48000.00").
    StopPrice("49000.00").
    WorkingType(futures.WorkingTypeMarkPrice).
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
.PriceProtect(b bool)
.PriceMatch(m PriceMatchType)
.ClosePosition(b bool)
.ActivationPrice(p string)
.CallbackRate(r string)
.NewOrderResponseType(t NewOrderRespType)
.SelfTradePreventionMode(m SelfTradePreventionMode)
.GoodTillDate(t int64)
.Do(ctx) (*CreateOrderResponse, error)
```

---

### 4.2 修改订单 (ModifyOrder)

```go
resp, err := client.NewModifyOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    Side(futures.SideTypeBuy).
    Quantity("0.002").
    Price("51000.00").
    Do(ctx)
```

---

### 4.3 批量下单 (CreateBatchOrders)

```go
orders := []*futures.CreateOrderService{
    client.NewCreateOrderService().
        Symbol("BTCUSDT").
        Side(futures.SideTypeBuy).
        PositionSide(futures.PositionSideTypeLong).
        Type(futures.OrderTypeLimit).
        TimeInForce(futures.TimeInForceTypeGTC).
        Quantity("0.001").
        Price("50000.00"),
    client.NewCreateOrderService().
        Symbol("ETHUSDT").
        Side(futures.SideTypeBuy).
        PositionSide(futures.PositionSideTypeLong).
        Type(futures.OrderTypeLimit).
        TimeInForce(futures.TimeInForceTypeGTC).
        Quantity("0.01").
        Price("3000.00"),
}

resp, err := client.NewCreateBatchOrdersService(orders).Do(ctx)
for _, o := range resp.Orders {
    fmt.Printf("订单ID: %d, 状态: %s\n", o.OrderID, o.Status)
}
```

---

### 4.4 查询订单

```go
// 查询单个订单
order, err := client.NewGetOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    Do(ctx)

// 查询开放订单
orders, err := client.NewListOpenOrdersService().
    Symbol("BTCUSDT").
    Do(ctx)

// 查询所有订单
orders, err := client.NewListOrdersService().
    Symbol("BTCUSDT").
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)

// 查询单个开放订单
order, err := client.NewGetOpenOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    Do(ctx)
```

---

### 4.5 取消订单

```go
// 取消单个
resp, err := client.NewCancelOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    Do(ctx)

// 取消所有开放订单
err = client.NewCancelAllOpenOrdersService().
    Symbol("BTCUSDT").
    Do(ctx)

// 批量取消
results, err := client.NewCancelMultipleOrdersService().
    Symbol("BTCUSDT").
    OrderIDList([]int64{123, 456}).
    Do(ctx)
```

**Order 响应字段**:

```go
order.OrderID
order.ClientOrderID
order.Symbol
order.Side
order.PositionSide
order.Type
order.Price
order.OrigQuantity
order.ExecutedQuantity
order.AvgPrice
order.Status
order.TimeInForce
order.StopPrice
order.ClosePosition
order.WorkingType
order.PriceProtect
order.PriceMatch
order.SelfTradePreventionMode
order.UpdateTime
```

---

## 5. 持仓与保证金

### 5.1 修改杠杆 (ChangeLeverage)

```go
// 切换到 10x 杠杆
result, err := client.NewChangeLeverageService().
    Symbol("BTCUSDT").
    Leverage(10).
    Do(ctx)
fmt.Printf("杠杆: %d\n", result.Leverage)
```

### 5.2 变更保证金模式 (ChangeMarginType)

```go
// 切换到逐仓
err = client.NewChangeMarginTypeService().
    Symbol("BTCUSDT").
    MarginType(futures.MarginTypeIsolated).
    Do(ctx)

// 切换到全仓
err = client.NewChangeMarginTypeService().
    Symbol("BTCUSDT").
    MarginType(futures.MarginTypeCrossed).
    Do(ctx)
```

### 5.3 调整逐仓保证金 (UpdatePositionMargin)

```go
// 增加保证金（逐仓）
err = client.NewUpdatePositionMarginService().
    Symbol("BTCUSDT").
    PositionSide(futures.PositionSideTypeLong).
    Amount("0.01"). // 增加金额
    Type(1).        // 1=增加, 2=减少
    Do(ctx)
```

### 5.4 双向持仓模式 (Position Mode)

```go
// 开启双向持仓（ Hedge Mode）
err = client.NewChangePositionModeService().
    DualSide(true).
    Do(ctx)

// 查询当前持仓模式
mode, err := client.NewGetPositionModeService().
    Do(ctx)
fmt.Printf("双向持仓: %v\n", mode.DualSidePosition)
```

### 5.5 多资产模式 (Multi-Asset Mode)

```go
// 开启多资产模式
err = client.NewChangeMultiAssetModeService().
    MultiAssetsMargin(true).
    Do(ctx)

// 查询
mode, err := client.NewGetMultiAssetModeService().
    Do(ctx)
```

### 5.6 杠杆档位 (Leverage Bracket)

```go
brackets, err := client.NewGetLeverageBracketService().
    Symbol("BTCUSDT").
    Do(ctx)
for _, b := range brackets {
    fmt.Printf("档位 %d: 杠杆 %d~%d, 最大名义价值: %s\n",
        b.NotionalCap, b.MinLeverage, b.MaxLeverage, b.NotionalCap)
}
```

---

## 6. 账户与收益

### 6.1 获取账户 (GetAccount)

```go
account, err := client.NewGetAccountService().Do(ctx)
fmt.Printf("保证金余额: %s\n", account.TotalWalletBalance)
fmt.Printf("未实现盈亏: %s\n", account.TotalUnrealizedProfit)
for _, p := range account.Positions {
    fmt.Printf("持仓: %s 数量: %s 方向: %s 盈亏: %s\n",
        p.Symbol, p.PositionAmt, p.PositionSide, p.UnrealizedProfit)
}
```

**Account 响应字段**:

```go
Account{
    Assets: []*AccountAsset{
        Asset, InitialMargin, MaintMargin, MarginBalance,
        MaxWithdrawAmount, OpenOrderInitialMargin,
        PositionInitialMargin, UnrealizedProfit, WalletBalance,
        CrossWalletBalance, CrossUnPnl, AvailableBalance, UpdateTime
    }
    FeeTier: int                    // 手续费率等级
    CanTrade, CanDeposit, CanWithdraw, MultiAssetsMargin: bool
    TotalInitialMargin, TotalMaintMargin, TotalWalletBalance: string
    TotalUnrealizedProfit, TotalMarginBalance: string
    TotalPositionInitialMargin, TotalOpenOrderInitialMargin: string
    TotalCrossWalletBalance, TotalCrossUnPnl: string
    Positions: []*AccountPosition{
        Isolated, Leverage, Symbol, PositionSide, PositionAmt,
        EntryPrice, MaxNotional, LiquidationPrice, MarkPrice,
        UnrealizedProfit, Notional, BidNotional, AskNotional,
        IsolatedWallet, UpdateTime
    }
}
```

### 6.2 获取余额 (GetBalance)

```go
balances, err := client.NewGetBalanceService().Do(ctx)
for _, b := range balances {
    if b.AvailableBalance != "0" || b.CrossWalletBalance != "0" {
        fmt.Printf("%s: 可用=%s 保证金=%s 盈亏=%s\n",
            b.Asset, b.AvailableBalance, b.CrossWalletBalance, b.CrossUnPnl)
    }
}
```

### 6.3 获取持仓风险 (GetPositionRisk)

```go
positions, err := client.NewGetPositionRiskService().
    Symbol("BTCUSDT").
    Do(ctx)

for _, p := range positions {
    fmt.Printf("持仓: %s 数量=%s 方向=%s 盈亏=%s 强平价=%s 杠杆=%s\n",
        p.Symbol, p.PositionAmt, p.PositionSide, p.UnRealizedProfit,
        p.LiquidationPrice, p.MarginType)
}
```

### 6.4 收益历史 (GetIncomeHistory)

```go
history, err := client.NewGetIncomeHistoryService().
    Symbol("BTCUSDT").
    IncomeType("TRANSFER").  // 可选: TRANSFER, WELCOME_BONUS, REALIZED_PNL, COMMISSION, INSURANCE_CLEAR, ADL, LIQUIDATION_REJECT
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)
for _, h := range history {
    fmt.Printf("收益: %s 类型: %s 时间: %d\n", h.Income, h.IncomeType, h.Time)
}
```

### 6.5 调整保证金历史 (GetPositionMarginHistory)

```go
history, err := client.NewGetPositionMarginHistoryService().
    Symbol("BTCUSDT").
    Limit(10).
    Do(ctx)
```

### 6.6 手续费率 (CommissionRate)

```go
fee, err := client.NewCommissionRateService().
    Symbol("BTCUSDT").
    Do(ctx)
fmt.Printf("Maker: %s, Taker: %s\n", fee.MakerCommissionRate, fee.TakerCommissionRate)
```

### 6.7 账户配置 (AccountConfig)

```msg
// 设置账户配置
err = client.NewAccountConfigService().
    MultiAssetsMargin(true).
    Do(ctx)
```

---

## 7. 算法订单

### 7.1 创建算法订单 (CreateAlgoOrder)

```go
// 止损单
algo, err := client.NewCreateAlgoOrderService().
    AlgoType(futures.OrderAlgoTypeConditional). // 算法类型
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeLong).
    OrderType(futures.AlgoOrderTypeStop).       // STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET, TRAILING_STOP_MARKET
    Quantity("0.001").
    Price("49000.00").
    StopPrice("49500.00").
    WorkingType(futures.WorkingTypeMarkPrice).
    Do(ctx)

// 止盈止损市价单
algo, err := client.NewCreateAlgoOrderService().
    AlgoType(futures.OrderAlgoTypeConditional).
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeLong).
    OrderType(futures.AlgoOrderTypeTakeProfitMarket).
    Quantity("0.001").
    StopPrice("60000.00").
    WorkingType(futures.WorkingTypeMarkPrice).
    Do(ctx)

// 跟踪止损
algo, err := client.NewCreateAlgoOrderService().
    AlgoType(futures.OrderAlgoTypeConditional).
    Symbol("BTCUSDT").
    Side(futures.SideTypeSell).
    PositionSide(futures.PositionSideTypeLong).
    OrderType(futures.AlgoOrderTypeTrailingStopMarket).
    Quantity("0.001").
    CallbackRate("0.5").
    ActivationPrice("52000.00").
    Do(ctx)
```

### 7.2 取消算法订单 (CancelAlgoOrder)

```go
resp, err := client.NewCancelAlgoOrderService().
    AlgoID(123456).
    Do(ctx)
```

### 7.3 查询算法订单

```go
// 查询单个
algo, err := client.NewGetAlgoOrderService().
    AlgoID(123456).
    Do(ctx)

// 查询所有开放算法订单
algos, err := client.NewListOpenAlgoOrdersService().
    Symbol("BTCUSDT").
    Do(ctx)

// 查询全部算法订单历史
algos, err := client.NewListAllAlgoOrdersService().
    Symbol("BTCUSDT").
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)
```

### 7.4 取消全部开放算法订单

```go
err = client.NewCancelAllAlgoOpenOrdersService().
    Symbol("BTCUSDT").
    Do(ctx)
```

### 7.5 算法订单类型速查

| `AlgoOrderType` | 说明 | 触发方式 |
|-----------------|------|----------|
| `STOP` | 止损限价单 | 价格触发 |
| `STOP_MARKET` | 止损市价单 | 价格触发 |
| `TAKE_PROFIT` | 止盈限价单 | 价格触发 |
| `TAKE_PROFIT_MARKET` | 止盈市价单 | 价格触发 |
| `TRAILING_STOP_MARKET` | 跟踪止损市价单 | 回调率触发 |

---

## 8. WebSocket

> 详细 WebSocket 文档见 [websocket.md](./websocket.md)

### 8.1 深度行情

```go
doneC, stopC, err := futures.WsDepthServe("btcusdt",
    func(event *futures.WsDepthEvent) {
        fmt.Println("买一:", event.Bids[0].Price)
    }, errHandler,
)
```

### 8.2 K线

```go
doneC, _, err := futures.WsKlineServe("btcusdt", "1m",
    func(event *futures.WsKlineEvent) {
        k := event.Kline
        fmt.Printf("K线: C=%.2f V=%.2f\n", k.Close, k.Volume)
    }, errHandler,
)
```

### 8.3 标记价格

```go
doneC, _, err := futures.WsMarkPriceServe("btcusdt",
    func(event *futures.WsMarkPriceEvent) {
        fmt.Printf("标记价格: %s 资金费率: %s\n", event.MarkPrice, event.FundingRate)
    }, errHandler,
)
```

### 8.4 用户数据流

```go
listenKey, _ := client.NewStartUserStreamService().Do(ctx)

doneC, stopC, err := futures.WsUserDataServe(listenKey,
    func(event *futures.WsUserDataEvent) {
        switch e := event.Data.(type) {
        case *futures.WsUserDataMarginCall:
            for _, p := range e.MarginCallPositions {
                fmt.Printf("强平预警: %s 数量=%s 保证金类型=%s\n",
                    p.Symbol, p.Amount, p.MarginType)
            }
        case *futures.WsUserDataAccountUpdate:
            for _, b := range e.AccountUpdate.Balances {
                fmt.Printf("余额: %s=%s\n", b.Asset, b.Balance)
            }
            for _, p := range e.AccountUpdate.Positions {
                fmt.Printf("持仓更新: %s=%s\n", p.Symbol, p.Amount)
            }
        case *futures.WsUserDataOrderTradeUpdate:
            o := e.OrderTradeUpdate
            fmt.Printf("订单更新: %d %s %s %s 成交量=%s\n",
                o.OrderID, o.Side, o.Type, o.Status, o.AccumulatedFilledQty)
        case *futures.WsUserDataAlgoUpdate:
            a := e.AlgoUpdate
            fmt.Printf("算法更新: AlgoID=%d 状态=%s\n", a.AlgoID, a.AlgoStatus)
        }
    },
    func(err error) { fmt.Println("WS错误:", err) },
)
```

---

## 9. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `Client` | 合约客户端 |
| `PingService` | Ping |
| `ServerTimeService` | 服务器时间 |
| `KlinesService` | K线 |
| `ContinuousKlinesService` | 连续合约K线 |
| `IndexPriceKlinesService` | 指数价格K线 |
| `MarkPriceKlinesService` | 标记价格K线 |
| `DepthService` | 深度 |
| `AggTradesService` | 聚合交易 |
| `RecentTradesService` | 最近成交 |
| `HistoricalTradesService` | 历史成交 |
| `ListPricesService` | 价格列表 |
| `ListBookTickersService` | 订单簿ticker |
| `ListPriceChangeStatsService` | 价格变动统计 |
| `PremiumIndexService` | 资金费率基础指数 |
| `FundingRateService` | 历史资金费率 |
| `GetOpenInterestService` | 持仓量 |
| `OpenInterestStatisticsService` | 持仓量统计 |
| `LongShortRatioService` | 多空人数比 |
| `ExchangeInfoService` | 交易所信息 |
| `CreateOrderService` | 创建订单 |
| `ModifyOrderService` | 修改订单 |
| `CreateBatchOrdersService` | 批量下单 |
| `ModifyBatchOrdersService` | 批量修改 |
| `GetOrderService` | 查询订单 |
| `ListOpenOrdersService` | 开放订单 |
| `ListOrdersService` | 订单列表 |
| `CancelOrderService` | 取消订单 |
| `CancelAllOpenOrdersService` | 取消全部 |
| `CancelMultipleOrdersService` | 批量取消 |
| `GetOpenOrderService` | 查询开放订单 |
| `ListLiquidationOrdersService` | 强平订单 |
| `ListUserLiquidationOrdersService` | 用户强平订单 |
| `ChangeLeverageService` | 修改杠杆 |
| `GetLeverageBracketService` | 杠杆档位 |
| `ChangeMarginTypeService` | 变更保证金模式 |
| `UpdatePositionMarginService` | 调整保证金 |
| `ChangePositionModeService` | 双向持仓模式 |
| `GetPositionModeService` | 获取持仓模式 |
| `ChangeMultiAssetModeService` | 多资产模式 |
| `GetMultiAssetModeService` | 获取多资产模式 |
| `GetAccountService` | 账户信息 |
| `GetAccountV3Service` | 账户V3 |
| `GetBalanceService` | 余额 |
| `GetPositionRiskService` | 持仓风险 |
| `GetPositionRiskV3Service` | 持仓风险V3 |
| `GetIncomeHistoryService` | 收益历史 |
| `GetPositionMarginHistoryService` | 保证金调整历史 |
| `CommissionRateService` | 手续费率 |
| `AccountConfigService` | 账户配置 |
| `SymbolConfigService` | 交易对配置 |
| `CreateAlgoOrderService` | 创建算法订单 |
| `CancelAlgoOrderService` | 取消算法订单 |
| `CancelAllAlgoOpenOrdersService` | 取消全部算法订单 |
| `GetAlgoOrderService` | 查询算法订单 |
| `ListOpenAlgoOrdersService` | 开放算法订单 |
| `ListAllAlgoOrdersService` | 全部算法订单 |
| `RebateNewUserService` | 返佣 |
| `GetFeeBurnService` | 手续费率抵扣 |
| `FeeBurnService` | 设置抵扣 |
| `StartUserStreamService` | 开启用户流 |
| `KeepaliveUserStreamService` | 续期 |
| `CloseUserStreamService` | 关闭 |
| `DeliveryPriceService` | 交割价格 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `CreateOrderResponse` | 创建订单响应 |
| `ModifyOrderResponse` | 修改订单响应 |
| `CreateBatchOrdersResponse` | 批量下单响应 |
| `Order` | 订单详情 |
| `Balance` | 余额 |
| `Account` | 账户 |
| `AccountV3` | 账户V3 |
| `AccountAsset` | 账户资产 |
| `AccountPosition` | 账户持仓 |
| `PositionRisk` | 持仓风险 |
| `PositionRiskV3` | 持仓风险V3 |
| `SymbolLeverage` | 杠杆信息 |
| `PositionMode` | 持仓模式 |
| `MultiAssetMode` | 多资产模式 |
| `IncomeHistory` | 收益历史 |
| `CommissionRate` | 手续费率 |
| `CreateAlgoOrderResp` | 创建算法订单响应 |
| `GetAlgoOrderResp` | 算法订单详情 |
| `Kline` | K线 |
| `DepthResponse` | 深度响应 |
| `BookTicker` | 订单簿ticker |
| `PriceChangeStats` | 价格变动统计 |
| `FundingRate` | 资金费率 |
| `OpenInterest` | 持仓量 |
| `LongShortRatio` | 多空比 |
| `ExchangeInfo` | 交易所信息 |
| `LotSizeFilter` | 批量过滤器 |
| `PriceFilter` | 价格过滤器 |
| `PercentPriceFilter` | 百分比价格过滤器 |
| `LiquidationOrder` | 强平订单 |
| `UserLiquidationOrder` | 用户强平订单 |
| `AggTrade` | 聚合交易 |
| `AccountTrade` | 账户成交 |

### WebSocket Event Struct 一览

| 类型名 | 说明 |
|--------|------|
| `WsAggTradeEvent` | 聚合交易事件 |
| `WsMarkPriceEvent` | 标记价格事件 |
| `WsAllMarkPriceEvent` | 所有标记价格 |
| `WsKlineEvent` | K线事件 |
| `WsContinuousKlineEvent` | 连续合约K线事件 |
| `WsMiniMarketTickerEvent` | 迷你ticker |
| `WsAllMiniMarketTickerEvent` | 所有迷你ticker |
| `WsMarketTickerEvent` | ticker事件 |
| `WsAllMarketTickerEvent` | 所有ticker |
| `WsBookTickerEvent` | 订单簿ticker |
| `WsCombinedBookTickerEvent` | 组合ticker |
| `WsLiquidationOrderEvent` | 强平事件 |
| `WsDepthEvent` | 深度事件 |
| `WsUserDataEvent` | 用户数据事件 |
| `WsUserDataMarginCall` | 强平通知 |
| `WsUserDataAccountUpdate` | 账户更新 |
| `WsUserDataOrderTradeUpdate` | 订单更新 |
| `WsUserDataAccountConfigUpdate` | 账户配置更新 |
| `WsUserDataAlgoUpdate` | 算法更新 |
| `WsAlgoUpdate` | 算法更新详情 |
| `WsBalance` | 余额 |
| `WsPosition` | 持仓 |
| `WsOrderTradeUpdate` | 订单交易更新 |
| `WsComposition` | 指数成分 |
| `WsCompositiveIndexEvent` | 综合指数事件 |
