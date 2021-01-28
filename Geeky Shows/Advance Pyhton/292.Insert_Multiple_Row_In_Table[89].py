# Insert Multiple Rows
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
sql='INSERT INTO student(name,roll,fees) VALUES("Jai",102,45843.5),("Veeru",103,45201.7),("Basanti",104,48451.80)'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print('Rows Inserted')
except:
    conn.rollback()
    print('Unable To Insert Data')
myc.close()
conn.close()