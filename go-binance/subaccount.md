# 子账户管理模块 (subaccount)

> **模块路径**: `github.com/adshao/go-binance/v2`（通过 `client.NewTransferToSubAccountService()` 等使用）
> **相关文档**: [SKILL.md](../SKILL.md) | [spot.md](./spot.md) | [futures.md](./futures.md)

子账户模块提供母子账户之间的资金划转、账户管理、杠杆/合约开通等功能。

---

## 目录

1. [母子账户转账](#1-母子账户转账)
2. [子账户列表](#2-子账户列表)
3. [子账户杠杆](#3-子账户杠杆)
4. [子账户合约](#4-子账户合约)
5. [子账户期权](#5-子账户期权)
6. [子账户理财](#6-子账户理财)
7. [子账户快照](#7-子账户快照)
8. [子账户 API 密钥管理](#8-子账户-api-密钥管理)
9. [类型索引](#9-类型索引)

---

## 1. 母子账户转账

### 1.1 主账户 → 子账户 (TransferToSubAccount)

```go
resp, err := client.NewTransferToSubAccountService().
    ToEmail("subaccount@email.com").
    Asset("USDT").
    Amount("100").
    Do(ctx)
fmt.Printf("转账ID: %d\n", resp.TxnID)
```

### 1.2 子账户 → 主账户 (TransferSubToMaster)

```go
resp, err := client.NewTransferSubToMasterService().
    Asset("USDT").
    Amount("50").
    Do(ctx)
fmt.Printf("转账ID: %d\n", resp.TxnID)
```

### 1.3 母子账户通用转账 (UniversalTransfer)

```go
// 支持现货↔杠杆、现货↔合约等多种组合
resp, err := client.NewSubAccountUniversalTransferService().
    FromEmail("master@email.com").
    ToEmail("sub@email.com").
    FromAccountType("SPOT").    // SPOT, ISOLATED_MARGIN, MARGIN, USDT_M_FUTURES, COIN_M_FUTURES
    ToAccountType("SPOT").
    Asset("USDT").
    Amount("100").
    ClientTranId("my-transfer-001"). // 可选：自定义转账单号
    Do(ctx)
fmt.Printf("转账ID: %d\n", resp.TranId)
```

### 1.4 子账户转账历史

```go
// 子账户间转账历史
history, err := client.NewSubAccountTransferHistoryService().
    Asset("USDT").
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(100).
    Do(ctx)
for _, h := range history {
    fmt.Printf("转账: %s %s %s 金额=%s 类型=%s 时间=%d\n",
        h.Email, h.CounterParty, h.Type, h.Qty, h.Asset, h.Time)
}

// 主账户的子账户转账记录
snapshot, err := client.NewSubaccountSpotSummaryService().
    Email("sub@email.com").
    Page(1).
    Size(10).
    Do(ctx)
fmt.Printf("子账户现货资产总价值: %s BTC\n", snapshot.MasterAccountTotalAsset)
```

### 1.5 托管子账户转账 (Managed Sub Account)

托管子账户是管理人与被管理人的关系，与母子账户不同。

```go
// 存入（管理人 → 托管子账户）
resp, err := client.NewManagedSubAccountDepositService().
    ToEmail("managed@email.com").
    Asset("USDT").
    Amount("100").
    Do(ctx)
fmt.Printf("存入ID: %d\n", resp.ID)

// 取出（托管子账户 → 管理人）
resp, err := client.NewManagedSubAccountWithdrawalService().
    FromEmail("managed@email.com").
    Asset("USDT").
    Amount("50").
    TransferDate(time.Now().UnixMilli()). // 预设划转日期
    Do(ctx)
fmt.Printf("取出ID: %d\n", resp.ID)

// 查询托管子账户资产
assets, err := client.NewManagedSubAccountAssetsService().
    Email("managed@email.com").
    Do(ctx)
for _, a := range assets {
    fmt.Printf("%s: 余额=%s 可用=%s 冻结=%s 年化收益=%s\n",
        a.Asset, a.TotalBalance, a.AvailableBalance, a.InOrder, a.AnnualInterestRate)
}
```

---

## 2. 子账户列表

### 2.1 子账户列表

```go
list, err := client.NewSubAccountListService().
    IsFreeze(false).
    Page(1).
    Limit(10).
    Do(ctx)
for _, s := range list.SubAccounts {
    fmt.Printf("子账户: ID=%d Email=%s 备注=%s 冻结=%v 创建时间=%d\n",
        s.SubUserID, s.Email, s.Remark, s.IsFreeze, s.CreateTime)
}
```

### 2.2 子账户资产查询

```go
// 查询子账户的现货资产
assets, err := client.NewSubAccountAssetsService().
    Email("sub@email.com").
    Do(ctx)
for _, a := range assets.Balances {
    if a.Free != 0 || a.Locked != 0 {
        fmt.Printf("%s: 可用=%.8f 锁定=%.8f\n", a.Asset, a.Free, a.Locked)
    }
}

// 子账户资产（统一查询）
assetInfo, err := client.NewSubAccountAssetService().
    Email("sub@email.com").
    Do(ctx)
for _, a := range assetInfo.Balances {
    fmt.Printf("%s: 可用=%s 锁定=%s\n", a.Asset, a.Free, a.Locked)
}
```

### 2.3 子账户保证金余额

```go
account, err := client.NewSubAccountMarginAccountInfoService().
    Email("sub@email.com").
    Do(ctx)
fmt.Printf("保证金水平: %s 净资产: %s BTC\n",
    account.MarginLevel, account.TotalAssetOfBtc)
for _, a := range account.MarginUserAssetVoList {
    fmt.Printf("%s: 余额=%s 借款=%s 利息=%s\n",
        a.Asset, a.Free, a.Borrowed, a.Interest)
}
```

---

## 3. 子账户杠杆

### 3.1 开通杠杆

```go
resp, err := client.NewSubAccountMarginEnableService().
    Email("sub@email.com").
    Do(ctx)
fmt.Printf("杠杆开通: %v\n", resp.IsMarginEnabled)
```

### 3.2 查询保证金子账户汇总

```go
summary, err := client.NewSubAccountMarginAccountSummaryService().
    Do(ctx)
fmt.Printf("子账户保证金汇总: 净资产=%s BTC 保证金水平=%s\n",
    summary.TotalAssetOfBtc, summary.MarginLevel)
for _, s := range summary.SubAccountList {
    fmt.Printf("  子账户: %s 净资产=%s\n", s.Email, s.TotalAssetOfBtc)
}
```

### 3.3 子账户保证金划转

```go
resp, err := client.NewSubAccountMarginTransferService().
    Email("sub@email.com").
    Asset("USDT").
    Amount("100").
    TransferType(1). // 1=从现货到保证金, 2=从保证金到现货
    Do(ctx)
fmt.Printf("划转ID: %s\n", resp.TxnId)
```

---

## 4. 子账户合约

### 4.1 开通合约

```go
resp, err := client.NewSubAccountFuturesEnableService().
    Email("sub@email.com").
    Do(ctx)
fmt.Printf("合约开通: %v\n", resp.IsFuturesEnabled)
```

### 4.2 子账户合约账户 (USDT-M)

```go
account, err := client.NewSubAccountFuturesAccountService().
    Email("sub@email.com").
    Do(ctx)
fmt.Printf("合约账户: 净资产=%s 可交易=%v\n",
    account.TotalWalletBalance, account.CanTrade)
for _, p := range account.Positions {
    fmt.Printf("  持仓: %s 数量=%s 盈亏=%s\n",
        p.Symbol, p.PositionAmt, p.UnrealizedProfit)
}
```

### 4.3 子账户合约账户 V2 (USDT-M + 币本位)

```go
resp, err := client.NewSubAccountFuturesAccountV2Service().
    Email("sub@email.com").
    FuturesType(1). // 1=USDT-M, 2=币本位
    Do(ctx)
if resp.FutureAccountResp != nil {
    fmt.Printf("USDT-M: %s\n", resp.FutureAccountResp.Email)
}
if resp.DeliveryAccountResp != nil {
    fmt.Printf("币本位: %s\n", resp.DeliveryAccountResp.Email)
}
```

### 4.4 子账户合约账户汇总 V1

```go
summary, err := client.NewSubAccountFuturesSummaryV1Service().
    Do(ctx)
fmt.Printf("USDT总余额: %s 未实现盈亏: %s\n",
    summary.TotalWalletBalance, summary.TotalUnrealizedProfit)
```

### 4.5 子账户合约汇总 V2

```go
resp, err := client.NewSubAccountFuturesAccountSummaryService().
    FuturesType(1). // 1=USDT-M, 2=币本位
    Page(1).
    Limit(10).
    Do(ctx)
// USDT-M 汇总
if resp.FutureAccountSummaryResp != nil {
    fmt.Printf("USDT-M: 净资产=%s 未实现盈亏=%s\n",
        resp.FutureAccountSummaryResp.TotalWalletBalance,
        resp.FutureAccountSummaryResp.TotalUnrealizedProfit)
}
// 币本位汇总
if resp.DeliveryAccountSummaryResp != nil {
    fmt.Printf("币本位: 净资产=%s\n",
        resp.DeliveryAccountSummaryResp.TotalMarginBalanceOfBTC)
}
```

### 4.6 子账户合约持仓

```go
resp, err := client.NewSubAccountFuturesPositionsService().
    Email("sub@email.com").
    FuturesType(1). // 1=USDT-M, 2=币本位
    Do(ctx)
for _, p := range resp.FuturePositionRiskVos {
    fmt.Printf("持仓: %s 数量=%s 方向=%s 盈亏=%s 强平价=%s\n",
        p.Symbol, p.PositionAmount, p.Leverage, p.UnrealizedProfit, p.LiquidationPrice)
}
```

### 4.7 子账户合约划转

```go
// 主账户 ↔ 子账户合约
resp, err := client.NewSubAccountFuturesTransferV1Service().
    Email("sub@email.com").
    Asset("USDT").
    Amount("100").
    TransferType(1). // 1=主账户→子账户, 2=子账户→主账户
    Do(ctx)
fmt.Printf("划转ID: %d\n", resp.TranID)
```

### 4.8 子账户合约划转历史

```go
// 子账户合约划转历史
history, err := client.NewSubAccountFuturesTransferHistoryService().
    Email("sub@email.com").
    FuturesType(1).
    Limit(100).
    Do(ctx)
for _, h := range history.Transfers {
    fmt.Printf("划转: %s %s %s 数量=%s 时间=%d\n",
        h.From, h.To, h.Asset, h.Qty, h.Time)
}
```

### 4.9 子账户合约内部划转

```go
resp, err := client.NewSubAccountFuturesInternalTransferService().
    FromEmail("sub1@email.com").
    ToEmail("sub2@email.com").
    FuturesType(1). // 1=USDT-M, 2=币本位
    Asset("USDT").
    Amount("10").
    Do(ctx)
fmt.Printf("内部划转: %v ID: %s\n", resp.Success, resp.TxnId)
```

---

## 5. 子账户期权

### 5.1 开通期权

```go
resp, err := client.NewSubAccountOptionsEnableService().
    Email("sub@email.com").
    Do(ctx)
fmt.Printf("期权开通: %v\n", resp.IsEOptionsEnabled)
```

---

## 6. 子账户理财

### 6.1 开通理财 (BLVT)

```go
resp, err := client.NewSubAccountBlvtEnableService().
    Email("sub@email.com").
    EnableBlvt(true).
    Do(ctx)
fmt.Printf("BLVT开通: %v\n", resp.EnableBlvt)
```

### 6.2 托管子账户理财记录

```go
// 查询理财划转日志（托管人视角）
logs, err := client.NewManagedSubAccountQueryTransferLogService().
    StartTime(1700000000000).
    EndTime(1700100000000).
    Page(1).
    Limit(10).
    Transfers("TRANSFER").
    TransferFunctionAccountType("SPOT").
    Do(ctx)
for _, l := range logs.ManagerSubTransferHistoryVos {
    fmt.Printf("划转: %s %s → %s %s 数量=%s 时间=%d\n",
        l.FromEmail, l.FromAccountType,
        l.ToEmail, l.ToAccountType,
        l.Asset, l.CreateTime)
}

// 查询理财划转日志（投资人视角）
investorLogs, err := client.NewManagedSubAccountQueryTransferLogForInvestorService().
    Email("sub@email.com").
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(10).
    Do(ctx)

// 查询理财划转日志（交易员视角）
parentLogs, err := client.NewManagedSubAccountQueryTransferLogForTradeParentService().
    Email("sub@email.com").
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(10).
    Do(ctx)
```

### 6.3 托管子账户快照

```go
snapshots, err := client.NewManagedSubAccountSnapshotService().
    Email("sub@email.com").
    AccType("SPOT"). // SPOT, MARGIN, FUTURES
    StartTime(1700000000000).
    EndTime(1700100000000).
    Limit(10).
    Do(ctx)
for _, v := range snapshots.SnapshotVos {
    fmt.Printf("快照: 类型=%s 时间=%d\n", v.Type, v.UpdateTime)
}
```

---

## 7. 子账户快照

### 7.1 交易统计

```go
stats, err := client.NewSubAccountTransactionStatisticsService().
    Email("sub@email.com").
    Do(ctx)
for _, t := range stats.TradeInfoVos {
    fmt.Printf("统计: 日期=%d BTC交易=%f USDT交易=%f\n",
        t.Date, t.Btc, t.Busd)
}
```

---

## 8. 子账户 API 密钥管理

### 8.1 查询 IP 白名单

```go
resp, err := client.NewSubAccountApiIpRestrictionService().
    Email("sub@email.com").
    SubAccountApiKey("apiKeyFromSubAccount").
    Do(ctx)
fmt.Printf("IP限制: %s IP列表: %v\n", resp.IpRestrict, resp.IpList)
```

### 8.2 添加 IP

```go
resp, err := client.NewSubAccountApiAddIpRestrictionService().
    Email("sub@email.com").
    SubAccountApiKey("apiKey").
    Status("true"). // "true"=开启限制, "false"=关闭
    IpAddress("1.2.3.4").
    Do(ctx)
fmt.Printf("更新后IP列表: %v\n", resp.IpList)
```

### 8.3 删除 IP

```go
resp, err := client.NewSubAccountApiDeleteIpRestrictionService().
    Email("sub@email.com").
    SubAccountApiKey("apiKey").
    IpAddress("1.2.3.4").
    Do(ctx)
```

---

## 9. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `TransferToSubAccountService` | 主→子转账 |
| `TransferSubToMasterService` | 子→主转账 |
| `SubAccountUniversalTransferService` | 通用转账 |
| `SubAccountTransferHistoryService` | 转账历史 |
| `SubaccountSpotSummaryService` | 现货汇总 |
| `SubAccountListService` | 子账户列表 |
| `SubAccountAssetsService` | 子账户资产 |
| `SubAccountAssetService` | 子账户资产（统一）|
| `ManagedSubAccountDepositService` | 存入托管子账户 |
| `ManagedSubAccountWithdrawalService` | 从托管子账户取出 |
| `ManagedSubAccountAssetsService` | 托管子账户资产 |
| `SubAccountMarginEnableService` | 开通杠杆 |
| `SubAccountMarginAccountInfoService` | 杠杆账户信息 |
| `SubAccountMarginAccountSummaryService` | 杠杆账户汇总 |
| `SubAccountMarginTransferService` | 保证金划转 |
| `SubAccountFuturesEnableService` | 开通合约 |
| `SubAccountFuturesAccountService` | 合约账户（USDT-M）|
| `SubAccountFuturesAccountV2Service` | 合约账户 V2（USDT-M+币本位）|
| `SubAccountFuturesSummaryV1Service` | 合约账户汇总 V1 |
| `SubAccountFuturesAccountSummaryService` | 合约账户汇总 V2 |
| `SubAccountFuturesPositionsService` | 合约持仓 |
| `SubAccountFuturesTransferV1Service` | 合约划转 V1 |
| `SubAccountFuturesTransferHistoryService` | 合约划转历史 |
| `SubAccountFuturesInternalTransferService` | 合约内部划转 |
| `SubAccountOptionsEnableService` | 开通期权 |
| `SubAccountBlvtEnableService` | 开通 BLVT |
| `SubAccountDepositRecordService` | 充值记录 |
| `SubAccountApiIpRestrictionService` | 查询IP白名单 |
| `SubAccountApiAddIpRestrictionService` | 添加IP |
| `SubAccountApiDeleteIpRestrictionService` | 删除IP |
| `ManagedSubAccountSnapshotService` | 托管快照 |
| `ManagedSubAccountInfoService` | 托管子账户信息 |
| `ManagedSubAccountDepositAddressService` | 托管充值地址 |
| `ManagedSubAccountWithdrawService` | 托管提现 |
| `ManagedSubAccountQueryTransferLogService` | 理财划转日志 |
| `ManagedSubAccountQueryTransferLogForInvestorService` | 投资人视角划转日志 |
| `ManagedSubAccountQueryTransferLogForTradeParentService` | 交易员视角划转日志 |
| `ManagedSubAccountQueryFuturesAssetService` | 托管合约资产 |
| `ManagedSubAccountQueryMarginAssetService` | 托管杠杆资产 |
| `SubAccountTransactionStatisticsService` | 交易统计 |
| `CreateVirtualSubAccountService` | 创建虚拟子账户 |
| `SubAccountSpotTransferHistoryService` | 现货划转历史 |
