import mysql.connector as MyConn
#  print("Driver started!")

mydb=MyConn.connect(host="localhost",username="root",password=" ")
print(mydb,"connection established")

# db_cursor=mydb.cursor()

# db_cursor.execute('create database nikkii')
# print("database created")

# db_cursor.execute('create table emp(Number int, Name varchar(30), Salary int)')
# print("table created!")

# db_cursor.execute('INSERT INTO emp VALUES (1, "Asmita", 100)')
# db_cursor.execute('INSERT INTO emp VALUES (2, "shreeya", 200)')
# db_cursor.execute('INSERT INTO emp VALUES (3, "Sarvesh", 300)')
# db_cursor.execute('INSERT INTO emp VALUES (4, "Aditiy", 400)')
# db_cursor.execute('INSERT INTO emp VALUES (5, "Aditiy", 500)')
# mydb.commit()
# print(db_cursor.rowcount,"Record inserted")

# db_cursor.execute("select * from nikkii.Emp")
# db_select=db_cursor.fetchall()
# print(db_select)

# db_Updatedata = "update Emp set Name=%s where Number=%s"
# db_value=("Akhil", 5)
# db_cursor.execute(db_Updatedata,db_value)
# mydb.commit()
# print("Updated!")

# db_deletedata= "delete from Emp where Number=%s"
# db_value=(2,)
# db_cursor.execute(db_deletedata,db_value)
# print("Deleted")
