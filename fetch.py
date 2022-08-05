import mysql.connector as c
con = c.connect(host ='localhost',
                user ='root',
                passwd = 'Junaid@0786',
                database = 'school')
cursor = con.cursor()
#name = input("Enter the name ")
#age = int(input("age "))
#marks = float(input("marks "))
#query
#insert
query = "select * from detail"
cursor.execute(query)
#x = cursor.fetchone()
#x = cursor.fetchall()
x = cursor.fetchmany()
print (x)