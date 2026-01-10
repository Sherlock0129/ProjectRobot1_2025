"""
Sale Item Entity Class
"""

from domain.product import Product


class SaleItem:
    """Sale item class representing a single product item in a sale"""
    
    def __init__(self, product: Product, quantity: int):
        """
        Initialize sale item
        
        Args:
            product: Product object
            quantity: Purchase quantity
        """
        self.product = product
        self.quantity = quantity
    
    def get_subtotal(self) -> float:
        """
        Calculate subtotal
        
        Returns:
            float: Subtotal amount
        """
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity} = ${self.get_subtotal():.2f}"
    
    def __repr__(self):
        return f"SaleItem(product={self.product}, quantity={self.quantity})"
