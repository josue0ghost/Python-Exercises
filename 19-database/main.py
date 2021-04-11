import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""#,
    #database = "master_python"
)

"""
print(database) # correct connection?

cursor = database.cursor()

cursor.execute("CREATE DATABASE master_python")
"""

