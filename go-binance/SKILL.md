---
name: go-binance
description: |
  go-binance 是 Binance（币安）API 的 Golang SDK (github.com/adshao/go-binance/v2)，用于加密货币交易、量化策略、合约交易、杠杆借贷、期权交易等场景。
  
  触发条件（满足任一即调用）：
  - 用户提到 go-binance、go-binance/v2、adshao/go-binance
  - 用户提到 Binance API Golang、Binance Golang SDK、binance golang
  - 用户需要实现现货交易、合约交易（USDT-M/币本位）、杠杆借贷、期权交易
  - 用户需要获取行情数据、K线、深度、下单、撤单、账户余额
  - 用户提到量化交易、交易机器人、套利策略、网格交易
  - 用户问如何使用 Binance API、怎么调用 Binance 接口
---

# go-binance 开发助手

go-binance 是 Binance API 的 Golang SDK（v2.8.10），支持现货、杠杆、USDT-M 合约、币本位合约、期权、组合保证金等全产品线。

## 快速导航

| 模块 | 文件 | 场景 |
|------|------|------|
| 现货与杠杆 | `spot.md` | 下单、K线、账户 |
| USDT-M 合约 | `futures.md` | 合约下单、持仓、杠杆调整 |
| 币本位合约 | `delivery.md` | 币本位合约交易 |
| 期权交易 | `options.md` | 期权下单、行权、希腊字母 |
| 杠杆借贷 | `margin.md` | 借贷、利率、OCO订单 |
| 钱包操作 | `wallet.md` | 充值、提现、转账 |
| 子账户管理 | `subaccount.md` | 子账户划转、开通权限 |
| 理财储蓄 | `savings.md` | 灵活/定期储蓄 |
| 快速转换 | `convert.md` | 币币快速转换 |
| 组合保证金 | `portfolio.md` | 统一保证金 |
| 公共模块 | `common.md` | 签名、错误处理、限流 |
| WebSocket | `websocket.md` | 实时行情、用户数据流 |

## 快速开始

### 安装

```go
go get github.com/adshao/go-binance/v2
```

### 客户端初始化

```go
import "github.com/adshao/go-binance/v2"

// 现货/杠杆
client := binance.NewClient(apiKey, secretKey)

// USDT-M 合约
futuresClient := binance.NewFuturesClient(apiKey, secretKey)

// 币本位合约
deliveryClient := binance.NewDeliveryClient(apiKey, secretKey)

// 期权
optionsClient := binance.NewOptionsClient(apiKey, secretKey)

// 测试网
binance.UseTestnet = true
futures.UseTestnet = true
```

### 链式调用模式

所有 API 使用 Builder 模式，链式调用构建请求：

```go
// K线查询
klines, err := client.NewKlinesService().
    Symbol("BTCUSDT").
    Interval("1m").
    Limit(100).
    Do(ctx)

// 创建订单
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    TimeInForce(binance.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("50000.00").
    Do(ctx)
```

## 签名算法

详细签名方法见 `common.md`：

```go
import "github.com/adshao/go-binance/v2/common"

// HMAC-SHA256（默认）
sign, _ := common.HmacSHA256Encrypt(message, secretKey)

// HMAC-SHA512
sign, _ := common.HmacSHA512Encrypt(message, secretKey)

// RSA-SHA256
sign, _ := common.RSAEncrypt(message, privateKey)

// ED25519
sign, _ := common.Ed25519Sign(message, privateKey)
```

## 错误处理

```go
import "github.com/adshao/go-binance/v2/common"

order, err := client.NewCreateOrderService().Symbol("BTCUSDT").Do(ctx)
if err != nil {
    if apiErr, ok := err.(*common.APIError); ok {
        fmt.Printf("API错误: Code=%d Msg=%s\n", apiErr.Code, apiErr.Message)
    }
    if reqErr, ok := err.(*common.RequestError); ok {
        fmt.Printf("网络错误: %v\n", reqErr.Err)
    }
    return
}
```

## 常见场景

### 场景1：现货买入

```go
// 见 spot.md - CreateOrderService
order, err := client.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    TimeInForce(binance.TimeInForceTypeGTC).
    Quantity("0.001").
    Price("50000.00").
    Do(ctx)
```

### 场景2：合约开多/开空

```go
// 见 futures.md - CreateOrderService
order, err := futuresClient.NewCreateOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    PositionSide(binance.PositionSideTypeLong).
    Type(binance.OrderTypeLimit).
    Quantity("0.001").
    Price("50000.00").
    Do(ctx)
```

