"""
退货交易实体类
"""

from datetime import datetime
from typing import List
from domain.sale_item import SaleItem


class ReturnTransaction:
    """退货交易类，表示一次退货操作"""
    
    def __init__(self, return_id: str = None, original_sale_id: str = None):
        """
        初始化退货交易
        
        Args:
            return_id: 退货ID，如果为None则自动生成
            original_sale_id: 原始销售单ID
        """
        self.return_id = return_id or f"RET-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.original_sale_id = original_sale_id
        self.items: List[SaleItem] = []
        self.return_time = datetime.now()
        self.is_completed = False
    
    def add_item(self, item: SaleItem):
        """
        添加退货项
        
        Args:
            item: 销售项对象（退货的商品）
        """
        self.items.append(item)
    
    def get_total_refund(self) -> float:
        """
        计算退款总额
        
        Returns:
            float: 退款总额
        """
        return sum(item.get_subtotal() for item in self.items)
    
    def complete_return(self):
        """完成退货"""
        self.is_completed = True
    
    def __str__(self):
        items_str = "\n".join(f"  - {item}" for item in self.items)
        status = "已完成" if self.is_completed else "进行中"
        return f"退货单 {self.return_id} ({status})\n原始销售单: {self.original_sale_id}\n{items_str}\n退款总额: ¥{self.get_total_refund():.2f}"
    
    def __repr__(self):
        return f"ReturnTransaction(return_id='{self.return_id}', items={len(self.items)}, refund={self.get_total_refund()})"

