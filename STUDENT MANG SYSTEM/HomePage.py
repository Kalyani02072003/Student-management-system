from tkinter import *

from PIL import Image, ImageTk

import pyttsx3

root = Tk()
root.title("HOME PAGE")
#root.geometry("300x500")
root.configure(background="black")
#root.resizable(0,0)   #USE THIS TO MAXIMIZE OR MINIMIZE THE TK WINDOW 
#root.eval('tk::PlaceWindow . center')  #THIS WILL PLACE THE WINDOW LITERALLY IN THE MIDDLE AND STARTS SHOWING IMAGE FROM THERE

#=======================CENTERING WINDOW=============================
def center_window(width=300, height=500):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


#=====================SPECIFY THE WINDOW SIZE==========
center_window(500, 650)


#================RESIZING IMAGE TO WINDOW SIZE==============
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("STUDENT MANG SYSTEM/ASSETS/baymax.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        f1=Frame(self.master,bg="firebrick3").place(x=20,y=50,width=150,height=100)
        msg1=Label(f1,text="Hi! Its Baymax here",font=("arial",13),fg="white",bg="firebrick3")
        msg1.place(x=20,y=50)
        msg2=Label(f1,text="Please Login ",font=("arial",13),fg="white",bg="firebrick3")
        msg2.place(x=20,y=80)
        msg5=Label(f1,text="Register If New",font=("arial",13),fg="white",bg="firebrick3")
        msg5.place(x=20,y=110)
        msg4=Label(f1,text="Get Access To Student Mng.sys",font=("arial",13),fg="white",bg="firebrick3")
        msg4.place(x=40,y=510)
        msg4=Label(f1,text="Click Below To Get Started",font=("arial",13),fg="white",bg="firebrick3")
        msg4.place(x=40,y=540)
        btn_start=Button(root,text="GET STARTED",command=self.getting_started,font=("times new roman",10),bd=3,cursor="hand2",bg="white").place(x=70,y=580,width=150,height=50)

    def getting_started(self):
        print("OK started the program")
#=====TEXT TO SPEECH METHOD===================================
        engine = pyttsx3.init()
        engine.say("OK started the program")
        engine.runAndWait()
        self.master.destroy()
        import login_02

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

e = Example(root)
e.pack(fill=BOTH, expand=YES)



root.mainloop()
