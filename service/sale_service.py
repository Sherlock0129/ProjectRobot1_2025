"""
Sale Service
"""

from typing import List
from domain.sale import Sale
from domain.sale_item import SaleItem
from domain.product import Product
from service.inventory_service import InventoryService


class SaleService:
    """Sale service class"""
    
    def __init__(self, inventory_service: InventoryService):
        """
        Initialize sale service
        
        Args:
            inventory_service: Inventory service object
        """
        self.inventory_service = inventory_service
        self.sales_history: List[Sale] = []
    
    def create_sale(self) -> Sale:
        """
        Create new sale
        
        Returns:
            Sale: New sale object
        """
        return Sale()
    
    def add_item_to_sale(self, sale: Sale, product_id: str, quantity: int) -> bool:
        """
        Add item to sale
        
        Args:
            sale: Sale object
            product_id: Product ID
            quantity: Quantity
            
        Returns:
            bool: Whether addition was successful
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
        Complete sale
        
        Args:
            sale: Sale object
            payment_method: Payment method
            payment_amount: Payment amount
            
        Returns:
            bool: Whether completion was successful
        """
        total = sale.get_total()
        if payment_amount < total:
            return False
        
        sale.complete_sale(payment_method, payment_amount)
        self.sales_history.append(sale)
        return True
    
    def cancel_sale(self, sale: Sale):
        """
        Cancel sale (restore stock)
        
        Args:
            sale: Sale object
        """
        for item in sale.items:
            self.inventory_service.restore_stock(item.product.product_id, item.quantity)
    
    def get_sales_history(self) -> List[Sale]:
        """
        Get sales history
        
        Returns:
            List: List of sales history
        """
        return self.sales_history.copy()
