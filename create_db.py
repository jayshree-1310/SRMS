import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(Cid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Duration text,Charges text,Description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,Name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(Rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,Course text,marks text,fullmarks text,per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(Eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,question text,answer text,password text)")
    con.commit()

    con.close()
create_db() 