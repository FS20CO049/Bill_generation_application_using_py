
from tkinter import*
import math, random, os
from tkinter import messagebox
import os

class Bill_app:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Biling software")
        bg_color="#66CDAA"
        title=Label(self.root, text ="DAILY INVOICE",bd=12,relief=GROOVE,font=("times new roman",30,"bold"),fg="darkblue",bg=bg_color, pady=3).pack(fill=X)

        #cosmetic variable+++=+==++
        self.facewash=IntVar()
        self.haircolor=IntVar()
        self.perfume=IntVar()
        self.bodylotion=IntVar()
        self.shampooes=IntVar()
        self.facecream=IntVar()
        #_---------Grocery----------
        self.rice=IntVar()
        self.sugar=IntVar()
        self.flaur=IntVar()
        self.kidneybeans=IntVar()
        self.pasta=IntVar()
        self.cookingoil=IntVar()
        #-----------colddrink----------------
        self.cocacola=IntVar()
        self.sprite=IntVar()
        self.mazza=IntVar()
        self.fanta=IntVar()
        self.pepsi=IntVar()
        self.fizz=IntVar()
        #-----total product price& tax variable------
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.colddrink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.colddrink_tax=StringVar()
        #----------customer-------------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



       #customer frame
        f1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,fg="purple",font=("times new roman",15,"bold"),bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)
        cname_lab=Label(f1,text="Customer Name",bg=bg_color,fg="black",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lab=Label(f1,text="Phone No",bg=bg_color,fg="black",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_text=Entry(f1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lab=Label(f1,text="Bill number",bg=bg_color,fg="black",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_text=Entry(f1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(f1,text="Search",width=10,bd=7,command=self.find_bill,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        # cosmetics Frame
        f2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,fg="purple",font=("times new roman",15,"bold"),bg=bg_color)
        f2.place(x=5,y=180,width=325,height=380)
        facew_lbl=Label(f2,text="Facewash",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,sticky="w")
        facew_text=Entry(f2,width=10,textvariable=self.facewash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        hairc_lbl=Label(f2,text="Hair Color",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,sticky="w")
        hairc_text=Entry(f2,width=10,textvariable=self.haircolor,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        perfume_lbl=Label(f2,text="Perfume",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,sticky="w")
        perfume_text=Entry(f2,width=10,textvariable=self.perfume,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        bodyl_lbl=Label(f2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,sticky="w")
        bodyl_text=Entry(f2,width=10,textvariable=self.bodylotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hairsh_lbl=Label(f2,text="Shampoos",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,sticky="w")
        hairsh_text=Entry(f2,width=10,textvariable=self.shampooes,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        facec_lbl=Label(f2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,sticky="w")
        facec_text=Entry(f2,width=10,textvariable=self.facecream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


         # grocery Frame
        f3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,fg="purple",font=("times new roman",15,"bold"),bg=bg_color)
        f3.place(x=340,y=180,width=325,height=380)
        g1_lbl=Label(f3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,sticky="w")
        g1_text=Entry(f3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(f3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,sticky="w")
        g2_text=Entry(f3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(f3,text="Flour",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,sticky="w")
        g3_text=Entry(f3,width=10,textvariable=self.flaur,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(f3,text="Kidney beans",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,sticky="w")
        g4_text=Entry(f3,width=10,textvariable=self.kidneybeans,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(f3,text="Pasta",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,sticky="w")
        g5_text=Entry(f3,width=10,textvariable=self.pasta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(f3,text="Cooking Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,sticky="w")
        g6_text=Entry(f3,width=10,textvariable=self.cookingoil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         # soft drinks 
        f4=LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,fg="purple",font=("times new roman",15,"bold"),bg=bg_color)
        f4.place(x=670,y=180,width=325,height=380)
        d1_lbl=Label(f4,text="Coca-Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,sticky="w")
        d1_text=Entry(f4,width=10,textvariable=self.cocacola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        d2_lbl=Label(f4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,sticky="w")
        d2_text=Entry(f4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        d3_lbl=Label(f4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,sticky="w")
        d3_text=Entry(f4,width=10,textvariable=self.mazza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        d4_lbl=Label(f4,text="Fanta",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,sticky="w")
        d4_text=Entry(f4,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        d5_lbl=Label(f4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,sticky="w")
        d5_text=Entry(f4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        d6_lbl=Label(f4,text="Fizz",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,sticky="w")
        d6_text=Entry(f4,width=10,textvariable=self.fizz,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #Bill Area
        f5=LabelFrame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1010,y=180,width=340,height=380)
        Bill_title=Label(f5,text="Bill Area",font="Arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill menu
        f6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,fg="purple",font=("times new roman",15,"bold"),bg=bg_color)
        f6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(f6,text="Total Cosmetic Price",font=("times new roman",14,"bold"),fg="black",bg=bg_color).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(f6,text="Total Grocery Price",font=("times new roman",14,"bold"),fg="black",bg=bg_color).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(f6,width=18,textvariable=self.grocery_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(f6,text="Total Cold drink Price",font=("times new roman",14,"bold"),fg="black",bg=bg_color).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(f6,width=18,textvariable=self.colddrink_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(f6,text="Cosmetic Tax",font=("times new roman",14,"bold"),fg="black",bg=bg_color).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(f6,width=18,textvariable=self.cosmetic_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(f6,text="Grocery Tax",font=("times new roman",14,"bold"),fg="black",bg=bg_color).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(f6,width=18,textvariable=self.grocery_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(f6,text="Cold drink Tax",font=("times new roman",14,"bold"),fg="black",bg=bg_color).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(f6,width=18,textvariable=self.colddrink_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(f6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
            self.c_facewash_p=self.facewash.get()*80
            self.c_haircolor_p=self.haircolor.get()*70
            self.c_perfume_p=self.perfume.get()*100
            self.c_bodylotion_p=self.bodylotion.get()*170
            self.c_shampooes_p=self.shampooes.get()*85
            self.c_facecream_p=self.facecream.get()*120


            self.total_cosmatic_price=float(
                                        self.c_facewash_p+
                                        self.c_haircolor_p+
                                        self.c_perfume_p+
                                        self.c_bodylotion_p+
                                        self.c_shampooes_p+
                                        self.c_facecream_p
                                        )
            self.cosmetic_price.set("Rs "+str(self.total_cosmatic_price)) 
            self.c_tax=round((self.total_cosmatic_price*0.05),2)
            self.cosmetic_tax.set("Rs. "+str(self.c_tax))

            self.g_rice_p=self.rice.get()*110
            self.g_sugar_p=self.sugar.get()*45
            self.g_flaur_p=self.flaur.get()*85
            self.g_kidneybean_p=self.kidneybeans.get()*90
            self.g_pasta_p= self.pasta.get()*68
            self.g_oil_p=self.cookingoil.get()*250



            self.total_grocery_price=float(
                                        self.g_rice_p+
                                        self.g_sugar_p+
                                        self.g_flaur_p+
                                        self.g_kidneybean_p+
                                        self.g_pasta_p+
                                        self.g_oil_p
                                        )
            self.grocery_price.set("Rs "+str(self.total_grocery_price))
            self.g_tax=round((self.total_grocery_price*0.05),2)
            self.grocery_tax.set("Rs. "+str(self.g_tax) )


            self.d_cola_p=self.cocacola.get()*40
            self.d_sprite_p=self.sprite.get()*30
            self.d_mazza_p=self.mazza.get()*80
            self.d_fanta_p=self.fanta.get()*50
            self.d_pepsi_p=self.pepsi.get()*75
            self.d_fizz_p=self.fizz.get()*60

            self.total_colddrink_price=float(
                                        self.d_cola_p+
                                        self.d_sprite_p+
                                        self.d_mazza_p+
                                        self.d_fanta_p+
                                        self.d_pepsi_p+
                                        self.d_fizz_p
                                        )
            self.colddrink_price.set("Rs "+str(self.total_colddrink_price))
            self.d_tax=round((self.total_colddrink_price*0.05),2) 
            self.colddrink_tax.set("Rs. "+str(self.d_tax))

            self.total_Bill=float(self.total_cosmatic_price+self.total_grocery_price+self.total_colddrink_price+self.c_tax+self.g_tax+self.d_tax)
            


    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome to GK shop")
        self.textarea.insert(END,f"\n Bill No. : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone No: {self.c_phone.get()}")
        self.textarea.insert(END,f"\n ====================================")
        self.textarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.textarea.insert(END,f"\n ====================================")




    def  bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
           messagebox.showerror("Error","Enter Customer Details")
        elif self.cosmetic_price.get()=="Rs 0.0" and self.grocery_price.get()=="Rs 0.0" and self.colddrink_price.get()=="Rs 0.0":
            messagebox.showerror("Error","Products not Purchased")  
        else:   
        
          self.welcome_bill()
        
         #cosmetics prices
          if self.facewash.get()!=0:
            self.textarea.insert(END,f"\n facewash\t\t{self.facewash.get()}\t\t{self.c_facewash_p}")

          if self.haircolor.get()!=0:
            self.textarea.insert(END,f"\n Haircolor\t\t{self.haircolor.get()}\t\t{self.c_haircolor_p}")

          if self.perfume.get()!=0:
            self.textarea.insert(END,f"\n Perfume\t\t{self.perfume.get()}\t\t{self.c_perfume_p}")

          if self.bodylotion.get()!=0:
            self.textarea.insert(END,f"\n BodyLotion\t\t{self.bodylotion.get()}\t\t{self.c_bodylotion_p}")

          if self.shampooes.get()!=0:
            self.textarea.insert(END,f"\n Shampooes\t\t{self.shampooes.get()}\t\t{self.c_shampooes_p}")

          if self.facecream.get()!=0:
            self.textarea.insert(END,f"\n Facecream\t\t{self.facecream.get()}\t\t{self.c_facecream_p}")                

          #grocery prices
          if self.rice.get()!=0:
            self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}kg\t\t{self.g_rice_p}")

          if self.sugar.get()!=0:
            self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}kg\t\t{self.g_sugar_p}")

          if self.flaur.get()!=0:
            self.textarea.insert(END,f"\n Flour\t\t{self.flaur.get()}kg\t\t{self.g_flaur_p}")

          if self.kidneybeans.get()!=0:
            self.textarea.insert(END,f"\n KidneyBeans\t\t{self.kidneybeans.get()}kg\t\t{self.g_kidneybean_p}")

          if self.pasta.get()!=0:
            self.textarea.insert(END,f"\n Pasta\t\t{self.pasta.get()}kg\t\t{self.g_pasta_p}")

          if self.cookingoil.get()!=0:
            self.textarea.insert(END,f"\n Cooking Oil\t\t{self.cookingoil.get()}kg\t\t{self.g_oil_p}")

          #colddrink prices
          if self.cocacola.get()!=0:
            self.textarea.insert(END,f"\n CoCa-Cola\t\t{self.cocacola.get()}\t\t{self.d_cola_p}")

          if self.sprite.get()!=0:
            self.textarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_sprite_p}")

          if self.mazza.get()!=0:
            self.textarea.insert(END,f"\n Maaza\t\t{self.mazza.get()}\t\t{self.d_mazza_p}")

          if self.fanta.get()!=0:
            self.textarea.insert(END,f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_fanta_p}")

          if self.pepsi.get()!=0:
            self.textarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_pepsi_p}")

          if self.fizz.get()!=0:
            self.textarea.insert(END,f"\n Fizz\t\t{self.fizz.get()}\t\t{self.d_fizz_p}")


        self.textarea.insert(END,f"\n ------------------------------------")
        if self.cosmetic_tax.get()!="Rs. 0.0":
           self.textarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
        if self.grocery_tax.get()!="Rs. 0.0":
           self.textarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.colddrink_tax.get()!="Rs. 0.0":
           self.textarea.insert(END,f"\n ColdDrink Tax\t\t\t{self.colddrink_tax.get()}")      
        self.textarea.insert(END,f"\n ------------------------------------")  

        self.textarea.insert(END,f"\n Total Bill: \t\t\tRs.{str(self.total_Bill)}")  
        self.textarea.insert(END,f"\n ------------------------------------")
        self.save_bill()  

        

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do ypu want to save the Bill ?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open(r"C:\Users\kavya\OneDrive\Desktop\Billing app\bills"+str(self.bill_no.get())+".txt","w") 
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"bill no{self.bill_no.get()} saved successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir(r"C:\Users\kavya\OneDrive\Desktop\Billing app\bills") :
            if i.split('.')[0] ==self.search_bill.get() :
               f1 = open(f"Billing app\bills/{i}","r")
               self.textarea.delete('1.0',END)
               for d in f1:
                   self.textarea.insert(END,d)
               f1.close()
               present=="yes"
        if present=="no":
          messagebox.showerror("Error","Invalid bill no")

    def clear_data(self) :
        #cosmetic variable+++=+==++
        self.facewash.set(0)
        self.haircolor.set(0)
        self.perfume.set(0)
        self.bodylotion.set(0)
        self.shampooes.set(0)
        self.facecream.set(0)
        #_---------Grocery----------
        self.rice.set(0)
        self.sugar.set(0)
        self.flaur.set(0)
        self.kidneybeans.set(0)
        self.pasta.set(0)
        self.cookingoil.set(0)
        #-----------colddrink----------------
        self.cocacola.set(0)
        self.sprite.set(0)
        self.mazza.set(0)
        self.fanta.set(0)
        self.pepsi.set(0)
        self.fizz.set(0)
        #-----total product price& tax variable------
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.colddrink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.colddrink_tax.set("")
        #----------customer-------------
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def exit_app(self):
      op=messagebox.askyesno("Exit","Do you really want to exit?") 
      if op>0:
        self.root.destroy()   





root=Tk()
obj= Bill_app(root)
root.mainloop()



