from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#fff")
        self.root.focus_force()
        #==title==#
        title = Label(self.root ,text="MANAGE STUDENT DETAILS",font=("merriweather",20),bg = '#033054' ,fg="#fff").place(relx=0.5,y=30, width=50000, height= 30, anchor=CENTER)
        #==Variables==#
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        

        #==Widgets==#
        #==COL1==#
        lbl_ROLLNO=Label(self.root,text="ROLL NO",font=("merriweather",15),bg="white").place(x=10,y=70)
        lbl_NAME=Label(self.root,text="NAME",font=("merriweather",15),bg="white").place(x=10,y=110)
        lbl_EMAIL=Label(self.root,text="EMAIL",font=("merriweather",15),bg="white").place(x=10,y=150)
        lbl_GENDER=Label(self.root,text="GENDER",font=("merriweather",15),bg="white").place(x=10,y=190)
        lbl_STATE=Label(self.root,text="STATE",font=("merriweather",15),bg="white").place(x=10,y=230)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("merriweather",15),bg="lightblue").place(x=140,y=235,width=150)
        

        lbl_CITY=Label(self.root,text="CITY",font=("merriweather",15),bg="white").place(x=300,y=230)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("merriweather",15),bg="lightblue").place(x=380,y=235,width=150)
        lbl_pin=Label(self.root,text="PIN",font=("merriweather",15),bg="white").place(x=540,y=230)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("merriweather",15),bg="lightblue").place(x=600,y=235,width=100)
        
        
        lbl_ADDRESS=Label(self.root,text="ADDRESS",font=("merriweather",15),bg="white").place(x=10,y=270) 
        
        
        #==Entry_feilds1==#
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("merriweather",15),bg="lightblue")
        self.txt_roll.place(x=140,y=70,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("merriweather",15),bg="lightblue").place(x=140,y=110,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("merriweather",15),bg="lightblue").place(x=140,y=150,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Female","Male","Other"),font=("merriweather",15),state='readonly',justify=CENTER)
        self.txt_gender.place(x=140,y=190,width=200) 
        self.txt_gender.current(0)
        
        
        #==COL2==#
        lbl_DOB=Label(self.root,text="D.O.B",font=("merriweather",15),bg="white").place(x=360,y=70)
        lbl_CONTACT=Label(self.root,text="CONTACT",font=("merriweather",15),bg="white").place(x=360,y=110)
        lbl_ADDMISSION=Label(self.root,text="ADDMISSION",font=("merriweather",15),bg="white").place(x=360,y=150)
        lbl_COURSE=Label(self.root,text="COURSE",font=("merriweather",15),bg="white").place(x=360,y=190)
       
        
        #==Entry_feilds2==#
        self.course_list=[]
        #fuction call for list updation
        self.fetch_course()
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("merriweather",15),bg="lightblue").place(x=500,y=70,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("merriweather",15),bg="lightblue").place(x=500,y=110,width=200)
        txt_addmission=Entry(self.root,textvariable=self.var_a_date,font=("merriweather",15),bg="lightblue").place(x=500,y=150,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=(self.course_list),font=("merriweather",15),state='readonly',justify=CENTER)
        self.txt_course.place(x=500,y=190,width=200) 
        self.txt_course.set('Select')
        
        self.txt_address=Text(self.root,font=("merriweather",15),bg="lightblue")
        self.txt_address.place(x=140,y=280,width=560,height=100)

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
        lbl_search_roll=Label(self.root,text="ROLL NO.",font=("merriweather",15),bg="white").place(x=720,y=70)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("merriweather",15),bg="lightblue").place(x=860,y=70,width=180)
        btn_search=Button(self.root,text="Search",font=("merriweather",15),bg="#03a9f4",fg="#fff",cursor="hand2",command=self.search).place(x=1050,y=70,width=120,height=28)
        #==content==#
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=110,width=500,height=340)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","Name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("roll",text="Roll no")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")

        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=70)
        self.CourseTable.column("Name",width=100)
        self.CourseTable.column("email",width=150)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=200)
        
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    #===============================================
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(r""),
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Student should be added",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select student from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really wish to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])
    


    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll number should be added",parent=self.root)
            else:
                cur.execute("select * from course where Name=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll number already exist",parent=self.root)
                else:
                    cur.execute("insert into student(roll,Name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student added successfully",parent=self.root) 
                    self.show()                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll number should be added",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set Name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student updated successfully",parent=self.root)   
                    self.show()              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    
    
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("select Name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=NONE:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)  
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()