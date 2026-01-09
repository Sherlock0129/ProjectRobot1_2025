"""
Return Service
"""

from typing import List, Optional
from domain.return_transaction import ReturnTransaction
from domain.sale_item import SaleItem
from service.inventory_service import InventoryService
from service.sale_service import SaleService


class ReturnService:
    """Return service class"""
    
    def __init__(self, inventory_service: InventoryService, sale_service: SaleService):
        """
        Initialize return service
        
        Args:
            inventory_service: Inventory service object
            sale_service: Sale service object
        """
        self.inventory_service = inventory_service
        self.sale_service = sale_service
        self.return_history: List[ReturnTransaction] = []
    
    def create_return(self, original_sale_id: str = None) -> ReturnTransaction:
        """
        Create new return transaction
        
        Args:
            original_sale_id: Original sale ID
            
        Returns:
            ReturnTransaction: New return transaction object
        """
        return ReturnTransaction(original_sale_id=original_sale_id)
    
    def add_item_to_return(self, return_transaction: ReturnTransaction, 
                          product_id: str, quantity: int) -> bool:
        """
        Add item to return transaction
        
        Args:
            return_transaction: Return transaction object
            product_id: Product ID
            quantity: Quantity
            
        Returns:
            bool: Whether addition was successful
        """
        product = self.inventory_service.get_product(product_id)
        if not product:
            return False
        
        item = SaleItem(product, quantity)
        return_transaction.add_item(item)
        return True
    
    def complete_return(self, return_transaction: ReturnTransaction) -> bool:
        """
        Complete return
        
        Args:
            return_transaction: Return transaction object
            
        Returns:
            bool: Whether completion was successful
        """
        if not return_transaction.items:
            return False
        
        # Restore stock
        for item in return_transaction.items:
            self.inventory_service.restore_stock(item.product.product_id, item.quantity)
        
        return_transaction.complete_return()
        self.return_history.append(return_transaction)
        return True
    
    def get_return_history(self) -> List[ReturnTransaction]:
        """
        Get return history
        
        Returns:
            List: List of return history
        """
        return self.return_history.copy()
    
    def find_sale_by_id(self, sale_id: str) -> Optional:
        """
        Find sale by ID
        
        Args:
            sale_id: Sale ID
            
        Returns:
            Sale: Sale object, or None if not found
        """
        for sale in self.sale_service.get_sales_history():
            if sale.sale_id == sale_id:
                return sale
        return None
