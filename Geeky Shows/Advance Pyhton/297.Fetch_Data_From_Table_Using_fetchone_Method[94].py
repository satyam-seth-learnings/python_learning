# Retrive Row One By One
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
sql='SELECT * FROM student'  #Or sql='SELECT name FROM student' #Or sql='SELECT name,roll FROM student'
myc=conn.cursor()
try:
    myc.execute(sql)
    row=myc.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()
    print('Total Rows:',myc.rowcount)
except:
    conn.rollback()
    print('Unable To Show Data')
myc.close()
conn.close()