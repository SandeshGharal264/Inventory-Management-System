from graphlib import TopologicalSorter
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import os
import sqlite3
import time
import re
import tempfile
class billClass:
    def __init__(self,root):

    

        self.root=root
        self.root.geometry("1370x700+0+0")
        self.root.title("Inventory Administration System ")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0
#-----------Title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Administration System",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        btn_logout=Button(self.root,text="Logout",command=self.Login1,font=("times new roman",15,"bold"),bg="yellow", cursor="hand2").place(x=1150,y=10,height=50,width=150)
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Administration System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        self.pattern=re.compile("(0|91)?[-\s]?[6-9][0-9]{9}$")

        #--Product Frame---
        
        productFrame1=Frame(self.root,relief=RIDGE,bd=4,bg="white")
        productFrame1.place(x=6,y=110,width=410,height=550)

       
        ptitle=Label(productFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #--Product Search Frame---
        self.var_search=StringVar()
        
        productFrame2=Frame(productFrame1,relief=RIDGE,bd=2,bg="white")
        productFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(productFrame2,text="Search Product | BY Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_name=Label(productFrame2,text="Product Name ",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(productFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(productFrame2,text="Search",command=self.search,font=("times new roman",15),cursor="hand2",bg="#2196f3",fg="white").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(productFrame2,text="Show All",command=self.show,font=("times new roman",15),cursor="hand2",bg="#083531",fg="white").place(x=285,y=10,width=100,height=25)

        #--Product  Details Frame---

        productFrame3=Frame(productFrame1,bd=3,relief=RIDGE)
        productFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(productFrame3,orient=VERTICAL)
        scrollx=Scrollbar(productFrame3,orient=HORIZONTAL)

        self.Product_Table=ttk.Treeview(productFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.Product_Table.xview)
        scrolly.config(command=self.Product_Table.yview)


        self.Product_Table.heading("pid",text="PID")
        self.Product_Table.heading("name",text="Name")
        self.Product_Table.heading("price",text="Price")
        self.Product_Table.heading("qty",text="QTY")
        self.Product_Table.heading("status",text="Status")
        
       
        self.Product_Table["show"]="headings"

        self.Product_Table.column("pid",width=40)
        self.Product_Table.column("name",width=100)
        self.Product_Table.column("price",width=100)
        self.Product_Table.column("qty",width=40)
        self.Product_Table.column("status",width=90)
        self.Product_Table.pack(fill=BOTH,expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(productFrame1,text="Note: Enter 0 Quantity to remove product from the cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #--Customer Frame--
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        customerFrame=Frame(self.root,relief=RIDGE,bd=4,bg="white")
        customerFrame.place(x=420,y=110,width=530,height=70)

        ctitle=Label(customerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgrey").pack(side=TOP,fill=X)

        lbl_name=Label(customerFrame,text="Name ",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(customerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(customerFrame,text="Contact No. ",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(customerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

        #--Cal_cart frame

        cal_cart_Frame=Frame(self.root,relief=RIDGE,bd=2,bg="white")
        cal_cart_Frame.place(x=420,y=190,width=530,height=360)
        #calculator frame
        self.var_cal_input=StringVar()

        calFrame=Frame(cal_cart_Frame,relief=RIDGE,bd=9,bg="white")
        calFrame.place(x=5,y=10,width=268,height=340)
        txt_cal_input=Entry(calFrame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(calFrame,text='7',command=lambda:self.get_input(7),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(calFrame,text='8',command=lambda:self.get_input(8),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(calFrame,text='9',command=lambda:self.get_input(9),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(calFrame,text='+',command=lambda:self.get_input('+'),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(calFrame,text='4',command=lambda:self.get_input(4),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(calFrame,text='5',command=lambda:self.get_input(5),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(calFrame,text='6',command=lambda:self.get_input(6),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(calFrame,text='-',command=lambda:self.get_input('-'),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(calFrame,text='1',command=lambda:self.get_input(1),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(calFrame,text='2',command=lambda:self.get_input(2),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(calFrame,text='3',command=lambda:self.get_input(3),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(calFrame,text='*',command=lambda:self.get_input('*'),font=("arial",15,'bold'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(calFrame,text='0',command=lambda:self.get_input(0),font=("arial",15,'bold'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(calFrame,text='C',command=self.clear_cal,font=("arial",15,'bold'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(calFrame,text='=',command=self.perform_cal,font=("arial",15,'bold'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(calFrame,text='/',command=lambda:self.get_input('/'),font=("arial",15,'bold'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
    
        #cart frame

        cart_Frame=Frame(cal_cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)
        self.cart_title=Label(cart_Frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgrey")
        self.cart_title.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.cart_Table=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)


        self.cart_Table.heading("pid",text="PID")
        self.cart_Table.heading("name",text="Name")
        self.cart_Table.heading("price",text="Price")
        self.cart_Table.heading("qty",text="QTY")
        
        
       
        self.cart_Table["show"]="headings"

        self.cart_Table.column("pid",width=40)
        self.cart_Table.column("name",width=90)
        self.cart_Table.column("price",width=90)
        self.cart_Table.column("qty",width=40)
        self.cart_Table.pack(fill=BOTH,expand=1)
        self.cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)
        
        #-----ADD Cart Widgets Frame--
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()


        Add_Cart_Frame=Frame(self.root,relief=RIDGE,bd=2,bg="white")
        Add_Cart_Frame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_Cart_Frame,text="Product Name: ", font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_Cart_Frame,textvariable=self.var_pname, font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_Cart_Frame,text="Price Per Qty ", font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_Cart_Frame,textvariable=self.var_price, font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_Cart_Frame,text="Quantity", font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_Cart_Frame,textvariable=self.var_qty, font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_instock=Label(Add_Cart_Frame,text="In Stock", font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)

        btn_clear_cart=Button(Add_Cart_Frame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_Cart_Frame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        

 #---Billing Area------------
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)

        btitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)



        #Billing Buttons
        
        bill_menu_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menu_Frame.place(x=953,y=520,width=410,height=140)

        self.lbl_amount=Label(bill_menu_Frame,text="Bill Amount\n[0] ",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amount.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(bill_menu_Frame,text="Discount\n[5%] ",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(bill_menu_Frame,text="Net Pay \n[0] ",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)

        btn_Print=Button(bill_menu_Frame,text="Print",command=self.print_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
        btn_Print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(bill_menu_Frame,text="Clear All",command=self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg="grey",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(bill_menu_Frame,text="Generate/Save Bill",command=self.generate_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)

        #footer
        footer=Label(self.root,text="IMS-Inventory Administration System \n for any Technical issue contact: 8899556677",font=("times new roman",11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

        self.show()
        # self.bill_Top()
        self.update_date_time()
   
        #--All Functions--

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum) 
    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))



    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
                self.Product_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Product_Table.delete(*self.Product_Table.get_children())
                    for row in rows:
                        self.Product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.Product_Table.focus()
        content=(self.Product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')


    def get_data_cart(self,ev):
        f=self.cart_Table.focus()
        content=(self.cart_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        

    

    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please select product from the list",parent=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity is Required",parent=self.root)

        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        else:
            # price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            price_cal=self.var_price.get()
            cart_data= [self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            #Update cart
            present='NO'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present\nDo tou want to Update | Remove from cart List ",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal 
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_updates()


    def bill_updates(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))

        self.discount=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.discount
        self.lbl_amount.config(text=f'Bill Amnt.\n{str(self.bill_amt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cart_title.config(text=f"Cart\tTotal Product: [{str(len(self.cart_list))}]")
    


    def show_cart(self):
            try:
                self.cart_Table.delete(*self.cart_Table.get_children())
                for row in self.cart_list:
                    self.cart_Table.insert('',END,values=row)

            except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)


    def generate_bill(self):
        number=re.search(self.pattern,self.var_contact.get())
        if self.var_cname.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","Customer Details are required",parent=self.root)
        elif number==None:
            messagebox.showerror("Error","Invalid contact number",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","Please add product to the cart",parent=self.root)

        else:
            #------Bill Top-----
            self.bill_Top()
            #------Bill Middle-----
            self.bill_middle()
            #------Bill Bottom-----
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close
            self.chk_print=1
            messagebox.showinfo('Saved',"Bill has been generated/Saved in Backend",parent=self.root)

            
#----Bill top
    def bill_Top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No. 98725***** , Delhi-125001
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

#-----bill Bottom
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
        
#---- bill middle
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            for row in self.cart_list:
            # pid,name,price,qty,stock
        
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                cur.execute('Update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            self.show()
        except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)




    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In Stock ")
        self.var_stock.set('')
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cart_title.config(text=f"Cart\tTotal Product: [0]")
        self.lbl_amount.config(text=f'Bill Amnt.\n0')
        self.lbl_net_pay.config(text=f'Net Pay\n0')
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()


                    
            
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Administration System\t\t Date: {str(date_)}\t\t Time:{str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Error","Please generate bill,to print the receipt",parent=self.root)
            
    def Login1(self):
        self.root.destroy()
        os.system("python Login.py")

if __name__=="__main__":

    root=Tk()
    obj=billClass(root)
    root.mainloop()