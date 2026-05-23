# 常见错误码速查

## 目录

1. [现货/杠杆错误码](#1-现货杠杆错误码)
2. [USDT-M 合约错误码](#2-usdt-m-合约错误码)
3. [错误处理代码示例](#3-错误处理代码示例)

---

## 1. 现货/杠杆错误码

| 错误码 | 含义 | 解决方案 |
|--------|------|----------|
| -1013 | Invalid quantity | 检查数量精度 |
| -2015 | Invalid IP | 添加 IP 到白名单 |
| -1021 | Timestamp invalid | 同步系统时间 |
| -1003 | Too many requests | 降低请求频率 |
| -4000 | Invalid symbol | 检查交易对格式 |
| -1022 | Signature invalid | 检查 secret key |
| -2011 | Unknown order | 检查订单ID |
| -2019 | Balance insufficient | 检查账户余额 |
| -1016 | Service unavailable | 稍后重试 |
| -1010 | Too many new orders | 降低下单频率 |
| -1019 | Stop price would trigger immediately | 调整止损价格 |
| -1020 | Not a valid TIF | 使用有效的 TimeInForce |
| -2010 | New order rejected | 查看详细错误消息 |
| -2013 | Order does not exist | 检查订单ID |

---

## 2. USDT-M 合约错误码

| 错误码 | 含义 | 解决方案 |
|--------|------|----------|
| -5021 | Quantities are outside permissible range | 检查数量范围 |
| -5022 | Invalid quantity | 检查精度 |
| -5023 | Invalid initial leverage | 检查杠杆值 |
| -5024 | Leverage 5 is not allowed | 调整杠杆 |
| -5025 | Invalid margin type | 使用正确的保证金类型 |
| -5036 | Insufficient margin balance | 增加保证金 |
| -5045 | Invalid position side | 检查持仓方向 |
| -5046 | Invalid working type | 使用 MARK_PRICE 或 CONTRACT_PRICE |
| -5050 | Invalid reduce only | 检查 reduceOnly 参数 |
| -5061 | Order would trigger immediately | 调整触发价格 |
| -9000 | This transaction at this time is prohibited | 禁止交易时间 |
| -9020 | This time can't close position | 检查仓位状态 |

---

## 3. 错误处理代码示例

```go
import "github.com/adshao/go-binance/v2/common"

func handleError(err error) {
    if apiErr, ok := err.(*common.APIError); ok {
        switch apiErr.Code {
        case -1013:
            log.Println("数量格式错误")
        case -2015:
            log.Println("IP未授权，请检查API白名单")
        case -1021:
            log.Println("时间戳偏差过大，请同步系统时间")
        case -1003:
            log.Println("触发限流，请降低请求频率")
        case -4000:
            log.Println("交易对不存在")
        case -2019:
            log.Println("余额不足")
        default:
            log.Printf("API错误 [%d]: %s", apiErr.Code, apiErr.Message)
        }
        return
    }

    if reqErr, ok := err.(*common.RequestError); ok {
        log.Printf("网络错误: %v", reqErr.Err)
        return
    }

    log.Printf("未知错误: %v", err)
}
```
