import sqlite3
conn=sqlite3.connect("sqlite.db")
ins='''
        insert into student('st_name','st_class','st_email') VALUES ("Bishwajit","11th","bishwajit@gmail.com")
    '''
conn.execute(ins)
conn.commit()
conn.close()