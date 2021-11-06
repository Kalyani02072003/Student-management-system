#REGISTRATION FORM
from tkinter import*

from tkinter import ttk,messagebox                                  #ttk is imported for a combobox which will hold values to select from

from PIL import Image,ImageTk                    #image tk hepls in working with jpg files

import pymysql 
# install pymysql (total space 47kB) in command prompt below(i.e the terminal)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTRATION WINDOW")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="PaleTurquoise1")
        #=========BG IMAGE==============
    
        self.bg=ImageTk.PhotoImage(file="STUDENT MANG SYSTEM/ASSETS/ocean1.jpg")        #self by default is a object
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #=================================LEFT IMAGE====================================
        self.left=ImageTk.PhotoImage(file="STUDENT MANG SYSTEM/ASSETS/astonaut.png")    #self by default is a object
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        
        

        #====================REGISTER FRAME==============================================

        frame1=Frame(self.root,bg="white").place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=500,y=150)        
        # ---------FIRST NAME---------------
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=210)        
        self.text_fname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.text_fname.place(x=500,y=240,width=250)
        #-------------LAST NAME----------------
        f_lname=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=850,y=210)        
        self.text_lname=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.text_lname.place(x=850,y=240,width=250)

        #----------------------------ROW2-------------

        #-----------CONTACT------------------------
        cont=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=270)        
        self.text_cont=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.text_cont.place(x=500,y=300,width=250)

        #-------------EMAIL---------------
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=850,y=270)        
        self.text_email=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.text_email.place(x=850,y=300,width=250)

        
        #-----------ROW3-----------------
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=340)   

        self.cmb_ques=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_ques["values"]=("Select","Your First pet name","Birth Place","best friend")
        self.cmb_ques.place(x=500,y=370,width=250)
        self.cmb_ques.current(0)                 #here 0 is the index which will show the value of tuple at index 0 by default 
        

        #------------ANSWER FOR THE SECURITY QUESTION----------------
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=850,y=340)        
        self.text_ans=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.text_ans.place(x=850,y=370,width=250)

       #=================ROW3==========

        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=400)        
        self.text_password=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.text_password.place(x=500,y=430,width=250)

        #-------------CONFIRM PASSWORD---------------
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=850,y=400)        
        self.text_cpassword=Entry(frame1,font=("times new roman",15),bg="light gray")
        self.text_cpassword.place(x=850,y=430,width=250)

        #------------TERMS&CONDITONS------------------------- 
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=500,y=470)
        btn_register=Button(frame1,text="REGISTER NOW",bd=0,cursor="hand2",command=self.register_data,bg="pale turquoise").place(x=500,y=510,width=250)

        btn_login=Button(self.root,text="SIGN IN",command=self.register_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=510,width=180)
    
    def register_window(self):
        self.root.destroy()
        import login_02
    

    def clear(self):
        self.text_fname.delete(0,END)
        self.text_lname.delete(0,END)
        self.text_cont.delete(0,END)
        self.text_email.delete(0,END)
        self.cmb_ques.current(0)
        self.text_ans.delete(0,END)
        self.text_password.delete(0,END)
        self.text_cpassword.delete(0,END)


    def register_data(self):  
        if self.text_fname.get()=="" or self.text_cont.get()=="" or self.text_email.get()=="" or self.cmb_ques.get()=="Select" or self.text_ans.get()=="" or self.text_password.get()=="" or self.text_cpassword.get()=="":
            messagebox.showerror("ERROR","All feilds are required",parent=self.root)
        elif self.text_password.get()!=self.text_cpassword.get():
            messagebox.showerror("ERROR","PASSWORD AND CONFIRM PASSWORD MUST BE SAME",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("ERROR","Please agree our tems & conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="registration")
                cur=con.cursor()
                cur.execute("SELECT * FROM registration_form WHERE email=%s",self.text_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("ERROR","USER ALREADY EXISTS USE ANOTHER EMAIL",parent=self.root)
                else:
                    cur.execute("INSERT INTO registration_form (f_name,l_name,contact,email,question,answer,password) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                                  (self.text_fname.get(),
                                   self.text_lname.get(),
                                   self.text_cont.get(),            
                                   self.text_email.get(),
                                   self.cmb_ques.get(),
                                   self.text_ans.get(),
                                   self.text_password.get()
                                   ))

                    con.commit()
                    con.close()
                    messagebox.showinfo("SUCCESS","REGISTRATION SUCCESSFUL",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("ERROR",f"Error due to: {str(es)}",parent=self.root)




        
    
root=Tk()
obj=Register(root)
root.mainloop()