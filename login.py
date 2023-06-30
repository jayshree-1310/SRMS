from tkinter import *
from tkinter import messagebox,ttk
import sqlite3
import os

class Login_System:
    def __init__(self, root):
        self.root=root
        self.root.title("STUDENT RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#151e3d")
        
        login_frame=Frame(self.root, bd=2,relief=RIDGE, bg="white")
        login_frame.place(x=450, y=80,width=400,height=440)
        
        title=Label(login_frame, text="Login System", font=("merriweather", 30, "bold")).place(x=0, y=20, relwidth=1)
        
        email=Label(login_frame,text="Email Id", font=("Andalus",15),bg="white",fg="#373737").place(x=28,y=90) 
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="#ececec")
        self.txt_email.place(x=30,y=130,width=350,height=40)

        pass_=Label(login_frame,text="Password", font=("Andalus",15),bg="white",fg="#373737").place(x=28,y=190) 
        self.txt_pass_=Entry(login_frame,show="*",font=("times new roman",15),bg="#ececec")
        self.txt_pass_.place(x=30,y=230,width=350,height=40)
        
        btn_login=Button(login_frame,command=self.login,text="LOGIN",font=("Arial Rounded MT Bold",15),bg="#00b0f0",activebackground="#00b0f0",fg="#000",cursor="hand2").place(x=30,y=295,width=350,height=40)
        
        hr=Label(login_frame,bg="lightgray").place(x=30,y=370,width=150,height=2)
        txt_line=Label(login_frame,text="OR", font=("Andalus",15,"bold"),bg="white",fg="lightgray").place(x=185,y=360)
        hr=Label(login_frame,bg="lightgray").place(x=230,y=370,width=150,height=2)

        btn_forget=Button(login_frame,command=self.forget_password_window,text="FORGET PASSWORD",font=("Arial Rounded MT Bold",13),bg="white",fg="#00759E",bd=0,activebackground="white",cursor="hand2").place(x=105,y=390)      

        register_frame=Frame(self.root, bd=2,relief=RIDGE, bg="white")
        register_frame.place(x=450, y=530,width=400,height=50)
        btn_register=Button(register_frame,command=self.register_window,text="SIGN UP",font=("Arial Rounded MT Bold",13),bg="white",fg="#00759E",bd=0,activebackground="white",cursor="hand2").place(x=155, y=10)
        

    def reset(self):
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_ques.get()=="Select" or self.txt_ans.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_ques.get(),self.txt_new_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Security question or answer selected",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_password.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password updated successfully",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter mail Id to reset password",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Enter valid Email to reset password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("400x500+350+100")
                    self.root2.focus_force() #projects focus to to the working window
                    self.root2.grab_set() #Does not close unless user close it

                    t=Label(self.root2,text="Forget Password",font=("Andalus",30),fg="red").place(x=0,y=10,relwidth=1)
                    
                    ques=Label(self.root2,text="Security question",font=("merriweather", 15),fg="black").place(x=50,y=100)
                    self.cmb_ques=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify="center")
                    self.cmb_ques['values']=("Select","Your first pet","Your first school","Your Mother's maiden name","Your favourite song","Your best friend")
                    self.cmb_ques.place(x=50,y=140,width=290,height=30)
                    self.cmb_ques.current(0)
                    
                    ans=Label(self.root2,text="Security Answer",font=("merriweather", 15),fg="black").place(x=50,y=200)
                    self.txt_ans=Entry(self.root2,font=("times new roman",15),bg="#c5c6c7")
                    self.txt_ans.place(x=50,y=240,width=290,height=30)

                    new_password=Label(self.root2,text="New Password",font=("merriweather", 15),fg="black").place(x=50,y=300)
                    self.txt_new_password=Entry(self.root2,font=("times new roman",15),bg="#c5c6c7")
                    self.txt_new_password.place(x=50,y=330,width=290,height=30)

                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,font=("Arial Rounded MT",15),bg="#151e3d",fg="white").place(x=125,y=390)
            
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root) 

    def register_window(self):
        self.root.destroy()
        os.system("python register.py")

    def dashboard_window(self):
        self.root.destroy()
        os.system("python dashboard.py")


    def login(self):
        if self.txt_email.get()=="" and self.txt_pass_.get()=="":
            messagebox.showerror("Error","Email Id and password is required",parent=self.root)
        elif self.txt_email.get()=="":
            messagebox.showerror("Error","Email Id is required",parent=self.root)
        elif self.txt_pass_.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email Id or password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Login Successful",parent=self.root)
                    self.reset()
                    self.dashboard_window()
                    # self.root.destroy()
                    # os.system("python dashboard.py")
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
            # messagebox.showinfo("Information",f"Welcome {self.username.get()}\n")
if __name__=="__main__":
    root=Tk()
    obj=Login_System(root)
    root.mainloop()