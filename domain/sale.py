"""
Sale Entity Class
继承自 Transaction 基类，演示面向对象编程的继承和多态
"""

from datetime import datetime
from domain.sale_item import SaleItem
from domain.transaction import Transaction


class Sale(Transaction):
    """
    销售交易类
    继承自 Transaction 基类，实现销售特定的业务逻辑
    演示继承和多态的使用
    """
    
    def __init__(self, sale_id: str = None):
        """
        初始化销售交易
        
        Args:
            sale_id: 销售ID，如果为None则自动生成
        """
        # 先调用父类构造函数
        super().__init__(sale_id)
        # Sale specific attributes
        self.payment_method = None
        self.payment_amount = 0.0
        
        # Compatibility aliases
        self.sale_id = self.transaction_id  # old attribute name
        self.sale_time = self.transaction_time  # maintain old attribute
    
    def _generate_id(self) -> str:
        """
        生成销售ID（实现抽象方法，演示多态）
        
        Returns:
            str: 销售ID
        """
        return f"SALE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def get_total_amount(self) -> float:
        """
        计算总金额（实现抽象方法，演示多态）
        
        Returns:
            float: 总金额
        """
        return sum(item.get_subtotal() for item in self.items)
    
    def get_total(self) -> float:
        """
        计算总金额（保留原有方法名，向后兼容）
        
        Returns:
            float: 总金额
        """
        return self.get_total_amount()
    
    def complete(self, payment_method: str, payment_amount: float):
        """
        完成销售交易（实现抽象方法，演示多态）
        
        Args:
            payment_method: 支付方式
            payment_amount: 支付金额
        """
        self.payment_method = payment_method
        self.payment_amount = payment_amount
        self.is_completed = True
    
    def complete_sale(self, payment_method: str, payment_amount: float):
        """
        完成销售交易（保留原有方法名，向后兼容）
        
        Args:
            payment_method: 支付方式
            payment_amount: 支付金额
        """
        self.complete(payment_method, payment_amount)
    
    def get_change(self) -> float:
        """
        计算找零
        
        Returns:
            float: 找零金额
        """
        if self.is_completed:
            return self.payment_amount - self.get_total_amount()
        return 0.0
    
    def get_transaction_type(self) -> str:
        """
        获取交易类型（实现抽象方法，演示多态）
        
        Returns:
            str: 交易类型名称
        """
        return "Sale"
    
    def __str__(self):
        """字符串表示（重写父类方法，演示多态）"""
        items_str = "\n".join(f"  - {item}" for item in self.items)
        status = "Completed" if self.is_completed else "In Progress"
        return f"Sale {self.transaction_id} ({status})\n{items_str}\nTotal: ${self.get_total_amount():.2f}"
    
    def __repr__(self):
        """对象表示"""
        return f"Sale(transaction_id='{self.transaction_id}', items={len(self.items)}, total={self.get_total_amount()})"
