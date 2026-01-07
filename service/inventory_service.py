"""
库存管理服务
"""

from typing import Dict, Optional
from domain.product import Product


class InventoryService:
    """库存管理服务类"""
    
    def __init__(self):
        """初始化库存服务"""
        self.products: Dict[str, Product] = {}
        self._initialize_sample_products()
    
    def _initialize_sample_products(self):
        """初始化示例商品"""
        sample_products = [
            Product("P001", "苹果", 5.50, 100),
            Product("P002", "香蕉", 3.80, 80),
            Product("P003", "牛奶", 12.00, 50),
            Product("P004", "面包", 8.50, 60),
            Product("P005", "鸡蛋", 15.00, 40),
        ]
        for product in sample_products:
            self.products[product.product_id] = product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """
        根据ID获取产品
        
        Args:
            product_id: 产品ID
            
        Returns:
            Product: 产品对象，如果不存在则返回None
        """
        return self.products.get(product_id)
    
    def get_all_products(self) -> list[Product]:
        """
        获取所有产品
        
        Returns:
            list: 所有产品列表
        """
        return list(self.products.values())
    
    def add_product(self, product: Product):
        """
        添加产品
        
        Args:
            product: 产品对象
        """
        self.products[product.product_id] = product
    
    def update_stock(self, product_id: str, quantity: int) -> bool:
        """
        更新库存（减少）
        
        Args:
            product_id: 产品ID
            quantity: 数量（正数表示减少，负数表示增加）
            
        Returns:
            bool: 是否成功更新
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
        恢复库存（增加）
        
        Args:
            product_id: 产品ID
            quantity: 恢复的数量
        """
        product = self.get_product(product_id)
        if product:
            product.increase_stock(quantity)

