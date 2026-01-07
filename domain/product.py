"""
产品实体类
"""


class Product:
    """产品类，表示超市中的商品"""
    
    def __init__(self, product_id: str, name: str, price: float, stock: int = 0):
        """
        初始化产品
        
        Args:
            product_id: 产品ID
            name: 产品名称
            price: 单价
            stock: 库存数量
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def reduce_stock(self, quantity: int) -> bool:
        """
        减少库存
        
        Args:
            quantity: 减少的数量
            
        Returns:
            bool: 是否成功减少库存
        """
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
    
    def increase_stock(self, quantity: int):
        """
        增加库存
        
        Args:
            quantity: 增加的数量
        """
        self.stock += quantity
    
    def __str__(self):
        return f"{self.name} (ID: {self.product_id}, 价格: ¥{self.price:.2f}, 库存: {self.stock})"
    
    def __repr__(self):
        return f"Product(product_id='{self.product_id}', name='{self.name}', price={self.price}, stock={self.stock})"

