# Retrieve Multiple Row With WHERE Clause User Input
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
sql='SELECT * FROM student WHERE fees=%s'   #Or sql='SELECT * FROM student WHERE fees=?'
myc=conn.cursor(prepared=True)
fe=float(input('Enter Student Fees To Display:'))
disp_value=(fe,)
try:
    myc.execute(sql,disp_value)
    row=myc.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()
except:
    conn.rollback()
    print('Unable To Retrieve Data')
myc.close()
conn.close()