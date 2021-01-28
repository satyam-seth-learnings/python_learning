# Insert Single Row
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
sql='INSERT INTO student(name,roll,fees) VALUES("Sumit",101,50600.52)'
myc=conn.cursor()
myc.execute(sql)
conn.commit()
myc.close()
conn.close()