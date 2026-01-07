"""
退货服务
"""

from typing import List, Optional
from domain.return_transaction import ReturnTransaction
from domain.sale_item import SaleItem
from service.inventory_service import InventoryService
from service.sale_service import SaleService


class ReturnService:
    """退货服务类"""
    
    def __init__(self, inventory_service: InventoryService, sale_service: SaleService):
        """
        初始化退货服务
        
        Args:
            inventory_service: 库存服务对象
            sale_service: 销售服务对象
        """
        self.inventory_service = inventory_service
        self.sale_service = sale_service
        self.return_history: List[ReturnTransaction] = []
    
    def create_return(self, original_sale_id: str = None) -> ReturnTransaction:
        """
        创建新的退货交易
        
        Args:
            original_sale_id: 原始销售单ID
            
        Returns:
            ReturnTransaction: 新的退货交易对象
        """
        return ReturnTransaction(original_sale_id=original_sale_id)
    
    def add_item_to_return(self, return_transaction: ReturnTransaction, 
                          product_id: str, quantity: int) -> bool:
        """
        向退货交易中添加商品
        
        Args:
            return_transaction: 退货交易对象
            product_id: 产品ID
            quantity: 数量
            
        Returns:
            bool: 是否成功添加
        """
        product = self.inventory_service.get_product(product_id)
        if not product:
            return False
        
        item = SaleItem(product, quantity)
        return_transaction.add_item(item)
        return True
    
    def complete_return(self, return_transaction: ReturnTransaction) -> bool:
        """
        完成退货
        
        Args:
            return_transaction: 退货交易对象
            
        Returns:
            bool: 是否成功完成
        """
        if not return_transaction.items:
            return False
        
        # 恢复库存
        for item in return_transaction.items:
            self.inventory_service.restore_stock(item.product.product_id, item.quantity)
        
        return_transaction.complete_return()
        self.return_history.append(return_transaction)
        return True
    
    def get_return_history(self) -> List[ReturnTransaction]:
        """
        获取退货历史
        
        Returns:
            List: 退货历史列表
        """
        return self.return_history.copy()
    
    def find_sale_by_id(self, sale_id: str) -> Optional:
        """
        根据ID查找销售单
        
        Args:
            sale_id: 销售单ID
            
        Returns:
            Sale: 销售单对象，如果不存在则返回None
        """
        for sale in self.sale_service.get_sales_history():
            if sale.sale_id == sale_id:
                return sale
        return None

