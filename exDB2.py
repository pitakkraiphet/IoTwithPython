#insert data to table : data (id,rate)

import sqlite3

con = sqlite3.connect("mydb.db") #connect to database mydb or create mydb

sql = 'INSERT INTO data(id,rate) VALUES(104,1000)'
con.execute(sql)
con.commit()

sql = 'INSERT INTO data(id,rate) VALUES(105,2000)'
con.execute(sql)
con.commit()

sql = 'INSERT INTO data(id,rate) VALUES(106,3000)'
con.execute(sql)
con.commit()

print('Insert data OK')

con.close() #close connect database mydb