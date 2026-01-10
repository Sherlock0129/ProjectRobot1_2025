"""
Return Transaction Entity Class
"""

from datetime import datetime
from typing import List
from domain.sale_item import SaleItem


class ReturnTransaction:
    """Return transaction class representing a return operation"""
    
    def __init__(self, return_id: str = None, original_sale_id: str = None):
        """
        Initialize return transaction
        
        Args:
            return_id: Return ID, if None will be auto-generated
            original_sale_id: Original sale ID
        """
        self.return_id = return_id or f"RET-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.original_sale_id = original_sale_id
        self.items: List[SaleItem] = []
        self.return_time = datetime.now()
        self.is_completed = False
    
    def add_item(self, item: SaleItem):
        """
        Add return item
        
        Args:
            item: Sale item object (returned product)
        """
        self.items.append(item)
    
    def get_total_refund(self) -> float:
        """
        Calculate total refund amount
        
        Returns:
            float: Total refund amount
        """
        return sum(item.get_subtotal() for item in self.items)
    
    def complete_return(self):
        """Complete return"""
        self.is_completed = True
    
    def __str__(self):
        items_str = "\n".join(f"  - {item}" for item in self.items)
        status = "Completed" if self.is_completed else "In Progress"
        return f"Return {self.return_id} ({status})\nOriginal Sale: {self.original_sale_id}\n{items_str}\nTotal Refund: ${self.get_total_refund():.2f}"
    
    def __repr__(self):
        return f"ReturnTransaction(return_id='{self.return_id}', items={len(self.items)}, refund={self.get_total_refund()})"
