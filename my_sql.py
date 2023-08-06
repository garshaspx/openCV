import sqlite3
 
 
# create connection by using object
# to connect with hotel_data database
connection = sqlite3.connect('hotel_data.db')
 
# query to create a table named FOOD1
try:
    connection.execute(''' CREATE TABLE hotel
            (FIND INT PRIMARY KEY     NOT NULL,
            FNAME           TEXT    NOT NULL,
            COST            INT     NOT NULL,
            WEIGHT        INT);
            ''')
except:
    pass
# insert query to insert food  details in
# the above table
connection.execute("INSERT INTO hotel VALUES (13, 'casdkes',800,10 )")
connection.execute("INSERT INTO hotel VALUES (22, 'biscaasduits',100,20 )")
connection.execute("INSERT INTO hotel VALUES (43, 'chocasdos',1000,30 )")
connection.commit()

print("All data in food table\n")
 
# create a cousor object for select query
cursor = connection.execute("SELECT * from hotel ")
 
# display all data from hotel table
for row in cursor:
    print(row)