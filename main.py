"""
POS System Main Entry Point - CLI Version
"""

from service.inventory_service import InventoryService
from service.sale_service import SaleService
from service.return_service import ReturnService
from ui.pos_ui import POSUI


def main():
    """Main function"""
    # Initialize service layer
    inventory_service = InventoryService()
    sale_service = SaleService(inventory_service)
    return_service = ReturnService(inventory_service, sale_service)
    
    # Initialize UI layer
    ui = POSUI(sale_service, return_service, inventory_service)
    
    # Run system
    ui.run()


if __name__ == "__main__":
    main()
