import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Prvn$766", database='guvi')

mycursor = mydb.cursor()

# How to List Down all the databases
# mycursor.execute("show databases")

# Iterate
# for x in mycursor:
#     print(x)

# How to fire query the database and create and insert into table
# mycursor.execute("Use GUVI")
# mycursor.execute("CREATE TABLE Customer (name VARCHAR(255),address VARCHAR(255))")

# How to get all the tables
# mycursor.execute("show tables")
#
# for x in mycursor:
#     print(x)

# How to fetch from the table
# mycursor.execute("Select * from guvi")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)