import mysql.connector as myc
mycon = myc.connect (host = "localhost", user = "root", passwd = "Anubhav@2007", database = "nasa")
if mycon.is_connected() == False:
    print("Error connecting!!")
else:
    cur = mycon.cursor()
    cur.execute("create table student(sapid int primary key, name varchar(20), age int)")
    mycon.commit()
mycon.close()
