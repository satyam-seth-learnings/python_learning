# Update Row - Dictionary User Input
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
sql='UPDATE student SET name=%(n)s,roll=%(r)s,fees=%(f)s WHERE stuid=%(i)s'
myc=conn.cursor()
id=int(input('Enter Student ID To Update:'))
nm=input('Enter Name:')
ro=int(input('Enter Roll:'))
fe=float(input('Enter Fees:'))
update_value={'i':id,'n':nm,'r':ro,'f':fe}
try:
    myc.execute(sql,update_value)
    conn.commit()
    print(myc.rowcount,'Row Updated')
except:
    conn.rollback()
    print('Unable To Update Data')
myc.close()
conn.close()