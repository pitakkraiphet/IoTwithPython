#update record table : data where id=102 set rate=999

import sqlite3

con = sqlite3.connect("mydb.db") #connect to database mydb or create mydb

sql = 'UPDATE data SET rate=999 WHERE id=102'
con.execute(sql)
con.commit()#commit for delete

print('Update Table data : id=102 (rate=999) OK')

con.close() #close connect database mydb

