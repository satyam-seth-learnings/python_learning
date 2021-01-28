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
sql='DELETE FROM student WHERE stuid=%s'    #Or sql='DELETE FROM student WHERE stuid=?'
myc=conn.cursor(prepared=True)
del_value=(12,)
try:
    myc.execute(sql,del_value)
    conn.commit()   # Commiting The Changes
    print('Row Deleted')
except:
    conn.rollback() # Rollback The Changes
    print('Unable To Delete Data')
myc.close() # Close Cursor
conn.close()    # Close Connection