import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="abc",port=3306)
cur=myobj.cursor()
try:
	db="CREATE DATABASE school"
	cur.execute(db)
	print("database created")

except:
	print("database errer..")