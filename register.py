from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from login import Login_System
import os
class Registration_System:
    def __init__(self, root):
        self.root=root
        self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        
        self.left=ImageTk.PhotoImage(file="pics/t.jpg")
        left=Label(self.root,image=self.left)
        left.place(x=0,y=35)
        self.img=ImageTk.PhotoImage(file="pics/art.png")
        img=Label(self.root,image=self.img)
        img.place(x=430,y=0)
        frame1=Frame(self.root,bg="#FFF")
        frame1.place(x=480,y=80,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("merriweather", 18, "bold"),bg="white",fg="#151e3d").place(x=30,y=25)

        fname=Label(frame1,text="First Name",font=("merriweather", 15),bg="white",fg="black").place(x=30,y=80)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="#ececec")
        self.txt_fname.place(x=30,y=110,width=230,height=30)
        
        lname=Label(frame1,text="Last Name",font=("merriweather", 15),bg="white",fg="black").place(x=400,y=80)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="#ececec")
        self.txt_lname.place(x=400,y=110,width=230,height=30)

        contact=Label(frame1,text="Contact Number",font=("merriweather", 15),bg="white",fg="black").place(x=30,y=150)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="#ececec")
        self.txt_contact.place(x=30,y=190,width=230,height=30)
        email=Label(frame1,text="Email",font=("merriweather", 15),bg="white",fg="black").place(x=400,y=150)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="#ececec")
        self.txt_email.place(x=400,y=190,width=230,height=30)
        
        ques=Label(frame1,text="Security question",font=("merriweather", 15),bg="white",fg="black").place(x=30,y=230)
        self.cmb_ques=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify="center")
        self.cmb_ques['values']=("Select","Your first pet","Your first school","Your Mother's mainden name","Your favourite song","Your best friend")
        self.cmb_ques.place(x=30,y=270,width=230,height=30)
        self.cmb_ques.current(0)
        
        ans=Label(frame1,text="Security Answer",font=("merriweather", 15),bg="white",fg="black").place(x=400,y=230)
        self.txt_ans=Entry(frame1,font=("times new roman",15),bg="#ececec")
        self.txt_ans.place(x=400,y=270,width=230,height=30)
        
        password=Label(frame1,text="Password",font=("merriweather", 15),bg="white",fg="black").place(x=30,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="#ececec")
        self.txt_password.place(x=30,y=350,width=230,height=30)
        
        cnfrmpass=Label(frame1,text="Confirm Password",font=("merriweather", 15),bg="white",fg="black").place(x=400,y=310)
        self.txt_cnfrmpass=Entry(frame1,font=("times new roman",15),bg="#ececec")
        self.txt_cnfrmpass.place(x=400,y=350,width=230,height=30)

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I accept Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("Arial Rounded MT Bold",10),bg="#fff").place(x=30,y=390)

        btn_login=Button(frame1,text="Sign In",command=self.login_window,font=("Arial Rounded MT Bold",10),bg="#fff",fg="#000",cursor="hand2").place(x=30,y=470)
        btn_register=Button(frame1,text="REGISTER",font=("Arial Rounded MT Bold",15),bg="#151e3d",fg="#fff",cursor="hand2",command=self.register_data).place(x=30,y=420,width=230,height=40)

    def login_window(self):
          self.root.destroy()
          os.system("python login.py")

    def clear(self):
          self.txt_fname.delete(0,END)
          self.txt_lname.delete(0,END)
          self.txt_contact.delete(0,END)
          self.txt_email.delete(0,END)
          self.cmb_ques.current(0)
          self.txt_ans.delete(0,END)
          self.txt_password.delete(0,END)
          self.txt_cnfrmpass.delete(0,END)
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_ques.get()=="Select" or self.txt_ans.get()=="" or self.txt_password.get()=="" or self.txt_cnfrmpass.get()=="":
            #   self.txt_lname.get()
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cnfrmpass.get():
            messagebox.showerror("Error","Password and confirm password do not match",parent=self.root)
        elif self.var_chk==0:
            messagebox.showerror("Error","Agree to the terms and conditions",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Email Id already registered",parent=self.root())
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",(
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmb_ques.get(),
                        self.txt_ans.get(),
                        self.txt_password.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
                
if __name__=="__main__":
    root=Tk()
    obj=Registration_System(root)
    root.mainloop()