# Retrive Single Row With WHERE Clause
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='Seth7706',
        host='localhost',
        database='pdb',
        port=3306
    )
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable To Connect')
sql='SELECT * FROM student WHERE stuid=4'
myc=conn.cursor()
try:
    myc.execute(sql)
    row=myc.fetchone()
    print(row)
    print('Total Rows:',myc.rowcount)
except:
    conn.rollback()
    print('Unable To Show Data')
myc.close()
conn.close()