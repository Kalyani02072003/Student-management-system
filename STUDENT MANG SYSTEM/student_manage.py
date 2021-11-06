from tkinter import*

from tkinter import ttk

import pymysql
from tkinter import messagebox

from PIL import Image,ImageTk 

class student:


     def __init__(self,root):
        self.root=root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="gray1")

        self.bg=ImageTk.PhotoImage(file="STUDENT MANG SYSTEM/ASSETS/space1.jpg")        #self by default is a object
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
         
        title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("bradley hand itc",40,"bold"),bd=10,relief=GROOVE,bg="gray1",fg="turquoise1")
        title.pack(side=TOP,fill=X)



        #==========ALL VARIABLES-==========================
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        


        
#==============MANGEMENT FRAME==========================================================================
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="light sky blue")
        Manage_frame.place(x=20,y=90,width=500,height=590)

        
        
        m_title=Label(Manage_frame,text="MANAGE STUDENTS",font=("forte",28,"bold"),fg="navy",bg="light sky blue")
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll=Label(Manage_frame,text="ROLL NO",font=("bradley hand itc",20,"bold"),fg="navy",bg="light sky blue")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_frame,textvariable=self.Roll_No_var,font=("bradley hand itc",15,"bold"),bd=0,relief=GROOVE,fg="navy",bg="white")
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_frame,text="NAME",font=("bradley hand itc",20,"bold"),fg="navy",bg="light sky blue")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_name=Entry(Manage_frame,textvariable=self.name_var,font=("bradley hand itc",15,"bold"),fg="navy",bg="white")
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_frame,text="EMAIL",font=("bradley hand itc",20,"bold"),fg="navy",bg="light sky blue")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_frame,textvariable=self.email_var,font=("bradley hand itc",15,"bold"),bd=0,relief=GROOVE,fg="navy",bg="white")
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_frame,text="GENDER",font=("bradley hand itc",20,"bold"),fg="navy",bg="light sky blue")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        cmb_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("bradley hand itc",14,"bold"),state="readonly")
        cmb_gender["values"]=("Male","Female","Others")
        cmb_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact=Label(Manage_frame,text="CONTACT",font=("bradley hand itc",20,"bold"),fg="navy",bg="light sky blue")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_frame,font=("bradley hand itc",15,"bold"),textvariable=self.contact_var,fg="navy",bg="white")
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(Manage_frame,text="DOB",font=("bradley hand itc",20,"bold"),fg="navy",bg="light sky blue")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_frame,textvariable=self.dob_var,font=("bradley hand itc",15,"bold"),fg="navy",bg="white")
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(Manage_frame,text="ADDRESS",font=("bradley hand itc",20,"bold"),fg="navy",bg="light sky blue")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_frame,width=20,height=3,font=("",15))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

#====================button frame========================================================================

        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="light sky blue")
        btn_frame.place(x=10,y=530,width=410,height=50)

        add_btn=Button(btn_frame,command=self.add_students,text="ADD",width=10).grid(row=0,column=0,padx=10,pady=10)
        update_btn=Button(btn_frame,command=self.update_data,text="UPDATE",width=10).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(btn_frame,command=self.delete_data,text="DELETE",width=10).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(btn_frame,command=self.clear,text="CLEAR",width=10).grid(row=0,column=3,padx=10,pady=10)


#===============DETAILS FRAME===========================================================================

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="light sky blue")
        detail_frame.place(x=550,y=90,width=770,height=590)


        lbl_search=Label(detail_frame,text="Search By",font=("bradley hand itc",20,"bold"),fg="navy")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        cmb_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("bradley hand itc",14,"bold"),state="readonly")
        cmb_search["values"]=("Roll_no","Name","Contact",)
        cmb_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(detail_frame,textvariable=self.search_txt,font=("bradley hand itc",15,"bold"),width=15,fg="navy")
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_btn=Button(detail_frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showall_btn=Button(detail_frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#===================TABLE FRAME====================================================================

        table_frame=Frame(detail_frame,bd=2,relief=RIDGE,bg="sky blue")
        table_frame.place(x=10,y=70,width=740,height=500)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","dob","contact","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("dob",text="DOB")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("address",width=150)
        self.student_table.column("dob",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

     def add_students(self):
             if self.Roll_No_var.get()=="" or self.name_var.get()=="" :
                     messagebox.showerror("ERROR","ALL FEILDS ARE REQUIRED!!")
             else:                    
                     con=pymysql.connect(host="localhost",user="root",password="",database="stn")
                     cur=con.cursor()
                     cur.execute("INSERT INTO students1 VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.dob_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.txt_address.get("1.0",END)
                                                                                ))
                        
                     con.commit()
                     self.fetch_data()
                     self.clear()
                     con.close()
                     messagebox.showinfo("SUCCESS","RECORD INSERTED")
                  

     def fetch_data(self):

             con=pymysql.connect(host="localhost",user="root",password="",database="stn")
             cur=con.cursor()
             cur.execute("SELECT * FROM students1")

             rows=cur.fetchall()
             if len(rows)!=0:
                     self.student_table.delete(*self.student_table.get_children())
                     for row in rows:
                             self.student_table.insert('',END,values=row)
                     con.commit()
             con.close()


     def clear(self):
             self.Roll_No_var.set("")
             self.name_var.set("")
             self.email_var.set("")
             self.gender_var.set("")
             self.contact_var.set("")
             self.dob_var.set("")
             self.txt_address.delete("1.0",END)

     def get_cursor(self,ev):
             cursor_row=self.student_table.focus()
             contents=self.student_table.item(cursor_row)
             row=contents["values"]
             
             self.Roll_No_var.set(row[0])
             self.name_var.set(row[1])
             self.email_var.set(row[2])
             self.gender_var.set(row[3])
             self.contact_var.set(row[4])
             self.dob_var.set(row[5])
             self.txt_address.delete("1.0",END)
             self.txt_address.insert(END,row[6])
             
     def update_data(self):
             con=pymysql.connect(host="localhost",user="root",password="",database="stn")
             cur=con.cursor()
             cur.execute("UPDATE students1 SET name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s WHERE roll_no=%s",(
                                                                                                      self.name_var.get(),
                                                                                                      self.email_var.get(),
                                                                                                      self.gender_var.get(),
                                                                                                      self.contact_var.get(),
                                                                                                      self.dob_var.get(),
                                                                                                      self.txt_address.get("1.0",END),
                                                                                                      self.Roll_No_var.get()
                                                                                                      ))
                
             con.commit()
             self.fetch_data()
             self.clear()
             con.close()
             messagebox.showinfo("UPDATE","Record Updated")


     
     def delete_data(self):
             

             con=pymysql.connect(host="localhost",user="root",password="",database="stn")
             cur=con.cursor()
             cur.execute("DELETE FROM students1 WHERE roll_no=%s",self.Roll_No_var.get())
             con.commit()
             con.close()
             self.fetch_data()
             con.clear()
             messagebox.showinfo("DELETION COMPLETED","Deleted Selected Data")
            
     def search_data(self):

             con=pymysql.connect(host="localhost",user="root",password="",database="stn")
             cur=con.cursor()

             cur.execute("SELECT * FROM students1 WHERE" + str(self.search_by.get())+ " LIKE%'" + str(self.search_txt.get())+"%'")
             rows=cur.fetchall()
             if len(rows)!=0:
                     self.student_table.delete(*self.student_table.get_children())
                     for row in rows:
                             self.student_table.insert('',END,values=row)
                     con.commit()
             con.close()

root=Tk()
obj=student(root)
root.mainloop()
