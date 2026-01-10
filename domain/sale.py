"""
Sale Entity Class
"""

from datetime import datetime
from typing import List
from domain.sale_item import SaleItem


class Sale:
    """Sale class representing a complete sales transaction"""
    
    def __init__(self, sale_id: str = None):
        """
        Initialize sale
        
        Args:
            sale_id: Sale ID, if None will be auto-generated
        """
        self.sale_id = sale_id or f"SALE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.items: List[SaleItem] = []
        self.sale_time = datetime.now()
        self.payment_method = None
        self.payment_amount = 0.0
        self.is_completed = False
    
    def add_item(self, item: SaleItem):
        """
        Add sale item
        
        Args:
            item: Sale item object
        """
        self.items.append(item)
    
    def get_total(self) -> float:
        """
        Calculate total amount
        
        Returns:
            float: Total amount
        """
        return sum(item.get_subtotal() for item in self.items)
    
    def complete_sale(self, payment_method: str, payment_amount: float):
        """
        Complete sale
        
        Args:
            payment_method: Payment method
            payment_amount: Payment amount
        """
        self.payment_method = payment_method
        self.payment_amount = payment_amount
        self.is_completed = True
    
    def get_change(self) -> float:
        """
        Calculate change
        
        Returns:
            float: Change amount
        """
        if self.is_completed:
            return self.payment_amount - self.get_total()
        return 0.0
    
    def __str__(self):
        items_str = "\n".join(f"  - {item}" for item in self.items)
        status = "Completed" if self.is_completed else "In Progress"
        return f"Sale {self.sale_id} ({status})\n{items_str}\nTotal: ${self.get_total():.2f}"
    
    def __repr__(self):
        return f"Sale(sale_id='{self.sale_id}', items={len(self.items)}, total={self.get_total()})"
