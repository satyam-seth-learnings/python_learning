# Creating Database
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='Seth7706',
        host='localhost',
        port=3306
    )
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable To Connect')
sql='CREATE DATABASE pdb'
myc=conn.cursor()
myc.execute(sql)
conn.close()