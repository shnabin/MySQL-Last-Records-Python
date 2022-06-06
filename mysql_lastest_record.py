import logging
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="classicmodels")
mycursor = mydb.cursor(buffered=True , dictionary=True)

sql = "SELECT * FROM information_schema.tables where table_schema = 'classicmodels'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
tables = [d['TABLE_NAME'] for d in myresult]

for x in tables:
    sql1 = "select * from {}".format(x)
    mycursor.execute(sql1)
    myresult1 = mycursor.fetchone()
    for col, val in myresult1.items():
        print(f'{col} is {val}')
