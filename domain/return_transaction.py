"""
Return Transaction Entity Class
继承自 Transaction 基类，演示面向对象编程的继承和多态
"""

from datetime import datetime
from domain.sale_item import SaleItem
from domain.transaction import Transaction


class ReturnTransaction(Transaction):
    """
    退货交易类
    继承自 Transaction 基类，实现退货特定的业务逻辑
    演示继承和多态的使用
    """
    
    def __init__(self, return_id: str = None, original_sale_id: str = None):
        """
        初始化退货交易
        
        Args:
            return_id: 退货ID，如果为None则自动生成
            original_sale_id: 原始销售ID
        """
        # 先调用父类构造函数
        super().__init__(return_id)
        # 退货特有的属性
        self.original_sale_id = original_sale_id
        # 为了向后兼容，保留 return_id 属性（指向 transaction_id）
        self.return_id = self.transaction_id
    
    def _generate_id(self) -> str:
        """
        生成退货ID（实现抽象方法，演示多态）
        
        Returns:
            str: 退货ID
        """
        return f"RET-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def get_total_amount(self) -> float:
        """
        计算总退款金额（实现抽象方法，演示多态）
        
        Returns:
            float: 总退款金额
        """
        return sum(item.get_subtotal() for item in self.items)
    
    def get_total_refund(self) -> float:
        """
        计算总退款金额（保留原有方法名，向后兼容）
        
        Returns:
            float: 总退款金额
        """
        return self.get_total_amount()
    
    def complete(self):
        """
        完成退货交易（实现抽象方法，演示多态）
        注意：退货交易的完成不需要支付参数，展示多态的灵活性
        """
        self.is_completed = True
    
    def complete_return(self):
        """
        完成退货交易（保留原有方法名，向后兼容）
        """
        self.complete()
    
    def get_transaction_type(self) -> str:
        """
        获取交易类型（实现抽象方法，演示多态）
        
        Returns:
            str: 交易类型名称
        """
        return "Return"
    
    def __str__(self):
        """字符串表示（重写父类方法，演示多态）"""
        items_str = "\n".join(f"  - {item}" for item in self.items)
        status = "Completed" if self.is_completed else "In Progress"
        return f"Return {self.transaction_id} ({status})\nOriginal Sale: {self.original_sale_id}\n{items_str}\nTotal Refund: ${self.get_total_amount():.2f}"
    
    def __repr__(self):
        """对象表示"""
        return f"ReturnTransaction(transaction_id='{self.transaction_id}', items={len(self.items)}, refund={self.get_total_amount()})"
