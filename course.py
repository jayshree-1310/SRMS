from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#fff")
        self.root.focus_force()
        #==title==#
        title = Label(self.root ,text="MANAGE COURSE DETAILS",font=("merriweather",20),bg = '#033054' ,fg="#fff").place(relx=0.5,y=30, width=50000, height= 30, anchor=CENTER)
        #==Variables==#
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        #==Widgets==#
        lbl_courseName=Label(self.root,text="COURSE NAME",font=("merriweather",15),bg="white").place(x=10,y=70)
        lbl_DURATION=Label(self.root,text="DURATION",font=("merriweather",15),bg="white").place(x=10,y=110)
        lbl_CHARGES=Label(self.root,text="CHARGES",font=("merriweather",15),bg="white").place(x=10,y=150)
        lbl_DESCRIPTION=Label(self.root,text="DESCRIPTION",font=("merriweather",15),bg="white").place(x=10,y=190)

        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("merriweather",15),bg="lightblue")
        self.txt_courseName.place(x=180,y=70,width=200)
        txt_DURATION=Entry(self.root,textvariable=self.var_duration,font=("merriweather",15),bg="lightblue").place(x=180,y=110,width=200)
        txt_CHARGES=Entry(self.root,textvariable=self.var_charges,font=("merriweather",15),bg="lightblue").place(x=180,y=150,width=200)
        self.txt_DESCRIPTION=Text(self.root,font=("merriweather",15),bg="lightblue")
        self.txt_DESCRIPTION.place(x=180,y=190,width=500,height=150)

        #==button==#
        self.btn_add=Button(self.root,text="SAVE",font=("merriweather",15),bg="#2196f3",fg="#fff",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=410,width=110,height=40)
        self.btn_update=Button(self.root,text="UPDATE",font=("merriweather",15),bg="#4caf50",fg="#fff",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=410,width=110,height=40)
        self.btn_delete=Button(self.root,text="DELETE",font=("merriweather",15),bg="#f44336",fg="#fff",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=410,width=110,height=40)
        self.btn_clear=Button(self.root,text="CLEAR",font=("merriweather",15),bg="#607d8b",fg="#fff",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=410,width=110,height=40)

        #==searchpanel==#
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("merriweather",15),bg="white").place(x=720,y=70)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("merriweather",15),bg="lightblue").place(x=860,y=70,width=180)
        btn_search=Button(self.root,text="Search",font=("merriweather",15),bg="#03a9f4",fg="#fff",cursor="hand2",command=self.search).place(x=1050,y=70,width=120,height=28)
        #==content==#
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=110,width=500,height=340)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("Cid","Name","Duration","Charges","Description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("Cid",text="Course Id")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("Duration",text="Duration")
        self.CourseTable.heading("Charges",text="Charges")
        self.CourseTable.heading("Description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("Cid",width=80)
        self.CourseTable.column("Name",width=80)
        self.CourseTable.column("Duration",width=80)
        self.CourseTable.column("Charges",width=80)
        self.CourseTable.column("Description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    #===============================================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_DESCRIPTION.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be added",parent=self.root)
            else:
                cur.execute("select * from course where Name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select course from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really wish to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where Name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_DESCRIPTION.delete('1.0',END)
        self.txt_DESCRIPTION.insert(END,row[4])

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be added",parent=self.root)
            else:
                cur.execute("select * from course where Name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already exist",parent=self.root)
                else:
                    cur.execute("insert into course(Name,Duration,Charges,Description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_DESCRIPTION.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course added successfully",parent=self.root) 
                    self.show()                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be added",parent=self.root)
            else:
                cur.execute("select * from course where Name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course from list",parent=self.root)
                else:
                    cur.execute("update course set Duration=?,Charges=?,Description=? where Name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_DESCRIPTION.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course updated successfully",parent=self.root)   
                    self.show()              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    
    
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute(f"select * from course where Name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()