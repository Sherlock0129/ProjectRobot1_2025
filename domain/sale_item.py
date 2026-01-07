"""
销售项实体类
"""

from domain.product import Product


class SaleItem:
    """销售项类，表示一次销售中的单个商品项"""
    
    def __init__(self, product: Product, quantity: int):
        """
        初始化销售项
        
        Args:
            product: 产品对象
            quantity: 购买数量
        """
        self.product = product
        self.quantity = quantity
    
    def get_subtotal(self) -> float:
        """
        计算小计
        
        Returns:
            float: 小计金额
        """
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity} = ¥{self.get_subtotal():.2f}"
    
    def __repr__(self):
        return f"SaleItem(product={self.product}, quantity={self.quantity})"

