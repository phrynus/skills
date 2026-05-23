# 测试网配置参考

## 目录

1. [现货测试网](#1-现货测试网)
2. [合约测试网](#2-合约测试网)
3. [测试网 API Key](#3-测试网-api-key)
4. [端点对照表](#4-端点对照表)

---

## 1. 现货测试网

```go
import "github.com/adshao/go-binance/v2"

binance.UseTestnet = true
client := binance.NewClient(apiKey, secretKey)
```

---

## 2. 合约测试网

```go
import "github.com/adshao/go-binance/v2/futures"

futures.UseTestnet = true
futuresClient := futures.NewClient(apiKey, secretKey)
```

---

## 3. 测试网 API Key

测试网与主网账户独立，需要单独申请：

1. 访问 https://testnet.binance.vision
2. 登录后创建 API Key
3. **主网 Key 不能用于测试网**

---

## 4. 端点对照表

| 类型 | 主网 | 测试网 |
|------|------|--------|
| 现货 API | `api.binance.com` | `testnet.binance.vision` |
| 现货 WebSocket | `stream.binance.com:9443` | `stream.testnet.binance.vision` |
| USDT-M 合约 API | `fapi.binance.com` | `testnet.binancefuture.com` |
| USDT-M 合约 WebSocket | `fstream.binance.com` | `stream.binancefuture.com` |
| 币本位合约 API | `dapi.binance.com` | `testnet.binancefuture.com` |
| 期权 API | `eapi.binance.com` | `testnet.binancefuture.com` |
| 组合保证金 | `papi.binance.com` | `testnet.binance.vision` |
