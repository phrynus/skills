# go-binance 进阶参考

进阶参考资料索引，提供费率限制、最佳实践、测试网配置、项目结构等进阶内容。

> **相关文档**: [SKILL.md](./SKILL.md) | [spot.md](./spot.md) | [futures.md](./futures.md) | [common.md](./common.md) | [websocket.md](./websocket.md)

---

## 参考文档索引

| 文档 | 内容 |
|------|------|
| [reference-rate-limit.md](./reference-rate-limit.md) | API 费率限制、权重计算、防止限流 |
| [reference-best-practices.md](./reference-best-practices.md) | Context 超时、HTTP 复用、重试机制、Gin 集成 |
| [reference-testnet.md](./reference-testnet.md) | 测试网配置、测试网 API Key |
| [reference-project-structure.md](./reference-project-structure.md) | 项目目录结构、服务文件命名约定 |
| [reference-error-codes.md](./reference-error-codes.md) | 现货/杠杆/合约常见错误码速查 |
| [reference-type-index.md](./reference-type-index.md) | 完整类型索引（按模块分类）|

---

## 快速导航

### 费率限制
```go
// 权重追踪（自动更新）
fmt.Println(client.UsedWeight.Used)   // 当前已使用权重
fmt.Println(client.UsedWeight.Used1M) // 最近1分钟已使用权重

// 订单计数
fmt.Println(client.OrderCount.Count10s) // 10秒内订单数
fmt.Println(client.OrderCount.Count1d)  // 24h内订单数
```

### 错误处理
```go
if apiErr, ok := err.(*common.APIError); ok {
    fmt.Printf("API错误: %d - %s\n", apiErr.Code, apiErr.Message)
}
if reqErr, ok := err.(*common.RequestError); ok {
    fmt.Printf("网络错误: %v\n", reqErr.Err)
}
```

### 完整类型索引

各模块完整的类型定义和方法列表：
- [reference-type-index.md](./reference-type-index.md) - 按模块分类的完整类型列表

### 常见场景

| 场景 | 参考文档 |
|------|----------|
| 限流了怎么办 | `reference-rate-limit.md` |
| 如何处理超时和网络错误 | `reference-best-practices.md` |
| 如何使用测试网 | `reference-testnet.md` |
| 订单报错代码查询 | `reference-error-codes.md` |
| 想知道有哪些类型可用 | `reference-type-index.md` |
| 想知道项目结构 | `reference-project-structure.md` |
