# Update Row
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
sql='UPDATE student SET fees=%s WHERE stuid=%s' #Or sql='UPDATE student SET fees=? WHERE stuid=?'
myc=conn.cursor(prepared=True)
update_value=(2547,9)
try:
    myc.execute(sql,update_value)
    conn.commit()
    print('Row Updated')
except:
    conn.rollback()
    print('Unable To Update Data')
myc.close()
conn.close()