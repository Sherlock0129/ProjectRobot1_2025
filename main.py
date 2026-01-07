"""
POS系统主程序入口
"""

from service.inventory_service import InventoryService
from service.sale_service import SaleService
from service.return_service import ReturnService
from ui.pos_ui import POSUI


def main():
    """主函数"""
    # 初始化服务层
    inventory_service = InventoryService()
    sale_service = SaleService(inventory_service)
    return_service = ReturnService(inventory_service, sale_service)
    
    # 初始化UI层
    ui = POSUI(sale_service, return_service, inventory_service)
    
    # 运行系统
    ui.run()


if __name__ == "__main__":
    main()

