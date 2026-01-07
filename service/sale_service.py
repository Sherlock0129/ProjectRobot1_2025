"""
销售服务
"""

from typing import List
from domain.sale import Sale
from domain.sale_item import SaleItem
from domain.product import Product
from service.inventory_service import InventoryService


class SaleService:
    """销售服务类"""
    
    def __init__(self, inventory_service: InventoryService):
        """
        初始化销售服务
        
        Args:
            inventory_service: 库存服务对象
        """
        self.inventory_service = inventory_service
        self.sales_history: List[Sale] = []
    
    def create_sale(self) -> Sale:
        """
        创建新的销售
        
        Returns:
            Sale: 新的销售对象
        """
        return Sale()
    
    def add_item_to_sale(self, sale: Sale, product_id: str, quantity: int) -> bool:
        """
        向销售中添加商品
        
        Args:
            sale: 销售对象
            product_id: 产品ID
            quantity: 数量
            
        Returns:
            bool: 是否成功添加
        """
        product = self.inventory_service.get_product(product_id)
        if not product:
            return False
        
        if not product.reduce_stock(quantity):
            return False
        
        item = SaleItem(product, quantity)
        sale.add_item(item)
        return True
    
    def complete_sale(self, sale: Sale, payment_method: str, payment_amount: float) -> bool:
        """
        完成销售
        
        Args:
            sale: 销售对象
            payment_method: 支付方式
            payment_amount: 支付金额
            
        Returns:
            bool: 是否成功完成
        """
        total = sale.get_total()
        if payment_amount < total:
            return False
        
        sale.complete_sale(payment_method, payment_amount)
        self.sales_history.append(sale)
        return True
    
    def cancel_sale(self, sale: Sale):
        """
        取消销售（恢复库存）
        
        Args:
            sale: 销售对象
        """
        for item in sale.items:
            self.inventory_service.restore_stock(item.product.product_id, item.quantity)
    
    def get_sales_history(self) -> List[Sale]:
        """
        获取销售历史
        
        Returns:
            List: 销售历史列表
        """
        return self.sales_history.copy()

