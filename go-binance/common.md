# 公共模块 (common)

> **模块路径**: `github.com/adshao/go-binance/v2/common`
> **相关文档**: [SKILL.md](../SKILL.md) | [reference.md](./reference.md)

公共模块包含签名、错误处理、限流等跨模块共享的功能。

---

## 目录

1. [签名](#1-签名)
2. [错误处理](#2-错误处理)
3. [限流](#3-限流)
4. [辅助函数](#4-辅助函数)
5. [类型索引](#5-类型索引)

---

## 1. 签名

### 1.1 签名函数 (sign.go)

`sign.go` 提供多种签名算法的统一接口。

```go
import "github.com/adshao/go-binance/v2/common"
```

#### 签名工厂函数

```go
signFunc, err := common.SignFunc(common.KeyTypeHmac) // 默认 HMAC-SHA256
sign, err := signFunc(secretKey, message)
```

#### HMAC-SHA256（默认，推荐）

```go
sign, err := common.HmacSHA256Encrypt(message, secretKey)
```

#### HMAC-SHA512

```go
sign, err := common.HmacSHA512Encrypt(message, secretKey)
```

#### RSA-SHA256

```go
sign, err := common.RSAEncrypt(message, privateKey)
```

#### ED25519

```go
sign, err := common.Ed25519Sign(message, privateKey)
```

### 1.2 密钥类型常量

| 常量 | 值 | 说明 |
|------|-----|------|
| `KeyTypeHmac` | `"HMAC"` | HMAC 签名 |
| `KeyTypeRsa` | `"RSA"` | RSA 签名 |
| `KeyTypeEd25519` | `"ED25519"` | ED25519 签名 |

---

## 2. 错误处理

### 2.1 错误类型 (errors.go)

```go
import "github.com/adshao/go-binance/v2/common"
```

#### APIError

Binance API 返回的业务错误（如余额不足、参数错误等）：

```go
order, err := client.NewCreateOrderService().Symbol("BTCUSDT").Do(ctx)
if err != nil {
    if apiErr, ok := err.(*common.APIError); ok {
        fmt.Printf("API错误: Code=%d Message=%s\n", apiErr.Code, apiErr.Message)
        fmt.Printf("原始响应: %s\n", apiErr.Response)
    }
}
```

**常见错误码**:

| Code | 含义 | 解决方案 |
|------|------|----------|
| `-1013` | Invalid quantity | 检查数量精度 |
| `-2015` | Invalid IP | 添加 IP 到白名单 |
| `-1021` | Timestamp invalid | 同步系统时间 |
| `-1003` | Too many requests | 降低请求频率 |
| `-4000` | Invalid symbol | 检查交易对格式 |
| `-1022` | Signature invalid | 检查 secret key |
| `-2011` | Unknown order | 检查订单ID |
| `-2019` | Balance insufficient | 检查余额 |
| `-1016` | Service unavailable | 稍后重试 |
| `-1010` | Too many new orders | 降低下单频率 |

#### RequestError

网络请求错误（超时、连接失败等）：

```go
if reqErr, ok := err.(*common.RequestError); ok {
    fmt.Printf("网络错误: %v\n", reqErr.Err)
}
```

#### 错误判断辅助函数

```go
if common.IsAPIError(err) {
    // 处理 API 错误
}
```

### 2.2 错误结构体

```go
// APIError
type APIError struct {
    Code    int64   // 错误码
    Message string  // 错误消息
    Response []byte // 原始响应（当 Code 和 Message 无效时）
}
```

---

## 3. 限流

### 3.1 权重追踪 (UsedWeight)

每个 API 请求消耗权重，`UsedWeight` 追踪已使用的权重：

```go
// 客户端已内置权重追踪
client := binance.NewClient(apiKey, secretKey)

// 获取当前已使用权重
fmt.Printf("当前已使用权重: %d\n", client.UsedWeight.Used)
fmt.Printf("最近1分钟已使用权重: %d\n", client.UsedWeight.Used1M)
```

### 3.2 订单计数 (OrderCount)

追踪订单数量（用于防刷）：

```go
fmt.Printf("10秒内订单数: %d\n", client.OrderCount.Count10s)
fmt.Printf("24h内订单数: %d\n", client.OrderCount.Count1d)
```

### 3.3 权重更新

权重信息会在每次请求后自动从响应头更新：

```
X-MBX-USED-WEIGHT: <weight>
X-MBX-USED-WEIGHT-1M: <weight>
X-SAPI-REQUEST-ID: <id>
```

---

## 4. 辅助函数 (helpers.go)

```go
import "github.com/adshao/go-binance/v2/common"
```

| 函数 | 说明 |
|------|------|
| `AmountToLotSize(amount, minQty, stepSize string, precision int)` | 将数量转为合法的批量大小 |
| `ToJSONList(v []byte)` | 将 JSON 数组转为列表 |
| `ToInt(digit any)` | 转换为 int |
| `ToInt64(digit any)` | 转换为 int64 |
| `BaseUID()` | 生成基础 UID |
| `Uuid22()` | 生成 22 位 UUID |
| `GenerateSpotId()` | 生成现货 ID |
| `GenerateSwapId()` | 生成合约 ID |

---

## 5. 类型索引

### Struct 一览

| 类型名 | 说明 |
|--------|------|
| `UsedWeight` | 已使用权重 |
| `OrderCount` | 订单计数 |
| `APIError` | API 错误 |
| `PriceLevel` | 深度价格级别 |

### Type Alias 一览

| 类型名 | 说明 |
|--------|------|
| `WsApiMethodType` | WebSocket API 方法类型 |

### Struct 字段

```go
// UsedWeight
type UsedWeight struct {
    Used   int64 // 当前已使用权重
    Used1M int64 // 最近1分钟已使用权重
}

// OrderCount
type OrderCount struct {
    Count10s int64 // 10秒内订单数
    Count1d  int64 // 24h内订单数
}

// APIError
type APIError struct {
    Code     int64   // 错误码
    Message  string  // 错误消息
    Response []byte // 原始响应
}

// PriceLevel (见 common/priceLevel.go)
type PriceLevel struct {
    Price    string // 价格
    Quantity string // 数量
}
```

### Method 一览

```go
// 从 HTTP 响应头更新权重
func (*UsedWeight) UpdateByHeader(header http.Header)

// 从 HTTP 响应头更新订单计数
func (*OrderCount) UpdateByHeader(header http.Header)

// 解析价格级别
func (*PriceLevel) Parse() (float64, float64, error)
```

### Function 一览

| 函数 | 签名 |
|------|------|
| `HmacSHA256Encrypt` | `(message, secretKey string) (*string, error)` |
| `HmacSHA512Encrypt` | `(message, secretKey string) (*string, error)` |
| `RSAEncrypt` | `(message, secretKey string) (*string, error)` |
| `Ed25519Sign` | `(message, secretKey string) (*string, error)` |
| `SignFunc` | `(keyType string) (func(string, string) (*string, error), error)` |
| `IsAPIError` | `(e error) bool` |
| `AmountToLotSize` | `(amount, minQty, stepSize string, precision int) string` |
| `ToJSONList` | `(v []byte) []byte` |
| `ToInt` | `(digit any) (int, error)` |
| `ToInt64` | `(digit any) (int64, error)` |
| `BaseUID` | `() string` |
| `Uuid22` | `() string` |
| `GenerateSpotId` | `() string` |
| `GenerateSwapId` | `() string` |
