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
        INSERT INTO Student(Roll,Name)
        VALUES('101','SHAKIB')

"""
mycursor.execute(sqlquery)
mydbconnection.commit()#commit na korle database a update hbe na
print("Insert successfully")


