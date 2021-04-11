# Connect to DB
import sqlite3

# open connection
con = sqlite3.connect('tests.db')

# create cursor
cursor = con.cursor()
# create table
cursor.execute("CREATE TABLE IF NOT EXISTS products(" + 
"id INTEGER PRIMARY KEY AUTOINCREMENT," +
"title VARVHAR(200)," +
"description TEXT," +
"price INT(10)" +
")")

# save changes
con.commit()

# insert data
# cursor.execute("INSERT INTO products VALUES (null, 'First product', 'Description', 100)")
# con.commit()

# delete registers
cursor.execute("DELETE FROM products")
con.commit()

# insert multiple data
productsArray = [
    ("Laptop", "Nice laptop", 500),
    ("Phone", "Nice phone", 150),
    ("Tablet", "Nice tablet", 280)
]
cursor.executemany("INSERT INTO products VALUES (null, ?, ?, ?)", productsArray)
con.commit()

# read from table
cursor.execute("SELECT * FROM products")
products = cursor.fetchall() # fetchone() returns first object

for product in products:
    print("Title: ", product[1])
    print("Descrpition: ", product[2])
    print("Price: ", product[3])
    print("\n")

# close connection
con.close()