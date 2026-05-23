# 最佳实践参考

## 目录

1. [Context 超时控制](#1-context-超时控制)
2. [复用 HTTP 客户端](#2-复用-http-客户端)
3. [错误重试机制](#3-错误重试机制)
4. [Gin 框架集成](#4-gin-框架集成)
5. [批量操作优化](#5-批量操作优化)

---

## 1. Context 超时控制

```go
import "context"

// 5秒超时
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

ticker, err := client.NewListPricesService().Symbol("BTCUSDT").Do(ctx)
if err != nil {
    if ctx.Err() == context.DeadlineExceeded {
        log.Println("请求超时")
    }
}
```

**带取消的 Context**:

```go
ctx, cancel := context.WithCancel(context.Background())
defer cancel()

// 在另一个 goroutine 中取消
go func() {
    time.Sleep(10 * time.Second)
    cancel()
}()
```

---

## 2. 复用 HTTP 客户端

```go
import "net/http"

httpClient := &http.Client{
    Timeout: 10 * time.Second,
    Transport: &http.Transport{
        MaxIdleConns:        100,
        MaxIdleConnsPerHost: 10,
    },
}

client := binance.NewClient(apiKey, secretKey)
client.HTTPClient = httpClient
```

---

## 3. 错误重试机制

```go
func withRetry(fn func() error, maxRetries int, delay time.Duration) error {
    var err error
    for i := 0; i < maxRetries; i++ {
        err = fn()
        if err == nil {
            return nil
        }
        // 只对网络错误重试
        if _, ok := err.(*common.RequestError); !ok {
            return err // API 错误不重试，直接返回
        }
        time.Sleep(delay * time.Duration(i+1)) // 指数退避
    }
    return fmt.Errorf("达到最大重试次数 %d: %v", maxRetries, err)
}

// 使用示例
ticker, err := withRetry(
    func() error {
        t, e := client.NewListPricesService().Symbol("BTCUSDT").Do(ctx)
        _ = t
        return e
    },
    3,
    100*time.Millisecond,
)
```

---

## 4. Gin 框架集成

```go
package main

import (
    "github.com/gin-gonic/gin"
    "github.com/adshao/go-binance/v2"
)

func main() {
    r := gin.Default()
    client := binance.NewClient(apiKey, secretKey)

    // 获取行情
    r.GET("/ticker/:symbol", func(c *gin.Context) {
        symbol := c.Param("symbol")
        ticker, err := client.NewListPricesService().Symbol(symbol).Do(c.Request.Context())
        if err != nil {
            c.JSON(500, gin.H{"error": err.Error()})
            return
        }
        c.JSON(200, ticker)
    })

    // 创建订单
    r.POST("/order", func(c *gin.Context) {
        var req struct {
            Symbol   string `json:"symbol"`
            Side     string `json:"side"`
            Type     string `json:"type"`
            Quantity string `json:"quantity"`
            Price    string `json:"price"`
        }
        if err := c.ShouldBindJSON(&req); err != nil {
            c.JSON(400, gin.H{"error": err.Error()})
            return
        }

        order, err := client.NewCreateOrderService().
            Symbol(req.Symbol).
            Side(req.Side).
            Type(req.Type).
            Quantity(req.Quantity).
            Price(req.Price).
            Do(c.Request.Context())

        if err != nil {
            c.JSON(500, gin.H{"error": err.Error()})
            return
        }
        c.JSON(200, order)
    })

    r.Run(":8080")
}
```

---

## 5. 批量操作优化

### 5.1 现货批量下单（最多5个/请求）

```go
services := []*binance.CreateOrderService{
    client.NewCreateOrderService().
        Symbol("BTCUSDT").
        Side(binance.SideTypeBuy).
        Type(binance.OrderTypeLimit).
        TimeInForce(binance.TimeInForceTypeGTC).
        Quantity("0.001").
        Price("50000.00"),
    client.NewCreateOrderService().
        Symbol("ETHUSDT").
        Side(binance.SideTypeBuy).
        Type(binance.OrderTypeLimit).
        TimeInForce(binance.TimeInForceTypeGTC).
        Quantity("0.01").
        Price("3000.00"),
}
resp, err := client.NewCreateBatchOrdersService(services).Do(ctx)
for _, r := range resp.Orders {
    fmt.Printf("订单 %d: %s\n", r.OrderID, r.Status)
}
```

### 5.2 合约批量下单（最多5个/请求）

```go
orders := []*futures.CreateOrderService{
    futuresClient.NewCreateOrderService().Symbol("BTCUSDT").Side(futures.SideTypeBuy)...
    futuresClient.NewCreateOrderService().Symbol("ETHUSDT").Side(futures.SideTypeBuy)...
}
resp, err := futuresClient.NewCreateBatchOrdersService(orders).Do(ctx)
```

### 5.3 批量取消订单

```go
// 现货
results, err := client.NewCancelMultipleOrdersService().
    Symbol("BTCUSDT").
    OrderIDList([]int64{123, 456, 789}).
    Do(ctx)

// 合约
results, err := futuresClient.NewCancelMultipleOrdersService().
    Symbol("BTCUSDT").
    OrderIDList([]int64{123, 456, 789}).
    Do(ctx)
```

### 5.4 取消所有开放订单

```go
// 现货
err = client.NewCancelAllOpenOrdersService().Symbol("BTCUSDT").Do(ctx)

// 合约
err = futuresClient.NewCancelAllOpenOrdersService().Symbol("BTCUSDT").Do(ctx)
```
