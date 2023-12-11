import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123456'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE elderco')

print("All done!")