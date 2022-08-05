import mysql.connector as c
con = c.connect(host ='localhost',
                user ='root',
                passwd = 'Junaid@0786',
                database = 'school')
cursor = con.cursor()
name = input("Enter the name ")
age = int(input("age "))
marks = float(input("marks "))
#query
#insert
query = "insert into detail value ('{}',{},{})".format(name,age,marks)
cursor.execute(query)
con.commit()
print ("Data Entered Successfull!!")