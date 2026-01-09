"""
POS系统图形用户界面
使用Tkinter实现
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
from typing import Optional
from datetime import datetime
from domain.sale import Sale
from domain.return_transaction import ReturnTransaction
from service.sale_service import SaleService
from service.return_service import ReturnService
from service.inventory_service import InventoryService


class POSGUI:
    """POS系统图形用户界面类"""
    
    def __init__(self, sale_service: SaleService, return_service: ReturnService, 
                 inventory_service: InventoryService):
        """
        初始化GUI
        
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
        
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("超市收银系统 (POS System)")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # 设置样式
        self.setup_styles()
        
        # 创建界面
        self.create_main_interface()
    
    def setup_styles(self):
        """设置界面样式"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 配置按钮样式
        style.configure('Title.TLabel', font=('Microsoft YaHei', 16, 'bold'), 
                       background='#f0f0f0', foreground='#2c3e50')
        style.configure('Heading.TLabel', font=('Microsoft YaHei', 12, 'bold'),
                       background='#f0f0f0', foreground='#34495e')
        style.configure('Action.TButton', font=('Microsoft YaHei', 10),
                       padding=10)
        style.configure('Primary.TButton', font=('Microsoft YaHei', 10, 'bold'),
                       padding=10)
    
    def create_main_interface(self):
        """创建主界面"""
        # 标题栏
        title_frame = tk.Frame(self.root, bg='#3498db', height=80)
        title_frame.pack(fill=tk.X, padx=0, pady=0)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="超市收银系统", 
                              font=('Microsoft YaHei', 24, 'bold'),
                              bg='#3498db', fg='white')
        title_label.pack(pady=20)
        
        # 主内容区域
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 按钮区域
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # 创建功能按钮
        btn_width = 15
        btn_height = 3
        
        btn_sale = tk.Button(button_frame, text="处理销售\n(Process Sale)", 
                            font=('Microsoft YaHei', 12, 'bold'),
                            bg='#2ecc71', fg='white', width=btn_width, height=btn_height,
                            command=self.show_sale_window, cursor='hand2',
                            relief=tk.RAISED, bd=3)
        btn_sale.grid(row=0, column=0, padx=15, pady=10)
        
        btn_return = tk.Button(button_frame, text="处理退货\n(Handle Returns)", 
                              font=('Microsoft YaHei', 12, 'bold'),
                              bg='#e74c3c', fg='white', width=btn_width, height=btn_height,
                              command=self.show_return_window, cursor='hand2',
                              relief=tk.RAISED, bd=3)
        btn_return.grid(row=0, column=1, padx=15, pady=10)
        
        btn_products = tk.Button(button_frame, text="商品列表\n(View Products)", 
                                font=('Microsoft YaHei', 12, 'bold'),
                                bg='#3498db', fg='white', width=btn_width, height=btn_height,
                                command=self.show_products_window, cursor='hand2',
                                relief=tk.RAISED, bd=3)
        btn_products.grid(row=0, column=2, padx=15, pady=10)
        
        btn_history = tk.Button(button_frame, text="历史记录\n(View History)", 
                               font=('Microsoft YaHei', 12, 'bold'),
                               bg='#9b59b6', fg='white', width=btn_width, height=btn_height,
                               command=self.show_history_window, cursor='hand2',
                               relief=tk.RAISED, bd=3)
        btn_history.grid(row=0, column=3, padx=15, pady=10)
        
        # 状态栏
        status_frame = tk.Frame(self.root, bg='#34495e', height=40)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, text="就绪", 
                                     font=('Microsoft YaHei', 10),
                                     bg='#34495e', fg='white')
        self.status_label.pack(pady=10)
    
    def show_sale_window(self):
        """显示销售窗口"""
        sale_window = tk.Toplevel(self.root)
        sale_window.title("处理销售 - Process Sale")
        sale_window.geometry("800x600")
        sale_window.configure(bg='#f0f0f0')
        sale_window.transient(self.root)
        sale_window.grab_set()
        
        # 创建新的销售
        self.current_sale = self.sale_service.create_sale()
        
        # 标题
        title_frame = tk.Frame(sale_window, bg='#2ecc71', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text=f"销售单: {self.current_sale.sale_id}",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#2ecc71', fg='white')
        title_label.pack(pady=15)
        
        # 主内容区域
        content_frame = tk.Frame(sale_window, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 左侧：添加商品区域
        left_frame = tk.LabelFrame(content_frame, text="添加商品", 
                                   font=('Microsoft YaHei', 11, 'bold'),
                                   bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # 商品选择
        tk.Label(left_frame, text="商品ID:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, pady=5)
        product_var = tk.StringVar()
        product_combo = ttk.Combobox(left_frame, textvariable=product_var,
                                    font=('Microsoft YaHei', 10), width=20)
        products = self.inventory_service.get_all_products()
        product_combo['values'] = [f"{p.product_id} - {p.name} (¥{p.price:.2f})" 
                                   for p in products]
        product_combo.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(left_frame, text="数量:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, pady=5)
        quantity_var = tk.StringVar(value="1")
        quantity_entry = tk.Entry(left_frame, textvariable=quantity_var,
                                  font=('Microsoft YaHei', 10), width=22)
        quantity_entry.grid(row=1, column=1, pady=5, padx=5)
        
        def add_item():
            try:
                product_str = product_var.get()
                if not product_str:
                    messagebox.showwarning("警告", "请选择商品")
                    return
                
                product_id = product_str.split(' - ')[0]
                quantity = int(quantity_var.get())
                
                if quantity <= 0:
                    messagebox.showwarning("警告", "数量必须大于0")
                    return
                
                if self.sale_service.add_item_to_sale(self.current_sale, product_id, quantity):
                    messagebox.showinfo("成功", "商品已添加到销售单")
                    update_sale_list()
                    update_total()
                    quantity_var.set("1")
                else:
                    messagebox.showerror("错误", "添加失败：商品不存在或库存不足")
            except ValueError:
                messagebox.showerror("错误", "请输入有效的数量")
        
        add_btn = tk.Button(left_frame, text="添加商品", font=('Microsoft YaHei', 10, 'bold'),
                           bg='#3498db', fg='white', command=add_item,
                           width=15, cursor='hand2')
        add_btn.grid(row=2, column=0, columnspan=2, pady=15)
        
        # 右侧：销售单列表
        right_frame = tk.LabelFrame(content_frame, text="销售单明细", 
                                    font=('Microsoft YaHei', 11, 'bold'),
                                    bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 销售项列表
        sale_tree = ttk.Treeview(right_frame, columns=('name', 'quantity', 'price', 'subtotal'),
                                show='headings', height=12)
        sale_tree.heading('name', text='商品名称')
        sale_tree.heading('quantity', text='数量')
        sale_tree.heading('price', text='单价')
        sale_tree.heading('subtotal', text='小计')
        sale_tree.column('name', width=150)
        sale_tree.column('quantity', width=80)
        sale_tree.column('price', width=100)
        sale_tree.column('subtotal', width=100)
        sale_tree.pack(fill=tk.BOTH, expand=True)
        
        # 总计标签
        total_label = tk.Label(right_frame, text="总计: ¥0.00",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#f0f0f0', fg='#e74c3c')
        total_label.pack(pady=10)
        
        def update_sale_list():
            """更新销售单列表"""
            for item in sale_tree.get_children():
                sale_tree.delete(item)
            
            for sale_item in self.current_sale.items:
                sale_tree.insert('', 'end', values=(
                    sale_item.product.name,
                    sale_item.quantity,
                    f"¥{sale_item.product.price:.2f}",
                    f"¥{sale_item.get_subtotal():.2f}"
                ))
        
        def update_total():
            """更新总计"""
            total = self.current_sale.get_total()
            total_label.config(text=f"总计: ¥{total:.2f}")
        
        # 底部按钮区域
        bottom_frame = tk.Frame(sale_window, bg='#f0f0f0')
        bottom_frame.pack(fill=tk.X, padx=20, pady=10)
        
        def complete_sale():
            """完成销售"""
            if not self.current_sale.items:
                messagebox.showwarning("警告", "销售单为空，无法完成")
                return
            
            # 创建支付对话框
            payment_window = tk.Toplevel(sale_window)
            payment_window.title("完成支付")
            payment_window.geometry("400x300")
            payment_window.configure(bg='#f0f0f0')
            payment_window.transient(sale_window)
            payment_window.grab_set()
            
            tk.Label(payment_window, text="支付信息", font=('Microsoft YaHei', 14, 'bold'),
                    bg='#f0f0f0').pack(pady=20)
            
            total = self.current_sale.get_total()
            tk.Label(payment_window, text=f"应付金额: ¥{total:.2f}",
                    font=('Microsoft YaHei', 12), bg='#f0f0f0').pack(pady=10)
            
            tk.Label(payment_window, text="支付方式:", font=('Microsoft YaHei', 10),
                    bg='#f0f0f0').pack(pady=5)
            payment_method_var = tk.StringVar(value="现金")
            payment_combo = ttk.Combobox(payment_window, textvariable=payment_method_var,
                                        values=["现金", "刷卡", "移动支付"],
                                        font=('Microsoft YaHei', 10), width=20)
            payment_combo.pack(pady=5)
            
            tk.Label(payment_window, text="支付金额:", font=('Microsoft YaHei', 10),
                    bg='#f0f0f0').pack(pady=5)
            payment_amount_var = tk.StringVar()
            payment_entry = tk.Entry(payment_window, textvariable=payment_amount_var,
                                     font=('Microsoft YaHei', 10), width=22)
            payment_entry.pack(pady=5)
            payment_entry.focus()
            
            def confirm_payment():
                try:
                    payment_amount = float(payment_amount_var.get())
                    if payment_amount < total:
                        messagebox.showerror("错误", "支付金额不足")
                        return
                    
                    if self.sale_service.complete_sale(self.current_sale, 
                                                       payment_method_var.get(),
                                                       payment_amount):
                        change = self.current_sale.get_change()
                        msg = f"销售完成！\n\n"
                        msg += f"支付方式: {payment_method_var.get()}\n"
                        msg += f"支付金额: ¥{payment_amount:.2f}\n"
                        if change > 0:
                            msg += f"找零: ¥{change:.2f}\n"
                        msg += f"\n销售单号: {self.current_sale.sale_id}"
                        messagebox.showinfo("成功", msg)
                        payment_window.destroy()
                        sale_window.destroy()
                        self.update_status(f"销售完成: {self.current_sale.sale_id}")
                    else:
                        messagebox.showerror("错误", "支付失败")
                except ValueError:
                    messagebox.showerror("错误", "请输入有效的支付金额")
            
            confirm_btn = tk.Button(payment_window, text="确认支付", 
                                   font=('Microsoft YaHei', 10, 'bold'),
                                   bg='#2ecc71', fg='white', command=confirm_payment,
                                   width=15, cursor='hand2')
            confirm_btn.pack(pady=20)
        
        def cancel_sale():
            """取消销售"""
            if messagebox.askyesno("确认", "确定要取消本次销售吗？"):
                self.sale_service.cancel_sale(self.current_sale)
                self.current_sale = None
                sale_window.destroy()
                self.update_status("销售已取消")
        
        complete_btn = tk.Button(bottom_frame, text="完成销售", 
                                font=('Microsoft YaHei', 11, 'bold'),
                                bg='#2ecc71', fg='white', command=complete_sale,
                                width=12, cursor='hand2', padx=10, pady=5)
        complete_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(bottom_frame, text="取消销售", 
                              font=('Microsoft YaHei', 11),
                              bg='#95a5a6', fg='white', command=cancel_sale,
                              width=12, cursor='hand2', padx=10, pady=5)
        cancel_btn.pack(side=tk.LEFT, padx=5)
        
        # 初始化更新
        update_sale_list()
        update_total()
    
    def show_return_window(self):
        """显示退货窗口"""
        return_window = tk.Toplevel(self.root)
        return_window.title("处理退货 - Handle Returns")
        return_window.geometry("800x600")
        return_window.configure(bg='#f0f0f0')
        return_window.transient(self.root)
        return_window.grab_set()
        
        # 创建新的退货
        original_sale_id = simpledialog.askstring("原始销售单", 
                                                  "请输入原始销售单ID（可选，直接取消跳过）:",
                                                  parent=return_window)
        self.current_return = self.return_service.create_return(
            original_sale_id if original_sale_id else None
        )
        
        # 标题
        title_frame = tk.Frame(return_window, bg='#e74c3c', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_text = f"退货单: {self.current_return.return_id}"
        if original_sale_id:
            title_text += f" (原销售单: {original_sale_id})"
        title_label = tk.Label(title_frame, text=title_text,
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#e74c3c', fg='white')
        title_label.pack(pady=15)
        
        # 主内容区域
        content_frame = tk.Frame(return_window, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 左侧：添加退货商品区域
        left_frame = tk.LabelFrame(content_frame, text="添加退货商品", 
                                   font=('Microsoft YaHei', 11, 'bold'),
                                   bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # 商品选择
        tk.Label(left_frame, text="商品ID:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, pady=5)
        product_var = tk.StringVar()
        product_combo = ttk.Combobox(left_frame, textvariable=product_var,
                                    font=('Microsoft YaHei', 10), width=20)
        products = self.inventory_service.get_all_products()
        product_combo['values'] = [f"{p.product_id} - {p.name} (¥{p.price:.2f})" 
                                   for p in products]
        product_combo.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(left_frame, text="退货数量:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, pady=5)
        quantity_var = tk.StringVar(value="1")
        quantity_entry = tk.Entry(left_frame, textvariable=quantity_var,
                                  font=('Microsoft YaHei', 10), width=22)
        quantity_entry.grid(row=1, column=1, pady=5, padx=5)
        
        def add_item():
            try:
                product_str = product_var.get()
                if not product_str:
                    messagebox.showwarning("警告", "请选择商品")
                    return
                
                product_id = product_str.split(' - ')[0]
                quantity = int(quantity_var.get())
                
                if quantity <= 0:
                    messagebox.showwarning("警告", "数量必须大于0")
                    return
                
                if self.return_service.add_item_to_return(self.current_return, 
                                                          product_id, quantity):
                    messagebox.showinfo("成功", "退货商品已添加")
                    update_return_list()
                    update_total()
                    quantity_var.set("1")
                else:
                    messagebox.showerror("错误", "添加失败：商品不存在")
            except ValueError:
                messagebox.showerror("错误", "请输入有效的数量")
        
        add_btn = tk.Button(left_frame, text="添加退货商品", 
                           font=('Microsoft YaHei', 10, 'bold'),
                           bg='#3498db', fg='white', command=add_item,
                           width=15, cursor='hand2')
        add_btn.grid(row=2, column=0, columnspan=2, pady=15)
        
        # 右侧：退货单列表
        right_frame = tk.LabelFrame(content_frame, text="退货单明细", 
                                    font=('Microsoft YaHei', 11, 'bold'),
                                    bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 退货项列表
        return_tree = ttk.Treeview(right_frame, columns=('name', 'quantity', 'price', 'subtotal'),
                                  show='headings', height=12)
        return_tree.heading('name', text='商品名称')
        return_tree.heading('quantity', text='数量')
        return_tree.heading('price', text='单价')
        return_tree.heading('subtotal', text='小计')
        return_tree.column('name', width=150)
        return_tree.column('quantity', width=80)
        return_tree.column('price', width=100)
        return_tree.column('subtotal', width=100)
        return_tree.pack(fill=tk.BOTH, expand=True)
        
        # 退款总额标签
        total_label = tk.Label(right_frame, text="退款总额: ¥0.00",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#f0f0f0', fg='#e74c3c')
        total_label.pack(pady=10)
        
        def update_return_list():
            """更新退货单列表"""
            for item in return_tree.get_children():
                return_tree.delete(item)
            
            for return_item in self.current_return.items:
                return_tree.insert('', 'end', values=(
                    return_item.product.name,
                    return_item.quantity,
                    f"¥{return_item.product.price:.2f}",
                    f"¥{return_item.get_subtotal():.2f}"
                ))
        
        def update_total():
            """更新退款总额"""
            total = self.current_return.get_total_refund()
            total_label.config(text=f"退款总额: ¥{total:.2f}")
        
        # 底部按钮区域
        bottom_frame = tk.Frame(return_window, bg='#f0f0f0')
        bottom_frame.pack(fill=tk.X, padx=20, pady=10)
        
        def complete_return():
            """完成退货"""
            if not self.current_return.items:
                messagebox.showwarning("警告", "退货单为空，无法完成")
                return
            
            if messagebox.askyesno("确认", "确定要完成退货吗？"):
                if self.return_service.complete_return(self.current_return):
                    msg = f"退货完成！\n\n"
                    msg += f"退款总额: ¥{self.current_return.get_total_refund():.2f}\n"
                    msg += f"库存已恢复\n"
                    msg += f"\n退货单号: {self.current_return.return_id}"
                    messagebox.showinfo("成功", msg)
                    return_window.destroy()
                    self.update_status(f"退货完成: {self.current_return.return_id}")
                else:
                    messagebox.showerror("错误", "退货失败")
        
        def cancel_return():
            """取消退货"""
            if messagebox.askyesno("确认", "确定要取消本次退货吗？"):
                self.current_return = None
                return_window.destroy()
                self.update_status("退货已取消")
        
        complete_btn = tk.Button(bottom_frame, text="完成退货", 
                                 font=('Microsoft YaHei', 11, 'bold'),
                                 bg='#e74c3c', fg='white', command=complete_return,
                                 width=12, cursor='hand2', padx=10, pady=5)
        complete_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(bottom_frame, text="取消退货", 
                              font=('Microsoft YaHei', 11),
                              bg='#95a5a6', fg='white', command=cancel_return,
                              width=12, cursor='hand2', padx=10, pady=5)
        cancel_btn.pack(side=tk.LEFT, padx=5)
        
        # 初始化更新
        update_return_list()
        update_total()
    
    def show_products_window(self):
        """显示商品列表窗口"""
        products_window = tk.Toplevel(self.root)
        products_window.title("商品列表 - View Products")
        products_window.geometry("700x500")
        products_window.configure(bg='#f0f0f0')
        
        # 标题
        title_frame = tk.Frame(products_window, bg='#3498db', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="商品列表",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#3498db', fg='white')
        title_label.pack(pady=15)
        
        # 商品列表
        list_frame = tk.Frame(products_window, bg='#f0f0f0')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 创建表格
        tree = ttk.Treeview(list_frame, columns=('id', 'name', 'price', 'stock'),
                           show='headings', height=15)
        tree.heading('id', text='商品ID')
        tree.heading('name', text='商品名称')
        tree.heading('price', text='单价')
        tree.heading('stock', text='库存')
        tree.column('id', width=100)
        tree.column('name', width=200)
        tree.column('price', width=150)
        tree.column('stock', width=100)
        tree.pack(fill=tk.BOTH, expand=True)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # 填充数据
        products = self.inventory_service.get_all_products()
        for product in products:
            tree.insert('', 'end', values=(
                product.product_id,
                product.name,
                f"¥{product.price:.2f}",
                product.stock
            ))
    
    def show_history_window(self):
        """显示历史记录窗口"""
        history_window = tk.Toplevel(self.root)
        history_window.title("历史记录 - View History")
        history_window.geometry("900x600")
        history_window.configure(bg='#f0f0f0')
        
        # 创建标签页
        notebook = ttk.Notebook(history_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 销售历史标签页
        sales_frame = tk.Frame(notebook, bg='#f0f0f0')
        notebook.add(sales_frame, text="销售历史")
        
        sales_tree = ttk.Treeview(sales_frame, 
                                 columns=('id', 'time', 'items', 'total', 'payment'),
                                 show='headings', height=20)
        sales_tree.heading('id', text='销售单号')
        sales_tree.heading('time', text='时间')
        sales_tree.heading('items', text='商品数量')
        sales_tree.heading('total', text='总金额')
        sales_tree.heading('payment', text='支付方式')
        sales_tree.column('id', width=150)
        sales_tree.column('time', width=150)
        sales_tree.column('items', width=100)
        sales_tree.column('total', width=120)
        sales_tree.column('payment', width=100)
        sales_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 填充销售历史
        sales = self.sale_service.get_sales_history()
        for sale in sales:
            sales_tree.insert('', 'end', values=(
                sale.sale_id,
                sale.sale_time.strftime('%Y-%m-%d %H:%M:%S'),
                len(sale.items),
                f"¥{sale.get_total():.2f}",
                sale.payment_method or "未完成"
            ))
        
        # 退货历史标签页
        returns_frame = tk.Frame(notebook, bg='#f0f0f0')
        notebook.add(returns_frame, text="退货历史")
        
        returns_tree = ttk.Treeview(returns_frame,
                                    columns=('id', 'original', 'time', 'items', 'refund'),
                                    show='headings', height=20)
        returns_tree.heading('id', text='退货单号')
        returns_tree.heading('original', text='原销售单')
        returns_tree.heading('time', text='时间')
        returns_tree.heading('items', text='商品数量')
        returns_tree.heading('refund', text='退款金额')
        returns_tree.column('id', width=150)
        returns_tree.column('original', width=150)
        returns_tree.column('time', width=150)
        returns_tree.column('items', width=100)
        returns_tree.column('refund', width=120)
        returns_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 填充退货历史
        returns = self.return_service.get_return_history()
        for return_transaction in returns:
            returns_tree.insert('', 'end', values=(
                return_transaction.return_id,
                return_transaction.original_sale_id or "无",
                return_transaction.return_time.strftime('%Y-%m-%d %H:%M:%S'),
                len(return_transaction.items),
                f"¥{return_transaction.get_total_refund():.2f}"
            ))
    
    def update_status(self, message: str):
        """更新状态栏"""
        self.status_label.config(text=message)
        self.root.after(3000, lambda: self.status_label.config(text="就绪"))
    
    def run(self):
        """运行GUI"""
        self.root.mainloop()



