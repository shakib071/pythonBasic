import mysql.connector

mydbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sh@kib007"
)

print(mydbconnection)

db_name="python_test_db"

mycursor=mydbconnection.cursor()

sqlquery="CREATE DATABASE " + db_name#create database er por space dite hbe
mycursor.execute(sqlquery)
#eta korle mysql workbrench software a ekta databse create hye jabe

