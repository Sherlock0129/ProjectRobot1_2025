# POS系统架构设计文档

## 1. 系统架构概述

本POS系统采用**三层架构**设计，遵循面向对象设计原则。

```
┌─────────────────────────────────────┐
│        用户界面层 (UI Layer)        │
│         - POSUI                     │
└─────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────┐
│      业务逻辑层 (Service Layer)      │
│  - SaleService                      │
│  - ReturnService                     │
│  - InventoryService                 │
└─────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────┐
│     领域模型层 (Domain Layer)        │
│  - Product                          │
│  - Sale                             │
│  - SaleItem                         │
│  - ReturnTransaction                │
└─────────────────────────────────────┘
```

## 2. 领域模型 (Domain Model)

### 2.1 类图结构

```
┌──────────────┐
│   Product    │
├──────────────┤
│ +product_id  │
│ +name        │
│ +price       │
│ +stock       │
├──────────────┤
│ +reduce_stock()│
│ +increase_stock()│
└──────────────┘
       ↑
       │
       │ 1
       │
┌──────────────┐      ┌──────────────┐
│  SaleItem    │      │     Sale     │
├──────────────┤      ├──────────────┤
│ +product     │──────│ +sale_id     │
│ +quantity    │      │ +items[]     │
├──────────────┤      │ +sale_time   │
│ +get_subtotal()│    │ +payment_method│
└──────────────┘      │ +payment_amount│
                      │ +is_completed│
                      ├──────────────┤
                      │ +add_item()  │
                      │ +get_total() │
                      │ +complete_sale()│
                      └──────────────┘

┌──────────────────┐
│ReturnTransaction │
├──────────────────┤
│ +return_id       │
│ +original_sale_id│
│ +items[]         │
│ +return_time     │
│ +is_completed    │
├──────────────────┤
│ +add_item()      │
│ +get_total_refund()│
│ +complete_return()│
└──────────────────┘
```

### 2.2 实体类说明

#### Product (产品)
- **职责**: 表示超市中的商品
- **属性**: 
  - `product_id`: 产品唯一标识
  - `name`: 产品名称
  - `price`: 单价
  - `stock`: 库存数量
- **方法**:
  - `reduce_stock()`: 减少库存
  - `increase_stock()`: 增加库存

#### Sale (销售)
- **职责**: 表示一次完整的销售交易
- **属性**:
  - `sale_id`: 销售单ID
  - `items`: 销售项列表
  - `sale_time`: 销售时间
  - `payment_method`: 支付方式
  - `payment_amount`: 支付金额
  - `is_completed`: 是否完成
- **方法**:
  - `add_item()`: 添加销售项
  - `get_total()`: 计算总金额
  - `complete_sale()`: 完成销售
  - `get_change()`: 计算找零

#### SaleItem (销售项)
- **职责**: 表示一次销售中的单个商品项
- **属性**:
  - `product`: 产品对象
  - `quantity`: 购买数量
- **方法**:
  - `get_subtotal()`: 计算小计

#### ReturnTransaction (退货交易)
- **职责**: 表示一次退货操作
- **属性**:
  - `return_id`: 退货单ID
  - `original_sale_id`: 原始销售单ID
  - `items`: 退货项列表
  - `return_time`: 退货时间
  - `is_completed`: 是否完成
- **方法**:
  - `add_item()`: 添加退货项
  - `get_total_refund()`: 计算退款总额
  - `complete_return()`: 完成退货

## 3. 业务逻辑层 (Service Layer)

### 3.1 服务类说明

#### InventoryService (库存服务)
- **职责**: 管理商品库存
- **主要方法**:
  - `get_product()`: 获取产品
  - `get_all_products()`: 获取所有产品
  - `add_product()`: 添加产品
  - `update_stock()`: 更新库存
  - `restore_stock()`: 恢复库存

#### SaleService (销售服务)
- **职责**: 处理销售业务逻辑
- **主要方法**:
  - `create_sale()`: 创建销售
  - `add_item_to_sale()`: 添加商品到销售
  - `complete_sale()`: 完成销售
  - `cancel_sale()`: 取消销售
  - `get_sales_history()`: 获取销售历史

#### ReturnService (退货服务)
- **职责**: 处理退货业务逻辑
- **主要方法**:
  - `create_return()`: 创建退货
  - `add_item_to_return()`: 添加商品到退货
  - `complete_return()`: 完成退货
  - `get_return_history()`: 获取退货历史
  - `find_sale_by_id()`: 查找销售单

## 4. 用户界面层 (UI Layer)

### 4.1 POSUI类
- **职责**: 提供用户交互界面
- **主要功能**:
  - 显示主菜单
  - 处理销售流程
  - 处理退货流程
  - 显示商品列表
  - 显示历史记录

## 5. 用例实现

### 5.1 处理销售用例 (Process Sale)

**系统序列图**:
```
Cashier          POSUI          SaleService    InventoryService
   │                │                │                │
   │──添加商品──────>│                │                │
   │                │──add_item()───>│                │
   │                │                │──get_product()─>│
   │                │                │<──Product──────│
   │                │                │──reduce_stock()>│
   │                │<──成功─────────│                │
   │<──显示总计──────│                │                │
   │                │                │                │
   │──完成销售──────>│                │                │
   │                │──complete_sale()>│                │
   │                │<──成功─────────│                │
   │<──收据─────────│                │                │
```

### 5.2 处理退货用例 (Handle Returns)

**系统序列图**:
```
Cashier          POSUI          ReturnService  InventoryService
   │                │                │                │
   │──添加退货商品──>│                │                │
   │                │──add_item()───>│                │
   │                │                │──get_product()─>│
   │                │                │<──Product──────│
   │                │<──成功─────────│                │
   │                │                │                │
   │──完成退货──────>│                │                │
   │                │──complete_return()>│            │
   │                │                │──restore_stock()>│
   │                │<──成功─────────│                │
   │<──退款信息──────│                │                │
```

## 6. 设计模式

### 6.1 服务层模式 (Service Layer Pattern)
- 将业务逻辑封装在服务类中
- 提供清晰的业务接口
- 便于测试和维护

### 6.2 领域模型模式 (Domain Model Pattern)
- 实体类包含业务逻辑
- 数据和行为封装在一起
- 符合面向对象设计原则

## 7. 扩展性考虑

1. **数据持久化**: 可以添加数据访问层，使用数据库存储
2. **多支付方式**: 可以扩展支付服务，支持更多支付方式
3. **报表功能**: 可以添加报表服务，生成销售报表
4. **用户管理**: 可以添加用户认证和权限管理
5. **GUI界面**: 可以使用Tkinter、PyQt等框架开发图形界面

