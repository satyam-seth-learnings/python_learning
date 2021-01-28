# Update Row - Tuple
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
sql='UPDATE student SET fees=%s WHERE stuid=%s'
myc=conn.cursor()
update_value=(5000,4)
try:
    myc.execute(sql,update_value)
    conn.commit()
    print(myc.rowcount,'Row Updated')
except:
    conn.rollback()
    print('Unable To Update Data')
myc.close()
conn.close()