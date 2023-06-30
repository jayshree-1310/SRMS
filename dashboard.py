from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from login import Login_System
import sqlite3
import os
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fff")
        
        #==icon==#
        self.logo_dash=ImageTk.PhotoImage(file="pics/graduated.jpg")
        
        #==title==#
        title=Label(self.root,text="STUDENT RESULT MANAGMENT SYSTEM",padx=10,compound=LEFT,image=self.logo_dash, font=("merriweather",20,"bold"),bg="#033054",fg="#fff").place(x=0,y=0,relwidth=1,height=50)
        
        #==menu==#
        M_Frame=LabelFrame(self.root,text="MENU",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=60,width=1260,height=80)
        btn_course=Button(M_Frame,text="Course",font=("merriweather",15,"bold"),bg="#033054",fg="#fff",cursor="hand2",command=self.add_course).place(x=20,y=4,width=185,height=40)
        btn_student=Button(M_Frame,text="Student",font=("merriweather",15,"bold"),bg="#033054",fg="#fff",cursor="hand2",command=self.add_student).place(x=225,y=4,width=185,height=40)
        btn_result=Button(M_Frame,text="Result",font=("merriweather",15,"bold"),bg="#033054",fg="#fff",cursor="hand2",command=self.add_result).place(x=430,y=4,width=185,height=40)
        btn_viewresult=Button(M_Frame,text="View Result",font=("merriweather",15,"bold"),bg="#033054",fg="#fff",cursor="hand2",command=self.view_result).place(x=635,y=4,width=185,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("merriweather",15,"bold"),bg="#033054",fg="#fff",cursor="hand2",command=self.logout).place(x=840,y=4,width=185,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("merriweather",15,"bold"),bg="#033054",fg="#fff",cursor="hand2",command=self.exit_).place(x=1045,y=4,width=185,height=40)
        
        #==content==#
        self.bg_img=Image.open("pics/success.jpg")
        self.bg_img=self.bg_img.resize((750,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=200,y=150,width=900,height=350)
        
        #==update_label==#
        self.lbl_course=Label(self.root,text="TOTAL COURSES\n[0]",font=("merriweather",20),bd=10,relief=RIDGE,bg="#033054",fg="white")
        self.lbl_course.place(x=200,y=510,width=280,height=85)
        
        self.lbl_student=Label(self.root,text="TOTAL STUDENT\n[0]",font=("merriweather",20),bd=10,relief=RIDGE,bg="#033054",fg="white")
        self.lbl_student.place(x=500,y=510,width=280,height=85)
        
        self.lbl_result=Label(self.root,text="TOTAL RESULT\n[0]",font=("merriweather",20),bd=10,relief=RIDGE,bg="#033054",fg="white")
        self.lbl_result.place(x=800,y=510,width=280,height=85)
        
        #==footer==#
        footer=Label(self.root,text="STUDENT RESULT MANAGMENT SYSTEM\nContact us at:9876543210",font=("merriweather",15),bg="#262626",fg="#fff").pack(side=BOTTOM,fill=X)
        #self.update_details()
    

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:  
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"TOTAL COURSES\n[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_details)

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"TOTAL STUDENT\n[{str(len(cr))}]")
            self.lbl_student.after(200,self.update_details)

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"TOTAL RESULT\n[{str(len(cr))}]")
            self.lbl_result.after(200,self.update_details)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def add_course  (self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=CourseClass(self.new_win)

    def add_student  (self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=StudentClass(self.new_win)

    def add_result  (self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=resultClass(self.new_win)

    def view_result  (self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do yo really want to logout?",parent=self.root)
        if op==True:
          self.root.destroy()
          os.system("Python login.py") 

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do yo really want to exit?",parent=self.root)
        if op==True:
            # exit()
            self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
