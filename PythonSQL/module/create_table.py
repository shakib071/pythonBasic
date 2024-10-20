import mysql.connector
db_name="python_test_db"
mydbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sh@kib007",
    database=db_name #database already created
)

# print(mydbconnection)

mycursor=mydbconnection.cursor()
#multiline query
sqlquery="""
        CREATE TABLE STUDENT
        (
         Roll varchar(4),
         Name varchar(50)
        )

"""
mycursor.execute(sqlquery)


