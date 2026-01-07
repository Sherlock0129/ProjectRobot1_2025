"""
销售实体类
"""

from datetime import datetime
from typing import List
from domain.sale_item import SaleItem


class Sale:
    """销售类，表示一次完整的销售交易"""
    
    def __init__(self, sale_id: str = None):
        """
        初始化销售
        
        Args:
            sale_id: 销售ID，如果为None则自动生成
        """
        self.sale_id = sale_id or f"SALE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.items: List[SaleItem] = []
        self.sale_time = datetime.now()
        self.payment_method = None
        self.payment_amount = 0.0
        self.is_completed = False
    
    def add_item(self, item: SaleItem):
        """
        添加销售项
        
        Args:
            item: 销售项对象
        """
        self.items.append(item)
    
    def get_total(self) -> float:
        """
        计算总金额
        
        Returns:
            float: 总金额
        """
        return sum(item.get_subtotal() for item in self.items)
    
    def complete_sale(self, payment_method: str, payment_amount: float):
        """
        完成销售
        
        Args:
            payment_method: 支付方式
            payment_amount: 支付金额
        """
        self.payment_method = payment_method
        self.payment_amount = payment_amount
        self.is_completed = True
    
    def get_change(self) -> float:
        """
        计算找零
        
        Returns:
            float: 找零金额
        """
        if self.is_completed:
            return self.payment_amount - self.get_total()
        return 0.0
    
    def __str__(self):
        items_str = "\n".join(f"  - {item}" for item in self.items)
        status = "已完成" if self.is_completed else "进行中"
        return f"销售单 {self.sale_id} ({status})\n{items_str}\n总计: ¥{self.get_total():.2f}"
    
    def __repr__(self):
        return f"Sale(sale_id='{self.sale_id}', items={len(self.items)}, total={self.get_total()})"

