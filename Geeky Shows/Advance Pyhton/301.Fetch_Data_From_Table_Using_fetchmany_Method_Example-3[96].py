# Retrive n Number Of Rows
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
myc=conn.cursor(buffered=True)
try:
    myc.execute(sql)
    rows=myc.fetchmany(size=5)
    for row in rows:
        print(row)
    print('Total Rows:',myc.rowcount)
except:
    conn.rollback()
    print('Unable To Show Data')
myc.close()
conn.close()