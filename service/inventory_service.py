"""
Inventory Management Service
"""

from typing import Dict, Optional
from domain.product import Product


class InventoryService:
    """Inventory management service class"""
    
    def __init__(self):
        """Initialize inventory service"""
        self.products: Dict[str, Product] = {}
        self._initialize_sample_products()
    
    def _initialize_sample_products(self):
        """Initialize sample products"""
        sample_products = [
            Product("P001", "Apple", 5.50, 100),
            Product("P002", "Banana", 3.80, 80),
            Product("P003", "Milk", 12.00, 50),
            Product("P004", "Bread", 8.50, 60),
            Product("P005", "Egg", 15.00, 40),
        ]
        for product in sample_products:
            self.products[product.product_id] = product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """
        Get product by ID
        
        Args:
            product_id: Product ID
            
        Returns:
            Product: Product object, or None if not found
        """
        return self.products.get(product_id)
    
    def get_all_products(self) -> list[Product]:
        """
        Get all products
        
        Returns:
            list: List of all products
        """
        return list(self.products.values())
    
    def add_product(self, product: Product):
        """
        Add product
        
        Args:
            product: Product object
        """
        self.products[product.product_id] = product
    
    def update_stock(self, product_id: str, quantity: int) -> bool:
        """
        Update stock (decrease)
        
        Args:
            product_id: Product ID
            quantity: Quantity (positive to decrease, negative to increase)
            
        Returns:
            bool: Whether update was successful
        """
        product = self.get_product(product_id)
        if product:
            if quantity > 0:
                return product.reduce_stock(quantity)
            else:
                product.increase_stock(-quantity)
                return True
        return False
    
    def restore_stock(self, product_id: str, quantity: int):
        """
        Restore stock (increase)
        
        Args:
            product_id: Product ID
            quantity: Quantity to restore
        """
        product = self.get_product(product_id)
        if product:
            product.increase_stock(quantity)
