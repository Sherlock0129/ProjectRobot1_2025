"""
POS系统功能测试脚本
用于验证核心功能是否正常工作
"""

from domain.product import Product
from domain.sale import Sale
from domain.sale_item import SaleItem
from domain.return_transaction import ReturnTransaction
from service.inventory_service import InventoryService
from service.sale_service import SaleService
from service.return_service import ReturnService


def test_product():
    """测试Product类"""
    print("测试Product类...")
    product = Product("P001", "苹果", 5.50, 100)
    assert product.product_id == "P001"
    assert product.name == "苹果"
    assert product.price == 5.50
    assert product.stock == 100
    
    # 测试减少库存
    assert product.reduce_stock(10) == True
    assert product.stock == 90
    
    # 测试增加库存
    product.increase_stock(5)
    assert product.stock == 95
    
    print("[OK] Product类测试通过")


def test_sale():
    """测试Sale类"""
    print("测试Sale类...")
    product = Product("P001", "苹果", 5.50, 100)
    sale = Sale()
    
    # 添加商品
    item1 = SaleItem(product, 5)
    sale.add_item(item1)
    
    assert len(sale.items) == 1
    assert sale.get_total() == 27.50
    
    # 完成销售
    sale.complete_sale("现金", 30.00)
    assert sale.is_completed == True
    assert sale.get_change() == 2.50
    
    print("[OK] Sale类测试通过")


def test_inventory_service():
    """测试InventoryService"""
    print("测试InventoryService...")
    service = InventoryService()
    
    # 获取商品
    product = service.get_product("P001")
    assert product is not None
    assert product.name == "苹果"
    
    # 更新库存
    assert service.update_stock("P001", 10) == True
    product = service.get_product("P001")
    assert product.stock == 90
    
    print("[OK] InventoryService测试通过")


def test_sale_service():
    """测试SaleService"""
    print("测试SaleService...")
    inventory_service = InventoryService()
    sale_service = SaleService(inventory_service)
    
    # 创建销售
    sale = sale_service.create_sale()
    assert sale is not None
    
    # 添加商品
    assert sale_service.add_item_to_sale(sale, "P001", 5) == True
    assert len(sale.items) == 1
    
    # 完成销售
    assert sale_service.complete_sale(sale, "现金", 30.00) == True
    assert sale.is_completed == True
    
    # 检查库存是否减少
    product = inventory_service.get_product("P001")
    assert product.stock == 95  # 100 - 5 = 95
    
    print("[OK] SaleService测试通过")


def test_return_service():
    """测试ReturnService"""
    print("测试ReturnService...")
    inventory_service = InventoryService()
    sale_service = SaleService(inventory_service)
    return_service = ReturnService(inventory_service, sale_service)
    
    # 先进行一次销售
    sale = sale_service.create_sale()
    sale_service.add_item_to_sale(sale, "P001", 10)
    sale_service.complete_sale(sale, "现金", 100.00)
    
    initial_stock = inventory_service.get_product("P001").stock
    
    # 创建退货
    return_transaction = return_service.create_return(sale.sale_id)
    assert return_service.add_item_to_return(return_transaction, "P001", 3) == True
    
    # 完成退货
    assert return_service.complete_return(return_transaction) == True
    
    # 检查库存是否恢复
    product = inventory_service.get_product("P001")
    assert product.stock == initial_stock + 3
    
    print("[OK] ReturnService测试通过")


def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("开始运行POS系统功能测试")
    print("=" * 50)
    
    try:
        test_product()
        test_sale()
        test_inventory_service()
        test_sale_service()
        test_return_service()
        
        print("=" * 50)
        print("[OK] 所有测试通过！")
        print("=" * 50)
        return True
    except AssertionError as e:
        print(f"[FAIL] 测试失败: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] 测试出错: {e}")
        return False


if __name__ == "__main__":
    run_all_tests()

