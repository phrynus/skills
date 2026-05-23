# 组合保证金模块 (portfolio)

> **模块路径**: `github.com/adshao/go-binance/v2`（通过 `binance.NewPortfolioClient()` 创建）
> **相关文档**: [SKILL.md](../SKILL.md) | [futures.md](./futures.md)

组合保证金（Portfolio Margin）是一种高级保证金模式，用统一的账户余额同时支持现货、杠杆和合约交易，风险计算更高效。

---

## 目录

1. [客户端](#1-客户端)
2. [余额查询](#2-余额查询)
3. [类型索引](#3-类型索引)

---

## 1. 客户端

### 初始化

```go
import "github.com/adshao/go-binance/v2"

portfolioClient := binance.NewPortfolioClient(apiKey, secretKey)
```

---

## 2. 余额查询 (GetBalance)

获取组合保证金账户的资产余额。

```go
balances, err := portfolioClient.NewGetBalanceService().
    Asset("USDT"). // 可选，不填则返回全部
    Do(ctx)

for _, b := range balances {
    fmt.Printf("资产: %s\n", b.Asset)
    fmt.Printf("  钱包余额: %s\n", b.TotalWalletBalance)
    fmt.Printf("  交叉保证金资产: %s\n", b.CrossMarginAsset)
    fmt.Printf("  交叉保证金借款: %s\n", b.CrossMarginBorrowed)
    fmt.Printf("  交叉保证金空闲: %s\n", b.CrossMarginFree)
    fmt.Printf("  交叉保证金利息: %s\n", b.CrossMarginInterest)
    fmt.Printf("  交叉保证金锁定: %s\n", b.CrossMarginLocked)
    fmt.Printf("  UM钱包余额: %s\n", b.UMWalletBalance)
    fmt.Printf("  UM未实现盈亏: %s\n", b.UMUnrealizedPNL)
    fmt.Printf("  CM钱包余额: %s\n", b.CMWalletBalance)
    fmt.Printf("  CM未实现盈亏: %s\n", b.CMUnrealizedPNL)
    fmt.Printf("  更新时间: %d\n", b.UpdateTime)
    fmt.Printf("  负余额: %s\n", b.NegativeBalance)
}
```

---

## 3. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `GetBalanceService` | 组合保证金余额 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `Balance` | 资产余额 |

### Balance 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `Asset` | string | 资产名称 |
| `TotalWalletBalance` | string | 总钱包余额 |
| `CrossMarginAsset` | string | 交叉保证金资产 |
| `CrossMarginBorrowed` | string | 交叉保证金借款 |
| `CrossMarginFree` | string | 交叉保证金空闲 |
| `CrossMarginInterest` | string | 交叉保证金利息 |
| `CrossMarginLocked` | string | 交叉保证金锁定 |
| `UMWalletBalance` | string | UM钱包余额 |
| `UMUnrealizedPNL` | string | UM未实现盈亏 |
| `CMWalletBalance` | string | CM钱包余额 |
| `CMUnrealizedPNL` | string | CM未实现盈亏 |
| `UpdateTime` | int64 | 更新时间 |
| `NegativeBalance` | string | 负余额 |

### GetBalanceService 链式方法

```go
.Asset(asset string)    // 可选：不填则返回全部资产
.Do(ctx) ([]*Balance, error)
```
