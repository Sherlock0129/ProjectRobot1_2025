"""
POS系统主程序入口 - GUI版本
"""

from service.inventory_service import InventoryService
from service.sale_service import SaleService
from service.return_service import ReturnService
from ui.pos_gui import POSGUI


def main():
    """主函数"""
    # 初始化服务层
    inventory_service = InventoryService()
    sale_service = SaleService(inventory_service)
    return_service = ReturnService(inventory_service, sale_service)
    
    # 初始化GUI
    app = POSGUI(sale_service, return_service, inventory_service)
    
    # 运行系统
    app.run()


if __name__ == "__main__":
    main()

