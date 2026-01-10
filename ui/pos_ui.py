"""
POS System User Interface (CLI)
"""

from typing import Optional
from domain.sale import Sale
from domain.return_transaction import ReturnTransaction
from service.sale_service import SaleService
from service.return_service import ReturnService
from service.inventory_service import InventoryService


class POSUI:
    """POS System User Interface Class"""
    
    def __init__(self, sale_service: SaleService, return_service: ReturnService, 
                 inventory_service: InventoryService):
        """
        Initialize UI
        
        Args:
            sale_service: Sale service
            return_service: Return service
            inventory_service: Inventory service
        """
        self.sale_service = sale_service
        self.return_service = return_service
        self.inventory_service = inventory_service
        self.current_sale: Optional[Sale] = None
        self.current_return: Optional[ReturnTransaction] = None
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("          Point of Sale System (POS)")
        print("="*50)
        print("1. Process Sale")
        print("2. Handle Returns")
        print("3. View Products")
        print("4. View Sales History")
        print("5. View Return History")
        print("0. Exit")
        print("="*50)
    
    def display_products(self):
        """Display product list"""
        print("\n" + "-"*50)
        print("Product List")
        print("-"*50)
        products = self.inventory_service.get_all_products()
        if not products:
            print("No products available")
            return
        
        print(f"{'ID':<8} {'Product Name':<20} {'Price':<12} {'Stock':<10}")
        print("-"*50)
        for product in products:
            print(f"{product.product_id:<8} {product.name:<20} ${product.price:<11.2f} {product.stock:<10}")
        print("-"*50)
    
    def process_sale(self):
        """Process sale flow"""
        print("\n" + "-"*50)
        print("Process Sale")
        print("-"*50)
        
        self.current_sale = self.sale_service.create_sale()
        print(f"New Sale: {self.current_sale.sale_id}")
        
        while True:
            print(f"\nCurrent Sale Total: ${self.current_sale.get_total():.2f}")
            print("\nOptions:")
            print("1. Add Item")
            print("2. Complete Sale")
            print("3. Cancel Sale")
            
            choice = input("\nPlease select an option: ").strip()
            
            if choice == "1":
                self._add_item_to_sale()
            elif choice == "2":
                self._complete_sale()
                break
            elif choice == "3":
                self._cancel_sale()
                break
            else:
                print("Invalid choice, please try again")
    
    def _add_item_to_sale(self):
        """Add item to sale"""
        self.display_products()
        product_id = input("\nEnter Product ID: ").strip()
        try:
            quantity = int(input("Enter Quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be greater than 0")
                return
        except ValueError:
            print("Invalid quantity")
            return
        
        if self.sale_service.add_item_to_sale(self.current_sale, product_id, quantity):
            print(f"[Success] Item added successfully")
            print(f"Current Sale:")
            for item in self.current_sale.items:
                print(f"  - {item}")
        else:
            print("[Failed] Add failed: Product not found or insufficient stock")
    
    def _complete_sale(self):
        """Complete sale"""
        if not self.current_sale.items:
            print("Sale is empty, cannot complete")
            return
        
        print(f"\nSale Details:")
        for item in self.current_sale.items:
            print(f"  - {item}")
        print(f"Total: ${self.current_sale.get_total():.2f}")
        
        valid_methods = {"cash", "card", "mobile"}

        while True:
            payment_method = input("\nEnter Payment Method (cash/card/mobile): ").strip()

            if payment_method == "":
                payment_method = "cash"
                break

            if payment_method in valid_methods:
                break
            else:
                print("Invalid payment method")
        try:
            payment_amount = float(input("Enter Payment Amount: ").strip())
        except ValueError:
            print("Invalid payment amount")
            return
        
        if self.sale_service.complete_sale(self.current_sale, payment_method, payment_amount):
            change = self.current_sale.get_change()
            print(f"\n[Success] Sale completed!")
            print(f"Payment Method: {payment_method}")
            print(f"Payment Amount: ${payment_amount:.2f}")
            if change > 0:
                print(f"Change: ${change:.2f}")
            print(f"\nSale ID: {self.current_sale.sale_id}")
        else:
            print("[Failed] Insufficient payment amount")
            self.current_sale = None
    
    def _cancel_sale(self):
        """Cancel sale"""
        if self.current_sale:
            self.sale_service.cancel_sale(self.current_sale)
            print("Sale cancelled, stock restored")
            self.current_sale = None
    
    def handle_returns(self):
        """Handle return flow"""
        print("\n" + "-"*50)
        print("Handle Returns")
        print("-"*50)
        
        original_sale_id = input("Enter Original Sale ID (optional, press Enter to skip): ").strip()
        self.current_return = self.return_service.create_return(
            original_sale_id if original_sale_id else None
        )
        print(f"New Return: {self.current_return.return_id}")
        
        while True:
            print(f"\nCurrent Return Total Refund: ${self.current_return.get_total_refund():.2f}")
            print("\nOptions:")
            print("1. Add Return Item")
            print("2. Complete Return")
            print("3. Cancel Return")
            
            choice = input("\nPlease select an option: ").strip()
            
            if choice == "1":
                self._add_item_to_return()
            elif choice == "2":
                self._complete_return()
                break
            elif choice == "3":
                self._cancel_return()
                break
            else:
                print("Invalid choice, please try again")
    
    def _add_item_to_return(self):
        """Add item to return"""
        self.display_products()
        product_id = input("\nEnter Product ID: ").strip()
        try:
            quantity = int(input("Enter Return Quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be greater than 0")
                return
        except ValueError:
            print("Invalid quantity")
            return
        
        if self.return_service.add_item_to_return(self.current_return, product_id, quantity):
            print(f"[Success] Return item added successfully")
            print(f"Current Return:")
            for item in self.current_return.items:
                print(f"  - {item}")
        else:
            print("[Failed] Add failed: Product not found")
    
    def _complete_return(self):
        """Complete return"""
        if not self.current_return.items:
            print("Return is empty, cannot complete")
            return
        
        print(f"\nReturn Details:")
        for item in self.current_return.items:
            print(f"  - {item}")
        print(f"Total Refund: ${self.current_return.get_total_refund():.2f}")
        
        confirm = input("\nConfirm complete return? (y/n): ").strip().lower()
        if confirm == 'y':
            if self.return_service.complete_return(self.current_return):
                print(f"\n[Success] Return completed!")
                print(f"Total Refund: ${self.current_return.get_total_refund():.2f}")
                print(f"Stock restored")
                print(f"\nReturn ID: {self.current_return.return_id}")
            else:
                print("[Failed] Return failed")
        else:
            print("Return cancelled")
        self.current_return = None
    
    def _cancel_return(self):
        """Cancel return"""
        print("Return cancelled")
        self.current_return = None
    
    def view_sales_history(self):
        """View sales history"""
        print("\n" + "-"*50)
        print("Sales History")
        print("-"*50)
        sales = self.sale_service.get_sales_history()
        if not sales:
            print("No sales records")
            return
        
        for sale in sales:
            print(f"\n{sale}")
            if sale.is_completed:
                print(f"Payment Method: {sale.payment_method}, Payment Amount: ${sale.payment_amount:.2f}")
    
    def view_return_history(self):
        """View return history"""
        print("\n" + "-"*50)
        print("Return History")
        print("-"*50)
        returns = self.return_service.get_return_history()
        if not returns:
            print("No return records")
            return
        
        for return_transaction in returns:
            print(f"\n{return_transaction}")
    
    def run(self):
        """Run main loop"""
        while True:
            self.display_menu()
            choice = input("\nPlease select an option: ").strip()
            
            if choice == "1":
                self.process_sale()
            elif choice == "2":
                self.handle_returns()
            elif choice == "3":
                self.display_products()
            elif choice == "4":
                self.view_sales_history()
            elif choice == "5":
                self.view_return_history()
            elif choice == "0":
                print("\nThank you for using POS System. Goodbye!")
                break
            else:
                print("Invalid choice, please try again")
            
            input("\nPress Enter to continue...")
