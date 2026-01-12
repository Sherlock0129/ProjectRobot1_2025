"""
POS System Graphical User Interface
Implemented using Tkinter
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
    """POS System Graphical User Interface Class"""
    
    def __init__(self, sale_service: SaleService, return_service: ReturnService, 
                 inventory_service: InventoryService):
        """
        Initialize GUI
        
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
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Point of Sale System (POS)")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Setup styles
        self.setup_styles()
        
        # Create interface
        self.create_main_interface()
    
    def setup_styles(self):
        """Setup interface styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button styles
        style.configure('Title.TLabel', font=('Microsoft YaHei', 16, 'bold'), 
                       background='#f0f0f0', foreground='#2c3e50')
        style.configure('Heading.TLabel', font=('Microsoft YaHei', 12, 'bold'),
                       background='#f0f0f0', foreground='#34495e')
        style.configure('Action.TButton', font=('Microsoft YaHei', 10),
                       padding=10)
        style.configure('Primary.TButton', font=('Microsoft YaHei', 10, 'bold'),
                       padding=10)
    
    def create_main_interface(self):
        """Create main interface"""
        # Title bar
        title_frame = tk.Frame(self.root, bg='#3498db', height=80)
        title_frame.pack(fill=tk.X, padx=0, pady=0)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="Point of Sale System", 
                              font=('Microsoft YaHei', 24, 'bold'),
                              bg='#3498db', fg='white')
        title_label.pack(pady=20)
        
        # Main content area
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Button area
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # Create function buttons
        btn_width = 15
        btn_height = 3
        
        btn_sale = tk.Button(button_frame, text="Process Sale", 
                            font=('Microsoft YaHei', 12, 'bold'),
                            bg='#2ecc71', fg='white', width=btn_width, height=btn_height,
                            command=self.show_sale_window, cursor='hand2',
                            relief=tk.RAISED, bd=3)
        btn_sale.grid(row=0, column=0, padx=15, pady=10)
        
        btn_return = tk.Button(button_frame, text="Handle Returns", 
                              font=('Microsoft YaHei', 12, 'bold'),
                              bg='#e74c3c', fg='white', width=btn_width, height=btn_height,
                              command=self.show_return_window, cursor='hand2',
                              relief=tk.RAISED, bd=3)
        btn_return.grid(row=0, column=1, padx=15, pady=10)
        
        btn_products = tk.Button(button_frame, text="View Products", 
                                font=('Microsoft YaHei', 12, 'bold'),
                                bg='#3498db', fg='white', width=btn_width, height=btn_height,
                                command=self.show_products_window, cursor='hand2',
                                relief=tk.RAISED, bd=3)
        btn_products.grid(row=0, column=2, padx=15, pady=10)
        
        btn_history = tk.Button(button_frame, text="View History", 
                               font=('Microsoft YaHei', 12, 'bold'),
                               bg='#9b59b6', fg='white', width=btn_width, height=btn_height,
                               command=self.show_history_window, cursor='hand2',
                               relief=tk.RAISED, bd=3)
        btn_history.grid(row=0, column=3, padx=15, pady=10)
        
        btn_exit = tk.Button(button_frame, text="Exit System",
                            font=('Microsoft YaHei', 12, 'bold'),
                            bg='#7f8c8d', fg='white', width=btn_width, height=btn_height,
                            command=self.exit_system, cursor='hand2',
                            relief=tk.RAISED, bd=3)
        btn_exit.grid(row=1, column=0, padx=15, pady=20)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#34495e', height=40)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, text="Ready", 
                                     font=('Microsoft YaHei', 10),
                                     bg='#34495e', fg='white')
        self.status_label.pack(pady=10)
    
    def show_sale_window(self):
        """Show sale window"""
        sale_window = tk.Toplevel(self.root)
        sale_window.title("Process Sale")
        sale_window.geometry("800x600")
        sale_window.configure(bg='#f0f0f0')
        sale_window.transient(self.root)
        sale_window.grab_set()
        
        # Create new sale
        self.current_sale = self.sale_service.create_sale()
        
        # Title
        title_frame = tk.Frame(sale_window, bg='#2ecc71', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text=f"Sale: {self.current_sale.sale_id}",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#2ecc71', fg='white')
        title_label.pack(pady=15)
        
        # Main content area
        content_frame = tk.Frame(sale_window, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left: Add item area
        left_frame = tk.LabelFrame(content_frame, text="Add Item", 
                                   font=('Microsoft YaHei', 11, 'bold'),
                                   bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Product selection
        tk.Label(left_frame, text="Product ID:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, pady=5)
        product_var = tk.StringVar()
        product_combo = ttk.Combobox(left_frame, textvariable=product_var,
                                    font=('Microsoft YaHei', 10), width=20)
        products = self.inventory_service.get_all_products()
        product_combo['values'] = [f"{p.product_id} - {p.name} (¥{p.price:.2f})" 
                                   for p in products]
        product_combo.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(left_frame, text="Quantity:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, pady=5)
        quantity_var = tk.StringVar(value="1")
        quantity_entry = tk.Entry(left_frame, textvariable=quantity_var,
                                  font=('Microsoft YaHei', 10), width=22)
        quantity_entry.grid(row=1, column=1, pady=5, padx=5)
        
        def add_item():
            try:
                product_str = product_var.get()
                if not product_str:
                    messagebox.showwarning("Warning", "Please select a product")
                    return
                
                product_id = product_str.split(' - ')[0]
                quantity = int(quantity_var.get())
                
                if quantity <= 0:
                    messagebox.showwarning("Warning", "Quantity must be greater than 0")
                    return
                
                if self.sale_service.add_item_to_sale(self.current_sale, product_id, quantity):
                    messagebox.showinfo("Success", "Item added to sale")
                    update_sale_list()
                    update_total()
                    quantity_var.set("1")
                else:
                    messagebox.showerror("Error", "Add failed: Product not found or insufficient stock")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid quantity")
        
        add_btn = tk.Button(left_frame, text="Add Item", font=('Microsoft YaHei', 10, 'bold'),
                           bg='#3498db', fg='white', command=add_item,
                           width=15, cursor='hand2')
        add_btn.grid(row=2, column=0, columnspan=2, pady=15)
        
        # Right: Sale list
        right_frame = tk.LabelFrame(content_frame, text="Sale Details", 
                                    font=('Microsoft YaHei', 11, 'bold'),
                                    bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Sale items list
        sale_tree = ttk.Treeview(right_frame, columns=('name', 'quantity', 'price', 'subtotal'),
                                show='headings', height=12)
        sale_tree.heading('name', text='Product Name')
        sale_tree.heading('quantity', text='Quantity')
        sale_tree.heading('price', text='Price')
        sale_tree.heading('subtotal', text='Subtotal')
        sale_tree.column('name', width=150)
        sale_tree.column('quantity', width=80)
        sale_tree.column('price', width=100)
        sale_tree.column('subtotal', width=100)
        sale_tree.pack(fill=tk.BOTH, expand=True)
        
        # Total label
        total_label = tk.Label(right_frame, text="Total: $0.00",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#f0f0f0', fg='#e74c3c')
        total_label.pack(pady=10)
        
        def update_sale_list():
            """Update sale list"""
            for item in sale_tree.get_children():
                sale_tree.delete(item)
            
            for sale_item in self.current_sale.items:
                sale_tree.insert('', 'end', values=(
                    sale_item.product.name,
                    sale_item.quantity,
                    f"${sale_item.product.price:.2f}",
                    f"${sale_item.get_subtotal():.2f}"
                ))
        
        def update_total():
            """Update total"""
            total = self.current_sale.get_total()
            total_label.config(text=f"Total: ${total:.2f}")
        
        # Bottom button area
        bottom_frame = tk.Frame(sale_window, bg='#f0f0f0')
        bottom_frame.pack(fill=tk.X, padx=20, pady=10)
        
        def complete_sale():
            """Complete sale"""
            if not self.current_sale.items:
                messagebox.showwarning("Warning", "Sale is empty, cannot complete")
                return
            
            # Create payment dialog
            payment_window = tk.Toplevel(sale_window)
            payment_window.title("Complete Payment")
            payment_window.geometry("400x300")
            payment_window.configure(bg='#f0f0f0')
            payment_window.transient(sale_window)
            payment_window.grab_set()
            
            tk.Label(payment_window, text="Payment Information", font=('Microsoft YaHei', 14, 'bold'),
                    bg='#f0f0f0').pack(pady=20)
            
            total = self.current_sale.get_total()
            tk.Label(payment_window, text=f"Amount Due: ${total:.2f}",
                    font=('Microsoft YaHei', 12), bg='#f0f0f0').pack(pady=10)
            
            tk.Label(payment_window, text="Payment Method:", font=('Microsoft YaHei', 10),
                    bg='#f0f0f0').pack(pady=5)
            payment_method_var = tk.StringVar(value="Cash")
            payment_combo = ttk.Combobox(payment_window, textvariable=payment_method_var,
                                        values=["Cash", "Card", "Mobile"],
                                        font=('Microsoft YaHei', 10), width=20)
            payment_combo.pack(pady=5)
            
            tk.Label(payment_window, text="Payment Amount:", font=('Microsoft YaHei', 10),
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
                        messagebox.showerror("Error", "Insufficient payment amount")
                        return
                    
                    if self.sale_service.complete_sale(self.current_sale, 
                                                       payment_method_var.get(),
                                                       payment_amount):
                        change = self.current_sale.get_change()
                        msg = f"Sale Completed!\n\n"
                        msg += f"Payment Method: {payment_method_var.get()}\n"
                        msg += f"Payment Amount: ${payment_amount:.2f}\n"
                        if change > 0:
                            msg += f"Change: ${change:.2f}\n"
                        msg += f"\nSale ID: {self.current_sale.sale_id}"
                        messagebox.showinfo("Success", msg)
                        payment_window.destroy()
                        sale_window.destroy()
                        self.update_status(f"Sale completed: {self.current_sale.sale_id}")
                    else:
                        messagebox.showerror("Error", "Payment failed")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid payment amount")
            
            confirm_btn = tk.Button(payment_window, text="Confirm Payment", 
                                   font=('Microsoft YaHei', 10, 'bold'),
                                   bg='#2ecc71', fg='white', command=confirm_payment,
                                   width=15, cursor='hand2')
            confirm_btn.pack(pady=20)
        
        def cancel_sale():
            """Cancel sale"""
            if messagebox.askyesno("Confirm", "Are you sure you want to cancel this sale?"):
                self.sale_service.cancel_sale(self.current_sale)
                self.current_sale = None
                sale_window.destroy()
                self.update_status("Sale cancelled")
        
        complete_btn = tk.Button(bottom_frame, text="Complete Sale", 
                                font=('Microsoft YaHei', 11, 'bold'),
                                bg='#2ecc71', fg='white', command=complete_sale,
                                width=12, cursor='hand2', padx=10, pady=5)
        complete_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(bottom_frame, text="Cancel Sale", 
                              font=('Microsoft YaHei', 11),
                              bg='#95a5a6', fg='white', command=cancel_sale,
                              width=12, cursor='hand2', padx=10, pady=5)
        cancel_btn.pack(side=tk.LEFT, padx=5)
        
        # Initialize update
        update_sale_list()
        update_total()
    
    def show_return_window(self):
        """Show return window"""
        return_window = tk.Toplevel(self.root)
        return_window.title("Handle Returns")
        return_window.geometry("800x600")
        return_window.configure(bg='#f0f0f0')
        return_window.transient(self.root)
        return_window.grab_set()
        
        # Create new return
        original_sale_id = simpledialog.askstring("Original Sale", 
                                                  "Enter original sale ID (optional, cancel to skip):",
                                                  parent=return_window)
        self.current_return = self.return_service.create_return(
            original_sale_id if original_sale_id else None
        )
        
        # Title
        title_frame = tk.Frame(return_window, bg='#e74c3c', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_text = f"Return: {self.current_return.return_id}"
        if original_sale_id:
            title_text += f" (Original Sale: {original_sale_id})"
        title_label = tk.Label(title_frame, text=title_text,
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#e74c3c', fg='white')
        title_label.pack(pady=15)
        
        # Main content area
        content_frame = tk.Frame(return_window, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left: Add return item area
        left_frame = tk.LabelFrame(content_frame, text="Add Return Item", 
                                   font=('Microsoft YaHei', 11, 'bold'),
                                   bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Product selection
        tk.Label(left_frame, text="Product ID:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, pady=5)
        product_var = tk.StringVar()
        product_combo = ttk.Combobox(left_frame, textvariable=product_var,
                                    font=('Microsoft YaHei', 10), width=20)
        products = self.inventory_service.get_all_products()
        product_combo['values'] = [f"{p.product_id} - {p.name} (¥{p.price:.2f})" 
                                   for p in products]
        product_combo.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(left_frame, text="Return Quantity:", font=('Microsoft YaHei', 10),
                bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, pady=5)
        quantity_var = tk.StringVar(value="1")
        quantity_entry = tk.Entry(left_frame, textvariable=quantity_var,
                                  font=('Microsoft YaHei', 10), width=22)
        quantity_entry.grid(row=1, column=1, pady=5, padx=5)
        
        def add_item():
            try:
                product_str = product_var.get()
                if not product_str:
                    messagebox.showwarning("Warning", "Please select a product")
                    return
                
                product_id = product_str.split(' - ')[0]
                quantity = int(quantity_var.get())
                
                if quantity <= 0:
                    messagebox.showwarning("Warning", "Quantity must be greater than 0")
                    return
                
                if self.return_service.add_item_to_return(self.current_return, 
                                                          product_id, quantity):
                    messagebox.showinfo("Success", "Return item added")
                    update_return_list()
                    update_total()
                    quantity_var.set("1")
                else:
                    messagebox.showerror("Error", "Add failed: Product not found")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid quantity")
        
        add_btn = tk.Button(left_frame, text="Add Return Item", 
                           font=('Microsoft YaHei', 10, 'bold'),
                           bg='#3498db', fg='white', command=add_item,
                           width=15, cursor='hand2')
        add_btn.grid(row=2, column=0, columnspan=2, pady=15)
        
        # Right: Return list
        right_frame = tk.LabelFrame(content_frame, text="Return Details", 
                                    font=('Microsoft YaHei', 11, 'bold'),
                                    bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Return items list
        return_tree = ttk.Treeview(right_frame, columns=('name', 'quantity', 'price', 'subtotal'),
                                  show='headings', height=12)
        return_tree.heading('name', text='Product Name')
        return_tree.heading('quantity', text='Quantity')
        return_tree.heading('price', text='Price')
        return_tree.heading('subtotal', text='Subtotal')
        return_tree.column('name', width=150)
        return_tree.column('quantity', width=80)
        return_tree.column('price', width=100)
        return_tree.column('subtotal', width=100)
        return_tree.pack(fill=tk.BOTH, expand=True)
        
        # Total refund label
        total_label = tk.Label(right_frame, text="Total Refund: $0.00",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#f0f0f0', fg='#e74c3c')
        total_label.pack(pady=10)
        
        def update_return_list():
            """Update return list"""
            for item in return_tree.get_children():
                return_tree.delete(item)
            
            for return_item in self.current_return.items:
                return_tree.insert('', 'end', values=(
                    return_item.product.name,
                    return_item.quantity,
                    f"${return_item.product.price:.2f}",
                    f"${return_item.get_subtotal():.2f}"
                ))
              
        def update_total():
            """Update total refund"""
            total = self.current_return.get_total_refund()
            total_label.config(text=f"Total Refund: ${total:.2f}")
        
        # Bottom button area
        bottom_frame = tk.Frame(return_window, bg='#f0f0f0')
        bottom_frame.pack(fill=tk.X, padx=20, pady=10)
        
        def complete_return():
            """Complete return"""
            if not self.current_return.items:
                messagebox.showwarning("Warning", "Return is empty, cannot complete")
                return
            
            if messagebox.askyesno("Confirm", "Are you sure you want to complete this return?"):
                if self.return_service.complete_return(self.current_return):
                    msg = f"Return Completed!\n\n"
                    msg += f"Total Refund: ${self.current_return.get_total_refund():.2f}\n"
                    msg += f"Stock restored\n"
                    msg += f"\nReturn ID: {self.current_return.return_id}"
                    messagebox.showinfo("Success", msg)
                    return_window.destroy()
                    self.update_status(f"Return completed: {self.current_return.return_id}")
                else:
                    messagebox.showerror("Error", "Return failed")
        
        def cancel_return():
            """Cancel return"""
            if messagebox.askyesno("Confirm", "Are you sure you want to cancel this return?"):
                self.current_return = None
                return_window.destroy()
                self.update_status("Return cancelled")
        
        complete_btn = tk.Button(bottom_frame, text="Complete Return", 
                                 font=('Microsoft YaHei', 11, 'bold'),
                                 bg='#e74c3c', fg='white', command=complete_return,
                                 width=12, cursor='hand2', padx=10, pady=5)
        complete_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(bottom_frame, text="Cancel Return", 
                              font=('Microsoft YaHei', 11),
                              bg='#95a5a6', fg='white', command=cancel_return,
                              width=12, cursor='hand2', padx=10, pady=5)
        cancel_btn.pack(side=tk.LEFT, padx=5)
        
        # Initialize update
        update_return_list()
        update_total()
    
    def show_products_window(self):
        """Show products window"""
        products_window = tk.Toplevel(self.root)
        products_window.title("View Products")
        products_window.geometry("700x500")
        products_window.configure(bg='#f0f0f0')
        
        # Title
        title_frame = tk.Frame(products_window, bg='#3498db', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="Product List",
                              font=('Microsoft YaHei', 14, 'bold'),
                              bg='#3498db', fg='white')
        title_label.pack(pady=15)
        
        # Product list
        list_frame = tk.Frame(products_window, bg='#f0f0f0')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create table
        tree = ttk.Treeview(list_frame, columns=('id', 'name', 'price', 'stock'),
                           show='headings', height=15)
        tree.heading('id', text='Product ID')
        tree.heading('name', text='Product Name')
        tree.heading('price', text='Price')
        tree.heading('stock', text='Stock')
        tree.column('id', width=100)
        tree.column('name', width=200)
        tree.column('price', width=150)
        tree.column('stock', width=100)
        tree.pack(fill=tk.BOTH, expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Fill data
        products = self.inventory_service.get_all_products()
        for product in products:
            tree.insert('', 'end', values=(
                product.product_id,
                product.name,
                f"${product.price:.2f}",
                product.stock
            ))
    
    def show_history_window(self):
        """Show history window"""
        history_window = tk.Toplevel(self.root)
        history_window.title("View History")
        history_window.geometry("900x600")
        history_window.configure(bg='#f0f0f0')
        
        # Create tabs
        notebook = ttk.Notebook(history_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Sales history tab
        sales_frame = tk.Frame(notebook, bg='#f0f0f0')
        notebook.add(sales_frame, text="Sales History")
        
        sales_tree = ttk.Treeview(sales_frame, 
                                 columns=('id', 'time', 'items', 'total', 'payment'),
                                 show='headings', height=20)
        sales_tree.heading('id', text='Sale ID')
        sales_tree.heading('time', text='Time')
        sales_tree.heading('items', text='Items')
        sales_tree.heading('total', text='Total')
        sales_tree.heading('payment', text='Payment Method')
        sales_tree.column('id', width=150)
        sales_tree.column('time', width=150)
        sales_tree.column('items', width=100)
        sales_tree.column('total', width=120)
        sales_tree.column('payment', width=100)
        sales_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Fill sales history
        sales = self.sale_service.get_sales_history()
        for sale in sales:
            sales_tree.insert('', 'end', values=(
                sale.sale_id,
                sale.sale_time.strftime('%Y-%m-%d %H:%M:%S'),
                len(sale.items),
                f"${sale.get_total():.2f}",
                sale.payment_method or "Incomplete"
            ))
        
        # Return history tab
        returns_frame = tk.Frame(notebook, bg='#f0f0f0')
        notebook.add(returns_frame, text="Return History")
        
        returns_tree = ttk.Treeview(returns_frame,
                                    columns=('id', 'original', 'time', 'items', 'refund'),
                                    show='headings', height=20)
        returns_tree.heading('id', text='Return ID')
        returns_tree.heading('original', text='Original Sale')
        returns_tree.heading('time', text='Time')
        returns_tree.heading('items', text='Items')
        returns_tree.heading('refund', text='Refund Amount')
        returns_tree.column('id', width=150)
        returns_tree.column('original', width=150)
        returns_tree.column('time', width=150)
        returns_tree.column('items', width=100)
        returns_tree.column('refund', width=120)
        returns_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Fill return history
        returns = self.return_service.get_return_history()
        for return_transaction in returns:
            returns_tree.insert('', 'end', values=(
                return_transaction.return_id,
                return_transaction.original_sale_id or "None",
                return_transaction.return_time.strftime('%Y-%m-%d %H:%M:%S'),
                len(return_transaction.items),
                f"${return_transaction.get_total_refund():.2f}"
            ))
    
    def update_status(self, message: str):
        """Update status bar"""
        self.status_label.config(text=message)
        self.root.after(3000, lambda: self.status_label.config(text="Ready"))
    
    def exit_system(self):
        """Exit POS system"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit the system?"):
            self.root.destroy()
    
    def run(self):
        """Run GUI"""
        self.root.mainloop()



