import mysql.connector
import os
dataBase = mysql.connector.connect(
    host= os.environ.get('DJANGO_HOST','db'),
    user= os.environ.get('DJANGO_USER=','root'),
    passwd= os.environ.get('DJANGO_PASSWORD','123456')
)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE elderco')

print("All done!")