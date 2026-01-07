"""
POS系统用户界面
"""

from typing import Optional
from domain.sale import Sale
from domain.return_transaction import ReturnTransaction
from service.sale_service import SaleService
from service.return_service import ReturnService
from service.inventory_service import InventoryService


class POSUI:
    """POS系统用户界面类"""
    
    def __init__(self, sale_service: SaleService, return_service: ReturnService, 
                 inventory_service: InventoryService):
        """
        初始化UI
        
        Args:
            sale_service: 销售服务
            return_service: 退货服务
            inventory_service: 库存服务
        """
        self.sale_service = sale_service
        self.return_service = return_service
        self.inventory_service = inventory_service
        self.current_sale: Optional[Sale] = None
        self.current_return: Optional[ReturnTransaction] = None
    
    def display_menu(self):
        """显示主菜单"""
        print("\n" + "="*50)
        print("          超市收银系统 (POS System)")
        print("="*50)
        print("1. 处理销售 (Process Sale)")
        print("2. 处理退货 (Handle Returns)")
        print("3. 查看商品列表 (View Products)")
        print("4. 查看销售历史 (View Sales History)")
        print("5. 查看退货历史 (View Return History)")
        print("0. 退出系统 (Exit)")
        print("="*50)
    
    def display_products(self):
        """显示商品列表"""
        print("\n" + "-"*50)
        print("商品列表 (Product List)")
        print("-"*50)
        products = self.inventory_service.get_all_products()
        if not products:
            print("暂无商品")
            return
        
        print(f"{'ID':<8} {'商品名称':<15} {'单价':<10} {'库存':<10}")
        print("-"*50)
        for product in products:
            print(f"{product.product_id:<8} {product.name:<15} ¥{product.price:<9.2f} {product.stock:<10}")
        print("-"*50)
    
    def process_sale(self):
        """处理销售流程"""
        print("\n" + "-"*50)
        print("处理销售 (Process Sale)")
        print("-"*50)
        
        self.current_sale = self.sale_service.create_sale()
        print(f"新建销售单: {self.current_sale.sale_id}")
        
        while True:
            print(f"\n当前销售单总计: ¥{self.current_sale.get_total():.2f}")
            print("\n选项:")
            print("1. 添加商品")
            print("2. 完成销售")
            print("3. 取消销售")
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == "1":
                self._add_item_to_sale()
            elif choice == "2":
                self._complete_sale()
                break
            elif choice == "3":
                self._cancel_sale()
                break
            else:
                print("无效的选择，请重试")
    
    def _add_item_to_sale(self):
        """添加商品到销售单"""
        self.display_products()
        product_id = input("\n请输入商品ID: ").strip()
        try:
            quantity = int(input("请输入数量: ").strip())
            if quantity <= 0:
                print("数量必须大于0")
                return
        except ValueError:
            print("无效的数量")
            return
        
        if self.sale_service.add_item_to_sale(self.current_sale, product_id, quantity):
            print(f"[成功] 成功添加商品")
            print(f"当前销售单:")
            for item in self.current_sale.items:
                print(f"  - {item}")
        else:
            print("[失败] 添加失败：商品不存在或库存不足")
    
    def _complete_sale(self):
        """完成销售"""
        if not self.current_sale.items:
            print("销售单为空，无法完成")
            return
        
        print(f"\n销售单详情:")
        for item in self.current_sale.items:
            print(f"  - {item}")
        print(f"总计: ¥{self.current_sale.get_total():.2f}")
        
        payment_method = input("\n请输入支付方式 (现金/刷卡/移动支付): ").strip() or "现金"
        try:
            payment_amount = float(input("请输入支付金额: ").strip())
        except ValueError:
            print("无效的支付金额")
            return
        
        if self.sale_service.complete_sale(self.current_sale, payment_method, payment_amount):
            change = self.current_sale.get_change()
            print(f"\n[成功] 销售完成！")
            print(f"支付方式: {payment_method}")
            print(f"支付金额: ¥{payment_amount:.2f}")
            if change > 0:
                print(f"找零: ¥{change:.2f}")
            print(f"\n销售单号: {self.current_sale.sale_id}")
        else:
            print("[失败] 支付金额不足")
            self.current_sale = None
    
    def _cancel_sale(self):
        """取消销售"""
        if self.current_sale:
            self.sale_service.cancel_sale(self.current_sale)
            print("销售已取消，库存已恢复")
            self.current_sale = None
    
    def handle_returns(self):
        """处理退货流程"""
        print("\n" + "-"*50)
        print("处理退货 (Handle Returns)")
        print("-"*50)
        
        original_sale_id = input("请输入原始销售单ID (可选，直接回车跳过): ").strip()
        self.current_return = self.return_service.create_return(
            original_sale_id if original_sale_id else None
        )
        print(f"新建退货单: {self.current_return.return_id}")
        
        while True:
            print(f"\n当前退货单退款总额: ¥{self.current_return.get_total_refund():.2f}")
            print("\n选项:")
            print("1. 添加退货商品")
            print("2. 完成退货")
            print("3. 取消退货")
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == "1":
                self._add_item_to_return()
            elif choice == "2":
                self._complete_return()
                break
            elif choice == "3":
                self._cancel_return()
                break
            else:
                print("无效的选择，请重试")
    
    def _add_item_to_return(self):
        """添加商品到退货单"""
        self.display_products()
        product_id = input("\n请输入商品ID: ").strip()
        try:
            quantity = int(input("请输入退货数量: ").strip())
            if quantity <= 0:
                print("数量必须大于0")
                return
        except ValueError:
            print("无效的数量")
            return
        
        if self.return_service.add_item_to_return(self.current_return, product_id, quantity):
            print(f"[成功] 成功添加退货商品")
            print(f"当前退货单:")
            for item in self.current_return.items:
                print(f"  - {item}")
        else:
            print("[失败] 添加失败：商品不存在")
    
    def _complete_return(self):
        """完成退货"""
        if not self.current_return.items:
            print("退货单为空，无法完成")
            return
        
        print(f"\n退货单详情:")
        for item in self.current_return.items:
            print(f"  - {item}")
        print(f"退款总额: ¥{self.current_return.get_total_refund():.2f}")
        
        confirm = input("\n确认完成退货? (y/n): ").strip().lower()
        if confirm == 'y':
            if self.return_service.complete_return(self.current_return):
                print(f"\n[成功] 退货完成！")
                print(f"退款总额: ¥{self.current_return.get_total_refund():.2f}")
                print(f"库存已恢复")
                print(f"\n退货单号: {self.current_return.return_id}")
            else:
                print("[失败] 退货失败")
        else:
            print("退货已取消")
        self.current_return = None
    
    def _cancel_return(self):
        """取消退货"""
        print("退货已取消")
        self.current_return = None
    
    def view_sales_history(self):
        """查看销售历史"""
        print("\n" + "-"*50)
        print("销售历史 (Sales History)")
        print("-"*50)
        sales = self.sale_service.get_sales_history()
        if not sales:
            print("暂无销售记录")
            return
        
        for sale in sales:
            print(f"\n{sale}")
            if sale.is_completed:
                print(f"支付方式: {sale.payment_method}, 支付金额: ¥{sale.payment_amount:.2f}")
    
    def view_return_history(self):
        """查看退货历史"""
        print("\n" + "-"*50)
        print("退货历史 (Return History)")
        print("-"*50)
        returns = self.return_service.get_return_history()
        if not returns:
            print("暂无退货记录")
            return
        
        for return_transaction in returns:
            print(f"\n{return_transaction}")
    
    def run(self):
        """运行主循环"""
        while True:
            self.display_menu()
            choice = input("\n请选择操作: ").strip()
            
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
                print("\n感谢使用超市收银系统，再见！")
                break
            else:
                print("无效的选择，请重试")
            
            input("\n按回车键继续...")

