# Show Table
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
sql='SHOW TABLES'
myc=conn.cursor()
myc.execute(sql)
for i in myc:
    print(i)
myc.close()
conn.close()