# Retrieve Single Row With WHERE Clause
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
sql='SELECT * FROM student WHERE stuid=%s' #Or sql='SELECT * FROM student WHERE stuid=?'
myc=conn.cursor(prepared=True)
n=int(input('Enter Student ID To Display:'))
disp_value=(n,)
try:
    myc.execute(sql,disp_value)
    row=myc.fetchone()
    print(row)
except:
    conn.rollback()
    print('Unable To Retrieve Data')
myc.close()
conn.close()