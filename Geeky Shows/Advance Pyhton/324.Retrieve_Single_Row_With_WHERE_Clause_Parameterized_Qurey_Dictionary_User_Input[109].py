# Retrieve Single Row With WHERE Clause Dictionary User Input
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
sql='SELECT * FROM student WHERE stuid=%(id)s'
myc=conn.cursor()
n=int(input('Enter Student ID To Display:'))
disp_value={'id':n}
try:
    myc.execute(sql,disp_value)
    row=myc.fetchone()
    print(row)
    print('Total Rows:',myc.rowcount)
except:
    conn.rollback()
    print('Unable To Retrieve Data')
myc.close()
conn.close()