import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="garshasp",
  password="2411"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)