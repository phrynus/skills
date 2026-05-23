# 项目结构参考

## 目录

1. [目录结构](#1-目录结构)
2. [服务文件命名约定](#2-服务文件命名约定)

---

## 1. 目录结构

```
github.com/adshao/go-binance/
└── v2/
    ├── client.go                          # 主客户端（现货）
    ├── request.go                         # HTTP 请求处理
    ├── doc.go                             # 包文档
    │
    ├── common/
    │   ├── errors.go                     # APIError, RequestError
    │   ├── sign.go                        # 签名函数 (HMAC/RSA/ED25519)
    │   ├── helpers.go                    # 辅助函数 (ToInt64, AmountToLotSize...)
    │   ├── priceLevel.go                 # PriceLevel (深度档位)
    │   ├── types.go                      # UsedWeight, OrderCount
    │   └── websocket/
    │       ├── client.go                 # WebSocket 客户端核心
    │       └── types.go                  # WebSocket API 类型
    │
    ├── futures/                          # USDT-M 永续合约
    │   ├── client.go                     # 合约客户端
    │   ├── account_service.go           # 账户服务
    │   ├── order_service.go             # 订单服务
    │   ├── position_service.go          # 持仓服务
    │   ├── trade_service.go             # 交易服务
    │   ├── kline_service.go             # K线服务
    │   ├── depth_service.go             # 深度服务
    │   ├── ticker_service.go            # Ticker 服务
    │   ├── websocket/
    │   │   ├── websocket.go            # WebSocket 配置
    │   │   └── user_data_service.go    # 用户数据流
    │   └── *_service.go                 # 其他服务
    │
    ├── delivery/                        # 币本位合约
    │   ├── client.go
    │   ├── account_service.go
    │   ├── order_service.go
    │   └── position_service.go
    │
    ├── options/                        # 期权
    │   ├── client.go
    │   ├── account_service.go
    │   ├── order_service.go
    │   └── *_service.go
    │
    ├── portfolio/                      # 组合保证金
    │   └── balance_service.go
    │
    ├── subaccount/                    # 子账户
    ├── savings/                      # 理财/储蓄
    ├── convert/                     # 快速转换
    │
    ├── spot/                        # 独立 Spot 模块 (v2.7.0+)
    ├── margin/                      # 独立 Margin 模块 (v2.7.0+)
    ├── wallet/                      # 钱包
    │
    ├── order_service.go            # 现货订单
    ├── account_service.go         # 现货账户
    ├── kline_service.go
    ├── depth_service.go
    ├── trade_service.go
    ├── ticker_service.go
    ├── websocket_service.go       # 现货 WebSocket
    ├── margin_service.go          # 杠杆
    ├── margin_order_service.go    # 杠杆订单
    └── *_service.go               # 其他服务
```

---

## 2. 服务文件命名约定

| 文件前缀 | 用途 |
|----------|------|
| `[name]_service.go` | 服务定义（Builder 模式）|
| `[name]_service_test.go` | 测试文件 |

### 服务命名模式

每个服务文件遵循 Builder 模式：

```go
// 文件: kline_service.go

// 服务 Struct（用于链式调用）
type KlinesService struct {
    c *Client
    symbol string
    interval string
    limit *int
    startTime *int64
    endTime *int64
}

// 链式方法
func (s *KlinesService) Symbol(v string) *KlinesService { ... }
func (s *KlinesService) Interval(v string) *KlinesService { ... }
func (s *KlinesService) Limit(v int) *KlinesService { ... }
func (s *KlinesService) StartTime(v int64) *KlinesService { ... }
func (s *KlinesService) EndTime(v int64) *KlinesService { ... }
func (s *KlinesService) Do(ctx context.Context, opts ...RequestOption) ([]*Kline, error) { ... }

// 响应 Struct
type Kline struct {
    OpenTime, CloseTime, TradeNum int64
    Open, High, Low, Close, Volume string
    QuoteAssetVolume, TakerBuyBaseAssetVolume, TakerBuyQuoteAssetVolume string
}
```
