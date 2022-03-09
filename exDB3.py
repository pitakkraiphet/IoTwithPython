#show data from table : data (id,rate)

import sqlite3

con = sqlite3.connect("mydb.db") #connect to database mydb or create mydb

sql = 'select * from data'
result = con.execute(sql) #read database table to memory
#print(result)
for cols in result:
    print(cols)
    print(cols[0])
    print(cols[1])
    print('-------')

del result #delete result in memory
con.close() #close connect database mydb