"""
POS System Main Entry Point - GUI Version
"""

from service.inventory_service import InventoryService
from service.sale_service import SaleService
from service.return_service import ReturnService
from ui.pos_gui import POSGUI


def main():
    """Main function"""
    # Initialize service layer
    inventory_service = InventoryService()
    sale_service = SaleService(inventory_service)
    return_service = ReturnService(inventory_service, sale_service)
    
    # Initialize GUI
    app = POSGUI(sale_service, return_service, inventory_service)
    
    # Run system
    app.run()


if __name__ == "__main__":
    main()
