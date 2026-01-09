"""
Product Entity Class
"""


class Product:
    """Product class representing a product in the store"""
    
    def __init__(self, product_id: str, name: str, price: float, stock: int = 0):
        """
        Initialize product
        
        Args:
            product_id: Product ID
            name: Product name
            price: Unit price
            stock: Stock quantity
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def reduce_stock(self, quantity: int) -> bool:
        """
        Reduce stock
        
        Args:
            quantity: Quantity to reduce
            
        Returns:
            bool: Whether stock reduction was successful
        """
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
    
    def increase_stock(self, quantity: int):
        """
        Increase stock
        
        Args:
            quantity: Quantity to increase
        """
        self.stock += quantity
    
    def __str__(self):
        return f"{self.name} (ID: {self.product_id}, Price: ${self.price:.2f}, Stock: {self.stock})"
    
    def __repr__(self):
        return f"Product(product_id='{self.product_id}', name='{self.name}', price={self.price}, stock={self.stock})"
