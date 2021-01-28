# Retrieve Multiple Row With WHERE Clause
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
disp_value=(5000,)
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