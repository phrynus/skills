# 杠杆交易模块 (margin)

> **模块路径**: `github.com/adshao/go-binance/v2`（通过 `client.NewMarginTransferService()` 等使用）
> **相关文档**: [SKILL.md](../SKILL.md) | [spot.md](./spot.md) | [websocket.md](./websocket.md) | [common.md](./common.md)

杠杆交易允许用户借用保证金进行超额交易，放大收益和风险。支持全仓（Cross）和逐仓（Isolated）模式。

---

## 目录

1. [杠杆转账](#1-杠杆转账)
2. [杠杆借款还款](#2-杠杆借款还款)
3. [杠杆账户](#3-杠杆账户)
4. [杠杆订单](#4-杠杆订单)
5. [强平订单](#5-强平订单)
6. [用户数据流](#6-用户数据流)
7. [类型索引](#7-类型索引)

---

## 1. 杠杆转账

### 1.1 现货账户转杠杆账户 (Transfer)

```go
// 从现货转入杠杆账户
resp, err := client.NewMarginTransferService().
    Asset("USDT").
    Amount("100").
    Type(binance.MarginTransferTypeCentralizedIn). // 现货 → 杠杆
    Do(ctx)

// 从杠杆账户转出现货
resp, err := client.NewMarginTransferService().
    Asset("USDT").
    Amount("50").
    Type(binance.MarginTransferTypeCentralizedOut). // 杠杆 → 现货
    Do(ctx)
```

### 1.2 逐仓划转 (IsolatedMarginTransfer)

```go
resp, err := client.NewIsolatedMarginTransferService().
    Symbol("BTCUSDT").
    Asset("BTC").
    TransFrom(binance.AccountTypeSpot).   // 从现货
    TransTo(binance.AccountTypeMargin).     // 到逐仓
    Amount("0.01").
    Do(ctx)
```

### 1.3 借款 (Borrow)

```go
// 全仓借款
resp, err := client.NewMarginBorrowService().
    Asset("USDT").
    Amount("100").
    Do(ctx)

// 逐仓借款
resp, err := client.NewMarginBorrowService().
    Asset("USDT").
    Amount("100").
    IsIsolated(true).
    Symbol("BTCUSDT").
    Do(ctx)
```

### 1.4 还款 (Repay)

```go
// 全仓还款
resp, err := client.NewMarginRepayService().
    Asset("USDT").
    Amount("50").
    Do(ctx)

// 逐仓还款
resp, err := client.NewMarginRepayService().
    Asset("USDT").
    Amount("50").
    IsIsolated(true).
    Symbol("BTCUSDT").
    Do(ctx)
```

### 1.5 借款+还款合一 (BorrowRepay)

```go
// 直接还款（自动借款）
resp, err := client.NewMarginBorrowRepayService().
    Asset("USDT").
    Amount("50").
    Type(binance.MarginAccountBorrowRepayTypeRepay).
    Do(ctx)
```

---

## 2. 杠杆借款还款

### 2.1 借款记录 (ListMarginLoans)

```go
loans, err := client.NewListMarginLoansService().
    Asset("USDT").
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)
for _, l := range loans {
    fmt.Printf("借款: %s 数量=%s 时间=%d 状态=%s\n",
        l.Asset, l.Principal, l.Timestamp, l.Status)
}
```

### 2.2 还款记录 (ListMarginRepays)

```go
repayments, err := client.NewListMarginRepaysService().
    Asset("USDT").
    Limit(100).
    Do(ctx)
for _, r := range repayments {
    fmt.Printf("还款: %s 数量=%s 利息=%s 时间=%d\n",
        r.Asset, r.Amount, r.Interest, r.Timestamp)
}
```

### 2.3 借款/还款记录 (ListMarginBorrowRepays)

```go
records, err := client.NewListMarginBorrowRepayService().
    Asset("USDT").
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Type(binance.MarginAccountBorrowRepayTypeBorrow). // 或 Repay
    Do(ctx)
for _, r := range records {
    fmt.Printf("记录: %s 类型=%s 数量=%s 利息=%s\n",
        r.Asset, r.Type, r.Amount, r.Interest)
}
```

### 2.4 利息历史 (InterestHistory)

```go
history, err := client.NewInterestHistoryService().
    LendingType(binance.LendingTypeDaily). // Daily / Customized / Activity
    Asset("USDT").
    Limit(100).
    Do(ctx)
```

---

## 3. 杠杆账户

### 3.1 获取全仓账户 (GetMarginAccount)

```go
account, err := client.NewGetMarginAccountService().Do(ctx)
fmt.Printf("保证金水平: %s\n", account.MarginLevel)
fmt.Printf("净资产: %s BTC\n", account.TotalNetAssetOfBTC)
for _, a := range account.UserAssets {
    fmt.Printf("%s: 余额=%s 借款=%s 利息=%s 净资产=%s\n",
        a.Asset, a.Free, a.Borrowed, a.Interest, a.NetAsset)
}
```

### 3.2 获取逐仓账户 (GetIsolatedMarginAccount)

```go
account, err := client.NewGetIsolatedMarginAccountService().
    Symbols("BTCUSDT", "ETHUSDT"). // 不填则返回全部
    Do(ctx)
for _, a := range account.Assets {
    fmt.Printf("交易对: %s 保证金水平: %s 状态: %s\n",
        a.Symbol, a.MarginLevel, a.MarginLevelStatus)
    fmt.Printf("  基础资产: %s=%s 报价资产: %s=%s\n",
        a.BaseAsset.Asset, a.BaseAsset.NetAsset,
        a.QuoteAsset.Asset, a.QuoteAsset.NetAsset)
}
```

### 3.3 可借额度 (GetMaxBorrowable)

```go
max, err := client.NewGetMaxBorrowableService().
    Asset("USDT").
    Do(ctx)
fmt.Printf("最大可借: %s\n", max.Amount)
```

### 3.4 可转额度 (GetMaxTransferable)

```go
max, err := client.NewGetMaxTransferableService().
    Asset("USDT").
    Do(ctx)
fmt.Printf("最大可转: %s\n", max.Amount)
```

### 3.5 交易历史 (ListMarginTrades)

```go
trades, err := client.NewListMarginTradesService().
    Symbol("BTCUSDT").
    Limit(100).
    Do(ctx)
for _, t := range trades {
    fmt.Printf("成交: ID=%d 价格=%s 数量=%s 手续费=%s\n",
        t.ID, t.Price, t.Quantity, t.Commission)
}
```

---

## 4. 杠杆订单

杠杆订单与现货订单 API 基本相同，区别在于需要额外参数。

> 相关文档：[spot.md](./spot.md#4-订单管理)

### 4.1 创建杠杆订单

```go
// 杠杆限价单
order, err := client.NewCreateMarginOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    TimeInForce(binance.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("50000.00").
    Do(ctx)

// 杠杆市价单
order, err := client.NewCreateMarginOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeMarket).
    Quantity("0.001").
    QuoteOrderQty("100.00"). // 按成交额下单
    Do(ctx)

// 逐仓订单
order, err := client.NewCreateMarginOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    Quantity("0.001").
    Price("50000.00").
    IsIsolated(true).
    Do(ctx)

// 设置自动还款
order, err := client.NewCreateMarginOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    Quantity("0.001").
    Price("50000.00").
    AutoRepayAtCancel(true). // 取消时自动还款
    Do(ctx)
```

**CreateMarginOrderService 链式方法**:

```go
.Symbol(symbol string)
.IsIsolated(b bool)
.Side(side SideType)
.Type(orderType OrderType)
.TimeInForce(t TimeInForceType)
.Quantity(q string)
.QuoteOrderQty(q string)
.Price(p string)
.NewClientOrderID(id string)
.StopPrice(p string)
.IcebergQuantity(q string)
.NewOrderRespType(t NewOrderRespType)
.SideEffectType(s SideEffectType)
.SelfTradePreventionMode(m SelfTradePreventionMode)
.AutoRepayAtCancel(b bool)
.Do(ctx) (*CreateOrderResponse, error)
```

### 4.2 杠杆 OCO 订单

```go
resp, err := client.NewCreateMarginOCOService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeSell).
    Quantity("0.001").
    IsIsolated(true).
    // 限价单
    Price("55000.00").
    LimitClientOrderID("limit-oco-001").
    // 止损单
    StopPrice("54000.00").
    StopLimitPrice("53500.00").
    StopClientOrderID("stop-oco-001").
    Do(ctx)
```

### 4.3 查询杠杆订单

```go
// 查询订单
order, err := client.NewGetMarginOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    IsIsolated(true).
    Do(ctx)

// 查询所有订单
orders, err := client.NewListMarginOrdersService().
    Symbol("BTCUSDT").
    Limit(100).
    IsIsolated(true).
    Do(ctx)

// 查询开放订单
orders, err := client.NewListMarginOpenOrdersService().
    Symbol("BTCUSDT").
    IsIsolated(true).
    Do(ctx)
```

### 4.4 取消杠杆订单

```go
resp, err := client.NewCancelMarginOrderService().
    Symbol("BTCUSDT").
    OrderID(123456789).
    IsIsolated(true).
    Do(ctx)

// 取消所有开放订单
err = client.NewCancelAllMarginOrdersService().
    Symbol("BTCUSDT").
    IsIsolated(true).
    Do(ctx)
```

---

## 5. 强平订单

### 5.1 查询全仓强平订单

> 注意：此接口在 `spot.md` 的 `ListLiquidationOrdersService` 中（现货模块无杠杆强平，合约模块有）。

### 5.2 查询逐仓强平订单

```go
// 见 spot.md 中的 ListLiquidationOrdersService
// 需要通过现货客户端 client.NewListLiquidationOrdersService()
// 区分是否逐仓: IsIsolated 参数
```

---

## 6. 用户数据流

### 6.1 逐仓用户数据流

```go
// 开启逐仓账户的用户数据流（每个 symbol 独立）
listenKey, _ := client.NewStartIsolatedMarginUserStreamService().
    Symbol("BTCUSDT").
    Do(ctx)

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

// WebSocket 接收
// 见 websocket.md - 现货用户数据流（区分 IsIsolated）
```

---

## 7. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `MarginTransferService` | 现货↔杠杆转账 |
| `MarginLoanService` | 借款 |
| `MarginRepayService` | 还款 |
| `MarginBorrowRepayService` | 借款+还款合一 |
| `ListMarginLoansService` | 借款记录 |
| `ListMarginRepaysService` | 还款记录 |
| `ListMarginBorrowRepayService` | 借款/还款记录 |
| `ListMarginTradesService` | 杠杆交易历史 |
| `GetMarginAccountService` | 全仓账户 |
| `GetIsolatedMarginAccountService` | 逐仓账户 |
| `GetMaxBorrowableService` | 最大可借 |
| `GetMaxTransferableService` | 最大可转 |
| `GetMarginAssetService` | 资产信息 |
| `GetMarginPairService` | 交易对信息 |
| `GetMarginPriceIndexService` | 价格指数 |
| `GetAllMarginAssetsService` | 所有资产 |
| `GetIsolatedMarginAllPairsService` | 所有逐仓交易对 |
| `InterestHistoryService` | 利息历史 |
| `CreateMarginOrderService` | 创建杠杆订单 |
| `GetMarginOrderService` | 查询杠杆订单 |
| `ListMarginOrdersService` | 杠杆订单列表 |
| `ListMarginOpenOrdersService` | 杠杆开放订单 |
| `CancelMarginOrderService` | 取消杠杆订单 |
| `CancelAllMarginOrdersService` | 取消全部杠杆订单 |
| `CreateMarginOCOService` | 创建杠杆OCO |
| `CancelMarginOCOService` | 取消杠杆OCO |
| `StartIsolatedMarginUserStreamService` | 开启逐仓用户流 |
| `KeepaliveIsolatedMarginUserStreamService` | 续期 |
| `CloseIsolatedMarginUserStreamService` | 关闭 |
| `IsolatedMarginTransferService` | 逐仓划转 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `TransactionResponse` | 转账/借款/还款响应（包含 TranID）|
| `MarginLoanResponse` | 借款记录列表 |
| `MarginLoan` | 借款记录 |
| `MarginRepayResponse` | 还款记录列表 |
| `MarginRepay` | 还款记录 |
| `MarginBorrowRepayResponse` | 借款/还款记录列表 |
| `MarginBorrowRepay` | 借款/还款记录 |
| `MarginAccount` | 全仓账户 |
| `IsolatedMarginAccount` | 逐仓账户 |
| `IsolatedMarginAsset` | 逐仓资产 |
| `UserAsset` | 用户资产 |
| `IsolatedUserAsset` | 逐仓用户资产 |
| `MarginAsset` | 资产信息 |
| `MarginPair` | 交易对信息 |
| `MarginPriceIndex` | 价格指数 |
| `MaxBorrowable` | 最大可借 |
| `MaxTransferable` | 最大可转 |
| `MarginAllPair` | 全仓交易对 |
| `IsolatedMarginAllPair` | 逐仓交易对 |
| `InterestHistory` | 利息历史 |
| `InterestHistoryElement` | 利息记录 |
| `CreateOrderResponse` | 创建订单响应 |
| `CancelOrderResponse` | 取消订单响应 |
| `CancelAllMarginOrdersResponse` | 取消全部响应 |
| `CreateMarginOCOResponse` | 创建OCO响应 |
| `CancelMarginOCOResponse` | 取消OCO响应 |

### Const 一览

| 类型 | 值 |
|------|-----|
| `MarginTransferType` | `CentralizedIn`(1), `CentralizedOut`(2) |
| `MarginLoanStatusType` | `Pending`, `Confirmed`, `Failed` |
| `MarginRepayStatusType` | `Pending`, `Confirmed`, `Failed` |
| `MarginAccountBorrowRepayType` | `Borrow`(1), `Repay`(2) |
| `LendingType` | `Daily`, `Customized`, `Activity` |
| `SideEffectType` | `NoSideEffect`, `MarginBuy`, `AutoRepay` |
