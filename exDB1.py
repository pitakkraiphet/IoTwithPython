#create database : mydb / table : data (id,rate)

import sqlite3

con = sqlite3.connect("mydb.db") #connect to database mydb or create mydb

sql = 'CREATE TABLE data(id INT PRIMARY KEY NOT NULL,rate INT NOT NULL)'
con.execute(sql)
print('Create Table data OK')

con.close() #close connect database mydb