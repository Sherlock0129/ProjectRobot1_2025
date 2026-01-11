# 面向对象编程三个特性说明

本POS系统现在完整实现了面向对象编程的三个主要特性：**封装**、**继承**和**多态**。

## 1. 封装（Encapsulation）

封装是指将数据和方法封装在类中，通过接口访问和操作数据。

### 示例：

```python
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock  # 私有数据
    
    def reduce_stock(self, quantity):  # 公共接口
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
```

- **数据封装**：`stock` 等属性封装在类中
- **方法封装**：通过 `reduce_stock()` 等方法操作数据，而不是直接访问属性
- **私有方法**：使用下划线前缀（如 `_initialize_sample_products`）表示内部使用

## 2. 继承（Inheritance）

继承允许一个类（子类）继承另一个类（父类）的属性和方法。

### 类层次结构：

```
Transaction (抽象基类)
├── Sale (销售交易)
└── ReturnTransaction (退货交易)
```

### 代码示例：

```python
from abc import ABC, abstractmethod

class Transaction(ABC):
    """交易抽象基类"""
    def __init__(self, transaction_id=None):
        self.transaction_id = transaction_id or self._generate_id()
        self.items = []
        self.transaction_time = datetime.now()
        self.is_completed = False
    
    @abstractmethod
    def _generate_id(self):
        pass
    
    def add_item(self, item):
        """所有子类共享的方法"""
        self.items.append(item)

class Sale(Transaction):
    """销售交易类，继承自 Transaction"""
    def _generate_id(self):
        return f"SALE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def get_total_amount(self):
        return sum(item.get_subtotal() for item in self.items)
```

**继承的好处**：
- 代码复用：子类自动获得父类的所有属性和方法
- 统一的接口：所有交易类型都有相同的基础结构
- 易于扩展：添加新的交易类型只需继承基类

## 3. 多态（Polymorphism）

多态允许不同的类对同一方法有不同的实现，但通过统一的接口调用。

### 多态示例：

#### 3.1 抽象方法的多态实现

```python
class Transaction(ABC):
    @abstractmethod
    def get_total_amount(self) -> float:
        """抽象方法，子类必须实现"""
        pass
    
    @abstractmethod
    def _generate_id(self) -> str:
        """抽象方法，不同子类有不同的ID生成规则"""
        pass

class Sale(Transaction):
    def _generate_id(self):
        return f"SALE-{datetime.now().strftime('%Y%m%d%H%M%S')}"  # Sale的实现
    
    def get_total_amount(self):
        return sum(item.get_subtotal() for item in self.items)

class ReturnTransaction(Transaction):
    def _generate_id(self):
        return f"RET-{datetime.now().strftime('%Y%m%d%H%M%S')}"  # ReturnTransaction的实现
    
    def get_total_amount(self):
        return sum(item.get_subtotal() for item in self.items)  # 相同的逻辑，但可以是不同的实现
```

#### 3.2 使用多态的代码示例

```python
# 使用基类类型处理不同的子类
transactions: list[Transaction] = [Sale(), ReturnTransaction()]

for transaction in transactions:
    # 多态调用：相同的接口，不同的实现
    total = transaction.get_total_amount()  # 每个子类有自己的实现
    trans_type = transaction.get_transaction_type()  # 返回不同的类型名称
    print(f"{trans_type}: {total}")
```

**多态的好处**：
- 灵活性：同一接口可以处理不同的对象类型
- 可扩展性：添加新的交易类型不需要修改使用代码
- 代码简洁：通过统一接口处理不同类型的对象

## 完整示例

```python
from domain.sale import Sale
from domain.return_transaction import ReturnTransaction
from domain.product import Product
from domain.sale_item import SaleItem

# 创建产品
product = Product("P001", "苹果", 5.50, 100)
item = SaleItem(product, 2)

# 创建不同的交易类型（继承）
sale = Sale()
return_transaction = ReturnTransaction()

# 使用继承的方法（封装）
sale.add_item(item)
return_transaction.add_item(item)

# 多态：相同的方法调用，不同的实现
sale_total = sale.get_total_amount()  # Sale 的实现
return_total = return_transaction.get_total_amount()  # ReturnTransaction 的实现

# 多态：使用基类类型
from domain.transaction import Transaction
transactions: list[Transaction] = [sale, return_transaction]
for transaction in transactions:
    print(f"{transaction.get_transaction_type()}: {transaction.get_total_amount()}")
```

## 总结

本POS系统现在完整实现了面向对象编程的三个核心特性：

1. **封装** ✓：数据和方法封装在类中，通过接口访问
2. **继承** ✓：`Sale` 和 `ReturnTransaction` 继承自 `Transaction` 基类
3. **多态** ✓：抽象方法在不同子类中有不同的实现

这些特性使代码更加模块化、可维护和可扩展。

