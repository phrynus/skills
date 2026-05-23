# 费率限制参考

## 目录

1. [API 请求限制](#1-api-请求限制)
2. [权重计算](#2-权重计算)
3. [Rate Limit Headers](#3-rate-limit-headers)
4. [防止限流](#4-防止限流)

---

## 1. API 请求限制

| 接口类型 | 限制 | 说明 |
|----------|------|------|
| 现货/杠杆 | 1200 请求/分钟 | 按权重计算 |
| USDT-M 合约 | 2400 请求/分钟 | 按权重计算 |
| 币本位合约 | 2400 请求/分钟 | 按权重计算 |
| 期权 | 1200 请求/分钟 | 按权重计算 |
| WebSocket | 5 连接/IP/分钟 | 连接数限制 |
| WebSocket 用户流 | 30 连接/IP/分钟 | 用户数据流 |

---

## 2. 权重计算

每个 API 请求都有对应的权重：

| 操作 | 权重 |
|------|------|
| 查询类（/exchangeInfo, /ticker 等）| 1-10 |
| 下单类（/order 等）| 1 |
| 账户类（/account 等）| 5-10 |
| 合约下单 | 1-2 |

**示例**: 现货账户查询权重 = 5，所以 1200 / 5 = 240 次/分钟

---

## 3. Rate Limit Headers

每次请求响应头包含限流信息：

```
X-MBX-USED-WEIGHT: <weight>
X-MBX-USED-WEIGHT-1M: <weight>
X-SAPI-USED-QUOTA-WEIGHT: <weight>
```

客户端已内置权重追踪：

```go
client := binance.NewClient(apiKey, secretKey)

// 当前已使用权重
fmt.Println(client.UsedWeight.Used)
fmt.Println(client.UsedWeight.Used1M)

// 10秒内订单数
fmt.Println(client.OrderCount.Count10s)
// 24h内订单数
fmt.Println(client.OrderCount.Count1d)
```

---

## 4. 防止限流

### 4.1 简单限流

```go
import "time"

client := binance.NewClient(apiKey, secretKey)
lastRequest := time.Now()

for _, symbol := range symbols {
    // 确保请求间隔至少 50ms
    if time.Since(lastRequest) < 50*time.Millisecond {
        time.Sleep(50 * time.Millisecond)
    }
    ticker, _ := client.NewListPricesService().Symbol(symbol).Do(ctx)
    fmt.Println(ticker)
    lastRequest = time.Now()
}
```

### 4.2 并发控制（信号量）

```go
import "golang.org/x/sync/semaphore"

func concurrentCalls(symbols []string) {
    sem := semaphore.NewWeighted(10) // 最多10个并发

    for _, symbol := range symbols {
        sem.Acquire(ctx, 1)
        go func(s string) {
            defer sem.Release(1)
            ticker, _ := client.NewListPricesService().Symbol(s).Do(ctx)
            fmt.Println(ticker)
        }(symbol)
    }
}
```

### 4.3 限流器

```go
type RateLimiter struct {
    mu       sync.Mutex
    last     time.Time
    interval time.Duration
}

func NewRateLimiter(interval time.Duration) *RateLimiter {
    return &RateLimiter{interval: interval}
}

func (r *RateLimiter) Wait() {
    r.mu.Lock()
    defer r.mu.Unlock()
    if time.Since(r.last) < r.interval {
        time.Sleep(r.interval - time.Since(r.last))
    }
    r.last = time.Now()
}
```

### 4.4 指数退避

```go
func withRetry(fn func() error, maxRetries int, baseDelay time.Duration) error {
    var err error
    for i := 0; i < maxRetries; i++ {
        err = fn()
        if err == nil {
            return nil
        }
        // 只对网络错误重试
        if _, ok := err.(*common.RequestError); !ok {
            return err // API 错误不重试
        }
        time.Sleep(baseDelay * time.Duration(i+1))
    }
    return fmt.Errorf("达到最大重试次数 %d: %v", maxRetries, err)
}
```
