import mysql.connector

db=mysql.connector.connect(
     host="localhost",
     user="root",
     passwd=" ",
     database="testdatabase"
)
mycursor = db.cursor()


