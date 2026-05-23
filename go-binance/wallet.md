# 钱包操作模块 (wallet)

> **模块路径**: `github.com/adshao/go-binance/v2`（通过 `client.NewListDepositsService()` 等使用）
> **相关文档**: [SKILL.md](../SKILL.md) | [common.md](./common.md)

钱包模块提供充值、提现、地址查询等资产管理功能。

---

## 目录

1. [充值](#1-充值)
2. [提现](#2-提现)
3. [钱包余额](#3-钱包余额)
4. [类型索引](#4-类型索引)

---

## 1. 充值

### 1.1 充值记录 (ListDeposits)

```go
deposits, err := client.NewListDepositsService().
    Coin("USDT").
    Status(1).   // 0(未确认) 1(已确认)
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)

for _, d := range deposits {
    fmt.Printf("充值: %s 数量=%s 网络=%s 地址=%s txid=%s 时间=%d 状态=%d\n",
        d.Coin, d.Amount, d.Network, d.Address, d.TxID, d.InsertTime, d.Status)
}
```

### 1.2 充值地址 (GetDepositAddress)

```go
addr, err := client.NewGetDepositAddressService().
    Coin("BTC").
    Network("BTC"). // 可选：指定网络
    Do(ctx)

fmt.Printf("充值地址: %s 标签=%s\n", addr.Address, addr.Tag)
```

---

## 2. 提现

### 2.1 提现 (CreateWithdraw)

```go
resp, err := client.NewCreateWithdrawService().
    Coin("USDT").
    Address("钱包地址").
    Amount("100").
    Network("TRC20"). // 可选：指定网络
    // AddressTag("标签").   // 某些币需要标签
    // WithdrawOrderId("my-withdraw-001"). // 自定义提现单号
    // TransactionFeeFlag(true).           // 是否内扣手续费
    Do(ctx)

fmt.Printf("提现ID: %s\n", resp.ID)
```

### 2.2 提现记录 (ListWithdraws)

```go
withdraws, err := client.NewListWithdrawsService().
    Coin("USDT").
    Status(6).   // 状态码: 0=Email Sent, 1=Canceled, 2=Awaiting Approval, 3=Rejected, 4=Processing, 5=Failure, 6=Completed
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)

for _, w := range withdraws {
    fmt.Printf("提现: ID=%s %s 数量=%s 地址=%s txid=%s 时间=%s 状态=%d\n",
        w.ID, w.Coin, w.Amount, w.Address, w.TxID, w.ApplyTime, w.Status)
}
```

---

## 3. 钱包余额

### 3.1 钱包余额 (WalletBalance)

```go
balances, err := client.NewWalletBalanceService().
    Do(ctx)

for _, b := range balances {
    if b.Balance != "0" {
        fmt.Printf("钱包: %s 余额=%s 状态=%v\n",
            b.WalletName, b.Balance, b.Activate)
    }
}
```

---

## 4. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `ListDepositsService` | 充值记录 |
| `GetDepositAddressService` | 充值地址 |
| `CreateWithdrawService` | 提现 |
| `ListWithdrawsService` | 提现记录 |
| `WalletBalanceService` | 钱包余额 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `Deposit` | 充值记录 |
| `GetDepositAddressResponse` | 充值地址响应 |
| `CreateWithdrawResponse` | 提现响应（包含提现ID）|
| `Withdraw` | 提现记录 |
| `WalletBalance` | 钱包余额 |

### Deposit 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `Coin` | string | 币种 |
| `Amount` | string | 数量 |
| `Network` | string | 网络 |
| `Status` | int | 状态（0=未确认, 1=已确认）|
| `Address` | string | 地址 |
| `AddressTag` | string | 地址标签 |
| `TxID` | string | 交易哈希 |
| `InsertTime` | int64 | 充值时间 |
| `TransferType` | int64 | 转账类型 |
| `UnlockConfirm` | int64 | 解锁确认数 |
| `ConfirmTimes` | string | 确认次数 |

### Withdraw 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `ID` | string | 提现ID |
| `Coin` | string | 币种 |
| `Amount` | string | 数量 |
| `Network` | string | 网络 |
| `Address` | string | 地址 |
| `AddressTag` | string | 地址标签 |
| `TxID` | string | 交易哈希 |
| `ApplyTime` | string | 申请时间 |
| `Status` | int | 状态 |
| `TransactionFee` | string | 手续费 |
| `TransferType` | int | 转账类型 |
| `ConfirmNo` | int32 | 确认数 |
| `WalletType` | int | 钱包类型 |

### CreateWithdraw 链式方法

```go
.Coin(coin string)                             // 必填：币种
.WithdrawOrderId(id string)                   // 可选：自定义提现单号
.Network(network string)                       // 可选：网络
.Address(address string)                       // 必填：提现地址
.AddressTag(tag string)                        // 可选：地址标签
.Amount(amount string)                         // 必填：数量
.TransactionFeeFlag(b bool)                   // 可选：内扣手续费
.Name(name string)                            // 可选：备注
.WalletType(walletType int)                   // 可选：钱包类型
.Do(ctx) (*CreateWithdrawResponse, error)
```
