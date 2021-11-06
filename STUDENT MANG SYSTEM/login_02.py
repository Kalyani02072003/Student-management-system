#==============LOGIN & REGISTER & RESET PASSWORD============================================
from tkinter import*
#==================INSTALL PYTHON PIP=======================================================
from PIL import Image, ImageTk
#=============IMPORTING WIDJET MESSAGE BOX==================================================
from tkinter import ttk,messagebox
#=============IMPORT SQL CONNECTION=========================================================
import pymysql 
# A class is like an object constuctor or a blueprint for creating objects
#OR A class is a blueprint that defines the variables and the methods to all objects of a certain kind
class Login(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root

        root.title("GUI LOGIN FORM")
        root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #=======BG IMAGE========================================================
        self.bg=ImageTk.PhotoImage(file="STUDENT MANG SYSTEM/ASSETS/trees.jpg")     #CAN ALSO TREES.JPG
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #=========LOGIN FRAME====================================================

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        #============LABELS FOR USERNAME AND INPUT================================

        title=Label(Frame_login,text="login here",font=("Impact",35,"bold"),fg="lime green",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Accountant Employee LOGIN AREA",font=("Goudy old style",15,"bold"),fg="chartreuse2",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Email Address",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_email=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        reg=Button(Frame_login,text="Register New Account?",command=self.register_window,cursor="hand2",bg="white",fg="lime green",bd=0,font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="white",bg="lime green",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)
        forget_pass=Button(Frame_login,text="Forget Password",command=self.forget_password,cursor="hand2",bg="white",fg="lime green",bd=0,font=("times new roman",12)).place(x=300,y=280)

        #=============FUNCTION FOR GIVING COMMANDS TO BUTTON AND LABEL=====================================
    def register_window(self):
        self.root.destroy()
        import register
          
        #=================WINDOW FOR RESET PASSWORD & CHANGING IT==========================================

    def forget_pass_window(self):
        if self.cmb_ques.get()=="select" or self.text_ans.get()=="" or self.new_password.get()=="":
            messagebox.showerror("Error","All FEILDS ARE REQUIRED!!",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="registration")
                cur=con.cursor()
                #=====================TAKES VALID EMAIL AS AN INPUT========================================
                cur.execute("SELECT * FROM registration_form WHERE email=%s and question=%s and answer=%s ",(self.txt_email.get(),self.cmb_ques.get(),self.text_ans.get()))
                row=cur.fetchone()
                if row==None:
                    #========WILL SHOW ERROR IF ENTRIES ARE INCOORECTLY FILLED=============================
                    messagebox.showerror("ERROR","Please enter a select correct security question/answer",parent=self.root)
                else:
                    #==============UPDATES PASSWORD IF THE ANSWER TO SECURITY QUESTION IS CORRECT===========
                    cur.execute("UPDATE registration_form SET password=%s WHERE email=%s",(self.new_password.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("SUCCESS","PASSWORD RESET SUCCESSFULLY",parent=self.root2)
            except Exception as es:
                messagebox.showerror("ERROR",f"ERROR DUE TO: {str(es)}",parent=self.root)

        #=============FUNCTIOM FOR OPENING A NEW WINDOW FOR FORGET PASSWORD=================================

    def forget_password(self):
        #=============WILL ALLOW USER TO CHANGE PASSWORD ONLY IF EMAIL ENTRY FEILD ID FILLED=================
        #=================IF INCOORECT EMAIL IS ENTERED THEN WILL SHOW ERROR=================================
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email to reset password",parent=self.root)
        else:
            try:

                con=pymysql.connect(host="localhost",user="root",password="",database="registration")
                cur=con.cursor()
                cur.execute("SELECT * FROM registration_form WHERE email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Please enter a valid email address to reset",parent=self.root)
                    
                else:
                    con.close()
                    #self.root=Tk()  #To make new window
                    self.root2=Toplevel()  #Also makes another window on the top of previois window
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+550+150")
                    self.root2.config(bg="green")
                    self.root2.focus_force()  #FOCUSES THE THIS WINDOW
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=5,relwidth=1)

                    #-----------FORGET PASSWORD QUESTION FEILD-----------------
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=55,y=60)   

                    self.cmb_ques=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
                    self.cmb_ques["values"]=("Select","Your First pet name","Birth Place","best friend")
                    self.cmb_ques.place(x=55,y=100,width=160)
                    self.cmb_ques.current(0)                 #here 0 is the index which will show the value of tuple at index 0 by default 
        

                    #------------ANSWER FOR THE SECURITY QUESTION----------------
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=55,y=145)        
                    self.text_ans=Entry(self.root2,font=("times new roman",15),bg="light gray")
                    self.text_ans.place(x=55,y=190,width=160)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="green",fg="gray").place(x=55,y=230)        
                    self.new_password=Entry(self.root2,font=("times new roman",15),bg="light gray")
                    self.new_password.place(x=55,y=280,width=160)

                    btn_chnage_pass=Button(self.root2,text="Reset Password",command=self.forget_pass_window,bg="light green",font=("times new roman",15,"bold")).place(x=55,y=330)
                

            except Exception as es:
                messagebox.showerror("ERROR",f"ERROR DUE TO: {str(es)}",parent=self.root)

    # ================LOGIN CONNECTION WITH SQL======================================================================

    def login_function(self):

        if self.txt_pass.get()=="" or self.txt_email.get()=="":
            messagebox.showerror("ERROR","ALL FEILDS ARE REQUIRED",parent=self.root)
        else:
            try:

                con=pymysql.connect(host="localhost",user="root",password="",database="registration")
                cur=con.cursor()
                cur.execute("SELECT * FROM registration_form WHERE email=%s AND password=%s",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid email/password",parent=self.root)
                    

                else:
                    messagebox.showinfo("SUCCESS","WELCOME",parent=self.root)
                    self.root.destroy()
                    import student_manage
                    
                con.close()

            except Exception as es:
                messagebox.showerror("ERROR",f"ERROR DUE TO: {str(es)}",parent=self.root)

root=Tk()
obj=Login(root)
root.mainloop()

    