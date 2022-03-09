#delete record table : data id=101

import sqlite3

con = sqlite3.connect("mydb.db") #connect to database mydb or create mydb

sql = 'DELETE FROM data WHERE id=101'
con.execute(sql)
con.commit()#commit for delete

print('Delete Table data : id=101 OK')

con.close() #close connect database mydb
