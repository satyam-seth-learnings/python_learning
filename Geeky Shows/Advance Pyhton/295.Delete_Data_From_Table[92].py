# Delete Row
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
sql='DELETE FROM student WHERE stuid=11'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'Row Deleted')
except:
    conn.rollback()
    print('Unable To Delete Data')
myc.close()
conn.close()