### 场景3：杠杆借贷

```go
// 见 margin.md

// 从现货转入杠杆账户
resp, err := client.NewMarginTransferService().
    Asset("USDT").
    Amount("100").
    Type(binance.MarginTransferTypeCentralizedIn).
    Do(ctx)

// 借贷
borrow, err := client.NewMarginLoanService().
    Asset("USDT").
    Amount("100").
    Do(ctx)

// 创建杠杆订单
order, err := client.NewCreateMarginOrderService().
    Symbol("BTCUSDT").
    Side(binance.SideTypeBuy).
    Type(binance.OrderTypeLimit).
    Quantity("0.001").
    Price("50000.00").
    Do(ctx)
```

### 场景4：WebSocket 实时数据

```go
// 见 websocket.md

// 现货深度
doneC, stopC, _ := binance.WsDepthServe("BTCUSDT", func(event *binance.WsDepthEvent) {
    fmt.Printf("深度: 买1=%s 卖1=%s\n", event.Bids[0].Price, event.Asks[0].Price)
}, func(err error) { fmt.Println(err) })

// K线
doneC, _, _ := binance.WsKlineServe("BTCUSDT", "1m", func(event *binance.WsKlineEvent) {
    fmt.Printf("K线: 开=%s 高=%s 低=%s 收=%s\n",
        event.Kline.Open, event.Kline.High, event.Kline.Low, event.Kline.Close)
}, func(err error) { fmt.Println(err) })

// 用户数据流（订单更新、余额变动）
doneC, stopC, _ := binance.WsUserDataServe(listenKey, handler, errHandler)
```

### 场景5：子账户管理

```go
// 见 subaccount.md

// 开通杠杆
client.NewSubAccountMarginEnableService().Email("sub@email.com").Do(ctx)

// 开通合约
client.NewSubAccountFuturesEnableService().Email("sub@email.com").Do(ctx)

// 母子账户转账
client.NewTransferToSubAccountService().
    ToEmail("sub@email.com").
    Asset("USDT").
    Amount("100").
    Do(ctx)
```

## 常见问题

| 问题 | 解答 |
|------|------|
| 报 "signature error"？ | 检查密钥、时间戳同步、签名算法。见 `common.md`。 |
| WebSocket 断线？ | 内置自动重连，频繁断线检查网络或使用代理。见 `websocket.md`。 |
| 合约和现货有什么区别？ | 现货用 `client`，合约用 `futuresClient`。两者的客户端独立、API 端点不同。 |
| 子账户如何开通杠杆/合约/期权？ | 见 `subaccount.md` - SubAccountMarginEnableService / SubAccountFuturesEnableService。 |
| 如何获取合约资金费率？ | 见 `futures.md` - FundingRateService。 |
| 灵活储蓄和定期储蓄有什么区别？ | 灵活储蓄随时申赎，定期储蓄有锁定期。见 `savings.md`。 |
| 组合保证金和普通保证金有什么优势？ | 统一账户余额，风险计算更高效。见 `portfolio.md`。 |
| 如何获取用户的希腊字母（期权）？ | 见 `options.md` - AccountService 返回的 Greek 字段（Delta/Gamma/Theta/Vega）。 |

## 类型索引

| 模块 | 类型数 | 主要类型 |
|------|--------|----------|
| `spot.md` | ~50 | Client, CreateOrderService, GetAccountService, WsDepthEvent... |
| `futures.md` | ~80 | Client, CreateOrderService, PositionRisk, WsUserDataEvent... |
| `delivery.md` | ~30 | Client, CreateOrderService, Account, PositionRisk... |
| `options.md` | ~40 | Client, CreateOrderService, Account, Position... |
| `margin.md` | ~50 | MarginTransferService, MarginLoanService, CreateMarginOrderService... |
| `wallet.md` | ~10 | ListDepositsService, CreateWithdrawService... |
| `subaccount.md` | ~60 | TransferToSubAccountService, SubAccountFuturesAccountService... |
| `savings.md` | ~15 | ListSavingsFlexibleProductsService, PurchaseSavingsFlexibleProductService... |
| `convert.md` | ~10 | ConvertGetQuoteService, ConvertAcceptQuoteService... |
| `portfolio.md` | ~5 | GetBalanceService |
| `common.md` | ~10 | APIError, UsedWeight, OrderCount, PriceLevel... |
| `websocket.md` | ~30 | WsDepthEvent, WsKlineEvent, WsUserDataEvent... |
