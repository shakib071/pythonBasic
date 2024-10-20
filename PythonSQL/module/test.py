import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sh@kib007"
)

print(mydb)