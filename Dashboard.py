from graphlib import TopologicalSorter
from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
import sqlite3
from tkinter import messagebox
from product import productClass
import time
import os
from supplier import supplierClass
from category import categoryClass
from sales import salesClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Inventory Administration System ")
        self.root.config(bg="white")

        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Administration System",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        btn_logout=Button(self.root,text="Logout",command=self.Login1,font=("times new roman",15,"bold"),bg="yellow", cursor="hand2").place(x=1350,y=10,height=50,width=150)
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Administration System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        
        #----LeftMenu----
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,285),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=250,height=700)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP, fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.Exit,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)

        #---content----
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        



        #---footer---
        lbl_footer=Label(self.root,text="IMS-Inventory Administration System | Developed by  Akash\nFor any technical issue contact: 9955668852", font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)

        self.update_content()

    def employee(self):
        self.new__win=Toplevel(self.root)
        self.new_obj= employeeClass(self.new__win)
    
    def supplier(self):
        self.new__win=Toplevel(self.root)
        self.new_obj= supplierClass(self.new__win)

    def category(self):
        self.new__win=Toplevel(self.root)
        self.new_obj= categoryClass(self.new__win)

    
    def product(self):
        self.new__win=Toplevel(self.root)
        self.new_obj= productClass(self.new__win)

    def sales(self):
        self.new__win=Toplevel(self.root)
        self.new_obj= salesClass(self.new__win)
    
    
    def Login1(self):
        self.root.destroy()
        os.system("python Login.py")

    def Exit(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()
        
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Categories\n[{str(len(category))}]')

            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')

            self.lbl_sales.config(text=f"Total Sales\n [{str(len(os.listdir('bill')))}]")

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Administration System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
    
        
if __name__=="__main__":

    root=Tk()
    obj=IMS(root)
    root.mainloop()

