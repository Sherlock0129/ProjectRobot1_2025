"""
Transaction Abstract Base Class
演示面向对象编程的继承和多态
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from domain.sale_item import SaleItem


class Transaction(ABC):
    """
    交易抽象基类
    定义了所有交易类型的通用接口和行为
    演示继承和多态的使用
    """
    
    def __init__(self, transaction_id: str = None):
        """
        初始化交易
        
        Args:
            transaction_id: 交易ID，如果为None则自动生成
        """
        self.transaction_id = transaction_id or self._generate_id()
        self.items: List[SaleItem] = []
        self.transaction_time = datetime.now()
        self.is_completed = False
    
    @abstractmethod
    def _generate_id(self) -> str:
        """
        生成交易ID（抽象方法，子类必须实现）
        演示多态：不同子类有不同的ID生成规则
        
        Returns:
            str: 交易ID
        """
        pass
    
    def add_item(self, item: SaleItem):
        """
        添加交易项目（通用方法，所有子类共享）
        
        Args:
            item: 交易项目对象
        """
        self.items.append(item)
    
    @abstractmethod
    def get_total_amount(self) -> float:
        """
        计算总金额（抽象方法，演示多态）
        不同交易类型有不同的计算方式
        
        Returns:
            float: 总金额
        """
        pass
    
    @abstractmethod
    def complete(self, *args, **kwargs):
        """
        完成交易（抽象方法，演示多态）
        不同交易类型的完成逻辑不同
        
        Args:
            *args: 可变位置参数
            **kwargs: 可变关键字参数
        """
        pass
    
    def get_item_count(self) -> int:
        """
        获取交易项目数量（通用方法）
        
        Returns:
            int: 项目数量
        """
        return len(self.items)
    
    def is_empty(self) -> bool:
        """
        检查交易是否为空（通用方法）
        
        Returns:
            bool: 如果交易为空返回True
        """
        return len(self.items) == 0
    
    @abstractmethod
    def get_transaction_type(self) -> str:
        """
        获取交易类型（抽象方法，演示多态）
        
        Returns:
            str: 交易类型名称
        """
        pass
    
    def __str__(self):
        """字符串表示（通用方法，可被子类重写）"""
        items_str = "\n".join(f"  - {item}" for item in self.items)
        status = "Completed" if self.is_completed else "In Progress"
        return f"{self.get_transaction_type()} {self.transaction_id} ({status})\n{items_str}"
    
    def __repr__(self):
        """对象表示"""
        return f"{self.__class__.__name__}(transaction_id='{self.transaction_id}', items={len(self.items)})"

