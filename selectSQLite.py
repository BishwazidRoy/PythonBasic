import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT *FROM student")

print("ID","NAME  ","CLASS  ","EMAIL")

#for n in data:
 #   print(n)

for n in data:
    print(n[0],n[1],n[2],n[3])