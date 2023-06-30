from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#fff")
        self.root.focus_force() #puts focus on current window

        self.var_id=""
        self.var_search=StringVar()
        title = Label(self.root ,text="STUDENTS RESULT",font=("merriweather",20,"bold"),bg = '#033054' ,fg="#fff").place(relx=0.5,y=30, width=50000, height= 50, anchor=CENTER)
        lbl_search=Label(self.root,text="SEARCH BY ROLL NUMBER",font=("merriweather",18),bg="white").place(x=300,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("merriweather",18),bg="lightyellow").place(x=630,y=100,width=150)
        btn_search=Button(self.root,text="Search",font=("merriweather",15),bg="#03a9f4",fg="#fff",cursor="hand2",command=self.search).place(x=790,y=100,width=120,height=30)
        btn_clear=Button(self.root,text="Clear",font=("merriweather",15),bg="gray",fg="#fff",cursor="hand2",command=self.clear).place(x=920,y=100,width=120,height=30)
        
        #==labels==#
        lbl_roll=Label(self.root,text="ROLL NO",font=("merriweather",15),bg="white",bd=2,relief=GROOVE).place(x=170,y=200,width=120,height=50)# bd is border and groove is its style
        lbl_name=Label(self.root,text="NAME",font=("merriweather",15),bg="white",bd=2,relief=GROOVE).place(x=290,y=200,width=120,height=50)
        lbl_course=Label(self.root,text="COURSE",font=("merriweather",15),bg="white",bd=2,relief=GROOVE).place(x=410,y=200,width=120,height=50)
        lbl_marks_obt=Label(self.root,text="MARKS OBTAINED",font=("merriweather",15),bg="white",bd=2,relief=GROOVE).place(x=530,y=200,width=220,height=50)
        lbl_full_marks=Label(self.root,text="FULL MARKS",font=("merriweather",15),bg="white",bd=2,relief=GROOVE).place(x=750,y=200,width=150,height=50)
        lbl_per=Label(self.root,text="PERCENTAGE",font=("merriweather",15),bg="white",bd=2,relief=GROOVE).place(x=900,y=200,width=150,height=50)
        
        self.roll=Label(self.root,font=("merriweather",15),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=170,y=250,width=120,height=50)# bd is border and groove is its style
        self.name=Label(self.root,font=("merriweather",15),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=290,y=250,width=120,height=50)
        self.course=Label(self.root,font=("merriweather",15),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=410,y=250,width=120,height=50)
        self.marks_obt=Label(self.root,font=("merriweather",15),bg="white",bd=2,relief=GROOVE)
        self.marks_obt.place(x=530,y=250,width=220,height=50)
        self.full_marks=Label(self.root,font=("merriweather",15),bg="white",bd=2,relief=GROOVE)
        self.full_marks.place(x=750,y=250,width=150,height=50)
        self.per=Label(self.root,font=("merriweather",15),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=250,width=150,height=50)
            
        btn_delete=Button(self.root,text="Delete",font=("merriweather",20),bg="#800000",fg="#fff",cursor="hand2",command=self.delete).place(x=550,y=350,width=150,height=50)
        

        #====function==#
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Please enter a roll number")
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks_obt.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.per.config(text=row[6])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_obt.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_search.set("")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search student result first",parent=self.root)
            else:
                cur.execute("select * from result where Rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really wish to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where Rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()
        