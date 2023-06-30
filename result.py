from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#fff")
        self.root.focus_force()
        title = Label(self.root ,text="ADD STUDENTS RESULT",font=("merriweather",20),bg = '#033054' ,fg="#fff").place(relx=0.5,y=30, width=50000, height= 50, anchor=CENTER)
        #==widgets==#
        #==labels==#
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_obmarks=StringVar()
        self.var_fullmarks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        lbl_select=Label(self.root,text="SELECT STUDENTS",font=("merriweather",20),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="NAME",font=("merriweather",20),bg="white").place(x=50,y=160)
        lbl_course=Label(self.root,text="COURSE",font=("merriweather",20),bg="white").place(x=50,y=220)
        lbl_marks_obt=Label(self.root,text="MARKS OBTAINED",font=("merriweather",20),bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="FULL MARKS",font=("merriweather",20),bg="white").place(x=50,y=340)

        
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=(self.roll_list),font=("merriweather",15),state='readonly',justify=CENTER)
        self.txt_student.place(x=400,y=105,width=200) 
        self.txt_student.set('Select')
        btn_search=Button(self.root,text="Search",font=("merriweather",15),bg="#03a9f4",fg="#fff",cursor="hand2",command=self.search).place(x=620,y=105,width=120,height=28)
        
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("merriweather",15),bg="lightblue",state="readonly").place(x=400,y=160,width=340,height=30)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("merriweather",15),bg="lightblue",state="readonly").place(x=400,y=220,width=340,height=30)
        txt_obtmarks=Entry(self.root,textvariable=self.var_obmarks,font=("merriweather",15),bg="lightblue").place(x=400,y=280,width=340,height=30)
        txt_fullmarks=Entry(self.root,textvariable=self.var_fullmarks,font=("merriweather",15),bg="lightblue").place(x=400,y=340,width=340,height=30)
        

        #==button==#
        btn_add=Button(self.root,text="SUBMIT",font=("merriweather",15,),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=450,y=420,width=110,height=40)
        btn_clear=Button(self.root,text="CLEAR",font=("merriweather",15,),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=570,y=420,width=110,height=40)
       
        self.bg_img=Image.open("pics/result.jpg")
        self.bg_img=self.bg_img.resize((450,400),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=800,y=100)
        
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select Name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Search for student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_roll.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already exist",parent=self.root)
                else:
                    per=(int(self.var_obmarks.get())*100)/int(self.var_fullmarks.get())
                    cur.execute("insert into result(roll,Name,course,marks,fullmarks,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),                        
                        self.var_course.get(),
                        self.var_obmarks.get(),
                        self.var_fullmarks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result added successfully",parent=self.root)                 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set(""),
        self.var_name.set(""),                        
        self.var_course.set("Select"),
        self.var_obmarks.set(""),
        self.var_fullmarks.set(""),
        
if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()