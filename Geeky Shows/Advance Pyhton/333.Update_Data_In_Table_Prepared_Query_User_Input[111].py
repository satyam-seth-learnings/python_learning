# Update Row User Input
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
sql='UPDATE student SET roll=%s,fees=%s WHERE stuid=%s' #Or sql='UPDATE student SET roll=?,fees=? WHERE stuid=?'
myc=conn.cursor(prepared=True)
id=int(input('Enter Student ID To Update:'))
ro=int(input('Enter Roll:'))
fe=float(input('Enter Fees:'))
update_value=(fe,ro,id)
try:
    myc.execute(sql,update_value)
    conn.commit()
    print('Row Updated')
except:
    conn.rollback()
    print('Unable To Update Data')
myc.close()
conn.close()