# Retrieve Multiple Row With WHERE Clause Dictionary User Input
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
sql='SELECT * FROM student WHERE fees=%(fe)s'
myc=conn.cursor()
n=int(input('Enter Fees:'))
disp_value={'fe':n}
try:
    myc.execute(sql,disp_value)
    row=myc.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()
    print('Total Rows:',myc.rowcount)
except:
    conn.rollback()
    print('Unable To Retrieve Data')
myc.close()
conn.close()