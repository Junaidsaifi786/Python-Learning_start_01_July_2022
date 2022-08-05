import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Junaid@0786',
                database = 'cetpa')

cursor = con.cursor()


name = input("Enter the name")
#age = int(input("Enter the age"))
#salary = float(input("Enter the salary"))
#query
#insert
query = "delete from details where name = '{}'".format(name) #srtring formatting
# execute the queries
cursor.execute(query)
#now close the connection
con.commit()
print("data deleted successfull")


