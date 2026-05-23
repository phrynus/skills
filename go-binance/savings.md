# 理财/储蓄模块 (savings)

> **模块路径**: `github.com/adshao/go-binance/v2`（通过 `client.NewListSavingsFlexibleProductsService()` 等使用）
> **相关文档**: [SKILL.md](../SKILL.md) | [common.md](./common.md)

理财模块提供灵活储蓄和定期储蓄两种产品，以及持仓查询功能。

---

## 目录

1. [灵活储蓄](#1-灵活储蓄)
2. [定期/活动储蓄](#2-定期活动储蓄)
3. [持仓查询](#3-持仓查询)
4. [类型索引](#4-类型索引)

---

## 1. 灵活储蓄

灵活储蓄支持随时申购和赎回，无锁定期。

### 1.1 产品列表 (ListSavingsFlexibleProducts)

```go
products, err := client.NewListSavingsFlexibleProductsService().
    Status("ALL"). // ALL, SUBSCRIBABLE, SOLD_OUT
    Featured("ALL"). // ALL, AVAILABLE
    Limit(10).
    Do(ctx)

for _, p := range products {
    fmt.Printf("产品: %s 年化=%.2f%% 可申购=%v 可赎回=%v 已申购=%s\n",
        p.Asset, p.AnnualInterestRate*100, p.CanPurchase, p.CanRedeem, p.PurchasedAmount)
}
```

### 1.2 申购灵活储蓄 (Purchase)

```go
purchaseId, err := client.NewPurchaseSavingsFlexibleProductService().
    ProductId("USDT").
    Amount(100.0). // 申购数量
    Do(ctx)
fmt.Printf("申购成功, ID: %d\n", purchaseId)
```

### 1.3 赎回灵活储蓄 (Redeem)

```go
// 快速赎回（立即到账，有限额）
err = client.NewRedeemSavingsFlexibleProductService().
    ProductId("USDT").
    Amount(50.0).
    Type("FAST"). // FAST=快速赎回, NORMAL=正常赎回
    Do(ctx)

// 正常赎回
err = client.NewRedeemSavingsFlexibleProductService().
    ProductId("USDT").
    Amount(50.0).
    Type("NORMAL").
    Do(ctx)
```

---

## 2. 定期/活动储蓄

定期储蓄有固定期限，期限内不可提前赎回。

### 2.1 产品列表 (ListSavingsFixedAndActivityProducts)

```go
products, err := client.NewListSavingsFixedAndActivityProductsService().
    Asset("USDT").
    Type("ACTIVITY"). // ACTIVITY=活动, CUSTOMIZED_FIAT=定制, SYSTEM=系统定期
    Status("ALL").
    SortAsc(true).   // true=升序, false=降序
    SortBy("START_DATE").
    Limit(10).
    Do(ctx)

for _, p := range products {
    fmt.Printf("产品: %s 名称=%s 期限=%d天 年化=%.2f%% 已申购=%d/%d\n",
        p.Asset, p.ProjectName, p.Duration, p.InterestRate*100,
        p.LotsPurchased, p.LotsUpLimit)
}
```

---

## 3. 持仓查询

### 3.1 灵活储蓄持仓 (Flexible Product Positions)

```go
positions, err := client.NewSavingFlexibleProductPositionsService().
    Asset("USDT").
    Do(ctx)

for _, p := range positions {
    fmt.Printf("灵活储蓄持仓: %s 总金额=%s 已赚利息=%s 年化=%.2f%% 可赎回=%v\n",
        p.Asset, p.TotalAmount, p.TotalInterest,
        p.AnnualInterestRate*100, p.CanRedeem)
}
```

### 3.2 定期储蓄持仓 (Fixed Project Positions)

```go
positions, err := client.NewSavingFixedProjectPositionsService().
    Asset("USDT").
    Status("ALL"). // ALL, SUFFICIENT, EXPIRED
    ProjectID("BTCTP20230404001").
    Do(ctx)

for _, p := range positions {
    fmt.Printf("定期持仓: %s 项目=%s 期限=%d 利息=%s 本金=%s 状态=%s\n",
        p.Asset, p.ProjectName, p.Duration, p.Interest,
        p.Principal, p.Status)
}
```

---

## 4. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `ListSavingsFlexibleProductsService` | 灵活储蓄产品列表 |
| `PurchaseSavingsFlexibleProductService` | 申购灵活储蓄 |
| `RedeemSavingsFlexibleProductService` | 赎回灵活储蓄 |
| `ListSavingsFixedAndActivityProductsService` | 定期/活动储蓄产品 |
| `SavingFlexibleProductPositionsService` | 灵活储蓄持仓 |
| `SavingFixedProjectPositionsService` | 定期储蓄持仓 |

### Response Struct 一览

| 类型名 | 说明 |
|--------|------|
| `SavingsFlexibleProduct` | 灵活储蓄产品 |
| `PurchaseSavingsFlexibleProductResponse` | 申购响应 |
| `SavingsFixedProduct` | 定期/活动储蓄产品 |
| `SavingFlexibleProductPosition` | 灵活储蓄持仓 |
| `SavingFixedProjectPosition` | 定期储蓄持仓 |

### SavingsFlexibleProduct 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `Asset` | string | 币种 |
| `AnnualInterestRate` | string | 年化利率（需×100显示%）|
| `CanPurchase` | bool | 是否可申购 |
| `CanRedeem` | bool | 是否可赎回 |
| `DailyInterestPerThousand` | string | 千分之一日利率 |
| `Featured` | bool | 是否精选 |
| `MinPurchaseAmount` | string | 最小申购金额 |
| `ProductId` | string | 产品ID |
| `PurchasedAmount` | string | 已申购金额 |
| `Status` | string | 状态 |
| `UpLimit` | string | 申购上限 |
| `UpLimitPerUser` | string | 每人申购上限 |

### SavingsFixedProduct 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `Asset` | string | 币种 |
| `Duration` | int | 期限（天）|
| `InterestPerLot` | string | 每份利息 |
| `InterestRate` | string | 利率 |
| `LotSize` | string | 每份大小 |
| `LotsLowLimit` | int | 最少申购份数 |
| `LotsPurchased` | int | 已申购份数 |
| `LotsUpLimit` | int | 最多申购份数 |
| `MaxLotsPerUser` | int | 每人最多份数 |
| `ProjectId` | string | 项目ID |
| `ProjectName` | string | 项目名称 |
| `Status` | string | 状态 |
| `Type` | string | 类型 |

### SavingFlexibleProductPosition 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `Asset` | string | 币种 |
| `ProductId` | string | 产品ID |
| `ProductName` | string | 产品名称 |
| `AnnualInterestRate` | string | 年化利率 |
| `TotalAmount` | string | 总金额 |
| `TotalInterest` | string | 累计利息 |
| `PurchasedAmount` | string | 已申购金额 |
| `RedeemingAmount` | string | 赎回中金额 |
| `FreeAmount` | string | 可用金额 |
| `FreezeAmount` | string | 冻结金额 |
| `LockedAmount` | string | 锁定金额 |
| `CanRedeem` | bool | 是否可赎回 |

### SavingFixedProjectPosition 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `Asset` | string | 币种 |
| `CanTransfer` | bool | 是否可转账 |
| `Duration` | int64 | 期限（天）|
| `StartTime` | int64 | 开始时间 |
| `EndTime` | int64 | 结束时间 |
| `PurchaseTime` | int64 | 申购时间 |
| `Interest` | string | 已获得利息 |
| `InterestRate` | string | 利率 |
| `Lot` | int32 | 份数 |
| `PositionId` | int64 | 持仓ID |
| `Principal` | string | 本金 |
| `ProjectId` | string | 项目ID |
| `ProjectName` | string | 项目名称 |
| `ProjectType` | string | 项目类型 |
| `Status` | string | 状态 |

### Redeem 链式方法

```go
.ProductId(productId string)
.Amount(amount float64)
.Type(redeemType string)  // "FAST"=快速赎回, "NORMAL"=正常赎回
.Do(ctx) error
```
