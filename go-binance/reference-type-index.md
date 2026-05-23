# 完整类型索引

按模块分类的完整类型定义和方法列表。

> **相关文档**: [SKILL.md](./SKILL.md) | [spot.md](./spot.md) | [futures.md](./futures.md) | [common.md](./common.md)

---

## 目录

1. [现货模块类型](#1-现货模块类型)
2. [合约模块类型](#2-合约模块类型)
3. [杠杆模块类型](#3-杠杆模块类型)
4. [公共模块类型](#4-公共模块类型)
5. [WebSocket 类型](#5-websocket-类型)

---

## 1. 现货模块类型

### Service Struct

```
Client
PingService, ServerTimeService
KlinesService, ContinuousKlinesService, IndexPriceKlinesService, MarkPriceKlinesService
DepthService
AggTradesService, RecentTradesService, HistoricalTradesService, ListTradesService
ListPricesService, ListBookTickersService, ListPriceChangeStatsService
AveragePriceService, ListSymbolTickerService
ExchangeInfoService
CreateOrderService, ModifyOrderService, CreateBatchOrdersService, ModifyBatchOrdersService
GetOrderService, ListOrdersService, ListOpenOrdersService, GetOpenOrderService
CancelOrderService, CancelAllOpenOrdersService, CancelMultipleOrdersService
CancelReplaceOrderService
CreateOCOService, CancelOCOService, ListOpenOcoService
GetAccountService, GetAccountV3Service, GetBalanceService
GetAccountSnapshotService, GetAPIKeyPermission
StartUserStreamService, KeepaliveUserStreamService, CloseUserStreamService
```

### Response Struct

```
CreateOrderResponse, ModifyOrderResponse
CreateBatchOrdersResponse, ModifyBatchOrdersResponse
Order, Oco, CreateOCOResponse, CancelOCOResponse, CancelAllOCOResponse
Account, AccountV3, Balance, Snapshot, APIKeyPermission
Kline, DepthResponse, BookTicker, SymbolPrice, PriceChangeStats, AvgPrice, SymbolTicker
Trade, TradeV3, AggTrade
ExchangeInfo, RateLimit, Symbol
LotSizeFilter, PriceFilter, PercentPriceBySideFilter, NotionalFilter
MarketLotSizeFilter, MaxNumOrdersFilter, MaxNumAlgoOrdersFilter, TrailingDeltaFilter
```

### Const

| 类型 | 值 |
|------|-----|
| `SideType` | `Buy`, `Sell` |
| `OrderType` | `Limit`, `Market`, `StopLoss`, `StopLossLimit`, `TakeProfit`, `TakeProfitLimit`, `LimitMaker` |
| `TimeInForceType` | `GTC`, `IOC`, `FOK` |
| `OrderStatusType` | `New`, `PartiallyFilled`, `Filled`, `Canceled`, `Rejected`, `Expired` |
| `NewOrderRespType` | `ACK`, `RESULT`, `FULL` |
| `SelfTradePreventionMode` | `None`, `ExpireTaker`, `ExpireBoth`, `ExpireMaker` |
| `CancelReplaceMode` | `StopOnFailure` |

---

## 2. 合约模块类型

### Service Struct

```
Client
PingService, ServerTimeService
KlinesService, ContinuousKlinesService, IndexPriceKlinesService, MarkPriceKlinesService
DepthService
AggTradesService, RecentTradesService, HistoricalTradesService
ListPricesService, ListBookTickersService, ListPriceChangeStatsService
PremiumIndexService, PremiumIndexKlinesService
FundingRateService, FundingRateInfoService
GetOpenInterestService, OpenInterestStatisticsService
LongShortRatioService, TopLongShortAccountRatioService
TopLongShortPositionRatioService, TakerLongShortRatioService, BasisService
DeliveryPriceService, IndexInfoService, AssetIndexService, ConstituentsService
ExchangeInfoService
CreateOrderService, ModifyOrderService
CreateBatchOrdersService, ModifyBatchOrdersService
GetOrderService, ListOrdersService, ListOpenOrdersService, GetOpenOrderService
CancelOrderService, CancelAllOpenOrdersService, CancelMultipleOrdersService
ListLiquidationOrdersService, ListUserLiquidationOrdersService
ChangeLeverageService, GetLeverageBracketService
ChangeMarginTypeService, UpdatePositionMarginService
ChangePositionModeService, GetPositionModeService
ChangeMultiAssetModeService, GetMultiAssetModeService
GetAccountService, GetAccountV3Service, GetBalanceService
GetPositionRiskService, GetPositionRiskV3Service
GetIncomeHistoryService, GetPositionMarginHistoryService
CommissionRateService, RebateNewUserService
GetFeeBurnService, FeeBurnService
AccountConfigService, SymbolConfigService
CreateAlgoOrderService, CancelAlgoOrderService, CancelAllAlgoOpenOrdersService
GetAlgoOrderService, ListOpenAlgoOrdersService, ListAllAlgoOrdersService
StartUserStreamService, KeepaliveUserStreamService, CloseUserStreamService
```

### Const

| 类型 | 值 |
|------|-----|
| `SideType` | `Buy`, `Sell` |
| `PositionSideType` | `Both`, `Long`, `Short` |
| `OrderType` | `Limit`, `Market`, `Stop`, `StopMarket`, `TakeProfit`, `TakeProfitMarket`, `TrailingStopMarket`, `Liquidation` |
| `TimeInForceType` | `GTC`, `GTD`, `GTEGTC`, `IOC`, `FOK`, `GTX` |
| `OrderStatusType` | `New`, `PartiallyFilled`, `Filled`, `Canceled`, `Rejected`, `Expired`, `NewInsurance`, `NewADL` |
| `MarginType` | `Isolated`, `Crossed` |
| `WorkingType` | `MarkPrice`, `ContractPrice` |
| `PriceMatchType` | `Opponent`, `Opponent5`, `Opponent10`, `Opponent20`, `Queue`, `Queue5`, `Queue10`, `Queue20`, `None` |
| `AlgoOrderType` | `Conditional` |
| `AlgoOrderStatusType` | `New`, `Canceled`, `Rejected`, `Expired` |

---

## 3. 杠杆模块类型

### Service Struct

```
MarginTransferService, IsolatedMarginTransferService
MarginLoanService, MarginRepayService, MarginBorrowRepayService
ListMarginLoansService, ListMarginRepaysService, ListMarginBorrowRepayService
InterestHistoryService
GetMarginAccountService, GetIsolatedMarginAccountService
GetMaxBorrowableService, GetMaxTransferableService
ListMarginTradesService
GetMarginAssetService, GetMarginPairService, GetMarginPriceIndexService
GetAllMarginAssetsService, GetIsolatedMarginAllPairsService
CreateMarginOrderService, GetMarginOrderService
ListMarginOrdersService, ListMarginOpenOrdersService
CancelMarginOrderService, CancelAllMarginOrdersService
CreateMarginOCOService, CancelMarginOCOService
StartIsolatedMarginUserStreamService
KeepaliveIsolatedMarginUserStreamService
CloseIsolatedMarginUserStreamService
```

### Const

| 类型 | 值 |
|------|-----|
| `MarginTransferType` | `CentralizedIn`, `CentralizedOut` |
| `MarginLoanStatusType` | `Pending`, `Confirmed`, `Failed` |
| `MarginRepayStatusType` | `Pending`, `Confirmed`, `Failed` |
| `LendingType` | `Daily`, `Customized`, `Activity` |
| `SideEffectType` | `NoSideEffect`, `MarginBuy`, `AutoRepay` |

---

## 4. 公共模块类型

### Struct

```
UsedWeight
OrderCount
APIError
RequestError
PriceLevel
```

### Function

```
HmacSHA256Encrypt(message, secretKey string) (*string, error)
HmacSHA512Encrypt(message, secretKey string) (*string, error)
RSAEncrypt(message, privateKey string) (*string, error)
Ed25519Sign(message, privateKey string) (*string, error)
SignFunc(keyType string) (func(string, string) (*string, error), error)
IsAPIError(e error) bool
AmountToLotSize(amount, minQty, stepSize string, precision int) string
ToInt(digit any) (int, error)
ToInt64(digit any) (int64, error)
```

---

## 5. WebSocket 类型

### 现货 Handler 类型

```
WsPartialDepthHandler      → *WsPartialDepthEvent
WsDepthHandler             → *WsDepthEvent
WsKlineHandler            → *WsKlineEvent
WsAggTradeHandler          → *WsAggTradeEvent
WsTradeHandler             → *WsTradeEvent
WsCombinedTradeHandler     → *WsCombinedTradeEvent
WsUserDataHandler         → *WsUserDataEvent
WsMarketStatHandler       → *WsMarketStatEvent
WsAllMarketsStatHandler   → WsAllMarketsStatEvent
WsAllMiniMarketsStatServeHandler → WsAllMiniMarketsStatEvent
WsBookTickerHandler        → *WsBookTickerEvent
WsAnnouncementHandler      → *WsAnnouncementEvent
ErrHandler                 → error
```

### 合约 Handler 类型

```
WsAggTradeHandler          → *WsAggTradeEvent
WsMarkPriceHandler         → *WsMarkPriceEvent
WsAllMarkPriceHandler      → WsAllMarkPriceEvent
WsKlineHandler             → *WsKlineEvent
WsContinuousKlineHandler   → *WsContinuousKlineEvent
WsMiniMarketTickerHandler   → *WsMiniMarketTickerEvent
WsAllMiniMarketTickerHandler → WsAllMiniMarketTickerEvent
WsMarketTickerHandler      → *WsMarketTickerEvent
WsAllMarketTickerHandler   → WsAllMarketTickerEvent
WsBookTickerHandler        → *WsBookTickerEvent
WsLiquidationOrderHandler  → *WsLiquidationOrderEvent
WsDepthHandler             → *WsDepthEvent
WsUserDataHandler          → *WsUserDataEvent
```

### WebSocket Event Struct（现货）

```
WsPartialDepthEvent, WsDepthEvent, WsKlineEvent, WsKline
WsAggTradeEvent, WsTradeEvent, WsCombinedTradeEvent
WsUserDataEvent (多态)
  ├─ WsOutboundAccountPosition
  ├─ WsExecutionReport
  ├─ WsBalanceUpdate
  └─ WsListStatus
WsMarketStatEvent, WsAllMarketsStatEvent
WsMiniMarketsStatEvent, WsAllMiniMarketsStatEvent
WsBookTickerEvent, WsCombinedBookTickerEvent
WsAnnouncementEvent, WsAnnouncementParam
```

### WebSocket Event Struct（合约）

```
WsAggTradeEvent, WsMarkPriceEvent, WsAllMarkPriceEvent
WsKlineEvent, WsKline
WsContinuousKlineEvent, WsContinuousKline
WsMiniMarketTickerEvent, WsAllMiniMarketTickerEvent
WsMarketTickerEvent, WsAllMarketTickerEvent
WsBookTickerEvent, WsCombinedBookTickerEvent
WsLiquidationOrderEvent, WsDepthEvent
WsUserDataEvent (多态)
  ├─ WsUserDataMarginCall
  ├─ WsUserDataAccountUpdate
  ├─ WsUserDataOrderTradeUpdate
  ├─ WsUserDataAccountConfigUpdate
  ├─ WsUserDataAlgoUpdate
  └─ WsUserDataConditionalOrderTriggerReject
WsComposition, WsCompositiveIndexEvent
```
