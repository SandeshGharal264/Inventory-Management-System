import matplotlib.pyplot as plt
import numpy as np
import sqlite3
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class chartClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("450x200+100+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        lbl_rem=Label(self.root,text="REMAINING STOCK",font=("goudy old style",20),bg="white").place(x=50,y=100)
        btn_rem=Button(self.root,text="SHOW",command=self.remaining,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=100,y=170,width=110,height=28)
        
        # lbl_sale=Label(self.root,text="SALED PRODUCTS",font=("goudy old style",20),bg="white").place(x=350,y=100)
        # btn_sale=Button(self.root,text="SHOW",command=self.saled_stock,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=420,y=170,width=110,height=28)
        

        
        self.var_list1=[]
        self.var_list=[]
        self.var_list2=[]
        self.var_list3=[]
        self.var_list4=[]
        self.var_list5=[]
        self.var_list6=[]
        self.var_list7=[]
        self.rem_stocks()
        # self.Total_saled_stocks()

    

      
    def rem_stocks(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
           cur.execute("select * from product")
           rows=cur.fetchall()
           print(len(rows))
           i=1
           while i <= len(rows):
            cur.execute("select Name from product where pid=?",(f'{i}'))
            self.var_list.append(cur.fetchone())
            cur.execute("select qty from product where pid=?",(f'{i}'))
            self.var_list1.append(cur.fetchone())
            i+=1

           self.var_list = np.array(self.var_list)
           self.var_list=self.var_list.flatten()
        #    print(self.var_list1)
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def remaining(self):
        y = np.array(self.var_list1)
        y=y.flatten()
        total=sum(y)
        plt.pie(y, labels = self.var_list,autopct=lambda p:'{:.0f}'.format(p*total/100),shadow=True, startangle = 90)
        plt.title("REMAINING STOCKS")
        plt.show()

       
        
    # def Total_saled_stocks(self):
    #     con=sqlite3.connect(database=r'ims.db')
    #     cur=con.cursor()
    #     try:
    #        cur.execute("select * from productbackup")
    #        rows=cur.fetchall()
    #        i=1
    #        cur.execute("select Name from productbackup where pid=?",(f'{i}'))
    #        self.var_list4.append(cur.fetchone())
    #        cur.execute("select qty from productbackup where pid=?",(f'{i}'))
    #        self.var_list5.append(cur.fetchone())
    #        self.var_list5 = np.array(self.var_list5)
    #        self.var_list5=self.var_list5.flatten()

    #        while i < len(rows):
    #         del self.var_list6[:]
    #         cur.execute("select Name from productbackup where pid=?",(f'{i+1}'))
    #         self.var_list6.append(cur.fetchone())
    #         while self.var_list4[i-1]==self.var_list6[0]:
    #             cur.execute("select qty from productbackup where pid=?",(f'{i+1}'))
    #             self.var_list7.append(cur.fetchone())
    #             self.var_list7 = np.array(self.var_list7)
    #             self.var_list7=self.var_list6.flatten()
                
    #         if  self.var_list4[i-1]!=self.var_list6[0]:
    #             self.var_list4.append(self.var_list6[0])
    #             cur.execute("select qty from productbackup where pid=?",(f'{i+1}'))
    #             self.var_list5[i]=cur.fetchone()


    #         cur.execute("select qty from product where Name=?",(self.var_list4[i-1]))
    #         self.var_list2.append(cur.fetchone())
    #         print("list2:",self.var_list2)
    #         i=i+1
        

    #        self.var_list4 = np.array(self.var_list4)
    #        self.var_list4=self.var_list4.flatten()
           
    #     #    self.var_list5 = np.array(self.var_list5)
    #     #    self.var_list5=self.var_list5.flatten()
           
    #        self.var_list2 = np.array(self.var_list2)
    #        self.var_list2=self.var_list2.flatten()

    #        j=0
    #        while j<len(rows):
    #             self.var_list3.append(self.var_list7[j]-self.var_list2[j])
    #             self.var_list5.append(self.var_list5[i-1]+self.var_list3[i-1])
    #             j=j+1
          
    #     except Exception as ex:
    #         messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    # def saled_stock(self):
    #     y = np.array(self.var_list3)
    #     y=y.flatten()
    
    #     total=sum(y)
    # #    print(total)
    #     plt.pie(y, labels = self.var_list4,autopct=lambda p:'{:.0f}'.format(p*total/100),shadow=True, startangle = 90)
    #     plt.title("TOTAL SALED PRODUCTS")
    #     plt.show()
    

if __name__=="__main__":
    root=Tk()
    obj=chartClass(root)
    root.mainloop()

